from PIL import Image
import os


class ReanimImage:  # 一个不区分大小写的图片读取
    def __init__(self, path_list):
        self.file_path = []
        self.file_lower_name = {}
        self.file_suffix = []

        _index = 0
        for _path in path_list:
            _files = os.listdir(_path)
            for _file in _files:
                if '.' not in _file:
                    continue
                file_name, suffix = _file.rsplit(".", 1)
                if suffix not in ('png', 'jpg'):
                    continue
                self.file_path.append(_path + _file)
                self.file_suffix.append(suffix.lower())
                self.file_lower_name[file_name.lower()] = _index
                _index += 1

    def search(self, file_name):
        if file_name.lower() in self.file_lower_name:
            return self.file_lower_name[file_name.lower()]
        return None

    def open(self, name):
        index: int = self.search(name)
        index_mask: int = self.search(name + '_')
        if index is None:
            raise FileNotFoundError(name + '未找到')
        if self.file_suffix[index] == 'png' or index_mask is None:
            # 是 png 或者是 jpg 但无蒙版
            return Image.open(self.file_path[index]).convert('RGBA')

        raw_img = Image.open(self.file_path[index]).convert('RGBA')
        mask_img = Image.open(self.file_path[index_mask]).convert('L')
        new_img = Image.new('RGBA', raw_img.size)
        new_img.paste(raw_img, (0, 0), mask=mask_img)
        return new_img
