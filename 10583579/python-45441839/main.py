import pygame
import sys
import math

def sin(num):  # 正弦函数
    return math.sin(math.radians(num))
def cos(num):  # 余弦函数
    return math.cos(math.radians(num))

# 顶点类
class Point:
    def __init__(self, x, y, z, length=200):
        self.x, self.y, self.z = x, y, z
        self.abs_x, self.abs_y, self.abs_z = x, y, z
        self.length = length

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y, self.z + point.z, self.length)

    def translate(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    def scale(self, x, y, z):
        self.x *= x
        self.y *= y
        self.z *= z

    def rotatex(self, angle):
        self.y = self.y * cos(angle) - self.z * sin(angle)
        self.z = self.y * sin(angle) + self.z * cos(angle)

    def rotatey(self, angle):
        self.x = self.x * cos(angle) - self.z * sin(angle)
        self.z = self.x * sin(angle) + self.z * cos(angle)

    def rotatez(self, angle):
        self.x = self.x * cos(angle) - self.y * sin(angle)
        self.y = self.x * sin(angle) + self.y * cos(angle)

    def perspective(self):
        scale_factor = 400 / (self.z + 400)  # 修改透视的比例
        return (self.x * scale_factor, self.y * scale_factor)  # 平移坐标

    def __str__(self):
        return f"Point<x={self.x} y={self.y} z={self.z}>"
    __repr__ = __str__

# 立方体类
class Cube:
    def __init__(self, pivot: Point, points: Point, length=200):
        self.pivot = pivot
        self.rel = points
        self.update()

    def update(self):
        self.abs = [point + self.pivot for point in self.rel]

    def translate(self, x, y, z):
        for point in self.rel:
            point.translate(x, y, z)
        self.update()

    def scale(self, x, y, z):
        for point in self.rel:
            point.scale(x, y, z)
        self.update()

    def rotatex(self, angle):
        for point in self.rel:
            point.rotatex(angle)
        self.update()

    def rotatey(self, angle):
        for point in self.rel:
            point.rotatey(angle)
        self.update()

    def rotatez(self, angle):
        for point in self.rel:
            point.rotatez(angle)
        self.update()

    def draw(self, screen):
        pos = []
        # 顶点
        for point in self.abs:
            position = point.perspective()
            pos.append(position)
        # 12条线段
        pygame.draw.line(screen, (255, 0, 0), pos[0], pos[1])
        pygame.draw.line(screen, (255, 0, 0), pos[0], pos[2])
        pygame.draw.line(screen, (255, 0, 0), pos[1], pos[3])
        pygame.draw.line(screen, (255, 0, 0), pos[2], pos[3])
        pygame.draw.line(screen, (255, 0, 0), pos[4], pos[5])
        pygame.draw.line(screen, (255, 0, 0), pos[4], pos[6])
        pygame.draw.line(screen, (255, 0, 0), pos[5], pos[7])
        pygame.draw.line(screen, (255, 0, 0), pos[6], pos[7])
        pygame.draw.line(screen, (255, 0, 0), pos[0], pos[4])
        pygame.draw.line(screen, (255, 0, 0), pos[1], pos[5])
        pygame.draw.line(screen, (255, 0, 0), pos[2], pos[6])
        pygame.draw.line(screen, (255, 0, 0), pos[3], pos[7])

# 初始化
LENGTH = 200
pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('3D')
cube = Cube(Point(300,200,200),[Point(-50,-50,50),Point(50,-50,50),Point(-50,50,50),Point(50,50,50),Point(-50,-50,-50),Point(50,-50,-50),Point(-50,50,-50),Point(50,50,-50)])
# 主循环
clock = pygame.time.Clock()
cube.scale(2,2,2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    cube.draw(screen)   # 立方体绘制
    cube.rotatey(1)  # 修改旋转轴
    pygame.draw.circle(screen, (255,0,0), Point(300, 200, 200).perspective(), 3)  # 旋转中心点
    pygame.display.update()
    clock.tick(60)