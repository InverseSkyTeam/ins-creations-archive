from model import Model
import numpy as np
from model import read_img
from matrix import calc_transform_matrix
from speedup import generate_faces
import math
import pygame
import time
from xes_api import get_user_name


class People:
    def __init__(self, player):
        self.player = player
        self.tx, self.ty, self.tz = 0, 7, -65
        self.angle_alpha, self.angle_beta = 0, 0
        self.is_attack = True
        self.uid = '0'
        self.hp = 100
        self.is_show = False
        self._name = ''
        self.offline = 100
        self.last_value = '0'

        self.send_hp = False
        self.start_time = time.time()

        self.model = Model('data/people/people.obj', 'data/people/0.png', scale=1.6)
        self.name_model = Model('data/people/name.obj', 'data/people/0.png')
        self.name_texture = self.name_model.texture_array
        self.font = pygame.font.SysFont('Simhei', 15)
        self.normal_texture = {}
        self.attack_texture = {}
        self.direction = np.array((-180, -135, -90, -45, 0, 45, 90, 135, 180), dtype=np.int32)
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
        sf = pygame.Surface((80, 20))
        sf.fill((150,) * 3)
        text = self.font.render(name, True, (20, 20, 20))
        sf.blit(text, text.get_rect(center=(40, 10)))
        self.name_texture = pygame.surfarray.array2d(sf.convert()).T.copy(order='C')

    def get_name(self):
        return self._name

    def get_cloud_data(self):
        curv_time = str(int(round((time.time() - self.start_time) * 100)) % 2147483647)
        curv_time = '0' * (10-len(curv_time)) + curv_time
        state = str(np.array([self.hp, self.is_attack], dtype=np.uint8).view(np.uint16)[0])
        state = '0' * (5 - len(state)) + state
        return curv_time + state

    def set_cloud_data(self, a, b, c):
        if c != self.uid:
            self.uid = c
            self.set_name(get_user_name(c))
        if self.uid == '0':
            return
        a = (15-len(a)) * '0' + a
        b = (15-len(b)) * '0' + b
        self.tx, self.tz = np.array([int(a[:10])], dtype=np.uint32).view(np.float16).tolist()
        self.angle_alpha = np.array([int(a[10:])], dtype=np.uint16).view(np.float16)[0]
        self.hp, self.is_attack = np.array([int(b[10:])], dtype=np.uint16).view(np.uint8).tolist()
        # self.last_value = b

    def render(self, screen, z_buffer, my_tx, my_tz, scene_matrix):
        if self.hp <= 0 or not self.is_show:
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

        trans_mat = calc_transform_matrix(-new_angle + 180, 0, self.tx, -self.ty-1.5, self.tz)
        final_matrix = np.dot(scene_matrix, trans_mat).T
        pts_name = np.matmul(self.name_model.vertices, final_matrix)
        generate_faces(
            screen, self.name_model.indices, self.name_model.uv_indices, pts_name,
            self.name_model.uv_vertices, self.name_texture, z_buffer
        )  # 逐个绘制三角形
