import numpy as np
from numba import jit, prange


@jit('UniTuple(int32, 2)(float64,float64,float64)', nopython=True, cache=True)
def get_min_max(a, b, c):
    return int(min(min(a, b), c)), int(max(max(a, b), c))


@jit('int32(int32,int32,int32)', nopython=True, cache=True)
def clip(a, b, c):
    return max(b, min(a, c))


@jit('UniTuple(float64, 2)(float64,float64,float64,float64,float64,float64)', nopython=True, cache=True, fastmath=True)
def cross_product(a0, a1, a2, b0, b1, b2):
    x = a1 * b2 - a2 * b1
    y = a2 * b0 - a0 * b2
    return float(x), float(y)


@jit(nopython=True, cache=True, fastmath=True)
def generate_faces_new(indices, uv_indices, norm_indices, pts2, pts, uv_triangle,
                       clip_vert, norms, width, height, screen, texture_array, zbuffer, O2):
    # 使用 z-buffer 算法绘制三角形

    length: int = indices.shape[0]  # 三角形总个数

    for i in prange(length):
        pts2a = pts2[indices[i, 0], 0], pts2[indices[i, 0], 1]
        pts2b = pts2[indices[i, 1], 0], pts2[indices[i, 1], 1]
        pts2c = pts2[indices[i, 2], 0], pts2[indices[i, 2], 1]
        bc_c = (pts2c[0] - pts2a[0]) * (pts2b[1] - pts2a[1]) - (pts2b[0] - pts2a[0]) * (pts2c[1] - pts2a[1])
        if (-bc_c if O2 else abs(bc_c)) < 1e-3:
            continue
        ptsa = pts[indices[i, 0], 3]
        ptsb = pts[indices[i, 1], 3]
        ptsc = pts[indices[i, 2], 3]
        uva = uv_triangle[uv_indices[i, 0], 0], uv_triangle[uv_indices[i, 0], 1]
        uvb = uv_triangle[uv_indices[i, 1], 0], uv_triangle[uv_indices[i, 1], 1]
        uvc = uv_triangle[uv_indices[i, 2], 0], uv_triangle[uv_indices[i, 2], 1]
        norma, normb, normc = norms[norm_indices[i, 0]], norms[norm_indices[i, 1]], norms[norm_indices[i, 2]]
        minx, maxx = get_min_max(pts2a[0], pts2b[0], pts2c[0])
        miny, maxy = get_min_max(pts2a[1], pts2b[1], pts2c[1])
        minx, maxx = clip(minx, 0, screen.shape[0]-1), clip(maxx+1, 1, screen.shape[0])
        miny, maxy = clip(miny, 0, screen.shape[1]-1), clip(maxy+1, 1, screen.shape[1])
        for j in prange(minx, maxx):
            flag = False
            for k in prange(miny, maxy):
                # 必须显式转换成 double 参与底下的运算，不然结果是错的
                x = float(j)
                y = float(k)
                m = cross_product(pts2c[0] - pts2a[0], pts2b[0] - pts2a[0], pts2a[0] - x, pts2c[1] - pts2a[1], pts2b[1] - pts2a[1], pts2a[1] - y)
                bcy = m[1] / bc_c
                bcz = m[0] / bc_c
                bc = (1 - bcy - bcz, bcy, bcz)
                if bc[0] < -0.00001 or bc[1] < -0.00001 or bc[2] < -0.00001:
                    if flag:  # 优化：当可以确定超过的是右边界，可以直接换行
                        break
                    continue
                flag = True
                bc_clip_sum = (bc[0] / ptsa + bc[1] / ptsb + bc[2] / ptsc)
                bc_clip = (bc[0] / ptsa / bc_clip_sum,
                           bc[1] / ptsb / bc_clip_sum,
                           bc[2] / ptsc / bc_clip_sum)

                frag_depth = clip_vert[indices[i, 0], 2] * bc_clip[0] + clip_vert[indices[i, 1], 2] * bc_clip[1] + clip_vert[indices[i, 2], 2] * bc_clip[2]

                if frag_depth > zbuffer[j, k]:
                    continue
                # Blender 导出来的 uv 数据，跟之前的顶点数据有一样的问题，Y轴是个反的，
                # 所以这里的纹理图片要旋转一下才能 work
                v = (uva[0] * bc_clip[0] + uvb[0] * bc_clip[1] + uvc[0] * bc_clip[2]) * width
                u = (uva[1] * bc_clip[0] + uvb[1] * bc_clip[1] + uvc[1] * bc_clip[2]) * height
                if v >= width or u >= height or v < 0 or u < 0:
                    continue
                zbuffer[j, k] = frag_depth
                intensity = norma * bc_clip[0] + normb * bc_clip[1] + normc * bc_clip[2]
                color: np.ndarray = texture_array[int(u), int(v)]
                screen[j, screen.shape[1]-k-1] = min(int(color[0] * intensity), 255), min(int(color[1] * intensity), 255), min(int(color[2] * intensity), 255)
