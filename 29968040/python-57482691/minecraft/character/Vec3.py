# 3维向量
class Vec3:
    def __init__(self, x: float, y: float, z: float):
        self.x: float = x
        self.y: float = y
        self.z: float = z

    '''
     * 返回一个该向量与t向量之间的插值向量
     * @param t
     * @param p
     * @return 差值向量
    '''
    def interpolateTo(self, t, p: float):
        xt = self.x + (t.x - self.x) * p
        yt = self.y + (t.y - self.y) * p
        zt = self.z + (t.z - self.z) * p

        return Vec3(xt, yt, zt)

    '''
     * 设置向量
     * @param x
     * @param y
     * @param z
    '''
    def set(x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

