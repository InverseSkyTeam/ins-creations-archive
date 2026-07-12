import numpy as np
from PIL import Image
import random
import os


def normalize(v):
    # 归一化操作
    unit = np.linalg.norm(v)
    if unit == 0:
        return np.zeros(3, dtype=np.float64)
    return v / unit


class Model:
    def __init__(self, filename, texture_filename, div_num=1):
        """
        https://en.wikipedia.org/wiki/Wavefront_.obj_file#Vertex_normal_indices
        """
        self.vertices = []
        self.uv_vertices = []
        self.norm_vertices = []
        self.uv_indices = []
        self.indices = []
        self.norm_indices = []
        self.div_num = div_num
        self.new = False

        texture = Image.open(texture_filename)
        self.texture_array = np.array(texture)
        self.texture_width, self.texture_height = texture.size

        with open(filename, encoding='utf-8') as f:
            for line in f:
                line = line.replace('  ', ' ')
                if line.startswith("v "):
                    x, y, z = [float(d) for d in line.strip("v").strip().split(" ")][:3]
                    self.vertices.append(np.array([[x/self.div_num], [y/self.div_num], [z/self.div_num], [1]]))
                elif line.startswith("vn "):
                    norm = [float(d) for d in line.strip("vn").strip().split(" ")][:3]
                    self.norm_vertices.append(normalize(np.array(norm, dtype=np.float64)))
                elif line.startswith("vt "):
                    u, v = [float(d) for d in line.strip("vt").strip().split(" ")][:2]
                    self.uv_vertices.append([u, 1-v])
                elif line.startswith("f "):
                    facet = [d.split("/") for d in line.strip("f").strip().split(" ")]
                    self.indices.append([int(d[0])-1 for d in facet])
                    self.uv_indices.append([int(d[1])-1 for d in facet])
                    self.norm_indices.append([int(d[2])-1 for d in facet])
        self.vertices = np.array(self.vertices)
        self.indices = np.array(self.indices)
        self.uv_indices = np.array(self.uv_indices)
        self.uv_vertices = np.array(self.uv_vertices)
        self.norm_indices = np.array(self.norm_indices)
        self.norm_vertices = np.array(self.norm_vertices)
        print(f'3D模型 {filename} 加载成功')
        print(f'3D纹理 {texture_filename} 加载成功')
        print('总面数:', len(self.indices))
        print('总顶点数:', len(self.vertices))
        print('--------------------------------')


class ModelNew:
    def __init__(self, filename, div_num=1):
        """
        https://en.wikipedia.org/wiki/Wavefront_.obj_file#Vertex_normal_indices
        """
        self.vertices = []
        self.uv_vertices = []
        self.norm_vertices = []
        self.uv_indices = []
        self.indices = []
        self.norm_indices = []
        self.div_num = div_num
        self.new = True

        face_names = []
        mtl_filename = None
        path = os.path.dirname(filename)

        with open(filename, encoding='utf-8') as f:
            for line in f:
                line = line.replace('  ', ' ')
                if line.startswith("v "):
                    x, y, z = [float(d) for d in line.strip("v").strip().split(" ")][:3]
                    self.vertices.append(np.array([[x/self.div_num], [y/self.div_num-1.1], [z/self.div_num], [1]]))
                elif line.startswith("vn "):
                    norm = [float(d) for d in line.strip("vn").strip().split(" ")][:3]
                    self.norm_vertices.append(normalize(np.array(norm, dtype=np.float64)))
                elif line.startswith("vt "):
                    u, v = [float(d) for d in line.strip("vt").strip().split(" ")][:2]
                    if u < 0:
                        u = 1-abs(u)
                    if v < 0:
                        v = 1-abs(v)
                    self.uv_vertices.append([u, 1-v])
                elif line.startswith("usemtl "):
                    self.indices.append([])
                    self.uv_indices.append([])
                    self.norm_indices.append([])
                    face_names.append(line.strip("usemtl").strip())
                elif line.startswith("f "):
                    facet = [d.split("/") for d in line.strip("f").strip().split(" ")]
                    self.indices[-1].append([int(d[0])-1 for d in facet])
                    self.uv_indices[-1].append([int(d[1])-1 for d in facet])
                    self.norm_indices[-1].append([int(d[2])-1 for d in facet])
                elif line.startswith("mtllib "):
                    mtl_filename = line.strip("mtllib").strip()

        self.texture = [None for _ in range(len(face_names))]

        with open(path + '/' + mtl_filename, encoding='utf-8') as f:
            pos = -1
            for line in f:
                line = line.replace('  ', ' ')
                if line.startswith("newmtl "):
                    pos: int = face_names.index(line.strip("newmtl").strip())
                elif line.startswith("map_Kd "):
                    name = line.strip("map_Kd").strip()
                    img = Image.open(path + '/' + name)
                    self.texture[pos] = np.array(img)
        self.vertices = np.array(self.vertices)
        self.uv_vertices = np.array(self.uv_vertices)
        self.norm_vertices = np.array(self.norm_vertices)
        for i in range(len(self.indices)):
            self.indices[i] = np.array(self.indices[i])
            self.uv_indices[i] = np.array(self.uv_indices[i])
            self.norm_indices[i] = np.array(self.norm_indices[i])
        print(f'3D模型 {filename} 加载成功')
        print('--------------------------------')
