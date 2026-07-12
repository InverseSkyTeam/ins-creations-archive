import numpy as np


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


def zoom(scale):
    return np.array(
        [
            [scale, 0, 0, 0],
            [0, scale, 0, 0],
            [0, 0, scale, 0],
            [0, 0, 0, 1],
        ], dtype=np.float64
    )


def perspective_project(f):
    return np.array(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, -1/f, -1],
        ], dtype=np.float64
    )


def viewport(w, h):
    return np.array(
        [
            [1, 0, 0, w/2],
            [0, 1, 0, h/2],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ], dtype=np.float64
    )


def calc_matrix(w, h, r_x, r_y, scale):
    transform_matrix = np.dot(np.dot(rotate_x(r_x), rotate_y(r_y)), zoom(scale))
    proj_matrix = perspective_project(4000)
    viewport_matrix = viewport(w, h)
    # 矩阵预乘
    final_matrix = np.dot(viewport_matrix, np.dot(proj_matrix, transform_matrix)).T
    return final_matrix

