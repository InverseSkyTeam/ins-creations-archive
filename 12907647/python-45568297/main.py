import pygame
import sys
import os
import platform
import copy
import time

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
    def __init__(self,hp,limiter):
        self.state_red = pygame.image.load('./PlayerHeart/red.png')
        self.state_blue = pygame.image.load('./PlayerHeart/blue.png')
        self.state_die = pygame.image.load('./PlayerHeart/die.png')
        self.state = copy.copy(self.state_red)
        self.limiter = limiter
        self.rect = self.state_red.get_rect()
        self.rect.center = self.limiter.center
        self.speed = 5
        self.to = [0,0,0,0]
        self.hp = hp
        self.dying_t = 0
        self.over = False
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
    def check_hp(self):
        if not self.dying_t:
            if self.hp <= 0:
                self.hp = 0
                self.state = self.state_die
                self.dying_t = time.time()
        else:
            if time.time() - self.dying_t > 1.5:
                self.over = True
    def draw(self):
        screen.blit(self.state,self.rect)
    def auto(self):
        self.move()
        self.limit()
        self.check_hp()
        self.draw()

player = Player(92,play_rect)
clock = pygame.time.Clock()

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
            
            # 临时代码
            if '第1版临时代码':
                if event.key == pygame.K_a: player.hp -= 10
                if event.key == pygame.K_s: player.hp += 10
            # 临时结束
            break
            
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
    
    # 临时代码
    if '第1版临时代码':
        show_text('上下左右移动(undertale原版)，s/a加减血量(临时测试)',pos=(11,45),color=(111,255,255))
    # 临时结束
    
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
    
    pygame.display.update()
    clock.tick(100)

print('第1版体验结束')