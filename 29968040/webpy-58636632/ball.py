import math
from anim_manager import NumberAnimation, remove
import image_manager
import pygame.transform
from ball_data import BallData


class Ball:
    def __init__(self):
        self.id = 'img'
        self.pointX = 0
        self.pointY = 0
        self.preX = 0
        self.preY = 0
        self.vx = 0
        self.vy = 0
        self.r = 0
        self.cor = 0  # 碰撞后的能量损失值,为 1 表示碰撞后不会损失能量
        self.mass = 0  # 小球质量,球体越大,质量越大
        self.rotate = 0
        self.ballType = 0  # 小球类型
        self.mergeSrc = ""  # 合并时的动画资源
        self.mergeStart = False  # 启动合并动画显示
        self.endPointX = 0  # 合并时的终点x坐标
        self.endPointY = 0  # 启动合并的终点y坐标
        self.source = None
        self.transform = True

        self._width = 0
        self._height = 0
        
        self.cache_sf = {}
        
        self.widthAnimation = NumberAnimation(self, '_width', 300 / 1000)
        self.heightAnimation = NumberAnimation(self, '_height', 300 / 1000, None, None, self.set_size_finish)

        self.enPointXAnimation = NumberAnimation(self, 'pointX', 300 / 1000,
                                                 lambda: self.mergeStart,
                                                 lambda: (self.pointX, self.endPointX))
        self.enPointYAnimation = NumberAnimation(self, 'pointY', 300 / 1000,
                                                 lambda: self.mergeStart,
                                                 lambda: (self.pointY, self.endPointY))

        def _rotate_finish():
            self.preX, self.preY, self.mergeStart = self.pointX, self.pointY, False

        self.rotateAnimation = NumberAnimation(self, 'rotate', 300 / 1000,
                                               lambda: self.mergeStart,
                                               lambda: (None, self.calcEndRotate()),
                                               _rotate_finish)

        image_manager.add(self)

    @property
    def shapeChange(self):  # 形状是否在改变中,创建小球的时候,形状会慢慢变大,此时用户不能立即降落小球
        return self.widthAnimation.running

    @property
    def x(self):
        return self.pointX - self.width / 2
    
    @property
    def y(self):
        return self.pointY - self.height / 2
    
    def set_p(self, x):
        self.pointX = x
    
    @property
    def width(self):
        return int(self._width)
    
    def set_width(self, value):
        self.widthAnimation.start(_from=None, _to=value)

    def set_size_finish(self):
        h = int(self._height)
        _h = round(h * 1.42)
        new_sf = pygame.Surface((_h, _h), pygame.SRCALPHA)
        sf = pygame.transform.scale(self.source, (h, h))
        new_sf.blit(sf, ((_h - h) // 2,) * 2)
        self.cache_sf[h] = new_sf

    @property
    def height(self):
        return int(self._height)

    def set_height(self, value):
        self.heightAnimation.start(_from=None, _to=value)

    def calcEndRotate(self):
        distance = math.sqrt((self.endPointX - self.pointX) ** 2 + (self.endPointY - self.pointY) ** 2)

        if self.endPointX > self.pointX:  # 往右
            return self.rotate + 360/(2 * self.r * 3.14) * distance * 0.5
        else:  # 往左
            return self.rotate - 360/(2 * self.r * 3.14) * distance * 0.5

    def destroy(self):
        image_manager.remove(self)
        remove(self.rotateAnimation)
        remove(self.enPointYAnimation)
        remove(self.enPointXAnimation)
        remove(self.heightAnimation)
        remove(self.widthAnimation)
