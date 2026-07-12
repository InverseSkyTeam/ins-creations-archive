from model import Model
import numpy as np
from model import read_img
from matrix import calc_transform_matrix
from speedup import generate_faces
import math
import pygame
import time
from xes_api import get_user_name
from util import int_to_str


class People:
    def __init__(self, player):
        self.player = player
        self.tx, self.ty, self.tz = 0, 7, -65
        self.angle_alpha, self.angle_beta = 0, 0
        self.is_attack = True
        self.uid = '0'
        self.hp = 100
        self.die = False
        self.is_show = False
        self._name = ''
        self.offline = 5
        self.last_value = '0'

        self.send_hp = False

        self.model = Model('data/people/people.obj', 'data/people/0.png', scale=1.6)
        self.name_model = Model('data/people/name.obj', 'data/people/0.png')
        self.name_texture = self.name_model.texture_array
        self.font = pygame.font.SysFont('Simhei', 15)
        self.font1 = pygame.font.SysFont('Arial', 15)

        self.normal_texture = {}
        self.attack_texture = {}
        self.direction = np.array((-180, -135, -90, -45, 0, 45, 90, 135, 180), dtype=np.int32)
        self.init_texture()

    def init_texture(self):
        for i in (0, 45, 90, 135, 180):
            normal_img = read_img(f'data/people/normal_{i}.png')
            attack_img = read_img(f'data/people/attack_{i}.png')
            self.normal_texture[int(-i)] = np.array(normal_img)
            self.normal_texture[int(+i)] = np.fliplr(np.array(normal_img)).copy(order='C')
            self.attack_texture[int(-i)] = np.array(attack_img)
            self.attack_texture[int(+i)] = np.fliplr(np.array(attack_img)).copy(order='C')

    def get_angle(self, x1, y1):
        x2, y2 = self.tx, self.tz
        if y1 - y2 == 0:
            return -90 if x2 < x1 else 90
        if x1 - x2 == 0:
            return 0 if y2 > y1 else 180
        k = (y1 - y2) / (x1 - x2)
        res = 90 - math.degrees(math.atan(k))
        return res if x2 > x1 else res + 180

    def get_img(self, angle):
        angle = ((int(angle) + 180) % 360) - 180  # 缩放到 -180 - 180
        new_angle = self.direction[np.argmin(np.abs(self.direction - angle))]
        if self.is_attack:
            return self.attack_texture[int(new_angle)]
        return self.normal_texture[int(new_angle)]

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_cloud_data(self, a, b):
        a = '0' * (15 - len(a)) + a
        b = '0' * (15 - len(b)) + b

        is_attack, hp, uid = b[0], b[1: 5], b[5:]
        uid = str(int(uid))
        if int(self.uid) != int(uid):
            self.uid = uid
            self.set_name(get_user_name(uid))
        if self.uid == '0' or self.uid == 0:
            return
        self.is_attack = bool(int(is_attack))
        self.hp = int(hp)
        if self.hp <= 0:
            self.die = True
        else:
            self.die = False
        self.set_name_texture()

        self.tx, self.tz = np.array([int(a[:10])], dtype=np.uint32).view(np.float16).tolist()
        self.angle_alpha = np.array([int(a[10:])], dtype=np.uint16).view(np.float16)[0]

    def set_name_texture(self):
        sf = pygame.Surface((80, 40))
        sf.fill((150,) * 3)
        text = self.font.render(self.get_name(), True, (20, 20, 20))
        text1 = self.font1.render(f'HP: {self.hp}', True, (255, 0, 0))
        sf.blit(text, text.get_rect(center=(40, 10)))
        sf.blit(text1, text1.get_rect(center=(40, 30)))
        self.name_texture = pygame.surfarray.array2d(sf.convert()).T.copy(order='C')

    def get_cloud_data(self):
        time_stamp = str(int(round(time.time() * 100)))

        pos = int_to_str(np.array([self.tx, self.tz], dtype=np.float16).view(np.uint32)[0], 10)
        angle = int_to_str(np.array([self.angle_alpha], dtype=np.float16).view(np.uint16)[0], 5)

        uid = int_to_str(self.uid, 10)
        hp = int_to_str(self.hp, 4)
        is_attack = str(int(self.is_attack))
        return pos + angle, is_attack + hp + uid, time_stamp

    def render(self, screen, z_buffer, my_tx, my_tz, scene_matrix):
        if self.die or not self.is_show:
            return
        if self.tx == my_tx and self.tz == my_tz:  # 都重合了，就不需要绘制了
            return
        new_angle = self.get_angle(my_tx, my_tz)
        texture_array = self.get_img(self.angle_alpha - new_angle)
        trans_mat = calc_transform_matrix(-new_angle + 180, 0, self.tx, -self.ty+3.3, self.tz)
        final_matrix = np.dot(scene_matrix, trans_mat).T

        pts = np.matmul(self.model.vertices, final_matrix)  # 存储屏幕坐标
        generate_faces(
            screen, self.model.indices, self.model.uv_indices, pts,
            self.model.uv_vertices, texture_array, z_buffer
        )  # 逐个绘制三角形

        trans_mat = calc_transform_matrix(-new_angle + 180, 0, self.tx, -self.ty-2, self.tz)
        final_matrix = np.dot(scene_matrix, trans_mat).T
        pts_name = np.matmul(self.name_model.vertices, final_matrix)

        generate_faces(
            screen, self.name_model.indices, self.name_model.uv_indices, pts_name,
            self.name_model.uv_vertices, self.name_texture, z_buffer
        )  # 逐个绘制三角形
