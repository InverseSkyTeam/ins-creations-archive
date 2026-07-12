import pygame
import time
import sys
import platform
import sight

pygame.init()
pygame.key.stop_text_input()

# 定义常量(用户可以修改设置)
SC_WIDTH = 1000
SC_HEIGHT = 700
BLOCK_SIZE = 50
DROP_SIZE = 30
MP_WIDTH = 100 * BLOCK_SIZE
MP_HEIGHT = 111 * BLOCK_SIZE
WIDTH = int(SC_WIDTH / BLOCK_SIZE)
HEIGHT = int(SC_HEIGHT / BLOCK_SIZE)

print(f'''[INFO]
窗口大小: {SC_WIDTH}x{SC_HEIGHT}={SC_WIDTH*SC_HEIGHT}px
地图大小: {MP_WIDTH}x{MP_HEIGHT}={MP_WIDTH*MP_HEIGHT}px
地图方块: 100x111=11100个
单个方块: 50x50=2500px
掉落物: 30x30=900px
wsad/up down left right移动
(fps/xpos/ypos在窗口标题显示)
Version dev-3 随fps跟踪速度
Version dev-3.1 修复光标bug
Version dev-3.2 血条
Version dev-3.3 掉落物1
Version dev-3.4 方块硬度
Version dev-3.5 鼠标事件更新
Version dev-3.6 血条提前
Version dev-3.7 调参，避免无故卡墙
Version dev-3.8 选择范围
Version dev-4 掉落物2(未制作)
''')

screen = pygame.display.set_mode((SC_WIDTH,SC_HEIGHT))
pygame.display.set_caption('IDU Sandbox Driver')

if platform.system() == 'Windows':
    font = pygame.font.SysFont('kaiti', 20)
else:
    font = pygame.font.SysFont('kaittf', 20)
def show_text(text,color=(0,0,0),pos=(0,0)):
    screen.blit(font.render((text),True,color),pos)

def get_distance(x1,x2,y1,y2):
    return ((x1-x2)**2 + (y1-y2)**2) ** 0.5

i1 = pygame.image.load('./images/草地.png')
i2 = pygame.image.load('./images/土.png')
i3 = pygame.image.load('./images/石块.png')
images = {
    0: [None,None,0],
    1: [pygame.transform.scale(i1,(BLOCK_SIZE,BLOCK_SIZE)),
        pygame.transform.scale(i2,(DROP_SIZE,DROP_SIZE)),
        8,
       ],
    2: [pygame.transform.scale(i2,(BLOCK_SIZE,BLOCK_SIZE)),
        pygame.transform.scale(i2,(DROP_SIZE,DROP_SIZE)),
        10,
       ],
    3: [pygame.transform.scale(i3,(BLOCK_SIZE,BLOCK_SIZE)),
        pygame.transform.scale(i3,(DROP_SIZE,DROP_SIZE)),
        35,
       ],
}
data = [*([[0,images[0][2]] for i in range(100)] for line in range(10)),
        [[1,images[1][2]] for i in range(100)],
        *([[2,images[2][2]] for i in range(100)] for line in range(35)),
        *([[3,images[3][2]] for i in range(100)] for line in range(65)),]

class Life:
    pass

class Line:
    def __init__(self,full,width,site,color,text='line'):
        self.full = full
        self.width = width
        self.color = color
        self.text = text
        self.site = site
        self.textsite = (site[0] + 3, site[1])
        self.fullrect = pygame.Rect(self.site,(self.width,25))
        self.realrect = pygame.Rect(self.site,(self.width,25))
    def show(self,value):
        self.realrect.width = self.width * value / self.full
        pygame.draw.rect(screen,(128,128,128),self.fullrect,0)
        pygame.draw.rect(screen,self.color,self.realrect,0)
        pygame.draw.rect(screen,(0,0,0),self.fullrect,3)
        show_text(f'{self.text}: {value}/{self.full}',(0,0,0),self.textsite)

# 玩家内核
class Player:
    def __init__(self):
        self.hp = 100
        self.rect = pygame.Rect(0,0,40,120)
        self.rect.center = (SC_WIDTH/2,SC_HEIGHT/2)
        self.jumplity = 5      # 跳跃系数，越大越能跳高
        self.chooserange = 250     # 选择范围
        self.speed = 5
        self.attack = 1
        self.line_hp = Line(self.hp,200,(0,0),(255,0,0),'hp')
    def change_hp(self,value):
        self.hp = round(self.hp+value,1)
    def draw(self):
        pygame.draw.rect(screen,(255,0,0),self.rect,3)
    def draw_info(self):
        self.line_hp.show(self.hp)

# 地图（也算是游戏引擎类吧doge）
class GameMap:
    # 初始化
    def __init__(self,data,player):
        self.__state = 'unclick'
        self.__keystate = {
            pygame.K_UP: 0, pygame.K_DOWN: 0, pygame.K_LEFT: 0, pygame.K_RIGHT: 0,
            pygame.K_w: 0, pygame.K_s: 0, pygame.K_a: 0, pygame.K_d: 0,
            pygame.K_q: 0,    # 背包
            pygame.K_e: 0,    # 合成
        }
        self.data = data
        self.offset_x = 0
        self.offset_y = 0
        self.choose_bid = None
        self.choose_rect = pygame.Rect(0,0,BLOCK_SIZE,BLOCK_SIZE)
        self.player = player
        self.player_on_ground = False
        self.Fy = 0
    
    # 基础功能
    def state(self,s):
        self.__state = s
    def keyin(self,k,s):
        self.__keystate[k] = s
    def get_id(self,pos):
        col = round((self.offset_x + pos[0]) // BLOCK_SIZE)
        row = round((self.offset_y + pos[1]) // BLOCK_SIZE)
        return (row,col)
    def get_pos(self,row,col):
        if (row >= len(self.data)) or (col >= len(self.data[row])):
            return None
        x = col * BLOCK_SIZE - self.offset_x
        y = row * BLOCK_SIZE - self.offset_y
        return (x,y)
    
    # 光标选择
    def choose(self,epos):
        if 0 <= epos[0] <= SC_WIDTH and 0 <= epos[1] <= SC_HEIGHT:
            self.choose_bid = self.get_id(epos)
            self.choose_rect.topleft = self.get_pos(*self.choose_bid)
        else:
            self.choose_bid = None
    
    # 背包
    def backpack(self):
        ...
    # 合成
    def craft(self):
        ...
    
    # 事件处理专区
    def handle_event(self):
        # 测定player四个角所在的位置
        p_lt_site = self.get_id(self.player.rect.topleft)
        p_lb_site = self.get_id(self.player.rect.bottomleft)
        p_rt_site = self.get_id(self.player.rect.topright)
        p_rb_site = self.get_id(self.player.rect.bottomright)
        
        # 键盘移动
        ks = self.__keystate
        x_movement = ks[pygame.K_RIGHT] + ks[pygame.K_d] \
                   - ks[pygame.K_LEFT] - ks[pygame.K_a]
        if self.player_on_ground:     # 在地上，能跳
            self.Fy = ks[pygame.K_UP] | ks[pygame.K_w]
        else:     # 不在地上，按力落体
            self.Fy -= 0.05
        self.Fy = max(min(self.Fy,6),-6)
        y_movement = self.Fy * self.player.jumplity
        x_movement *= self.player.speed
        x_movement *= expect_fps / real_fps
        
        self.player_on_ground = False
        if x_movement < 0:
            col = p_lt_site[1] - 1
            for row in range(p_lt_site[0],p_lb_site[0]+1):
                if data[row][col][0]:
                    maxleft = self.player.rect.left - (self.get_pos(row,col)[0] + BLOCK_SIZE)
                    x_movement = -min(maxleft,-x_movement)
                    break
        elif x_movement > 0:
            col = p_rt_site[1] + 1
            for row in range(p_rt_site[0],p_rb_site[0]+1):
                if data[row][col][0]:
                    maxright = self.get_pos(row,col)[0] - self.player.rect.right - 1
                    x_movement = min(maxright,x_movement)
                    break
        if y_movement < 0:
            row = p_lb_site[0] + 1
            for col in range(p_lb_site[1],p_rb_site[1]+1):
                if data[row][col][0]:
                    maxdown = self.get_pos(row,col)[1] - self.player.rect.bottom - 1
                    y_movement = -min(maxdown,-y_movement)
                    if y_movement == 0:
                        self.player_on_ground = True
                        if self.Fy < -3:       # 摔地扣血
                            self.player.change_hp((self.Fy+3) * 30)
                    break
        elif y_movement > 0:
            row = p_lt_site[0] - 1
            for col in range(p_lt_site[1],p_rt_site[1]+1):
                if data[row][col][0]:
                    maxup = self.player.rect.top - (self.get_pos(row,col)[1] + BLOCK_SIZE)
                    y_movement = min(maxup,y_movement)
                    break
        
        self.offset_x += x_movement
        self.offset_y -= y_movement
        self.offset_x = max(min(self.offset_x, MP_WIDTH - SC_WIDTH - 1), 0)
        self.offset_y = max(min(self.offset_y, MP_HEIGHT - SC_HEIGHT - 1), 0)
        
        # 按键对应的拓展
        if ks[pygame.K_q]:
            self.backpack()    # 打开背包
        if ks[pygame.K_e]:
            self.craft()    # 合成
        
        # 光标选择
        self.choose(evt_pos)
    
    # 绘制地图
    def show(self):
        left = round(self.offset_x // BLOCK_SIZE)
        top = round(self.offset_y // BLOCK_SIZE)
        for row in range(top, top + HEIGHT + 1):
            for col in range(left, left + WIDTH + 1):
                b = self.data[row][col]
                img = images[b[0]][0]
                if img:
                    p_ = self.get_pos(row,col)
                    screen.blit(img,p_)
                    if get_distance(p_[0]+BLOCK_SIZE/2,self.player.rect.centerx,p_[1]+BLOCK_SIZE/2,self.player.rect.centery) < player.chooserange:
                        hard = b[1]
                        fullhard = images[b[0]][2]
                        pygame.draw.line(screen,(0,0,0),
                            (p_[0]+BLOCK_SIZE/4,p_[1]+3),
                            (p_[0]+BLOCK_SIZE/4*3,p_[1]+3),
                        1)
                        pygame.draw.line(screen,(100,255,255),
                            (p_[0]+BLOCK_SIZE/4,p_[1]+3),
                            (p_[0]+BLOCK_SIZE/4+(hard*BLOCK_SIZE/2/fullhard),p_[1]+3),
                        1)
        if self.choose_bid and get_distance(self.choose_rect.centerx,self.player.rect.centerx,self.choose_rect.centery,self.player.rect.centery) < self.player.chooserange:
            if self.data[self.choose_bid[0]][self.choose_bid[1]][0]:
                pygame.draw.rect(screen,(0,0,0),self.choose_rect,3)
            else:
                pygame.draw.rect(screen,(155,155,155),self.choose_rect,1)
        self.player.draw()
        if self.choose_bid and self.__state == 'clickleft' and get_distance(self.choose_rect.centerx,self.player.rect.centerx,self.choose_rect.centery,self.player.rect.centery) < self.player.chooserange:
            row, col = self.choose_bid
            if (row < len(self.data)) and (col < len(self.data[row])) and self.data[row][col][0]:
                self.data[row][col][1] -= self.player.attack
                if self.data[row][col][1] <= 0:
                    self.data[row][col] = [0,images[0][2]]
        elif self.choose_bid and self.__state == 'clickright' and get_distance(self.choose_rect.centerx,self.player.rect.centerx,self.choose_rect.centery,self.player.rect.centery) < self.player.chooserange:
            row, col = self.choose_bid
            if (row < len(self.data)) and (col < len(self.data[row])) and (not self.data[row][col][0]):
                self.data[row][col] = [3,35]
    
    # 死 亡 回 放
    def reset(self):
        self.player.hp = 100
        self.offset_x = 0
        self.offset_y = 0

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

player = Player()
gamemap = GameMap(data,player)
sun = SunAct(SC_WIDTH,SC_HEIGHT,(6,18))
sightbg = sight.generate_surface(SC_WIDTH,SC_HEIGHT,150,50)
sightbg.set_alpha(0)

clock = pygame.time.Clock()
expect_fps = 100
real_fps = 100
evt_pos = (-1,-1)

gamestarttime = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            evt_pos = event.pos
            gamemap.choose(evt_pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            ebtn = event.button
            if ebtn == 1:
                gamemap.state('clickleft')
            elif ebtn == 3:
                gamemap.state('clickright')
        if event.type == pygame.MOUSEBUTTONUP:
            gamemap.state('unclick')
        if event.type == pygame.KEYDOWN:
            gamemap.keyin(event.key,1)
        if event.type == pygame.KEYUP:
            gamemap.keyin(event.key,0)
    
    screen.fill((255,255,255))
    gametime = (time.time() - gamestarttime) * 1000 / 3600 + 6
    gamedaytime = gametime % 24
    sun.get_sun_pos(gamedaytime)
    sun.day()
    gamemap.handle_event()
    gamemap.show()
    sun.night(gamedaytime)
    player.draw_info()
    if player.hp <= 0:
        gamemap.reset()
    pygame.display.update()
    clock.tick(expect_fps)
    real_fps = max(1,round(clock.get_fps()))
    
    pygame.display.set_caption(f'IDU Sandbox Driver (FPS: {real_fps})')