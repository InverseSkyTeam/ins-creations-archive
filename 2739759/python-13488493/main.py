# from xes.tool import*
# xopen()
import moviepy.editor
from moviepy.editor import *
import pygame,sys
pygame.init()
try:
    import ntpath # 如果成功，那么是Windows
    FONTNAME = "Simhei"
    del ntpath
except ImportError: # 如果失败，是MacOS
    FONTNAME = "kaittf"
pygame.display.set_caption("Mac工作室logo")
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
    screen.blit(pygame.font.SysFont(FONTNAME,50).render("Mac工作室",True,(0,0,0)),(550,575.0))
    screen.blit(pygame.font.SysFont(FONTNAME,20).render("极致、极爱、极简",True,(0,0,0)),(580,625.0))
    pygame.display.update()
try:
    import ntpath # 如果成功，那么是Windows
    FONTNAME = "kaiti"
    del ntpath
except ImportError: # 如果失败，是MacOS
    FONTNAME = "kaittf"
# 以下是第二个界面主循环
a = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    if b == 0:
        a = a + 1
    if b == 1:
        a = a - 1
    if a >= 255:
        time.sleep(1)
        b = 1
    if a <= 0:
        b = 0
    logo.set_alpha(a)
    screen.blit(logo, (0, 0))
    pygame.display.update()