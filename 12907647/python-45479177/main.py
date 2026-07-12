import pygame,sys
import random
import numpy as np

class Cuboid:
    def __init__(self,screen,xl,yl,zl,w):
        x = [xl,-xl,-xl,xl,xl,-xl,-xl,xl]
        y = [yl,yl,-yl,-yl,yl,yl,-yl,-yl]
        z = [zl,zl,zl,zl,-zl,-zl,-zl,-zl]
        self.x = np.array(x)
        self.y = np.array(y)
        self.z = np.array(z)
        self.w = w
        self.scx = 0
        self.scy = 0
        self.scz = 0
        self.dl = []
        self.screen = screen
        self.screen_w, self.screen_h = self.screen.get_width(), self.screen.get_height()
        self.screen_w /= 2
        self.screen_h /= 2
    def act_rotate_x(self,angle):
        newy = self.y * np.cos(angle) - self.z * np.sin(angle)
        newz = self.y * np.sin(angle) + self.z * np.cos(angle)
        self.y, self.z = newy, newz
    def act_rotate_y(self,angle):
        newx = self.x * np.cos(angle) + self.z * np.sin(angle)
        newz = self.z * np.cos(angle) - self.x * np.sin(angle)
        self.x, self.z = newx, newz
    def act_move(self,addx,addy,addz):
        self.x += addx
        self.y += addy
        self.z += addz
    def XZr(self,xa,ya):
        self.act_rotate_x(xa)
        self.act_rotate_y(ya)
    def plTO(self,px,py,pz):#根据摄像机位置进行平移
        self.act_move(-px,-py,-pz)
    def plXZr(self,pxa,pya):#根据摄像机角度进行转换
        self.scy = self.y * np.cos(pxa) - self.z * np.sin(pxa)
        self.z = self.y * np.sin(pxa) + self.z * np.cos(pxa)
        self.scx = self.x * np.cos(pya) + self.z * np.sin(pya)
        self.scz = self.z * np.cos(pya) - self.x * np.sin(pya)
    def WZ3D(self):#根据倍率和窗口中心位置对图像进行平移然后投影
        dx = self.scx * self.w / self.scz + self.screen_w
        dy = self.scy * self.w / self.scz + self.screen_h
        self.dl = [[dx[i],dy[i]] for i in range(len(dx))]
    def draw(self):
        for i in self.dl:
            pygame.draw.rect(self.screen,(0,255,255),pygame.Rect(i[0],i[1],5,5),0)

def drawd(xa,ya,pxa,pya):
    zhl = Cuboid(screen,666,666,666,1000)
    zhl.XZr(xa,ya)
    zhl.plTO(0,0,-5000)
    zhl.plXZr(pxa,pya)
    zhl.WZ3D()
    zhl.draw()

pygame.init()
screen = pygame.display.set_mode((800,800))

xu = 0
yu = 0

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEMOTION:
            xu = (400-event.pos[0]) / 100
            yu = (event.pos[1]-400) / 100
    drawd(yu,xu,yu/8,xu/8)
    pygame.display.update()