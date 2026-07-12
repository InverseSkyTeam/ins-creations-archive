import numpy as np
import math


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


def zoom():
    return np.array(
        [
            [-1, 0,  0, 0],
            [0,  1,  0, 0],
            [0,  0, -1, 0],
            [0,  0,  0, 1],
        ], dtype=np.float64
    )


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
            [0, 1, 0, -ty],
            [0, 0, 1, tz],
            [0, 0, 0, 1],
        ], dtype=np.float64
    )


def calc_matrix(width, height, angle_y, angle_x, tx, ty, tz):
    transform_matrix = np.dot(
        np.dot(
            rotate_x(math.radians(angle_x)), rotate_y(math.radians(angle_y))
        ),
        np.dot(
            translation(tx, ty, tz),
            zoom()
        )
    )
    Projection = gluPerspective(300, width/height, 0.1, 500)  # 透视矩阵
    Viewport = viewport(0, 0, width, height)  # 视口矩阵

    # 矩阵预乘
    final_matrix = np.dot(Viewport, np.dot(Projection, transform_matrix)).T
    return final_matrix
