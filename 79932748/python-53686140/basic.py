import pygame

# 资源
recipe = {
    (
        (1004,),
    ): (1005,4),
    (
        (1005,),
        (1005,),
    ): (2001,4),
    (
        (1005,1005),
        (1005,1005),
    ): (1006,1),
    (
        (1003,1003,1003),
        (1003,1006,1003),
        (1003,1003,1003),
    ): (1007,1),
}



# pygame基本对象
def loadblock(name,s):
    return pygame.transform.scale(pygame.image.load(f'./images/{name}'),(s,s))
lb = loadblock



# python基本对象
def get_distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2) ** 0.5

def hit_rect(x1,y1,w1,h1,x2,y2,w2,h2):     # 只有坐标的矩形碰撞
    l1, r1, t1, b1 = x1, x1 + w1, y1, y1 + h1
    l2, r2, t2, b2 = x2, x2 + w2, y2, y2 + h2
    return not (l1 < r1 < l2 < r2 or 
                l2 < r2 < l1 < r1 or 
                t1 < b1 < t2 < b2 or 
                t2 < b2 < t1 < b1)

class Slider:
    def __init__(self,value,full,digit=1):
        self.value = value
        self.full = full
        self.digit = digit
    def __iadd__(self,n):
        self.value = max(0, min(self.value + n, self.full))
        return self
    def __isub__(self,n):
        self.value = max(0, min(self.value - n, self.full))
        return self
    def __imul__(self,n):
        self.value = max(0, min(self.value * n, self.full))
        return self
    def __itruediv__(self,n):
        self.value = max(0, min(self.value / n, self.full))
        return self
    def __add__(self,n):
        return round(max(0, min(self.value + n, self.full)), self.digit)
    def __sub__(self,n):
        return round(max(0, min(self.value - n, self.full)), self.digit)
    def __mul__(self,n):
        return round(max(0, min(self.value * n, self.full)), self.digit)
    def __truediv__(self,n):
        return round(max(0, min(self.value / n, self.full)), self.digit)
    def __lt__(self,n):
        return self.value < n
    def __le__(self,n):
        return self.value <= n
    def __gt__(self,n):
        return self.value > n
    def __ge__(self,n):
        return self.value >= n
    def clear(self):
        self.value = 0
    def fill(self):
        self.value = self.full
    def set(self,n):
        self.value = n
    def change_full(self,n):
        self.full = n
    @property
    def v(self):
        return round(self.value,self.digit)
    @property
    def f(self):
        return round(self.full,self.digit)
    @property
    def part(self):
        return self.value / self.full