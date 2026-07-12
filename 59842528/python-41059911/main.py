import pygame,sys,random,time,os
from moviepy.editor import *
pygame.init()

clip = VideoFileClip("./fireworks.mp4",target_resolution=(500,950))


screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Fireworks")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    clip.preview()
    clip.close()
    pygame.display.update()
