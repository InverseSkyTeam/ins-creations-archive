from block_model import BlockModel
from texture_manager import TextureManager
import numpy as np
import pygame
from chinese import chinese


cube_model = BlockModel('data/models/cube.obj')  # 方块通用模型


class BlockData:  # 存储单个方块的数据（如方块模型，纹理图片等）
    def __init__(self, texture_manager, name="unknown", block_face_textures=None, model=cube_model, font_nums=None):
        self.name = name
        self.block_face_textures = block_face_textures if block_face_textures is not None else {"all": "cobblestone"}
        self.model = model
        self.tex_indices = [0] * 6  # TODO: 目前只支持六面正方体
        self.tex_indices_triangle = np.zeros(6, dtype=np.uint32)
        self.upper_name = self.name.replace(" ", "_").upper()
        self.thumbnail = pygame.image.load(f'data/thumbnail/{chinese[self.upper_name]}.png').convert_alpha()
        self.font_nums = font_nums
        self.max_num = 64

        def set_block_face(_face, _texture_index):  # 设置面的纹理 index
            # 确保不添加不存在的面
            if _face > len(self.tex_indices) - 1:
                return
            self.tex_indices[_face] = _texture_index
            self.tex_indices_triangle[_face] = _texture_index

        for face in block_face_textures:
            texture = block_face_textures[face]
            texture_manager.add_texture(texture)

            texture_index = texture_manager.textures.index(texture)

            if face == "all":
                for i in range(len(self.tex_indices)):
                    set_block_face(i, texture_index)

            elif face == "sides":
                set_block_face(0, texture_index)
                set_block_face(1, texture_index)
                set_block_face(4, texture_index)
                set_block_face(5, texture_index)

            elif face == "x":
                set_block_face(0, texture_index)
                set_block_face(1, texture_index)

            elif face == "y":
                set_block_face(2, texture_index)
                set_block_face(3, texture_index)

            elif face == "z":
                set_block_face(4, texture_index)
                set_block_face(5, texture_index)

            else:
                set_block_face(["right", "left", "top", "bottom", "front", "back"].index(face), texture_index)

    def render(self, screen, rect, num):
        screen.blit(self.thumbnail, rect)
        if num == 1:
            return
        num_sf = self.font_nums[num]
        w, h = num_sf.get_size()
        num_x, num_y = rect.bottomright
        num_x += 1 - w
        num_y += 1 - h
        screen.blit(num_sf, (num_x, num_y))


class AllBlockData:
    def __init__(self):
        font = pygame.font.Font('data/unifont.otf', 17)
        font_nums = [font.render(str(i), True, (255,) * 3).convert_alpha() for i in range(65)]

        self.texture_manager = TextureManager(16, 16, 256)  # TODO: 32是最大贴图数
        self.all_block_data = [None]

        blocks_data_file = open("data/blocks_data.idu", encoding='utf-8')
        blocks_data = blocks_data_file.readlines()
        blocks_data_file.close()

        for block in blocks_data:
            if block[0] in ['\n', '#']:  # 跳过注释和空行
                continue

            number, props = block.split(':', 1)
            number = int(number)  # 方块编号

            # 默认方块

            name = "Unknown"
            model = cube_model
            texture = {"all": "unknown"}

            # 读取方块属性

            for prop in props.split(','):  # 不同的属性用逗号分隔
                prop = prop.strip()  # 去掉首尾空格
                prop = list(filter(None, prop.split(' ', 1)))  # 用空格分隔属性名和属性内容

                if prop[0] == "sameas":
                    sameas_number = int(prop[1])

                    name = self.all_block_data[sameas_number].name
                    texture = self.all_block_data[sameas_number].block_face_textures
                    model = self.all_block_data[sameas_number].model

                elif prop[0] == "name":
                    name = eval(prop[1])

                elif prop[0][:7] == "texture":
                    _, side = prop[0].split('.')
                    texture[side] = prop[1].strip()

            # 添加方块类型

            _block_data = BlockData(self.texture_manager, name, texture, model, font_nums)

            if number < len(self.all_block_data):
                self.all_block_data[number] = _block_data

            else:
                while len(self.all_block_data) - 1 < number - 1:
                    self.all_block_data.append(None)
                self.all_block_data.append(_block_data)

    def __getitem__(self, item):
        return self.all_block_data[item]
