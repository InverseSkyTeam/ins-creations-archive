import numpy as np
import math
from collections import defaultdict


def find_unique_indices(arr, decimal=3):
    """
    找出三维数组中不重复的一级子列表的索引
    
    参数:
    arr (np.ndarray): 三维数组，形状为(n, m, k)
    decimal (int): 浮点数比较时四舍五入的小数位数
    
    返回:
    list: 不重复元素的索引列表，按升序排序
    """
    # 对数组进行四舍五入处理（考虑浮点数容差）
    arr_rounded = np.around(arr, decimals=decimal)
    
    # 使用字典记录每个签名对应的索引列表
    signature_dict = defaultdict(list)
    
    # 遍历每个一级子列表
    for i, sub_arr in enumerate(arr_rounded):
        # 将子列表中的每个向量转换为元组
        tuple_list = [tuple(vector) for vector in sub_arr]
        # 对元组列表排序（忽略内部顺序）
        tuple_list_sorted = sorted(tuple_list)
        # 创建签名（不可变的元组）
        signature = tuple(tuple_list_sorted)
        
        # 记录当前索引
        signature_dict[signature].append(i)
    
    # 收集所有只出现一次的索引
    unique_indices = []
    for indices in signature_dict.values():
        if len(indices) == 1:  # 只出现一次的元素
            unique_indices.append(indices[0])
    
    # 按索引升序排序
    unique_indices.sort()
    return unique_indices


def normalize(v):
    # 归一化操作
    unit = np.linalg.norm(v)
    if unit == 0:
        return np.zeros(v.shape[0], dtype=np.float64)
    return v / unit


def gluPerspective(fov, aspect, near, far):
    ymax = near * math.tan(fov * math.pi / 360)
    ymin = -ymax
    xmin = ymin * aspect
    xmax = -xmin
    return np.array(
        [
            [(2*near)/(xmax-xmin), 0, (xmax+xmin)/(xmax-xmin), 0],
            [0,  (2*near)/(ymax-ymin), (ymax+ymin)/(ymax-ymin), 0],
            [0,  0, -((far+near)/(far-near)), -((2*far*near)/(far-near))],
            [0,  0, -1, 0],
        ], dtype=np.float64
    )


def glRotatef(angle, x, y, z):
    x, y, z = normalize(np.array([x, y, z], dtype=np.float64))
    alpha = angle
    s = np.sin(alpha)
    c = np.cos(alpha)
    t = 1.0 - c
    return np.array(
        [
            [t * x * x + c, t * x * y + s * z, t * x * z - s * y, 0],
            [t * x * y - s * z, t * y * y + c, t * y * z + s * x, 0],
            [t * x * z + s * y, t * y * z - s * x, t * z * z + c, 0],
            [0, 0, 0, 1],
        ], dtype=np.float64
    ).T


def glTranslate(vec):
    return np.array(
        [
            [1, 0, 0, vec[0]],
            [0, 1, 0, vec[1]],
            [0, 0, 1, vec[2]],
            [0, 0, 0, 1],
        ], dtype=np.float64
    )


def glViewport(x, y, w, h):
    return np.array(
        [
            [w/2, 0, 0, x+w/2],
            [0, h/2, 0, y+h/2],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ], dtype=np.float64
    )


def calc_matrix(screen_size, rotation):
    w, h = screen_size
    p_matrix_np = gluPerspective(90, float(w) / h, 0.1, 500)
    mv_matrix_np = np.dot(glRotatef(rotation[0], -1, 0, 0),
                          glRotatef(rotation[1], 0, 1, 0))
    mv_matrix_np = np.dot(glTranslate([0, 0, -4]), mv_matrix_np)
    mvp_matrix_np = np.dot(p_matrix_np, mv_matrix_np)
    viewport = glViewport(0, 0, w, h)
    final_matrix = np.dot(viewport, mvp_matrix_np).T
    return final_matrix


def shoelace(v):
    area = 0.0
    for i in range(4):
        j = (i + 1) % 4
        area += v[i][0] * v[j][1]
        area -= v[i][1] * v[j][0]
    return area


def render_cube(screen, screen_size, texture_manager, rotation, cube):
    vertices = []
    tex_indices = []
    for _cube in cube:
        vertices += [_cube.get_vertices()]
        tex_indices += [_cube.block_type.tex_indices]
    vertices = np.concatenate(vertices, axis=0).astype(np.float64)
    tex_indices = np.concatenate(tex_indices, axis=0).astype(np.uint32)

    final_matrix = calc_matrix(screen_size, rotation)
    pts = np.matmul(vertices, final_matrix)
    pts[:, :, 0] /= pts[:, :, 3]
    pts[:, :, 1] /= pts[:, :, 3]
    
    index = find_unique_indices(pts)
    pts = pts[index]
    tex_indices = tex_indices[index]
    
    borders = []
    texs = []
    zs = []
    for i in range(len(tex_indices)):
        border = [(p[0], p[1]) for p in pts[i]]
        if -shoelace(border) < 1e-3:
            continue
        texs += [texture_manager.texture_array[tex_indices[i]]]
        borders += [border]
        z = [p[2] for p in pts[i]]
        zs += [sum(z) / len(z)]

    for i in reversed(np.argsort(zs)):
        texs[i].render(screen, borders[i])
        
