import numpy as np
import pygame
import speedup


def render_cube(model, screen, zbuffer, final_matrix, O2=True):
    # 绘制 3d 模型
    # 初始化矩阵
    pts = np.matmul(final_matrix, model.vertices)[:, :, 0]  # 存储屏幕坐标

    speedup.generate_faces_flat(
        model.indices, model.uv_indices, pts, model.uv_vertices, model.uv_index,
        model.texture_width, model.texture_height, pygame.surfarray.pixels2d(screen),
        model.texture_array, zbuffer, O2
    )  # 逐个绘制三角形
