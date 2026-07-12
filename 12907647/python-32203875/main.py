import pygame,sys,random
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("高精度碰撞检测示例-小轩and胡锦辉")

r = (255,0,0)
g = (0,255,0)
b = (0,0,255)
l = (0,0,0)

class Dot(object):              # 一个5x5的像素
    def __init__(self,y,x,c):
        self.rect = pygame.Rect(x*5,y*5,5,5)
        self.color = c
    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect,0)

class Hero(object):
    def __init__(self,r,g,b,l,x,y):
        self.x = x / 5
        self.y = y / 5
        self.did = 'none'
        self.shaped()
    def shaped(self):
        self.shape = [
            Dot(self.y+0,self.x+3,g),Dot(self.y+0,self.x+5,g),Dot(self.y+0,self.x+7,g),Dot(self.y+0,self.x+9,g),  # 第0列，第3行
            Dot(self.y+1,self.x+2,g),Dot(self.y+1,self.x+4,g),Dot(self.y+1,self.x+6,l),Dot(self.y+1,self.x+8,l),
            Dot(self.y+2,self.x+3,r),Dot(self.y+2,self.x+5,r),Dot(self.y+2,self.x+7,l),Dot(self.y+2,self.x+9,l),
            Dot(self.y+3,self.x+2,r),Dot(self.y+3,self.x+4,r),Dot(self.y+3,self.x+6,r),Dot(self.y+3,self.x+8,r),
            Dot(self.y+4,self.x+3,b),Dot(self.y+4,self.x+5,b),Dot(self.y+4,self.x+7,b),Dot(self.y+4,self.x+9,b),
            Dot(self.y+5,self.x+2,b),Dot(self.y+5,self.x+4,b),Dot(self.y+5,self.x+6,b),Dot(self.y+5,self.x+8,b),Dot(self.y+5,self.x+9,b),Dot(self.y+5,self.x+10,b),Dot(self.y+5,self.x+11,b),Dot(self.y+5,self.x+12,b),Dot(self.y+5,self.x+13,b),Dot(self.y+5,self.x+14,b),Dot(self.y+5,self.x+15,r),
            Dot(self.y+6,self.x+3,g),Dot(self.y+6,self.x+5,g),Dot(self.y+6,self.x+7,g),Dot(self.y+6,self.x+9,g),
            Dot(self.y+7,self.x+2,g),Dot(self.y+7,self.x+4,g),Dot(self.y+7,self.x+6,g),Dot(self.y+7,self.x+8,g),
            Dot(self.y+8,self.x+3,l),Dot(self.y+8,self.x+5,r),Dot(self.y+8,self.x+7,r),Dot(self.y+8,self.x+9,r),
            Dot(self.y+9,self.x+2,l),Dot(self.y+9,self.x+4,r),Dot(self.y+9,self.x+6,r),Dot(self.y+9,self.x+8,r),
            Dot(self.y+10,self.x+3,l),Dot(self.y+10,self.x+5,b),Dot(self.y+10,self.x+7,b),Dot(self.y+10,self.x+9,b),
            Dot(self.y+11,self.x+2,l),Dot(self.y+11,self.x+4,b),Dot(self.y+11,self.x+6,b),Dot(self.y+11,self.x+8,b),
        ]
    def draw(self):
        for self.i in self.shape:
            self.i.draw()

class Eat(object):   # hjh,我懒得类继承了，直接复制粘贴了
    def __init__(self,r,g,b,l,x,y):
        self.x = x / 5
        self.y = y / 5
        self.shaped()
    def shaped(self):
        self.shape = [
            Dot(self.y+0,self.x+3,g),Dot(self.y+0,self.x+5,g),Dot(self.y+0,self.x+7,g),Dot(self.y+0,self.x+9,g),
            Dot(self.y+1,self.x+2,g),Dot(self.y+1,self.x+4,g),Dot(self.y+1,self.x+6,g),Dot(self.y+1,self.x+8,g),
            Dot(self.y+2,self.x+3,l),Dot(self.y+2,self.x+5,l),Dot(self.y+2,self.x+7,l),Dot(self.y+2,self.x+9,l),Dot(self.y+2,self.x+10,l),Dot(self.y+2,self.x+11,l),
            Dot(self.y+3,self.x+2,l),Dot(self.y+3,self.x+4,l),Dot(self.y+3,self.x+6,l),Dot(self.y+3,self.x+8,l),Dot(self.y+3,self.x+10,l),Dot(self.y+3,self.x+11,l),
        ]
    def draw(self):
        self.shaped()
        for self.i in self.shape:
            self.i.draw()

hero = Hero(r,g,b,l,0,0)
food = Eat(r,g,b,l,800,400)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == ord('w'):
                hero.did = 'up'
            if event.key == ord('s'):
                hero.did = 'down'
            if event.key == ord('a'):
                hero.did = 'left'
            if event.key == ord('d'):
                hero.did = 'right'
        if event.type == pygame.KEYUP:
            hero.did = 'none'
    screen.fill((255,255,255))
    food.x -= 0.025
    if food.x < 5:
        food.x = 160 # 800/5
    food.draw()
    if hero.did == 'up':
        hero.y -= 0.1
        hero.shaped()
    if hero.did == 'down':
        hero.y += 0.1
        hero.shaped()
    if hero.did == 'left':
        hero.x -= 0.1
        hero.shaped()
    if hero.did == 'right':
        hero.x += 0.1
        hero.shaped()
    hero.draw()
    for i in hero.shape:
        for x in food.shape:
            if i.rect.colliderect(x.rect):
                food = Eat(r,g,b,l,800,random.randint(1,500))
    if food.shape == []:
        food = Eat(r,g,b,l,800,random.randint(1,500))
    pygame.display.update()