from util import *
from functools import lru_cache as cache

SUBCHUNK_WIDTH = 4  # 子块宽
SUBCHUNK_HEIGHT = 4  # 子块高
SUBCHUNK_LENGTH = 4  # 子块长


@cache(maxsize=None)
def smooth(a, b, c, d):
    if not a or not b or not c or not d:
        min_val = a
        if b:
            min_val = min(min_val, b)
        if c:
            min_val = min(min_val, c)
        if d:
            min_val = min(min_val, d)
        a = max(a, min_val)
        b = max(b, min_val)
        c = max(c, min_val)
        d = max(d, min_val)
    return (a + b + c + d) / 4


@cache(maxsize=None)
def ao(s1, s2, c):
    if s1 and s2:
        return 0.25
    return 1 - (s1 + s2 + c) / 4


def get_neighbour_voxels(npos, face):
    if face == 0:  # EAST
        neighbours = [
            (npos[0]+UP_SOUTH[0], npos[1]+UP_SOUTH[1], npos[2]+UP_SOUTH[2]),   (npos[0]+UP[0], npos[1]+UP[1], npos[2]+UP[2]),   (npos[0]+UP_NORTH[0], npos[1]+UP_NORTH[1], npos[2]+UP_NORTH[2]),
            (npos[0]+SOUTH[0], npos[1]+SOUTH[1], npos[2]+SOUTH[2]),                   (npos[0]+NORTH[0], npos[1]+NORTH[1], npos[2]+NORTH[2]),
            (npos[0]+DOWN_SOUTH[0], npos[1]+DOWN_SOUTH[1], npos[2]+DOWN_SOUTH[2]), (npos[0]+DOWN[0], npos[1]+DOWN[1], npos[2]+DOWN[2]), (npos[0]+DOWN_NORTH[0], npos[1]+DOWN_NORTH[1], npos[2]+DOWN_NORTH[2])
        ]
    elif face == 1:  # WEST
        neighbours = [
            (npos[0]+UP_NORTH[0], npos[1]+UP_NORTH[1], npos[2]+UP_NORTH[2]),   (npos[0]+UP[0], npos[1]+UP[1], npos[2]+UP[2]),   (npos[0]+UP_SOUTH[0], npos[1]+UP_SOUTH[1], npos[2]+UP_SOUTH[2]),
            (npos[0]+NORTH[0], npos[1]+NORTH[1], npos[2]+NORTH[2]),                   (npos[0]+SOUTH[0], npos[1]+SOUTH[1], npos[2]+SOUTH[2]),
            (npos[0]+DOWN_NORTH[0], npos[1]+DOWN_NORTH[1], npos[2]+DOWN_NORTH[2]), (npos[0]+DOWN[0], npos[1]+DOWN[1], npos[2]+DOWN[2]), (npos[0]+DOWN_SOUTH[0], npos[1]+DOWN_SOUTH[1], npos[2]+DOWN_SOUTH[2])
        ]
    elif face == 2:  # UP
        neighbours = [
            (npos[0]+SOUTH_EAST[0], npos[1]+SOUTH_EAST[1], npos[2]+SOUTH_EAST[2]), (npos[0]+SOUTH[0], npos[1]+SOUTH[1], npos[2]+SOUTH[2]), (npos[0]+SOUTH_WEST[0], npos[1]+SOUTH_WEST[1], npos[2]+SOUTH_WEST[2]),
            (npos[0]+EAST[0], npos[1]+EAST[1], npos[2]+EAST[2]),                     (npos[0]+WEST[0], npos[1]+WEST[1], npos[2]+WEST[2]),
            (npos[0]+NORTH_EAST[0], npos[1]+NORTH_EAST[1], npos[2]+NORTH_EAST[2]), (npos[0]+NORTH[0], npos[1]+NORTH[1], npos[2]+NORTH[2]), (npos[0]+NORTH_WEST[0], npos[1]+NORTH_WEST[1], npos[2]+NORTH_WEST[2])
        ]
    elif face == 3:  # DOWN
        neighbours = [
            (npos[0]+SOUTH_WEST[0], npos[1]+SOUTH_WEST[1], npos[2]+SOUTH_WEST[2]), (npos[0]+SOUTH[0], npos[1]+SOUTH[1], npos[2]+SOUTH[2]), (npos[0]+SOUTH_EAST[0], npos[1]+SOUTH_EAST[1], npos[2]+SOUTH_EAST[2]),
            (npos[0]+WEST[0], npos[1]+WEST[1], npos[2]+WEST[2]),                     (npos[0]+EAST[0], npos[1]+EAST[1], npos[2]+EAST[2]),
            (npos[0]+NORTH_WEST[0], npos[1]+NORTH_WEST[1], npos[2]+NORTH_WEST[2]), (npos[0]+NORTH[0], npos[1]+NORTH[1], npos[2]+NORTH[2]), (npos[0]+NORTH_EAST[0], npos[1]+NORTH_EAST[1], npos[2]+NORTH_EAST[2])
        ]
    elif face == 4:
        neighbours = [
            (npos[0]+UP_WEST[0],   npos[1]+UP_WEST[1],   npos[2]+UP_WEST[2]),   (npos[0]+UP[0],   npos[1]+UP[1],   npos[2]+UP[2]),   (npos[0]+UP_EAST[0],   npos[1]+UP_EAST[1],   npos[2]+UP_EAST[2]),
            (npos[0]+WEST[0],      npos[1]+WEST[1],      npos[2]+WEST[2]), (npos[0]+EAST[0], npos[1]+EAST[1], npos[2]+EAST[2]),
            (npos[0]+DOWN_WEST[0], npos[1]+DOWN_WEST[1], npos[2]+DOWN_WEST[2]), (npos[0]+DOWN[0], npos[1]+DOWN[1], npos[2]+DOWN[2]), (npos[0]+DOWN_EAST[0], npos[1]+DOWN_EAST[1], npos[2]+DOWN_EAST[2])
        ]
    elif face == 5:
        neighbours = [
            (npos[0]+UP_EAST[0], npos[1]+UP_EAST[1], npos[2]+UP_EAST[2]),   (npos[0]+UP[0], npos[1]+UP[1], npos[2]+UP[2]),   (npos[0]+UP_WEST[0], npos[1]+UP_WEST[1], npos[2]+UP_WEST[2]),
            (npos[0]+EAST[0], npos[1]+EAST[1], npos[2]+EAST[2]),                   (npos[0]+WEST[0], npos[1]+WEST[1], npos[2]+WEST[2]),
            (npos[0]+DOWN_EAST[0], npos[1]+DOWN_EAST[1], npos[2]+DOWN_EAST[2]), (npos[0]+DOWN[0], npos[1]+DOWN[1], npos[2]+DOWN[2]), (npos[0]+DOWN_WEST[0], npos[1]+DOWN_WEST[1], npos[2]+DOWN_WEST[2])
        ]
    else:
        return []
    return neighbours


def get_face_ao(s1, s2, s3,
                s4,     s5,
                s6, s7, s8):
    vertex1 = ao(s2, s4, s1)
    vertex2 = ao(s4, s7, s6)
    vertex3 = ao(s5, s7, s8)
    vertex4 = ao(s2, s5, s3)
    return vertex1, vertex2, vertex3, vertex4


def get_smooth_face_light(light, light1, light2, light3,
                                 light4,         light5,
                                 light6, light7, light8):
    vertex1 = smooth(light, light2, light4, light1)
    vertex2 = smooth(light, light4, light7, light6)
    vertex3 = smooth(light, light5, light7, light8)
    vertex4 = smooth(light, light2, light5, light3)
    return 0.8**(15.0-vertex1), 0.8**(15.0-vertex2), 0.8**(15.0-vertex3), 0.8**(15.0-vertex4)


class Subchunk:
    def __init__(self, parent, subchunk_position):
        self.parent = parent
        self.world = self.parent.world

        self.subchunk_position = subchunk_position

        self.local_position = (
            self.subchunk_position[0] * SUBCHUNK_WIDTH,
            self.subchunk_position[1] * SUBCHUNK_HEIGHT,
            self.subchunk_position[2] * SUBCHUNK_LENGTH)  # 相对于当前区块的位置

        self.position = (
            self.parent.position[0] + self.local_position[0],
            self.parent.position[1] + self.local_position[1],
            self.parent.position[2] + self.local_position[2])  # 在世界中的位置

        # mesh variables
        self.vertices = []
        self.indices = []
        self.uv_index = []
        self.lights = []
        self.skylights = []
        self.shading = []
        self.vertices_num = 0

    def get_raw_light(self, pos, npos):
        if not npos:  # 当前 block 不是方块时，用当前位置的光照
            light_levels = self.world.get_light(pos)
        else:  # 当前 block 是方块时，有相邻方块坐标，用相邻坐标位置的光照
            light_levels = self.world.get_light(npos)
        return [light_levels] * 4  # 复制四次是因为每个面有四个角

    def get_raw_skylight(self, pos, npos):
        if not npos:  # 当前 block 不是方块时，用当前位置的太阳光照强度
            light_levels = self.world.get_skylight(pos)
        else:  # 否则用相邻位置的太阳光照强度
            light_levels = self.world.get_skylight(npos)
        return [light_levels] * 4

    def get_light_smooth(self, npos, neighbours):
        nlights = (self.world.get_light(neighbour_pos) for neighbour_pos in neighbours)
        return get_smooth_face_light(self.world.get_light(npos), *nlights)

    def get_skylight_smooth(self, npos, neighbours):
        nlights = (self.world.get_skylight(neighbour_pos) for neighbour_pos in neighbours)
        return get_smooth_face_light(self.world.get_skylight(npos), *nlights)

    def get_ambient(self, block_type, face, neighbours):
        raw_shading = block_type.shading_values[face]
        neighbour_opacity = (self.world.is_opaque_block(neighbour_pos) for neighbour_pos in neighbours)
        face_ao = get_face_ao(*neighbour_opacity)
        return [a * b for a, b in zip(face_ao, raw_shading)]

    def add_face(self, face, block_type, npos):
        tex_index = block_type.tex_indices[face]

        if self.world.options.SMOOTH_LIGHTING:
            neighbours = get_neighbour_voxels(npos, face)
            shading = self.get_ambient(block_type, face, neighbours)
            lights = self.get_light_smooth(npos, neighbours)
            skylights = self.get_skylight_smooth(npos, neighbours)
        else:
            shading = block_type.shading_values[face]
            lights = [0.8**(15.0-self.world.get_light(npos))] * 4
            skylights = [0.8**(15.0-self.world.get_skylight(npos))] * 4

        indices = block_type.indices[face]
        self.indices.append(indices[[0, 1, 2]] + self.vertices_num)
        self.indices.append(indices[[0, 2, 3]] + self.vertices_num)
        self.uv_index.append(tex_index)

        self.lights.append([lights[0], lights[1], lights[2]])
        self.lights.append([lights[0], lights[2], lights[3]])

        self.skylights.append([skylights[0], skylights[1], skylights[2]])
        self.skylights.append([skylights[0], skylights[2], skylights[3]])

        self.shading.append([shading[0], shading[1], shading[2]])
        self.shading.append([shading[0], shading[2], shading[3]])

    def add_face_no_cube(self, face, block_type, lights, skylights):
        tex_index = block_type.tex_indices[face]
        shading = block_type.shading_values[face]

        indices = block_type.indices[face]
        self.indices.append(indices[[0, 1, 2]] + self.vertices_num)
        self.indices.append(indices[[0, 2, 3]] + self.vertices_num)
        self.uv_index.append(tex_index)

        self.lights.append([lights[0], lights[1], lights[2]])
        self.lights.append([lights[0], lights[2], lights[3]])

        self.skylights.append([skylights[0], skylights[1], skylights[2]])
        self.skylights.append([skylights[0], skylights[2], skylights[3]])

        self.shading.append([shading[0], shading[1], shading[2]])
        self.shading.append([shading[0], shading[2], shading[3]])

    def can_render_face(self, block_number, position):
        # block_number: 当前位置的 block 的编号
        # position: 当前遍历到的某个相邻的方块的位置
        # 逻辑：相邻方块不透明 或 当前方块和相邻方块均是玻璃 就不用绘制该面
        return not (
                self.world.is_opaque_block(position) or
                (self.world.block_glass[block_number] and self.world.get_block_number(position) == block_number)
        )

    def update_mesh(self):
        self.vertices = []
        self.indices = []
        self.uv_index = []
        self.lights = []
        self.skylights = []
        self.shading = []
        self.vertices_num = 0

        for local_x in range(SUBCHUNK_WIDTH):
            for local_y in range(SUBCHUNK_HEIGHT):
                for local_z in range(SUBCHUNK_LENGTH):
                    parent_lx = self.local_position[0] + local_x
                    parent_ly = self.local_position[1] + local_y
                    parent_lz = self.local_position[2] + local_z  # 在当前区块中的位置

                    block_number = self.parent.blocks[parent_lx][parent_ly][parent_lz]  # 当前位置的方块的类型

                    if block_number:  # 当前位置方块不是空气
                        block_type = self.world.block_types[block_number]  # 方块类型
                        if block_type.model.translucent:
                            continue

                        # 当前位置在世界中的位置
                        pos = (self.position[0] + local_x, self.position[1] + local_y, self.position[2] + local_z)
                        flag = False
                        if self.world.block_is_cube[block_number] and block_number not in self.world.light_blocks:  # 当前位置是方块且不是光源
                            for face, direction in enumerate(DIRECTIONS_TUPLE):  # 遍历相邻的六个不同的方向/六个面的法线
                                npos = (pos[0] + direction[0], pos[1] + direction[1], pos[2] + direction[2])  # 相邻面的新位置
                                if self.can_render_face(block_number, npos):
                                    flag = True
                                    self.add_face(face, block_type, npos)
                        elif block_type.slab:
                            flag = True
                            for face, direction in enumerate(DIRECTIONS_TUPLE):  # 遍历相邻的六个不同的方向/六个面的法线
                                npos = (pos[0] + direction[0], pos[1] + direction[1], pos[2] + direction[2])  # 相邻面的新位置
                                self.add_face(face, block_type, npos)
                        elif self.world.block_is_cube[block_number] and block_number in self.world.light_blocks:
                            flag = False
                            lights = [0.8**(15.0-self.parent.get_block_light(parent_lx, parent_ly, parent_lz))] * 4
                            skylights = [0.8**(15.0-self.parent.get_sky_light(parent_lx, parent_ly, parent_lz))] * 4
                            for face, direction in enumerate(DIRECTIONS_TUPLE):  # 遍历相邻的六个不同的方向/六个面的法线
                                npos = (pos[0] + direction[0], pos[1] + direction[1], pos[2] + direction[2])  # 相邻面的新位置
                                if self.can_render_face(block_number, npos):
                                    flag = True
                                    self.add_face_no_cube(face, block_type, lights, skylights)
                        else:
                            lights = [0.8**(15.0-self.parent.get_block_light(parent_lx, parent_ly, parent_lz))] * 4
                            skylights = [0.8**(15.0-self.parent.get_sky_light(parent_lx, parent_ly, parent_lz))] * 4
                            for i in range(len(block_type.vertex_positions)):
                                self.add_face_no_cube(i, block_type, lights, skylights)
                            flag = True

                        if flag:
                            x, y, z = pos
                            new_vertices = block_type.vertices.copy()
                            new_vertices[:, 0] += x
                            new_vertices[:, 1] += y
                            new_vertices[:, 2] += z
                            self.vertices.append(new_vertices)
                            self.vertices_num += len(block_type.vertices)
