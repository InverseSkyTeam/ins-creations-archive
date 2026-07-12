from config import Config as config
import math
import numpy as np
import pygame


def regenerateGlobe():
    segX = config.segX
    segY = config.segY

    vertices = []

    radius = 536 / 2

    phiStart = 0
    phiLength = math.pi * 2

    thetaStart = 0
    thetaLength = math.pi
    for y in range(segY + 1):
        vertices_row = []
        for x in range(segX + 1):
            u = x / segX
            v = 0.05 + y / segY * (1 - 0.1)

            vertex = {
                'x': -radius * math.cos(phiStart + u * phiLength) * math.sin(thetaStart + v * thetaLength),
                'y': -radius * math.cos(thetaStart + v * thetaLength),
                'z': radius * math.sin(phiStart + u * phiLength) * math.sin(thetaStart + v * thetaLength),
                'u': u,
                'v': 1 - v,
            }
            vertices_row.append(vertex)
        vertices.append(vertices_row)

    return vertices


class Model:
    def __init__(self, texture):
        self.vertices = []
        self.uv_vertices = []
        self.indices = []

        temp_vert = regenerateGlobe()

        for verticesRow in temp_vert:
            for vertex in verticesRow:
                self.vertices.append(np.array([vertex['x'], vertex['y'], vertex['z'], 1]))
                self.uv_vertices.append([vertex['u'], vertex['v']])
        for y in range(config.segY):
            for x in range(config.segX):
                tl = y * (config.segX + 1) + x
                tr = y * (config.segX + 1) + x + 1
                br = (y + 1) * (config.segX + 1) + x + 1
                bl = (y + 1) * (config.segX + 1) + x
                self.indices.append([tl, tr, br])
                self.indices.append([tl, br, bl])
        self.vertices = np.array(self.vertices, dtype=np.float64)
        self.uv_vertices = np.array(self.uv_vertices, dtype=np.float64)
        self.indices = np.array(self.indices, dtype=np.uint32)
        sf = pygame.image.load(texture).convert()
        self.texture_array = pygame.surfarray.array2d(sf).T.copy(order='C')
