import chunk
import math
import numpy as np
from collections import deque
import np_gl
import block_type
import models
import save
from util import DIRECTIONS_TUPLE
import pygame
import time
from numba import njit


@njit(fastmath=True)
def dist1(p, q):
    return math.sqrt((p[0]-q[0])**2 + (p[2]-q[2])**2)


def get_chunk_position(position):  # 获取某个位置所在的区块位置
    x, y, z = position

    return x // chunk.CHUNK_WIDTH, y // chunk.CHUNK_HEIGHT, z // chunk.CHUNK_LENGTH


def get_local_position(position):  # 获取某个位置在所在区块中的相对位置
    x, y, z = position
    
    return int(x % chunk.CHUNK_WIDTH), int(y % chunk.CHUNK_HEIGHT), int(z % chunk.CHUNK_LENGTH)


class World:
    def __init__(self, player, texture_manager, options):
        self.options = options
        self.player = player
        self.texture_manager = texture_manager
        self.block_types = [None]  # 方块类型数组，以方块编号为索引

        self.daylight = 1800
        self.incrementer = 0
        self.time = 0

        # 兼容
        self.get_chunk_position = get_chunk_position
        self.get_local_position = get_local_position

        # 解析方块属性文档

        blocks_data_file = open("data/blocks.mcpy")
        blocks_data = blocks_data_file.readlines()
        blocks_data_file.close()

        # Loading block models
        for block in blocks_data:
            if block[0] in ['\n', '#']:  # 跳过注释和空行
                continue
            
            number, props = block.split(':', 1)
            number = int(number)  # 方块编号

            # 默认方块

            name = "Unknown"
            model = models.cube
            texture = {"all": "unknown"}

            # 读取方块属性

            for prop in props.split(','):  # 不同的属性用逗号分隔
                prop = prop.strip()  # 去掉首尾空格
                prop = list(filter(None, prop.split(' ', 1)))  # 用空格分隔属性名和属性内容

                if prop[0] == "sameas":
                    sameas_number = int(prop[1])

                    name = self.block_types[sameas_number].name
                    texture = self.block_types[sameas_number].block_face_textures
                    model = self.block_types[sameas_number].model
                
                elif prop[0] == "name":
                    name = eval(prop[1])
                
                elif prop[0][:7] == "texture":
                    _, side = prop[0].split('.')
                    texture[side] = prop[1].strip()

                elif prop[0] == "model":
                    model = eval(prop[1])
            
            # 添加方块类型

            _block_type = block_type.Block_type(self.texture_manager, name, texture, model)

            if number < len(self.block_types):
                self.block_types[number] = _block_type
            
            else:
                self.block_types.append(_block_type)

        self.light_blocks = [10, 11, 50, 51, 62, 75]  # 是光源的方块编号
        self.light_blocks = [i for i in self.light_blocks if not self.block_types[i].model.translucent]
        # print(self.light_blocks)
        self.block_transparency = [(2 if not i else i.transparent) for i in self.block_types]
        self.block_opaque = [(False if not i else (not i.transparent)) for i in self.block_types]
        self.block_is_cube = [(i.is_cube if i is not None else None) for i in self.block_types]
        self.block_glass = [(i.glass if i is not None else None) for i in self.block_types]

        # load the world

        self.save = save.Save(self)

        self.chunks = {}

        # light update queue

        self.light_increase_queue = deque()  # Node: World Position, light
        self.light_decrease_queue = deque()  # Node: World position, light
        self.skylight_increase_queue = deque()
        self.skylight_decrease_queue = deque()
        self.chunk_building_queue = deque()

        print('加载存档中...\n')
        self.save.load()

        print("计算光照中...")
        for i, world_chunk in enumerate(self.chunks.values()):
            a = time.time()
            self.init_skylight(world_chunk)
            b = time.time()
            print(f'第 {i+1}/{len(self.chunks.values())} 个区块计算成功，用时 {round(b-a, 3)}s')

        for world_chunk in self.chunks.values():
            world_chunk.update_subchunk_meshes()

        self.visible_chunks = []

        # Debug variables

        self.pending_chunk_update_count = 0
        self.chunk_update_counter = 0

        print('\n\n生成区块中...')
        for i, world_chunk in enumerate(self.chunks.values()):
            a = time.time()
            world_chunk.process_chunk_updates1()
            b = time.time()
            print(f'第 {i+1}/{len(self.chunks.values())} 个区块生成成功，用时 {round(b-a, 3)}s')

    def increase_light(self, world_pos, newlight, light_update=True):  # 添加光源, newlight指光源的光照强度
        _chunk = self.chunks[get_chunk_position(world_pos)]  # 光源所在的区块
        local_pos = get_local_position(world_pos)  # 光源相对所在区块的坐标

        _chunk.set_block_light(*local_pos, newlight)

        self.light_increase_queue.append((world_pos, newlight))

        self.propagate_increase(light_update)

    def propagate_increase(self, light_update):
        """开始传播所有排队的块光增加
        该算法源自仙女座星球的教程
        它使用一个FIFO队列来排队待处理的块以进行照明
        然后检查其6个相邻块，并将光传播到其中一个，如果后者的光级别低于前者"""

        while self.light_increase_queue:
            pos, light_level = self.light_increase_queue.popleft()            

            for direction in DIRECTIONS_TUPLE:
                neighbour_pos = (pos[0] + direction[0], pos[1] + direction[1], pos[2] + direction[2])

                _chunk = self.chunks.get(get_chunk_position(neighbour_pos), None)
                if not _chunk:
                    continue
                lx, ly, lz = get_local_position(neighbour_pos)

                if not self.block_opaque[_chunk.blocks[lx][ly][lz]] and _chunk.get_block_light(lx, ly, lz) + 2 <= light_level:  # 新位置透明且新位置的光照强度低于当前位置光照强度
                    _chunk.set_block_light(lx, ly, lz, light_level - 1)

                    self.light_increase_queue.append((neighbour_pos, light_level - 1))

                    if light_update:
                        _chunk.update_at_position(neighbour_pos)
                        cx, cy, cz = get_chunk_position(neighbour_pos)
                        x, y, z = neighbour_pos

                        def try_update_chunk_at_position(_chunk_position, _position):
                            if _chunk_position in self.chunks:
                                self.chunks[_chunk_position].update_at_position(_position)

                        if lx == chunk.CHUNK_WIDTH - 1:
                            try_update_chunk_at_position((cx + 1, cy, cz), (x + 1, y, z))
                        if lx == 0:
                            try_update_chunk_at_position((cx - 1, cy, cz), (x - 1, y, z))

                        if ly == chunk.CHUNK_HEIGHT - 1:
                            try_update_chunk_at_position((cx, cy + 1, cz), (x, y + 1, z))
                        if ly == 0:
                            try_update_chunk_at_position((cx, cy - 1, cz), (x, y - 1, z))

                        if lz == chunk.CHUNK_LENGTH - 1:
                            try_update_chunk_at_position((cx, cy, cz + 1), (x, y, z + 1))
                        if lz == 0:
                            try_update_chunk_at_position((cx, cy, cz - 1), (x, y, z - 1))

    def init_skylight(self, pending_chunk):
        """ Initializes the skylight of each chunks
        To avoid unsufferable lag from propagating from the top of the chunks when
        most of the heights would be air, it instead runs a simple algorithm
        to check where the highest point of the chunk is and propagates skylight from
        this height"""
        chunk_pos = pending_chunk.position

        # 检测某区块内最高的方块的高度
        height = 0
        for lx in range(chunk.CHUNK_WIDTH):
            for lz in range(chunk.CHUNK_LENGTH):
                for ly in range(chunk.CHUNK_HEIGHT - 1, -1, -1):
                    if pending_chunk.blocks[lx][ly][lz]:
                        break
                if ly > height:
                    height = ly

        # Initialize skylight to 15 until that point and then queue a skylight propagation increase
        for lx in range(chunk.CHUNK_WIDTH):
            for lz in range(chunk.CHUNK_LENGTH):
                for ly in range(chunk.CHUNK_HEIGHT - 1, height, -1):
                    pending_chunk.set_sky_light(lx, ly, lz, 15)
                pos = (chunk_pos[0] + lx, height+1, chunk_pos[2] + lz)
                self.skylight_increase_queue.append((pos, 15))

        self.propagate_skylight_increase(False)
        
    def propagate_skylight_increase(self, light_update):
        """Similar to the block light algorithm, but 
        do not lower the light level in the downward direction"""
        while self.skylight_increase_queue:
            pos, light_level = self.skylight_increase_queue.popleft()

            for direction in DIRECTIONS_TUPLE:
                neighbour_pos = (pos[0] + direction[0], pos[1] + direction[1], pos[2] + direction[2])
                if neighbour_pos[1] > chunk.CHUNK_HEIGHT:
                    continue

                _chunk = self.chunks.get(get_chunk_position(neighbour_pos), None)
                if not _chunk:
                    continue
                lx, ly, lz = get_local_position(neighbour_pos)

                transparency = self.block_transparency[_chunk.blocks[lx][ly][lz]]

                if transparency and ((_chunk.lightmap[lx][ly][lz] >> 4) & 0xF) < light_level:
                    newlight = light_level + transparency - 2

                    if light_update:
                        _chunk.update_at_position(neighbour_pos)

                    if direction[1] == -1:
                        _chunk.lightmap[lx][ly][lz] = (_chunk.lightmap[lx][ly][lz] & 0xF) | (newlight << 4)
                        # _chunk.set_sky_light(lx, ly, lz, newlight)
                        self.skylight_increase_queue.append((neighbour_pos, newlight))
                    elif ((_chunk.lightmap[lx][ly][lz] >> 4) & 0xF) + 2 <= light_level:
                        _chunk.lightmap[lx][ly][lz] = (_chunk.lightmap[lx][ly][lz] & 0xF) | ((newlight - 1) << 4)
                        # _chunk.set_sky_light(lx, ly, lz, newlight - 1)
                        self.skylight_increase_queue.append((neighbour_pos, newlight - 1))

    def decrease_light(self, world_pos):
        _chunk = self.chunks[get_chunk_position(world_pos)]
        local_pos = get_local_position(world_pos)
        old_light = _chunk.get_block_light(*local_pos)
        _chunk.set_block_light(*local_pos, 0)
        self.light_decrease_queue.append((world_pos, old_light))
        
        self.propagate_decrease(True)
        self.propagate_increase(True)

    def propagate_decrease(self, light_update):
        """Starts propagating all queued block light decreases
        This algorithm is derived from the Seed of Andromeda's tutorial
        It uses a FIFO queue to queue the pending blocks to unlight
        It then checks its 6 neighbours and unlight to one of them if the latter's light level 
        is lower than the former one"""

        while self.light_decrease_queue:
            pos, light_level = self.light_decrease_queue.popleft()

            for direction in DIRECTIONS_TUPLE:
                neighbour_pos = (pos[0] + direction[0], pos[1] + direction[1], pos[2] + direction[2])

                _chunk = self.chunks.get(get_chunk_position(neighbour_pos), None)
                if not _chunk: continue
                lx, ly, lz = get_local_position(neighbour_pos)
                block_number = _chunk.blocks[lx][ly][lz]

                if block_number in self.light_blocks:
                    self.light_increase_queue.append((neighbour_pos, 15))
                    continue

                if not self.block_opaque[block_number]:
                    neighbour_level = _chunk.get_block_light(lx, ly, lz)
                    if not neighbour_level:
                        continue

                    if neighbour_level < light_level:
                        _chunk.set_block_light(lx, ly, lz, 0)
                        if light_update:
                            _chunk.update_at_position(neighbour_pos)
                        self.light_decrease_queue.append((neighbour_pos, neighbour_level))
                    elif neighbour_level >= light_level:
                        self.light_increase_queue.append((neighbour_pos, neighbour_level))

    def decrease_skylight(self, world_pos, light_update=True):
        _chunk = self.chunks[get_chunk_position(world_pos)]
        local_pos = get_local_position(world_pos)
        old_light = _chunk.get_sky_light(*local_pos)
        _chunk.set_sky_light(*local_pos, 0)
        self.skylight_decrease_queue.append((world_pos, old_light))
        
        self.propagate_skylight_decrease(light_update)
        self.propagate_skylight_increase(light_update)

    def propagate_skylight_decrease(self, light_update=True):
        """Similar to the block light algorithm, but 
        always unlight in the downward direction"""
        while self.skylight_decrease_queue:
            pos, light_level = self.skylight_decrease_queue.popleft()

            for direction in DIRECTIONS_TUPLE:
                neighbour_pos = (pos[0] + direction[0], pos[1] + direction[1], pos[2] + direction[2])

                _chunk = self.chunks.get(get_chunk_position(neighbour_pos), None)
                if not _chunk:
                    continue
                lx, ly, lz = get_local_position(neighbour_pos)

                if self.block_transparency[_chunk.blocks[lx][ly][lz]]:
                    neighbour_level = _chunk.get_sky_light(lx, ly, lz)
                    if not neighbour_level:
                        continue
                    if direction[1] == -1 or neighbour_level < light_level:
                        _chunk.set_sky_light(lx, ly, lz, 0)
                        if light_update:
                            _chunk.update_at_position(neighbour_pos)
                        self.skylight_decrease_queue.append((neighbour_pos, neighbour_level))
                    elif neighbour_level >= light_level:
                        self.skylight_increase_queue.append((neighbour_pos, neighbour_level))

    # Getter and setters
    def get_raw_light(self, position):  # 获取方块原始光照强度
        _chunk = self.chunks.get(get_chunk_position(position), None)
        if not _chunk:  # 空气
            return 15 << 4
        local_position = self.get_local_position(position)
        return _chunk.get_raw_light(*local_position)

    def get_light(self, position):  # 获取方块光照强度
        _chunk = self.chunks.get(get_chunk_position(position), None)
        if not _chunk:  # 空气
            return 0
        local_position = self.get_local_position(position)
        return _chunk.get_block_light(*local_position)

    def get_skylight(self, position):  # 获取太阳光照强度
        _chunk = self.chunks.get(get_chunk_position(position), None)
        if not _chunk:  # 空气
            return 15
        local_position = self.get_local_position(position)
        return _chunk.get_sky_light(*local_position)

    def set_light(self, position, light):  # 设置方块光照强度
        _chunk = self.chunks.get(get_chunk_position(position), None)
        local_position = get_local_position(position)
        _chunk.set_block_light(*local_position, light)

    def set_skylight(self, position, light):  # 设置太阳光照强度
        _chunk = self.chunks.get(get_chunk_position(position), None)
        local_position = get_local_position(position)
        _chunk.set_sky_light(*local_position, light)

    #################################################
    
    def get_block_number(self, position):  # 获取世界中的方块的编号
        chunk_position = get_chunk_position(position)

        if chunk_position not in self.chunks:
            return 0
        
        lx, ly, lz = get_local_position(position)

        block_number = self.chunks[chunk_position].blocks[lx][ly][lz]
        return block_number

    def get_transparency(self, position):
        return self.block_transparency[self.get_block_number(position)]

    def is_opaque_block(self, position):
        # get block type and check if it's opaque or not
        # air counts as a transparent block, so test for that too
        return self.block_opaque[self.get_block_number(position)]
    
    def create_chunk(self, chunk_position):  # 创建区块
        self.chunks[chunk_position] = chunk.Chunk(self, np.array(chunk_position, dtype=np.int32))
        self.init_skylight(self.chunks[chunk_position])
        _x, _y, _z = chunk_position
        for x in (-1, 0, 1):
            for z in (-1, 0, 1):
                _chunk = self.chunks.get((_x + x, _y, _z + z), None)
                if _chunk is None:
                    continue
                for _subchunk in _chunk.subchunks:
                    _chunk.subchunks[_subchunk].init()
    
    def set_block(self, position, number):  # 设置0号方块（空气）可以删除方块
        x, y, z = position
        chunk_position = get_chunk_position(position)

        if chunk_position not in self.chunks:  # 如果此位置不存在区块，则创建一个新区块
            if number == 0:
                return  # 如果我们不打算添加任何内容，那么创建一个全新的区块就没有意义了

            self.create_chunk(chunk_position)
        
        if self.get_block_number(position) == number:  # 如果方块是相同的，更新网格就没有意义了
            return
        
        lx, ly, lz = get_local_position(position)

        self.chunks[chunk_position].blocks[lx][ly][lz] = number
        self.chunks[chunk_position].modified = True

        self.chunks[chunk_position].update_at_position((x, y, z))

        if number:
            if number in self.light_blocks:
                self.increase_light((x, y, z), 15)

            elif self.block_types[number].transparent != 2:
                self.decrease_light((x, y, z))
                self.decrease_skylight((x, y, z))
        
        elif not number:
            self.decrease_light((x, y, z))
            self.decrease_skylight((x, y, z))

        cx, cy, cz = chunk_position

        def try_update_chunk_at_position(_chunk_position, _position):
            if _chunk_position in self.chunks:
                self.chunks[_chunk_position].update_at_position(_position)
        
        if lx == chunk.CHUNK_WIDTH - 1:
            try_update_chunk_at_position((cx + 1, cy, cz), (x + 1, y, z))
        if lx == 0:
            try_update_chunk_at_position((cx - 1, cy, cz), (x - 1, y, z))

        if ly == chunk.CHUNK_HEIGHT - 1:
            try_update_chunk_at_position((cx, cy + 1, cz), (x, y + 1, z))
        if ly == 0:
            try_update_chunk_at_position((cx, cy - 1, cz), (x, y - 1, z))

        if lz == chunk.CHUNK_LENGTH - 1:
            try_update_chunk_at_position((cx, cy, cz + 1), (x, y, z + 1))
        if lz == 0:
            try_update_chunk_at_position((cx, cy, cz - 1), (x, y, z - 1))

    def try_set_block(self, position, number, collider):
        # if we're trying to remove a block, whatever let it go through

        if not number:
            return self.set_block(position, 0)

        # make sure the block doesn't intersect with the passed collider

        for block_collider in self.block_types[number].colliders:
            if collider & (block_collider + position):
                return
        
        self.set_block(position, number)

    def toggle_AO(self):
        self.options.SMOOTH_LIGHTING = not self.options.SMOOTH_LIGHTING
        for _chunk in self.chunks.values():
            _chunk.update_subchunk_meshes()

    def speed_daytime(self):
        if self.daylight <= 480:
            self.incrementer = 1
        if self.daylight >= 1800:
            self.incrementer = -1

    def prepare_rendering(self):
        player_chunk = self.get_chunk_position(self.player.position)
        chunk_positions = np.array(list(self.chunks.keys()), dtype=np.float64)
        player_chunk_np = np.array(player_chunk, dtype=np.float64)
        player_chunk_np[1] = 0
        distance = np.sqrt(np.sum((player_chunk_np - chunk_positions) ** 2, axis=1))
        sort_index = np.argsort(distance)
        mask = distance[sort_index] < self.options.RENDER_DISTANCE
        visible_chunk_positions = chunk_positions[sort_index][mask]
        self.visible_chunks = [self.chunks[tuple(chunk_position)] for chunk_position in visible_chunk_positions if self.player.check_in_frustum(chunk_position)]

    def draw(self, screen):
        daylight_multiplier = self.daylight / 1800
        screen.fill((min(0.5 * (daylight_multiplier - 0.26) * 255, 255),
                     min(0.8 * (daylight_multiplier - 0.26) * 255, 255),
                     min((daylight_multiplier - 0.26) * 1.36 * 255, 255)))

        z_buffer = np.full(screen.get_size(), np.inf, dtype=np.float64)  # 深度缓冲数组

        viewport = np_gl.glViewport(0, 0, *screen.get_size())
        final_matrix = np.dot(viewport, self.player.mvp_matrix_np).T

        _screen = pygame.surfarray.pixels3d(screen)

        for render_chunk in self.visible_chunks:
            render_chunk.draw(_screen, z_buffer, final_matrix, daylight_multiplier)

        # self.draw_translucent()

    def update_daylight(self):
        if self.incrementer == -1:
            if self.daylight < 480:  # Moonlight of 4
                self.incrementer = 0
        elif self.incrementer == 1:
            if self.daylight >= 1800:
                self.incrementer = 0

        if self.time % 36000 == 0:
            self.incrementer = 1
        elif self.time % 36000 == 18000:
            self.incrementer = -1

        self.daylight += self.incrementer
    
    def build_pending_chunks(self):
        if self.chunk_building_queue:
            pending_chunk = self.chunk_building_queue.popleft()
            pending_chunk.update_mesh()

    def process_chunk_updates(self):
        for _chunk in self.visible_chunks:
            _chunk.process_chunk_updates()
    
    def tick(self, delta_time):
        self.chunk_update_counter = 0
        self.time += int(delta_time/(1/60))
        self.pending_chunk_update_count = sum(len(_chunk.chunk_update_queue) for _chunk in self.chunks.values())
        self.update_daylight()
        self.build_pending_chunks()
        self.process_chunk_updates()
