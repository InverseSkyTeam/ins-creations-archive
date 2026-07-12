import pygame,sys
from turtle import*
from time import*
g=goto
lt=left
rt=right
fd=forward
wh=width
pd=pendown
pp=penup
w=1
hideturtle()
def turnt(x,y):
    if x>250:
        x=x-250
    else:
        x=-(250-x)
    if y>250:
        y=-(y-250)
    else:
        y=(250-y)
    return(x,y)
wh(w)
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("我的作品")
myImg = pygame.image.load("img1.png")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEMOTION:
            print(event.pos)
            g(turnt(event.pos[0],event.pos[1]))
        if event.type==pygame.MOUSEBUTTONDOWN:
            w=w+1
        if event.type==pygame.KEYDOWN:
            w=w-1
    wh(w)
    screen.fill((255,255,255))
    screen.blit(myImg,(0,0))
    pygame.display.update()