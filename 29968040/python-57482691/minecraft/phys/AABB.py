'''
 * @author Administrator
 * 轴对齐碰撞盒
 * </br>若从z轴正方向的反方向看过去
 * </br>x0,y0,z0推测为左下前顶点，名为1顶点
 * </br>x0,y0,z0推测为右上后顶点，名为2顶点
'''

class AABB:
    '''
     * 偏移量，指发生碰撞时二者的分离距离
     * 
    '''
    epsilon: float = 0.0

    def __init__(self, x0: float, y0: float, z0: float, 
                 x1: float, y1: float, z1: float):
        self.x0: float = x0
        self.y0: float = y0
        self.z0: float = z0
        self.x1: float = x1
        self.y1: float = y1
        self.z1: float = z1

    '''
     * 扩大AABB盒
     *</br> 如果xa,ya,za中的某个是负数，则1顶点的对应的坐标向对应轴的负方向扩展相应的大小
     *</br> 比如xa = -11，则1号顶点的x坐标向x轴负方向扩展11
     *</br> 如果xa,ya,za中的某个是正数，则2顶点的对应的坐标向对应轴的正方向扩展相应的大小
     *</br> 比如ya = 5，则2号顶点的y坐标向y轴正方向扩展5
     * @param xa
     * @param ya
     * @param za
     * @return 返回一个扩大的AABB盒
    '''
    def expand(self, xa: float, ya: float, za: float):
        _x0: float = self.x0
        _y0: float = self.y0
        _z0: float = self.z0
        _x1: float = self.x1
        _y1: float = self.y1
        _z1: float = self.z1
        
        if xa < 0.0:
            _x0 += xa
        if xa > 0.0:
            _x1 += xa

        if ya < 0.0:
            _y0 += ya
        if ya > 0.0:
            _y1 += ya

        if za < 0.0:
            _z0 += za
        if za > 0.0:
            _z1 += za

        return AABB(_x0, _y0, _z0, _x1, _y1, _z1)

    '''
     * aabb盒均匀扩大(我能理解,不知道怎么描述)
     * @param xa
     * @param ya
     * @param za
     * @return
    '''
    def grow(self, xa: float, ya: float, za: float):
        _x0: float = self.x0 - xa
        _y0: float = self.y0 - ya
        _z0: float = self.z0 - za
        _x1: float = self.x1 + xa
        _y1: float = self.y1 + ya
        _z1: float = self.z1 + za
        
        return AABB(_x0, _y0, _z0, _x1, _y1, _z1)

    '''
     * 计算碰撞盒c是否能沿x轴前进xa而不碰到该碰撞盒，若可以则返回xa，若不行，则返回能前进的最大距离(指c移动这么多刚好碰到该碰撞盒)
     * @param c
     * @param xa 尝试前进的距离
     * @return 
    '''
    def clipXCollide(self, c, xa: float) -> float:
        # 下面两种情况AABB盒不可能相交，直接返回
        if c.y1 <= self.y0 or c.y0 >= self.y1:
            return xa
        if c.z1 <= self.z0 or c.z0 >= self.z1:
            return xa

        if xa > 0.0 and c.x1 <= self.x0:
            _max: float = self.x0 - c.x1 - self.epsilon  # 计算两个碰撞盒在X轴上的最大距离，epsilon是偏移量
            if _max < xa:
                xa = _max
        if xa < 0.0 and c.x0 >= self.x1:
            _max: float = self.x1 - c.x0 + self.epsilon
            if _max > xa:
                xa = _max

        return xa

    '''
     * 计算碰撞盒c是否能沿y轴前进ya而不碰到该碰撞盒，若可以则返回ya，若不行，则返回能前进的最大距离(指c移动这么多刚好碰到该碰撞盒)
     * @param c
     * @param ya 尝试前进的距离
     * @return
    '''
    def clipYCollide(self, c, ya: float) -> float:
        if c.x1 <= self.x0 or c.x0 >= self.x1:
            return ya
        if c.z1 <= self.z0 or c.z0 >= self.z1:
            return ya

        if ya > 0.0 and c.y1 <= self.y0:
            _max: float = self.y0 - c.y1 - self.epsilon
            if _max < ya:
                ya = _max
        if ya < 0.0 and c.y0 >= self.y1:
            _max: float = self.y1 - c.y0 + self.epsilon
            if _max > ya:
                ya = _max

        return ya

    '''
     * 计算碰撞盒c是否能沿z轴前进za而不碰到该碰撞盒，若可以则返回za，若不行，则返回能前进的最大距离(指c移动这么多刚好碰到该碰撞盒)
     * @param c
     * @param za 尝试前进的距离
     * @return
    '''
    def clipZCollide(self, c, za: float) -> float:
        if c.x1 <= self.x0 or c.x0 >= self.x1:
            return za
        if c.y1 <= self.y0 or c.y0 >= self.y1:
            return za

        if za > 0.0 and c.z1 <= self.z0:
            _max: float = self.z0 - c.z1 - self.epsilon
            if _max < za:
                za = _max
        if za < 0.0 and c.z0 >= self.z1:
            _max: float = self.z1 - c.z0 + self.epsilon
            if _max > za:
                za = _max

        return za

    '''
     * 计算碰撞盒c是否与该碰撞盒相交
     * @param c
     * @return
    '''
    def intersects(self, c) -> bool:
        if c.x1 <= self.x0 or c.x0 >= self.x1:
            return False
        if c.y1 <= self.y0 or c.y0 >= self.y1:
            return False
        if c.z1 <= self.z0 or c.z0 >= self.z1:
            return False
        return True

    '''
     * 移动该碰撞盒(向XYZ方向移动对应距离)
     * @param xa
     * @param ya
     * @param za
    '''
    def move(self, xa: float, ya: float, za: float):
        self.x0 += xa
        self.y0 += ya
        self.z0 += za
        self.x1 += xa
        self.y1 += ya
        self.z1 += za
