import numpy as np
from numba import jit, prange


@jit('UniTuple(int32, 2)(float64,float64,float64)', nopython=True, cache=True)
def get_min_max(a, b, c):
    return int(min(min(a, b), c)), int(max(max(a, b), c))


@jit('int32(int32,int32,int32)', nopython=True, cache=True)
def clip(a, b, c):
    return max(b, min(a, c))


@jit('float64(float64,float64,float64,float64,float64)', nopython=True, cache=True, fastmath=True)
def new_dot_product(a0, a1, a2, b0, b1):
    return float(a0 * b0 + a1 * b1 + a2)


@jit(nopython=True, cache=True, fastmath=True)
def generate_faces_new(triangles, pts, uv_triangle, clip_vert,
                       width, height, screen, texture_array, intensities, zbuffer, mats):
    # 使用 z-buffer 算法绘制三角形

    length: int = triangles.shape[0]  # 三角形总个数

    for i in prange(length):
        if intensities[i] < 0:
            continue
        ptsa = pts[i, 0]
        ptsb = pts[i, 1]
        ptsc = pts[i, 2]
        uva = uv_triangle[i, 0, 0], uv_triangle[i, 0, 1]
        uvb = uv_triangle[i, 1, 0], uv_triangle[i, 1, 1]
        uvc = uv_triangle[i, 2, 0], uv_triangle[i, 2, 1]

        pts2a = triangles[i, 0, 0], triangles[i, 0, 1]
        pts2b = triangles[i, 1, 0], triangles[i, 1, 1]
        pts2c = triangles[i, 2, 0], triangles[i, 2, 1]
        minx, maxx = get_min_max(pts2a[0], pts2b[0], pts2c[0])
        miny, maxy = get_min_max(pts2a[1], pts2b[1], pts2c[1])
        minx, maxx = clip(minx, 0, screen.shape[0]-1), clip(maxx+1, 1, screen.shape[0])
        miny, maxy = clip(miny, 0, screen.shape[1]-1), clip(maxy+1, 1, screen.shape[1])
        mata, matb, matc = mats[i, 0], mats[i, 1], mats[i, 2]
        for j in prange(minx, maxx):
            flag = False
            for k in prange(miny, maxy):
                # 必须显式转换成 double 参与底下的运算，不然结果是错的
                x = float(j)
                y = float(k)
                bc = (
                    new_dot_product(mata[0], mata[1], mata[2], x, y),
                    new_dot_product(matb[0], matb[1], matb[2], x, y),
                    new_dot_product(matc[0], matc[1], matc[2], x, y),
                )
                if bc[0] < -0.00001 or bc[1] < -0.00001 or bc[2] < -0.00001:
                    if flag:  # 优化：当可以确定超过的是右边界，可以直接换行
                        break
                    continue
                flag = True
                bc_clip_sum = (bc[0] / ptsa + bc[1] / ptsb + bc[2] / ptsc)
                bc_clip = (bc[0] / ptsa / bc_clip_sum,
                           bc[1] / ptsb / bc_clip_sum,
                           bc[2] / ptsc / bc_clip_sum)

                frag_depth = clip_vert[i, 0] * bc_clip[0] + clip_vert[i, 1] * bc_clip[1] + clip_vert[i, 2] * bc_clip[2]

                if frag_depth > zbuffer[j, k]:
                    continue
                # Blender 导出来的 uv 数据，跟之前的顶点数据有一样的问题，Y轴是个反的，
                # 所以这里的纹理图片要旋转一下才能 work
                v = (uva[0] * bc_clip[0] + uvb[0] * bc_clip[1] + uvc[0] * bc_clip[2]) * width
                u = (uva[1] * bc_clip[0] + uvb[1] * bc_clip[1] + uvc[1] * bc_clip[2]) * height
                if v >= width or u >= height:
                    continue
                zbuffer[j, k] = frag_depth
                intensity = intensities[i]
                color: np.ndarray = texture_array[int(u), int(v)]
                screen[j, screen.shape[1]-k-1] = int(color[0] * intensity), int(color[1] * intensity), int(color[2] * intensity)
