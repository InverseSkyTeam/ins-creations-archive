import pygame, sys

class Thing:
    def __init__(self,w,h,m,c):
        self.Fx = 0   # 力(N)
        self.Fy = 0
        self.Ax = 0   # 加速度(1px/s^2 1m=100px)
        self.Ay = 0
        self.Sx = 0   # 速度
        self.Sy = 0
        self.x = 200    # 位置
        self.y = 200
        self.m = m    # 质量(kg)
        self.color = c
        self.rect = pygame.Rect(self.x,self.y,w,h)
    def __str__(self):
        d = self.info()
        for i in d:
            d[i] = round(d[i])
        return str(d)
    def force(self,direction,value):
        if direction == 'x':
            self.Fx += value
        else:
            self.Fy += value
        self.Fx *= 0.9    # 空气阻力
        self.Fy *= 0.9
        self.Ax = self.Fx / self.m * 100
        self.Ay = self.Fy / self.m * 100
    def run(self):
        self.Sx += self.Ax
        self.Sy += self.Ay
        self.x += self.Sx
        self.y += self.Sy
        self.rect.topleft = [round(self.x),round(self.y)]
    def blit(self):
        pygame.draw.rect(screen,self.color,self.rect,0,10)
    def info(self):
        return {
            'x': self.x,
            'y': self.y,
            'm': self.m,
            'Sx': self.Sx,
            'Sy': self.Sy,
            'Ax': self.Ax,
            'Ay': self.Ay,
            'Fx': self.Fx,
            'Fy': self.Fy,
        }

animal = Thing(100,100,100,(0,255,200))

pygame.init()
pygame.key.stop_text_input()
screen = pygame.display.set_mode((800,600))

c = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                animal.force('y',-0.005)
            if e.key == pygame.K_DOWN:
                animal.force('y',0.005)
            if e.key == pygame.K_LEFT:
                animal.force('x',-0.005)
            if e.key == pygame.K_RIGHT:
                animal.force('x',0.005)
    screen.fill((255,255,255))
    animal.run()
    animal.blit()
    pygame.display.update()
    pygame.display.set_caption(str(animal))
    c.tick(100)