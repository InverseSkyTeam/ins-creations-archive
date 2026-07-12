from __future__ import annotations
from typing import Tuple, List, Any

import platform
import pygame
import random
import time
import sys

from basic import *
from recipe import *
import save

''' 游戏编写设定
量词使用:
  sc: screen量词 (相对于screen而言)
  mp: map量词 (相对于map而言)
  px: pixel量词 (像素单位)
  bl: block量词 (方块单位)
  * example: mp_bl意思是相对map的以block为单位的量词
'''


# 常量和定义
if '基本构造设定':
    BLOCK_SIZE = 50                                       # (px)
    SLOT_SIZE = 50                                        # (px)
    DROP_SIZE = 40                                        # (px)
    BLOCK_SIZE_1in5 = BLOCK_SIZE // 5                     # (px)
    SLOT_DROP_SPACE = (SLOT_SIZE - DROP_SIZE) // 2        # (px)

if '屏幕大小':
    SCW_px = 1000                                  # (px)
    SCH_px = 700                                   # (px)
    SCW_bl = SCW_px // BLOCK_SIZE                  # (bl)
    SCH_bl = SCH_px // BLOCK_SIZE                  # (bl)
    SCW_px_half = SCW_px // 2                      # (px)
    SCH_px_half = SCH_px // 2                      # (px)

if '地图大小':
    MPW_bl = len(save.data[0])                     # (bl)
    MPH_bl = len(save.data)                        # (bl)
    MPW_px = MPW_bl * BLOCK_SIZE                   # (px)
    MPH_px = MPH_bl * BLOCK_SIZE                   # (px)
    MPR_px = MPW_px - SCW_px - 1                   # (px)
    MPB_px = MPH_px - SCH_px - 1                   # (px)

if '自然条件':
    GRAVITY = 15
g = GRAVITY / 100

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
def load_actor(name):
    return pygame.image.load(f'./images/actor/{name}.png')
def load_block(name,s):
    return pygame.transform.smoothscale(pygame.image.load(f'./images/{name}'),(s,s))
def load_decorate(name):
    return pygame.image.load(f'./images/decorate/{name}.png')
la, lb, ld = load_actor, load_block, load_decorate

binfo = {
    0: [],
    100101: [lb('土.png', BLOCK_SIZE), 200101, 10, 0, 0, [0, 0, 0, 0]],
    100102: [lb('草地.png', BLOCK_SIZE), 200101, 5, 0, 0, [0, 0, 0, 0]],
    100201: [lb('石块.png', BLOCK_SIZE), 200201, 30, 1, 0, [0, 0, 0, 0]],
    100301: [lb('树干.png', BLOCK_SIZE), 200301, 20, 0, 1, [0, 0, 0, 0]],
    100401: [lb('木板.png', BLOCK_SIZE), 200401, 10, 0, 1, [0, 0, 0, 0]],
    100601: [lb('工作台.png', BLOCK_SIZE), 200601, 25, 0, 1, [0, 0, 0, 0]],
    200101: [lb('土.png', DROP_SIZE), 100101, 64],
    200201: [lb('石块.png', DROP_SIZE), 100201, 64],
    200301: [lb('树干.png', DROP_SIZE), 100301, 64],
    200401: [lb('木板.png', DROP_SIZE), 100401, 64],
    200501: [lb('木棍.png', DROP_SIZE), 0, 64],
    200601: [lb('工作台.png', DROP_SIZE), 100601, 64],
}

screen = pygame.display.set_mode((SCW_px, SCH_px))
pygame.display.set_caption('IDU 24H2 Sandbox Driver')



class Map:
    def __init__(self):
        self.x = 0.0                  # 地图左上角x坐标(px)
        self.y = 0.0                  # 地图左上角y坐标(px)
        self.data = [[]]
        self.drop_list: List[Drop] = []
        self.dig_pos = None
        self.dig_progress = 0
        self.hightlight_rect = pygame.Rect(0, 0, BLOCK_SIZE, BLOCK_SIZE)
    def load(self, data: list):
        self.data = data
    def save(self) -> list:
        return self.data
    
    def cannot_cross_block(self, row: int, col: int) -> bool:    # 判断方块是否不能被穿过
        return self.data[row][col] and binfo[self.data[row][col]][4] == 0
    
    def recv(self, event: dict):        # 接收游戏事件
        col, row = px_to_bl(sc_to_mp(self, event['mpos']))
        mx, my = bl_to_px((col, row))
        x, y = mp_to_sc(self, (mx, my))
        bid = self.data[row][col]

        # 绘制方块高亮框
        hightlightwidth = {True: 3, False: 2}[bool(bid)]
        self.hightlight_rect.topleft = (x, y)
        pygame.draw.rect(screen, (0, 0, 0), self.hightlight_rect, hightlightwidth, 3)

        # 左键按下：挖掘
        if event['mb 1'] and bid:
            if self.dig_pos == (col, row):
                self.dig_progress += 1
                if self.dig_progress < binfo[bid][2]:
                    x += BLOCK_SIZE_1in5
                    y += 5
                    draw_progress(screen, self.dig_progress, binfo[bid][2], x, y, BLOCK_SIZE_1in5 * 3, 2, (88, 255, 188))
                    return
                self.data[row][col] = 0
                self.drop_list.append(Drop(binfo[bid][1]))
                self.drop_list[-1].set_p(mx, my)
            else:
                self.dig_pos = (col, row)
        else:
            self.dig_pos = None
        self.dig_progress = 0
        
        if event['mb 3'] and (not bid):
            chosen_slot = player.bag.items[inventory_chosen_index]
            if chosen_slot.bid:
                self.data[row][col] = binfo[chosen_slot.bid][1]
                chosen_slot.count -= 1
                chosen_slot.update()
    
    def update_drop(self):
        for drop in self.drop_list:
            if drop.floating:
                drop.vy += g
            drop.move(self)
            drop.show(self)
    
    def set_sight(self, visitor: Entity, offset: Tuple[int, int]):
        ox, oy = offset
        self.x = min(max(0, visitor.x - ox), MPR_px)
        self.y = min(max(0, visitor.y - oy), MPB_px)
    def show(self):
        for row in range(SCH_bl + 1):
            for col in range(SCW_bl + 1):
                bid = self.data[self.y_bl + row][self.x_bl + col]
                if bid:
                    screen.blit(binfo[bid][0], (col * BLOCK_SIZE - self.x_offset, row * BLOCK_SIZE - self.y_offset))
    
    @property
    def x_bl(self) -> int:                         # 地图左上角x坐标(bl)
        return int(self.x / BLOCK_SIZE)
    @property
    def y_bl(self) -> int:                         # 地图左上角y坐标(bl)
        return int(self.y / BLOCK_SIZE)
    @property
    def x_offset(self) -> int | float:             # 地图左上角在屏幕上的x偏移量(px)
        return self.x % BLOCK_SIZE
    @property
    def y_offset(self) -> int | float:             # 地图左上角在屏幕上的y偏移量(px)
        return self.y % BLOCK_SIZE

slotimg = ld('slot')
slotimg_selected = ld('slot_red')

class Slot:
    def __init__(self, x: int | float, y: int | float, mode: str = 'normal'):
        self.bid = 0
        self.count = 0
        self.mode = mode
        self.selected = False
        self.set_p(x, y)
    def set_p(self, x: int | float, y: int | float):
        self.x = x
        self.y = y
    def exchange_with(self, other: Slot):
        b, c = self.bid, self.count
        self.bid, self.count = other.bid, other.count
        other.bid, other.count = b, c
    def give_to(self, other: Slot):
        self.count -= 1
        other.count += 1
        if not other.bid:
            other.bid = self.bid
    def connect1(self, signal: int):
        if self.mode == 'craft':
            return
        match signal:
            case [1, 0, 0]:
                self.selected = True
            case [0, 0, 1]:
                self.selected = False
    def connect2(self, other: Slot, signal: int) -> str | None:
        # 合成格子
        if self.mode == 'craft':
            res = 'failed'
            if signal == 1 and self.bid and other.count + self.count <= 64:
                if other.bid and self.bid == other.bid:
                    other.count += self.count
                    self.count = 0
                else:
                    self.exchange_with(other)
                res = 'complete'
            self.update()
            return res
        # 普通格子
        if not (self.bid or other.bid):           # 格子空，鼠标空
            return
        if self.bid and other.bid:                # 格子有，鼠标有
            if (self.bid == other.bid and self.count == 64) or (self.bid != other.bid):
                self.exchange_with(other)
                return
            match signal:
                case 1:
                    if other.count >= 64:
                        self.exchange_with(other)
                        return
                    self.count += other.count
                    other.count = 0
                    other.bid = 0
                    if self.count > 64:
                        other.count = self.count - 64
                        other.bid = self.bid
                        self.count = 64
                case 3:
                    other.give_to(self)
                case 4:
                    other.give_to(self)
                case 5 if other.count < 64:
                    self.give_to(other)
        elif self.bid:                            # 格子有，鼠标空
            match signal:
                case 1:
                    self.exchange_with(other)
                case 3:
                    other.bid = self.bid
                    other.count = self.count // 2
                    self.count -= other.count
                case 5:
                    self.give_to(other)
                case _:
                    ...
        else:                                     # 格子空，鼠标有
            match signal:
                case 1:
                    self.exchange_with(other)
                case 3:
                    other.give_to(self)
                case 4:
                    other.give_to(self)
                case _:
                    ...
        self.update()
        other.update()
    def update(self):
        if not self.bid:
            self.count = 0
            return
        if not self.count:
            self.bid = 0
            return
    def show(self):
        if self.mode != 'on mouse':
            screen.blit(slotimg_selected if self.selected else slotimg, (self.x, self.y))
        if self.bid:
            screen.blit(binfo[self.bid][0], (self.x + SLOT_DROP_SPACE, self.y + SLOT_DROP_SPACE))
            if self.count > 9:
                show_text(str(self.count), (255, 255, 255), (self.x + SLOT_DROP_SPACE + DROP_SIZE - 20, self.y + SLOT_DROP_SPACE + DROP_SIZE - 20), 20)
            elif self.count > 1:
                show_text(str(self.count), (255, 255, 255), (self.x + SLOT_DROP_SPACE + DROP_SIZE - 10, self.y + SLOT_DROP_SPACE + DROP_SIZE - 20), 20)

class Page:
    def __init__(self, x: int | float, y: int | float, w: int, h: int, mode: str = 'normal'):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.mode = mode
        self.showing = False
        self.items: List[Slot] = []
        self.rect = pygame.Rect(x, y, w, h)
    def tap(self):
        if self.showing:
            self.showing = False
            showing_pages.remove(self)
        else:
            self.showing = True
            showing_pages.append(self)
    def append(self, item: Slot):
        self.items.append(item)
    def insert_drop(self, bid: int):
        empty_slot = False
        for slot in self.items:
            if slot.bid == bid and slot.count < 64:
                slot.count += 1
                return True
            if not (slot.bid or empty_slot):
                empty_slot = slot
        if empty_slot:
            empty_slot.bid = bid
            empty_slot.count = 1
            return True
        return False
    def unselect_all(self):
        for item in self.items:
            item.selected = False
    def show(self):
        if self.showing:
            pygame.draw.rect(screen, (128, 128, 128), self.rect, 0, 10)
            pygame.draw.rect(screen, (0, 68, 68), self.rect, 3, 10)
            for item in self.items:
                item.show()
        elif self.mode == 'player-bag':
            for i in range(9):
                self.items[i].show()

class Entity:
    def __init__(self, w: int, h: int):
        self.x = 0.0
        self.y = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.w = w
        self.h = h
        self.floating = True
    def set_p(self, x: int | float | None = None, y: int | float | None = None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
    def set_v(self, vx: int | float | None = None, vy: int | float | None = None):
        if vx is not None:
            self.vx = vx
        if vy is not None:
            self.vy = vy
    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(0, 0, self.w, self.h)
    def collide(self, other: Entity) -> bool:
        return collision(self.x, self.y, self.w, self.h, other.x, other.y, other.w, other.h)
    
    def move(self, map: Map):
        self.floating = True

        # x方向碰撞箱处理
        if self.vx < 0:
            for row in range(self.t_bl, self.b_bl + 1):
                if self.l_bl <= 0 or map.cannot_cross_block(row, self.l_bl - 1):
                    self.vx = -min(-self.vx, self.l_space)
                    break
        elif self.vx > 0:
            for row in range(self.t_bl, self.b_bl + 1):
                if self.r_bl >= MPW_bl - 1 or map.cannot_cross_block(row, self.r_bl + 1):
                    self.vx = min(self.vx, self.r_space)
                    break
        self.set_p(x = self.x + self.vx)             # 不先移动x的后果是，遇到左上角向右下这类情况，直接卡墙！

        # y方向碰撞箱处理
        if self.vy < 0:
            for col in range(self.l_bl, self.r_bl + 1):
                if self.t_bl <= 0 or map.cannot_cross_block(self.t_bl - 1, col):
                    self.vy = -min(-self.vy, self.t_space)
                    break
        elif self.vy > 0:
            for col in range(self.l_bl, self.r_bl + 1):
                if self.b_bl >= MPH_bl - 1 or map.cannot_cross_block(self.b_bl + 1, col):
                    self.vy = min(self.vy, self.b_space)
                    if not self.vy:
                        self.floating = False
                    break
        self.set_p(y = self.y + self.vy)
    
    def draw(self, x: int | float, y: int | float):
        pass
    def show(self, map: Map):
        x, y = mp_to_sc(map, (self.x, self.y))
        if -self.w <= x <= SCW_px and -self.h <= y <= SCH_px:
            self.draw(x, y)
    
    @property
    def l(self) -> int | float:
        return self.x
    @property
    def r(self) -> int | float:
        return self.x + self.w - 1
    @property
    def t(self) -> int | float:
        return self.y
    @property
    def b(self) -> int | float:
        return self.y + self.h - 1
    @property
    def l_bl(self) -> int:
        return int(self.l / BLOCK_SIZE)
    @property
    def r_bl(self) -> int:
        return int(self.r / BLOCK_SIZE)
    @property
    def t_bl(self) -> int:
        return int(self.t / BLOCK_SIZE)
    @property
    def b_bl(self) -> int:
        return int(self.b / BLOCK_SIZE)
    @property
    def l_space(self) -> int | float:            # 实体左边到左边block的距离(px) 下面以此类推
        return self.l % BLOCK_SIZE
    @property
    def r_space(self) -> int | float:
        return BLOCK_SIZE - 1 - self.r % BLOCK_SIZE
    @property
    def t_space(self) -> int | float:
        return self.t % BLOCK_SIZE
    @property
    def b_space(self) -> int | float:
        return BLOCK_SIZE - 1 - self.b % BLOCK_SIZE

class Drop(Entity):
    def __init__(self, bid: int):
        super().__init__(DROP_SIZE, DROP_SIZE)
        self.bid = bid
    def draw(self, x: int | float, y: int | float):
        screen.blit(binfo[self.bid][0], (x, y))

class Animal(Entity):
    def __init__(self, hp: int | float, w: int, h: int):
        super().__init__(w, h)
        self.hp = hp
        self.jump_force = 5.0
        self.walkspeed = 3.0

class Player(Animal):
    def __init__(self):
        super().__init__(100, 40, 120)
        self.rect = self.get_rect()
        self.bag = Page(225, 430, 550, 260, 'player-bag')
        for i in range(9):
            self.bag.append(Slot(275 + i * SLOT_SIZE, 625))
        for row in range(3):
            for col in range(9):
                self.bag.append(Slot(275 + col * SLOT_SIZE, 450 + row * SLOT_SIZE))
    def control(self):
        if self.floating:
            self.vy += g
        elif event_state[pygame.K_w]:
            self.vy = -self.jump_force
            self.floating = True
        self.set_v((event_state[pygame.K_d] - event_state[pygame.K_a]) * self.walkspeed)
    def get_drop(self, drop_list: List[Drop]):
        for drop in drop_list:
            if self.collide(drop):
                if self.bag.insert_drop(drop.bid):
                    drop_list.remove(drop)
    def next(self, map: Map):
        self.show(map)
        self.bag.show()
        self.control()
        self.move(map)
        self.get_drop(map.drop_list)
    def draw(self, x: int | float, y: int | float):
        self.rect.topleft = (x, y)
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 3)

def get_recipe(slot_list: List[Slot], row: int, col: int) -> Tuple[int, int]:
    recipe = [[slot_list[i * col + j].bid for j in range(col)] for i in range(row)]
    top, left = row - 1, col - 1
    right = bottom = 0
    for i in range(row):
        for j in range(col):
            if recipe[i][j]:
                top = min(top, i)
                bottom = max(bottom, i)
                left = min(left, j)
                right = max(right, j)
    if top > bottom or left > right:
        return (0, 0)
    recipe_clip = tuple(tuple(recipe[i][j] for j in range(left, right + 1)) for i in range(top, bottom + 1))
    if recipe_clip in recipes:
        return recipes[recipe_clip]
    return (0, 0)

def sc_to_mp(map: Map, pos: Tuple[int | float, int | float]) -> Tuple[int | float, int | float]:
    x, y = pos
    return x + map.x, y + map.y
def mp_to_sc(map: Map, pos: Tuple[int | float, int | float]) -> Tuple[int | float, int | float]:
    x, y = pos
    return x - map.x, y - map.y
def px_to_bl(pos: Tuple[int | float, int | float]) -> Tuple[int | float, int | float]:
    x, y = pos
    return int(x / BLOCK_SIZE), int(y / BLOCK_SIZE)
def bl_to_px(pos: Tuple[int | float, int | float]) -> Tuple[int | float, int | float]:
    x, y = pos
    return x * BLOCK_SIZE, y * BLOCK_SIZE



event_state = {
    pygame.K_UP: 0,
    pygame.K_DOWN: 0,
    pygame.K_LEFT: 0,
    pygame.K_RIGHT: 0,
    pygame.K_w: 0,
    pygame.K_s: 0,
    pygame.K_a: 0,
    pygame.K_d: 0,
    pygame.K_SPACE: 0,
    'mb 1': 0,        # 鼠标左键 (mb = mouse button)
    'mb 2': 0,        # 鼠标中键
    'mb 3': 0,        # 鼠标右键
    'mb 4': 0,        # 鼠标滚轮向上
    'mb 5': 0,        # 鼠标滚轮向下
    'mpos': (0, 0),   # 鼠标位置 (scx, scy) (px)
}

clock = pygame.time.Clock()
mouse_slot = Slot(0, 0, 'on mouse')

map = Map()
map.load(save.data)
slot_select_mode = False
showing_pages: List[Page] = []
craft_page = Page(300, 200, 400, 200)
for row in range(2):
    for col in range(2):
        craft_page.append(Slot(400 + col * SLOT_SIZE, 250 + row * SLOT_SIZE))
craft_page.append(Slot(550, 275, 'craft'))
player = Player()
inventory_chosen_index = 0
inventory_chosen_rect = pygame.Rect(player.bag.items[0].x, player.bag.items[0].y, SLOT_SIZE, SLOT_SIZE)

player.set_p(y=325*BLOCK_SIZE)
player.bag.items[0].bid, player.bag.items[0].count = 200301, 20



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEMOTION:
            event_state['mpos'] = event.pos
            if slot_select_mode:
                for page in showing_pages:
                    for slot in page.items:
                        if collision(slot.x, slot.y, SLOT_SIZE, SLOT_SIZE, *event.pos, 1, 1):
                            slot.connect1(event.buttons)
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            event_state[f'mb {event.button}'] = 1
            if showing_pages:        # 打开背包的情况
                # 选择模式有滚轮就执行这里。但选择模式左右中键和普通模式情况一样，跳到普通模式板块。
                if slot_select_mode:
                    if event.button == 4:
                        for page in showing_pages:
                            for slot in page.items:
                                if not mouse_slot.bid:
                                    break
                                if slot.selected:
                                    if slot.bid == mouse_slot.bid and slot.count < 64:
                                        slot.count += 1
                                        mouse_slot.count -= 1
                                        mouse_slot.update()
                                    elif not slot.bid:
                                        slot.bid = mouse_slot.bid
                                        slot.count = 1
                                        mouse_slot.count -= 1
                                        mouse_slot.update()
                        continue
                    elif event.button == 5:
                        for page in showing_pages:
                            for slot in page.items:
                                if slot.selected and slot.bid:
                                    if (slot.bid == mouse_slot.bid and mouse_slot.count < 64) or (not mouse_slot.bid):
                                        slot.count -= 1
                                        mouse_slot.count += 1
                                        if not mouse_slot.bid:
                                            mouse_slot.bid = slot.bid
                                        slot.update()
                        continue
                # 普通模式
                res = crafted = False
                for page in showing_pages:
                    for slot in page.items:
                        if collision(slot.x, slot.y, SLOT_SIZE, SLOT_SIZE, *event.pos, 1, 1):
                            res = slot.connect2(mouse_slot, event.button)
                            if slot.mode == 'craft' and res == 'complete':
                                crafted = True
                            break
                    if res in [None, 'complete']:      # res=False说明没有点击格子，否则都是点击了，因为res返回None或者'complete'点击了
                        break
                if crafted:      # 如果合成了物品，那么清空合成需要的物品
                    for slot in craft_page.items:
                        if slot.bid:
                            slot.count -= 1
                            slot.update()
            else:       # 没有打开背包
                if event.button == 4:
                    inventory_chosen_index = max(0, inventory_chosen_index - 1)
                    inventory_chosen_rect.x = player.bag.items[inventory_chosen_index].x
                elif event.button == 5:
                    inventory_chosen_index = min(8, inventory_chosen_index + 1)
                    inventory_chosen_rect.x = player.bag.items[inventory_chosen_index].x
        
        elif event.type == pygame.MOUSEBUTTONUP:
            event_state[f'mb {event.button}'] = 0
            if showing_pages:
                craft_page.items[-1].bid, craft_page.items[-1].count = get_recipe(craft_page.items, 2, 2)
        
        elif event.type == pygame.KEYDOWN:
            event_state[event.key] = 1
            if event.key == ord('e'):
                player.bag.tap()
                craft_page.tap()
            if showing_pages:
                if event.key == ord('s'):
                    slot_select_mode = not slot_select_mode
                    for page in showing_pages:
                        page.unselect_all()
                if slot_select_mode:
                    if event.key == ord('a'):         # 平均分配物品
                        all_put: List[Slot] = []
                        for page in showing_pages:
                            for slot in page.items:
                                if slot.selected and ((not slot.bid) or (slot.bid and slot.bid == mouse_slot.bid and slot.count < 64)):
                                    all_put.append(slot)           # 加入的选中的slot满足：1.没有物品 2.有物品且和鼠标的相同且没满
                        count = len(all_put)
                        if mouse_slot.count < count:           # 鼠标数量不够平均分，直接跳过了
                            continue
                        adds = mouse_slot.count // count       # adds >= 1
                        overflow = mouse_slot.count % count    # 0 <= overflow数量 <= 原来数量
                        for slot in all_put:
                            slot.count += adds
                            if not slot.bid:
                                slot.bid = mouse_slot.bid
                            if slot.count > 64:
                                overflow += slot.count - 64
                                slot.count = 64
                        mouse_slot.count = overflow
                        mouse_slot.update()
            else:
                if 49 <= event.key <= 57:
                    inventory_chosen_index = event.key - 49
                    inventory_chosen_rect.x = player.bag.items[inventory_chosen_index].x
        
        elif event.type == pygame.KEYUP:
            event_state[event.key] = 0
            if showing_pages:
                craft_page.items[-1].bid, craft_page.items[-1].count = get_recipe(craft_page.items, 2, 2)

    screen.fill((255, 255, 255))

    map.set_sight(player, (SCW_px_half - player.w // 2, SCH_px_half - player.h // 2))
    map.show()
    if not showing_pages:
        map.recv(event_state)
    map.update_drop()
    player.next(map)
    pygame.draw.rect(screen, (33, 233, 255), inventory_chosen_rect, 3, 5)
    craft_page.show()

    mouse_slot.set_p(*event_state['mpos'])
    mouse_slot.show()

    pygame.display.update()
    clock.tick(100)