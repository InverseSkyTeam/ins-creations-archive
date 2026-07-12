import numpy as np
import pygame
from matrix import calc_matrix
from speedup import generate_faces
from model import Model
from functools import lru_cache as cache


class GunNormal:
    def __init__(self):
        self.gun = pygame.image.load('data/gun/tag-gun.png')

    @cache(maxsize=32)
    def get_img(self, w, h):
        return pygame.transform.scale(self.gun, (w, h)).convert_alpha()

    def render(self, screen, w, h):
        if abs(w / 480) > abs(h / 360):
            scale = 2 * w / 480
        else:
            scale = 2 * h / 360
        gun_w, gun_h = self.gun.get_size()
        img = self.get_img(int(gun_w * scale), int(gun_h * scale))
        screen.blit(img, img.get_rect(bottomright=(w - 20 * scale, h + 30 * scale)))


class GunAttack:
    def __init__(self):
        self.gun = pygame.image.load('data/gun/tag-gun2.png')

    @cache(maxsize=32)
    def get_img(self, w, h):
        return pygame.transform.scale(self.gun, (w, h)).convert_alpha()

    def render(self, screen, w, h):
        if abs(w / 480) > abs(h / 360):
            scale = 2 * w / 480
        else:
            scale = 2 * h / 360
        gun_w, gun_h = self.gun.get_size()
        img = self.get_img(int(gun_w * scale), int(gun_h * scale))
        screen.blit(img, img.get_rect(bottomright=(w - 20 * scale, h + 30 * scale)))


class Render:
    def __init__(self, people_manager):
        self.model = Model('data/scene/scene.obj', 'data/scene/texture.png')

        self.crosshair = pygame.image.load('data/gun/crosshair.png')
        self.crosshair = pygame.transform.smoothscale(self.crosshair, (20, 20)).convert_alpha()

        self.gun_normal = GunNormal()
        self.gun_attack = GunAttack()
        self.people_manager = people_manager

    def render3d(self, screen, w, h, angle_alpha, angle_beta, tx, ty, tz):
        _screen = pygame.surfarray.pixels2d(screen)
        z_buffer = np.full((w, h), np.inf, dtype=np.float64)
        final_matrix = calc_matrix(w, h, angle_alpha, angle_beta, tx, ty, tz)
        pts = np.matmul(self.model.vertices, final_matrix.T)  # 存储屏幕坐标
        generate_faces(
            _screen, self.model.indices, self.model.uv_indices,
            pts, self.model.uv_vertices, self.model.texture_array, z_buffer
        )  # 逐个绘制三角形
        for people in self.people_manager.peoples:
            people.render(_screen, z_buffer, tx, tz, final_matrix)

    def render2d(self, screen, w, h, is_attack):
        screen.blit(self.crosshair, self.crosshair.get_rect(center=(w//2, h//2)))
        if not is_attack:
            self.gun_normal.render(screen, w, h)
        else:
            self.gun_attack.render(screen, w, h)
