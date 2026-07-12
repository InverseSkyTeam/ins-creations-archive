import pygame
import sys
from random import randint as r

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('IDU_main2d_block_object')

block_list = [
    '空气',
    {'name': '草',
     'image': None,
     'hard': 1},
    {'name': '土',
     'image': None,
     'hard': 2},
    {'name': '铁',
     'image': None,
     'hard': 5},
]
for i in block_list:
    if type(i) == dict:
        i['image'] = pygame.image.load(f'./方块-{i["name"]}.png')

class Block(pygame.Rect):
    def __init__(self,bid=0,x=0,y=0,w=50,h=50):
        super().__init__(x,y,w,h)
        self.ID = bid
        self.state = 'normal'
        self.image = block_list[bid]['image']
    def draw(self,screen):
        screen.blit(self.image,self)
        if self.state == 'normal':
            pygame.draw.rect(screen,(0,0,0),self,1)
        else:
            pygame.draw.rect(screen,(0,0,0),self,2)

block1 = Block(1,60,10)
block2 = Block(2,110,10)
block3 = Block(3,160,10)
a = [Block(1,1000,1000) for i in range(10000)]
clock = pygame.time.Clock()
print('\033[?25l')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            if block1.collidepoint(event.pos):
                block1.state = 'on'
            else:
                block1.state = 'normal'
            if block2.collidepoint(event.pos):
                block2.state = 'on'
            else:
                block2.state = 'normal'
            if block3.collidepoint(event.pos):
                block3.state = 'on'
            else:
                block3.state = 'normal'
    
    screen.fill((255,255,255))
    block1.draw(screen)
    block2.draw(screen)
    block3.draw(screen)
    for i in a:
        i.draw(screen)
    if not r(0,10):print(f'\033[100A\033[2J\033[100A方块个数:10004\nfps:{clock.get_fps()}')
    
    pygame.display.update()
    clock.tick()