import numpy as np
import pygame


def normalize(v):
    # 归一化操作
    unit = np.linalg.norm(v)
    if unit == 0:
        return np.zeros(3, dtype=np.float64)
    return v / unit


class ModelOld:
    def __init__(self, filename, div_num=None, pos=None):
        self.vertices = []
        self.uv_vertices = []
        self.uv_indices = []
        self.indices = []
        self.div_num = div_num
        self.new = False

        self.texture_array = np.zeros((1, 1000, 700), dtype=np.uint32)
        self.texture_width, self.texture_height = 700, 1000

        with open(filename, encoding='utf-8') as f:
            for line in f:
                line = line.replace('  ', ' ')
                if line.startswith("v "):
                    x, y, z = [float(d) for d in line.strip("v").strip().split(" ")][:3]
                    self.vertices.append(np.array([[-x/2*self.div_num[0]+pos[0]], [-y/2*self.div_num[1]+pos[1]], [z+pos[2]-2], [1]]))
                elif line.startswith("vt "):
                    u, v = [float(d) for d in line.strip("vt").strip().split(" ")][:2]
                    self.uv_vertices.append([u, v])
                elif line.startswith("f "):
                    facet = [d.split("/") for d in line.strip("f").strip().split(" ")]
                    self.indices.append([int(d[0])-1 for d in facet])
                    self.uv_indices.append([int(d[1])-1 for d in facet])
        self.vertices = np.array(self.vertices)
        self.indices = np.array(self.indices)
        self.uv_indices = np.array(self.uv_indices)
        self.uv_vertices = np.array(self.uv_vertices)
        self.uv_index = np.zeros(2, dtype=np.uint32)


class WorldModel:
    def __init__(self, texture_manager, uv_vertices, uv_indices, is_focused=False):
        self.vertices = None
        self.uv_vertices = uv_vertices
        self.uv_indices = uv_indices
        self.uv_index = None
        self.indices = None

        self.texture_array = texture_manager.texture_array
        if is_focused:
            self.texture_array = texture_manager.texture_array_focused
        self.texture_width, self.texture_height = texture_manager.texture_width, texture_manager.texture_height
