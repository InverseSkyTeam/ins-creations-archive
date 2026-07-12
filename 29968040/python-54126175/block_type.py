import collider
import models.cube  # 默认模型
import numpy as np


def gl_vertex_positions_to_obj(vertex_positions):
    # 把 opengl 格式的顶点转成 obj 格式的顶点
    vertices = []
    indices = []

    for face in vertex_positions:
        indices.append([])
        for _point in range(0, len(face), 3):
            x, y, z = face[_point:_point + 3]
            point = [x, y, z, 1]
            if point in vertices:
                pass
            else:
                vertices.append(point)
            indices[-1].append(vertices.index(point))

    vertices = np.array(vertices, dtype=np.float64)
    indices = np.array(indices, dtype=np.uint32)

    return vertices, indices


class Block_type:
    # 新的可选模型参数（默认为立方体模型）
    def __init__(self, texture_manager, name="unknown", block_face_textures=None, model=models.cube):
        self.name = name
        self.block_face_textures = block_face_textures if block_face_textures is not None else {"all": "cobblestone"}
        self.model = model

        # 根据模型属性创建成员

        self.transparent = model.transparent
        self.is_cube = model.is_cube
        self.glass = model.glass
        self.translucent = model.translucent

        # 创建碰撞箱

        self.colliders = []

        for _collider in model.colliders:
            self.colliders.append(collider.Collider(*_collider))

        # 用模型特定数据替换numbers.py中包含的数据

        self.vertex_positions = model.vertex_positions
        self.vertices, self.indices = gl_vertex_positions_to_obj(self.vertex_positions)
        self.tex_coords = model.tex_coords  # 废弃
        self.tex_indices = np.zeros(len(self.tex_coords), dtype=np.uint32)  # 用 np 数组存储
        self.shading_values = model.shading_values
        self.slab = False
        if name == 'Slab' or 'stairs' in name.lower():
            self.slab = True

        def set_block_face(_face, _texture):
            # 确保不添加不存在的面
            if _face > len(self.tex_coords) - 1:
                return
            self.tex_indices[_face] = _texture

        for face in block_face_textures:
            texture = block_face_textures[face]
            texture_manager.add_texture(texture)

            texture_index = texture_manager.textures.index(texture)

            if face == "all":
                for i in range(len(self.tex_coords)):
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
