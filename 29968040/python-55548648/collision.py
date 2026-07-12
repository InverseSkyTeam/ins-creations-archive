import numpy as np
import pygame


class Collision:
    def __init__(self, filename):
        self.vertices = []
        self.collision_pos = ()
        self.collision_n = ()

        with open(filename, encoding='utf-8') as f:
            for line in f:
                line = line.replace('  ', ' ')
                if line.startswith("v "):
                    x, y, z = [float(d) for d in line.strip("v").strip().split(" ")][:3]
                    self.vertices.append((-x, -z))
                elif line.startswith("l "):
                    a, b = [int(d)-1 for d in line.strip("l").strip().split(" ")][:2]
                    self.collision_pos += (self.vertices[a], self.vertices[b])
                    _x = self.vertices[a][0] - self.vertices[b][0]
                    _z = self.vertices[b][1] - self.vertices[a][1]
                    rsqrt = 1/np.sqrt(_x * _x + _z * _z)
                    self.collision_n += (_z * rsqrt, _x * rsqrt)
