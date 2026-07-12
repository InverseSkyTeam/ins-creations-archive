import numpy as np
from numba import jit, prange


@jit('UniTuple(int32, 2)(float64,float64,float64)', nopython=True)
def get_min_max(a, b, c):
    return int(min(min(a, b), c)), int(max(max(a, b), c))


@jit('int32(int32,int32,int32)', nopython=True)
def clip(a, b, c):
    return max(b, min(a, c))


@jit('float64(float64[:],float64[:])', nopython=True, fastmath=True)
def get_intersect_ratio(prev, curv):
    return (prev[3] - 0.1) / (prev[3] - curv[3])


@jit('float64[:](float64[:],float64[:],float64)', nopython=True, fastmath=True)
def lerp_vec(start, end, alpha):
    return start + (end - start) * alpha


@jit(nopython=True, fastmath=True)
def lerp_tuple(start, end, alpha):
    return start[0] + (end[0] - start[0]) * alpha, start[1] + (end[1] - start[1]) * alpha, start[2] + (end[2] - start[2]) * alpha


@jit(nopython=True, fastmath=True, looplift=True)
def render_clip_face(screen, zbuffer, ptsa, ptsb, ptsc, uva, uvb, uvc, width, height, texture_array,
                     light_a, light_b, light_c, light_buffer, O2):
    clip_a, clip_b, clip_c = ptsa[2], ptsb[2], ptsc[2]
    pts2a = ptsa[0] / ptsa[3], ptsa[1] / ptsa[3]
    pts2b = ptsb[0] / ptsb[3], ptsb[1] / ptsb[3]
    pts2c = ptsc[0] / ptsc[3], ptsc[1] / ptsc[3]
    bc_c = (pts2c[0] - pts2a[0]) * (pts2b[1] - pts2a[1]) - (pts2b[0] - pts2a[0]) * (pts2c[1] - pts2a[1])
    if (-bc_c if O2 else abs(bc_c)) < 1e-3:
        return
    ptsa, ptsb, ptsc = 1 / ptsa[3], 1 / ptsb[3], 1 / ptsc[3]
    minx, maxx = get_min_max(pts2a[0], pts2b[0], pts2c[0])
    miny, maxy = get_min_max(pts2a[1], pts2b[1], pts2c[1])
    minx, maxx = clip(minx, 0, screen.shape[0] - 1), clip(maxx + 1, 1, screen.shape[0])
    miny, maxy = clip(miny, 0, screen.shape[1] - 1), clip(maxy + 1, 1, screen.shape[1])
    a, b, c, d = (pts2c[0] - pts2a[0]) / bc_c, (pts2b[0] - pts2a[0]) / bc_c, (pts2c[1] - pts2a[1]) / bc_c, (pts2b[1] - pts2a[1]) / bc_c
    uva = uva[0] * width * ptsa, uva[1] * height * ptsa
    uvb = uvb[0] * width * ptsb, uvb[1] * height * ptsb
    uvc = uvc[0] * width * ptsc, uvc[1] * height * ptsc
    light_a = light_a[0] * ptsa, light_a[1] * ptsa, light_a[2] * ptsa
    light_b = light_b[0] * ptsb, light_b[1] * ptsb, light_b[2] * ptsb
    light_c = light_c[0] * ptsc, light_c[1] * ptsc, light_c[2] * ptsc
    clip_a, clip_b, clip_c = clip_a * ptsa, clip_b * ptsb, clip_c * ptsc
    tmp1 = pts2a[1] - miny + 1

    for j in prange(minx, maxx):
        flag = False
        temp = pts2a[0] - float(j)
        m0, m1 = b * tmp1 - temp * d, temp * c - a * tmp1
        m2 = 1 - m1 - m0  # 重心坐标使用递推计算
        bc_clip_sum = m2 * ptsa + m1 * ptsb + m0 * ptsc
        clip_sum = m2 * clip_a + m1 * clip_b + m0 * clip_c
        u, v = uva[1] * m2 + uvb[1] * m1 + uvc[1] * m0, uva[0] * m2 + uvb[0] * m1 + uvc[0] * m0
        light_r = light_a[0] * m2 + light_b[0] * m1 + light_c[0] * m0
        light_g = light_a[1] * m2 + light_b[1] * m1 + light_c[1] * m0
        light_b1 = light_a[2] * m2 + light_b[2] * m1 + light_c[2] * m0

        addm0, addm1, addm2 = -b, a, -(a - b)
        bc_clip_add = addm2 * ptsa + addm1 * ptsb + addm0 * ptsc
        clip_add = addm2 * clip_a + addm1 * clip_b + addm0 * clip_c
        u_add, v_add = uva[1] * addm2 + uvb[1] * addm1 + uvc[1] * addm0, uva[0] * addm2 + uvb[0] * addm1 + uvc[0] * addm0
        light_r_add = light_a[0] * addm2 + light_b[0] * addm1 + light_c[0] * addm0
        light_g_add = light_a[1] * addm2 + light_b[1] * addm1 + light_c[1] * addm0
        light_b_add = light_a[2] * addm2 + light_b[2] * addm1 + light_c[2] * addm0
        for k in prange(screen.shape[1] - miny - 1, screen.shape[1] - maxy - 1, -1):
            # 必须显式转换成 double 参与底下的运算，不然结果是错的
            m0 += addm0
            m1 += addm1
            m2 += addm2
            bc_clip_sum += bc_clip_add
            clip_sum += clip_add
            u += u_add
            v += v_add
            light_r += light_r_add
            light_g += light_g_add
            light_b1 += light_b_add

            if m0 < 0 or m1 < 0 or m2 < 0:
                if flag:  # 优化：当可以确定超过的是右边界，可以直接换行
                    break
                continue
            flag = True

            frag_depth = clip_sum / bc_clip_sum
            last_depth = zbuffer[j, k]

            if frag_depth > last_depth or frag_depth > 60:
                continue
            zbuffer[j, k] = frag_depth
            u1, v1 = int(u / bc_clip_sum), int(v / bc_clip_sum)
            if u1 >= texture_array.shape[0] or v1 >= texture_array.shape[1] or u1 < 0 or v1 < 0:
                continue
            if texture_array[u1, v1] == 0x1000000:
                zbuffer[j, k] = last_depth
                continue
            screen[j, k] = texture_array[u1, v1]
            light_buffer[j, k] = light_r / bc_clip_sum, light_g / bc_clip_sum, light_b1 / bc_clip_sum


@jit(nopython=True, fastmath=True, looplift=True)
def generate_faces_flat(indices, uv_indices, pts, uv_triangle, uv_index, width, height,
                        screen, v_light_r, v_light_g, v_light_b, texture_arrays, z_buffer,
                        light_buffer, O2):
    # 使用 z-buffer 算法绘制三角形，以及 flat 着色

    length: int = indices.shape[0]  # 三角形总个数

    for i in prange(length):
        ptsa, ptsb, ptsc = pts[indices[i, 0]], pts[indices[i, 1]], pts[indices[i, 2]]
        uva = uv_triangle[uv_indices[i & 1, 0], 0], 0  # uv_triangle[uv_indices[i & 1, 0], 1]
        uvb = uv_triangle[uv_indices[i & 1, 1], 0], uv_triangle[uv_indices[i & 1, 1], 1]
        uvc = uv_triangle[uv_indices[i & 1, 2], 0], uv_triangle[uv_indices[i & 1, 2], 1]
        light_a = v_light_r[i, 0], v_light_g[i, 0], v_light_b[i, 0]
        light_b = v_light_r[i, 1], v_light_g[i, 1], v_light_b[i, 1]
        light_c = v_light_r[i, 2], v_light_g[i, 2], v_light_b[i, 2]
        texture_array = texture_arrays[uv_index[i >> 1]]
        nums = (ptsa[3] < 0.1) + (ptsb[3] < 0.1) + (ptsc[3] < 0.1)  # 指有几个点在屏幕外
        if nums:  # 透视裁剪
            if nums == 3:
                continue
            out_vert_num = 0
            out_pts = np.empty((4, 4), dtype=np.float64)
            out_uv = np.empty((4, 2), dtype=np.float64)
            out_light = np.empty((4, 3), dtype=np.float64)
            for j in range(3):
                curv_index = j
                prev_index = (j - 1 + 3) % 3
                curv = pts[indices[i, curv_index]]
                prev = pts[indices[i, prev_index]]
                is_cur_inside = curv[3] >= 0.1
                is_pre_inside = prev[3] >= 0.1
                if is_cur_inside != is_pre_inside:
                    ratio = get_intersect_ratio(prev, curv)
                    out_pts[out_vert_num] = lerp_vec(prev, curv, ratio)
                    out_uv[out_vert_num] = lerp_vec(uv_triangle[uv_indices[i & 1, prev_index]],
                                                    uv_triangle[uv_indices[i & 1, curv_index]], ratio)
                    out_light[out_vert_num] = lerp_tuple(
                        (v_light_r[i, prev_index], v_light_g[i, prev_index], v_light_b[i, prev_index]),
                        (v_light_r[i, curv_index], v_light_g[i, curv_index], v_light_b[i, curv_index]),
                        ratio
                    )
                    out_vert_num += 1
                if is_cur_inside:
                    out_pts[out_vert_num] = curv
                    out_uv[out_vert_num] = uv_triangle[uv_indices[i & 1, curv_index]]
                    out_light[out_vert_num] = v_light_r[i, curv_index], v_light_g[i, curv_index], v_light_b[i, curv_index]
                    out_vert_num += 1
            if out_vert_num == 3:
                uva = out_uv[0, 0], out_uv[0, 1]
                uvb = out_uv[1, 0], out_uv[1, 1]
                uvc = out_uv[2, 0], out_uv[2, 1]
                ptsa, ptsb, ptsc = out_pts[0], out_pts[1], out_pts[2]
                light_a = out_light[0, 0], out_light[0, 1], out_light[0, 2]
                light_b = out_light[1, 0], out_light[1, 1], out_light[1, 2]
                light_c = out_light[2, 0], out_light[2, 1], out_light[2, 2]
            elif out_vert_num == 4:
                uva = out_uv[0, 0], out_uv[0, 1]
                uvb = out_uv[1, 0], out_uv[1, 1]
                uvc = out_uv[2, 0], out_uv[2, 1]
                ptsa, ptsb, ptsc = out_pts[0], out_pts[1], out_pts[2]
                light_a = out_light[0, 0], out_light[0, 1], out_light[0, 2]
                light_b = out_light[1, 0], out_light[1, 1], out_light[1, 2]
                light_c = out_light[2, 0], out_light[2, 1], out_light[2, 2]
                render_clip_face(screen, z_buffer, ptsa, ptsb, ptsc, uva, uvb, uvc, width, height, texture_array,
                                 light_a, light_b, light_c, light_buffer, O2)
                uva = out_uv[0, 0], out_uv[0, 1]
                uvb = out_uv[2, 0], out_uv[2, 1]
                uvc = out_uv[3, 0], out_uv[3, 1]
                ptsa, ptsb, ptsc = out_pts[0], out_pts[2], out_pts[3]
                light_a = out_light[0, 0], out_light[0, 1], out_light[0, 2]
                light_b = out_light[2, 0], out_light[2, 1], out_light[2, 2]
                light_c = out_light[3, 0], out_light[3, 1], out_light[3, 2]
        clip_a, clip_b, clip_c = ptsa[2], ptsb[2], ptsc[2]
        pts2a = ptsa[0] / ptsa[3], ptsa[1] / ptsa[3]
        pts2b = ptsb[0] / ptsb[3], ptsb[1] / ptsb[3]
        pts2c = ptsc[0] / ptsc[3], ptsc[1] / ptsc[3]
        bc_c = (pts2c[0] - pts2a[0]) * (pts2b[1] - pts2a[1]) - (pts2b[0] - pts2a[0]) * (pts2c[1] - pts2a[1])
        if (-bc_c if O2 else abs(bc_c)) < 1e-3:
            continue
        ptsa, ptsb, ptsc = 1 / ptsa[3], 1 / ptsb[3], 1 / ptsc[3]
        minx, maxx = get_min_max(pts2a[0], pts2b[0], pts2c[0])
        miny, maxy = get_min_max(pts2a[1], pts2b[1], pts2c[1])
        minx, maxx = clip(minx, 0, screen.shape[0]-1), clip(maxx+1, 1, screen.shape[0])
        miny, maxy = clip(miny, 0, screen.shape[1]-1), clip(maxy+1, 1, screen.shape[1])
        a, b, c, d = (pts2c[0] - pts2a[0])/bc_c, (pts2b[0] - pts2a[0])/bc_c, (pts2c[1] - pts2a[1])/bc_c, (pts2b[1] - pts2a[1])/bc_c
        uva = uva[0] * width * ptsa, uva[1] * height * ptsa
        uvb = uvb[0] * width * ptsb, uvb[1] * height * ptsb
        uvc = uvc[0] * width * ptsc, uvc[1] * height * ptsc
        light_a = light_a[0] * ptsa, light_a[1] * ptsa, light_a[2] * ptsa
        light_b = light_b[0] * ptsb, light_b[1] * ptsb, light_b[2] * ptsb
        light_c = light_c[0] * ptsc, light_c[1] * ptsc, light_c[2] * ptsc
        clip_a, clip_b, clip_c = clip_a * ptsa, clip_b * ptsb, clip_c * ptsc
        tmp1 = pts2a[1] - miny + 1

        for j in prange(minx, maxx):
            flag = False
            temp = pts2a[0] - float(j)
            m0, m1 = b * tmp1 - temp * d, temp * c - a * tmp1
            m2 = 1 - m1 - m0  # 重心坐标使用递推计算
            bc_clip_sum = m2 * ptsa + m1 * ptsb + m0 * ptsc
            clip_sum = m2 * clip_a + m1 * clip_b + m0 * clip_c
            u, v = uva[1] * m2 + uvb[1] * m1 + uvc[1] * m0, uva[0] * m2 + uvb[0] * m1 + uvc[0] * m0
            light_r = light_a[0] * m2 + light_b[0] * m1 + light_c[0] * m0
            light_g = light_a[1] * m2 + light_b[1] * m1 + light_c[1] * m0
            light_b1 = light_a[2] * m2 + light_b[2] * m1 + light_c[2] * m0

            addm0, addm1, addm2 = -b, a, -(a - b)
            bc_clip_add = addm2 * ptsa + addm1 * ptsb + addm0 * ptsc
            clip_add = addm2 * clip_a + addm1 * clip_b + addm0 * clip_c
            u_add, v_add = uva[1] * addm2 + uvb[1] * addm1 + uvc[1] * addm0, uva[0] * addm2 + uvb[0] * addm1 + uvc[0] * addm0
            light_r_add = light_a[0] * addm2 + light_b[0] * addm1 + light_c[0] * addm0
            light_g_add = light_a[1] * addm2 + light_b[1] * addm1 + light_c[1] * addm0
            light_b_add = light_a[2] * addm2 + light_b[2] * addm1 + light_c[2] * addm0
            for k in prange(screen.shape[1]-miny-1, screen.shape[1]-maxy-1, -1):
                # 必须显式转换成 double 参与底下的运算，不然结果是错的
                m0 += addm0
                m1 += addm1
                m2 += addm2
                bc_clip_sum += bc_clip_add
                clip_sum += clip_add
                u += u_add
                v += v_add
                light_r += light_r_add
                light_g += light_g_add
                light_b1 += light_b_add

                if m0 < 0 or m1 < 0 or m2 < 0:
                    if flag:  # 优化：当可以确定超过的是右边界，可以直接换行
                        break
                    continue
                flag = True

                frag_depth = clip_sum / bc_clip_sum
                last_depth = z_buffer[j, k]

                if frag_depth > last_depth or frag_depth > 60:
                    continue
                z_buffer[j, k] = frag_depth
                u1, v1 = int(u / bc_clip_sum), int(v / bc_clip_sum)
                if u1 >= texture_array.shape[0] or v1 >= texture_array.shape[1] or u1 < 0 or v1 < 0:
                    continue
                if texture_array[u1, v1] == 0x1000000:
                    z_buffer[j, k] = last_depth
                    continue
                screen[j, k] = texture_array[u1, v1]
                light_buffer[j, k] = light_r / bc_clip_sum, light_g / bc_clip_sum, light_b1 / bc_clip_sum
