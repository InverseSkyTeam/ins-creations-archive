from .Vec3 import Vec3


class Vertex:
    def __init__(self, *args, **kwargs):
        # 格式：
        # x, y, z, u, v
        # Vertex, u, v
        # Vec3, u, v
        arg = args + tuple(kwargs.values())
        
        self.u: float = arg[-2]
        self.v: float = arg[-1]
        if len(arg) == 5:
            self.pos: Vec3 = Vec3(*arg[:3])
        elif len(arg) == 3:
            if isinstance(arg[0], Vertex):
                self.pos: Vec3 = arg[0].pos
            elif isinstance(arg[0], Vec3):
                self.pos: Vec3 = arg[0]

    '''
     * 返回一个空间坐标相同，二维纹理坐标不同的顶点
     * @param u
     * @param v
     * @return
    '''
    def remap(self, u: float, v: float):
        return Vertex(self, u, v)



