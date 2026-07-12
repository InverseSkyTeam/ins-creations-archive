import time
from options import *
from numba import njit
from collections import deque
from noise_gen import NoiseGen
import random
import numpy as np

from configure import *
from render import WorldModel
from block_data import cube_model


@njit
def normalize(position):  # 将 position 坐标取整
    x, y, z = position
    x, y, z = round(x), round(y), round(z)
    return x, y, z


def sectorize(position):   # 返回位置 position 所在区块的坐标。
    x, y, z = normalize(position)  # 将位置取整
    x, y, z = x // SECTOR_SIZE, y // SECTOR_SIZE, z // SECTOR_SIZE  # 根据SECTOR_SIZE将位置转换为区块坐标
    return x, 0, z


class World(object):
    def __init__(self, block_data):
        self.size = 128  # 世界大小
        self.world = {}  # 存储某个位置的方块对应的纹理

        self.shown = {}  # 和`world`相同，但只包含显示的方块。

        # 存储某个位置的方块的顶点数据、边数据、纹理数据
        self._shown_vertices = {}
        self._shown_indices = {}
        self._shown_uv_index = {}

        # 存储某个区块中的所有方块的纹理
        self.sectors = {}

        # 简单的函数队列实现。队列由 _show_block() 和 _hide_block() 方法调用填充。
        self.queue = deque()

        self.block_data = block_data
        self.model = WorldModel(block_data.texture_manager, cube_model.uv_vertices, cube_model.uv_indices)

    def initialize(self, seed=452692):  # 生成世界
        print("开始生成世界")
        gen = NoiseGen(seed)
        random.seed(11)

        range_n = np.arange(self.size)

        print('初始化地形高度')
        height_map = np.zeros((self.size, self.size))
        for x in range_n:
            for z in range_n:
                height_map[x, z] = int(gen.getHeight(x, z))
        print('地形高度初始化完成')

        # 生成世界
        for x in range_n:
            for z in range_n:
                h = height_map[x, z]
                self.add_block((x, 0, z), BEDROCK, immediate=False)
                if h < 15:
                    for y in np.arange(1, max(int(h / 2), 2)):
                        self.add_block((x, y, z), STONE, immediate=False)
                    for y in np.arange(max(int(h / 2), 2), 15):
                        self.add_block((x, y, z), WATER, immediate=False)
                    continue
                self.add_block((x, h, z), GRASS, immediate=False)
                for y in np.arange(h - 1, 0, -1):
                    self.add_block((x, y, z), STONE, immediate=False)
                # 可能在这个位置(x, z)添加树
                if h > 20:
                    if random.randrange(0, 1000) > 990:
                        tree_height = random.randrange(5, 7)
                        # 树干
                        for y in np.arange(h + 1, h + tree_height):
                            self.add_block((x, y, z), LOG, immediate=False)
                        # 树叶
                        leafh = h + tree_height
                        for lz in np.arange(z + -2, z + 3):
                            for lx in np.arange(x + -2, x + 3):
                                for ly in np.arange(3):
                                    self.add_block((lx, leafh + ly, lz), LEAVES, immediate=False)
        print("世界生成完成")

    def hit_test(self, position, vector, max_distance=7):
        """从当前位置进行视线搜索。如果遇到方块，则返回该方块以及视线上的前一个方块。
        如果没有找到方块，则返回None，None。

        参数
        ----------
        position : 长度为3的元组
            要检查可见性的位置(x, y, z)。
        vector : 长度为3的元组
            视线向量。
        max_distance : 整数
            搜索碰撞的最大距离（单位：方块）。

        """
        m = 8
        x, y, z = position
        dx, dy, dz = vector
        previous = None
        for _ in range(max_distance * m):
            key = normalize((x, y, z))
            if key != previous and key in self.world:
                return key, previous
            previous = key
            x, y, z = x + dx / m, y + dy / m, z + dz / m
        return None, None

    def exposed(self, position):
        """如果给定的`position`在所有6个面都被方块包围，则返回False，否则返回True。

        """
        x, y, z = position
        for dx, dy, dz in FACES:
            if (x + dx, y + dy, z + dz) not in self.world:
                return True
            if (x + dx, y + dy, z + dz) in self.world and self.world[(x + dx, y + dy, z + dz)] in (GLASS, LEAVES):
                return True
        return False

    def add_block(self, position, texture, immediate=True):
        """将带有给定纹理和位置的方块添加到世界中。

        参数
        ----------
        position：长度为3的元组
            要添加的方块的(x, y, z)位置。
        texture：长度为3的列表
            纹理方块的坐标。使用`tex_coords()`生成。
        immediate：bool
            是否立即绘制方块。

        """
        if position in self.world:
            self.remove_block(position, immediate)
        self.world[position] = texture
        self.sectors.setdefault(sectorize(position), []).append(position)
        if immediate:
            if self.exposed(position):
                self.show_block(position)
            self.check_neighbors(position)

    def remove_block(self, position, immediate=True):
        """删除给定位置处的方块。

        参数
        ----------
        position：长度为3的元组
            要删除的方块的(x, y, z)位置。
        immediate：bool
            是否立即从画布中移除方块。

        """
        del self.world[position]
        self.sectors[sectorize(position)].remove(position)
        if immediate:
            if position in self.shown:
                self.hide_block(position)
            self.check_neighbors(position)

    def check_neighbors(self, position):
        """检查“position”周围的所有方块，并确保它们的可视状态是准确的。
        这意味着隐藏未显示的方块，并显示所有暴露的方块。通常在添加或删除方块后使用。

        """
        x, y, z = position
        for dx, dy, dz in FACES:
            key = (x + dx, y + dy, z + dz)
            if key not in self.world:
                continue
            if self.exposed(key):
                if key not in self.shown:
                    self.show_block(key)
            else:
                if key in self.shown:
                    self.hide_block(key)

    def show_block(self, position, immediate=True):
        """显示给定位置处的方块。这个方法假设方块已经使用add_block()方法添加了。

        参数
        ----------
        position：长度为3的元组
            要显示的方块的(x, y, z)位置。
        immediate：bool
            是否立即显示方块。

        """
        texture = self.world[position]
        self.shown[position] = texture
        if immediate:
            self._show_block(position, texture)
        else:
            self._enqueue(self._show_block, position, texture)

    def _show_block(self, position, texture_index):
        """show_block()方法的私有实现。

        参数
        ----------
        position：长度为3的元组
            要显示的方块的(x, y, z)位置。
        texture：长度为3的列表
            纹理方块的坐标。使用`tex_coords()`生成。

        """
        x, y, z = position
        texture = self.block_data[texture_index]
        new_vertices = texture.model.vertices.copy()
        new_vertices[:, 0, 0] += x
        new_vertices[:, 1, 0] += y
        new_vertices[:, 2, 0] += z
        self._shown_vertices[position] = new_vertices
        self._shown_indices[position] = texture.model.indices.copy()
        self._shown_uv_index[position] = texture.tex_indices_triangle.copy()

    def hide_block(self, position, immediate=True):
        """隐藏给定位置处的方块。隐藏不会从世界中移除方块。

        参数
        ----------
        position：长度为3的元组
            要隐藏的方块的(x, y, z)位置。
        immediate：bool
            是否立即从画布中移除方块。

        """
        self.shown.pop(position)
        if immediate:
            self._hide_block(position)
        else:
            self._enqueue(self._hide_block, position)

    def _hide_block(self, position):
        """hide_block()方法的私有实现。

        """
        self._shown_vertices.pop(position)
        self._shown_indices.pop(position)
        self._shown_uv_index.pop(position)

    def show_sector(self, sector):
        """确保需要显示的给定区块中的所有方块都绘制到画布上。

        """
        for position in self.sectors.get(sector, []):
            if position not in self.shown and self.exposed(position):
                self.show_block(position, False)

    def hide_sector(self, sector):
        """确保需要隐藏的给定区块中的所有方块都从画布中移除。

        """
        for position in self.sectors.get(sector, []):
            if position in self.shown:
                self.hide_block(position, False)

    def change_sectors(self, before, after):
        """从“before”区块移动到“after”区块。区块是世界的连续x、y子区域。区块用于加速世界渲染。

        """
        before_set = set()
        after_set = set()
        pad = 4
        for dx in range(-pad, pad + 1):
            dy = 0
            for dz in range(-pad, pad + 1):
                if dx ** 2 + dy ** 2 + dz ** 2 > (pad + 1) ** 2:
                    continue
                if before:
                    x, y, z = before
                    before_set.add((x + dx, y + dy, z + dz))
                if after:
                    x, y, z = after
                    after_set.add((x + dx, y + dy, z + dz))
        show = after_set - before_set
        hide = before_set - after_set
        for sector in show:
            self.show_sector(sector)
        for sector in hide:
            self.hide_sector(sector)

    def _enqueue(self, func, *args):
        """将“func”添加到内部队列中。

        """
        self.queue.append((func, args))

    def _dequeue(self):
        """从内部队列中弹出顶部函数并调用它。

        """
        func, args = self.queue.popleft()
        func(*args)

    def process_queue(self):
        """在定期休息的同时处理整个队列。这样可以使游戏循环顺利运行。
        队列包含对_show_block()和_hide_block()的调用，所以如果add_block()或remove_block()使用immediate=False调用，应该调用该方法。

        """
        start = time.process_time()
        while self.queue and time.process_time() - start < 1.0 / TICKS_PER_SEC:
            self._dequeue()

    def process_entire_queue(self):
        """处理整个队列，没有休息。

        """
        while self.queue:
            self._dequeue()

    def render(self):
        cube_num = len(self._shown_vertices)
        if cube_num <= 0:
            return True
        vertices = np.concatenate(list(self._shown_vertices.values()), axis=0)
        indices = np.concatenate(list(self._shown_indices.values()), axis=0)
        uv_index = np.concatenate(list(self._shown_uv_index.values()), axis=0)
        indices += np.repeat(np.arange(0, cube_num * 8, 8), repeats=12)[:, None]
        self.model.vertices = vertices
        self.model.indices = indices
        self.model.uv_index = uv_index
        return False
