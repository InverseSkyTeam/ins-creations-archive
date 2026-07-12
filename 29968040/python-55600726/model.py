import numpy as np
import pygame


def read_img(path):
    sf = pygame.image.load(path).convert_alpha()
    bg = pygame.Surface(sf.get_size())
    bg.fill((0x99, 0x66, 0xff))
    bg.blit(sf, (0, 0))
    return pygame.surfarray.array2d(bg.convert()).T.copy(order='C')


class Model:
    def __init__(self, filename, texture, scale=1):
        self.vertices = []
        self.uv_vertices = []
        self.uv_indices = []
        self.indices = []

        self.texture_array = read_img(texture)

        with open(filename, encoding='utf-8') as f:
            for line in f:
                line = line.replace('  ', ' ')
                if line.startswith("v "):
                    x, y, z = [float(d) for d in line.strip("v").strip().split(" ")][:3]
                    self.vertices.append(np.array([x*scale, y*scale, z*scale, 1]))
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
