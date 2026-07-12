import pygame
import sys
import os
import platform
import copy
import time
import random

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

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
pygame.display.set_caption('INS DreamUniverse 逆天团队-联梦宇宙')
screen_width, screen_height = screen.get_size()
screen_left, screen_top = (screen_width - 1200) / 2, (screen_height - 800) / 2
screen_right, screen_bottom = screen_width - screen_left , screen_height - screen_top

play_window = pygame.Rect(screen_left,screen_top,1200,800)
play_rect = pygame.Rect(screen_left+300,screen_bottom-400,600,300)
health_rect = pygame.Rect(play_rect.left+330,play_rect.bottom+12,184,30)
health_rect_now = pygame.Rect(play_rect.left+330,play_rect.bottom+12,184,30)

QuestionSquare = pygame.Rect(0,screen_top+60,150,150)
QuestionSquare.centerx = screen_left+600
QuestionSquare_color = (255,233,111)
def QuestionSquare_show_que(symbol='?'):
    show_text(symbol,
              QuestionSquare_color,
              (QuestionSquare.x+50,QuestionSquare.y+25),
              size=100)

class Player(object):
    def __init__(self,hp,limiter,hurtw=0.2):
        self.state_red = pygame.image.load('./PlayerHeart/red.png')
        self.state_blue = pygame.image.load('./PlayerHeart/blue.png')
        self.state_die = pygame.image.load('./PlayerHeart/die.png')
        self.state = copy.copy(self.state_red)
        self.limiter = limiter
        self.rect = self.state_red.get_rect()
        self.rect.center = self.limiter.center
        self.speed = 6
        self.to = [0,0,0,0]
        self.hp = hp
        self.dying_t = 0
        self.over = False
        self.hurt_time = time.time()
        self.hurt_wait = hurtw
    def move(self):
        if self.to[0]: self.rect.y -= self.speed
        if self.to[1]: self.rect.y += self.speed
        if self.to[2]: self.rect.x -= self.speed
        if self.to[3]: self.rect.x += self.speed
    def limit(self):
        if self.rect.left < self.limiter.left + 10:
            self.rect.left = self.limiter.left + 10
        elif self.rect.right > self.limiter.right - 10:
            self.rect.right = self.limiter.right - 10
        if self.rect.top < self.limiter.top + 10:
            self.rect.top = self.limiter.top + 10
        elif self.rect.bottom > self.limiter.bottom - 10:
            self.rect.bottom = self.limiter.bottom - 10
        if self.hp <= 0:
            self.hp = 0
    def check_hp(self):
        if not self.dying_t:
            if self.hp <= 0:
                self.hp = 0
                self.state = self.state_die
                self.dying_t = time.time()
        else:
            if time.time() - self.dying_t > 1.5:
                self.over = True
    def hurt(self,hp):
        if time.time() - self.hurt_time > self.hurt_wait:
            self.hp -= hp
            self.hurt_time = time.time()
    def draw(self):
        screen.blit(self.state,self.rect)
    def auto(self):
        self.move()
        self.limit()
        self.check_hp()
        self.draw()

class Laser(object):
    def __init__(self,x,y,to,size=100,wait=(0.5,0.4)):
        self.size = size
        self.rect = pygame.Rect(x,y,self.size,self.size)
        self.state = 0  # 未发射
        self.used = 0  # 未使用
        self.to = to
        self.wait = wait[0]
        self.waitend = wait[1]
        self.started = 0
        self.locked = 0
        self.symbol = random.choice(['?','!','#',':'])
        if self.to == 'left':
            self.set_laser('row')
            self.laser_rect.right = self.rect.centerx
        elif self.to == 'right':
            self.set_laser('row')
            self.laser_rect.left = self.rect.centerx
        elif self.to == 'top':
            self.set_laser('col')
            self.laser_rect.bottom = self.rect.centery
        else:
            self.set_laser('col')
            self.laser_rect.top = self.rect.centery
    def set_start(self):
        self.started = 1
        self.start = time.time()
    def set_laser(self,tp):
        if tp == 'row':
            self.laser_rect = pygame.Rect(0,0,1500,self.size-30)
            self.laser_rect.centery = self.rect.centery
        else:
            self.laser_rect = pygame.Rect(0,0,self.size-30,1500)
            self.laser_rect.centerx = self.rect.centerx
    def hit(self,player):
        if self.laser_rect.colliderect(player.rect) and self.state:
            return True
        return False
    def lock(self,player):
        if not self.locked:
            self.locked = 1
            if self.to in ('left','right'):
                self.laser_rect.centery = self.rect.centery = player.rect.centery
            else:
                self.laser_rect.centerx = self.rect.centerx = player.rect.centerx
    def draw(self):
        if self.state:
            pygame.draw.rect(screen,(255,15,5),self.laser_rect,0)
        pygame.draw.rect(screen,(255,245,100),self.rect,0)
        pygame.draw.rect(screen,(50,50,50),self.rect,3)
        if self.state:
            # 60是最好拆分、因数很多的整十数，用它真香
            show_text(self.symbol,color=(255,0,111),pos=(self.rect.centerx-15,self.rect.centery-30),size=60)
    def auto(self,player):
        if not self.started:
            self.set_start()
        if not self.used:
            if self.state:
                if time.time() - self.start > self.waitend:
                    self.state = 0
                    self.used = 1
                    self.waitend = 65535  # 限制不再进入此分支
            else:
                if time.time() - self.start > self.wait:
                    self.start = time.time()
                    self.state = 1
                    self.wait = 65535
        self.draw()
        if self.hit(player):
            player.hurt(random.randint(1,4))

player = Player(92,play_rect)
clock = pygame.time.Clock()

laser_list = [
                Laser(
                    play_rect.left-120,
                    random.randint(play_rect.top,play_rect.bottom-100),
                    'right',
                ) for i in range(30)
             ]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:    player.to[0] = 1
            if event.key == pygame.K_DOWN:  player.to[1] = 1
            if event.key == pygame.K_LEFT:  player.to[2] = 1
            if event.key == pygame.K_RIGHT: player.to[3] = 1
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:    player.to[0] = 0
            if event.key == pygame.K_DOWN:  player.to[1] = 0
            if event.key == pygame.K_LEFT:  player.to[2] = 0
            if event.key == pygame.K_RIGHT: player.to[3] = 0
    
    screen.fill((11,11,11))
    show_text(f'FPS: {round(clock.get_fps())}',pos=(11,11),color=(255,255,255))
    show_text('YOU  LV.19',pos=(play_rect.left,play_rect.bottom+10),color=(255,255,255))
    show_text('HP',pos=(health_rect.left-45,play_rect.bottom+10),color=(255,255,255))
    show_text(f'{player.hp}/92',pos=(health_rect.right+15,play_rect.bottom+10),color=(255,255,255))
    
    pygame.draw.rect(screen,(0,66,111),play_window,11,border_radius=30)
    pygame.draw.rect(screen,QuestionSquare_color,QuestionSquare,6,border_radius=15)
    pygame.draw.rect(screen,(255,255,255),play_rect,10)
    pygame.draw.rect(screen,(210,20,0),health_rect,0)
    pygame.draw.rect(screen,(255,240,0),health_rect_now,0)
    health_rect_now.width = player.hp * 2
    
    QuestionSquare_show_que()
    player.auto()
    
    if player.over:
        gamepart = 'over'
        break
    
    if laser_list:
        if len(laser_list) <= 10:
            laser_list[0].lock(player)
        laser_list[0].auto(player)
        if laser_list[0].used:
            del laser_list[0]
    else:
        gamepart = 'win'
        break
    
    pygame.display.update()
    clock.tick(80)

print('第2版体验结束')
print('赢了' if gamepart == 'win' else '输了')