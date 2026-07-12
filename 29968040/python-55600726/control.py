import pygame
import math
import time
from collision import Collision
from ray import Ray
import numpy as np
from xes_api import get_my_id
from util import get_spwan_pos, int_to_str
from random import randint


default_hp = 100


class Control:
    def __init__(self, people_manager):
        self.exclusive = False  # 是否获得鼠标焦点
        self.spwan = False
        self.prev_time = time.time()
        self.tx, self.ty, self.tz = get_spwan_pos()  # 0, 7, -65
        self.angle_alpha, self.angle_beta = 0, 0
        self.is_attack = False
        self.uid = get_my_id()
        self.hp = self.last_hp = default_hp
        self.mouse_down_time = time.time()
        self.die_time = 0
        self.last_update_hp_time = time.time()
        self.total_players = 0
        self.add_attack = False

        self.collision = Collision('data/scene/collision.txt')
        self.d = 3  # 玩家圆柱碰撞体半径
        self.target_fps = 30  # 在任意 fps 下玩家的移动总是以该 fps 的移动速度移动
        self.v_z = 0
        self.v_x = 0
        self.ray = Ray(self.collision)
        self.people_manager = people_manager

    def set_exclusive_mouse(self, exclusive):
        if self.exclusive == exclusive:
            return
        pygame.event.set_grab(exclusive)
        pygame.mouse.set_visible(not exclusive)
        self.exclusive = exclusive

    def update_events(self, events, skills):
        if pygame.mouse.get_pressed()[0] and self.hp > 0 and self.exclusive:
            if (time.time() - self.mouse_down_time) > 0.1:
                self.is_attack = not self.is_attack
                self.mouse_down_time = time.time()
        else:
            self.is_attack = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 0 and self.hp > 0 and self.exclusive:
                    self.mouse_down_time = time.time()
                self.set_exclusive_mouse(True)
            if event.type == pygame.MOUSEMOTION and self.exclusive:
                self.angle_alpha += event.rel[0] * 0.2
                self.angle_beta += event.rel[1] * 0.3
                self.angle_beta = max(-90, min(self.angle_beta, 90))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.set_exclusive_mouse(False)
                for skill in skills:
                    skill.on_key_down(event.key)
            if event.type == pygame.VIDEORESIZE:
                for skill in skills:
                    skill.on_resize(event.w, event.h)

    def update_hp(self, curv_time):
        if self.hp < self.last_hp:
            self.last_update_hp_time = curv_time
            self.last_hp = self.hp
            if self.hp == 0:
                self.die_time = curv_time
        if self.hp <= 0 and curv_time - self.die_time > 3:
            self.spwan = True

    def update(self, events, skills):
        curv_time = time.time()
        time_step = curv_time - self.prev_time
        self.prev_time = curv_time
        self.update_hp(curv_time)
        if self.hp <= 0:
            return

        self.update_events(events, skills)
        key_pressed = pygame.key.get_pressed()
        press_w = key_pressed[pygame.K_w]
        press_a = key_pressed[pygame.K_a]
        press_s = key_pressed[pygame.K_s]
        press_d = key_pressed[pygame.K_d]

        cos_alpha = math.cos(math.radians(self.angle_alpha))
        sin_alpha = math.sin(math.radians(self.angle_alpha))

        self.v_z += ((press_w - press_s) * 0.6 - self.v_z) * 0.5
        self.v_x += ((press_d - press_a) * 0.6 - self.v_x) * 0.5
        self.tx += (self.v_x * cos_alpha + self.v_z * sin_alpha) * self.target_fps * time_step
        self.tz += (self.v_z * cos_alpha - self.v_x * sin_alpha) * self.target_fps * time_step
        self.check_collision()
        self.ray.update_ray(self.angle_alpha, self.angle_beta)
        if self.is_attack:
            self.ray.ray_collision(self.tx, self.ty, self.tz, self.people_manager.peoples)

    def check_collision(self):
        d_x, d_z = 0, 0
        min_dist = 114514
        min_dx, min_dz = 0, 0
        is_hit = 0
        
        collision_pos = self.collision.collision_pos
        collision_n = self.collision.collision_n
        for collision_i in range(len(collision_pos)):
            _x = self.tx - collision_pos[collision_i][0]
            _z = self.tz - collision_pos[collision_i][1]
            _length = math.sqrt(_x * _x + _z * _z)
            if (collision_i + 1) % 2 == 1:
                boundary_x = collision_pos[collision_i+1][0] - collision_pos[collision_i][0]
                boundary_z = collision_pos[collision_i+1][1] - collision_pos[collision_i][1]
                if 0 < (_x * boundary_x + _z * boundary_z) < (boundary_x ** 2 + boundary_z ** 2):
                    _dist = _x * collision_n[collision_i] + _z * collision_n[collision_i+1]
                    if abs(_dist) < self.d:
                        is_hit = 1
                        d_x += _dist / abs(_dist) * (self.d - abs(_dist)) * collision_n[collision_i]
                        d_z += _dist / abs(_dist) * (self.d - abs(_dist)) * collision_n[collision_i+1]
            if _length < self.d and min_dist > _length:
                min_dist = _length
                min_dx = (self.d - _length) * (_x / _length)
                min_dz = (self.d - _length) * (_z / _length)

        d_x += (1 - is_hit) * min_dx
        d_z += (1 - is_hit) * min_dz
        self.tx += d_x
        self.tz += d_z

    def get_cloud_data(self):
        time_stamp = str(int(round(time.time() * 100)))

        pos = int_to_str(np.array([self.tx, self.tz], dtype=np.float16).view(np.uint32)[0], 10)
        angle = int_to_str(np.array([self.angle_alpha], dtype=np.float16).view(np.uint16)[0], 5)

        uid = int_to_str(self.uid, 10)
        hp = int_to_str(self.hp, 4)
        is_attack = str(int(self.is_attack))
        return pos + angle, is_attack + hp + uid, time_stamp

    def set_hp(self, b):
        b = '0' * (15 - len(b)) + b
        self.hp = int(b[1: 5])

    def start_spwan(self):
        self.spwan = False
        self.hp = self.last_hp = default_hp
        self.angle_alpha = 0
        self.tx, self.ty, self.tz = get_spwan_pos()  # 0, 7, -65

    def get_attack_hp(self):
        if self.add_attack:
            return randint(6, 12)
        else:
            return randint(3, 6)
