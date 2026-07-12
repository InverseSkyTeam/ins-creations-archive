import numpy as np
from PIL import Image


class Model:
    def __init__(self, filename, texture_filename):
        """
        https://en.wikipedia.org/wiki/Wavefront_.obj_file#Vertex_normal_indices
        """
        self.vertices = []
        self.uv_vertices = []
        self.uv_indices = []
        self.indices = []

        texture = Image.open(texture_filename)
        self.texture_array = np.array(texture)
        self.texture_width, self.texture_height = texture.size

        with open(filename) as f:
            for line in f:
                line = line.replace('  ', ' ')
                if line.startswith("v "):
                    x, y, z = [float(d) for d in line.strip("v").strip().split(" ")]
                    self.vertices.append(np.array([[x], [y], [z], [1]]))
                elif line.startswith("vt "):
                    u, v = [float(d) for d in line.strip("vt").strip().split(" ")][:2]
                    self.uv_vertices.append([u, 1-v])
                elif line.startswith("f "):
                    facet = [d.split("/") for d in line.strip("f").strip().split(" ")]
                    self.indices.append([int(d[0]) for d in facet])
                    self.uv_indices.append([int(d[1]) for d in facet])
        self.vertices = np.array(self.vertices)
        self.indices = np.array(self.indices)
        self.uv_indices = np.array(self.uv_indices)
        self.uv_vertices = np.array(self.uv_vertices)
        print(f'3D模型 {filename} 加载成功')
        print(f'3D纹理 {texture_filename} 加载成功')
        print('总面数:', len(self.indices))
        print('总顶点数:', len(self.vertices))
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
                        if yyy == 0 and xxx == zzz:
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
