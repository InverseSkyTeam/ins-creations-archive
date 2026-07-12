import pygame
import sys
pygame.init()
name = 'INS jhx Python GAMEBOX window helper-V0.04'

def hello():
    print(name)
    print('Started working.Hello!YOU CAN USE ME NOW.')
    print('Simple and Easy gui games.')
    print('tp-work..|tran:-09.f')

class Window(object):
    def __init__(self,w=800,h=600,title='INS igamebox main window',icon=None):
        self.w = w
        self.h = h
        self.title = title
        self.icon = icon
        self.screen = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption(self.title)
    def draw_bg(self,r=255,g=255,b=255,bg=None,bgsite=(0,0)):
        self.screen.fill((r,g,b))
        if bg:
            self.draw_pic(bg,bgsite)
    def draw_pic(self,pic,picsite=(0,0)):
        self.screen.blit(pic,picsite)