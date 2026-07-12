import speedup
import numpy as np
import pygame


def render_cube(model, screen, zbuffer, final_matrix, daylight, light_buffer, O2=True):
    # 绘制 3d 模型
    # 初始化矩阵
    pts = np.matmul(model.vertices, final_matrix)
    skylight = model.skylights * daylight
    v_light_r = np.clip(model.lights_1_5, skylight, 1.0) * model.shading
    v_light_g = np.clip(model.lights_1_25, skylight, 1.0) * model.shading
    v_light_b = np.clip(model.skylights * (2.0 - daylight**2), model.lights, 1.0) * model.shading

    speedup.generate_faces_flat(
        model.indices, model.uv_indices, pts, model.uv_vertices, model.uv_index,
        model.texture_width, model.texture_height, pygame.surfarray.pixels2d(screen),
        v_light_r, v_light_g, v_light_b, model.texture_array, zbuffer, light_buffer, O2
    )  # 逐个绘制三角形
