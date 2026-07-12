from moviepy.editor import *
import pygame,sys
pygame.init()
try:
    import ntpath # 如果成功，那么是Windows
    FONTNAME = "Simhei"
    del ntpath
except ImportError: # 如果失败，是MacOS
    FONTNAME = "heititf"
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
from moviepy.editor import *
clip = VideoFileClip('v1.mp4')
clip= clip.resize(newsize=(1280,720))
clip.preview()