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
    return (prev[3] + 0.1) / (prev[3] - curv[3])


@jit('float64[:](float64[:],float64[:],float64)', nopython=True, fastmath=True)
def lerp_vec(start, end, alpha):
    return start + (end - start) * alpha


@jit(nopython=True, fastmath=True, looplift=True)
def render_opaque_face(screen, zbuffer, ptsa, ptsb, ptsc, uva, uvb, uvc, width, height, texture_array):
    clip_a, clip_b, clip_c = ptsa[2], ptsb[2], ptsc[2]
    pts2a = ptsa[0] / ptsa[3], ptsa[1] / ptsa[3]
    pts2b = ptsb[0] / ptsb[3], ptsb[1] / ptsb[3]
    pts2c = ptsc[0] / ptsc[3], ptsc[1] / ptsc[3]
    bc_c = (pts2c[0] - pts2a[0]) * (pts2b[1] - pts2a[1]) - (pts2b[0] - pts2a[0]) * (pts2c[1] - pts2a[1])
    if bc_c < 1e-3:
        return
    ptsa, ptsb, ptsc = 1 / ptsa[3], 1 / ptsb[3], 1 / ptsc[3]
    minx, maxx = get_min_max(pts2a[0], pts2b[0], pts2c[0])
    miny, maxy = get_min_max(pts2a[1], pts2b[1], pts2c[1])
    minx, maxx = clip(minx, 0, zbuffer.shape[0] - 1), clip(maxx + 1, 1, zbuffer.shape[0])
    miny, maxy = clip(miny, 0, zbuffer.shape[1] - 1), clip(maxy + 1, 1, zbuffer.shape[1])
    a, b, c, d = (pts2c[0] - pts2a[0]) / bc_c, (pts2b[0] - pts2a[0]) / bc_c, (pts2c[1] - pts2a[1]) / bc_c, (pts2b[1] - pts2a[1]) / bc_c
    uva = uva[0] * width * ptsa, uva[1] * height * ptsa
    uvb = uvb[0] * width * ptsb, uvb[1] * height * ptsb
    uvc = uvc[0] * width * ptsc, uvc[1] * height * ptsc
    clip_a, clip_b, clip_c = clip_a * ptsa, clip_b * ptsb, clip_c * ptsc
    tmp1 = pts2a[1] - miny + 1

    addm0, addm1, addm2 = -(a - b), a, -b
    bc_clip_add = addm0 * ptsa + addm1 * ptsb + addm2 * ptsc
    clip_add = addm0 * clip_a + addm1 * clip_b + addm2 * clip_c
    u_add, v_add = uva[1] * addm0 + uvb[1] * addm1 + uvc[1] * addm2, uva[0] * addm0 + uvb[0] * addm1 + uvc[0] * addm2

    addmm0, addmm1, addmm2 = -(d - c), -c, d
    add_bc_clip_sum = addmm0 * ptsa + addmm1 * ptsb + addmm2 * ptsc
    add_clip_sum = addmm0 * clip_a + addmm1 * clip_b + addmm2 * clip_c
    add_u = uva[1] * addmm0 + uvb[1] * addmm1 + uvc[1] * addmm2
    add_v = uva[0] * addmm0 + uvb[0] * addmm1 + uvc[0] * addmm2

    temp = pts2a[0] - float(minx)
    mm0, mm1, mm2 = b * tmp1 - temp * d, temp * c - a * tmp1, 1 + temp * (d - c) + tmp1 * (a - b)
    _bc_clip_sum = mm2 * ptsa + mm1 * ptsb + mm0 * ptsc
    _clip_sum = mm2 * clip_a + mm1 * clip_b + mm0 * clip_c
    _u, _v = uva[1] * mm2 + uvb[1] * mm1 + uvc[1] * mm0, uva[0] * mm2 + uvb[0] * mm1 + uvc[0] * mm0
    for j in prange(minx, maxx):
        flag = False
        m0, m1, m2 = mm0, mm1, mm2
        bc_clip_sum = _bc_clip_sum
        clip_sum = _clip_sum
        u, v = _u, _v

        mm0 += addmm2
        mm1 += addmm1
        mm2 += addmm0
        _bc_clip_sum += add_bc_clip_sum
        _clip_sum += add_clip_sum
        _u += add_u
        _v += add_v
        if (m0 < 0 and addm2 <= 0) or (m1 < 0 and addm1 <= 0) or (m2 < 0 and addm0 <= 0):
            continue
        n = max((0 if m0 >= 0 else int(-m0/addm2)), (0 if m1 >= 0 else int(-m1/addm1)), (0 if m2 >= 0 else int(-m2/addm0)))
        if n:
            m0 += n * addm2
            m1 += n * addm1
            m2 += n * addm0
            bc_clip_sum += n * bc_clip_add
            clip_sum += n * clip_add
            u += n * u_add
            v += n * v_add
        for k in prange(miny+n, maxy):
            # 必须显式转换成 double 参与底下的运算，不然结果是错的
            m0 += addm2
            m1 += addm1
            m2 += addm0
            bc_clip_sum += bc_clip_add
            clip_sum += clip_add
            u += u_add
            v += v_add

            if m0 < 0 or m1 < 0 or m2 < 0:
                if flag:  # 优化：当可以确定超过的是右边界，可以直接换行
                    break
                continue
            flag = True

            frag_depth = clip_sum / bc_clip_sum

            if frag_depth > zbuffer[j, k]:
                continue
            zbuffer[j, k] = frag_depth
            screen[j, k] = texture_array[int(u / bc_clip_sum), int(v / bc_clip_sum)]


@jit(nopython=True, fastmath=True, looplift=True)
def generate_faces_new(screen, indices, uv_indices, pts, uv_triangle, texture_array, zbuffer):
    # 使用 z-buffer 算法绘制三角形，以及 flat 着色

    length: int = indices.shape[0]  # 三角形总个数
    width, height = texture_array.shape[1], texture_array.shape[0]

    for i in prange(length):
        ptsa, ptsb, ptsc = pts[indices[i, 0]], pts[indices[i, 1]], pts[indices[i, 2]]
        uva = uv_triangle[uv_indices[i, 0], 0], uv_triangle[uv_indices[i, 0], 1]
        uvb = uv_triangle[uv_indices[i, 1], 0], uv_triangle[uv_indices[i, 1], 1]
        uvc = uv_triangle[uv_indices[i, 2], 0], uv_triangle[uv_indices[i, 2], 1]
        nums = int(ptsa[3] > -0.1) + int(ptsb[3] > -0.1) + int(ptsc[3] > -0.1)  # 指有几个点在屏幕外
        if nums:  # 透视裁剪
            if nums == 3:
                continue
            out_vert_num = 0
            out_pts = np.empty((4, 4), dtype=np.float64)
            out_uv = np.empty((4, 2), dtype=np.float64)
            for j in range(3):
                curv_index = j
                prev_index = (j - 1 + 3) % 3
                curv = pts[indices[i, curv_index]]
                prev = pts[indices[i, prev_index]]
                is_cur_inside = curv[3] <= -0.1
                is_pre_inside = prev[3] <= -0.1
                if is_cur_inside != is_pre_inside:
                    ratio = get_intersect_ratio(prev, curv)
                    out_pts[out_vert_num] = lerp_vec(prev, curv, ratio)
                    out_uv[out_vert_num] = lerp_vec(uv_triangle[uv_indices[i, prev_index]],
                                                    uv_triangle[uv_indices[i, curv_index]], ratio)
                    out_vert_num += 1
                if is_cur_inside:
                    out_pts[out_vert_num] = curv
                    out_uv[out_vert_num] = uv_triangle[uv_indices[i, curv_index]]
                    out_vert_num += 1
            if out_vert_num == 3:
                uva = out_uv[0, 0], out_uv[0, 1]
                uvb = out_uv[1, 0], out_uv[1, 1]
                uvc = out_uv[2, 0], out_uv[2, 1]
                ptsa, ptsb, ptsc = out_pts[0], out_pts[1], out_pts[2]
            elif out_vert_num == 4:
                uva = out_uv[0, 0], out_uv[0, 1]
                uvb = out_uv[1, 0], out_uv[1, 1]
                uvc = out_uv[2, 0], out_uv[2, 1]
                ptsa, ptsb, ptsc = out_pts[0], out_pts[1], out_pts[2]
                render_opaque_face(screen, zbuffer, ptsa, ptsb, ptsc, uva, uvb, uvc, width, height, texture_array)
                uva = out_uv[0, 0], out_uv[0, 1]
                uvb = out_uv[2, 0], out_uv[2, 1]
                uvc = out_uv[3, 0], out_uv[3, 1]
                ptsa, ptsb, ptsc = out_pts[0], out_pts[2], out_pts[3]
            else:
                continue
        render_opaque_face(screen, zbuffer, ptsa, ptsb, ptsc, uva, uvb, uvc, width, height, texture_array)
