import GL11
from typing import List
import math
import numpy as np


class Frustum:
    RIGHT: int = 0
    LEFT: int = 1
    BOTTOM: int = 2
    TOP: int = 3
    BACK: int = 4
    FRONT: int = 5
    A: int = 0
    B: int = 1
    C: int = 2
    D: int = 3
    frustum = None  # Frustum()

    def __init__(self):
        self.m_Frustum = [[0.0] * 4] * 6  # float[6][4]
        self._proj = np.zeros(16, dtype=np.float32)
        self._modl = np.zeros(16, dtype=np.float32)
        self._clip = np.zeros(16, dtype=np.float32)
        self.proj = [0.0] * 16  # float[16]
        self.modl = [0.0] * 16  # float[16]
        self.clip = [0.0] * 16  # float[16]
    
    @staticmethod
    def getFrustum():
        Frustum.frustum.calculateFrustum()
        return Frustum.frustum

    def normalizePlane(self, frustum: List[List[float]], side: int):
        magnitude: float = math.sqrt(frustum[side][0] ** 2 + \
                                     frustum[side][1] ** 2 + \
                                     frustum[side][2] ** 2)
        frustum[side][0] /= magnitude
        frustum[side][1] /= magnitude
        frustum[side][2] /= magnitude
        frustum[side][3] /= magnitude

    def calculateFrustum(self):
        # self._proj.clear()
        # self._modl.clear()
        # self._clip.clear()

        GL11.glGetFloat(GL11.GL_PROJECTION_MATRIX, self._proj)

        GL11.glGetFloat(GL11.GL_MODELVIEW_MATRIX, self._modl)

        # self._proj.flip().limit(16)
        # self._proj.get(self.proj)
        # self._modl.flip().limit(16)
        # self._modl.get(self.modl)
        self.proj = self._proj.tolist()
        self.modl = self._modl.tolist()

        self.clip[0] = self.modl[0] * self.proj[0] + \
                       self.modl[1] * self.proj[4] + \
                       self.modl[2] * self.proj[8] + \
                       self.modl[3] * self.proj[12]

        self.clip[1] = self.modl[0] * self.proj[1] + \
                       self.modl[1] * self.proj[5] + \
                       self.modl[2] * self.proj[9] + \
                       self.modl[3] * self.proj[13]
        
        self.clip[2] = self.modl[0] * self.proj[2] + \
                       self.modl[1] * self.proj[6] + \
                       self.modl[2] * self.proj[10] + \
                       self.modl[3] * self.proj[14]

        self.clip[3] = self.modl[0] * self.proj[3] + \
                       self.modl[1] * self.proj[7] + \
                       self.modl[2] * self.proj[11] + \
                       self.modl[3] * self.proj[15]

        self.clip[4] = self.modl[4] * self.proj[0] + \
                       self.modl[5] * self.proj[4] + \
                       self.modl[6] * self.proj[8] + \
                       self.modl[7] * self.proj[12]

        self.clip[5] = self.modl[4] * self.proj[1] + \
                       self.modl[5] * self.proj[5] + \
                       self.modl[6] * self.proj[9] + \
                       self.modl[7] * self.proj[13]

        self.clip[6] = self.modl[4] * self.proj[2] + \
                       self.modl[5] * self.proj[6] + \
                       self.modl[6] * self.proj[10] + \
                       self.modl[7] * self.proj[14]

        self.clip[7] = self.modl[4] * self.proj[3] + \
                       self.modl[5] * self.proj[7] + \
                       self.modl[6] * self.proj[11] + \
                       self.modl[7] * self.proj[15]

        self.clip[8] = self.modl[8] * self.proj[0] + \
                       self.modl[9] * self.proj[4] + \
                       self.modl[10] * self.proj[8] + \
                       self.modl[11] * self.proj[12]

        self.clip[9] = self.modl[8] * self.proj[1] + \
                       self.modl[9] * self.proj[5] + \
                       self.modl[10] * self.proj[9] + \
                       self.modl[11] * self.proj[13]

        self.clip[10] = self.modl[8] * self.proj[2] + \
                        self.modl[9] * self.proj[6] + \
                        self.modl[10] * self.proj[10] + \
                        self.modl[11] * self.proj[14]

        self.clip[11] = self.modl[8] * self.proj[3] + \
                        self.modl[9] * self.proj[7] + \
                        self.modl[10] * self.proj[11] + \
                        self.modl[11] * self.proj[15]

        self.clip[12] = self.modl[12] * self.proj[0] + \
                        self.modl[13] * self.proj[4] + \
                        self.modl[14] * self.proj[8] + \
                        self.modl[15] * self.proj[12]

        self.clip[13] = self.modl[12] * self.proj[1] + \
                        self.modl[13] * self.proj[5] + \
                        self.modl[14] * self.proj[9] + \
                        self.modl[15] * self.proj[13]

        self.clip[14] = self.modl[12] * self.proj[2] + \
                        self.modl[13] * self.proj[6] + \
                        self.modl[14] * self.proj[10] + \
                        self.modl[15] * self.proj[14]

        self.clip[15] = self.modl[12] * self.proj[3] + \
                        self.modl[13] * self.proj[7] + \
                        self.modl[14] * self.proj[11] + \
                        self.modl[15] * self.proj[15]

        self.m_Frustum[0][0] = (self.clip[3] - self.clip[0])
        self.m_Frustum[0][1] = (self.clip[7] - self.clip[4])
        self.m_Frustum[0][2] = (self.clip[11] - self.clip[8])
        self.m_Frustum[0][3] = (self.clip[15] - self.clip[12])

        self.normalizePlane(self.m_Frustum, 0)

        self.m_Frustum[1][0] = (self.clip[3] + self.clip[0])
        self.m_Frustum[1][1] = (self.clip[7] + self.clip[4])
        self.m_Frustum[1][2] = (self.clip[11] + self.clip[8])
        self.m_Frustum[1][3] = (self.clip[15] + self.clip[12])

        self.normalizePlane(self.m_Frustum, 1)

        self.m_Frustum[2][0] = (self.clip[3] + self.clip[1])
        self.m_Frustum[2][1] = (self.clip[7] + self.clip[5])
        self.m_Frustum[2][2] = (self.clip[11] + self.clip[9])
        self.m_Frustum[2][3] = (self.clip[15] + self.clip[13])

        self.normalizePlane(self.m_Frustum, 2)

        self.m_Frustum[3][0] = (self.clip[3] - self.clip[1])
        self.m_Frustum[3][1] = (self.clip[7] - self.clip[5])
        self.m_Frustum[3][2] = (self.clip[11] - self.clip[9])
        self.m_Frustum[3][3] = (self.clip[15] - self.clip[13])

        self.normalizePlane(self.m_Frustum, 3)

        self.m_Frustum[4][0] = (self.clip[3] - self.clip[2])
        self.m_Frustum[4][1] = (self.clip[7] - self.clip[6])
        self.m_Frustum[4][2] = (self.clip[11] - self.clip[10])
        self.m_Frustum[4][3] = (self.clip[15] - self.clip[14])

        self.normalizePlane(self.m_Frustum, 4)

        self.m_Frustum[5][0] = (self.clip[3] + self.clip[2])
        self.m_Frustum[5][1] = (self.clip[7] + self.clip[6])
        self.m_Frustum[5][2] = (self.clip[11] + self.clip[10])
        self.m_Frustum[5][3] = (self.clip[15] + self.clip[14])

        self.normalizePlane(self.m_Frustum, 5)

    def pointInFrustum(self, x: float, y: float, z: float) -> bool:
        for i in range(6):
            temp = self.m_Frustum[i][0] * x + \
                   self.m_Frustum[i][1] * y + \
                   self.m_Frustum[i][2] * z + \
                   self.m_Frustum[i][3]
            if temp <= 0.0:
                return False
        return True

    def sphereInFrustum(self, x: float, y: float, z: float, radius: float) -> bool:
        for i in range(6):
            temp = self.m_Frustum[i][0] * x + \
                   self.m_Frustum[i][1] * y + \
                   self.m_Frustum[i][2] * z + \
                   self.m_Frustum[i][3] 
            if temp <= -radius:
                return False
        return True

    def cubeFullyInFrustum(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> bool:
        for i in range(6):
            if self.m_Frustum[i][0] * x1 + self.m_Frustum[i][1] * y1 + self.m_Frustum[i][2] * z1 + self.m_Frustum[i][3] <= 0.0:
                return False
            if self.m_Frustum[i][0] * x2 + self.m_Frustum[i][1] * y1 + self.m_Frustum[i][2] * z1 + self.m_Frustum[i][3] <= 0.0:
                return False
            if self.m_Frustum[i][0] * x1 + self.m_Frustum[i][1] * y2 + self.m_Frustum[i][2] * z1 + self.m_Frustum[i][3] <= 0.0:
                return False
            if self.m_Frustum[i][0] * x2 + self.m_Frustum[i][1] * y2 + self.m_Frustum[i][2] * z1 + self.m_Frustum[i][3] <= 0.0:
                return False
            if self.m_Frustum[i][0] * x1 + self.m_Frustum[i][1] * y1 + self.m_Frustum[i][2] * z2 + self.m_Frustum[i][3] <= 0.0:
                return False
            if self.m_Frustum[i][0] * x2 + self.m_Frustum[i][1] * y1 + self.m_Frustum[i][2] * z2 + self.m_Frustum[i][3] <= 0.0:
                return False
            if self.m_Frustum[i][0] * x1 + self.m_Frustum[i][1] * y2 + self.m_Frustum[i][2] * z2 + self.m_Frustum[i][3] <= 0.0:
                return False
            if self.m_Frustum[i][0] * x2 + self.m_Frustum[i][1] * y2 + self.m_Frustum[i][2] * z2 + self.m_Frustum[i][3] <= 0.0:
                return False
        return True

    def cubeInFrustum(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> bool:
        for i in range(6):
            if (self.m_Frustum[i][0] * x1 + self.m_Frustum[i][1] * y1 + self.m_Frustum[i][2] * z1 + self.m_Frustum[i][3] <= 0.0) and (self.m_Frustum[i][0] * x2 + self.m_Frustum[i][1] * y1 + self.m_Frustum[i][2] * z1 + self.m_Frustum[i][3] <= 0.0) and (self.m_Frustum[i][0] * x1 + self.m_Frustum[i][1] * y2 + self.m_Frustum[i][2] * z1 + self.m_Frustum[i][3] <= 0.0) and (self.m_Frustum[i][0] * x2 + self.m_Frustum[i][1] * y2 + self.m_Frustum[i][2] * z1 + self.m_Frustum[i][3] <= 0.0) and (self.m_Frustum[i][0] * x1 + self.m_Frustum[i][1] * y1 + self.m_Frustum[i][2] * z2 + self.m_Frustum[i][3] <= 0.0) and (self.m_Frustum[i][0] * x2 + self.m_Frustum[i][1] * y1 + self.m_Frustum[i][2] * z2 + self.m_Frustum[i][3] <= 0.0) and (self.m_Frustum[i][0] * x1 + self.m_Frustum[i][1] * y2 + self.m_Frustum[i][2] * z2 + self.m_Frustum[i][3] <= 0.0) and (self.m_Frustum[i][0] * x2 + self.m_Frustum[i][1] * y2 + self.m_Frustum[i][2] * z2 + self.m_Frustum[i][3] <= 0.0):
                return False
        return True

    def isVisible(self, aabb):
        return self.cubeInFrustum(aabb.x0, aabb.y0, aabb.z0, 
                                  aabb.x1, aabb.y1, aabb.z1)


Frustum.frustum = Frustum()