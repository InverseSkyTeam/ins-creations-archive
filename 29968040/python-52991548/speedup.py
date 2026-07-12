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


@jit('float64(float64,float64,float64)', nopython=True, fastmath=True)
def lerp_num(start, end, alpha):
    return start + (end - start) * alpha


@jit(nopython=True, fastmath=True, looplift=True)
def render_clip_face(screen, zbuffer, ptsa, ptsb, ptsc, uva, uvb, uvc,
                     clip_a, clip_b, clip_c, width, height, texture_array, O2):
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

        addm0, addm1, addm2 = -b, a, -(a - b)
        bc_clip_add = addm2 * ptsa + addm1 * ptsb + addm0 * ptsc
        clip_add = addm2 * clip_a + addm1 * clip_b + addm0 * clip_c
        u_add, v_add = uva[1] * addm2 + uvb[1] * addm1 + uvc[1] * addm0, uva[0] * addm2 + uvb[0] * addm1 + uvc[0] * addm0
        for k in prange(screen.shape[1] - miny - 1, screen.shape[1] - maxy - 1, -1):
            # 必须显式转换成 double 参与底下的运算，不然结果是错的
            m0 += addm0
            m1 += addm1
            m2 += addm2
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

            if frag_depth > zbuffer[j, k] or frag_depth > 60:
                continue
            zbuffer[j, k] = frag_depth
            u1, v1 = int(u / bc_clip_sum), int(v / bc_clip_sum)
            if u1 >= texture_array.shape[0] or v1 >= texture_array.shape[1] or u1 < 0 or v1 < 0:
                continue
            screen[j, k] = texture_array[u1, v1]


@jit(nopython=True, fastmath=True, looplift=True)
def generate_faces_flat(indices, uv_indices, pts, uv_triangle,
                        clip_vert, width, height, screen, texture_array, zbuffer, O2):
    # 使用 z-buffer 算法绘制三角形，以及 flat 着色

    length: int = indices.shape[0]  # 三角形总个数

    for i in prange(length):
        ptsa, ptsb, ptsc = pts[indices[i, 0]], pts[indices[i, 1]], pts[indices[i, 2]]
        uva = uv_triangle[uv_indices[i, 0], 0], uv_triangle[uv_indices[i, 0], 1]
        uvb = uv_triangle[uv_indices[i, 1], 0], uv_triangle[uv_indices[i, 1], 1]
        uvc = uv_triangle[uv_indices[i, 2], 0], uv_triangle[uv_indices[i, 2], 1]
        clip_a = clip_vert[indices[i, 0], 2]
        clip_b = clip_vert[indices[i, 1], 2]
        clip_c = clip_vert[indices[i, 2], 2]
        nums = (ptsa[3] < 0.1) + (ptsb[3] < 0.1) + (ptsc[3] < 0.1)  # 指有几个点在屏幕外
        if nums:  # 透视裁剪
            if nums == 3:
                continue
            out_vert_num = 0
            out_pts = np.empty((4, 4), dtype=np.float64)
            out_uv = np.empty((4, 2), dtype=np.float64)
            out_clip = np.empty(4, dtype=np.float64)
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
                    out_uv[out_vert_num] = lerp_vec(uv_triangle[uv_indices[i, prev_index]],
                                                    uv_triangle[uv_indices[i, curv_index]], ratio)
                    out_clip[out_vert_num] = lerp_num(clip_vert[indices[i, prev_index], 2],
                                                      clip_vert[indices[i, curv_index], 2], ratio)
                    out_vert_num += 1
                if is_cur_inside:
                    out_pts[out_vert_num] = curv
                    out_uv[out_vert_num] = uv_triangle[uv_indices[i, curv_index]]
                    out_clip[out_vert_num] = clip_vert[indices[i, curv_index], 2]
                    out_vert_num += 1
            if out_vert_num == 3:
                uva = out_uv[0, 0], out_uv[0, 1]
                uvb = out_uv[1, 0], out_uv[1, 1]
                uvc = out_uv[2, 0], out_uv[2, 1]
                ptsa, ptsb, ptsc = out_pts[0], out_pts[1], out_pts[2]
                clip_a, clip_b, clip_c = out_clip[0], out_clip[1], out_clip[2]
            elif out_vert_num == 4:
                uva = out_uv[0, 0], out_uv[0, 1]
                uvb = out_uv[1, 0], out_uv[1, 1]
                uvc = out_uv[2, 0], out_uv[2, 1]
                ptsa, ptsb, ptsc = out_pts[0], out_pts[1], out_pts[2]
                clip_a, clip_b, clip_c = out_clip[0], out_clip[1], out_clip[2]
                render_clip_face(screen, zbuffer, ptsa, ptsb, ptsc, uva, uvb, uvc,
                                 clip_a, clip_b, clip_c, width, height, texture_array, O2)
                uva = out_uv[0, 0], out_uv[0, 1]
                uvb = out_uv[2, 0], out_uv[2, 1]
                uvc = out_uv[3, 0], out_uv[3, 1]
                ptsa, ptsb, ptsc = out_pts[0], out_pts[2], out_pts[3]
                clip_a, clip_b, clip_c = out_clip[0], out_clip[2], out_clip[3]

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

            addm0, addm1, addm2 = -b, a, -(a - b)
            bc_clip_add = addm2 * ptsa + addm1 * ptsb + addm0 * ptsc
            clip_add = addm2 * clip_a + addm1 * clip_b + addm0 * clip_c
            u_add, v_add = uva[1] * addm2 + uvb[1] * addm1 + uvc[1] * addm0, uva[0] * addm2 + uvb[0] * addm1 + uvc[0] * addm0
            for k in prange(screen.shape[1]-miny-1, screen.shape[1]-maxy-1, -1):
                # 必须显式转换成 double 参与底下的运算，不然结果是错的
                m0 += addm0
                m1 += addm1
                m2 += addm2
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

                if frag_depth > zbuffer[j, k] or frag_depth > 60:
                    continue
                zbuffer[j, k] = frag_depth
                u1, v1 = int(u / bc_clip_sum), int(v / bc_clip_sum)
                if u1 >= texture_array.shape[0] or v1 >= texture_array.shape[1] or u1 < 0 or v1 < 0:
                    continue
                screen[j, k] = texture_array[u1, v1]


@jit(nopython=True, fastmath=True, looplift=True)
def fog_calc(screen, zbuffer):
    r, g, b = round(0.5*255), round(0.69*255), round(1.0*255)
    for x in prange(screen.shape[0]):
        for y in prange(screen.shape[1]):
            if 40 < zbuffer[x, y] <= 60:
                alpha = abs(zbuffer[x, y] - 60)/20
                screen[x, y, 0] = (1 - alpha) * r + alpha * screen[x, y, 0]
                screen[x, y, 1] = (1 - alpha) * g + alpha * screen[x, y, 1]
                screen[x, y, 2] = (1 - alpha) * b + alpha * screen[x, y, 2]
