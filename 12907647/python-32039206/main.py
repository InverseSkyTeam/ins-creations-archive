import pygame,sys,random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,360),0,32)
color = (200,156,64)
points = []

print('点击屏幕任意位置几个点就有线了，一笔画\n按任意键清除')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            points.clear()
        if event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)
            color = (random.randint(111,255),random.randint(111,255),random.randint(111,255))
    screen.fill((0,0,0))
    if len(points) > 1:
        pygame.draw.lines(screen,color, False, points, 5)
    pygame.display.update()