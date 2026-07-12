# 导入模块
import pygame,time
import sys  
import math  
from pygame.locals import *
from xes.tool import *

# 初始化
pygame.init()

# 定义窗口大小、标题名称、字体设置、创建时钟(可以控制游戏循环频率)等
size = width, height = 1280,720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("宇宙工作室logo")
myfont = pygame.font.Font(None,60)
clock = pygame.time.Clock()
size = width, height = 1280,668
# 定义三个空列表
pos_e = pos_mm = []
# 地球和月球等其他行星的公转过的角度
roll_e = roll_m = 0
roll_2 = roll_3 = roll_4 = roll_5 = roll_6 = roll_7 = roll_8 = 0
h = 668
y = 0 
times = 0
timese = 0
bgtime= 0
# 循环，达到万事万物永不停息的目的
t1 = time.time()
t11 = time.time()
try:
    import ntpath # 如果成功，那么是Windows
    FONTNAME = "kaiti"
    del ntpath
except ImportError: # 如果失败，是MacOS
    FONTNAME = "kaittf"
rect = pygame.Rect(460,140,550,550)
bg = pygame.image.load("星空.jpg").convert() # 背景
bg = pygame.transform.scale(bg,(1280,720))
bg.set_alpha(100)
while True:
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    # 太阳
    sun = pygame.image.load("太阳.png")
    screen.blit(pygame.transform.scale(sun, (100-(1*times), 100-(1*times))), ((1280-(100-(1*times)))/2,(668-(100-(1*times)))/2))

    # 水星
    roll_3 += 0.077  # 每帧公转pi
    pos_3_x = int(size[0] // 2 + size[1] // 8 * math.sin(roll_3))
    pos_3_y = int(size[1] // 2 + size[1] // 8 * math.cos(roll_3)) + y
    mercury = pygame.image.load("水星.png")
    screen.blit(pygame.transform.scale(mercury, (8, 8)), (pos_3_x, pos_3_y))

    # 金星
    roll_2 += 0.069  # 每帧公转pi
    pos_2_x = int(size[0] // 2 + size[1] // 7 * math.sin(roll_2))
    pos_2_y = int(size[1] // 2 + size[1] // 7 * math.cos(roll_2)) + y
    venus = pygame.image.load("金星.png")
    screen.blit(pygame.transform.scale(venus, (10, 10)), (pos_2_x, pos_2_y))

    # 地球
    roll_e += 0.060  # 每帧公转pi
    pos_e_x = int(size[0] // 2 + size[1] // 6 * math.sin(roll_e))
    pos_e_y = int(size[1] // 2 + size[1] // 6 * math.cos(roll_e)) + y
    earth = pygame.image.load("地球.jpg")
    screen.blit(pygame.transform.scale(earth, (15, 15)), (pos_e_x, pos_e_y))

    # 月球
    roll_m += 0.2  # 每帧公转pi
    pos_m_x = int(pos_e_x + size[1] // 30 * math.sin(roll_m))
    pos_m_y = int(pos_e_y + size[1] // 30 * math.cos(roll_m))
    mouth = pygame.image.load("水星.png")
    screen.blit(pygame.transform.scale(mouth, (8, 8)), (pos_m_x+5, pos_m_y+5))

    # 火星
    roll_4 += 0.053  # 每帧公转pi
    pos_4_x = int(size[0] // 2 + size[1] // 5 * math.sin(roll_4))
    pos_4_y = int(size[1] // 2 + size[1] // 5 * math.cos(roll_4)) + y
    venus = pygame.image.load("火星.png")
    screen.blit(pygame.transform.scale(venus, (13, 13)), (pos_4_x, pos_4_y))

    # 木星
    roll_5 += 0.045  # 每帧公转pi
    pos_5_x = int(size[0] // 2 + size[1] // 4 * math.sin(roll_5))
    pos_5_y = int(size[1] // 2 + size[1] // 4 * math.cos(roll_5)) + y
    mouth = pygame.image.load("木星.png")
    screen.blit(pygame.transform.scale(mouth, (70-(1*times), 70-(1*times))), (pos_5_x, pos_5_y))

    # 土星
    roll_6 += 0.037  # 每帧公转pi
    pos_6_x = int(size[0] // 2 + size[1] // 3.5 * math.sin(roll_6))
    pos_6_y = int(size[1] // 2 + size[1] // 3.5 * math.cos(roll_6)) + y
    saturn = pygame.image.load("土星.png")
    screen.blit(pygame.transform.scale(saturn, (80-(1*times), 80-(1*times))), (pos_6_x, pos_6_y))

    # 天王星
    roll_7 += 0.031  # 每帧公转pi
    pos_7_x = int(size[0] // 2 + size[1] // 2.7 * math.sin(roll_7))
    pos_7_y = int(size[1] // 2 + size[1] // 2.7 * math.cos(roll_7)) + y
    uranus = pygame.image.load("天王星.png")
    screen.blit(pygame.transform.scale(uranus, (47-(1*times), 47-(1*times))), (pos_7_x, pos_7_y))

    # 海王星
    roll_8 += 0.025  # 每帧公转pi
    pos_8_x = int(size[0] // 2 + size[1] // 2 * math.sin(roll_8))
    pos_8_y = int(size[1] // 2 + size[1] // 2 * math.cos(roll_8)) + y
    neptune = pygame.image.load("海王星.png")
    screen.blit(pygame.transform.scale(neptune, (50-(1*times), 50-(1*times))), (pos_8_x, pos_8_y))
    
    if bgtime > 10:
        bg.set_alpha(150)
        while True:
            screen.fill((0,0,0))
            screen.blit(bg,(0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            screen.blit(pygame.font.SysFont(FONTNAME,100).render("宇宙工作室",True,(255,255,255)),(390,600))
            # 太阳
            sun = pygame.image.load("太阳.png")
            screen.blit(pygame.transform.scale(sun, (100-(1*times), 100-(1*times))), ((1280-(100-(1*times)))/2,(668-(100-(1*times)))/2))
        
            # 水星
            roll_3 += 0.077  # 每帧公转pi
            mercury = pygame.image.load("水星.png")
            screen.blit(pygame.transform.scale(mercury, (8, 8)), (pos_3_x, pos_3_y))
        
            # 金星
            roll_2 += 0.069  # 每帧公转pi
            venus = pygame.image.load("金星.png")
            screen.blit(pygame.transform.scale(venus, (10, 10)), (pos_2_x, pos_2_y))
        
            # 地球
            roll_e += 0.060  # 每帧公转pi
            earth = pygame.image.load("地球.jpg")
            screen.blit(pygame.transform.scale(earth, (15, 15)), (pos_e_x, pos_e_y))
        
            #月球
            roll_m += 0.2  # 每帧公转pi
            mouth = pygame.image.load("水星.png")
            screen.blit(pygame.transform.scale(mouth, (8, 8)), (pos_m_x+5, pos_m_y+5))
        
            # 火星
            roll_4 += 0.053  # 每帧公转pi
            venus = pygame.image.load("火星.png")
            screen.blit(pygame.transform.scale(venus, (13, 13)), (pos_4_x, pos_4_y))
        
            # 木星
            roll_5 += 0.045  # 每帧公转pi
            mouth = pygame.image.load("木星.png")
            screen.blit(pygame.transform.scale(mouth, (70-(1*times), 70-(1*times))), (pos_5_x, pos_5_y))
        
            # 土星
            roll_6 += 0.037  # 每帧公转pi
            saturn = pygame.image.load("土星.png")
            screen.blit(pygame.transform.scale(saturn, (80-(1*times), 80-(1*times))), (pos_6_x, pos_6_y))
        
            # 天王星
            roll_7 += 0.031  # 每帧公转pi
            uranus = pygame.image.load("天王星.png")
            screen.blit(pygame.transform.scale(uranus, (45-(1*times), 45-(1*times))), (pos_7_x, pos_7_y))
        
            # 海王星
            roll_8 += 0.025  # 每帧公转pi
            neptune = pygame.image.load("海王星.png")
            screen.blit(pygame.transform.scale(neptune, (50-(1*times), 50-(1*times))), (pos_8_x, pos_8_y))
            rect.center = ((1280-(100-(1*times)))/2+((100-(1*times))/2),(668-(100-(1*times)))/2+((100-(1*times))/2))
            pygame.draw.ellipse(screen,(255,255,255),rect,10)
            pygame.display.update()
    if timese >= 0.25:
        times = times + 1
        timese = 0
        t1 = time.time()
    h = h-0.75
    size = width, height = 1280,h
    y = (668-h)/2
    # 刷新
    pygame.display.flip()
    # 数值越大刷新越快，小球运动越快
    clock.tick(50)
    t2 = time.time()
    t22 = time.time()
    timese = t2-t1
    bgtime = t22-t11