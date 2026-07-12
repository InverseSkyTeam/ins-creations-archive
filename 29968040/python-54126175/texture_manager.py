import numpy as np
import pygame
from PIL import Image


class TextureManager:
    def __init__(self, texture_width, texture_height, max_textures):
        self.texture_width = texture_width
        self.texture_height = texture_height

        self.max_textures = max_textures

        self.textures = []

        # self.textures_sizes = np.zeros((self.max_textures, 2), dtype=np.uint32)
        self.texture_array = np.zeros((self.max_textures, self.texture_height, self.texture_width), dtype=np.uint32)
        self.texture_array_focused = np.zeros((self.max_textures, self.texture_height, self.texture_width), dtype=np.uint32)

    @staticmethod
    def load_texture_img(name):
        pic = pygame.image.load(name).convert().copy()
        pic_arr = pygame.surfarray.pixels2d(pic).copy()
        mask = np.array(Image.open(name).convert('RGBA'))[:, :, 3] == 0
        res = np.copy(pic_arr.swapaxes(0, 1), order='C')
        res[mask] = 0x1000000
        return res

    def add_texture(self, texture):
        if texture not in self.textures:
            self.textures.append(texture)
            texture_index = len(self.textures) - 1
            texture_arr = self.load_texture_img(f"textures/{texture}.png")
            texture_width, texture_height = texture_arr.shape[1], texture_arr.shape[0]
            # self.textures_sizes[texture_index, :] = texture_width, texture_height
            self.texture_array[texture_index, :texture_height, :texture_width] = texture_arr[:, :]
            self.texture_array_focused[texture_index, 1:texture_height-1, 1:texture_width-1] = texture_arr[1:-1, 1:-1]
