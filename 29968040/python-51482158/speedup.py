import numpy as np
from math import sqrt
from numba import jit, prange, njit


@jit(nopython=True, cache=True)
def normalize(x, y, z):
    unit = sqrt(x * x + y * y + z * z)
    if unit == 0:
        return 0, 0, 0
    return x / unit, y / unit, z / unit


@jit(nopython=True, cache=True)
def get_min_max(a, b, c):
    return int(min(min(a, b), c)), int(max(max(a, b), c))


@jit(nopython=True, cache=True)
def clip(a, b, c):
    return max(b, min(a, c))


@jit(nopython=True, cache=True)
def dot_product(a0, a1, a2, b0, b1, b2):
    return float(a0 * b0 + a1 * b1 + a2 * b2)


@jit(nopython=True, cache=True)
def new_dot_product(a0, a1, a2, b0, b1):
    return float(a0 * b0 + a1 * b1 + a2)


@jit(nopython=True, cache=True)
def cross_product(a0, a1, a2, b0, b1, b2):
    x = a1 * b2 - a2 * b1
    y = a2 * b0 - a0 * b2
    z = a0 * b1 - a1 * b0
    return float(x), float(y), float(z)


@jit(nopython=True, cache=True)
def generate_faces(triangles, width, height, screen, texture_array, intensities, zbuffer, mats):
    """ draw the triangle faces with z buffer

    Args:
        triangles: groups of vertices

    FYI:
        * zbuffer, https://github.com/ssloy/tinyrenderer/wiki/Lesson-3:-Hidden-faces-removal-(z-buffer)
        * uv mapping and perspective correction
    """
    length: int = triangles.shape[0]

    for i in prange(length):
        if intensities[i] < 0:
            continue
        ptsa = triangles[i, 0, 6], triangles[i, 0, 7], triangles[i, 0, 8], triangles[i, 0, 9]
        ptsb = triangles[i, 1, 6], triangles[i, 1, 7], triangles[i, 1, 8], triangles[i, 1, 9]
        ptsc = triangles[i, 2, 6], triangles[i, 2, 7], triangles[i, 2, 8], triangles[i, 2, 9]
        pts2a = triangles[i, 0, 10], triangles[i, 0, 11]
        pts2b = triangles[i, 1, 10], triangles[i, 1, 11]
        pts2c = triangles[i, 2, 10], triangles[i, 2, 11]
        uva = triangles[i, 0, 4], triangles[i, 0, 5]
        uvb = triangles[i, 1, 4], triangles[i, 1, 5]
        uvc = triangles[i, 2, 4], triangles[i, 2, 5]
        minx, maxx = get_min_max(pts2a[0], pts2b[0], pts2c[0])
        miny, maxy = get_min_max(pts2a[1], pts2b[1], pts2c[1])
        minx, maxx = clip(minx, 0, screen.shape[0]-1), clip(maxx+2, 1, screen.shape[0])
        miny, maxy = clip(miny-1, 0, screen.shape[1]-1), clip(maxy+2, 1, screen.shape[1])
        mata, matb, matc = mats[i, 0], mats[i, 1], mats[i, 2]
        for j in prange(minx, maxx):
            for k in prange(miny, maxy):
                # 必须显式转换成 double 参与底下的运算，不然结果是错的
                x = float(j)
                y = float(k)
                bc = (
                    new_dot_product(mata[0], mata[1], mata[2], x, y),
                    new_dot_product(matb[0], matb[1], matb[2], x, y),
                    new_dot_product(matc[0], matc[1], matc[2], x, y),
                )
                # here, -0.00001 because of the precision lose
                if bc[0] < -0.00001 or bc[1] < -0.00001 or bc[2] < -0.00001:
                    continue
                bc_clip_sum = (bc[0] / ptsa[3] + bc[1] / ptsb[3] + bc[2] / ptsc[3])
                bc_clip = (bc[0] / ptsa[3] / bc_clip_sum,
                           bc[1] / ptsb[3] / bc_clip_sum,
                           bc[2] / ptsc[3] / bc_clip_sum)

                frag_depth = triangles[i, 0, 2] * bc_clip[0] + triangles[i, 1, 2] * bc_clip[1] + triangles[i, 2, 2] * bc_clip[2]

                if frag_depth > zbuffer[j, k]:
                    continue
                # Blender 导出来的 uv 数据，跟之前的顶点数据有一样的问题，Y轴是个反的，
                # 所以这里的纹理图片要旋转一下才能 work
                v = (uva[0] * bc_clip[0] + uvb[0] * bc_clip[1] + uvc[0] * bc_clip[2]) * width
                u = (uva[1] * bc_clip[0] + uvb[1] * bc_clip[1] + uvc[1] * bc_clip[2]) * height

                zbuffer[j, k] = frag_depth
                intensity = intensities[i]
                color: np.ndarray = texture_array[int(u) - 1, int(v) - 1]
                screen[j, screen.shape[1]-k] = int(color[0] * intensity), int(color[1] * intensity), int(color[2] * intensity)
