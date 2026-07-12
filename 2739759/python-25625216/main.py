# 记得导出素材
# 记得导出素材
# 记得导出素材
# 导出素材可以解注释下面这几行代码
# from xes.tool import xopen
# xopen()
import pygame,sys,time
pygame.init()
screen = pygame.display.set_mode((800,600))     #修改这行代码修改窗口分辨率(不推荐修改)
pygame.display.set_caption("方圆工作室动态logo")    #修改这行代码来更换窗口名称
myImg = pygame.image.load("logo.jpg").convert()
a = 0
myImg.set_alpha(a)
# 73,17,632,590
circle = pygame.Rect(800,17,632,590)
rect1 = pygame.Rect(0,0,70,800)
rect2 = pygame.Rect(700,0,100,800)
flag = 0
b = 800
rect = pygame.Surface((800,600)).convert()
rect.fill((0,0,0))
c = 0
rect.set_alpha(c)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if circle.x>73:
        circle.x-=10
    if circle.x <= 73:
        circle.x=73
        flag = 1
    screen.fill((0,0,0))
    if flag == 1:
        a += 5
        if b>0:
            b -= 16
        myImg.set_alpha(a)
        rect1 = pygame.Rect(0,0,70,b)
        rect2 = pygame.Rect(700,0,100,b)
        screen.blit(myImg,(0,0))
        pygame.draw.rect(screen,(0,0,0),rect1,0)
        pygame.draw.rect(screen,(0,0,0),rect2,0)
    pygame.draw.ellipse(screen,(255,255,255),circle,10)
    if a>=800:
        c += 5
        rect.set_alpha(c)
        screen.blit(rect,(0,0))
    pygame.display.update()
#在下面的循环中添加正式游戏代码
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    pygame.display.update()