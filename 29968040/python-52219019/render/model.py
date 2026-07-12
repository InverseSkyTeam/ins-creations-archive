import numpy as np
from PIL import Image
import pygame
import os


def normalize(v):
    # 归一化操作
    unit = np.linalg.norm(v)
    if unit == 0:
        return np.zeros(3, dtype=np.float64)
    return v / unit


class NoneModel:
    def __init__(self, texture, vertices, uv_vertices, norms, uv_indices, indices):
        self.vertices = vertices
        self.uv_vertices = uv_vertices
        self.norms = norms
        self.uv_indices = uv_indices
        self.indices = indices

        self.texture_array = texture
        self.texture_width, self.texture_height = texture.shape[1], texture.shape[0]


class Cube:
    def __init__(self, filename, add, icon):
        """
        https://en.wikipedia.org/wiki/Wavefront_.obj_file#Vertex_normal_indices
        """
        self.vertices = []
        self.uv_indices = []
        self.indices = []
        self.icon = pygame.image.load(icon)
        self.add = 12 * add
        self.div_num = 2

        with open(filename) as f:
            for line in f:
                line = line.replace('  ', ' ')
                if line.startswith("v "):
                    x, y, z = [float(d) for d in line.strip("v").strip().split(" ")][:3]
                    self.vertices.append(np.array([[x/self.div_num], [y/self.div_num], [z/self.div_num], [1]]))
                elif line.startswith("f "):
                    facet = [d.split("/") for d in line.strip("f").strip().split(" ")]
                    self.indices.append([int(d[0])-1 for d in facet])
                    self.uv_indices.append([int(d[1])-1+self.add for d in facet])
        self.vertices = np.array(self.vertices)
        self.indices = np.array(self.indices)
        self.uv_indices = np.array(self.uv_indices)

        self.norms = np.empty((self.indices.shape[0], 3))
        for i, face in enumerate(self.indices):
            v1, v2, v3 = self.vertices[:, :3, 0][face]
            self.norms[i] = normalize(np.cross(v2 - v1, v3 - v1))


class Texture:
    def __init__(self, filename, texture_filename, texture_filename_focused):
        self.uv_vertices = []

        texture = Image.open(texture_filename)
        texture_focused = Image.open(texture_filename_focused)
        self.texture_array = np.array(texture)
        self.texture_array_focused = np.array(texture_focused)
        self.texture_width, self.texture_height = texture.size
        with open(filename, encoding='utf-8') as f:
            for line in f:
                line = line.replace('  ', ' ')
                if line.startswith("vt "):
                    u, v = [float(d) for d in line.strip("vt").strip().split(" ")][:2]
                    self.uv_vertices.append([u, 1-v])
        self.uv_vertices = np.array(self.uv_vertices)
