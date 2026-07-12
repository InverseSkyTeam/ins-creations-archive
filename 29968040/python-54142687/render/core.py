import speedup
import numpy as np
from numba import jit


#@jit(nopython=True, fastmath=True, looplift=True)
def light_calc_nb(skylights, daylight, shading, lights, lights_1_5, lights_1_25):
    _skylight = skylights * daylight
    v_light_r = np.maximum(lights_1_5, _skylight)
    v_light_g = np.maximum(lights_1_25, _skylight)
    v_light_b = np.clip(skylights * (2.0 - daylight ** 2), lights, shading)
    return v_light_r, v_light_g, v_light_b


def render_cube(model, color_buffer, zbuffer, final_matrix, daylight, light_buffer, O2=True):
    # 绘制 3d 模型
    # 初始化矩阵
    pts = np.matmul(model.vertices, final_matrix)
    v_light_r, v_light_g, v_light_b = light_calc_nb(model.skylights, daylight, model.shading, model.lights,
                                                    model.lights_1_5, model.lights_1_25)

    speedup.generate_faces_flat(
        model.indices, model.uv_indices, pts, model.uv_vertices, model.uv_index,
        model.texture_width, model.texture_height, color_buffer,
        v_light_r, v_light_g, v_light_b, model.texture_array, model.have_alpha,
        zbuffer, light_buffer, O2
    )  # 逐个绘制三角形
