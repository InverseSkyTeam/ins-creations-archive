from .phys import AABB
import random
import math


class Entity:
    def __init__(self, world):
        self.xo: float = 0.0
        self.yo: float = 0.0
        self.zo: float = 0.0
    
        # 实体中心的世界位置(本质上是实体包围盒的中心位置)
        self.x: float = 0.0
        self.y: float = 0.0
        self.z: float = 0.0

        # 速度向量
        self.xd: float = 0.0
        self.yd: float = 0.0
        self.zd: float = 0.0
    
        # 该实体绕某个轴的旋转角度
        self.yRot: float = 0.0
        self.xRot: float = 0.0
    
        # 该实体的AABB盒
        self.bb: AABB = None
    
        # 标记是否接触地面
        self.onGround: bool = False
        # 标记是否被移除
        self.removed: bool = False
        self.heightOffset: float = 0.0

        self.bbWidth: float = 0.6
        self.bbHeight: float = 1.8
        
        self.world = world
        self.resetPos()

    '''
     * 重置实体位置(随机)
    '''
    def resetPos(self):
        x: float = float(random.random() * self.world.width)
        y: float = float(self.world.depth + 10)
        z: float = float(random.random() * self.world.height)
        self.setPos(x, y, z)

    '''
     * 移除实体
    '''
    def remove(self):
        self.removed = True

    '''
     * 设置包裹整个实体的AABB盒的大小(一个长方体，底部为正方形，边长为w)
     * @param w
     * @param h
    '''
    def setSize(self, w: float, h: float):
        self.bbWidth = w
        self.bbHeight = h

    '''
     * 设置实体中心位置
     * @param x
     * @param y
     * @param z
    '''
    def setPos(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
        w: float = self.bbWidth / 2.0
        h: float = self.bbHeight / 2.0
        self.bb = AABB(x - w, y - h, z - w, x + w, y + h, z + w)


    '''
     * 将自身绕x,y轴旋转(坐标系为当前实体自身坐标系)
     * @param y_rot
     * @param x_rot
    '''
    def turn(self, y_rot: float, x_rot: float):
        self.yRot = float(self.yRot + y_rot * 0.15)
        self.xRot = float(self.xRot - x_rot * 0.15)
        if self.xRot < -90.0:
            self.xRot = -90.0
        if self.xRot > 90.0:
            self.xRot = 90.0

    '''
     * 游戏刻
    '''
    def tick(self):
        self.xo = self.x
        self.yo = self.y
        self.zo = self.z

    '''
     * 尝试将该实体移动到(xa,ya,za)[世界坐标系]
     * <br>注:游戏逻辑里经常将速度与位移的概念混用，经常有move(xd,yd,zd)的用法[常见于tick方法里]
     * @param xa
     * @param ya
     * @param za
    '''
    def move(self, xa: float, ya: float, za: float):
        xaOrg: float = xa
        yaOrg: float = ya
        zaOrg: float = za

        aABBs: list = self.world.getCubes(self.bb.expand(xa, ya, za))

        
        for i in range(len(aABBs)):
            ya = aABBs[i].clipYCollide(self.bb, ya)
        self.bb.move(0.0, ya, 0.0)

        for i in range(len(aABBs)):
            xa = aABBs[i].clipXCollide(self.bb, xa)
        self.bb.move(xa, 0.0, 0.0)

        for i in range(len(aABBs)):
            za = aABBs[i].clipZCollide(self.bb, za)
        self.bb.move(0.0, 0.0, za)

        
        self.onGround = (yaOrg != ya) and (yaOrg < 0.0)

        if xaOrg != xa:
            self.xd = 0.0
        if yaOrg != ya:
            self.yd = 0.0
        if zaOrg != za:
            self.zd = 0.0

        # 更新实体中心位置
        self.x = (self.bb.x0 + self.bb.x1) / 2.0
        self.y = self.bb.y0 + self.heightOffset
        self.z = (self.bb.z0 + self.bb.z1) / 2.0

    '''
     * 相对自身坐标系的移动(自身坐标系：玩家正视方向为z轴负方向(什么反人类设定),玩家右侧为x轴正方向)
     * </br>
     * </br>(xa,ya)是移动方向向量,speed是移动速度
     * @param xa 
     * @param za 
     * @param speed 移动速度
    '''
    def moveRelative(self, xa: float, za: float, speed: float):
        dist: float = xa * xa + za * za
        if dist < 0.01:
            return

        dist = speed / float(math.sqrt(dist))
        
        xa *= dist
        za *= dist

        sin: float = math.sin(self.yRot * math.pi / 180.0)
        cos: float = math.cos(self.yRot * math.pi / 180.0)

        # 计算其在世界坐标系中的速度向量，并与原速度向量叠加
        self.xd += xa * cos - za * sin
        self.zd += za * cos + xa * sin

    def isLit(self) -> bool:
        xTile: int = int(self.x)
        yTile: int = int(self.y)
        zTile: int = int(self.z)
        return self.world.isLit(xTile, yTile, zTile)
