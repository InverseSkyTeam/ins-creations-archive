import numpy as np
from PIL import Image


class TextureManager:
    def __init__(self, texture_width, texture_height, max_textures):
        self.texture_width = texture_width
        self.texture_height = texture_height

        self.max_textures = max_textures

        self.textures = []

        self.texture_array = np.zeros((self.max_textures, self.texture_height, self.texture_width, 4), dtype=np.uint32)

    @staticmethod
    def load_texture_img(name):
        return np.array(Image.open(name).convert('RGBA'))

    def add_texture(self, texture):
        if texture not in self.textures:
            self.textures.append(texture)
            texture_index = len(self.textures) - 1
            texture_arr = self.load_texture_img(f"textures/{texture}.png")
            texture_width, texture_height = texture_arr.shape[1], texture_arr.shape[0]
            self.texture_array[texture_index, :texture_height, :texture_width] = texture_arr[:, :]
