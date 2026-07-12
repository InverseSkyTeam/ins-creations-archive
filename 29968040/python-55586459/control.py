import pygame
import math
import time
from collision import Collision
from ray import Ray
import numpy as np
from xes_api import get_my_id


class Control:
    def __init__(self, people_manager):
        self.exclusive = False  # 是否获得鼠标焦点
        self.prev_time = time.time()
        self.tx, self.ty, self.tz = 0, 7, -65
        self.angle_alpha, self.angle_beta = 0, 0
        self.is_attack = False
        self.uid = get_my_id()
        self.hp = 100
        self.start_time = time.time()

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

    def update_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.set_exclusive_mouse(True)
            if event.type == pygame.MOUSEMOTION and self.exclusive:
                self.angle_alpha += event.rel[0] * 0.2
                self.angle_beta += event.rel[1] * 0.3
                self.angle_beta = max(-90, min(self.angle_beta, 90))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.set_exclusive_mouse(False)
                if event.key == pygame.K_UP:
                    self.ty += 1
                if event.key == pygame.K_DOWN:
                    self.ty -= 1

    def update(self, events):
        curv_time = time.time()
        time_step = curv_time - self.prev_time
        self.prev_time = curv_time

        self.update_events(events)
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
        curv_time = str(int(round((time.time() - self.start_time) * 100)) % 2147483647)
        curv_time = '0' * (10-len(curv_time)) + curv_time
        pos = str(np.array([self.tx, self.tz], dtype=np.float16).view(np.uint32)[0])
        pos = '0' * (10 - len(pos)) + pos
        angle = str(np.array([self.angle_alpha], dtype=np.float16).view(np.uint16)[0])
        angle = '0' * (5 - len(angle)) + angle
        state = str(np.array([self.hp, self.is_attack], dtype=np.uint8).view(np.uint16)[0])
        state = '0' * (5 - len(state)) + state
        return pos + angle, curv_time + state, str(self.uid)

    def set_cloud_data(self, b):
        self.hp = np.array([int(b[10:])], dtype=np.uint16).view(np.uint8)[0]
