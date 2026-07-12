import numpy as np
import pygame
from Surface3d import Surface3d


_vertex_positions = [
	[ 0.5,  0.5,  0.5,  0.5, -0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5], # right
	[-0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5,  0.5,  0.5], # left
	[ 0.5,  0.5,  0.5,  0.5,  0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5,  0.5], # top
	[-0.5, -0.5,  0.5, -0.5, -0.5, -0.5,  0.5, -0.5, -0.5,  0.5, -0.5,  0.5], # bottom
	[-0.5,  0.5,  0.5, -0.5, -0.5,  0.5,  0.5, -0.5,  0.5,  0.5,  0.5,  0.5], # front
	[ 0.5,  0.5, -0.5,  0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,  0.5, -0.5], # back
]


def merge_vertex(vertex_positions):
    vertices = np.array([
        [(face[i], face[i+1], face[i+2], 1) for i in range(0, len(face), 3)]
        for face in vertex_positions
    ], dtype=np.float64)

    return vertices


class TextureManager:
    def __init__(self):
        self.textures = []
        self.texture_array = []

    @staticmethod
    def load_texture_img(name):
        return Surface3d(pygame.image.load(name))

    def add_texture(self, texture):
        if texture not in self.textures:
            self.textures.append(texture)
            self.texture_array.append(self.load_texture_img(f"textures/{texture}.png"))


class BlockType:
    # 新的可选模型参数（默认为立方体模型）
    def __init__(self, texture_manager, block_face_textures):
        self.block_face_textures = block_face_textures
        
        self.vertex_positions = _vertex_positions
        self.vertices = merge_vertex(self.vertex_positions)
        self.tex_indices = [0] * 6

        def set_block_face(_face, _texture):
            # 确保不添加不存在的面
            if _face > 5:
                return
            self.tex_indices[_face] = _texture

        for face in block_face_textures:
            texture = block_face_textures[face]
            texture_manager.add_texture(texture)

            texture_index = texture_manager.textures.index(texture)

            if face == "all":
                for i in range(6):
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


class Block:
    def __init__(self, block_type, position):
        self.block_type: BlockType = block_type
        self.x, self.y, self.z = position
    
    def get_vertices(self):
        new_vertices = self.block_type.vertices.copy()
        new_vertices[:, :, 1] = -new_vertices[:, :, 1]
        new_vertices[:, :, 0] += self.x
        new_vertices[:, :, 1] += self.y
        new_vertices[:, :, 2] += self.z
        return new_vertices
