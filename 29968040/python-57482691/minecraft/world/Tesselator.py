import GL11


# @author Shiron
# </BR>四边形绘制器
class Tesselator:
    MAX_MEMORY_USE: int = 4194304
    MAX_FLOATS: int = 524288
    instance = None  # new Tesselator()

    def __init__(self):
        self.buffer = None  # BufferUtils.createFloatBuffer(524288)
        self.array = [0.0] * 524288

        self.vertices: int = 0
        self.u: float = 0.0
        self.v: float = 0.0
        self.r: float = 0.0
        self.g: float = 0.0
        self.b: float = 0.0
        self.hasColor = False
        self.hasTexture = False
        self.len: int = 3 * 4
        self.p: int = 0

    # 绘制并清除缓存
    def flush(self):
        self.buffer = (GL11.GLfloat * self.p)(*self.array[:self.p])

        if self.hasTexture and self.hasColor:
            GL11.glInterleavedArrays(GL11.GL_T2F_C3F_V3F, 0, self.buffer)
        elif self.hasTexture:
            GL11.glInterleavedArrays(GL11.GL_T2F_V3F, 0, self.buffer)
        elif self.hasColor:
            GL11.glInterleavedArrays(GL11.GL_C3F_V3F, 0, self.buffer)
        else:
            GL11.glInterleavedArrays(GL11.GL_V3F, 0, self.buffer)
        GL11.glEnableClientState(GL11.GL_VERTEX_ARRAY)
        if self.hasTexture:
            GL11.glEnableClientState(GL11.GL_TEXTURE_COORD_ARRAY)
        if self.hasColor:
            GL11.glEnableClientState(GL11.GL_COLOR_ARRAY)

        GL11.glDrawArrays(7, 0, self.vertices)

        GL11.glDisableClientState(GL11.GL_VERTEX_ARRAY)
        if self.hasTexture:
            GL11.glDisableClientState(GL11.GL_TEXTURE_COORD_ARRAY)
        if self.hasColor:
            GL11.glDisableClientState(GL11.GL_COLOR_ARRAY)

        self.clear()

    def clear(self):
        self.vertices = 0
        self.buffer = None
        self.p = 0

    def init(self):
        self.clear()
        self.hasColor = False
        self.hasTexture = False

    def tex(self, u: float, v: float):
        if not self.hasTexture:
            self.len += 2 * 4
        self.hasTexture = True
        self.u = u
        self.v = v

    def color(self, r: float, g: float, b: float):
        if not self.hasColor:
            self.len += 3 * 4
        self.hasColor = True
        self.r = r
        self.g = g
        self.b = b

    def vertexUV(self, x: float, y: float, z: float, u: float, v: float):
        self.tex(u, v)
        self.vertex(x, y, z)

    # 设置顶点位置
    def vertex(self, x: float, y: float, z: float):
        if self.hasTexture:
            self.array[self.p] = self.u
            self.array[self.p + 1] = self.v
            self.p += 2
        if self.hasColor:
            self.array[self.p] = self.r
            self.array[self.p + 1] = self.g
            self.array[self.p + 2] = self.b
            self.p += 3
        self.array[self.p] = x
        self.array[self.p + 1] = y
        self.array[self.p + 2] = z
        self.p += 3

        self.vertices += 1
        if self.p >= 524288 - self.len and self.vertices % 4 == 0:
            self.flush()


Tesselator.instance = Tesselator()
