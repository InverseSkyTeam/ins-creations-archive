from numba import jit, njit, prange
import numpy as np
from .canvas import Canvas
import pygame
import sys

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


def look_at(eye: np.ndarray, center: np.ndarray, up: np.ndarray):
    """
    Args:
        eye: 摄像机的世界坐标位置
        center: 观察点的位置
        up: 就是你想让摄像机立在哪个方向
    """
    z = normalize(center - eye)
    x = normalize(cross_product(up, z))
    y = normalize(cross_product(z, x))

    rotate_matrix = np.array(
        [[*x, 0], [*y, 0], [*z, 0], [0, 0, 0, 1.0]],
        dtype=np.float64
    )
    translate_matrix = np.array(
        [[1, 0, 0, -eye[0]], [0, 1, 0, -eye[1]], [0, 0, 1, -eye[2]], [0, 0, 0, 1.0]],
        dtype=np.float64
    )

    return np.dot(rotate_matrix, translate_matrix)


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


@njit(cache=True)
def convert_mat(arr):
    new_arr = np.ones((3, 3), dtype=np.float64)
    new_arr[:, :2] = arr[:, :2]
    return new_arr


@njit(cache=True)
def convert_model(clip_vert, indices, uv_vertices, uv_indices, world_vertices,
                  intensities, triangles, pts, pts2, mats):
    for i, triangle_indices in enumerate(indices):
        clip_vert_temp = clip_vert[triangle_indices - 1]
        pts_temp = pts[triangle_indices - 1]
        pts2_temp = pts2[triangle_indices - 1]
        ABC = convert_mat(pts2_temp)
        if np.linalg.det(ABC) < 1e-3:
            intensities[i] = -1
            continue
        mats[i] = np.linalg.inv(ABC).T
        uv_triangle = uv_vertices[uv_indices[i] - 1]
        world_triangle = world_vertices[triangle_indices - 1, :3]
        intensities[i] = abs(get_light_intensity(world_triangle))
        triangles[i] = np.column_stack((clip_vert_temp, uv_triangle, pts_temp, pts2_temp))
        # i:       0-3: clip_vert_temp, 4-5: uv_triangle, 6-9: pts, 10-11: pts2


def draw_with_z_buffer(clip_vert, world_vertices, model, canvas, pts, pts2):
    """ z-buffer algorithm
    """
    intensities = np.zeros((model.indices.shape[0]), dtype=np.float64)
    triangles = np.zeros((model.indices.shape[0], 3, 12), dtype=np.float64)
    mats = np.zeros((model.indices.shape[0], 3, 3), dtype=np.float64)
    convert_model(clip_vert, model.indices, model.uv_vertices, model.uv_indices,
                  world_vertices, intensities, triangles, pts, pts2, mats)
    zbuffer = np.full(canvas.img.shape[:2], np.inf, dtype=np.float64)
    speedup.generate_faces(
        triangles, model.texture_width, model.texture_height,
        canvas.img, model.texture_array, intensities, zbuffer, mats
    )


@njit(cache=True)
def ndc(vertices, temp, model_matrix, Viewport, world_vertices, clip_vert, pts):
    for i in range(vertices.shape[0]):
        v = np.dot(model_matrix, vertices[i])
        world_vertices[i] = v[:, 0]
        v = np.dot(temp, v)
        clip_vert[i] = v[:, 0]
        v = np.dot(Viewport, v)[:, 0]
        pts[i] = v


def render(model, height, width, screen, angleX, angleY, scale, x, y, z):
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
    eye, center, up = np.array((x, y, z), dtype=np.float64), np.zeros(3, dtype=np.float64), np.array((0, 1, 0), dtype=np.float64)
    ModelView = look_at(eye, center, up)
    Projection = perspective_project(np.sqrt(np.dot(eye-center, eye-center)))
    Viewport = viewport(width/8, height/8, width*3/4, height*3/4)
    temp = np.dot(Projection, ModelView)

    # the render pipeline
    world_vertices = np.zeros((model.vertices.shape[0], 4), dtype=np.float64)
    clip_vert = np.zeros((model.vertices.shape[0], 4), dtype=np.float64)
    pts = np.zeros((model.vertices.shape[0], 4), dtype=np.float64)
    pts2 = np.zeros((model.vertices.shape[0], 2), dtype=np.float64)
    ndc(model.vertices, temp, model_matrix, Viewport, world_vertices, clip_vert, pts)
    pts2[:, 0], pts2[:, 1] = pts[:, 0] / pts[:, 3], pts[:, 1] / pts[:, 3]
    canvas = Canvas(height, width, screen)
    draw_with_z_buffer(clip_vert, world_vertices, model, canvas, pts, pts2)
