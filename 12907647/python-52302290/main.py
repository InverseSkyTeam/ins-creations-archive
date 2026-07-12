import pygame
import time
import sys
import sight

pygame.init()
pygame.key.stop_text_input()

# 定义常量(用户可以修改设置)
SC_WIDTH = 1000
SC_HEIGHT = 700
BLOCK_SIZE = 50
MP_WIDTH = 100 * BLOCK_SIZE
MP_HEIGHT = 111 * BLOCK_SIZE
WIDTH = int(SC_WIDTH / BLOCK_SIZE)
HEIGHT = int(SC_HEIGHT / BLOCK_SIZE)

print(f'''[INFO]
窗口大小: {SC_WIDTH}x{SC_HEIGHT}={SC_WIDTH*SC_HEIGHT}px
地图大小: {MP_WIDTH}x{MP_HEIGHT}={MP_WIDTH*MP_HEIGHT}px
地图方块: 100x111=11100个
单个方块: 50x50=2500px
wsad/up down left right移动
(fps/xpos/ypos在窗口标题显示)
Version dev-2 碰撞检测
Version dev-2.1 丝滑跳跃
Version dev-2.2 太阳运动
Version dev-2.3 右键添加方块
Version dev-2.4 圆角太阳
Version dev-2.5 视野
Version dev-2.6 黑夜
Version dev-2.7 日月交替
''')

screen = pygame.display.set_mode((SC_WIDTH,SC_HEIGHT))
pygame.display.set_caption('IDU Sandbox Driver')

images = {
    0: None,
    1: pygame.transform.scale(pygame.image.load('./images/草地.png'),(BLOCK_SIZE,BLOCK_SIZE)),
    2: pygame.transform.scale(pygame.image.load('./images/土.png'),(BLOCK_SIZE,BLOCK_SIZE)),
    3: pygame.transform.scale(pygame.image.load('./images/石块.png'),(BLOCK_SIZE,BLOCK_SIZE)),
}
data = [*([0 for i in range(100)] for line in range(10)),
        [1 for i in range(100)],
        *([2 for i in range(100)] for line in range(35)),
        *([3 for i in range(100)] for line in range(65)),]

class Life:
    pass

# 玩家内核
class Player:
    def __init__(self):
        self.hp = 100
        self.rect = pygame.Rect(0,0,40,120)
        self.rect.center = (SC_WIDTH/2,SC_HEIGHT/2)
        self.jumplity = 1      # 跳跃系数，越大越能跳
        self.chooserange = 200     # 选择范围（未制作）
    def draw(self):
        pygame.draw.rect(screen,(255,0,0),self.rect,3)

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
        self.choose_pos = None
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
        self.choose_bid = self.get_id(epos)
        self.choose_rect.topleft = self.get_pos(*self.choose_bid)
    
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
            self.Fy -= 0.01
        y_movement = self.Fy * self.player.jumplity
        
        self.player_on_ground = False
        if x_movement < 0:
            col = p_lt_site[1] - 1
            for row in range(p_lt_site[0],p_lb_site[0]+1):
                if data[row][col]:
                    maxleft = self.player.rect.left - (self.get_pos(row,col)[0] + BLOCK_SIZE)
                    x_movement = -min(maxleft,-x_movement)
                    break
        elif x_movement > 0:
            col = p_rt_site[1] + 1
            for row in range(p_rt_site[0],p_rb_site[0]+1):
                if data[row][col]:
                    maxright = self.get_pos(row,col)[0] - self.player.rect.right - 1
                    x_movement = min(maxright,x_movement)
                    break
        if y_movement < 0:
            row = p_lb_site[0] + 1
            for col in range(p_lb_site[1],p_rb_site[1]+1):
                if data[row][col]:
                    maxdown = self.get_pos(row,col)[1] - self.player.rect.bottom - 1
                    y_movement = -min(maxdown,-y_movement)
                    if y_movement == 0:
                        self.player_on_ground = True
                    break
        elif y_movement > 0:
            row = p_lt_site[0] - 1
            for col in range(p_lt_site[1],p_rt_site[1]+1):
                if data[row][col]:
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
                img = images[self.data[row][col]]
                if img:
                    screen.blit(img,self.get_pos(row,col))
        self.player.draw()
        if self.data[self.choose_bid[0]][self.choose_bid[1]]:
            pygame.draw.rect(screen,(0,0,0),self.choose_rect,3)
        else:
            pygame.draw.rect(screen,(155,155,155),self.choose_rect,1)
        if self.__state == 'clickleft':
            row, col = self.choose_bid
            if (row < len(self.data)) and (col < len(self.data[row])) and self.data[row][col]:
                self.data[row][col] = 0
        elif self.__state == 'clickright':
            row, col = self.choose_bid
            if (row < len(self.data)) and (col < len(self.data[row])) and (not self.data[row][col]):
                self.data[row][col] = 3

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
    pygame.display.update()
    clock.tick()
    
    pygame.display.set_caption(f'IDU Sandbox Driver (FPS: {int(clock.get_fps())})')