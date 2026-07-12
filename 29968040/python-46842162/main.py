import pygame
import numpy as np
import heapq
from numba import jit, prange
import platform,os,sys

opsystem_info = {
    'system_name': platform.system(),
    'username': os.getlogin(),
    'path': os.getcwd(),
}


# 定义立方体的8个顶点
vertices = np.array([[-1, -1, -1],
                     [1, -1, -1],
                     [1, 1, -1],
                     [-1, 1, -1],
                     [-1, -1, 1],
                     [1, -1, 1],
                     [1, 1, 1],
                     [-1, 1, 1]])

# 定义立方体的6个面，每个面是一个顶点索引的列表
faces = [(0, 1, 2, 3),
         (1, 5, 6, 2),
         (5, 4, 7, 6),
         (4, 0, 3, 7),
         (0, 4, 5, 1),
         (3, 2, 6, 7)]

# 加载纹理图片
texture = pygame.image.load('img.png')
texture_np = pygame.surfarray.array3d(texture)

# 定义光源位置
light = np.array([0, 0, 3])

def project(points, screen_width, screen_height, fov, viewer_distance):
    # 将三维点投影到二维屏幕上
    factor = fov / (viewer_distance + points[2])
    x = points[0] * factor + screen_width / 2
    y = -points[1] * factor + screen_height / 2
    return np.array([x, y, points[2]])  # 返回投影后的点及其z坐标

def rotate(points, angleX, angleY):
    # 绕y轴进行旋转变换
    rot_matrix_x = np.array([[1, 0, 0],
                             [0, np.cos(angleX), -np.sin(angleX)],
                             [0, np.sin(angleX), np.cos(angleX)]])
    rot_matrix_y = np.array([[np.cos(angleY), 0, np.sin(angleY)],
                             [0, 1, 0],
                             [-np.sin(angleY), 0, np.cos(angleY)]])
    return np.dot(np.dot(points, rot_matrix_y),rot_matrix_x)

@jit(nopython=True)
def point_in_polygon(x, y, polygon):
    # 判断点是否在多边形内部（假设多边形是凸多边形，且点在多边形的包围盒内部）
    inside = False
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]
        if y > min(y1, y2):
            if y <= max(y1, y2):
                if x <= max(x1, x2):
                    if y1 != y2:
                        xinters = (y - y1) * (x2 - x1) / (y2 - y1) + x1
                    if x1 == x2 or x <= xinters:
                        inside = not inside
    return inside

@jit(nopython=True)
def rasterize_polygon(screen_np, points, texture_np, min_x, max_x, min_y, max_y, intensity):
    # 对多边形内部的像素进行颜色填充
    for i in prange(min_x, max_x):
        for j in prange(min_y, max_y):
            if point_in_polygon(i, j, points):
                # 将像素映射到纹理上
                u = (i - min_x) / (max_x - min_x)
                v = (j - min_y) / (max_y - min_y)
                tex_x = int(u * texture_np.shape[0])
                tex_y = int(v * texture_np.shape[1])
                color = texture_np[tex_x, tex_y]
                screen_np[i, j] = np.clip(color * intensity, 0, 255)

def calculate_intensity(face, vertices, light):
    # 计算面的法向量
    normal = np.cross(vertices[face[1]] - vertices[face[0]], vertices[face[2]] - vertices[face[0]])
    normal = normal / np.linalg.norm(normal)  # 对法向量进行归一化

    # 计算从面到光源的向量
    face_center = np.mean([vertices[i] for i in face], axis=0)
    light_vector = light - face_center
    light_vector = light_vector / np.linalg.norm(light_vector)  # 对光源向量进行归一化

    # 计算光照强度
    intensity = np.dot(normal, light_vector)
    if intensity < 0:  # 面背向光源
        intensity = 0

    return intensity

def draw_cube(screen, vertices, faces, texture_np, angleX, angleY, screen_width, screen_height, fov, viewer_distance):
    # 对顶点进行旋转变换
    rotated_vertices = [rotate((x, y, z), angleX, angleY) for x, y, z in vertices]

    # 计算每个面的深度和光照强度
    depths = []
    intensities = []
    for face in faces:
        # 计算面的深度
        depths.append(sum(rotated_vertices[i][2] for i in face) / 4)

        # 计算光照强度
        intensities.append(calculate_intensity(face, rotated_vertices, light))

    # 将顶点投影到屏幕上
    projected_vertices = [project(v, screen_width, screen_height, fov, viewer_distance) for v in rotated_vertices]

    # 创建一个优先队列用于存储面
    face_queue = []

    # 更新优先队列
    for face, depth, intensity in zip(faces, depths, intensities):
        heapq.heappush(face_queue, (-depth, (face, intensity)))  # 使用负深度是因为heapq是最小堆

    # 绘制每个面
    screen_np = pygame.surfarray.array3d(screen)
    while face_queue:
        _, (face, intensity) = heapq.heappop(face_queue)
        points = [projected_vertices[i][:2] for i in face]  # 只使用x和y坐标进行绘制
        min_x = int(min(point[0] for point in points))
        max_x = int(max(point[0] for point in points))
        min_y = int(min(point[1] for point in points))
        max_y = int(max(point[1] for point in points))
        rasterize_polygon(screen_np, points, texture_np, min_x, max_x, min_y, max_y, intensity)
    pygame.surfarray.blit_array(screen, screen_np)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    def show_text(text,color=(0,0,0),pos=(0,0),size=30):
        if opsystem_info['system_name'] == 'Windows':
            screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)
        else:
            screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)
    
    clock = pygame.time.Clock()
    angle = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((255, 255, 255))
        draw_cube(screen, vertices, faces, texture_np, angle, 0.3, 800, 600, 800, 10)  # 增加viewer_distance到10
        show_text(f'FPS: {round(clock.get_fps())}',pos=(11,11),color=(0,0,0))
        pygame.display.flip()
        clock.tick(80)
        angle += 0.1

if __name__ == "__main__":
    main()
