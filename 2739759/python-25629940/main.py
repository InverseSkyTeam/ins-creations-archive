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
# circle2 = pygame.Rect(800,17,632,590)
circle = pygame.Rect(800,17,10,10)
rect1 = pygame.Rect(0,0,70,800)
rect2 = pygame.Rect(700,0,100,800)
flag = 0
b = 800
rect = pygame.Surface((800,600)).convert()
rect.fill((0,0,0))
yingyang = pygame.image.load("yingyang.png")
yingyang_rect = yingyang.get_rect()
yingyang_left = pygame.image.load("yingyang_left.png")
yingyang_right = pygame.image.load("yingyang_right.png")
yingyang_left_x = -800
yingyang_right_x = 800
c = 0
rect.set_alpha(c)
angle = 0
flag2 = 0
flag3 = 0
width = 0
rectheight = 20
rectwidth = 20
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # if circle.x>73:
    #     circle.x-=10
    # if circle.x <= 73:
    #     circle.x=73
    screen.fill((0,0,0))
    if flag == 1:
        # (150, 100, 470,435)
        if rectwidth<475:
            rectwidth+=10
        if rectwidth>=475:
            if rectheight<435:
                rectheight+=10
            else:
                flag3 = 1
        pygame.draw.rect(screen,(255,255,255),(150,95,rectwidth,rectheight),10,border_radius=50)
        
    if flag3 == 1:
        a += 5
        if b>0:
            b -= 16
        myImg.set_alpha(a)
        rect1 = pygame.Rect(0,0,70,b)
        rect2 = pygame.Rect(700,0,100,b)
        screen.blit(myImg,(0,0))
        pygame.draw.rect(screen,(0,0,0),rect1,0)
        pygame.draw.rect(screen,(0,0,0),rect2,0)
    # yingyang = pygame.image.load("yingyang.png")
    # yingyang_rect = yingyang.get_rect()
    # newLeaf = pygame.transform.rotate(yingyang,angle)
    # newRect = newLeaf.get_rect(center=yingyang_rect.center)
    # angle += 1
    # screen.blit(newLeaf, newRect)
    if flag2 == 1:
        circle.width+=11
        circle.height+=10
        circle.center = (393,315.5)
        if circle.width>=632 :
            circle.width=632
            circle.height=590
            flag = 1
        pygame.draw.ellipse(screen,(255,255,255),circle,10)
    # screen.blit(yingyang,yingyang_rect)
    if yingyang_left_x<0:
        yingyang_left_x+=10
    else:
        flag2 = 1
    if yingyang_right_x>0:
        yingyang_right_x-=10
    screen.blit(yingyang_left,(yingyang_left_x,0))
    screen.blit(yingyang_right,(yingyang_right_x,0))
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