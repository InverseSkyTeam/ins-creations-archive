import pygame
import time
import sys
import platform

from basic import *
import sight

pygame.init()
pygame.key.stop_text_input()

# 定义常量(用户可以修改设置)
SC_WIDTH = 1000
SC_HEIGHT = 700
BLOCK_SIZE = 50
DROP_SIZE = 30
MP_WIDTH = 100 * BLOCK_SIZE
MP_HEIGHT = 100 * BLOCK_SIZE
WIDTH = int(SC_WIDTH / BLOCK_SIZE)
HEIGHT = int(SC_HEIGHT / BLOCK_SIZE)

if platform.system() == 'Windows':
    font = pygame.font.SysFont('kaiti', 20)
else:
    font = pygame.font.SysFont('kaittf', 20)
def show_text(text,color=(0,0,0),pos=(0,0)):
    screen.blit(font.render((text),True,color),pos)

screen = pygame.display.set_mode((SC_WIDTH,SC_HEIGHT))
pygame.display.set_caption('IDU Sandbox Driver (实变函数版)')



img = pygame.transform.scale(pygame.image.load('./images/土.png'),(BLOCK_SIZE,BLOCK_SIZE))
data = [
    *([[0,None] for i in range(100)] for line in range(10)),
    *([[2,img] for i in range(100)] for line in range(90)),
]

g = 0.15

class Bar:
    def __init__(self,width,site,color,text='text'):
        self.width = width
        self.color = color
        self.text = text
        self.site = site
        self.textsite = (site[0] + 3, site[1])
        self.fullrect = pygame.Rect(self.site, (self.width, 25))
        self.realrect = pygame.Rect(self.site, (self.width, 25))
    def show(self,slider):
        self.realrect.width = self.width * slider.part
        pygame.draw.rect(screen,(128,128,128),self.fullrect,0)
        pygame.draw.rect(screen,self.color,self.realrect,0)
        pygame.draw.rect(screen,(0,0,0),self.fullrect,3)
        show_text(f'{self.text}: {slider.v}/{slider.f}',(0,0,0),self.textsite)

class Player:
    def __init__(self):
        # 位参
        self.x = SC_WIDTH / 2 - 20
        self.y = SC_HEIGHT / 2 - 60
        self.xspeed = 3   # 向右
        self.yspeed = 0   # 向下
        self.hitground = False
        self.rect = pygame.Rect(self.x,self.y,40,120)
        # 属性参
        self.jumpforce = 5
        self.attack = 1
        self.chooserange = 250
        self.hp = Slider(100,100)
        self.hpBar = Bar(200,(10,10),(255,0,0),'HP')
        self.satiety = Slider(100,100)
        self.satietyBar = Bar(200,(10,40),(255,200,0),'ST')
    def bind(self,map_):
        self.map = map_
    
    def move(self):
        # 读取键盘移动意图
        xoffset = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
        xoffset *= self.xspeed
        if self.hitground:
            if keystate[pygame.K_UP]:
                self.hitground = False
                self.yspeed = -self.jumpforce
        else:
            self.yspeed = min(15, self.yspeed + g)
        yoffset = self.yspeed
        
        # 四种情况详细研究碰撞
        bleft, btop = self.map.convert(1,self.x,self.y)
        bright, bbottom = self.map.convert(1,self.x+self.rect.w-1,self.y+self.rect.h-1)
        if xoffset < 0:    # 左右碰到方块限制
            for row in range(btop,bbottom+1):
                if self.map.data[row][bleft-1][0]:
                    delta = self.x - bleft * 50
                    xoffset = -min(-xoffset, delta)
                    break
        elif xoffset > 0:
            for row in range(btop,bbottom+1):
                if self.map.data[row][bright+1][0]:
                    delta = bright * 50 + 50 - self.x - self.rect.w
                    xoffset = min(xoffset, delta)
                    break
        self.x += xoffset    # x移动（提前移动避免出现斜对角卡方块情况）
        self.x = min(max(self.x, 0), MP_WIDTH - 41)
        
        bleft, btop = self.map.convert(1,self.x,self.y)
        bright, bbottom = self.map.convert(1,self.x+self.rect.w-1,self.y+self.rect.h-1)
        self.hitground = False
        if yoffset < 0:    # 上下碰到方块限制
            for col in range(bleft,bright+1):
                if self.map.data[btop-1][col][0]:
                    delta = self.y - btop * 50
                    yoffset = -min(-yoffset, delta)
                    break
        elif yoffset > 0:
            for col in range(bleft,bright+1):
                if self.map.data[bbottom+1][col][0]:
                    delta = bbottom * 50 + 50 - self.y - self.rect.h
                    if yoffset >= delta:
                        yoffset = delta
                        self.hitground = True
                        self.yspeed = 0
                    break
        self.y += yoffset      # y移动
        self.y = min(max(self.y, 0), MP_HEIGHT - 121)
        
        # 在地图边缘自移动
        if self.x < SC_WIDTH / 2 - 20:
            self.rect.x = int(self.x)
        elif self.x >= MP_WIDTH - SC_WIDTH / 2 - 20:
            self.rect.x = int(SC_WIDTH-MP_WIDTH+self.x+1)
        if self.y < SC_HEIGHT / 2 - 60:
            self.rect.y = int(self.y)
        elif self.y >= MP_HEIGHT - SC_HEIGHT / 2 - 60:
            self.rect.y = int(SC_HEIGHT-MP_HEIGHT+self.y+1)
    
    def draw(self):
        pygame.draw.rect(screen,(255,0,0),self.rect,3)
    def draw_info(self):
        self.hpBar.show(self.hp)
        self.satietyBar.show(self.satiety)
    
    @property
    def position(self):
        return [self.x, self.y, self.rect.x, self.rect.y]
    @property
    def center(self):
        return self.rect.center

class GameMap:
    def __init__(self,data):
        self.__keystate = {
            pygame.K_UP: 0, pygame.K_DOWN: 0, pygame.K_LEFT: 0, pygame.K_RIGHT: 0,
            pygame.K_w: 0, pygame.K_s: 0, pygame.K_a: 0, pygame.K_d: 0,
        }
        self.data = data
        self.highlightrect = pygame.Rect(0,0,50,50)
    def include(self,player):
        self.player = player
    
    def convert(self,tp,x,y,scx=None,scy=None):
        if tp == 1:     # 绝对坐标转绝对方块
            return [int(x // 50), int(y // 50)]
        if tp == 2:     # 绝对方块转绝对坐标
            return [x * 50, y * 50]
        if tp == 3:     # 绝对方块转相对坐标
            return [x * 50 - scx, y * 50 - scy]
    
    def draw(self):
        # 绘制
        px, py, psx, psy = self.player.position
        x = min(max(0, px - psx), MP_WIDTH - SC_WIDTH - 1)
        y = min(max(0, py - psy), MP_HEIGHT - SC_HEIGHT - 1)
        bleft, btop = self.convert(1, x, y)
        bright, bbottom = bleft + WIDTH, btop + HEIGHT
        while btop <= bbottom:
            while bleft <= bright:
                image = self.data[btop][bleft][1]
                if image:
                    screen.blit(image,self.convert(3, bleft, btop, x, y))
                bleft += 1
            bleft = bleft - 1 - WIDTH
            btop += 1
        
        # 高亮
        ex, ey = mousestate['pos']
        px, py = self.player.center
        distance = get_distance(ex,ey,px,py)
        if 0 <= ex < SC_WIDTH and 0 <= ey <= SC_HEIGHT and distance <= self.player.chooserange:
            highlight_col, highlight_row = self.convert(1, x+ex, y+ey)
            highbid = self.data[highlight_row][highlight_col][0]
            if highbid:
                border = 3
                if mousestate[1]:
                    self.data[highlight_row][highlight_col] = [0,None]
            else:
                border = 1
                if mousestate[3]:
                    self.data[highlight_row][highlight_col] = [2,img]
            self.highlightrect.topleft = self.convert(3, highlight_col, highlight_row, x, y)
            pygame.draw.rect(screen,(0,0,0),self.highlightrect,border,3)

class SunAct:
    def __init__(self,d,h,suntime):
        self.d = d
        self.h = h
        self.r = self.d / 2
        self.sunrise, self.sunset = suntime
        self.noon = (self.sunrise + self.sunset) / 2
        self.v = self.d / (self.sunset - self.sunrise)
        self.rect = pygame.Rect(0,0,100,100)
        self.sun_pos = False
    def get_sun_pos(self,t):
        '''
        x 与 time 的关系：
            x = (t - noon) / (sunset - sunrise) * d
        y 与 x 的关系：
            圆标准方程（不知道别的什么函数/方程能更好描述天体运动路径了）
        '''
        if t < self.sunrise or t > self.sunset:
            self.sun_pos = False
            return
        x = round((t - self.noon) * self.v)
        y = round((self.r ** 2 - x ** 2) ** 0.5)
        self.sun_pos = (x+self.r, self.h-y)      # 返回的坐标系是数学的，所以改变
    def day(self):
        if self.sun_pos:
            self.rect.center = self.sun_pos
            pygame.draw.rect(screen,(255,0,0),self.rect,0,25)
            pygame.draw.rect(screen,(255,195,111),self.rect,5,25)
    def night(self,t):
        if not self.sun_pos:
            if self.sunrise - 1 <= t <= self.sunrise:
                sightbg_alpha = (self.sunrise - t) * 255
            elif self.sunset <= t <= self.sunset + 1:
                sightbg_alpha = (t - self.sunset) * 255
            else:
                sightbg_alpha = 255
            sightbg.set_alpha(sightbg_alpha)
            screen.blit(sightbg,(0,0))
    def background(self,t):
        # 默认日出日落为6点和18点
        if 6.5 <= t < 16.5:
            color = (255,255,255)
        elif 4.5 <= t < 5:
            delta = t - 4.5
            color = (10+delta*90,10+delta*90,10+delta*300)
        elif 5 <= t < 5.5:
            delta = t - 5
            color = (55+delta*400,55+delta*200,160-delta*200)
        elif 5.5 <= t < 6.5:
            delta = t - 5.5
            color = (255,155+delta*100,60+delta*195)
        elif 16.5 <= t < 17.5:
            delta = t - 16.5
            color = (255,255-delta*100,255-delta*200)
        elif 17.5 <= t < 18:
            delta = t - 17.5
            color = (255-delta*400,155-delta*200,55+delta*300)
        elif 18 <= t < 18.5:
            delta = t - 18
            color = (55-delta*90,55-delta*90,205-delta*390)
        else:
            color = (10,10,10)
        screen.fill(color)



player = Player()
gamemap = GameMap(data)
player.bind(gamemap)
gamemap.include(player)
sun = SunAct(SC_WIDTH,SC_HEIGHT,(6,18))
sightbg = sight.generate_surface(SC_WIDTH,SC_HEIGHT,150,50)
sightbg.set_alpha(0)

clock = pygame.time.Clock()

keystate = {
    pygame.K_UP: 0,
    pygame.K_DOWN: 0,
    pygame.K_LEFT: 0,
    pygame.K_RIGHT: 0,
    pygame.K_w: 0,
    pygame.K_s: 0,
    pygame.K_a: 0,
    pygame.K_d: 0,
}
mousestate = {
    'pos': (-1,-1),
    1: 0,
    3: 0,
}

gamestarttime = time.time()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mousestate['pos'] = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousestate[event.button] = 1
        if event.type == pygame.MOUSEBUTTONUP:
            mousestate[event.button] = 0
        if event.type == pygame.KEYDOWN:
            keystate[event.key] = 1
        if event.type == pygame.KEYUP:
            keystate[event.key] = 0
    
    gametime = (time.time() - gamestarttime) * 1000 / 3600 + 6
    gamedaytime = gametime % 24
    sun.background(gamedaytime)
    
    # 白天（太阳图层在最底下）
    sun.get_sun_pos(gamedaytime)
    sun.day()
    
    gamemap.draw()
    player.move()
    player.draw()
    
    # 黑夜（视野图层在最顶上）
    sun.night(gamedaytime)
    
    player.draw_info()
    
    pygame.display.update()
    clock.tick(100)