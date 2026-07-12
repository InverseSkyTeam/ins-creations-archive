import pygame
import random
import time
import sys
import platform

from basic import *
import sight
import save

# Const
SC_WIDTH = 1000
SC_HEIGHT = 700
BLOCK_SIZE = 50
BOX_SIZE = 50
DROP_SIZE = 40
HALF_SC_WIDTH = SC_WIDTH // 2
HALF_SC_HEIGHT = SC_HEIGHT // 2
WIDTH = SC_WIDTH // BLOCK_SIZE
HEIGHT = SC_HEIGHT // BLOCK_SIZE
MPW = len(save.data[0])
MPH = len(save.data)
MPWPX = MPW * BLOCK_SIZE
MPHPX = MPH * BLOCK_SIZE
MWLIMIT = MPWPX - SC_WIDTH - 1
MHLIMIT = MPHPX - SC_HEIGHT - 1
BLOCK_SIZE_1_in_5 = BLOCK_SIZE // 5
BLOCK_SIZE_4_in_5 = BLOCK_SIZE - BLOCK_SIZE_1_in_5
BLOCK_SIZE_3_in_5 = BLOCK_SIZE_4_in_5 - BLOCK_SIZE_1_in_5
INVENTORY_LEFT = (SC_WIDTH - 9 * BOX_SIZE) // 2
BOX_SPACE = (BOX_SIZE - DROP_SIZE) // 2

g = 0.15

# 基础Init
pygame.init()
pygame.key.stop_text_input()

if platform.system() == 'Windows':
    font = {
        10: pygame.font.SysFont('kaiti', 10),
        20: pygame.font.SysFont('kaiti', 20),
        25: pygame.font.SysFont('kaiti', 25),
        30: pygame.font.SysFont('kaiti', 30),
        40: pygame.font.SysFont('kaiti', 40),
    }
else:
    font = {
        10: pygame.font.SysFont('kaittf', 10),
        20: pygame.font.SysFont('kaittf', 20),
        25: pygame.font.SysFont('kaittf', 25),
        30: pygame.font.SysFont('kaittf', 30),
        40: pygame.font.SysFont('kaittf', 40),
    }
def show_text(text,color=(0,0,0),pos=(0,0),size=20):
    screen.blit(font[size].render((text),True,color),pos)
def loadactor(name):
    return pygame.image.load(f'./images/actor/{name}.png')
def loadblock(name,s):
    return pygame.transform.smoothscale(pygame.image.load(f'./images/{name}'),(s,s))
la, lb = loadactor, loadblock
inventory_choose_rect = pygame.Rect(INVENTORY_LEFT, SC_HEIGHT - 20 - BOX_SIZE, BOX_SIZE, BOX_SIZE)
inventory_choose_index = 0
box_image = pygame.image.load('./images/decorate/box.png')

# +---------------------------------+
# |            方块信息             |
# | 0    空气                       |
# | 1XXX 普通方块                   |
# |      [0]图片                    |
# |      [1]掉落物id                |
# |      [2]硬度                    |
# |      [3]碰撞箱削弱              |
# | 2XXX 物品（非工具）             |
# |      [0]图片                    |
# |      [1]原方块id                |
# |      [2]占用容量                |
# | 3XXX 物品（工具）               |
# |      [0]图片                    |
# |      [1]耐久                    |
# |      [2]加成                    |
# |      [*]占用容量都为256         |
# | 4XXX 其他/特殊                  |
# | 5位数: 代表多格方块             |
# +---------------------------------+
# *加成 = [范围, 挖掘, 铲土, 攻击, 跳跃, 防护, 速度]
# *碰撞箱削弱 = [上px, 下px, 左px, 右px]
binfo = {
    0: [],
    1001: [lb('草地.png',BLOCK_SIZE), 2001, 10, [0, 0, 0, 0]],
    1002: [lb('土.png',BLOCK_SIZE), 2001, 10, [0, 0, 0, 0]],
    1003: [lb('石块.png',BLOCK_SIZE), 2002, 10, [0, 0, 0, 0]],
    2001: [lb('土.png',DROP_SIZE), 1002, 1],
    2002: [lb('石块.png',DROP_SIZE), 1003, 1],
    3001: [lb('木镐.png',DROP_SIZE), 100, [0, 1, 0, 1, 0, 0]],
}


# 事物Init
screen = pygame.display.set_mode((SC_WIDTH,SC_HEIGHT))
pygame.display.set_caption('IDU Sandbox Driver 2')

class Command:
    def __init__(self):
        self.text = '<cmd>'
        self.cmd = {
            'p': self.c_p,
        }
    def execute(self, text, permission=1):
        t = text.split()
        if t[0][0] != '/':
            return (False, '[/] 命令前缺少匹配符</>')
        self.cmd[t[0][1:]](t[1:])
    def c_p(self, args):
        thing = eval(args[0])
        if get_class_text(thing)[0] != 'thing':
            return (False, '[/p] 传输的事物的基类必须是<thing>')
        thing.p(int(args[1]), int(args[2]))
        return True

class Map:
    def __init__(self):
        self.text = '<map>'
        self.data = [[]]
        self.visitor = None
        self.highlight_rect = pygame.Rect(0, 0, BLOCK_SIZE, BLOCK_SIZE)
        self.dig_progress = Slider(0, 0, 0)
        self.dig_pos = None
    def read(self):
        return self.data
    def write(self, d):
        self.data = d
    def draw(self):
        l = int(self.x / BLOCK_SIZE)
        t = int(self.y / BLOCK_SIZE)
        offsetx = int(self.x) % BLOCK_SIZE
        offsety = int(self.y) % BLOCK_SIZE
        for i in range(HEIGHT+1):
            for j in range(WIDTH+1):
                bid = self.data[t+i][l+j]
                if bid:
                    screen.blit(binfo[bid][0], (BLOCK_SIZE * j - offsetx, BLOCK_SIZE * i - offsety))
        mx, my = mouse_pos
        highlightx = (mx + offsetx) // BLOCK_SIZE * BLOCK_SIZE - offsetx
        highlighty = (my + offsety) // BLOCK_SIZE * BLOCK_SIZE - offsety
        self.highlight_rect.topleft = (highlightx, highlighty)
        pygame.draw.rect(screen, (0, 0, 0), self.highlight_rect, 2, 3)
    def dig(self, row, col):
        if row >= 0 and col >= 0 and self.data[row][col]:
            if self.dig_pos != (row, col):
                self.dig_pos = (row, col)
                self.dig_progress.clear()
                self.dig_progress.change_full(binfo[self.data[row][col]][2])
            else:
                self.dig_progress += 1
                x, y = self.highlight_rect.topleft
                lx = x + BLOCK_SIZE_1_in_5
                rx = x + BLOCK_SIZE_4_in_5
                y += 5
                pygame.draw.line(screen, (0, 0, 0), (lx, y), (rx, y), 2)
                pygame.draw.line(screen, (88,255,188), (lx, y), (lx + self.dig_progress.part * BLOCK_SIZE_3_in_5, y), 2)
                if self.dig_progress.isf:
                    drop_list.append(Drop(binfo[self.data[row][col]][1]))
                    drop_list[-1].p(col * 50, row * 50)
                    self.data[row][col] = 0
                    self.dig_pos = None
                    self.dig_progress.clear()
    def put(self, row, col):
        if row >= 0 and col >= 0 and (not self.data[row][col]):
            c = self.visitor.bag.items[-1][inventory_choose_index].card
            if c.bid // 1000 == 2:
                c.count -= 1
                self.data[row][col] = binfo[c.bid][1]
    @property
    def x(self):
        return min(MWLIMIT, max(0, self.visitor.cx - HALF_SC_WIDTH))
    @property
    def y(self):
        return min(MHLIMIT, max(0, self.visitor.cy - HALF_SC_HEIGHT))

class Page:
    def __init__(self, w, h, title='页面'):
        self.text = '<page>'
        self.showing = False
        self.rect = pygame.Rect(0, 0, w, h)
        self.items = []
        self.title = title
    def show(self):
        self.showing = True
    def hide(self):
        self.showing = False
    def float_on(self, y):
        self.rect.x = (SC_WIDTH - self.rect.width) // 2
        self.rect.bottom = y - 20
    def include(self, item):
        self.items.append(item)
    def draw(self):
        if self.showing:
            pygame.draw.rect(screen, (128, 128, 128), self.rect, 0, 5)
            pygame.draw.rect(screen, (0, 68, 68), self.rect, 2, 5)
            show_text(self.title, (255, 255, 255), (self.rect.left + 5, self.rect.top + 5), 25)
            for i in self.items:
                i.draw()

class Card:
    def __init__(self, bid, count):
        self.text = '<card>'
        self.bid = bid
        self.count = count
    def draw(self, pos):
        if self.part:
            screen.blit(binfo[self.bid][0], pos)
            if self.count > 9:
                show_text(str(self.count), (255, 255, 255), (pos[0] + DROP_SIZE - 20, pos[1] + DROP_SIZE - 20), 20)
            elif self.count > 1:
                show_text(str(self.count), (255, 255, 255), (pos[0] + DROP_SIZE - 10, pos[1] + DROP_SIZE - 20), 20)
    @property
    def full(self):
        return self.bid and self.count == 64
    @property
    def have(self):
        return self.bid and self.count
    @property
    def part(self):
        return self.bid and 0 < self.count < 64
    @property
    def empty(self):
        return not self.have

class Box:
    def __init__(self, pos):
        self.text = '<box>'
        self.card = Card(0, 0)
        self.pos = pos
    def catch(self, card):
        self.card = card
    def draw(self):
        screen.blit(box_image, self.pos)
        self.card.draw((self.pos[0] + BOX_SPACE, self.pos[1] + BOX_SPACE))

class Bag:
    def __init__(self, row=1, col=3):
        self.text = '<bag>'
        self.row = row
        self.col = col
        self.items = [[Box((INVENTORY_LEFT + j * BOX_SIZE, SC_HEIGHT - 20 - (row - i) * BOX_SIZE)) for j in range(self.col)] for i in range(self.row)]
        self.rect = pygame.Rect(self.items[0][0].pos[0] - 10, self.items[0][0].pos[1] - 10, col * BOX_SIZE + 20, row * BOX_SIZE + 20)
        self.hide()
    def __list__(self):
        return self.items
    def show(self):
        self.showing = True
    def hide(self):
        self.showing = False
    def change(self):
        self.showing = not self.showing
    def draw(self):
        if self.showing:
            pygame.draw.rect(screen, (128, 128, 128), self.rect, 0, 5)
            pygame.draw.rect(screen, (0, 68, 68), self.rect, 3, 5)
            for i in self.items:
                for j in i:
                    j.draw()
    def find_put(self, bid, l):
        empty_box = (2, -1)
        for box in range(len(l)):
            if l[box].card.part and l[box].card.bid == bid:
                return (1, box)
            if l[box].card.empty and empty_box[1] == -1:
                empty_box = (2, box)
        return empty_box

class PlayerBag(Bag):
    def __init__(self):
        super().__init__(4, 9)
    def draw(self):
        if self.showing:
            pygame.draw.rect(screen, (128, 128, 128), self.rect, 0, 5)
            pygame.draw.rect(screen, (0, 68, 68), self.rect, 2, 5)
            for i in self.items:
                for j in i:
                    j.draw()
        else:
            for j in self.items[-1]:
                j.draw()
        pygame.draw.rect(screen, (255, 0, 0), inventory_choose_rect, 3, 5)
    def include(self, card):
        # inventory 遍历
        inventory_record = self.find_put(card.bid, self.items[-1])
        if inventory_record[0] == 1:
            self.items[-1][inventory_record[1]].card.count += 1
            return True
        first_empty = inventory_record[1]
        first_empty_row = -1

        # bag 遍历
        for l in range(self.row - 1):
            bag_record = self.find_put(card.bid, self.items[l])
            if bag_record[0] == 1:
                self.items[l][bag_record[1]].card.count += 1
                return True
            if first_empty == -1:
                first_empty = bag_record[1]
                first_empty_row = l
        if first_empty == -1:
            return False
        
        # 最终判断（首个空位会留在这里）
        self.items[first_empty_row][first_empty].catch(card)
        return True

class Thing:
    def __init__(self, w=1, h=1):
        self.text = '<thing>'
        self.x = 0.0
        self.y = 0.0
        self.xspeed = 0.0
        self.yspeed = 0.0
        self.w = w
        self.h = h
        self.floating = True
    def __str__(self):
        return f'<{self.text[1:-1]} | x: {round(self.x,1)}, y: {round(self.y,1)}, sx: {round(self.xspeed,1)}, sy: {round(self.yspeed,1)}, >'
    def p(self, x=None, y=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
    def v(self, x=None, y=None):
        if x is not None:
            self.xspeed = x
        if y is not None:
            self.yspeed = max(-30, min(30, y))
    def movep(self, addx=0.0, addy=0.0):
        self.x += addx
        self.y += addy
    def speedup(self, addsx=0.0, addsy=0.0):
        self.v(self.xspeed + addsx, self.yspeed + addsy)
    def move(self, data):
        vx, vy = self.xspeed, self.yspeed
        self.floating = True
        
        # l & r
        top = int(self.top / 50)
        bottom = int(self.bottom / 50)
        left = int(self.left / 50)
        right = int(self.right / 50)
        if vx < 0:
            for row in range(top, bottom + 1):
                if left <= 0 or data[row][left-1]:
                    vx = -min(-vx, self.space_left)
                    break
        elif vx > 0:
            for row in range(top, bottom + 1):
                if right >= MPW - 1 or data[row][right+1]:
                    vx = min(vx, self.space_right)
                    break
        self.v(x = vx)             # 不先移动x的后果是，遇到左上角向右下这类情况，直接卡墙！
        self.movep(addx = self.xspeed)
        
        # t & b
        top = int(self.top / 50)
        bottom = int(self.bottom / 50)
        left = int(self.left / 50)
        right = int(self.right / 50)
        if vy < 0:
            for col in range(left, right + 1):
                if top <= 0 or data[top-1][col]:
                    vy = -min(-vy, self.space_top)
                    break
        elif vy > 0:
            for col in range(left, right + 1):
                if bottom >= MPH - 1 or data[bottom+1][col]:
                    vy = min(vy, self.space_bottom)
                    if not vy:
                        self.floating = False
                    break
        self.v(y = vy)
        self.movep(addy = self.yspeed)
    def hit(self, other):
        return collision(self.x, self.y, self.w, self.h, other.x, other.y, other.w, other.h)
    def next(self, data):
        if self.floating:
            self.speedup(addsy=g)
        self.move(data)
    def visit(self, map):
        map.visitor = self
    @property
    def left(self):
        return self.x
    @property
    def right(self):
        return self.x + self.w - 1
    @property
    def top(self):
        return self.y
    @property
    def bottom(self):
        return self.y + self.h - 1
    @property
    def cx(self):
        return self.x + self.w / 2
    @property
    def cy(self):
        return self.y + self.h / 2
    @property
    def space_left(self):
        return self.left % 50
    @property
    def space_right(self):
        return 49 - self.right % 50
    @property
    def space_top(self):
        return self.top % 50
    @property
    def space_bottom(self):
        return 49 - self.bottom % 50

class Drop(Thing):
    def __init__(self, bid):
        super().__init__(DROP_SIZE, DROP_SIZE)
        self.text = '<thing-drop>'
        self.bid = bid
    def draw(self, gamemap):
        scx = self.x - gamemap.x
        scy = self.y - gamemap.y
        if -DROP_SIZE <= scx <= SC_WIDTH and -DROP_SIZE <= scy <= SC_HEIGHT:
            screen.blit(binfo[self.bid][0], (scx, scy))

class Living(Thing):           # 基础的、普通的生物
    def __init__(self, hp, w=1, h=1):
        super().__init__(w, h)
        self.text = '<thing-living>'
        self.hp = hp
        self.jumpforce = 5.0
        self.walkspeed = 3.0

class AutoLiving(Living):      # 比较高级的智能一些的生物(NPC)
    def __init__(self, hp, w=1, h=1):
        super().__init__(hp, w, h)
        self.bag = Bag()
    def get_drop(self):
        for drop in drop_list:
            if self.hit(drop):
                if self.bag.include(Card(drop.bid, 1)):
                    drop_list.remove(drop)

class Player(AutoLiving):
    def __init__(self, w=40, h=120):
        super().__init__(100, w, h)
        self.rect = pygame.Rect(0, 0, self.w, self.h)
        self.bag = PlayerBag()
        self.page = Page(400, 300, '我的')
        self.page.float_on(self.bag.rect.top)
        self.page.include(Box((self.page.rect.left + 10, self.page.rect.top + 100)))
        self.page.include(Box((self.page.rect.left + 10 + BOX_SIZE, self.page.rect.top + 100)))
        self.page.include(Box((self.page.rect.left + 10, self.page.rect.top + 100 + BOX_SIZE)))
        self.page.include(Box((self.page.rect.left + 10 + BOX_SIZE, self.page.rect.top + 100 + BOX_SIZE)))
        self.page.include(Box((self.page.rect.left + 80 + BOX_SIZE * 2, self.page.rect.top + 100 + BOX_SIZE // 2)))
    def control(self):
        if self.floating:
            self.speedup(addsy=g)
        elif keystate[pygame.K_w]:
            self.v(y=-self.jumpforce)
            self.floating = True
        self.v((keystate[pygame.K_d] - keystate[pygame.K_a]) * self.walkspeed)
    def next(self, data):
        self.control()
        self.move(data)
        self.get_drop()
    def draw(self, gamemap):
        scx = self.x - gamemap.x
        scy = self.y - gamemap.y
        self.rect.topleft = [scx, scy]
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 3)
        self.bag.draw()

def get_class_text(obj):
    t = obj.text
    if (t[0] != '<') or (t[-1] != '>'):
        raise Exception('不匹配的class_text')
    return t[1:-1].split('-')

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
mouse_state = {
    1: 0,
    2: 0,
    3: 0,
}

drop_list = []


# 准备对象
cmd = Command()
gamemap = Map()
gamemap.write(save.data)
player = Player()
player.visit(gamemap)
clock = pygame.time.Clock()
mouse_pos = (-1, -1)
mouse_row = -1
mouse_col = -1
mouse_card = Card(0, 0)
on_page = None

player.p(y=325*BLOCK_SIZE)

# 主程序
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_state[event.button] = 1
            if player.bag.showing:
                ...
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_state[event.button] = 0
        if event.type == pygame.KEYDOWN:
            ek = event.key
            keystate[ek] = 1
            if 49 <= ek <= 57:
                inventory_choose_index = ek - 49
                inventory_choose_rect.x = INVENTORY_LEFT + inventory_choose_index * BOX_SIZE
            if ek == ord('e'):
                player.bag.change()
                if on_page:
                    on_page.hide()
                    on_page = None
                else:
                    on_page = player.page
                    on_page.show()
        if event.type == pygame.KEYUP:
            keystate[event.key] = 0
    
    x = mouse_pos[0] + gamemap.x
    y = mouse_pos[1] + gamemap.y
    mouse_col = int(x / BLOCK_SIZE)
    mouse_row = int(y / BLOCK_SIZE)
    
    screen.fill((255, 255, 255))

    gamemap.draw()
    for drop in drop_list:
        drop.next(gamemap.data)
        drop.draw(gamemap)
    if not player.bag.showing:
        if mouse_state[1]:
            gamemap.dig(mouse_row, mouse_col)
        if mouse_state[3]:
            gamemap.put(mouse_row, mouse_col)
    player.next(gamemap.data)
    player.draw(gamemap)
    if on_page:
        on_page.draw()
    mouse_card.draw(mouse_pos)
    
    pygame.display.update()
    clock.tick(100)