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
        pygame.draw.rect(screen,cblank,self.rect,0)
        pygame.draw.rect(screen,cedge,self.rect,2)

class Card:
    def __init__(self,text):
        self.text = text
        self.image = tower_images[self.text][1]
        self.cost = data.cards[self.text][1]['cost']
        self.on = False
        self.rect = pygame.Rect(0,0,50,50)
    def onpos(self,pos):
        if self.rect.collidepoint(pos):
            self.on = True
        return self.on
    def draw(self,pos,mpos):
        self.rect.topleft = pos
        pygame.draw.rect(screen,(53,53,53),self.rect,0)
        pygame.draw.rect(screen,(238,238,238),self.rect,2)
        screen.blit(self.image,self.rect)
        if self.on:
            screen.blit(self.image,mpos)

class Tower:
    def __init__(self,text,pos,index):
        self.text = text
        self.index = index
        self.pos = pos
        self.rect = pygame.Rect(self.pos,(50,50))
        self.uprect = pygame.Rect(self.rect.centerx-40,self.rect.top-40,35,35)
        self.salerect = pygame.Rect(self.rect.centerx+5,self.rect.top-40,35,35)
        self.rangerect = pygame.Rect(0,0,0,0)
        self.rangesur_pos = None
        self.rangesurface = None
        self.level = 1
        self.state = 'normal'
        self.get_attr()
    def get_attr(self):
        self.attr = data.cards[self.text][self.level]
        self.image = tower_images[self.text][self.level]
        self.get_range()
    def get_range(self):
        _range = self.attr['range']
        self.rangerect.width = _range * 2
        self.rangerect.height = _range * 2
        self.rangesur_pos = (self.rect.centerx-_range,self.rect.centery-_range)
        self.rangesurface = pygame.Surface((self.rangerect.width,self.rangerect.height),pygame.SRCALPHA)
    def onpos(self,pos,energy,master):
        if self.state == 'on':
            if self.uprect.collidepoint(pos) and (self.level < data.cards[self.text][0]['max_level']) and (energy >= data.cards[self.text][self.level+1]['cost']):
                self.level += 1
                energy -= data.cards[self.text][self.level]['cost']
                self.get_attr()
            if self.salerect.collidepoint(pos):
                energy += data.cards[self.text][self.level]['sale']
                tower_list.remove(self)
                master.mode = '-'
                master.tower = None
        if self.rect.collidepoint(pos) and self.state == 'normal':
            self.state = 'on'
        else:
            self.state = 'normal'
        return energy
    def draw(self):
        screen.blit(self.image,self.rect)
    def draw_range(self):
        if self.state == 'on':
            pygame.draw.ellipse(self.rangesurface,(255,255,255,80),self.rangerect)
            screen.blit(self.rangesurface,self.rangesur_pos)
            screen.blit(levelup_image,self.uprect)
            screen.blit(sale_image,self.salerect)
            pygame.draw.rect(screen,(255,0,0),self.rect,5)

energy_rect = pygame.Rect(1005,5,190,40)
energy_image = pygame.image.load('./image/电池.png')
levelup_image = pygame.image.load('./image/升级按钮.png')
sale_image = pygame.image.load('./image/售出按钮.png')
tower_images = {
    '中心塔': [
        None,    # 索引0就空着吧
        pygame.image.load('./image/中心塔1.png'),
        pygame.image.load('./image/中心塔2.png'),
        pygame.image.load('./image/中心塔3.png'),
    ],
}
tower_center_card = Card('中心塔')

block_rects = [[Block((x,y),data.level1[y][x]) for x in range(20)] for y in range(15)]
mpos = (0,0)
mmode = 'normal'
energy = 3000

tower_list = []



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mpos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mmode == 'normal':
                if tower_center_card.onpos(mpos):
                    mmode = 'on'
                    break
                for blockline in block_rects:
                    for block in blockline:
                        tower = block.tower
                        if tower:
                            energy = tower.onpos(mpos,energy,block)
            elif mmode == 'on':
                mmode = 'normal'
                tower_center_card.on = False
                if tower_center_card.cost > energy:
                    break
                for y in block_rects:
                    for x in y:
                        if x.mode == '*':
                            x.mode = '/'
                            t = Tower(tower_center_card.text,x.pos,x.index)
                            x.tower = t
                            tower_list.append(t)
                            energy -= tower_center_card.cost
    screen.fill((208,235,235))
    
    for y in block_rects:
        for x in y:
            x.hover(mpos)
            x.draw()
    for tower in tower_list:
        tower.draw()
    for tower in tower_list:
        tower.draw_range()
    pygame.draw.rect(screen,(148,235,148),energy_rect,0,15)
    screen.blit(energy_image,(1010,10))
    show_text(str(energy),(11,66,33),(1040,10))
    
    tower_center_card.draw((1010,60),mpos)
    pygame.display.update()