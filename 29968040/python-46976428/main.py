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
vertices = np.array([[1.07, 1, 1.07],
                        [1, 1.1, 1],
                        [0, 1.1, 1.4],
                        [0, 1, 1.5],
                        [0.99, 1, 0.99],
                        [0, 1, 1.4],
                        [1.5, 1, 0],
                        [1.4, 1.1, 0],
                        [1.4, 1, 0],
                        [-1.07, 1, 1.07],
                        [-1, 1.1, 1],
                        [-1.4, 1.1, 0],
                        [-1.5, 1, 0],
                        [-0.99, 1, 0.99],
                        [-1.4, 1, 0],
                        [-1.07, 1, -1.07],
                        [-1, 1.1, -1],
                        [0, 1.1, -1.4],
                        [0, 1, -1.5],
                        [-0.99, 1, -0.99],
                        [0, 1, -1.4],
                        [1.07, 1, -1.07],
                        [1, 1.1, -1],
                        [0.99, 1, -0.99],
                        [1.42, -0.5, 1.42],
                        [1.31, 0.22, 1.31],
                        [0, 0.22, 1.84],
                        [0, -0.5, 2],
                        [2, -0.5, 0],
                        [1.84, 0.22, 0],
                        [-1.42, -0.5, 1.42],
                        [-1.31, 0.22, 1.31],
                        [-1.84, 0.22, 0],
                        [-2, -0.5, 0],
                        [-1.42, -0.5, -1.42],
                        [-1.31, 0.22, -1.31],
                        [0, 0.22, -1.84],
                        [0, -0.5, -2],
                        [1.42, -0.5, -1.42],
                        [1.31, 0.22, -1.31],
                        [1.07, -1.25, 1.07],
                        [1.24, -1.02, 1.24],
                        [0, -1.02, 1.75],
                        [0, -1.25, 1.5],
                        [1.5, -1.25, 0],
                        [1.75, -1.02, 0],
                        [-1.07, -1.25, 1.07],
                        [-1.24, -1.02, 1.24],
                        [-1.75, -1.02, 0],
                        [-1.5, -1.25, 0],
                        [-1.07, -1.25, -1.07],
                        [-1.24, -1.02, -1.24],
                        [0, -1.02, -1.75],
                        [0, -1.25, -1.5],
                        [1.07, -1.25, -1.07],
                        [1.24, -1.02, -1.24],
                        [-2.85, 0.4, 0.23],
                        [-2.52, 0.7, 0.23],
                        [-2.62, 0.79, 0],
                        [-3, 0.4, 0],
                        [-1.55, 0.74, 0.23],
                        [-1.5, 0.85, 0],
                        [-2.7, 0.4, 0],
                        [-2.41, 0.6, 0],
                        [-1.6, 0.63, 0],
                        [-2.85, 0.4, -0.23],
                        [-2.52, 0.7, -0.23],
                        [-1.55, 0.74, -0.23],
                        [-1.95, -0.65, 0.23],
                        [-2.63, -0.15, 0.23],
                        [-2.73, -0.24, 0],
                        [-1.9, -0.8, 0],
                        [-2.54, -0.05, 0],
                        [-1.95, -0.65, -0.23],
                        [-2.63, -0.15, -0.23],
                        [3, 1, 0.19],
                        [2.54, 0.22, 0.34],
                        [2.69, 0.04, 0],
                        [3.3, 1, 0],
                        [1.7, -0.39, 0.5],
                        [1.7, -0.8, 0],
                        [2.7, 1, 0],
                        [2.39, 0.4, 0],
                        [1.7, 0.02, 0],
                        [3, 1, -0.19],
                        [2.54, 0.22, -0.34],
                        [1.7, -0.39, -0.5],
                        [3, 1, 0.11],
                        [3.13, 1.07, 0.15],
                        [3.43, 1.08, 0],
                        [3.2, 1, 0],
                        [2.8, 1, 0],
                        [2.82, 1.06, 0],
                        [3, 1, -0.11],
                        [3.13, 1.07, -0.15],
                        [0.14, 1.3, 0.14],
                        [0.23, 1.58, 0.23],
                        [0, 1.58, 0.33],
                        [0, 1.3, 0.2],
                        [0, 1.75, 0],
                        [0.2, 1.3, 0],
                        [0.33, 1.58, 0],
                        [-0.14, 1.3, 0.14],
                        [-0.23, 1.58, 0.23],
                        [-0.33, 1.58, 0],
                        [-0.2, 1.3, 0],
                        [-0.14, 1.3, -0.14],
                        [-0.23, 1.58, -0.23],
                        [0, 1.58, -0.33],
                        [0, 1.3, -0.2],
                        [0.14, 1.3, -0.14],
                        [0.23, 1.58, -0.23],
                        [0.92, 1, 0.92],
                        [0.59, 1.15, 0.59],
                        [0, 1.15, 0.83],
                        [0, 1, 1.3],
                        [1.3, 1, 0],
                        [0.83, 1.15, 0],
                        [-0.92, 1, 0.92],
                        [-0.59, 1.15, 0.59],
                        [-0.83, 1.15, 0],
                        [-1.3, 1, 0],
                        [-0.92, 1, -0.92],
                        [-0.59, 1.15, -0.59],
                        [0, 1.15, -0.83],
                        [0, 1, -1.3],
                        [0.92, 1, -0.92],
                        [0.59, 1.15, -0.59],
                        [0.91, -1.35, -0.91],
                        [0, -1.35, -1.28],
                        [0, -1.4, 0],
                        [1.28, -1.35, 0],
                        [-0.91, -1.35, -0.91],
                        [-1.28, -1.35, 0],
                        [-0.91, -1.35, 0.91],
                        [0, -1.35, 1.28],
                        [0.91, -1.35, 0.91]])

# 定义立方体的6个面(但是因为只能渲染三角形，所以分割成12个面)，每个面是一个顶点索引的列表
faces = np.array([[0, 1, 2],
[0, 2, 3],
[1, 4, 5],
[1, 5, 2],
[6, 7, 1],
[6, 1, 0],
[7, 8, 4],
[7, 4, 1],
[9, 10, 11],
[9, 11, 12],
[10, 13, 14],
[10, 14, 11],
[3, 2, 10],
[3, 10, 9],
[2, 5, 13],
[2, 13, 10],
[15, 16, 17],
[15, 17, 18],
[16, 19, 20],
[16, 20, 17],
[12, 11, 16],
[12, 16, 15],
[11, 14, 19],
[11, 19, 16],
[21, 22, 7],
[21, 7, 6],
[22, 23, 8],
[22, 8, 7],
[18, 17, 22],
[18, 22, 21],
[17, 20, 23],
[17, 23, 22],
[24, 25, 26],
[24, 26, 27],
[25, 0, 3],
[25, 3, 26],
[28, 29, 25],
[28, 25, 24],
[29, 6, 0],
[29, 0, 25],
[30, 31, 32],
[30, 32, 33],
[31, 9, 12],
[31, 12, 32],
[27, 26, 31],
[27, 31, 30],
[26, 3, 9],
[26, 9, 31],
[34, 35, 36],
[34, 36, 37],
[35, 15, 18],
[35, 18, 36],
[33, 32, 35],
[33, 35, 34],
[32, 12, 15],
[32, 15, 35],
[38, 39, 29],
[38, 29, 28],
[39, 21, 6],
[39, 6, 29],
[37, 36, 39],
[37, 39, 38],
[36, 18, 21],
[36, 21, 39],
[40, 41, 42],
[40, 42, 43],
[41, 24, 27],
[41, 27, 42],
[44, 45, 41],
[44, 41, 40],
[45, 28, 24],
[45, 24, 41],
[46, 47, 48],
[46, 48, 49],
[47, 30, 33],
[47, 33, 48],
[43, 42, 47],
[43, 47, 46],
[42, 27, 30],
[42, 30, 47],
[50, 51, 52],
[50, 52, 53],
[51, 34, 37],
[51, 37, 52],
[49, 48, 51],
[49, 51, 50],
[48, 33, 34],
[48, 34, 51],
[54, 55, 45],
[54, 45, 44],
[55, 38, 28],
[55, 28, 45],
[53, 52, 55],
[53, 55, 54],
[52, 37, 38],
[52, 38, 55],
[56, 57, 58],
[56, 58, 59],
[57, 60, 61],
[57, 61, 58],
[62, 63, 57],
[62, 57, 56],
[63, 64, 60],
[63, 60, 57],
[65, 66, 63],
[65, 63, 62],
[66, 67, 64],
[66, 64, 63],
[59, 58, 66],
[59, 66, 65],
[58, 61, 67],
[58, 67, 66],
[68, 69, 70],
[68, 70, 71],
[69, 56, 59],
[69, 59, 70],
[33, 72, 69],
[33, 69, 68],
[72, 62, 56],
[72, 56, 69],
[73, 74, 72],
[73, 72, 33],
[74, 65, 62],
[74, 62, 72],
[71, 70, 74],
[71, 74, 73],
[70, 59, 65],
[70, 65, 74],
[75, 76, 77],
[75, 77, 78],
[76, 79, 80],
[76, 80, 77],
[81, 82, 76],
[81, 76, 75],
[82, 83, 79],
[82, 79, 76],
[84, 85, 82],
[84, 82, 81],
[85, 86, 83],
[85, 83, 82],
[78, 77, 85],
[78, 85, 84],
[77, 80, 86],
[77, 86, 85],
[87, 88, 89],
[87, 89, 90],
[88, 75, 78],
[88, 78, 89],
[91, 92, 88],
[91, 88, 87],
[92, 81, 75],
[92, 75, 88],
[93, 94, 92],
[93, 92, 91],
[94, 84, 81],
[94, 81, 92],
[90, 89, 94],
[90, 94, 93],
[89, 78, 84],
[89, 84, 94],
[95, 96, 97],
[95, 97, 98],
[96, 99, 97],
[100, 101, 96],
[100, 96, 95],
[101, 99, 96],
[102, 103, 104],
[102, 104, 105],
[103, 99, 104],
[98, 97, 103],
[98, 103, 102],
[97, 99, 103],
[106, 107, 108],
[106, 108, 109],
[107, 99, 108],
[105, 104, 107],
[105, 107, 106],
[104, 99, 107],
[110, 111, 101],
[110, 101, 100],
[111, 99, 101],
[109, 108, 111],
[109, 111, 110],
[108, 99, 111],
[112, 113, 114],
[112, 114, 115],
[113, 95, 98],
[113, 98, 114],
[116, 117, 113],
[116, 113, 112],
[117, 100, 95],
[117, 95, 113],
[118, 119, 120],
[118, 120, 121],
[119, 102, 105],
[119, 105, 120],
[115, 114, 119],
[115, 119, 118],
[114, 98, 102],
[114, 102, 119],
[122, 123, 124],
[122, 124, 125],
[123, 106, 109],
[123, 109, 124],
[121, 120, 123],
[121, 123, 122],
[120, 105, 106],
[120, 106, 123],
[126, 127, 117],
[126, 117, 116],
[127, 110, 100],
[127, 100, 117],
[125, 124, 127],
[125, 127, 126],
[124, 109, 110],
[124, 110, 127],
[54, 128, 129],
[54, 129, 53],
[128, 130, 129],
[44, 131, 128],
[44, 128, 54],
[131, 130, 128],
[50, 132, 133],
[50, 133, 49],
[132, 130, 133],
[53, 129, 132],
[53, 132, 50],
[129, 130, 132],
[46, 134, 135],
[46, 135, 43],
[134, 130, 135],
[49, 133, 134],
[49, 134, 46],
[133, 130, 134],
[40, 136, 131],
[40, 131, 44],
[136, 130, 131],
[43, 135, 136],
[43, 136, 40],
[135, 130, 136]])

# 加载纹理图片
texture = pygame.image.load('img.png')
texture_np = pygame.surfarray.array3d(texture)

# 定义光源位置
light = np.array([0, 0, -5])

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
    u[bool_arr,0],u[bool_arr,1],u[bool_arr,2] = 1-(u[bool_arr,0]+u[bool_arr,1])/u[bool_arr,2], u[bool_arr,1]/u[bool_arr,2], u[bool_arr,0]/u[bool_arr,2]
    u[~bool_arr] = np.array([float(-1), float(1), float(1)])
    return u
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
    light_vector = light*3 - face_center
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
    draw_num=0
    for i in range(len(faces)):
        face, intensity = faces[i], intensities[i]
        if intensity < 0:
            continue
        draw_num+=1
        points = projected_vertices[face]#[projected_vertices[i] for i in face]  # 只使用x和y坐标进行绘制
        rasterize_polygon_fast(screen_width, screen_height, screen_np, z_buffer, points, texture_np, intensity)
    
    pygame.surfarray.blit_array(screen, screen_np)
    return draw_num
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
        a=draw_cube(screen, vertices, faces, texture_np, 0, angle, 800, 600, 800, 20)  # 增加viewer_distance到20
        show_text(f'FPS: {round(clock.get_fps())}'+'    实际渲染图形数量：'+str(a),pos=(11,11),color=(255,0,0))
        pygame.display.flip()
        clock.tick(80)
        angle += 0.05

if __name__ == "__main__":
    main()
