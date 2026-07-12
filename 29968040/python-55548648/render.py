import numpy as np
import pygame
from matrix import calc_matrix
from speedup import generate_faces
from model import Model


class Render:
    def __init__(self):
        self.model = Model('data/scene.obj', 'data/texture.png')

    def render3d(self, screen, w, h, angle_alpha, angle_beta, tx, ty, tz):
        z_buffer = np.full((w, h), np.inf, dtype=np.float64)
        final_matrix = calc_matrix(w, h, angle_alpha, angle_beta, tx, ty, tz)
        pts = np.matmul(self.model.vertices, final_matrix)  # 存储屏幕坐标
        generate_faces(
            pygame.surfarray.pixels2d(screen), self.model.indices, self.model.uv_indices,
            pts, self.model.uv_vertices, self.model.texture_array, z_buffer
        )  # 逐个绘制三角形
