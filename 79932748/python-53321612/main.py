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
BOX_SIZE = 50
DROP_SIZE = 40
BLOCK_DROP_DELTA = (BLOCK_SIZE - DROP_SIZE) / 2
BOX_CARD_DELTA = (BOX_SIZE - DROP_SIZE) / 2
MP_BLW = 100
MP_BLH = 200
MP_WIDTH = MP_BLW * BLOCK_SIZE
MP_HEIGHT = MP_BLH * BLOCK_SIZE
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


def loadblock(name,s):
    return pygame.transform.scale(pygame.image.load(f'./images/{name}'),(s,s))
lb = loadblock
binfo = {    # 原图片,作为掉落物的图片,掉落物的bid,硬度
    0: [None,None,0],
    1: [lb('草地.png',BLOCK_SIZE),lb('土.png',DROP_SIZE),2,5],
    2: [lb('土.png',BLOCK_SIZE),lb('土.png',DROP_SIZE),2,10],
    3: [lb('石块.png',BLOCK_SIZE),lb('石块.png',DROP_SIZE),3,35],
    4: [lb('树干.png',BLOCK_SIZE),lb('树干.png',DROP_SIZE),4,20],
}
data = [
    *([0 for i in range(100)] for line in range(10)),
    *([1 for i in range(100)] for line in range(1)),
    *([2 for i in range(100)] for line in range(90)),
    *([3 for i in range(100)] for line in range(99)),
]

g = 0.15
boxclick = []
droplist = []

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

class Drop:
    def __init__(self,bid,pos):
        self.bid = bid
        self.pos = pos   # 在地图中的绝对坐标
        self.speed = 0
        droplist.append(self)
    def drop(self,map):
        y = self.pos[1] + 40 - 1
        xl = self.pos[0]
        xr = xl + DROP_SIZE
        lx, ly = map.convert(1,xl,y)
        rx, ry = map.convert(1,xr,y)
        delta = 49
        # ly必定和ry相等，不用再判断ry.
        if ly >= MP_BLH - 1 or map.data[ly+1][lx] or map.data[ry+1][rx]:
            delta = 49 - y % 50
        self.pos[1] += min(self.speed, delta)
        if delta < 1:
            self.speed = 0
        else:
            self.speed += g
    def draw(self,mx,my):
        ax, ay = self.pos
        sx, sy = round(ax - mx), round(ay - my)
        if (-DROP_SIZE <= sx < SC_WIDTH) and (-DROP_SIZE <= sy < SC_HEIGHT):
            screen.blit(binfo[self.bid][1],(sx,sy))

class Card:
    def __init__(self,bid,value=1):
        self.bid = bid
        self.value = value
    def __iadd__(self,other):
        self.value += other.value
        return self
    def __isub__(self,other):
        self.value -= other.value
        return self
    def __add__(self,other):
        return self.value + other.value
    def __sub__(self,other):
        return self.value - other.value
    def overflow(self):
        if self.value < 256:
            return 0
        over = self.value - 255
        self.value = 255
        return over
    def draw(self,pos):
        screen.blit(binfo[self.bid][1],pos)
        if 2 <= self.value < 10:
            show_text(str(self.value),(255,255,255),(pos[0]+DROP_SIZE-10,pos[1]+DROP_SIZE-20))
        elif 10 <= self.value < 100:
            show_text(str(self.value),(255,255,255),(pos[0]+DROP_SIZE-20,pos[1]+DROP_SIZE-20))
        elif 100 <= self.value < 256:
            show_text(str(self.value),(255,255,255),(pos[0]+DROP_SIZE-30,pos[1]+DROP_SIZE-20))

class Box:
    def __init__(self,x,y,tp='save'):
        self.x, self.y = x, y
        self.tp = tp
        self.rect = pygame.Rect(self.x, self.y, BOX_SIZE, BOX_SIZE)
        self.inside = None
        boxclick.append(self)
    def catch(self,card):
        self.inside = card
    def push(self):
        card = self.inside
        self.inside = None
        return card
    def draw(self,color=(88,88,88)):
        pygame.draw.rect(screen,(188,188,188),self.rect,0,5)
        pygame.draw.rect(screen,color,self.rect,3,5)
        if self.inside:
            self.inside.draw((self.rect.x+BOX_CARD_DELTA, self.rect.y+BOX_CARD_DELTA))

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
        if xoffset:
            self.satiety -= 0.0003
        if self.hitground:
            if keystate[pygame.K_UP]:
                self.hitground = False
                self.yspeed = -self.jumpforce
                self.satiety -= 0.02
        else:
            self.yspeed = min(15, self.yspeed + g)
        yoffset = self.yspeed
        
        # 四种情况详细研究碰撞
        bleft, btop = self.map.convert(1,self.x,self.y)
        bright, bbottom = self.map.convert(1,self.x+self.rect.w-1,self.y+self.rect.h-1)
        if xoffset < 0:    # 左右碰到方块限制
            for row in range(btop,bbottom+1):
                if bleft <= 0 or self.map.data[row][bleft-1]:
                    delta = self.x - bleft * 50
                    xoffset = -min(-xoffset, delta)
                    break
        elif xoffset > 0:
            for row in range(btop,bbottom+1):
                if bright >= MP_BLW - 1 or self.map.data[row][bright+1]:
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
                if btop <= 0 or self.map.data[btop-1][col]:
                    delta = self.y - btop * 50
                    yoffset = -min(-yoffset, delta)
                    break
        elif yoffset > 0:
            for col in range(bleft,bright+1):
                if bbottom >= MP_BLH - 1 or self.map.data[bbottom+1][col]:
                    delta = bbottom * 50 + 50 - self.y - self.rect.h
                    if yoffset >= delta:
                        yoffset = delta
                        self.hitground = True
                        self.yspeed = 0
                    break
        self.y += yoffset      # y移动
        self.y = min(max(self.y, 0), MP_HEIGHT - 121)
        
        # 在地图边缘自移动
        if self.x <= SC_WIDTH / 2 - 20:
            self.rect.x = int(self.x)
        elif self.x >= MP_WIDTH - SC_WIDTH / 2 - 20:
            self.rect.x = int(SC_WIDTH-MP_WIDTH+self.x+1)
        if self.y <= SC_HEIGHT / 2 - 60:
            self.rect.y = int(self.y)
        elif self.y >= MP_HEIGHT - SC_HEIGHT / 2 - 60:
            self.rect.y = int(SC_HEIGHT-MP_HEIGHT+self.y+1)
    
    def keep(self):
        self.satiety -= 0.001
        self.hp += 0.001
    def hit_drop(self):
        dropindex = 0
        while dropindex < len(droplist):
            drop = droplist[dropindex]
            if hit_rect(self.x,self.y,
                        self.rect.w,self.rect.h,
                        drop.pos[0],drop.pos[1],
                        DROP_SIZE,DROP_SIZE):
                if receive_drop(drop.bid,inventory):
                    droplist.remove(drop)
                elif receive_drop(drop.bid,bag):
                    droplist.remove(drop)
            else:
                dropindex += 1
    
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
        self.data = data
        self.highlightrect = pygame.Rect(0,0,50,50)
        self.offsetx = self.offsety = 0
    
    def include(self,player):
        self.player = player
        pl_pos = self.player.position
        self.offsetx = pl_pos[0] - pl_pos[2]
        self.offsety = pl_pos[1] - pl_pos[3]
    def convert(self,tp,x,y,scx=None,scy=None):
        if tp == 1:     # 绝对坐标转绝对方块
            return [int(x // 50), int(y // 50)]
        if tp == 2:     # 绝对方块转绝对坐标
            return [x * 50, y * 50]
        if tp == 3:     # 绝对方块转相对坐标
            return [x * 50 - scx, y * 50 - scy]
    
    def draw_drops(self):
        for drop in droplist:
            drop.drop(self)
            drop.draw(self.offsetx, self.offsety)
    def draw(self):
        # 绘制
        px, py, psx, psy = self.player.position
        self.offsetx, self.offsety = px - psx, py - psy
        bleft, btop = self.convert(1, self.offsetx, self.offsety)
        bright, bbottom = bleft + WIDTH, btop + HEIGHT
        while btop <= bbottom:
            while bleft <= bright:
                image = binfo[self.data[btop][bleft]][0]
                if image:
                    screen.blit(image,self.convert(3, bleft, btop, self.offsetx, self.offsety))
                bleft += 1
            bleft = bleft - 1 - WIDTH
            btop += 1
        
        # 高亮
        if not bag_open:
            ex, ey = mousestate['pos']
            px, py = self.player.center
            distance = get_distance(ex,ey,px,py)
            if 0 <= ex < SC_WIDTH and 0 <= ey <= SC_HEIGHT and distance <= self.player.chooserange:
                highlight_col, highlight_row = self.convert(1, self.offsetx+ex, self.offsety+ey)
                highbid = self.data[highlight_row][highlight_col]
                if highbid:
                    border = 3
                    if mousestate[1]:
                        self.player.satiety -= 0.02
                        self.data[highlight_row][highlight_col] = 0
                        highleft, hightop = self.convert(2, highlight_col, highlight_row)
                        Drop(binfo[highbid][2], [highleft+BLOCK_DROP_DELTA, hightop+BLOCK_DROP_DELTA])
                else:
                    border = 1
                    if mousestate[3]:
                        self.player.satiety -= 0.005
                        invent = inventory[invent_choose-1].inside
                        if invent:
                            self.data[highlight_row][highlight_col] = invent.bid
                            invent.value -= 1
                            if invent.value < 1:
                                inventory[invent_choose-1].push()
                self.highlightrect.topleft = self.convert(3, highlight_col, highlight_row, self.offsetx, self.offsety)
                pygame.draw.rect(screen,(0,0,0),self.highlightrect,border,3)
        
        # 绘制掉落物
        self.draw_drops()

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

def receive_drop(bid,boxes):
    search_index = None
    for boxindex in range(len(boxes)):
        box = boxes[boxindex]
        if box.inside and box.inside.bid == bid and box.inside.value < 255:
            boxes[boxindex].inside.value += 1
            return True
        if (not search_index) and (not box.inside):
            search_index = boxindex
    if search_index:
        boxes[search_index].catch(Card(bid,1))
        return True
    return False

def get_craft(craft):
    craft_net = list(map(lambda box: box.inside.bid if box.inside else 0, craft))
    for i in recipe:
        if i[0] == craft_net:
            return i[1]
def clear_craft(craft):
    for box in craft:
        box.catch(None)



player = Player()
gamemap = GameMap(data)
player.bind(gamemap)
gamemap.include(player)
sun = SunAct(SC_WIDTH,SC_HEIGHT,(6,18))
sightbg = sight.generate_surface(SC_WIDTH,SC_HEIGHT,150,50)
sightbg.set_alpha(0)

inventory = [Box((SC_WIDTH-9*BOX_SIZE)/2+BOX_SIZE*(i-1), SC_HEIGHT-BOX_SIZE-20) for i in range(1,10)]
invent_choose = 1
bag = [Box((SC_WIDTH-12*BOX_SIZE)/2+col*50,SC_HEIGHT-BOX_SIZE-100-BOX_SIZE*row) for row in range(3) for col in range(12)]
bag_open = False
bag_rect = pygame.Rect(SC_WIDTH/2-400,SC_HEIGHT/2-260,800,600)
craft = [Box(bag_rect.x+100+col*50,bag_rect.y+100+BOX_SIZE*row,'craft') for row in range(2) for col in range(2)]
to_craft = Box(bag_rect.x+300,bag_rect.y+125,'to_craft')

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

inventory[0].catch(Card(2,16))
inventory[1].catch(Card(3,16))
inventory[2].catch(Card(4,16))
bag[0].catch(Card(2,128))
bag[1].catch(Card(3,128))

mousecard = None



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mousestate['pos'] = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousestate[event.button] = 1
            if bag_open:
                for box in boxclick:
                    if box.rect.collidepoint(mousestate['pos']):
                        boxcard = box.push()
                        if event.button == 1:
                            if mousecard and boxcard and mousecard.bid == boxcard.bid and box.tp != 'to_craft':
                                box.catch(boxcard)
                                box.inside += mousecard
                                mousecard.value = box.inside.overflow()
                            else:
                                if box.tp == 'to_craft':
                                    if boxcard and (not mousecard):
                                        clear_craft(craft)
                                    else:
                                        box.catch(boxcard)
                                        break
                                box.catch(mousecard)
                                mousecard = boxcard
                            if mousecard and mousecard.value < 1: mousecard = None
                            break
                        if event.button == 3:
                            if box.tp == 'to_craft':
                                box.catch(boxcard)
                                break
                            if mousecard and boxcard and mousecard.bid == boxcard.bid:
                                box.catch(boxcard)
                                if box.inside.value < 255:
                                    box.inside.value += 1
                                    mousecard.value -= 1
                            elif mousecard and (not boxcard):
                                box.catch(Card(mousecard.bid,1))
                                mousecard.value -= 1
                            elif (not mousecard) and boxcard:
                                mousecard = Card(boxcard.bid,boxcard.value // 2)
                                box.catch(boxcard)
                                box.inside -= mousecard
                            else:
                                box.catch(boxcard)
                            if mousecard and mousecard.value < 1: mousecard = None
                            break
                gc = get_craft(craft)
                if gc:
                    to_craft.catch(Card(*gc))
                else:
                    to_craft.catch(None)
        if event.type == pygame.MOUSEBUTTONUP:
            mousestate[event.button] = 0
        if event.type == pygame.KEYDOWN:
            ek = event.key
            keystate[ek] = 1
            if 49 <= ek <= 57:
                invent_choose = int(chr(ek))
            if ek == ord('e'):
                bag_open = not bag_open
        if event.type == pygame.KEYUP:
            keystate[event.key] = 0
    
    gametime = (time.time() - gamestarttime) * 1000 / 3600 + 6
    gamedaytime = gametime % 24
    sun.background(gamedaytime)
    
    # 白天（太阳图层在最底下）
    sun.get_sun_pos(gamedaytime)
    sun.day()
    
    gamemap.draw()
    player.keep()
    player.move()
    player.hit_drop()
    player.draw()
    
    # 黑夜（视野图层在最顶上）
    sun.night(gamedaytime)
    
    if bag_open:
        pygame.draw.rect(screen,(128,128,128),bag_rect,0,15)
        pygame.draw.rect(screen,(0,0,0),bag_rect,3,15)
        for box in bag:
            box.draw()
        for box in craft:
            box.draw()
        to_craft.draw()
    for box in inventory:
        box.draw()
    inventory[invent_choose-1].draw((255,0,0))
    player.draw_info()
    
    if mousecard:
        mousecard.draw(mousestate['pos'])
    
    pygame.display.update()
    clock.tick(100)