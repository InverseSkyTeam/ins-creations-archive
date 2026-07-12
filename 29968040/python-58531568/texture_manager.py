import numpy as np
from reanim_image import ReanimImage
from config import IMG_PATH


class NumpyList:
    def __init__(self, shape, dtype):
        self.data: np.ndarray = np.zeros(shape, dtype=dtype)
        self._len: int = 0

    def push_arr(self, data):
        s_index = self._len
        e_index = self._len + data.shape[0]
        self.data[s_index:e_index] = data.copy()
        self._len = e_index
        return s_index, e_index

    def push(self, data):
        index = self._len
        self.data[index] = data
        self._len += 1
        return index

    def get_data(self):
        return self.data


class TextureManager:
    def __init__(self):
        self.data = NumpyList(18000000, dtype=np.uint32)
        self.index = NumpyList(3000, dtype=np.uint32)
        self.size = NumpyList((3000, 2), dtype=np.uint16)
        self.texture: dict = {}
        
        self.reanim_image = ReanimImage(IMG_PATH)

    def load_texture(self, name):
        if name in self.texture:
            return self.texture[name]

        img = self.reanim_image.open(name)
        arr = np.array(img).swapaxes(0, 1).astype(np.uint32)
        _arr = (arr[:, :, 3] << 24) | (arr[:, :, 0] << 16) | (arr[:, :, 1] << 8) | arr[:, :, 2]
        s_index, e_index = self.data.push_arr(_arr.ravel())
        index, index1 = self.index.push(s_index), self.size.push(img.size)
        assert index == index1
        assert e_index - s_index == img.width * img.height
        self.texture[name] = index
        return index
