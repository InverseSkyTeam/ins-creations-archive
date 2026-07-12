import pygame.math
import entity
from np_gl import *
from util import *
import numpy as np

WALKING_SPEED = 4.317
SPRINTING_SPEED = 7  # faster than in Minecraft, feels better


class Frustum:
    left = np.ones(4, dtype=np.float64)
    right = np.ones(4, dtype=np.float64)
    top = np.ones(4, dtype=np.float64)
    bottom = np.ones(4, dtype=np.float64)
    near = np.ones(4, dtype=np.float64)
    far = np.ones(4, dtype=np.float64)


class Player(entity.Entity):
    def __init__(self, world, width, height):
        super().__init__(world)

        self.view_width = width
        self.view_height = height

        # create matrices
        self.mvp_matrix_np = None
        self.mv_matrix_np = None
        self.p_matrix_np = None

        # camera variables
        self.eyelevel = self.height - 0.2
        self.input = [0, 0, 0]

        self.target_speed = WALKING_SPEED
        self.speed = self.target_speed

        self.interpolated_position = self.position
        self.rounded_position = self.position
        self.view_ray = np.ones(3, dtype=np.float64)

    def update(self, delta_time):
        # process input

        self.view_ray = np.array([np.cos(self.rotation[0]) * np.cos(self.rotation[1]),
                        np.sin(self.rotation[1]),
                        np.sin(self.rotation[0]) * np.cos(self.rotation[1])], dtype=np.float64)

        if delta_time * 20 > 1:
            self.speed = self.target_speed

        else:
            self.speed += (self.target_speed - self.speed) * delta_time * 20

        multiplier = self.speed * (1, 2)[self.flying]

        if self.flying and self.input[1]:
            self.accel[1] = self.input[1] * multiplier

        if self.input[0] or self.input[2]:
            angle = self.rotation[0] - math.atan2(self.input[2], self.input[0]) + math.tau / 4

            self.accel[0] = math.cos(angle) * multiplier
            self.accel[2] = math.sin(angle) * multiplier

        if not self.flying and self.input[1] > 0:
            self.jump()

        # process physics & collisions &c

        super().update(delta_time)

        self.rounded_position = [round(i) for i in self.position]
    
    def update_interpolation(self, delta_time):
        pos = np.array(self.position, dtype=np.float64)
        old_pos = np.array(self.old_position,dtype=np.float64)
        self.interpolated_position = pos * (1 - self.step) + old_pos * self.step
        self.step -= delta_time

    def update_frustum(self, mat):
        for i in range(4): 
            Frustum.left[i] = mat[3][i] + mat[0][i]
            Frustum.right[i] = mat[3][i] - mat[0][i]
            Frustum.bottom[i] = mat[3][i] + mat[1][i]
            Frustum.top[i] = mat[3][i] - mat[1][i]
            Frustum.near[i] = mat[3][i] + mat[2][i]
            Frustum.far[i] = mat[3][i] - mat[2][i]
            
        Frustum.left = normalize(Frustum.left)  # .tolist()
        Frustum.right = normalize(Frustum.right)  # .tolist()
        Frustum.bottom = normalize(Frustum.bottom)  # .tolist()
        Frustum.top = normalize(Frustum.top)  # .tolist()
        Frustum.near = normalize(Frustum.near)  # .tolist()
        Frustum.far = normalize(Frustum.far)  # .tolist()

    @staticmethod
    def check_in_frustum(chunk_pos):
        """Frustum check of each chunk. If the chunk is not in the view frustum, it is discarded"""
        planes = (Frustum.left, Frustum.right, Frustum.bottom, Frustum.top, Frustum.near, Frustum.far)
        result = 2
        center = pygame.math.Vector3(chunk_pos[0] * CHUNK_WIDTH, 0, chunk_pos[2] * CHUNK_LENGTH) + chunk1

        def dot(a, b):
            return a * b

        for plane in planes:
            _in = 0
            _out = 0
            normal = pygame.math.Vector3(*plane[:3])
            w = plane[3]
            if dot(normal, center + chunk2) + w < 0:
                _out += 1
            else:
                _in += 1
            if dot(normal, center + chunk3) + w < 0:
                _out += 1
            else:
                _in += 1
            if dot(normal, center + chunk4) + w < 0:
                _out += 1
            else:
                _in += 1
            if dot(normal, center + chunk5) + w < 0:
                _out += 1
            else:
                _in += 1
            if dot(normal, center + chunk6) + w < 0:
                _out += 1
            else:
                _in += 1
            if dot(normal, center + chunk7) + w < 0:
                _out += 1
            else:
                _in += 1
            if dot(normal, center + chunk8) + w < 0:
                _out += 1
            else:
                _in += 1
            if dot(normal, center + chunk9) + w < 0:
                _out += 1
            else:
                _in += 1
            if not _in:
                return 0
            elif _out:
                result = 1
        return result

    def update_matrices(self):

        # 创建透视矩阵
        self.p_matrix_np = gluPerspective(
            (self.world.options.FOV + 10 * (self.speed - WALKING_SPEED) / (SPRINTING_SPEED - WALKING_SPEED)),
            float(self.view_width) / self.view_height, 0.1, 500)

        # 创建模型矩阵
        self.mv_matrix_np = np.dot(glRotatef(self.rotation[1], -1, 0, 0),
                                   glRotatef(self.rotation[0] + math.tau / 4, 0, 1, 0))
        move_np = -np.array(self.interpolated_position, dtype=np.float64) - np.array([0, self.eyelevel, 0],
                                                                                     dtype=np.float64)
        self.mv_matrix_np = np.dot(self.mv_matrix_np, glTranslate(move_np))
        self.mvp_matrix_np = np.dot(self.p_matrix_np, self.mv_matrix_np)

        self.update_frustum(self.mvp_matrix_np)
