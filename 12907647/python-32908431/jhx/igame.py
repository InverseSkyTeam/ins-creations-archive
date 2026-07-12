import pygame
import sys
pygame.init()
name = 'INS jhx Python GAMEBOX window helper-V0.08'

def hello():
    print(name)
    print('Started working.Hello!YOU CAN USE ME NOW.')
    print('Simple and Easy gui games.')
    print('tp-work..|tran:-09.f')

class Rect(object):
    def __init__(self,window,x=0,y=0,w=100,h=100,name='rect?id=1',pic=None,r=0,g=0,b=0):
        self.father = window
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = r
        self.g = g
        self.b = b
        self.name = name
        self.pic = pic
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
    def hit(self,other):
        if type(other) == list and self.rect.collidelist(other):
            return True
        elif type(other) == tuple and len(other)==2 and self.rect.collidepoint(other):
            return True
        else:
            if self.rect.colliderect(other):
                return True
    def draw(self):
        pygame.draw.rect(self.father.screen,(self.r,self.g,self.b),self.rect,0)

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