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

        with open(filename) as f:
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
                    self.uv_vertices.append([u, v])
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
        self.uv_indices = {}
        self.indices = {}
        self.div_num = div_num
        self.new = True
        mtl_filename = None
        path = os.path.dirname(filename)

        self.texture = {}

        with open(filename, encoding='utf-8') as f:
            face_name = None
            for line in f:
                line = line.replace('  ', ' ')
                if line.startswith("v "):
                    x, y, z = [float(d) for d in line.strip("v").strip().split(" ")][:3]
                    self.vertices.append(np.array([[x/self.div_num], [y/self.div_num], [z/self.div_num], [1]]))
                elif line.startswith("vt "):
                    u, v = [float(d) for d in line.strip("vt").strip().split(" ")][:2]
                    if u < 0:
                        u = 1-abs(u)
                    if v < 0:
                        v = 1-abs(v)
                    self.uv_vertices.append([u, 1-v])
                elif line.startswith("usemtl "):
                    face_name = line.strip("usemtl").strip()
                    if face_name not in self.indices:
                        self.indices[face_name] = []
                        self.uv_indices[face_name] = []
                elif line.startswith("f "):
                    facet = [d.split("/") for d in line.strip("f").strip().split(" ")]
                    self.indices[face_name].append([int(d[0]) for d in facet])
                    self.uv_indices[face_name].append([int(d[1]) for d in facet])
                elif line.startswith("mtllib "):
                    mtl_filename = line.strip("mtllib").strip()

        with open(path + '/' + mtl_filename, encoding='utf-8') as f:
            face_name = None
            for line in f:
                line = line.replace('  ', ' ')
                if line.startswith("newmtl "):
                    face_name = line.strip("newmtl").strip()
                    if face_name not in self.texture:
                        self.texture[face_name] = None
                elif line.startswith("map_Kd "):
                    name = line.strip("map_Kd").strip()
                    img = Image.open(path + '/' + name)
                    self.texture[face_name] = np.array(img)
        self.vertices = np.array(self.vertices)
        self.uv_vertices = np.array(self.uv_vertices)
        for key in self.indices:
            self.indices[key] = np.array(self.indices[key])
            self.uv_indices[key] = np.array(self.uv_indices[key])
        print(f'3D模型 {filename} 加载成功')
        print('--------------------------------')


class CubeModel:
    def __init__(self, filename, texture_filename):
        """
        https://en.wikipedia.org/wiki/Wavefront_.obj_file#Vertex_normal_indices
        """
        self.vertices = []
        self.uv_vertices = []
        self.uv_indices = []
        self.indices = []
        self.indices_cube = []
        self.uv_indices_cube = []
        self.new = False

        texture = Image.open(texture_filename)
        self.texture_array = np.array(texture)
        self.texture_width, self.texture_height = texture.size
        self.cube_num = 0

        with open(filename) as f:
            for line in f:
                line = line.replace('  ', ' ')
                if line.startswith("vt "):
                    u, v = [float(d) for d in line.strip("vt").strip().split(" ")][:2]
                    self.uv_vertices.append([u, 1-v])
                if line.startswith("f "):
                    facet = [d.split("/") for d in line.strip("f").strip().split(" ")]
                    self.indices_cube.append([int(d[0]) for d in facet])
                    self.uv_indices_cube.append([int(d[1]) for d in facet])
            for yyy in range(0, -3, -1):
                for xxx in range(-5, 5+1):
                    for zzz in range(-5, 5+1):
                        if random.randint(0, 1000) > 900:
                            continue
                        self.add_cube(xxx, yyy, zzz)
        self.vertices = np.array(self.vertices)
        self.indices = np.array(self.indices)
        self.uv_indices = np.array(self.uv_indices)
        self.uv_vertices = np.array(self.uv_vertices)
        print('总面数:', len(self.indices))

    def add_cube(self, x, y, z):
        xx = [-1, -1, -1, -1, 1, 1, 1, 1]
        yy = [-1, 1, -1, 1, 1, 1, -1, -1]
        zz = [1, -1, -1, 1, -1, 1, -1, 1]
        indices = self.indices_cube
        uv_indices = self.uv_indices_cube
        for i in range(8):
            idx = xx[i] + 2*x
            idy = yy[i] + 2*y
            idz = zz[i] + 2*z
            self.vertices.append(np.array([[idx / 10], [idy / 10], [idz / 10], [1]]))
        for i in range(12):
            self.indices.append([xxx + self.cube_num*8 for xxx in indices[i]])
            self.uv_indices.append(uv_indices[i])
        self.cube_num += 1
