import numpy as np
import pygame
import speedup


eye = np.array([0, 0, 3], dtype=np.float64)  # 相机位置
center = np.array([0, 0, 0], dtype=np.float64)  # 观察点的位置
up = np.array((0, 1, 0), dtype=np.float64)  # 相机朝向


def normalize(v):
    # 归一化操作
    unit = np.linalg.norm(v)
    if unit == 0:
        return np.zeros(3, dtype=np.float64)
    return v / unit


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


def zoom(scale):
    return np.array(
        [
            [scale, 0, 0, 0],
            [0, scale, 0, 0],
            [0, 0, scale, 0],
            [0, 0, 0, 1],
        ], dtype=np.float64
    )


def look_at(_eye: np.ndarray, _center: np.ndarray, _up: np.ndarray):
    """
    Args:
        _eye: 摄像机的世界坐标位置
        _center: 观察点的位置
        _up: 就是你想让摄像机立在哪个方向
    """
    z = normalize(_center - _eye)
    x = normalize(np.cross(_up, z))
    y = normalize(np.cross(z, x))

    Minv = np.array(
        [[*x, 0], [*y, 0], [*z, 0], [0, 0, 0, 1.0]],
        dtype=np.float64
    )
    Tr = np.array(
        [[1, 0, 0, -_eye[0]], [0, 1, 0, -_eye[1]], [0, 0, 1, -_eye[2]], [0, 0, 0, 1.0]],
        dtype=np.float64
    )

    return np.dot(Minv, Tr)


def perspective_project(f):
    return np.array(
        [
            [1,  0,    0, 0],
            [0, -1,    0, 0],
            [0,  0,    1, 0],
            [0,  0, -1/f, 0],
        ], dtype=np.float64
    )


def frustum_opengl(left, right, bottom, top, near, far):
    r_width = 1.0 / (right - left)
    r_height = 1.0 / (top - bottom)
    r_depth = 1.0 / (near - far)
    x = 2.0 * (near * r_width)
    y = 2.0 * (near * r_height)
    A = (right + left) * r_width
    B = (top + bottom) * r_height
    C = (far + near) * r_depth
    D = 2.0 * (far * near * r_depth)
    return np.array(
        [
            [x, 0, 0, 0],
            [0, -y, 0, 0],
            [A, B, C, -1],
            [0, 0, D, 0],
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


light_dirs = [normalize(np.array([1, 1, 1], dtype=np.float64)),
              normalize(np.array([0, 0, -1], dtype=np.float64))]


def render(model, height, width, screen, zbuffer, angle_x, angle_y, scale, mode, O2, tx, ty, tz):
    # 绘制 3d 模型
    transform_matrix = np.dot(
        translation(tx, ty, tz),
        np.dot(
            np.dot(
                rotate_x(angle_x), rotate_y(angle_y)
            ),
            zoom(scale)
        )
    )
    ModelView = look_at(eye, center, up)  # 模型矩阵
    Projection = perspective_project(np.linalg.norm(eye-center))  # 透视矩阵
    Viewport = viewport(width/8, height/8, width*3/4, height*3/4)  # 视口矩阵

    ModelView = np.dot(ModelView, transform_matrix)
    Projection_ModelView = np.dot(Projection, ModelView)  # 因为矩阵乘法满足结合律，可以进行预乘，以减少运算量
    Viewport_Projection_ModelView = np.dot(Viewport, Projection_ModelView)

    clip_vert = np.matmul(Projection_ModelView, model.vertices)[:, :, 0]  # 存储模型相机坐标系坐标，且进行透视
    pts = np.matmul(Viewport_Projection_ModelView, model.vertices)[:, :, 0]  # 存储屏幕坐标
    pts2 = pts[:, :2] / pts[:, 3][:, None]
    norm_vertices = np.zeros(model.norm_vertices.shape[0], dtype=np.float64)

    for light_dir in light_dirs:
        norm_vertices += np.maximum(np.dot(model.norm_vertices, light_dir), 0.0)

    if mode == 0:
        lines = pts2[model.indices].astype(int)
        lines[:, :, 1] = screen.get_height() - lines[:, :, 1] - 1
        lines[:, :, :] *= 2
        temp_surface = pygame.Surface((width*2, height*2), pygame.SRCALPHA)  # 暴力 SSAA
        speedup.render_lines(pygame.surfarray.pixels2d(temp_surface), lines)
        screen.blit(pygame.transform.smoothscale(temp_surface, (width, height)), (0, 0))
        # _ = [pygame.draw.aalines(screen, (0,) * 3, True, j) for j in lines]
    else:
        speedup.generate_faces_new(
            model.indices, model.uv_indices, model.norm_indices, pts2, pts,
            model.uv_vertices, clip_vert, norm_vertices,
            model.texture_width, model.texture_height, pygame.surfarray.pixels3d(screen),
            model.texture_array, zbuffer, O2
        )  # 逐个绘制三角形


def render_new(model, height, width, screen, zbuffer, angle_x, angle_y, scale, mode, O2, tx, ty, tz):
    # 绘制 3d 模型
    transform_matrix = np.dot(
        translation(tx, ty, tz),
        np.dot(
            np.dot(
                rotate_x(angle_x), rotate_y(angle_y)
            ),
            zoom(scale)
        )
    )
    ModelView = look_at(eye, center, up)  # 模型矩阵
    Projection = perspective_project(np.linalg.norm(eye-center))  # 透视矩阵
    Viewport = viewport(width/8, height/8, width*3/4, height*3/4)  # 视口矩阵

    ModelView = np.dot(ModelView, transform_matrix)
    Projection_ModelView = np.dot(Projection, ModelView)  # 因为矩阵乘法满足结合律，可以进行预乘，以减少运算量
    Viewport_Projection_ModelView = np.dot(Viewport, Projection_ModelView)

    clip_vert = np.matmul(Projection_ModelView, model.vertices)[:, :, 0]  # 存储模型相机坐标系坐标，且进行透视
    pts = np.matmul(Viewport_Projection_ModelView, model.vertices)[:, :, 0]  # 存储屏幕坐标
    pts2 = pts[:, :2] / pts[:, 3][:, None]
    norm_vertices = np.zeros(model.norm_vertices.shape[0], dtype=np.float64)

    for light_dir in light_dirs:
        norm_vertices += np.maximum(np.dot(model.norm_vertices, light_dir), 0.0)

    if mode == 0:
        for i in range(len(model.indices)):
            lines = pts2[model.indices[i]].astype(int)
            lines[:, :, 1] = screen.get_height() - lines[:, :, 1] - 1
            lines[:, :, :] *= 2
            temp_surface = pygame.Surface((width * 2, height * 2), pygame.SRCALPHA)  # 暴力 SSAA
            speedup.render_lines(pygame.surfarray.pixels2d(temp_surface), lines)
            screen.blit(pygame.transform.smoothscale(temp_surface, (width, height)), (0, 0))
    else:
        for i in range(len(model.indices)):
            speedup.generate_faces_new(
                model.indices[i], model.uv_indices[i], model.norm_indices[i], pts2, pts,
                model.uv_vertices, clip_vert, norm_vertices,
                model.texture[i].shape[1], model.texture[i].shape[0], pygame.surfarray.pixels3d(screen),
                model.texture[i], zbuffer, O2
            )  # 逐个绘制三角形
