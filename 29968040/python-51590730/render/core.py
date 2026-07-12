from numba import jit, njit
import numpy as np
import pygame
import pygame.gfxdraw
import math
import speedup


eye = np.array([0, 0, 3], dtype=np.float64)  # 相机位置
center = np.array([0, 0, 0], dtype=np.float64)  # 观察点的位置
up = np.array((0, 1, 0), dtype=np.float64)  # 相机朝向


@njit(cache=True, fastmath=True)
def cross_product(a0, a1, a2, b0, b1, b2):
    x = a1 * b2 - a2 * b1
    y = a2 * b0 - a0 * b2
    z = a0 * b1 - a1 * b0
    return x, y, z


def normalize(v):
    # 归一化操作
    unit = np.linalg.norm(v)
    if unit == 0:
        return np.zeros(3, dtype=np.float64)
    return v / unit


@njit(cache=True, fastmath=True)
def normalize1(v):
    # 归一化操作
    unit = math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])
    if unit == 0:
        return 0, 0, 0
    return v[0] / unit, v[1] / unit, v[2] / unit


@njit(cache=True, fastmath=True)
def get_light_intensity(a, b, light) -> float:
    # 计算某个面的漫反射强度
    _up = normalize1(cross_product(a[0], a[1], a[2], b[0], b[1], b[2]))
    return _up[0] * light[0] + _up[1] * light[1] + _up[2] * light[2]


def rotate_x(angle):
    return np.array(
        [
            [1, 0, 0, 0],
            [0, np.cos(angle), -np.sin(angle), 0],
            [0, np.sin(angle), np.cos(angle), 0],
            [0, 0, 0, 1],
        ], dtype=np.float64
    )


def rotate_y(angle):
    return np.array(
        [
            [np.cos(angle), 0, -np.sin(angle), 0],
            [0, 1, 0, 0],
            [np.sin(angle), 0, np.cos(angle), 0],
            [0, 0, 0, 1],
        ], dtype=np.float64
    )


def rotate_z(angle):
    return np.array(
        [
            [np.cos(angle), -np.sin(angle), 0, 0],
            [np.sin(angle), np.cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ], dtype=np.float64
    )


def zoom(scale):
    return np.array(
        [
            [scale, 0, 0, 0],
            [0, scale, 0, 0],
            [0, 0, scale, 0],
            [0, 0, 0, 1],
        ], dtype=np.float64
    )


def look_at(_eye: np.ndarray, _center: np.ndarray, _up: np.ndarray):
    """
    Args:
        _eye: 摄像机的世界坐标位置
        _center: 观察点的位置
        _up: 就是你想让摄像机立在哪个方向
    """
    z = normalize(_center - _eye)
    x = normalize(np.cross(_up, z))
    y = normalize(np.cross(z, x))

    Minv = np.array(
        [[*x, 0], [*y, 0], [*z, 0], [0, 0, 0, 1.0]],
        dtype=np.float64
    )
    Tr = np.array(
        [[1, 0, 0, -_eye[0]], [0, 1, 0, -_eye[1]], [0, 0, 1, -_eye[2]], [0, 0, 0, 1.0]],
        dtype=np.float64
    )

    return np.dot(Minv, Tr)


def perspective_project(f):
    return np.array(
        [
            [1,  0,    0, 0],
            [0, -1,    0, 0],
            [0,  0,    1, 0],
            [0,  0, -1/f, 0],
        ], dtype=np.float64
    )


def viewport(x, y, w, h):
    return np.array(
        [
            [w/2, 0, 0, x+w/2],
            [0, h/2, 0, y+h/2],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ], dtype=np.float64
    )


@jit(nopython=True)
def determinant(A):
    """A shape should be (B,n,n) return shape (B,)  """
    B, n, _ = A.shape
    AM = A.copy()
    # Section 2: Row ops on A to get in upper triangle form
    product = np.ones(B, dtype=A.dtype)
    for b in range(B):
        for fd in range(n):  # A) fd stands for focus diagonal
            for i in range(fd + 1, n):  # B) only use rows below fd row
                if AM[b][fd][fd] == 0:  # C) if diagonal is zero ...
                    AM[b][fd][fd] = 1.0e-18  # change to ~zero
                # D) cr stands for "current row"
                crScaler = AM[b][i][fd] / AM[b][fd][fd]
                # E) cr - crScaler * fdRow, one element at a time
                for j in range(n):
                    AM[b][i][j] = AM[b][i][j] - crScaler * AM[b][fd][j]
        # Section 3: Once AM is in upper triangle form ...
        for i in range(n):
            # ... product of diagonals is determinant
            product[b] *= AM[b][i][i]

    return product


@njit
def inv(ABC, mats, dets, intensities, model_triangle, light, O2):
    for i, data in enumerate(ABC):
        X = dets[i] if O2 else abs(dets[i])
        if X < 1e-3:
            continue
        mats[i] = np.linalg.inv(data).T
        intensities[i] = abs(get_light_intensity(model_triangle[i, 0], model_triangle[i, 1], light))


def draw_with_z_buffer_new(clip_vert, model_vertices, model, screen, pts, pts2, zbuffer, light, O2):
    """ z-buffer 算法
    """
    mats = np.empty((model.indices.shape[0], 3, 3), dtype=np.float64)  # 存储计算重心坐标的矩阵
    # 注意：重心坐标 ≠ 重心，重心只能有一个，但是重心坐标有无数个
    intensities = np.full((model.indices.shape[0]), -1, dtype=np.float64)  # 每个三角形漫反射光照强度
    new_pst2 = pts2[model.indices - 1]
    ABC = np.ones((model.indices.shape[0], 3, 3), dtype=np.float64)
    ABC[:, :, :2] = new_pst2
    dets = determinant(ABC)  # 这个直接 numba 算，实测比 np 快将近 10倍
    temp = model_vertices[model.indices - 1, :3]
    new_model_vertices = np.empty((model.indices.shape[0], 2, 3), dtype=np.float64)
    new_model_vertices[:, :2] = np.subtract(temp[:, 1:], temp[:, 0][:, np.newaxis])
    inv(ABC, mats, dets, intensities, new_model_vertices, light, O2)

    speedup.generate_faces_new(
        new_pst2, pts[model.indices - 1, 3], model.uv_vertices[model.uv_indices - 1],
        clip_vert[model.indices - 1, 2],
        model.texture_width, model.texture_height, screen, model.texture_array,
        intensities, zbuffer, mats
    )  # 逐个绘制三角形


def render_lines(i, screen):
    i = i.astype(int)
    i[:, :, 1] = screen.get_height() - i[:, :, 1] - 1
    return [pygame.gfxdraw.aatrigon(screen, *j[0], *j[1], *j[2], (0,) * 3) for j in i]


light_raw = np.array([[1], [1], [1], [1]], dtype=np.float64)


def render(model, height, width, screen, zbuffer, angle_x, angle_y, scale, mode, O2):
    # 绘制 3d 模型
    rotate_matrix = np.dot(np.dot(rotate_x(angle_x), rotate_y(angle_y)), zoom(scale))
    ModelView = look_at(eye, center, up)  # 模型矩阵
    Projection = perspective_project(np.linalg.norm(eye-center))  # 透视矩阵
    Viewport = viewport(width/8, height/8, width*3/4, height*3/4)  # 视口矩阵
    light = normalize(np.dot(rotate_matrix, light_raw)[:, 0])

    ModelView = np.dot(ModelView, rotate_matrix)
    Projection_ModelView = np.dot(Projection, ModelView)  # 因为矩阵乘法满足结合律，可以进行预乘，以减少运算量
    Viewport_Projection_ModelView = np.dot(Viewport, Projection_ModelView)

    model_vertices = np.matmul(rotate_matrix, model.vertices)[:, :, 0]  # 存储模型局部坐标系下的坐标
    clip_vert = np.matmul(Projection_ModelView, model.vertices)[:, :, 0]  # 存储模型相机坐标系坐标，且进行透视
    pts = np.matmul(Viewport_Projection_ModelView, model.vertices)[:, :, 0]  # 存储屏幕坐标
    pts2 = pts[:, :2] / pts[:, 3][:, None]
    if mode == 0:
        render_lines(pts2[model.indices - 1], screen)
    else:
        draw_with_z_buffer_new(clip_vert, model_vertices, model,
                               pygame.surfarray.pixels3d(screen),
                               pts, pts2, zbuffer, light, O2)
