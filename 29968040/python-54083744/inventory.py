import pygame
from configure import *
from options import MESH_SIZE, MESH_BORDER_SIZE


class Mesh:  # 格子的类
    def __init__(self, rect, w, h, size=None):
        self.rect = rect
        self.size = size or MESH_BORDER_SIZE  # 格子的大小（带边框）
        self.w, self.h = w, h  # 长宽各几个格子
        self.real_w, real_h = w * self.size, h * self.size  # 长宽有多少像素
        self.offset = (self.size - MESH_SIZE) // 2

        self.data = [[None for _ in range(w)] for _ in range(h)]
        self.data_num = [[0 for _ in range(w)] for _ in range(h)]
        self.data_rect = [[pygame.Rect(rect.x+self.offset+j*size, rect.y+self.offset+i*size, MESH_SIZE, MESH_SIZE) for j in range(w)] for i in range(h)]

    def window_resize(self, rect):
        self.rect = rect
        self.data_rect = [[pygame.Rect(rect.x+self.offset+j*self.size, rect.y+self.offset+i*self.size, MESH_SIZE, MESH_SIZE) for j in range(self.w)] for i in range(self.h)]

    def get_texture(self, parent, i, j, num):  # 获取某个格子上的物品信息
        return self.data[i][j], min(num, self.data_num[i][j]), self.data_rect[i][j].copy()

    def pick_up(self, parent, i, j, num):
        # 当前格子没物品，或拿的物品数量为 0
        if self.data[i][j] is None or self.data_num[i][j] == 0 or not num:
            return

        # 拿起
        pick_up_texture, pick_up_num, pick_up_rect = self.get_texture(parent, i, j, num)
        parent.set_focus(pick_up_texture, pick_up_num, pick_up_rect)  # TODO: parent要把move改成true

        # 更新原有的物品数量
        self.data_num[i][j] -= pick_up_num
        if self.data_num[i][j] == 0:
            self.data[i][j] = None

    def put_down(self, parent, i, j, num):
        # 手里没有指定数量的物品，或格子放不下指定的数量
        focus_texture, focus_num, focus_max_num = parent.get_focus()
        put_down_num = min(focus_num, num, focus_max_num - self.data_num[i][j])

        # 放置物品
        self.data[i][j] = focus_texture
        self.data_num[i][j] += num  # 增加物品数

        # 更新手中已拿起的物品数量
        parent.set_focus(focus_texture, focus_num - put_down_num, self.data_rect[i][j])

    def change(self, parent, i, j):
        temp_data, temp_data_num = self.data[i][j], self.data_num[i][j]
        self.data[i][j], self.data_num[i][j], _ = parent.get_focus()
        parent.set_focus(temp_data, temp_data_num, self.data_rect[i][j])

    def render(self, screen, parent, mouse_x=None, mouse_y=None):
        for i in range(len(self.data_rect)):
            for j, rect in enumerate(self.data_rect[i]):
                if self.data_num[i][j] == 0 or self.data[i][j] is None:
                    continue
                if i == mouse_x and j == mouse_y:
                    pygame.draw.rect(screen, (208, 205, 209), rect)
                screen.blit(parent.get_thumbnail(), rect)
                if self.data_num[i][j] > 1:
                    num_sf, w, h = parent.get_num_sf(self.data_num[i][j])
                    num_x, num_y = rect.bottomright
                    num_x += 1 - w
                    num_y += 1 - h
                    screen.blit(num_sf, (num_x, num_y))


class MeshManager:
    def __init__(self, block_data):
        self.meshs = []
        self.block_data = block_data

        self.focus_texture = None
        self.focus_rect = None
        self.focus_num = 0
        self.move = False

    def get_focus(self):
        return self.focus_texture, self.focus_num, self.block_data[self.focus_texture].max_num

    def set_focus(self, texture, num, rect):
        self.focus_num = num
        if num == 0:
            self.move = False
            self.focus_texture = self.focus_rect = None
        else:
            self.focus_texture = texture
            self.focus_rect = rect
            self.move = True


class Inventory:
    def __init__(self, screen, block_data):
        self.block_data = block_data
        self.screen = screen
        self.w, self.h = screen.get_size()

        self.bg = pygame.transform.scale(pygame.image.load('data/物品栏.png'), (182 * 2, 22 * 2)).convert_alpha()
        self.pic_w, self.pic_h = self.bg.get_size()
        self.bg_rect = pygame.Rect((self.w-self.pic_w)//2, self.h-self.pic_h, self.pic_w, self.pic_h)

        self.set_inventory = pygame.transform.scale(pygame.image.load('data/被选中.png'), (48, 48)).convert_alpha()
        self.set_w, self.set_h = self.set_inventory.get_size()

        self.inventory = [STONE, DIAMOND_BLOCK, DIRT, COBBLESTONE, PLANKS, BEDROCK, CRAFTING_TABLE, SAND, GRAVEL]   # 玩家可以放置的方块列表。
        self.inventory_index = 0  # 用户可以放置的当前方块。
        self.inventory_num = [64, 64, 64, 64, 64, 64, 64, 64, 64]  # 每个格子的方块数量

        self.mode = 0  # 是否无限放置
        self.font = pygame.font.Font('data/unifont.otf', 17)
        self.font_nums = [self.font.render(str(i), True, (255,) * 3).convert_alpha() for i in range(65)]

    def update_size(self):
        self.w, self.h = self.screen.get_size()
        self.bg_rect = pygame.Rect((self.w - self.pic_w) // 2, self.h - self.pic_h, self.pic_w, self.pic_h)

    def set_index(self, index):
        self.inventory_index = index

    def get_block(self):
        res = self.inventory[self.inventory_index]
        if not res or self.mode:  # 没有物品或是创造模式
            return res
        self.inventory_num[self.inventory_index] -= 1  # 物品数量减一
        if self.inventory_num[self.inventory_index] == 0:  # 物品取完
            self.inventory[self.inventory_index] = None
        return res

    def get_rect(self, index):
        return pygame.Rect(self.bg_rect.x + (self.set_w - 8) * index - 2, self.bg_rect.y-2, self.set_w, self.set_h)

    def render(self):
        self.screen.blit(self.bg, self.bg_rect)
        for i, texture in enumerate(self.inventory):
            if texture is None:
                continue
            self.block_data[texture].render(self.screen,
                                            self.block_data[texture].thumbnail.get_rect(center=self.get_rect(i).center),
                                            self.inventory_num[i])
        self.screen.blit(self.set_inventory, self.get_rect(self.inventory_index))


class BackPack:
    def __init__(self, screen, inventory, block_data):
        self.block_data = block_data
        self.screen = screen
        self.inventory = inventory
        self.bg = pygame.transform.scale(pygame.image.load('data/背包.png'), (704//2, 664//2)).convert_alpha()
        self.bg_black = pygame.Surface((1, 1), pygame.SRCALPHA)
        self.bg_black.fill((0, 0, 0, 150))
        self.bg_blacks = {}
        self.bg_rect = self.bg.get_rect(center=self.screen.get_rect().center)
        x, y = self.bg_rect.bottomleft

        self.backpack = [[None for _ in range(9)], [None for _ in range(9)],
                         [None for _ in range(9)], self.inventory.inventory,
                         [None for _ in range(5)]]
        self.backpack = [[TNT, BOOKSHELF, MOSSY_COBBLESTONE, OBSIDIAN, CHEST, SPONGE, GLASS, RED_CLOTH, ORANGE_CLOTH],
                         [YELLOW_CLOTH, LIME_CLOTH, GREEN_CLOTH, AQUA_CLOTH, CYAN_CLOTH, BLUE_CLOTH, PURPLE_CLOTH, INDIGO_CLOTH, VIOLET_CLOTH],
                         [MAGENTA_CLOTH, PINK_CLOTH, BLACK_CLOTH, GREY_CLOTH, WHITE_CLOTH, GOLD_BLOCK, IRON_BLOCK, DOUBLE_SLAB, BRICKS],
                         self.inventory.inventory,
                         [None for _ in range(5)]]
        no = [WATER, GOLD_ORE, IRON_ORE, COAL_ORE, DIAMOND_ORE, GRASS, LOG, LEAVES, REDSTONE_ORE, LIT_REDSTONE_ORE, LIT_FURNACE]
        _x = [[FURNACE, SNOW_BLOCK, CLAY, JUKEBOX]]
        self.backpack_num = [[64 for _ in range(9)], [64 for _ in range(9)],
                             [64 for _ in range(9)], self.inventory.inventory_num,
                             [0 for _ in range(5)]]
        self.backpack_rect = [[pygame.Rect(x + 16 + i * 36, y - 116 - 48, 32, 32) for i in range(9)],
                              [pygame.Rect(x + 16 + i * 36, y - 80 - 48, 32, 32) for i in range(9)],
                              [pygame.Rect(x + 16 + i * 36, y - 44 - 48, 32, 32) for i in range(9)],
                              [pygame.Rect(x + 16 + i * 36, y - 48, 32, 32) for i in range(9)],
                              [pygame.Rect(300 + j, 186 + i, 32, 32) for i in (0, 36) for j in (0, 36)] +
                              [pygame.Rect(412, 206, 32, 32)]]

        self.focus_texture = None
        self.focus_rect = None
        self.focus_num = None
        self.move = False

    def update_size(self):
        self.bg_rect = self.bg.get_rect(center=self.screen.get_rect().center)
        x, y = self.bg_rect.bottomleft
        self.backpack_rect = [[pygame.Rect(x + 16 + i * 36, y - 116 - 48, 32, 32) for i in range(9)],
                              [pygame.Rect(x + 16 + i * 36, y - 80 - 48, 32, 32) for i in range(9)],
                              [pygame.Rect(x + 16 + i * 36, y - 44 - 48, 32, 32) for i in range(9)],
                              [pygame.Rect(x + 16 + i * 36, y - 48, 32, 32) for i in range(9)],
                              [pygame.Rect(300 + j, 186 + i, 32, 32) for i in (0, 36) for j in (0, 36)] +
                              [pygame.Rect(412, 206, 32, 32)]]

    def render(self):
        if self.screen.get_size() not in self.bg_blacks:
            self.bg_blacks[self.screen.get_size()] = pygame.transform.scale(self.bg_black, self.screen.get_size()).convert_alpha()
        self.screen.blit(self.bg_blacks[self.screen.get_size()], (0, 0))
        self.screen.blit(self.bg, self.bg_rect)
        pos = self.get_mouse_index(pygame.mouse.get_pos())
        for i in range(5):
            for j in range(len(self.backpack_num[i])):
                if i == pos[0] and j == pos[1]:
                    pygame.draw.rect(self.screen, (208, 205, 209), self.backpack_rect[i][j])
                if self.backpack[i][j] is None or not self.backpack_num[i][j]:
                    continue
                self.block_data[self.backpack[i][j]].render(self.screen, self.backpack_rect[i][j], self.backpack_num[i][j])
        if self.move:
            self.block_data[self.focus_texture].render(self.screen, self.focus_rect, self.focus_num)

    def get_mouse_index(self, mouse_pos):  # 获取鼠标光标在哪一个格子
        x, y = mouse_pos
        for i, rect in enumerate(self.backpack_rect[4]):
            if rect.collidepoint(mouse_pos):
                return 4, i
        for line in range(4):
            if self.backpack_rect[line][0].top-2 <= y < self.backpack_rect[line][0].bottom+2:
                if self.backpack_rect[line][0].left - 2 <= x < self.backpack_rect[line][-1].right + 2:
                    return line, (x - (self.backpack_rect[line][0].left - 2)) // 36
        return None, None

    def get_index_texture(self, i, j, num):  # 获取某个格子上的物品信息
        if i == 4 and j == 4:
            return CRAFTING.pick_res(self.backpack[4], self.backpack_num[4])
        return self.backpack[i][j], min(num, self.backpack_num[i][j])

    def pick_up(self, i, j, num):  # 拿起某个格子上的物品
        # 当前格子没物品，或拿的物品数量为 0
        if self.backpack[i][j] is None or self.backpack_num[i][j] == 0 or not num:
            return

        # 拿起
        self.focus_texture, self.focus_num = self.get_index_texture(i, j, num)
        self.focus_rect = self.backpack_rect[i][j].copy()
        self.move = True

        # 更新原有的物品数量
        self.backpack_num[i][j] -= self.focus_num
        if self.backpack_num[i][j] == 0:
            self.backpack[i][j] = None

    def put_down(self, i, j, num):
        # 手里没有指定数量的物品，或格子放不下指定的数量
        num = min(self.focus_num, num, self.block_data[self.focus_texture].max_num - self.backpack_num[i][j])

        # 放置物品
        self.backpack[i][j] = self.focus_texture
        self.backpack_num[i][j] += num  # 增加物品数

        # 更新手中已拿起的物品数量
        self.focus_num -= num
        if self.focus_num == 0:  # 物品全放完了
            self.focus_texture = self.focus_num = self.focus_rect = None
            self.move = False

    def change(self, i, j):  # 把当前拿的物品和当前格子里的物品交换
        self.focus_texture, self.backpack[i][j] = self.backpack[i][j], self.focus_texture
        self.focus_num, self.backpack_num[i][j] = self.backpack_num[i][j], self.focus_num

    def on_mouse_press(self, button, pos):  # 按下鼠标
        i, j = self.get_mouse_index(pos)
        if i is None or j is None or button not in (1, 3):  # 鼠标不在有效的背包格子中，或者不是有效的按键
            return
        pick_num = {1: self.backpack_num[i][j], 3: max(self.backpack_num[i][j]//2, 1)}
        put_num = {1: self.focus_num, 3: 1}
        if not self.move:  # 不在拖动物品
            self.pick_up(i, j, pick_num[button])
        elif i != 4 or j != 4:  # 不是合成格
            if self.backpack[i][j] is None or self.backpack[i][j] == self.focus_texture:  # 同种物品或无物品
                self.put_down(i, j, put_num[button])  # 放物品
            else:
                self.change(i, j)  # 否则交换物品
        elif self.backpack[4][4] and self.backpack[4][4] == self.focus_texture:
            if self.backpack_num[i][j] + self.focus_num <= self.focus_texture.max_num:
                self.focus_num += CRAFTING.pick_res(self.backpack[4], self.backpack_num[4])[1]

        self.backpack[4][4], self.backpack_num[4][4] = CRAFTING.check(self.backpack[4][:4], self.backpack_num[4][:4])

    def on_mouse_motion(self, rel):
        if self.move:
            self.focus_rect.move_ip(*rel)
