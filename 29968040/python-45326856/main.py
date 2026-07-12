import pygame,sys
import copy,math
import numpy as np
from PIL import Image
import my_3d
img = Image.open('逆天团队.png')
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("我的作品")
pygame.init()
num=0
num1=300
def calc(s,e,t):
    return [s[0]+(e[0]-s[0])*t,
            s[1]+(e[1]-s[1])*t]
try:import ntpath
except:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)")
else:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)")
finally:pass
count=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0xe3,0xff,0xfe))
    num+=count
    num=min(num,9)
    cd=my_3d.my_3d(num)
    logo_s=[cd[0][1]+num1,cd[0][2]+num1]
    logo_e=[cd[4][1]+num1,cd[4][2]+num1]
    name_s=[cd[2][1]+num1,cd[2][2]+num1]
    name_e=[cd[3][1]+num1,cd[3][2]+num1]
    
    screen.blit(cd[1][0],[cd[1][1]+num1,cd[1][2]+num1])
    
    #screen.blit(cd[0][0],logo_s)
    #screen.blit(cd[2][0],name_s)
    #screen.blit(cd[4][0],logo_s)
    for i in range(0,2):
        screen.blit(cd[4][0],calc(logo_s,logo_e,i/2))
        screen.blit(cd[3][0],calc(name_s,name_e,i/2))
    screen.blit(cd[0][0],logo_e)
    screen.blit(cd[2][0],name_e)
    if count==0:
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(100,285,300,30), width=0, border_radius=10)
        show_text('点击屏幕开始播放动画',(255,0,0),(100,285))
    if pygame.mouse.get_pressed()[0]:
        count=0.25
    #pygame.draw.lines(screen,(0,0,0),True,cd[1],3)
    #pygame.draw.lines(screen,(0,0,0),True,[c,(0,0)])
    pygame.display.update()
    pygame.time.Clock().tick(60)