import numpy as np
from PIL import Image
from numba import njit


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
        self.cube_num = 0
        self.mode = ['obj', 'cube'][0]

        with open(filename) as f:
            for line in f:
                line = line.replace('  ', ' ')
                if self.mode == 'cube':
                    # print(line, line.startswith("vt "))
                    if line.startswith("vt "):
                        u, v = [float(d) for d in line.strip("vt").strip().split(" ")][:2]
                        self.uv_vertices.append([u, 1-v])
                else:
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
            if self.mode == 'cube':
                self.add_cube(0, 0, 0)
                '''for yyy in range(0, -3, -1):
                    for xxx in range(-5, 5+1):
                        for zzz in range(-5, 5+1):
                            self.add_cube(xxx, yyy, zzz)'''
        self.vertices = np.array(self.vertices)
        self.indices = np.array(self.indices)
        self.uv_indices = np.array(self.uv_indices)
        self.uv_vertices = np.array(self.uv_vertices)
        print('总面数:', len(self.indices))

    def add_cube(self, x, y, z):
        xx = [-1, -1, -1, -1, 1, 1, 1, 1]
        yy = [-1, 1, -1, 1, 1, 1, -1, -1]
        zz = [1, -1, -1, 1, -1, 1, -1, 1]
        indices = [[1, 2, 3], [4, 5, 2], [6, 7, 5], [8, 3, 7], [5, 3, 2], [4, 8, 6], [1, 4, 2], [4, 6, 5], [6, 8, 7], [8, 1, 3], [5, 7, 3], [4, 1, 8]]
        uv_indices = [[1, 2, 3], [4, 5, 2], [6, 7, 5], [8, 9, 7], [5, 10, 11], [12, 8, 6], [1, 4, 2], [4, 6, 5], [6, 8, 7], [8, 13, 9], [5, 7, 10], [12, 14, 8]]
        for i in range(8):
            idx = xx[i] + 2*x
            idy = yy[i] + 2*y
            idz = zz[i] + 2*z
            self.vertices.append(np.array([[idx / 1], [idy / 1], [idz / 1], [1]]))
        for i in range(12):
            self.indices.append([xxx + self.cube_num*8 for xxx in indices[i]])
            self.uv_indices.append(uv_indices[i])
        self.cube_num += 1
