# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False
# cython: initializedcheck=False
# cython: nonecheck=False
# cython: cdivision=True

import cython
import numpy as np
cimport numpy as cnp
from cython cimport view
import math
from libc.math cimport round, ceil

ctypedef cnp.uint32_t uint32
ctypedef cnp.int32_t int32
ctypedef cnp.float32_t float64
ctypedef cnp.int64_t int64
ctypedef cnp.uint8_t uint8
ctypedef (float64, float64, float64, float64) vec4
ctypedef (float64, float64, float64, float64, float64) vs_out

cdef float64 clip_xmin(
    float64[4] c, 
    vec4 a, 
    vec4 b
) nogil:
    cdef float64 t, dx, dy, dz, dw, den
    dx = (b[0] - a[0])
    dy = (b[1] - a[1])
    dz = (b[2] - a[2])
    dw = (b[3] - a[3])
    den = dx + dw
    if den == 0:
        t=0
    else:
        t = ( - a[0] - a[3]) / den
    c[1] = a[1] + t * dy
    c[2] = a[2] + t * dz
    c[3] = a[3] + t * dw
    c[0] = - c[3]
    return t


cdef float64 clip_xmax(
    float64[4] c, 
    vec4 a, 
    vec4 b
) nogil:
    cdef float64 t, dx, dy, dz, dw, den
    dx = (b[0] - a[0])
    dy = (b[1] - a[1])
    dz = (b[2] - a[2])
    dw = (b[3] - a[3])
    den = -dx + dw
    if den == 0:
        t=0
    else:
        t = ( + a[0] - a[3]) / den
    c[1] = a[1] + t * dy
    c[2] = a[2] + t * dz
    c[3] = a[3] + t * dw
    c[0] = + c[3]
    return t


cdef float64 clip_ymin(
    float64[4] c, 
    vec4 a,
    vec4 b
) nogil:
    cdef float64 t, dx, dy, dz, dw, den
    dx = (b[0] - a[0])
    dy = (b[1] - a[1])
    dz = (b[2] - a[2])
    dw = (b[3] - a[3])
    den = dy + dw
    if den == 0:
        t=0
    else:
        t = ( - a[1] - a[3]) / den
    c[0] = a[0] + t * dx
    c[2] = a[2] + t * dz
    c[3] = a[3] + t * dw
    c[1] = - c[3]
    return t


cdef float64 clip_ymax(
    float64[4] c, 
    vec4 a, 
    vec4 b
) nogil:
    cdef float64 t, dx, dy, dz, dw, den
    dx = (b[0] - a[0])
    dy = (b[1] - a[1])
    dz = (b[2] - a[2])
    dw = (b[3] - a[3])
    den = -dy + dw
    if den == 0:
        t=0
    else:
        t = ( + a[1] - a[3]) / den
    c[0] = a[0] + t * dx
    c[2] = a[2] + t * dz
    c[3] = a[3] + t * dw
    c[1] = + c[3]
    return t


cdef float64 clip_zmin(
    float64[4] c, 
    vec4 a, 
    vec4 b
) nogil:
    cdef float64 t, dx, dy, dz, dw, den
    dx = (b[0] - a[0])
    dy = (b[1] - a[1])
    dz = (b[2] - a[2])
    dw = (b[3] - a[3])
    den = dz + dw
    if den == 0:
        t=0
    else:
        t = ( - a[2] - a[3]) / den
    c[0] = a[0] + t * dx
    c[1] = a[1] + t * dy
    c[3] = a[3] + t * dw
    c[2] = - c[3]
    return t


cdef float64 clip_zmax(
    float64[4] c, 
    vec4 a, 
    vec4 b
) nogil:
    cdef float64 t, dx, dy, dz, dw, den
    dx = (b[0] - a[0])
    dy = (b[1] - a[1])
    dz = (b[2] - a[2])
    dw = (b[3] - a[3])
    den = -dz + dw
    if den == 0:
        t = 0
    else:
        t = ( + a[2] - a[3]) / den
    c[0] = a[0] + t * dx
    c[1] = a[1] + t * dy
    c[3] = a[3] + t * dw
    c[2] = + c[3]
    return t


cdef float64 clip_proc(
    float64[4] c, 
    vec4 a, 
    vec4 b, 
    const int clip_bit
) nogil:
    if clip_bit == 0:
        return clip_zmin(c, a, b)
    elif clip_bit == 1:
        return clip_zmax(c, a, b)
    elif clip_bit == 2:
        return clip_xmin(c, a, b)
    elif clip_bit == 3:
        return clip_xmax(c, a, b)
    elif clip_bit == 4:
        return clip_ymin(c, a, b)
    elif clip_bit == 5:
        return clip_ymax(c, a, b)


cdef inline int gl_clipcode(vec4 pt) nogil:
    cdef float64 w = pt[3] * (1.0 + 1E-5)
    return (((pt[2] < -w) | ((pt[2] >  w) << 1)) & 3) | ((pt[0] < -w) << 2) | ((pt[0] >  w) << 3) | ((pt[1] < -w) << 4) | ((pt[1] >  w) << 5)


cdef void draw_triangle(
    vec4 v0, vs_out v0_vs_out, 
    vec4 v1, vs_out v1_vs_out, 
    vec4 v2, vs_out v2_vs_out, 
    uint32[:] screen, int w, int h, 
    float64[:] zbuffer, const uint8[:, :, :] texture
):
    cdef int v0_clip_code = gl_clipcode(v0), v1_clip_code = gl_clipcode(v1), v2_clip_code = gl_clipcode(v2)
    cdef int c_or, c_and = v0_clip_code & v1_clip_code & v2_clip_code
    
    # have to set here because we can re use vertices
    # for multiple triangles in STRIP and FAN
    cdef int v0_edge_flag = 1, v1_edge_flag = 1, v2_edge_flag = 1
    
    if c_and != 0:
        return

    c_or = v0_clip_code | v1_clip_code | v2_clip_code
    if c_or == 0:
        draw_triangle_final(
            v0, v0_vs_out, 
            v1, v1_vs_out,
            v2, v2_vs_out,
            screen, w, h, zbuffer, texture
        )
    else:
        draw_triangle_clip(v0, v0_clip_code, v0_edge_flag, v0_vs_out,
                           v1, v1_clip_code, v1_edge_flag, v1_vs_out,
                           v2, v2_clip_code, v2_edge_flag, v2_vs_out,
                           0, screen, w, h, zbuffer, texture)

cdef inline (float64, float64, float64) vec4_to_vec3h(
    (float64, float64, float64, float64) a
) nogil:
    return (a[0] / a[3], a[1] / a[3], a[2] / a[3])
    

cdef inline vec4 mult_vp_vec4(
    int w, int h, vec4 v
) nogil:
    cdef float64 r = (w - 0.01) / 2, t = (h - 0.01) / 2
    return (r*v[0] + r*v[3], t*v[1] + t*v[3], v[2], v[3])


cdef inline (float64, float64, float64) make_Line(
    float64 x1, float64 y1, float64 x2, float64 y2
) nogil:
    return (y1 - y2, x2 - x1, x1*y2 - x2*y1)


cdef inline float64 line_func(
    (float64, float64, float64) line, float64 x, float64 y
) nogil:
    return line[0]*x + line[1]*y + line[2]


cdef void draw_triangle_final(
    vec4 _v0, vs_out v0_vs_out, 
    vec4 _v1, vs_out v1_vs_out, 
    vec4 _v2, vs_out v2_vs_out, 
    uint32[:] screen, int w, int h, 
    float64[:] zbuffer, const uint8[:, :, :] texture
):
    cdef int ix, iy
    cdef vec4 p0 = mult_vp_vec4(w, h, _v0)
    cdef vec4 p1 = mult_vp_vec4(w, h, _v1)
    cdef vec4 p2 = mult_vp_vec4(w, h, _v2)

    cdef (float64, float64, float64) hp0 = vec4_to_vec3h(p0)
    cdef (float64, float64, float64) hp1 = vec4_to_vec3h(p1)
    cdef (float64, float64, float64) hp2 = vec4_to_vec3h(p2)
    
    if hp0[0]*hp1[1] - hp1[0]*hp0[1] + hp1[0]*hp2[1] - hp2[0]*hp1[1] + hp2[0]*hp0[1] - hp0[0]*hp2[1] <= 0:
        return

    if hp0[1] > hp1[1]:
        p0, p1 = p1, p0
        hp0, hp1 = hp1, hp0
        v0_vs_out, v1_vs_out = v1_vs_out, v0_vs_out
    if hp0[1] > hp2[1]:
        p0, p2 = p2, p0
        hp0, hp2 = hp2, hp0
        v0_vs_out, v2_vs_out = v2_vs_out, v0_vs_out
    if hp1[1] > hp2[1]:
        p2, p1 = p1, p2
        hp2, hp1 = hp1, hp2
        v2_vs_out, v1_vs_out = v1_vs_out, v2_vs_out

    cdef float64 x_min = min(min(hp0[0], hp1[0]), hp2[0])
    cdef float64 x_max = max(max(hp0[0], hp1[0]), hp2[0])
    cdef float64 y_min = min(min(hp0[1], hp1[1]), hp2[1])
    cdef float64 y_max = max(max(hp0[1], hp1[1]), hp2[1])

    cdef int ix_min = <int>max(0, x_min)
    cdef int ix_max = <int>round(min(w, x_max))
    cdef int iy_min = <int>max(0, y_min)
    cdef int iy_max = <int>round(min(h, y_max))
    
    cdef float64 inv_w0 = 1 / p0[3], inv_w1 = 1 / p1[3], inv_w2 = 1 / p2[3]

    cdef (float64, float64, float64) l01 = make_Line(hp0[0], hp0[1], hp1[0], hp1[1])
    cdef (float64, float64, float64) l12 = make_Line(hp1[0], hp1[1], hp2[0], hp2[1])
    cdef (float64, float64, float64) l20 = make_Line(hp2[0], hp2[1], hp0[0], hp0[1])

    cdef float64 alpha, beta, gamma, tmp2, z, x, y, _u, _v, light_r, light_g, light_b
    cdef int u, v, y_index, new_ix_min, min_add

    cdef vs_out perspective0 = (v0_vs_out[0] * inv_w0 * 16, v0_vs_out[1] * inv_w0 * 16, v0_vs_out[2] * inv_w0, v0_vs_out[3] * inv_w0, v0_vs_out[4] * inv_w0)
    cdef vs_out perspective1 = (v1_vs_out[0] * inv_w1 * 16, v1_vs_out[1] * inv_w1 * 16, v1_vs_out[2] * inv_w1, v1_vs_out[3] * inv_w1, v1_vs_out[4] * inv_w1)
    cdef vs_out perspective2 = (v2_vs_out[0] * inv_w2 * 16, v2_vs_out[1] * inv_w2 * 16, v2_vs_out[2] * inv_w2, v2_vs_out[3] * inv_w2, v2_vs_out[4] * inv_w2)

    cdef bint alpha_clip = (line_func(l12, hp0[0], hp0[1]) * line_func(l12, -1, -2.5) > 0)
    cdef bint beta_clip = (line_func(l20, hp1[0], hp1[1]) * line_func(l20, -1, -2.5) > 0)
    cdef bint gamma_clip = (line_func(l01, hp2[0], hp2[1]) * line_func(l01, -1, -2.5) > 0)

    cdef float64 gamma_div = 1 / line_func(l01, hp2[0], hp2[1])
    cdef float64 beta_div = 1 / line_func(l20, hp1[0], hp1[1])
    
    cdef (float64, float64, float64) l01_gamma = (l01[0] * gamma_div, l01[1] * gamma_div, l01[2] * gamma_div)
    cdef (float64, float64, float64) l20_beta = (l20[0] * beta_div, l20[1] * beta_div, l20[2] * beta_div)

    # Precompute starting barycentric coordinates for the first pixel
    cdef float64 start_x = ix_min + 0.5
    cdef float64 start_y = iy_min + 0.5
    
    cdef float64 gamma0 = l01_gamma[0] * start_x + l01_gamma[1] * start_y + l01_gamma[2]
    cdef float64 gamma0_add = l01_gamma[1], gamma_add = l01_gamma[0]
    
    cdef float64 beta0 = l20_beta[0] * start_x + l20_beta[1] * start_y + l20_beta[2]
    cdef float64 beta0_add = l20_beta[1], beta_add = l20_beta[0]
    
    cdef float64 alpha0 = 1.0 - beta0 - gamma0
    cdef float64 alpha0_add = -(l01_gamma[1] + l20_beta[1]), alpha_add = -(l01_gamma[0] + l20_beta[0])
    
    cdef float64 tmp2_0 = alpha0 * inv_w0 + beta0 * inv_w1 + gamma0 * inv_w2
    cdef float64 tmp2_0_add = alpha0_add * inv_w0 + beta0_add * inv_w1 + gamma0_add * inv_w2
    cdef float64 tmp2_add = alpha_add * inv_w0 + beta_add * inv_w1 + gamma_add * inv_w2
    
    cdef float64 z0 = alpha0 * hp0[2] + beta0 * hp1[2] + gamma0 * hp2[2]
    cdef float64 z0_add = alpha0_add * hp0[2] + beta0_add * hp1[2] + gamma0_add * hp2[2]
    cdef float64 z_add = alpha_add * hp0[2] + beta_add * hp1[2] + gamma_add * hp2[2]
    
    cdef float64 v0 = alpha0 * perspective0[0] + beta0 * perspective1[0] + gamma0 * perspective2[0]
    cdef float64 v0_add = alpha0_add * perspective0[0] + beta0_add * perspective1[0] + gamma0_add * perspective2[0]
    cdef float64 v_add = alpha_add * perspective0[0] + beta_add * perspective1[0] + gamma_add * perspective2[0]
    
    cdef float64 u0 = alpha0 * perspective0[1] + beta0 * perspective1[1] + gamma0 * perspective2[1]
    cdef float64 u0_add = alpha0_add * perspective0[1] + beta0_add * perspective1[1] + gamma0_add * perspective2[1]
    cdef float64 u_add = alpha_add * perspective0[1] + beta_add * perspective1[1] + gamma_add * perspective2[1]
    
    cdef float64 light_r0 = alpha0 * perspective0[2] + beta0 * perspective1[2] + gamma0 * perspective2[2]
    cdef float64 light_r0_add = alpha0_add * perspective0[2] + beta0_add * perspective1[2] + gamma0_add * perspective2[2]
    cdef float64 light_r_add = alpha_add * perspective0[2] + beta_add * perspective1[2] + gamma_add * perspective2[2]
    
    cdef float64 light_g0 = alpha0 * perspective0[3] + beta0 * perspective1[3] + gamma0 * perspective2[3]
    cdef float64 light_g0_add = alpha0_add * perspective0[3] + beta0_add * perspective1[3] + gamma0_add * perspective2[3]
    cdef float64 light_g_add = alpha_add * perspective0[3] + beta_add * perspective1[3] + gamma_add * perspective2[3]
    
    cdef float64 light_b0 = alpha0 * perspective0[4] + beta0 * perspective1[4] + gamma0 * perspective2[4]
    cdef float64 light_b0_add = alpha0_add * perspective0[4] + beta0_add * perspective1[4] + gamma0_add * perspective2[4]
    cdef float64 light_b_add = alpha_add * perspective0[4] + beta_add * perspective1[4] + gamma_add * perspective2[4]
   
    cdef (float64, float64) lt_line, lb_line
    
    cdef bint flag = 1
    
    y_index = iy_min * -w + (h - 1) * w
    
    if l01[0] == 0:  # 平顶
        flag = 0
        lt_line = (l20[1]/l20[0], l20[2]/l20[0]) if hp0[0] < hp1[0] else (l12[1]/l12[0], l12[2]/l12[0])
    elif l12[0] == 0:  # 平底
        flag = 0
        lt_line = (l01[1]/l01[0], l01[2]/l01[0]) if hp1[0] < hp2[0] else (l20[1]/l20[0], l20[2]/l20[0])
    else:  # 一般三角形
        if (hp2[0] - hp0[0]) * (hp1[1] - hp0[1]) - (hp2[1] - hp0[1]) * (hp1[0] - hp0[0]) < 0:  # 左边为主
            flag = 0
            lt_line = (l20[1]/l20[0], l20[2]/l20[0])
        elif hp1[1] <= iy_min + 0.5:
            flag = 0
            lt_line = (l12[1]/l12[0], l12[2]/l12[0])
        elif hp1[1] >= iy_max - 0.5:
            flag = 0
            lt_line = (l01[1]/l01[0], l01[2]/l01[0])
        else:
            flag = 1
            lt_line = (l01[1]/l01[0], l01[2]/l01[0])
            lb_line = (l12[1]/l12[0], l12[2]/l12[0])
    
    # cdef (float64, float64) l01_y = (min(hp0[1], hp1[1]), max(hp0[1], hp1[1]))
    # cdef (float64, float64) l12_y = (min(hp1[1], hp2[1]), max(hp1[1], hp2[1]))
    # cdef (float64, float64) l20_y = (min(hp2[1], hp0[1]), max(hp2[1], hp0[1]))
    # cdef (float64, float64) l01_n = (l01[1]/l01[0], l01[2]/l01[0])
    # cdef (float64, float64) l12_n = (l12[1]/l12[0], l12[2]/l12[0])
    # cdef (float64, float64) l20_n = (l20[1]/l20[0], l20[2]/l20[0])
    # cdef int new_ix_min_tmp
    
    if flag == 0:
        for iy in range(iy_min, iy_max):
            gamma = gamma0
            beta = beta0
            alpha = alpha0
            tmp2 = tmp2_0
            z = z0
            _u = u0
            _v = v0
            light_r = light_r0
            light_g = light_g0
            light_b = light_b0
            
            new_ix_min = -<int>(lt_line[0]*(iy + 0.5) + lt_line[1])
            
            if ix_min < new_ix_min < ix_max:
                min_add = new_ix_min - ix_min
                gamma += min_add * gamma_add
                beta += min_add * beta_add
                alpha += min_add * alpha_add
                tmp2 += min_add * tmp2_add
                z += min_add * z_add
                _u += min_add * u_add
                _v += min_add * v_add
                light_r += min_add * light_r_add
                light_g += min_add * light_g_add 
                light_b += min_add * light_b_add
            else:
                new_ix_min = ix_min
            for ix in range(new_ix_min, ix_max):
                if alpha >= 0 and beta >= 0 and gamma >= 0 and (alpha > 0 or alpha_clip) and (beta > 0 or beta_clip) and (gamma > 0 or gamma_clip) and z < 0.995 and z < zbuffer[ix + y_index]:
                    v = <int>(_v / tmp2)
                    u = <int>(_u / tmp2)
                    if texture[u, v, 3]:
                        zbuffer[ix + y_index] = z
                        screen[ix + y_index] = (
                            (min(<int>(texture[u, v, 0] * light_r / tmp2), 255) << 16) |
                            (min(<int>(texture[u, v, 1] * light_g / tmp2), 255) << 8) |
                             min(<int>(texture[u, v, 2] * light_b / tmp2), 255)
                        )
                # Increment barycentric coordinates horizontally
                gamma += gamma_add
                beta += beta_add
                alpha += alpha_add
                tmp2 += tmp2_add
                z += z_add
                _u += u_add
                _v += v_add
                light_r += light_r_add
                light_g += light_g_add
                light_b += light_b_add
    
            # Increment barycentric coordinates vertically
            gamma0 += gamma0_add
            beta0 += beta0_add
            alpha0 += alpha0_add
            tmp2_0 += tmp2_0_add
            z0 += z0_add
            u0 += u0_add
            v0 += v0_add
            light_r0 += light_r0_add
            light_g0 += light_g0_add
            light_b0 += light_b0_add
            y_index += -w
        return
    
    cdef int iy_sep = <int>ceil(hp1[1] - 0.5)
    for iy in range(iy_min, iy_sep):
        gamma = gamma0
        beta = beta0
        alpha = alpha0
        tmp2 = tmp2_0
        z = z0
        _u = u0
        _v = v0
        light_r = light_r0
        light_g = light_g0
        light_b = light_b0

        new_ix_min = -<int>(lt_line[0]*(iy + 0.5) + lt_line[1])
        if ix_min < new_ix_min < ix_max:
            min_add = new_ix_min - ix_min
            gamma += min_add * gamma_add
            beta += min_add * beta_add
            alpha += min_add * alpha_add
            tmp2 += min_add * tmp2_add
            z += min_add * z_add
            _u += min_add * u_add
            _v += min_add * v_add
            light_r += min_add * light_r_add
            light_g += min_add * light_g_add
            light_b += min_add * light_b_add
        else:
            new_ix_min = ix_min
        for ix in range(new_ix_min, ix_max):
            if alpha >= 0 and beta >= 0 and gamma >= 0 and (alpha > 0 or alpha_clip) and (beta > 0 or beta_clip) and (gamma > 0 or gamma_clip) and z < 0.995 and z < zbuffer[ix + y_index]:
                v = <int>(_v / tmp2)
                u = <int>(_u / tmp2)
                if texture[u, v, 3]:
                    zbuffer[ix + y_index] = z
                    screen[ix + y_index] = (
                        (min(<int>(texture[u, v, 0] * light_r / tmp2), 255) << 16) |
                        (min(<int>(texture[u, v, 1] * light_g / tmp2), 255) << 8) |
                         min(<int>(texture[u, v, 2] * light_b / tmp2), 255)
                    )

            # Increment barycentric coordinates horizontally
            gamma += gamma_add
            beta += beta_add
            alpha += alpha_add
            tmp2 += tmp2_add
            z += z_add
            _u += u_add
            _v += v_add
            light_r += light_r_add
            light_g += light_g_add
            light_b += light_b_add

        # Increment barycentric coordinates vertically
        gamma0 += gamma0_add
        beta0 += beta0_add
        alpha0 += alpha0_add
        tmp2_0 += tmp2_0_add
        z0 += z0_add
        u0 += u0_add
        v0 += v0_add
        light_r0 += light_r0_add
        light_g0 += light_g0_add
        light_b0 += light_b0_add
        y_index += -w
    for iy in range(iy_sep, iy_max):
        gamma = gamma0
        beta = beta0
        alpha = alpha0
        tmp2 = tmp2_0
        z = z0
        _u = u0
        _v = v0
        light_r = light_r0
        light_g = light_g0
        light_b = light_b0

        new_ix_min = -<int>(lb_line[0]*(iy + 0.5) + lb_line[1])
        if ix_min < new_ix_min < ix_max:
            min_add = new_ix_min - ix_min
            gamma += min_add * gamma_add
            beta += min_add * beta_add
            alpha += min_add * alpha_add
            tmp2 += min_add * tmp2_add
            z += min_add * z_add
            _u += min_add * u_add
            _v += min_add * v_add
            light_r += min_add * light_r_add
            light_g += min_add * light_g_add
            light_b += min_add * light_b_add
        else:
            new_ix_min = ix_min
        for ix in range(new_ix_min, ix_max):
            if alpha >= 0 and beta >= 0 and gamma >= 0 and (alpha > 0 or alpha_clip) and (beta > 0 or beta_clip) and (gamma > 0 or gamma_clip) and z < 0.995 and z < zbuffer[ix + y_index]:
                v = <int>(_v / tmp2)
                u = <int>(_u / tmp2)
                if texture[u, v, 3]:
                    zbuffer[ix + y_index] = z
                    screen[ix + y_index] = (
                        (min(<int>(texture[u, v, 0] * light_r / tmp2), 255) << 16) |
                        (min(<int>(texture[u, v, 1] * light_g / tmp2), 255) << 8) |
                         min(<int>(texture[u, v, 2] * light_b / tmp2), 255)
                    )

            # Increment barycentric coordinates horizontally
            gamma += gamma_add
            beta += beta_add
            alpha += alpha_add
            tmp2 += tmp2_add
            z += z_add
            _u += u_add
            _v += v_add
            light_r += light_r_add
            light_g += light_g_add
            light_b += light_b_add

        # Increment barycentric coordinates vertically
        gamma0 += gamma0_add
        beta0 += beta0_add
        alpha0 += alpha0_add
        tmp2_0 += tmp2_0_add
        z0 += z0_add
        u0 += u0_add
        v0 += v0_add
        light_r0 += light_r0_add
        light_g0 += light_g0_add
        light_b0 += light_b0_add
        y_index += -w


cdef inline vs_out update_clip_pt(
    vs_out v0_vs_out, 
    vs_out v1_vs_out, 
    float64 t
) nogil:
    return (
        v0_vs_out[0] + (v1_vs_out[0] - v0_vs_out[0]) * t,
        v0_vs_out[1] + (v1_vs_out[1] - v0_vs_out[1]) * t,
        v0_vs_out[2] + (v1_vs_out[2] - v0_vs_out[2]) * t,
        v0_vs_out[3] + (v1_vs_out[3] - v0_vs_out[3]) * t,
        v0_vs_out[4] + (v1_vs_out[4] - v0_vs_out[4]) * t
    ) 


cdef void draw_triangle_clip(
    vec4 v0, int v0_clip_code, int v0_edge_flag, vs_out v0_vs_out,
    vec4 v1, int v1_clip_code, int v1_edge_flag, vs_out v1_vs_out,
    vec4 v2, int v2_clip_code, int v2_edge_flag, vs_out v2_vs_out,
    int clip_bit, uint32[:] screen, int w, int h, 
    float64[:] zbuffer, const uint8[:, :, :] texture
):
    cdef int c_or, c_and, c_ex_or, edge_flag_tmp, clip_mask
    cdef float64 tt
    
    cdef vec4   tmp1,           tmp2
    cdef int    tmp1_clip_code, tmp2_clip_code
    cdef int    tmp1_edge_flag, tmp2_edge_flag
    cdef vs_out tmp1_vs_out,    tmp2_vs_out
    
    cdef vec4   q0,           q1,           q2
    cdef int    q0_clip_code, q1_clip_code, q2_clip_code
    cdef int    q0_edge_flag, q1_edge_flag, q2_edge_flag
    cdef vs_out q0_vs_out,    q1_vs_out,    q2_vs_out
    
    cdef float64[4] carr

    c_or = v0_clip_code | v1_clip_code | v2_clip_code
    
    if c_or == 0:
        draw_triangle_final(
            v0, v0_vs_out, 
            v1, v1_vs_out,
            v2, v2_vs_out, 
            screen, w, h, zbuffer, texture
        )
    else:
        c_and = v0_clip_code & v1_clip_code & v2_clip_code
        # the triangle is completely outside
        if c_and != 0:
            return

        # find the next direction to clip
        while (clip_bit < 6) and (c_or & (1 << clip_bit)) == 0:
            clip_bit += 1

        # 只有在出现舍入误差的情况下，才会出现此情况
        if clip_bit == 6:
            return

        clip_mask = 1 << clip_bit
        c_ex_or = (v0_clip_code ^ v1_clip_code ^ v2_clip_code) & clip_mask

        if c_ex_or:
            # one point outside
            if v0_clip_code & clip_mask:
                q0=v0; q0_clip_code=v0_clip_code; q0_edge_flag=v0_edge_flag; q0_vs_out=v0_vs_out
                q1=v1; q1_clip_code=v1_clip_code; q1_edge_flag=v1_edge_flag; q1_vs_out=v1_vs_out
                q2=v2; q2_clip_code=v2_clip_code; q2_edge_flag=v2_edge_flag; q2_vs_out=v2_vs_out
            elif v1_clip_code & clip_mask:
                q0=v1; q0_clip_code=v1_clip_code; q0_edge_flag=v1_edge_flag; q0_vs_out=v1_vs_out
                q1=v2; q1_clip_code=v2_clip_code; q1_edge_flag=v2_edge_flag; q1_vs_out=v2_vs_out
                q2=v0; q2_clip_code=v0_clip_code; q2_edge_flag=v0_edge_flag; q2_vs_out=v0_vs_out
            else:
                q0=v2; q0_clip_code=v2_clip_code; q0_edge_flag=v2_edge_flag; q0_vs_out=v2_vs_out
                q1=v0; q1_clip_code=v0_clip_code; q1_edge_flag=v0_edge_flag; q1_vs_out=v0_vs_out
                q2=v1; q2_clip_code=v1_clip_code; q2_edge_flag=v1_edge_flag; q2_vs_out=v1_vs_out

            tt = clip_proc(carr, q0, q1, clip_bit)
            tmp1 = (carr[0], carr[1], carr[2], carr[3])
            tmp1_clip_code = gl_clipcode(tmp1)
            tmp1_vs_out = update_clip_pt(q0_vs_out, q1_vs_out, tt)

            tt = clip_proc(carr, q0, q2, clip_bit)
            tmp2 = (carr[0], carr[1], carr[2], carr[3])
            tmp2_clip_code = gl_clipcode(tmp2)
            tmp2_vs_out = update_clip_pt(q0_vs_out, q2_vs_out, tt)

            tmp1_edge_flag = q0_edge_flag
            edge_flag_tmp  = q2_edge_flag
            q2_edge_flag = 0
            draw_triangle_clip(
                tmp1, tmp1_clip_code, tmp1_edge_flag, tmp1_vs_out,
                  q1,   q1_clip_code,   q1_edge_flag,   q1_vs_out,
                  q2,   q2_clip_code,   q2_edge_flag,   q2_vs_out,
                clip_bit+1, screen, w, h, zbuffer, texture
            )

            tmp2_edge_flag = 0
            tmp1_edge_flag = 0  # fixed from TinyGL, was 1
            q2_edge_flag = edge_flag_tmp
            draw_triangle_clip(
                tmp2, tmp2_clip_code, tmp2_edge_flag, tmp2_vs_out,
                tmp1, tmp1_clip_code, tmp1_edge_flag, tmp1_vs_out, 
                  q2,   q2_clip_code,   q2_edge_flag,   q2_vs_out, 
                clip_bit+1, screen, w, h, zbuffer, texture
            )
        else:
            # two points outside
            if (v0_clip_code & clip_mask) == 0:
                q0=v0; q0_clip_code=v0_clip_code; q0_edge_flag=v0_edge_flag; q0_vs_out=v0_vs_out
                q1=v1; q1_clip_code=v1_clip_code; q1_edge_flag=v1_edge_flag; q1_vs_out=v1_vs_out
                q2=v2; q2_clip_code=v2_clip_code; q2_edge_flag=v2_edge_flag; q2_vs_out=v2_vs_out
            elif (v1_clip_code & clip_mask) == 0:
                q0=v1; q0_clip_code=v1_clip_code; q0_edge_flag=v1_edge_flag; q0_vs_out=v1_vs_out
                q1=v2; q1_clip_code=v2_clip_code; q1_edge_flag=v2_edge_flag; q1_vs_out=v2_vs_out
                q2=v0; q2_clip_code=v0_clip_code; q2_edge_flag=v0_edge_flag; q2_vs_out=v0_vs_out
            else:
                q0=v2; q0_clip_code=v2_clip_code; q0_edge_flag=v2_edge_flag; q0_vs_out=v2_vs_out
                q1=v0; q1_clip_code=v0_clip_code; q1_edge_flag=v0_edge_flag; q1_vs_out=v0_vs_out
                q2=v1; q2_clip_code=v1_clip_code; q2_edge_flag=v1_edge_flag; q2_vs_out=v1_vs_out

            tt = clip_proc(carr, q0, q1, clip_bit)
            tmp1 = (carr[0], carr[1], carr[2], carr[3])
            tmp1_clip_code = gl_clipcode(tmp1)
            tmp1_vs_out = update_clip_pt(q0_vs_out, q1_vs_out, tt)

            tt = clip_proc(carr, q0, q2, clip_bit)
            tmp2 = (carr[0], carr[1], carr[2], carr[3])
            tmp2_clip_code = gl_clipcode(tmp2)
            tmp2_vs_out = update_clip_pt(q0_vs_out, q2_vs_out, tt)

            tmp1_edge_flag = 0  # fixed from TinyGL, was 1
            tmp2_edge_flag = q2_edge_flag
            draw_triangle_clip(
                  q0,   q0_clip_code,   q0_edge_flag,   q0_vs_out,
                tmp1, tmp1_clip_code, tmp1_edge_flag, tmp1_vs_out, 
                tmp2, tmp2_clip_code, tmp2_edge_flag, tmp2_vs_out,
                clip_bit+1, screen, w, h, zbuffer, texture
            )


def generate_faces(
    uint32[:] screen,
    int64[:] z_sorted,
    uint32[:, :] indices,
    uint32[:, :] uv_indices,
    float64[:, :] pts,
    float64[:, :] uv_triangle,
    uint32[:] uv_index,
    int width,
    int height,
    float64[:, :] v_light_r, float64[:, :] v_light_g, float64[:, :] v_light_b, 
    uint8[:, :, :, :] texture_arrays,
    float64[:] z_buffer
):
    
    cdef:
        int _i, i
        uint8[:, :, :] texture_array
        float64[:] ptsa, ptsb, ptsc
        vec4 v0, v1, v2
        vs_out v0_vs_out, v1_vs_out, v2_vs_out
    
    for _i in range(indices.shape[0]):
        i = z_sorted[_i]

        v0 = (pts[indices[i, 0], 0], pts[indices[i, 0], 1], pts[indices[i, 0], 2], pts[indices[i, 0], 3])
        v1 = (pts[indices[i, 1], 0], pts[indices[i, 1], 1], pts[indices[i, 1], 2], pts[indices[i, 1], 3])
        v2 = (pts[indices[i, 2], 0], pts[indices[i, 2], 1], pts[indices[i, 2], 2], pts[indices[i, 2], 3])
        v0_vs_out = (uv_triangle[uv_indices[i & 1, 0], 0], 0, v_light_r[i, 0], v_light_g[i, 0], v_light_b[i, 0])
        v1_vs_out = (uv_triangle[uv_indices[i & 1, 1], 0], uv_triangle[uv_indices[i & 1, 1], 1], v_light_r[i, 1], v_light_g[i, 1], v_light_b[i, 1])
        v2_vs_out = (uv_triangle[uv_indices[i & 1, 2], 0], uv_triangle[uv_indices[i & 1, 2], 1], v_light_r[i, 2], v_light_g[i, 2], v_light_b[i, 2])
        
        draw_triangle(
            v0, v0_vs_out, 
            v1, v1_vs_out, 
            v2, v2_vs_out, 
            screen, width, height,
            z_buffer, texture_arrays[uv_index[i >> 1]]
        )

