# block index:
'''
1.草，叶子(ok)
2.土地(ok)
3.河水
4.木
5.火，岩浆
6.矿
7.金
8.咔咔石
9.结界紫钻
10.普通石
11.砖
'''
import pygame,sys,random
pygame.init()

screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption('普通沙盒')

class Block:
    def __init__(self,x,y):
        self.rect = pygame.Rect((x,y,20,20))
        self.color = (211,238,238)
    def set_index(self,index=1):
        if index == 1:
            self.color = (15,255,65)
            self.hard = 1
        elif index == 2:
            self.color = (185,145,15)
            self.hard = 2
    def move(self,index,speed):
        if index[0] == 1:
            self.rect.x -= speed
        elif index[0] == 2:
            self.rect.x += speed
        if index[1] == 1:
            self.rect.y -= speed
        elif index[1] == 2:
            self.rect.y += speed
    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect,0)
        pygame.draw.rect(screen,(0,0,0),self.rect,1)

class World:
    def __init__(self,w=100,h=35,b=500):
        self.bnum = b
        self.set_speed()
        self.index = [0,0]
        if self.bnum < w*7:
            b = w*7
            self.bnum = b
        self.bsite = [0,h-7]
        self.blist = [[0 for i in range(w)] for i in range(h)]
        self.is_onclick = 0
        while self.bnum:
            if b-self.bnum >= w*7:
                xpos = random.randint(0,w-1)
                ypos = random.choice([
                        random.randint(int(h/4*3),h-1),
                        random.randint(int(h/4*3),h-1),
                        random.randint(int(h/3*2),h-1),
                        random.randint(int(h/3*2),h-1),
                        random.randint(int(h/3*2),h-1),
                        random.randint(int(h/3*2),h-1),
                        random.randint(int(h/3*2),h-1),
                        random.randint(int(h/3*2),h-1),
                        random.randint(int(h/2),h-1),
                    ])
            else:
                xpos,ypos = self.bsite
                self.bsite[0] += 1
                if self.bsite[0] == w:
                    self.bsite[0] = 0
                    self.bsite[1] += 1
            if not self.blist[ypos][xpos]:
                self.blist[ypos][xpos] = Block(x=20*xpos,y=20*ypos)
                self.bnum -= 1
        for ypos in range(len(self.blist)):
            for xpos in range(len(self.blist[ypos])):
                if self.blist[ypos][xpos]:
                    if ypos == 0 or (not self.blist[ypos-1][xpos]):
                        blockindex = 1
                    else:
                        blockindex = 2
                    self.blist[ypos][xpos].set_index(blockindex)
        self.setup_pos()
    
    def set_speed(self,speed=2):
        self.movespeed = speed
    
    def move(self,key):
        if key == pygame.K_LEFT:
            self.index[0] = 2
        elif key == pygame.K_RIGHT:
            self.index[0] = 1
        elif key == pygame.K_UP:
            self.index[1] = 2
        elif key == pygame.K_DOWN:
            self.index[1] = 1
    
    def onclick(self,p):
        for i in self.blist:
            for j in i:
                if j and j.rect.collidepoint(p):
                    self.is_onclick = j
                    return
        self.is_onclick = 0
    
    def clicked(self,p,attackblock):
        for i in range(len(self.blist)):
            for j in range(len(self.blist[i])):
                if self.blist[i][j] and self.blist[i][j].rect.collidepoint(p):
                    self.blist[i][j].hard -= attackblock
                    if self.blist[i][j].hard <= 0:
                        self.blist[i][j] = 0
                        return
    
    def setup_pos(self,size=20):    # size:调整时向上移动区间值，默认一个方块
        while self.blist[-1][0].rect.y >= 700:
            for i in self.blist:
                for j in i:
                    if j:
                        j.move([0,1],size)
    
    def moveip(self):
        for i in self.blist:
            for j in i:
                if j:
                    j.move(self.index,self.movespeed)
        return self.back_side()
    
    def back_side(self):
        is_back = 0
        if self.blist[-1][0].rect.x > 0:
            is_back = 1
            delta = self.blist[-1][0].rect.x
            for i in self.blist:
                for j in i:
                    if j:
                        j.move([1,0],delta)
        if self.blist[-1][-1].rect.x < 1000:
            is_back = 1
            delta = 1000-self.blist[-1][-1].rect.x
            for i in self.blist:
                for j in i:
                    if j:
                        j.move([2,0],delta)
        if self.blist[-1][-1].rect.y < 680:
            is_back = 1
            delta = 680-self.blist[-1][-1].rect.y
            for i in self.blist:
                for j in i:
                    if j:
                        j.move([0,2],delta)
        return is_back
    
    def stop(self,key):
        if key == pygame.K_LEFT:
            self.index[0] = 0
        elif key == pygame.K_RIGHT:
            self.index[0] = 0
        elif key == pygame.K_UP:
            self.index[1] = 0
        elif key == pygame.K_DOWN:
            self.index[1] = 0
    
    def draw(self):
        for i in self.blist:
            for j in i:
                if j:
                    j.draw()

class Bio:
    def __init__(self,w=1,h=2,c=(0,255,0),border=(1,0,0,255),HP=100,attack=20,de=5,s=2):
        self.w = w
        self.h = h
        self.rect = pygame.Rect(0,0,w*20,h*20)
        self.color = c
        self.bsize = border[0]
        self.bcolor = (border[1],border[2],border[3])
        self.fullHP = HP
        self.HP = HP
        self.attack = attack
        self.de = de   # 防御
        self.speed = s
        self.index = [0,0]
    def moveip(self):
        if self.index[0] == 1:
            self.rect.x -= self.speed
        elif self.index[0] == 2:
            self.rect.x += self.speed
        if self.index[1] == 1:
            self.rect.y -= self.speed
        elif self.index[1] == 2:
            self.rect.y += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1000:
            self.rect.right = 1000
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 700:
            self.rect.bottom = 700
    def drop(self,world):
        self.droping = 1
        coll = 0
        if world.blist[-1][0].rect.bottom > 700:
            for i in world.blist:
                for j in i:
                    if j and j.rect.colliderect(self.rect):
                        coll = 1
                        break
        for i in world.blist:
            for j in i:
                if j:
                    j.move([0,1],world.movespeed)
        if coll:
            for i in world.blist:
                for j in i:
                    if j:
                        j.move([0,2],world.movespeed)
            self.droping = 0
            return
        
        if world.blist[-1][0].rect.bottom <= 700:
            self.rect.y += self.speed
            for i in world.blist:
                for j in i:
                    if j and j.rect.colliderect(self.rect):
                        self.droping = 0
                        self.rect.y -= self.speed
                        return
    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect,0)
        pygame.draw.rect(screen,self.bcolor,self.rect,self.bsize)

class People(Bio):
    def __init__(self,c=(0,255,0),border=(1,0,0,255),HP=120,attack=25,de=3,s=2):
        super().__init__(c=c,border=border,HP=HP,attack=attack,de=de,s=s)

class Player(People):
    def __init__(self,HP=120,attack=25,de=5,s=2):
        super().__init__(c=(11,235,158),border=(2,190,130,11),HP=HP,attack=attack,de=de,s=s)
        self.setup()
        self.jumping = 0
        self.droping = 0
        self.ablock = 1
        self.bag = [0 for i in range(1,6)]
    def setup(self):
        self.rect.x = 490
    def move2d(self,world_dont_move):
        if world_dont_move:
            self.moveip()
    def move(self,key):
        if key == pygame.K_LEFT:
            self.index[0] = 1
        elif key == pygame.K_RIGHT:
            self.index[0] = 2
        elif key == pygame.K_UP and not self.droping:
            self.jumping = 1
            self.index[1] = 1
        elif key == pygame.K_DOWN:
            self.index[1] = 2
    def stop(self,key):
        if key == pygame.K_LEFT:
            self.index[0] = 0
        elif key == pygame.K_RIGHT:
            self.index[0] = 0
        elif key == pygame.K_UP:
            self.jumping = 0
            self.index[1] = 0
        elif key == pygame.K_DOWN:
            self.index[1] = 0

world = World(b=5000,w=300,h=45)
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            world.move(event.key)
            player.move(event.key)
        if event.type == pygame.KEYUP:
            world.stop(event.key)
            player.stop(event.key)
        if event.type == pygame.MOUSEMOTION:
            world.onclick(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                world.clicked(event.pos,player.ablock)
                break
    screen.fill((255,255,255))
    world.draw()
    if world.is_onclick:
        pygame.draw.rect(screen,(255,111,88),world.is_onclick.rect,3)
    player.draw()
    player.move2d(world.moveip())
    if not player.jumping:
        player.drop(world)
    pygame.display.update()