from math import *
import pygame
import sys
import time
import random

pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("INS-GameBox:保卫逆天塔防")

towerlist = []
def add_tower(x,y,rindex):
    global towerlist
    towerlist.append(Tower(x,y,rindex))

def ctc(a,b):  # calc_triangle_linec
    return sqrt(abs(a)**2+abs(b)**2)

class Floor(object):          # class Floor():或者class Floor:都行，这里是装逼
    def __init__(self,moveid,rect_index):
        self.rectindex = rect_index
        self.rect = pygame.Rect(self.rectindex%25*40,self.rectindex//25*40,40,40)
        self.color = (225,255,255)
        self.move_tip = {'w':'up','s':'down','a':'left','d':'right','0':'none'}[moveid]
    def show(self,pos,clicked):
        if self.move_tip != 'none':
            pygame.draw.rect(screen,self.color,self.rect,0)
        elif self.rect.collidepoint(pos):
            pygame.draw.rect(screen,(255,240,220),self.rect,0)
            if clicked:
                self.move_ip = 'powered'
                add_tower(self.rect.x,self.rect.y,self.rectindex)

class MainGameMap(object):
    def __init__(self,the_map):
        self.map = []
        for self.i in range(len(the_map)):
            self.map.append(Floor(the_map[self.i],self.i))
    def show(self,pos,clicked):
        for self.i in self.map:
            self.i.show(pos,clicked)

class Enemy(object):
    def __init__(self,the_map):
        self.rect = pygame.Rect(40,80,40,40)
        self.go_where = 'none'
        self.mapp = the_map
        self.startup_hp = 10
        self.HP = self.startup_hp
        self.update_health()
    def update_go(self):
        for self.i in self.mapp:
            if self.rect.topleft == self.i.rect.topleft:
                self.go_where = self.i.move_tip
    def update_health(self):
        self.healthlinef = pygame.Rect(self.rect.x,self.rect.y-4,40,3)
        self.healthline = pygame.Rect(self.rect.x,self.rect.y-4,40 / self.startup_hp * self.HP,3)
    def move(self):
        self.update_go()
        self.update_health()
        if self.go_where == 'up':
            self.rect.y -= 1
        if self.go_where == 'down':
            self.rect.y += 1
        if self.go_where == 'left':
            self.rect.x -= 1
        if self.go_where == 'right':
            self.rect.x += 1
    def is_out(self):
        if self.rect.topleft == (920,40) or self.HP <= 0:
            return True
        else:
            return False
    def show(self):
        pygame.draw.rect(screen,(0,0,255),self.rect,0)
        pygame.draw.rect(screen,(255,0,0),self.healthlinef,0)
        pygame.draw.rect(screen,(0,255,0),self.healthline,0)

class Bullet(object):
    def __init__(self,pos,enemy,erc):
        self.rect = pygame.Rect(0,0,10,10)
        self.rect.center = pos
        self.color = (255,0,0)
        self.attack = 1
        self.speed = 5
        self.enemy = enemy
        self.ercx = erc[0]
        self.ercy = erc[1]
    def move(self):
        if self.rect.centerx < self.ercx:
            self.rect.centerx += self.speed
        else:
            self.rect.centerx -= self.speed
        if self.rect.centery < self.ercy:
            self.rect.centery += self.speed
        else:
            self.rect.centery -= self.speed
        if abs(self.rect.centery - self.ercy) <= 5:
            return True
        else:
            return False
    def hit(self):
        if self.rect.colliderect(self.enemy.rect):
            return True
        else:
            return False
    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect,0)

class Tower(object):
    def __init__(self,x,y,myfloor):
        self.rect = pygame.Rect(x,y,40,40)
        self.color = (0,255,0)
        self.attack = 1
        self.bulletlist = []
        self.bulletwaittime = 0.2
        self.bulletwaittimeget = time.time()
    def draw(self):
        for i in self.bulletlist:
            i.draw()
        pygame.draw.rect(screen,self.color,self.rect,0)

# 第一关地图
game_map1 = [
    '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
    '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','w','0',
    '0','d','d','d','d','d','d','d','d','d','s','0','0','0','0','0','0','0','0','0','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','s','0','0','0','0','0','0','0','0','0','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','s','0','0','0','0','d','d','d','d','s','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','s','0','0','0','0','w','0','0','0','s','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','s','0','0','0','0','w','0','0','0','s','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','s','0','0','0','0','w','0','0','0','s','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','s','0','0','0','0','w','0','0','0','s','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','s','0','0','0','0','w','0','0','0','s','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','s','0','0','0','0','w','0','0','0','s','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','d','d','d','d','d','w','0','0','0','d','d','d','d','w','0',
    '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
    '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
    '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
    ]
main_game_map1 = MainGameMap(game_map1)
enemylist = [Enemy(main_game_map1.map)]
tt = time.time()
tt2 = time.time()
tickclock = pygame.time.Clock()
eventpos = (-1,-1)
is_click = False



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            eventpos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                is_click = True
        if event.type == pygame.MOUSEBUTTONUP:
            is_click = False
    screen.fill((255,255,255))
    if time.time() - tt > 1:
        tt = time.time()
        enemylist.append(Enemy(main_game_map1.map))
    main_game_map1.show(eventpos,is_click)
    for i in towerlist:
        i.draw()
    for i in enemylist:
        i.move()
        i.show()
        if i.is_out():
            enemylist.remove(i)
    for e in enemylist:
        for t in towerlist:
            if ctc(e.rect.centerx-t.rect.centerx, e.rect.centery-t.rect.centery) < 60:
                if time.time() - t.bulletwaittimeget > t.bulletwaittime:
                    t.bulletlist.append(Bullet(t.rect.center,e,e.rect.center))
                    t.bulletwaittimeget = time.time()
                for b in t.bulletlist:
                    if b.move():
                        try:
                            t.bulletlist.remove(b)
                        except:
                            pass
                    if b.hit() and b.enemy == e:
                        try:
                            t.bulletlist.remove(b)
                        except:
                            pass
                        e.HP -= 0.5
    pygame.display.update()
    tickclock.tick(100)