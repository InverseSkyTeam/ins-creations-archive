from .Vertex import Vertex
from typing import List
import GL11

'''
 * @author Administrator
 * 多边形绘制器(其实是矩形)
'''
class Polygon:
    def __init__(self, vertices: List[Vertex], 
                 u0: int = None, v0: int = None, 
                 u1: int = None, v1: int = None):
        self.vertices: List[Vertex] = vertices
        self.vertexCount: int = len(vertices)
        if u0 is None:
            return
        self.vertices[0] = self.vertices[0].remap(u1, v0)
        self.vertices[1] = self.vertices[1].remap(u0, v0)
        self.vertices[2] = self.vertices[2].remap(u0, v1)
        self.vertices[3] = self.vertices[3].remap(u1, v1)

    '''
     * 绘制多边形(划掉)
    '''
    def render(self):
        GL11.glColor3f(1.0, 1.0, 1.0)
        for i in range(3, -1, -1):
            v: Vertex = self.vertices[i]
            GL11.glTexCoord2f(v.u / 63.999001, v.v / 31.999001)
            GL11.glVertex3f(v.pos.x, v.pos.y, v.pos.z)
