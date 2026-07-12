import moviepy.editor
from moviepy.editor import *
import pygame,sys
pygame.init()
try:
    import ntpath # 如果成功，那么是Windows
    FONTNAME = "Simhei"
    del ntpath
except ImportError: # 如果失败，是MacOS
    FONTNAME = "heititf"
pygame.display.set_caption("Mac工作室招募令")
clip = VideoFileClip('logo.gif')
clip= clip.resize(newsize=(1280,720))
clip.preview()
screen = pygame.display.set_mode((1280,720))
logo = pygame.image.load("logo_img.png")
logo = pygame.transform.scale(logo,(1280,720))
for i in range(300):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    screen.blit(logo,(-1,-1))
    screen.blit(pygame.font.SysFont(FONTNAME,50).render("Mac工作室",True,(0,0,0)),(550.952380952381,575.0))
    pygame.display.update()
try:
    import ntpath # 如果成功，那么是Windows
    FONTNAME = "kaiti"
    del ntpath
except ImportError: # 如果失败，是MacOS
    FONTNAME = "kaittf"

cover = pygame.image.load("c.png")
cover = pygame.transform.scale(cover,(420,720))
rect = pygame.Rect(450,550,325,50)
x1 = 0
y1 = 0
color = (0,0,125)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            x1 = event.pos[0]
            y1 = event.pos[1]
        if rect.collidepoint(x1,y1):
            color = (0,0,225)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    import webbrowser
                    webbrowser.open("https://code.xueersi.com/ide/code/13488493")
                    pygame.quit()
                    sys.exit()
        if not rect.collidepoint(x1,y1):
            color = (0,0,125)
    screen.fill((255,255,255))
    screen.blit(cover,(0,0))
    screen.blit(pygame.font.SysFont(FONTNAME,50).render("要求：",True,(0,0,0)),(450,50))
    screen.blit(pygame.font.SysFont(FONTNAME,50).render("1.能够熟练掌握python的基本代码",True,(0,0,0)),(450,100))
    screen.blit(pygame.font.SysFont(FONTNAME,50).render("2.对pygame模块可以进行熟练运用",True,(0,0,0)),(450,150))
    screen.blit(pygame.font.SysFont(FONTNAME,50).render("3.在发布的作品前加入我们的logo",True,(0,0,0)),(450,200))
    screen.blit(pygame.font.SysFont(FONTNAME,50).render("愿意加入且符合条件的请在评论区",True,(0,0,0)),(450,250))
    screen.blit(pygame.font.SysFont(FONTNAME,50).render("回复Mac",True,(0,0,0)),(450,300))
    screen.blit(pygame.font.SysFont(FONTNAME,50).render("注意：本工作室只接受pygame，爬",True,(0,0,0)),(450,350))
    screen.blit(pygame.font.SysFont(FONTNAME,50).render("虫，大数据分析，html的作品。无",True,(0,0,0)),(450,400))
    screen.blit(pygame.font.SysFont(FONTNAME,50).render("关作品请不要加入logo",True,(0,0,0)),(450,450))
    screen.blit(pygame.font.SysFont(FONTNAME,50).render("P.S.logo链接点击蓝字进入",True,(0,0,0)),(450,500))
    screen.blit(pygame.font.SysFont(FONTNAME,50).render("Mac工作室logo",True,color),rect)
    pygame.display.update()