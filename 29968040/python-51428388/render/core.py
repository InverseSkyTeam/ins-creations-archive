import typing as t
from functools import partial
from numba import jit, njit, prange
import time
import numpy as np
from .canvas import Canvas

import speedup


# Math util
@njit(cache=True)
def normalize(v):
    return np.array(speedup.normalize(v[0], v[1], v[2]), dtype=np.float64)


@njit(cache=True)
def dot_product(a: np.ndarray, b: np.ndarray):
    return speedup.dot_product(a[0], a[1], a[2], b[0], b[1], b[2])


@njit(cache=True)
def cross_product(a: np.ndarray, b: np.ndarray):
    return np.array(speedup.cross_product(a[0], a[1], a[2], b[0], b[1], b[2]), dtype=np.float64)


@njit(cache=True)
def get_light_intensity(face) -> float:
    light = np.array((-2, 4, -10))
    v1, v2, v3 = face
    up = normalize(cross_product(v2 - v1, v3 - v1))
    return dot_product(up, normalize(light))


def look_at(eye: np.ndarray, target: np.ndarray, up: np.ndarray):
    """
    http://www.songho.ca/opengl/gl_camera.html#lookat

    Args:
        eye: 摄像机的世界坐标位置
        target: 观察点的位置
        up: 就是你想让摄像机立在哪个方向
            https://stackoverflow.com/questions/10635947/what-exactly-is-the-up-vector-in-opengls-lookat-function
            这里默认使用了 0, -1, 0， 因为 blender 导出来的模型数据似乎有问题，导致y轴总是反的，于是把摄像机的up也翻一下得了。
    """
    f = normalize(eye - target)
    l = normalize(cross_product(up, f))  # noqa: E741
    u = cross_product(f, l)

    rotate_matrix = np.matrix(
        [[*l, 0], [*u, 0], [*f, 0], [0, 0, 0, 1.0]]
    )
    translate_matrix = np.matrix(
        [[1, 0, 0, -eye[0]], [0, 1, 0, -eye[1]], [0, 0, 1, -eye[2]], [0, 0, 0, 1.0]]
    )

    return rotate_matrix * translate_matrix


def perspective_project(r, t, n, f):  # noqa: E741
    """
    目的：
        把相机坐标转换成投影在视网膜的范围在(-1, 1)的笛卡尔坐标

    原理：
        对于x，y坐标，相似三角形可以算出投影点的x，y
        对于z坐标，是假设了near是-1，far是1，然后带进去算的
        http://www.songho.ca/opengl/gl_projectionmatrix.html
        https://www.scratchapixel.com/lessons/3d-basic-rendering/perspective-and-orthographic-projection-matrix/opengl-perspective-projection-matrix

    推导出来的矩阵：
        [
            2n/(r-l) 0        (r+l/r-l)   0
            0        2n/(t-b) (t+b)/(t-b) 0
            0        0        -(f+n)/f-n  (-2*f*n)/(f-n)
            0        0        -1          0
        ]

    实际上由于我们用的视网膜(near pane)是个关于远点对称的矩形，所以矩阵简化为：
        [
            n/r      0        0           0
            0        n/t      0           0
            0        0        -(f+n)/f-n  (-2*f*n)/(f-n)
            0        0        -1          0
        ]

    Args:
        :param r: right,
        :param t: top,
        :param n: near,
        :param f: far
    """
    return np.matrix(
        [
            [n / r, 0, 0, 0],
            [0, n / t, 0, 0],
            [0, 0, -(f + n) / (f - n), (-2 * f * n) / (f - n)],
            [0, 0, -1, 0],
        ]
    )


@njit(cache=True)
def convert_model(screen_vertices, indices, uv_vertices, uv_indices, world_vertices,
                  intensities, triangles):
    for i, triangle_indices in enumerate(indices):
        screen_triangle = screen_vertices[triangle_indices - 1]
        uv_triangle = uv_vertices[uv_indices[i] - 1]
        world_triangle = world_vertices[triangle_indices - 1, :3]
        intensities[i] = abs(get_light_intensity(world_triangle))
        triangles[i] = np.column_stack((screen_triangle, uv_triangle))


def draw_with_z_buffer(screen_vertices, world_vertices, model, canvas):
    """ z-buffer algorithm
    """
    intensities = np.zeros((model.indices.shape[0]), dtype=np.float64)
    triangles = np.zeros((model.indices.shape[0], 3, 5), dtype=np.float64)
    convert_model(screen_vertices, model.indices, model.uv_vertices, model.uv_indices,
                  world_vertices, intensities, triangles)
    speedup.generate_faces(
        triangles, model.texture_width, model.texture_height,
        canvas.img, model.texture_array, intensities
    )


@njit(cache=True)
def ndc(vertices, temp, width, height, model_matrix, world_vertices):
    res = np.zeros((vertices.shape[0], 3), dtype=np.float64)
    for i in range(vertices.shape[0]):
        """
        各个坐标同时除以 w，得到 NDC 坐标
        """
        v = np.dot(model_matrix, vertices[i])
        world_vertices[i] = v[:, 0]
        v = np.dot(temp, v)
        w = v[3, 0]
        xx, yy, zz = v[0, 0] / w, v[1, 0] / w, v[2, 0] / w
        x = y = 0
        n, f = 0.3, 1000
        res[i] = [
            width * 0.5 * xx + x + width * 0.5,
            height * 0.5 * yy + y + height * 0.5,
            0.5 * (f - n) * zz + 0.5 * (f + n),
        ]
    return res


def render(model, height, width, filename, screen, angleX, angleY):
    """
    Args:
        model: the Model object
        height: cavas height
        width: cavas width
        filename: picture file name
    """
    model_matrix = np.array([[1, 0, 0, 0],
                             [0, np.cos(angleX), np.sin(angleX), 0],
                             [0, -np.sin(angleX), np.cos(angleX), 0],
                             [0, 0, 0, 1]], dtype=np.float64)
    model_matrix1 = np.array([[np.cos(angleY), 0, -np.sin(angleY), 0],
                              [0, 1, 0, 0],
                              [np.sin(angleY), 0, np.cos(angleY), 0],
                              [0, 0, 0, 1]], dtype=np.float64)
    model_matrix = np.dot(model_matrix, model_matrix1)
    # TODO: camera configration2
    view_matrix = look_at(np.array((-4, -4, 10)), np.zeros(3), np.array((0, -1, 0), dtype=np.float64))
    projection_matrix = perspective_project(0.5, 0.5, 3, 1000)
    temp = np.array(projection_matrix * view_matrix)

    # the render pipeline
    world_vertices = np.zeros((model.vertices.shape[0], 4), dtype=np.float64)
    screen_vertices = ndc(model.vertices, temp, width, height, model_matrix, world_vertices)
    canvas = Canvas(filename, height, width, screen)
    draw_with_z_buffer(screen_vertices, world_vertices, model, canvas)
