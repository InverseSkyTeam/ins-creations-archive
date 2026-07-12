import speedup
import numpy as np


def light_calc_np(skylights, daylight, shading, lights, lights_1_5, lights_1_25):
    _skylight = skylights * daylight
    v_light_r = np.maximum(lights_1_5, _skylight)
    v_light_g = np.maximum(lights_1_25, _skylight)
    v_light_b = np.clip(skylights * (2.0 - daylight ** 2), lights, shading)
    return v_light_r, v_light_g, v_light_b


def render_cube(model, screen, zbuffer, final_matrix, daylight, options, O2=True):
    # 绘制 3d 模型
    # 初始化矩阵
    pts = np.matmul(model.vertices, final_matrix)
    v_light_r, v_light_g, v_light_b = light_calc_np(model.skylights, daylight, model.shading, model.lights,
                                                    model.lights_1_5, model.lights_1_25)

    if options.EARLY_Z:
        z_sorted = np.argsort(pts[model.sort_indices, 2], kind=options.EARLY_Z_ALGORITHM)  # early-z
    else:
        z_sorted = model.sort_indices_no_early_z

    if options.PARALLEL:
        speedup.generate_faces_parallel(
            screen, z_sorted, model.indices, model.uv_indices, pts, model.uv_vertices,
            model.uv_index, model.texture_width, model.texture_height,
            v_light_r, v_light_g, v_light_b, model.texture_array,
            zbuffer, O2
        )  # 逐个绘制三角形
    else:
        speedup.generate_faces(
            screen, z_sorted, model.indices, model.uv_indices, pts, model.uv_vertices,
            model.uv_index, model.texture_width, model.texture_height,
            v_light_r, v_light_g, v_light_b, model.texture_array,
            zbuffer, O2
        )  # 逐个绘制三角形
