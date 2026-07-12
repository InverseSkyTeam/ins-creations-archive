import numpy as np
import pygame


class Model:
    def __init__(self, filename, texture):
        self.vertices = []
        self.uv_vertices = []
        self.uv_indices = []
        self.indices = []

        sf = pygame.image.load(texture).convert()
        self.texture_array = pygame.surfarray.array2d(sf).T.copy(order='C')

        with open(filename, encoding='utf-8') as f:
            for line in f:
                line = line.replace('  ', ' ')
                if line.startswith("v "):
                    x, y, z = [float(d) for d in line.strip("v").strip().split(" ")][:3]
                    self.vertices.append(np.array([x, y, z, 1]))
                elif line.startswith("vt "):
                    u, v = [float(d) for d in line.strip("vt").strip().split(" ")][:2]
                    self.uv_vertices.append([u, 1-v])
                elif line.startswith("f "):
                    facet = [d.split("/") for d in line.strip("f").strip().split(" ")]
                    self.indices.append([int(d[0])-1 for d in facet])
                    self.uv_indices.append([int(d[1])-1 for d in facet])
        self.vertices = np.array(self.vertices, dtype=np.float64)
        self.uv_vertices = np.array(self.uv_vertices, dtype=np.float64)
        self.indices = np.array(self.indices, dtype=np.uint32)
        self.uv_indices = np.array(self.uv_indices, dtype=np.uint32)
