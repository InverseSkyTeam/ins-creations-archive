import pygame
import data
import sys
import os
import platform

pygame.init()

opsystem_info = {
    'system_name': platform.system(),
    'username': os.getlogin(),
    'path': os.getcwd(),
}

if opsystem_info['system_name'] == 'Windows':
    exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)")
else:
    print('非windows系统不一定支持哦')
    exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)")

screen = pygame.display.set_mode((20*50+200,15*50))
pygame.display.set_caption('INS GameBox - SuperTower (超级塔防)')

class Block:
    def __init__(self,index,mode):
        self.mode = mode
        self.index = index
        self.pos = (self.index[0]*50,self.index[1]*50)
        self.rect = pygame.Rect((self.pos[0],self.pos[1],50,50))
        self.tower = None
    def hover(self,pos):
        if self.mode in ('-','*'):
            if self.rect.collidepoint(pos):
                self.mode = '*'
            else:
                self.mode = '-'
    def draw(self):
        cblank, cedge = {'-':((53,53,53),(35,35,35)),
                         '/':((53,53,53),(35,35,35)),
                         '*':((238,238,238),(111,111,111)),
                         '+':((111,255,111),(63,255,63)),
                         'S':((255,111,111),(255,63,63)),
                         'E':((111,111,255),(63,63,255)),
        }[self.mode]
        pygame.draw.rect(screen,cblank,x,0)
        pygame.draw.rect(screen,cedge,x,2)
        if self.tower:
            self.tower.draw()

class Card:
    def __init__(self,text,image,cost):
        self.text = text
        self.image = image
        self.cost = cost
        self.on = False
        self.rect = pygame.Rect(0,0,50,50)
    def onpos(self,pos):
        if self.rect.collidepoint(pos):
            self.on = True
    def draw(self,pos,mpos):
        self.rect.topleft = pos
        pygame.draw.rect(screen,(53,53,53),self.rect,0)
        pygame.draw.rect(screen,(238,238,238),self.rect,2)
        screen.blit(self.image,self.rect)
        if self.on:
            screen.blit(self.image,mpos)

class Tower:
    def __init__(self,text,image,pos,index):
        self.text = text
        self.image = image
        self.index = index
        self.pos = pos
    def draw(self):
        screen.blit(self.image,self.pos)

energy_rect = pygame.Rect(1005,5,190,40)
energy_image = pygame.image.load('./image/电池.png')
tower_center_l1 = pygame.image.load('./image/中心塔1.png')
tower_center_l2 = pygame.image.load('./image/中心塔2.png')
tower_center_l3 = pygame.image.load('./image/中心塔3.png')
tower_center_card = Card('中心塔',tower_center_l1,50)

block_rects = [[Block((x,y),data.level1[y][x]) for x in range(20)] for y in range(15)]
mpos = (0,0)
mmode = 'normal'
energy = 300

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mpos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mmode == 'normal':
                mmode = 'on'
                tower_center_card.onpos(mpos)
            elif mmode == 'on':
                mmode = 'normal'
                tower_center_card.on = False
                if tower_center_card.cost > energy:
                    break
                for y in block_rects:
                    for x in y:
                        if x.mode == '*':
                            x.mode = '/'
                            t = Tower(tower_center_card.text,tower_center_card.image,x.pos,x.index)
                            x.tower = t
                            energy -= tower_center_card.cost
    screen.fill((208,235,235))
    
    for y in block_rects:
        for x in y:
            x.hover(mpos)
            x.draw()
    
    pygame.draw.rect(screen,(148,235,148),energy_rect,0,15)
    screen.blit(energy_image,(1010,10))
    show_text(str(energy),(11,66,33),(1040,10))
    
    tower_center_card.draw((1010,60),mpos)
    pygame.display.update()