import numpy as np
import math
from options import PLAYER_FOV


def normalize(v):
    # 归一化操作
    unit = np.linalg.norm(v)
    if unit == 0:
        return np.zeros(3, dtype=np.float64)
    return v / unit


def glRotatef(angle, x, y, z):
    x, y, z = normalize(np.array([x, y, z], dtype=np.float64))
    alpha = angle / 180 * np.pi
    s = np.sin(alpha)
    c = np.cos(alpha)
    t = 1.0 - c
    return np.array(
        [
            [t * x * x + c, t * x * y + s * z, t * x * z - s * y, 0],
            [t * x * y - s * z, t * y * y + c, t * y * z + s * x, 0],
            [t * x * z + s * y, t * y * z - s * x, t * z * z + c, 0],
            [0, 0, 0, 1],
        ], dtype=np.float64
    ).T


def gluPerspective(fov, aspect, near, far):
    ymax = near * math.tan(fov * math.pi / 360)
    ymin = -ymax
    xmin = ymin * aspect
    xmax = -xmin
    return np.array(
        [
            [(2*near)/(xmax-xmin), 0, (xmax+xmin)/(xmax-xmin), 0],
            [0,  (2*near)/(ymax-ymin), (ymax+ymin)/(ymax-ymin), 0],
            [0,  0, -((far+near)/(far-near)), -((2*far*near)/(far-near))],
            [0,  0, -1, 0],
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


def translation(tx, ty, tz):
    return np.array(
        [
            [1, 0, 0, tx],
            [0, 1, 0, ty],
            [0, 0, 1, tz],
            [0, 0, 0, 1],
        ], dtype=np.float64
    )


def update_matrix(rotation, position, is_crouch, fov_offset, width, height):
    x, y, z = position
    tx, ty, tz = -x, -y + bool(is_crouch) * 0.2, -z

    rotate_matrix = glRotatef(rotation[0], 0, 1, 0)
    rotate_matrix1 = glRotatef(-rotation[1], math.cos(math.radians(rotation[0])), 0, math.sin(math.radians(rotation[0])))
    transform_matrix = np.dot(
        np.dot(rotate_matrix, rotate_matrix1),
        translation(tx, ty, tz)
    )
    projection_matrix = gluPerspective(PLAYER_FOV + fov_offset, width / height, 0.1, 60.0)  # 透视矩阵
    viewport_matrix = viewport(0, 0, width, height)

    # 矩阵预乘
    final_matrix = np.dot(viewport_matrix, np.dot(projection_matrix, transform_matrix))

    return final_matrix
