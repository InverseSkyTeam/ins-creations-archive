import GL11
from .Vertex import Vertex
from .Polygon import Polygon
from typing import List


class Cube:
    def __init__(self, xTexOffs: int, yTexOffs: int):
        self.vertices: list = None
        self.polygons: list = None
        self.x: float = 0.0
        self.y: float = 0.0
        self.z: float = 0.0
        self.xRot: float = 0.0
        self.yRot: float = 0.0
        self.zRot: float = 0.0
        self.compiled: bool = False
        self.list: int = 0
        self.xTexOffs: int = xTexOffs
        self.yTexOffs: int = yTexOffs

    def setTexOffs(self, xTexOffs: int, yTexOffs: int):
        self.xTexOffs: int = xTexOffs
        self.yTexOffs: int = yTexOffs

    def addBox(self, x0: float, y0: float, z0: float, w: int, h: int, d: int):
        self.vertices = [None] * 8
        self.polygons = [None] * 6

        x1: float = x0 + w
        y1: float = y0 + h
        z1: float = z0 + d

        u0: Vertex = Vertex(x0, y0, z0, 0.0, 0.0)
        u1: Vertex = Vertex(x1, y0, z0, 0.0, 8.0)
        u2: Vertex = Vertex(x1, y1, z0, 8.0, 8.0)
        u3: Vertex = Vertex(x0, y1, z0, 8.0, 0.0)

        l0: Vertex = Vertex(x0, y0, z1, 0.0, 0.0)
        l1: Vertex = Vertex(x1, y0, z1, 0.0, 8.0)
        l2: Vertex = Vertex(x1, y1, z1, 8.0, 8.0)
        l3: Vertex = Vertex(x0, y1, z1, 8.0, 0.0)

        self.vertices[0] = u0
        self.vertices[1] = u1
        self.vertices[2] = u2
        self.vertices[3] = u3
        self.vertices[4] = l0
        self.vertices[5] = l1
        self.vertices[6] = l2
        self.vertices[7] = l3

        self.polygons[0] = Polygon([l1, u1, u2, l2], 
                                   self.xTexOffs + d + w, 
                                   self.yTexOffs + d, 
                                   self.xTexOffs + d + w + d, 
                                   self.yTexOffs + d + h)
        self.polygons[1] = Polygon([u0, l0, l3, u3],
                                   self.xTexOffs + 0, 
                                   self.yTexOffs + d, 
                                   self.xTexOffs + d,
                                   self.yTexOffs + d + h)
        self.polygons[2] = Polygon([l1, l0, u0, u1],
                                   self.xTexOffs + d, 
                                   self.yTexOffs + 0, 
                                   self.xTexOffs + d + w,
                                   self.yTexOffs + d)
        self.polygons[3] = Polygon([u2, u3, l3, l2],
                                   self.xTexOffs + d + w, 
                                   self.yTexOffs + 0, 
                                   self.xTexOffs + d + w + w, 
                                   self.yTexOffs + d)
        self.polygons[4] = Polygon([u1, u0, u3, u2],
                                   self.xTexOffs + d, 
                                   self.yTexOffs + d, 
                                   self.xTexOffs + d + w,
                                   self.yTexOffs + d + h)
        self.polygons[5] = Polygon([l0, l1, l2, l3],
                                   self.xTexOffs + d + w + d, 
                                   self.yTexOffs + d, 
                                   self.xTexOffs + d + w + d + w, 
                                   self.yTexOffs + d + h)

    def setPos(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def render(self):
        if not self.compiled:
            self.compile()

        c: float = 57.29578
        GL11.glPushMatrix()
        GL11.glTranslatef(self.x, self.y, self.z)
        GL11.glRotatef(self.zRot * c, 0.0, 0.0, 1.0)
        GL11.glRotatef(self.yRot * c, 0.0, 1.0, 0.0)
        GL11.glRotatef(self.xRot * c, 1.0, 0.0, 0.0)

        GL11.glCallList(self.list)
        GL11.glPopMatrix()

    def compile(self):
        self.list = GL11.glGenLists(1)
        GL11.glNewList(self.list, GL11.GL_COMPILE)
        GL11.glBegin(GL11.GL_QUADS)
        for i in range(len(self.polygons)):
            self.polygons[i].render()
        GL11.glEnd()
        GL11.glEndList()
        self.compiled = True
