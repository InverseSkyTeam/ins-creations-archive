from collections import deque
import numpy as np
import subchunk
from render import WorldModel, render_cube

CHUNK_WIDTH = 16  # 区块宽
CHUNK_HEIGHT = 128  # 区块高
CHUNK_LENGTH = 16  # 区块长


class Chunk:
    def __init__(self, world, chunk_position, init_blocks=True):
        self.world = world
        
        self.modified = False
        self.chunk_position = chunk_position

        self.position = (
            self.chunk_position[0] * CHUNK_WIDTH,
            self.chunk_position[1] * CHUNK_HEIGHT,
            self.chunk_position[2] * CHUNK_LENGTH)

        if init_blocks:
            self.blocks = [[[0 for _ in range(CHUNK_LENGTH)]  # z
                            for _ in range(CHUNK_HEIGHT)]  # y
                           for _ in range(CHUNK_WIDTH)]  # x
        else:
            self.blocks = None
        # Numpy is really slow there
        self.lightmap = [[[0 for _ in range(CHUNK_LENGTH)]
                          for _ in range(CHUNK_HEIGHT)]
                         for _ in range(CHUNK_WIDTH)]  # 存储光照强度（八位二进制存储，前四位是太阳光，后四位是点光）
        
        self.subchunks = {}
        self.chunk_update_queue = deque()  # 当前区块更新队列
        
        for x in range(int(CHUNK_WIDTH / subchunk.SUBCHUNK_WIDTH)):
            for y in range(int(CHUNK_HEIGHT / subchunk.SUBCHUNK_HEIGHT)):
                for z in range(int(CHUNK_LENGTH / subchunk.SUBCHUNK_LENGTH)):
                    self.subchunks[(x, y, z)] = subchunk.Subchunk(self, (x, y, z))

        self.model = WorldModel(self.world.texture_manager)

    def get_block_light(self, x, y, z):  # 获取光照强度
        return self.lightmap[x][y][z] & 0xF  # 获取最后四位二进制

    def set_block_light(self, x, y, z, value):  # 设置光照强度
        self.lightmap[x][y][z] = (self.lightmap[x][y][z] & 0xF0) | value  # 清空原有的数据的后四位二进制，再加上光照强度

    def get_sky_light(self, x, y, z):  # 获取太阳光照强度
        return (self.lightmap[x][y][z] >> 4) & 0xF

    def set_sky_light(self, x, y, z, value):  # 设置太阳光照强度
        self.lightmap[x][y][z] = (self.lightmap[x][y][z] & 0xF) | (value << 4)

    def get_raw_light(self, x, y, z):  # 获取原始光照强度数据
        return self.lightmap[x][y][z]

    def get_block_number(self, position):  # 获取当前区块某个方块的编号
        lx, ly, lz = position  # 相对当前区块的坐标

        block_number = self.blocks[lx][ly][lz]
        return block_number

    def get_transparency(self, position):  # 获取方块透明属性
        block_type = self.world.block_types[self.get_block_number(position)]  # 方块类型

        if not block_type:  # 空气
            return 2
        
        return block_type.transparent

    def is_opaque_block(self, position):  # 方块是否不透明（空气也可看作透明方块）
        block_type = self.world.block_types[self.get_block_number(position)]
        
        if not block_type:  # 是空气
            return False
        
        return not block_type.transparent
    
    def update_subchunk_meshes(self):
        self.chunk_update_queue.clear()  # 清空队列
        for _subchunk in self.subchunks.values():
            self.chunk_update_queue.append(_subchunk)

    def update_at_position(self, position):  # 更新“子区块更新队列”
        x, y, z = position

        lx = int(x % subchunk.SUBCHUNK_WIDTH)
        ly = int(y % subchunk.SUBCHUNK_HEIGHT)
        lz = int(z % subchunk.SUBCHUNK_LENGTH)  # 位置在所在子区块中的相对位置

        clx, cly, clz = self.world.get_local_position(position)  # 位置在所在区块中的相对位置

        sx = clx // subchunk.SUBCHUNK_WIDTH  # 所在子区块的位置
        sy = cly // subchunk.SUBCHUNK_HEIGHT
        sz = clz // subchunk.SUBCHUNK_LENGTH

        if self.subchunks[(sx, sy, sz)] not in self.chunk_update_queue:
            self.chunk_update_queue.append(self.subchunks[(sx, sy, sz)])

        def try_update_subchunk_mesh(subchunk_position):  # 向队列添加要更新的子区块
            if subchunk_position in self.subchunks:  # 子区块已经在更新队列中
                if not self.subchunks[subchunk_position] in self.chunk_update_queue:
                    self.chunk_update_queue.append(self.subchunks[subchunk_position])

        # 分类讨论在子区块边缘的情况，此时需要对相邻的区块进行更新
        if lx == subchunk.SUBCHUNK_WIDTH - 1:
            try_update_subchunk_mesh((sx + 1, sy, sz))
        if lx == 0:
            try_update_subchunk_mesh((sx - 1, sy, sz))
        
        if ly == subchunk.SUBCHUNK_HEIGHT - 1:
            try_update_subchunk_mesh((sx, sy + 1, sz))
        if ly == 0:
            try_update_subchunk_mesh((sx, sy - 1, sz))

        if lz == subchunk.SUBCHUNK_LENGTH - 1:
            try_update_subchunk_mesh((sx, sy, sz + 1))
        if lz == 0:
            try_update_subchunk_mesh((sx, sy, sz - 1))

    def process_chunk_updates(self):  # 处理“子区块更新队列”中的子区块
        for i in range(self.world.options.CHUNK_UPDATES):
            if self.chunk_update_queue:
                _subchunk = self.chunk_update_queue.popleft()  # 弹出队首
                _subchunk.update_mesh()  # 更新子区块
                self.world.chunk_update_counter += 1  # 更新子区块数量增加
                if not self.chunk_update_queue:  # 队列已清空
                    self.world.chunk_building_queue.append(self)  # 当前区块更新完成，加入进世界区块更新队列
                    return

    def process_chunk_updates1(self):  # 处理 子区块更新队列 中的子区块
        while 1:
            if self.chunk_update_queue:
                _subchunk = self.chunk_update_queue.popleft()  # 弹出队首
                _subchunk.update_mesh()  # 更新子区块
                self.world.chunk_update_counter += 1  # 更新子区块数量增加
                if not self.chunk_update_queue:  # 队列已清空
                    self.world.chunk_building_queue.append(self)  # 当前区块更新完成，加入进世界区块更新队列
                    return

    def update_mesh(self):
        # 把所有子区块的网格合并成大的区块网格
        subchunk_vertices = []
        subchunk_indices = []
        subchunk_uv_index = []
        subchunk_lights = []
        subchunk_skylights = []
        subchunk_shading = []
        vertices_num = 0
        for _subchunk in self.subchunks.values():
            if len(_subchunk.indices) == 0:
                continue
            subchunk_vertices += _subchunk.vertices
            subchunk_indices.append(np.array(_subchunk.indices, dtype=np.uint32)+vertices_num)
            subchunk_uv_index += _subchunk.uv_index
            vertices_num += _subchunk.vertices_num
            subchunk_lights += _subchunk.lights
            subchunk_skylights += _subchunk.skylights
            subchunk_shading += _subchunk.shading

        self.model.vertices = np.concatenate(subchunk_vertices, axis=0)
        self.model.indices = np.concatenate(subchunk_indices, axis=0)
        self.model.uv_index = np.array(subchunk_uv_index, dtype=np.uint32)
        self.model.shading = np.array(subchunk_shading, dtype=np.float64)
        self.model.lights = np.array(subchunk_lights, dtype=np.float64) * self.model.shading
        self.model.lights_1_5 = np.minimum(self.model.lights * 1.5, self.model.shading)
        self.model.lights_1_25 = np.minimum(self.model.lights * 1.25, self.model.shading)
        self.model.skylights = np.array(subchunk_skylights, dtype=np.float64) * self.model.shading

        self.model.sort_indices = self.model.indices[:, 0]
        self.model.sort_indices_no_early_z = np.arange(self.model.indices.shape[0])

    def draw(self, screen, zbuffer, matrix, daylight_multiplier):
        if self.model.indices is None or not len(self.model.indices):
            return
        render_cube(self.model, screen, zbuffer, matrix, daylight_multiplier, self.world.options)
