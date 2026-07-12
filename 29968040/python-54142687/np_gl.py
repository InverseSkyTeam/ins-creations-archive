import numpy as np
import math


def normalize(v):
    # 归一化操作
    unit = np.linalg.norm(v)
    if unit == 0:
        return np.zeros(v.shape[0], dtype=np.float64)
    return v / unit


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


def glRotatef(angle, x, y, z):
    x, y, z = normalize(np.array([x, y, z], dtype=np.float64))
    alpha = angle
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


def glTranslate(vec):
    return np.array(
        [
            [1, 0, 0, vec[0]],
            [0, 1, 0, vec[1]],
            [0, 0, 1, vec[2]],
            [0, 0, 0, 1],
        ], dtype=np.float64
    )


def glViewport(x, y, w, h):
    return np.array(
        [
            [w/2, 0, 0, x+w/2],
            [0, h/2, 0, y+h/2],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ], dtype=np.float64
    )

