from speedup import *
import pygame
import pygame.gfxdraw
import numpy as np
from model import Model
from matrix import calc_matrix
from config import Config
import math
from util import clampLng
from functools import lru_cache as cache


class BgImage:
    def __init__(self):
        self.bg = pygame.image.load('css_globe_bg.jpg').convert()
        self.bg_width, self.bg_height = self.bg.get_size()
        self.storage = {}

    @cache(maxsize=32)
    def get_img(self, new_w, new_h):
        return pygame.transform.smoothscale(self.bg, (new_w, new_h))
        # if (new_w, new_h) not in self.storage:
        #     self.storage[(new_w, new_h)] = pygame.transform.smoothscale(self.bg, (new_w, new_h))
        # return self.storage[(new_w, new_h)]
    
    def render(self, screen, w, h):
        ratio_bg = 1 + math.pow(Config.zoom, 3) * 0.3
        scale = max(w / self.bg_width, h / self.bg_height)
        new_bg_width = int(self.bg_width * scale * ratio_bg)
        new_bg_height = int(self.bg_height * scale * ratio_bg)
        new_bg = self.get_img(new_bg_width, new_bg_height)
        screen.blit(new_bg, new_bg.get_rect(center=(w//2, h//2)))


class HaloImage:
    def __init__(self):
        self.img = pygame.image.load('css_globe_halo.png').convert_alpha()
        self.storage = {}

    @cache(maxsize=32)
    def get_img(self, new_w, new_h):
        return pygame.transform.smoothscale(self.img, (new_w, new_h)).convert_alpha()
        # if (new_w, new_h) not in self.storage:
        #     self.storage[(new_w, new_h)] = pygame.transform.smoothscale(self.img, (new_w, new_h)).convert_alpha()
        # return self.storage[(new_w, new_h)]
    
    def render(self, screen, w, h, ratio):
        halo = self.get_img(int(730 * ratio), int(715 * ratio))
        _x, _y = int(w/2-368*ratio), int(h/2-350*ratio)
        screen.blit(halo, (_x, _y))


class Render:
    def __init__(self):
        self.pixelExpandOffset = 1.5
        self.bg = BgImage()
        self.halo = HaloImage()
        
        self.model = Model(texture='css_globe_diffuse.jpg')
    
    def render_3d(self, screen, w, h, ratio):
        r_x = -Config.lat / 180 * math.pi
        r_y = (clampLng(Config.lng) - 270 + 180) / 180 * math.pi
        # 绘制 3d 模型
        z_buffer = np.full((w, h), np.inf, dtype=np.float64)
        final_matrix = calc_matrix(w, h, r_x+1e-13, r_y+1e-13, ratio)
        pts = np.matmul(self.model.vertices, final_matrix)  # 存储屏幕坐标
        generate_faces_new(
            pygame.surfarray.pixels2d(screen), self.model.indices, self.model.indices,
            pts, self.model.uv_vertices, self.model.texture_array, z_buffer
        )  # 逐个绘制三角形
    
    def render(self, screen, w, h):
        ratio = math.pow(Config.zoom, 1.5)
        self.pixelExpandOffset = 1.5 + ratio * -1.25
        ratio = 1 + ratio * 3
        
        self.bg.render(screen, w, h)
        if Config.isPoleVisible:
            pygame.draw.circle(screen, (255,) * 3, (w // 2, h // 2), int(530 * ratio / 2), width=0)
        self.render_3d(screen, w, h, ratio)
        if Config.isHaloVisible:
            self.halo.render(screen, w, h, ratio)
