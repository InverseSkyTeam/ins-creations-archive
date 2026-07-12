import bs4
from texture_manager import TextureManager
from typing import List
import numpy as np
from config import REANIM_PATH
import math
import time


def calc_trans(kx, ky, sx, sy, x, y):
    deg = math.pi / 180
    degkx = deg * kx
    degky = deg * ky
    a = sx * math.cos(degkx)
    b = sx * math.sin(degkx)
    c = -sy * math.sin(degky)
    d = sy * math.cos(degky)
    return a, b, c, d, x, y


class Track:
    def __init__(self, name, data_length):
        self.name = name
        self.data: List[np.ndarray] = [None] * data_length
        # self.raw_data: List[str] = [None] * data_length


class ReanimFile:
    def __init__(self, path, texture_manager):
        with open(REANIM_PATH + path, 'r') as f:
            string = f.read()
        self.dom = bs4.BeautifulSoup(string.replace('\n', ''), 'lxml').body
        self.texture_manager: TextureManager = texture_manager

        self.fps = 0
        self.action = {}
        self.track: List[Track] = []

        a = time.time()
        self.parse()
        print(f'{path} 解析成功，用时 {time.time() - a}s')

    def parse(self):
        self.fps = float(self.dom.fps.string)
        for data in self.dom.contents[1:]:
            track_name = data.find('name').string  # 图层名称
            track_data = data.contents[1:]
            if data.find('i') is None and track_name.startswith('anim_'):  # 是用于表示动作起止帧特殊图层
                self.parse_index_track(track_name, track_data)
            elif data.find('i') is not None:  # 表示动画的图片图层
                self.parse_image_track(track_name, track_data)

        if not self.action:
            self.action['anim_idle'] = (0, len(self.track[0].data))

    def load_image(self, name):
        _name = name[len('IMAGE_REANIM_'):]
        return self.texture_manager.load_texture(_name)

    def parse_index_track(self, action_name, dom):  # 读取动画图层
        f = 0
        frame_f = [-1 for _ in range(len(dom) + 1)]
        for frame_index, anim in enumerate(dom):
            f = f if anim.f is None else int(anim.f.string)
            frame_f[frame_index] = f
        if 0 not in frame_f:
            return
        s = frame_f.index(0)
        e = frame_f.index(-1, s)
        self.action[action_name] = (s, e)  # 左闭右开，[s, e)

    def parse_image_track(self, track_name, dom):
        track = Track(track_name, len(dom))
        x, y, sx, sy, kx, ky, f, a, image = 0, 0, 1, 1, 0, 0, 0, 1, -1
        for frame_index, anim in enumerate(dom):
            x = x if anim.x is None else float(anim.x.string)
            y = y if anim.y is None else float(anim.y.string)
            sx = sx if anim.sx is None else float(anim.sx.string)
            sy = sy if anim.sy is None else float(anim.sy.string)
            kx = kx if anim.kx is None else float(anim.kx.string)
            ky = ky if anim.ky is None else float(anim.ky.string)
            f = f if anim.f is None else int(anim.f.string)
            a = a if anim.a is None else float(anim.a.string)
            image = image if anim.i is None else self.load_image(anim.i.string)
            track.data[frame_index] = np.array([a, *calc_trans(kx, ky, sx, sy, x, y), image, f], dtype=np.float64)
            # track.raw_data[frame_index] = str(anim)
        self.track.append(track)
