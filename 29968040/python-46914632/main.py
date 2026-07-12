import pygame
import numpy as np
from numba import jit, prange, njit
import platform,os,sys

opsystem_info = {
    'system_name': platform.system(),
    'username': os.getlogin(),
    'path': os.getcwd(),
}

MINN=-float('inf')
MAXN=float('inf')

# 定义立方体的8个顶点
vertices = np.array([[-1, -1, -1],
                     [1, -1, -1],
                     [1, 1, -1],
                     [-1, 1, -1],
                     [-1, -1, 1],
                     [1, -1, 1],
                     [1, 1, 1],
                     [-1, 1, 1]])

# 定义立方体的6个面(但是因为只能渲染三角形，所以分割成12个面)，每个面是一个顶点索引的列表
faces = np.array([[0, 1, 2],
                  [0, 2, 3],
                  [1, 5, 6],
                  [1, 6, 2],
                  [5, 4, 7],
                  [5, 7, 6],
                  [4, 0, 3],
                  [4, 3, 7],
                  [0, 4, 5],
                  [0, 5, 1],
                  [3, 2, 6],
                  [3, 6, 7]])

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
    return np.array([x, y, -points[2]])  # 返回投影后的点及其z坐标

def rotate(points, angleX, angleY):
    # 绕x和y轴进行旋转变换
    rot_matrix_x = np.array([[1, 0, 0],
                             [0, np.cos(angleX), -np.sin(angleX)],
                             [0, np.sin(angleX), np.cos(angleX)]])
    rot_matrix_y = np.array([[np.cos(angleY), 0, np.sin(angleY)],
                             [0, 1, 0],
                             [-np.sin(angleY), 0, np.cos(angleY)]])
    return np.dot(np.dot(points, rot_matrix_y),rot_matrix_x)

def create_pos(a, b, c, d):
    #生成包围框里所有可能的坐标
    arr = np.mgrid[a:b + 1, c:d + 1].reshape(2, -1).T
    return arr

def barycentric_array(points,c):
    #批量计算三角形的重心
    a = np.column_stack((np.full(c.shape[0], points[2][0]-points[0][0]), np.full(c.shape[0], points[1][0]-points[0][0]), points[0][0]-c[:, 0]))
    b = np.column_stack((np.full(c.shape[0], points[2][1]-points[0][1]), np.full(c.shape[0], points[1][1]-points[0][1]), points[0][1]-c[:, 1]))
    u = np.cross(a,b)
    bool_arr=np.abs(u[:, 2])>1e-2
    u[:,0],u[:,1],u[:,2] = 1-(u[:,0]+u[:,1])/u[:,2], u[:,1]/u[:,2], u[:,0]/u[:,2]
    return np.where(bool_arr[:,None], u, np.array([float(-1),float(1),float(1)]))

def rasterize_polygon_fast(screen_width, screen_height, screen_np, z_buffer, points, texture_np, intensity):
    bboxmin=[MAXN,MAXN]
    bboxmax=[MINN,MINN]
    clamp=[screen_width-1,screen_height-1]
    for i in prange(3):
        for j in prange(2):
            bboxmin[j] = max(0,        min(bboxmin[j],points[i][j]))
            bboxmax[j] = min(clamp[j], max(bboxmax[j],points[i][j]))
    pos=create_pos(int(bboxmin[0]), int(bboxmax[0]), int(bboxmin[1]), int(bboxmax[1]))
    bc_screen=barycentric_array(points, pos)
    #print(bc_screen)
    bool_draw = np.all(bc_screen >= 0, axis=1)
    poss=pos[bool_draw]
    zs=np.sum(points[:, 2] * bc_screen[bool_draw],axis=1)
    
    update_mask = z_buffer[poss[:, 0], poss[:, 1]] < zs
    updated_pixels = np.where(update_mask) # 获取需要更新的像素索引
    
    z_buffer[poss[updated_pixels][:,0], poss[updated_pixels][:,1]] = zs[updated_pixels]
    screen_np[poss[updated_pixels][:,0], poss[updated_pixels][:,1]] = np.clip(np.array([255,255,255]) * intensity, 0, 255)
    
@njit()
def barycentric(points,i,j):
    #计算三角形的重心
    u=np.cross(np.array([points[2][0]-points[0][0], points[1][0]-points[0][0], points[0][0]-i]), np.array([points[2][1]-points[0][1], points[1][1]-points[0][1], points[0][1]-j]))
    if np.abs(u[2])>1e-2:
        return np.array([1-(u[0]+u[1])/u[2],u[1]/u[2],u[0]/u[2]])
    return np.array([float(-1),float(1),float(1)])

@jit(nopython=True)
def rasterize_polygon(screen_width, screen_height, screen_np, z_buffer, points, texture_np, intensity):
    bboxmin=[MAXN,MAXN]
    bboxmax=[MINN,MINN]
    clamp=[screen_width-1,screen_height-1]
    for i in prange(3):
        for j in prange(2):
            bboxmin[j] = max(0,        min(bboxmin[j],points[i][j]))
            bboxmax[j] = min(clamp[j], max(bboxmax[j],points[i][j]))
    
    # 对多边形内部的像素进行颜色填充
    for i in prange(bboxmin[0], bboxmax[0]+1):
        for j in prange(bboxmin[1], bboxmax[1]+1):
            # 将像素映射到纹理上
            bc_screen=barycentric(points,i,j)
            if bc_screen[0]<0 or bc_screen[1]<0 or bc_screen[2]<0:
                continue
            z=np.sum(points[:, 2] * bc_screen)
            if z_buffer[i, j]<z:
                z_buffer[i, j]=z
                screen_np[i, j] = np.clip(np.array([255,255,255]) * intensity, 0, 255)

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

    return intensity

def draw_cube(screen, vertices, faces, texture_np, angleX, angleY, screen_width, screen_height, fov, viewer_distance):
    # 对顶点进行旋转变换
    rotated_vertices = [rotate((x, y, z), angleX, angleY) for x, y, z in vertices]
    
    # 将顶点投影到屏幕上
    projected_vertices = np.array([project(v, screen_width, screen_height, fov, viewer_distance) for v in rotated_vertices])
    
    # 计算每个面的深度和光照强度
    intensities = []
    for face in faces:
        # 计算光照强度
        intensities.append(calculate_intensity(face, rotated_vertices, light))
    
    # 绘制每个面
    screen_np = np.zeros((screen_width,screen_height,3),dtype='uint8')
    z_buffer = np.full((screen_width,screen_height),MINN)
    for i in range(len(faces)):
        face, intensity = faces[i], intensities[i]
        if intensity < 0:
            continue
        points = projected_vertices[face]#[projected_vertices[i] for i in face]  # 只使用x和y坐标进行绘制
        rasterize_polygon_fast(screen_width, screen_height, screen_np, z_buffer, points, texture_np, intensity)
    
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

        screen.fill((0, 0, 0))
        draw_cube(screen, vertices, faces, texture_np, angle, 0.3, 800, 600, 800, 20)  # 增加viewer_distance到20
        show_text(f'FPS: {round(clock.get_fps())}',pos=(11,11),color=(255,0,0))
        pygame.display.flip()
        clock.tick(80)
        angle += 0.05

if __name__ == "__main__":
    main()
