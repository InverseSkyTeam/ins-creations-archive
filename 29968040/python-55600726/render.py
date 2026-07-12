import numpy as np
import pygame
from matrix import calc_matrix
from speedup import generate_faces
from model import Model
from functools import lru_cache as cache
import time


class WeaponNormal:
    def __init__(self):
        self.img = pygame.image.load('data/weapon/tag-weapon.png')

    @cache(maxsize=32)
    def get_img(self, w, h):
        return pygame.transform.scale(self.img, (w, h)).convert_alpha()

    def render(self, screen, w, h):
        if abs(w / 480) > abs(h / 360):
            scale = 2 * w / 480
        else:
            scale = 2 * h / 360
        weapon_w, weapon_h = self.img.get_size()
        img = self.get_img(int(weapon_w * scale), int(weapon_h * scale))
        screen.blit(img, img.get_rect(bottomright=(w - 20 * scale, h + 30 * scale)))


class WeaponAttack:
    def __init__(self):
        self.img = pygame.image.load('data/weapon/tag-weapon2.png')

    @cache(maxsize=32)
    def get_img(self, w, h):
        return pygame.transform.scale(self.img, (w, h)).convert_alpha()

    def render(self, screen, w, h):
        if abs(w / 480) > abs(h / 360):
            scale = 2 * w / 480
        else:
            scale = 2 * h / 360
        weapon_w, weapon_h = self.img.get_size()
        img = self.get_img(int(weapon_w * scale), int(weapon_h * scale))
        screen.blit(img, img.get_rect(bottomright=(w - 20 * scale, h + 30 * scale)))


class Render:
    def __init__(self, people_manager, control):
        self.model = Model('data/scene/scene.obj', 'data/scene/texture.png')

        self.crosshair = pygame.image.load('data/weapon/crosshair.png')
        self.crosshair = pygame.transform.smoothscale(self.crosshair, (20, 20)).convert_alpha()

        self.font = pygame.font.SysFont('Arial', 20)
        self.font_ch = pygame.font.SysFont('SimHei', 15)

        self.weapon_normal = WeaponNormal()
        self.weapon_attack = WeaponAttack()
        self.people_manager = people_manager
        self.control = control

    def render3d(self, screen, w, h):
        _screen = pygame.surfarray.pixels2d(screen)
        z_buffer = np.full((w, h), np.inf, dtype=np.float64)
        final_matrix = calc_matrix(w, h, self.control.angle_alpha, self.control.angle_beta,
                                   self.control.tx, self.control.ty, self.control.tz)
        pts = np.matmul(self.model.vertices, final_matrix.T)  # 存储屏幕坐标
        generate_faces(
            _screen, self.model.indices, self.model.uv_indices,
            pts, self.model.uv_vertices, self.model.texture_array, z_buffer
        )  # 逐个绘制三角形
        for people in self.people_manager.peoples:
            people.render(_screen, z_buffer, self.control.tx, self.control.tz, final_matrix)
        del z_buffer

    def render2d(self, screen, w, h):
        screen.blit(self.crosshair, self.crosshair.get_rect(center=(w//2, h//2)))
        if not self.control.is_attack:
            self.weapon_normal.render(screen, w, h)
        else:
            self.weapon_attack.render(screen, w, h)
            sf1 = pygame.Surface((w, h), pygame.SRCALPHA)
            pygame.draw.rect(sf1, (0x99, 0xff, 0xff, int(255*0.1)), sf1.get_rect())
            screen.blit(sf1.convert_alpha(), (0, 0))

    def render_ui(self, screen, w, h):
        hp_txt = self.font.render(f'HP: {self.control.hp}', True, (255, 0, 0))
        screen.blit(hp_txt, (10, 10))
        players_txt = self.font_ch.render(f'在线人数: {self.control.total_players}', True, (255, 0, 0))
        screen.blit(players_txt, (10, 40))

        if time.time() - self.control.last_update_hp_time < 0.1:
            sf = pygame.Surface((w, h), pygame.SRCALPHA)
            pygame.draw.rect(sf, (255, 0, 0, int(255 * 0.2)), (0, 0, w, h))
            screen.blit(sf, (0, 0))
        if self.control.hp <= 0:
            screen.fill((0, ) * 3)
            txt = pygame.font.SysFont('Arial', 40).render('You die!', True, (255, 0, 0))
            screen.blit(txt, txt.get_rect(center=(w//2, h//2)))
