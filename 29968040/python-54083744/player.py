from numba import njit
from options import *
import math
from world import sectorize, normalize
import time
import numpy as np
import pygame

from configure import *
from render import WorldModel


@njit(fastmath=True)
def get_sight_vector(x, y):
    """返回当前视线向量，指示玩家的朝向。"""
    # y 范围从 -90 到 90 ，或从 -pi/2 到 pi/2 ，因此 m 范围从 0 到 1 ，
    # 当平行于地面向前看时， m 为 1 ，正对正上或正下时为 0 。
    rad_y = math.radians(y)
    rad_x = math.radians(x - 90)
    m = math.cos(rad_y)
    # dy范围从-1到1，在正对下方时为-1，在正对上方时为1。
    dy = math.sin(rad_y)
    dx = math.cos(rad_x) * m
    dz = math.sin(rad_x) * m
    return dx, dy, dz


class Player:
    def __init__(self, world, inventory, block_data):
        # 当飞行时，重力无效且速度增加
        self.flying = False

        # 用于持续跳跃。如果按住空格键，则为True；否则为False
        self.jumping = False

        # 如果玩家实际进行了跳跃，则为True
        self.jumped = False

        # 如果为True，则在最终的glTranslate中添加蹲伏偏移量
        self.crouch = False

        # 玩家冲刺
        self.sprinting = False

        # 这是一个偏移值，因此可以轻松添加速度药水等内容
        self.fov_offset = 0

        self.collision_types = {"top": False, "bottom": False, "right": False, "left": False}

        self.strafe = [0, 0]

        # 当前世界坐标(x、y、z)位置，使用浮点数表示。请注意，
        # 与数学课程不同，y轴是垂直轴。
        self.position = (30, 50, 80)

        # 第一个元素是在x-z平面(地面)上玩家的旋转角度，从z轴向下测量。
        # 第二个元素是从地面到上方的旋转角度。旋转以度为单位。
        #
        # 垂直平面旋转范围从-90(看向直线下方)到90(看向直线上方)。
        # 水平旋转范围无限制。
        self.rotation = (0, 0)

        # 玩家当前所在的区块
        self.sector = None

        # 在y(向上)方向的速度
        self.dy = 0

        # 便捷的数字键列表。
        self.num_keys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                         pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

        self.last_time = time.time()

        self.world = world
        self.inventory = inventory
        self.block_data = block_data

    def get_sight_vector(self):
        return get_sight_vector(*self.rotation)

    def get_motion_vector(self):
        """返回当前运动向量，指示玩家的速度。

        返回
        -------
        vector : 长度为3的元组
            包含x、y和z速度的元组。

        """
        if any(self.strafe):
            x, y = self.rotation
            strafe = math.degrees(math.atan2(*self.strafe))
            y_angle = math.radians(y)
            x_angle = math.radians(x + strafe)
            if self.flying:
                m = math.cos(y_angle)
                dy = math.sin(y_angle)
                if self.strafe[1]:
                    # 向左或向右移动。
                    dy = 0.0
                    m = 1
                if self.strafe[0] > 0:
                    # 向后移动。
                    dy *= -1
                # 当你向上或向下飞行时，左右运动更少。
                dx = math.cos(x_angle) * m
                dz = math.sin(x_angle) * m
            else:
                dy = 0.0
                dx = math.cos(x_angle)
                dz = math.sin(x_angle)
        else:
            dy = dx = dz = 0.0
        return dx, dy, dz

    def update(self):
        """这个方法被pyglet的时钟重复调用。

        参数
        ----------
        dt : 浮点数
            自上次调用以来的时间变化量。

        """
        dt = time.time() - self.last_time  # 1.0 / TICKS_PER_SEC
        self.last_time = time.time()
        self.world.process_queue()
        sector = sectorize(self.position)
        if sector != self.sector:
            self.world.change_sectors(self.sector, sector)
            if self.sector is None:
                self.world.process_entire_queue()
            self.sector = sector
        m = 8
        dt = min(dt, 0.2)
        for _ in np.arange(m):
            self._update(dt / m)

    def _update(self, dt):
        """ update() 方法的私有实现。这是大部分运动逻辑、重力和碰撞检测的地方。

        参数
        ----------
        dt : float
            自上次调用以来的时间变化量。

        """
        # 行走
        if self.flying:
            speed = FLYING_SPEED  # 飞行速度
        elif self.sprinting:
            speed = SPRINT_SPEED  # 冲刺速度
        elif self.crouch:
            speed = CROUCH_SPEED  # 蹲伏速度
        else:
            speed = WALKING_SPEED  # 步行速度

        if self.jumping:
            if self.collision_types["top"]:
                self.dy = JUMP_SPEED  # 跳跃速度
                self.jumped = True
        else:
            if self.collision_types["top"]:
                self.jumped = False
        if self.jumped:
            speed += 0.7

        d = dt * speed  # 这一帧移动的距离
        dx, dy, dz = self.get_motion_vector()
        # 新的空间位置，尚未考虑重力。
        dx, dy, dz = dx * d, dy * d, dz * d
        # 重力
        if not self.flying:
            # 更新垂直速度：如果你在下落，加速直到达到极限速度；如果你在跳跃，减速直到开始下落。
            self.dy -= dt * GRAVITY  # 重力加速度
            self.dy = max(self.dy, -TERMINAL_VELOCITY)  # 最大下降速度
            dy += self.dy * dt
        # 碰撞检测
        old_pos = self.position
        x, y, z = old_pos
        x, y, z = self.collide((x + dx, y + dy, z + dz), PLAYER_HEIGHT)
        self.position = (x, y, z)

        # 冲刺相关。如果玩家在 x 和 z 方向上停止移动，则停止冲刺并从视野偏移中减去冲刺视野。
        if old_pos[0] - self.position[0] == 0 and old_pos[2] - self.position[2] == 0:
            disablefov = False
            if self.sprinting:
                disablefov = True
            self.sprinting = False
            if disablefov:
                self.fov_offset -= SPRINT_FOV

    def collide(self, position, height):
        """ 检查给定位置和高度的玩家是否与世界中的任何方块碰撞。

        参数
        ----------
        position : 长度为 3 的元组
            要检查碰撞的 (x, y, z) 位置。
        height : int 或 float
            玩家的高度。

        返回
        -------
        position : 长度为 3 的元组
            考虑到碰撞后玩家的新位置。

        """
        # 需要有多少与周围方块的维度重叠才能算作碰撞。
        # 如果为 0，则任何与地形接触都算作碰撞。
        # 如果为0.49，则你会陷入地面，就像走在高草里一样。
        # 如果 >= 0.5，你会穿过地面。
        pad = 0.25
        p = list(position)  # 当前坐标
        np_ = normalize(position)  # 强转成整数后的
        self.collision_types = {"top": False, "bottom": False, "right": False, "left": False}
        for face in FACES:  # 检查所有周围的方块
            for i in range(3):  # 按照每个维度单独检查
                if not face[i]:  # 当前维度无需检查
                    continue
                # 你在这个维度上的重叠程度。
                d = (p[i] - np_[i]) * face[i]
                if d < pad:
                    continue
                for dy in range(height):  # 检查每个高度
                    op = list(np_)
                    op[1] -= dy
                    op[i] += face[i]
                    if tuple(op) not in self.world.world:
                        continue
                    p[i] -= (d - pad) * face[i]
                    # 如果你与地面或天花板发生碰撞，则停止下落/上升。
                    if face == (0, -1, 0):
                        self.collision_types["top"] = True
                        self.dy = 0
                    if face == (0, 1, 0):
                        self.collision_types["bottom"] = True
                        self.dy = 0
                    break
        return tuple(p)

    @staticmethod
    def check_ctrl_down():
        return pygame.key.get_pressed()[pygame.K_LCTRL] or pygame.key.get_pressed()[pygame.K_RCTRL]

    def calc_length(self, previous):
        length_a = math.sqrt((previous[0] - self.position[0]) ** 2 +
                             (previous[1] - self.position[1]) ** 2 +
                             (previous[2] - self.position[2]) ** 2)
        length_b = math.sqrt((previous[0] - self.position[0]) ** 2 +
                             (previous[1] - self.position[1] + 1) ** 2 +
                             (previous[2] - self.position[2]) ** 2)
        return length_a >= 0.7 and length_b >= 0.7
    
    def on_mouse_press(self, button):
        vector = self.get_sight_vector()
        block, previous = self.world.hit_test(self.position, vector)
        if button == 3 or (button == 1 and self.check_ctrl_down()):
            if previous and self.calc_length(previous):
                block = self.inventory.get_block()
                if block:
                    self.world.add_block(previous, block)
        elif button == 1 and block:
            texture = self.world.world[block]
            if texture != BEDROCK:
                self.world.remove_block(block)
                # self.world.add_drop(texture, block)

    def on_mouse_motion(self, dx, dy):
        dy = -dy
        m = 0.15
        x, y = self.rotation
        x, y = x + dx * m, y + dy * m
        y = max(-90, min(90, y))
        self.rotation = (x, y)

    def on_key_press(self, symbol):
        if symbol == pygame.K_w:
            self.strafe[0] -= 1
        elif symbol == pygame.K_s:
            self.strafe[0] += 1
        elif symbol == pygame.K_a:
            self.strafe[1] -= 1
        elif symbol == pygame.K_d:
            self.strafe[1] += 1
        elif symbol == pygame.K_c:
            self.fov_offset -= 60.0  # 望远镜模式（自己编的，作者没玩过mc）
        elif symbol == pygame.K_SPACE:
            self.jumping = True
        elif symbol == pygame.K_LSHIFT:
            self.crouch = True  # 潜行
            if self.sprinting:
                self.fov_offset -= SPRINT_FOV
                self.sprinting = False
        elif symbol == pygame.K_r:
            if not self.crouch:
                if not self.sprinting:
                    self.fov_offset += SPRINT_FOV
                self.sprinting = True  # 疾跑
        elif symbol == pygame.K_TAB:
            self.flying = not self.flying
        elif symbol in self.num_keys:
            index = (symbol - 1 - self.num_keys[0]) % 9
            self.inventory.set_index(index)
    
    def on_key_release(self, symbol):
        if symbol == pygame.K_w:
            self.strafe[0] += 1
        elif symbol == pygame.K_s:
            self.strafe[0] -= 1
        elif symbol == pygame.K_a:
            self.strafe[1] += 1
        elif symbol == pygame.K_d:
            self.strafe[1] -= 1
        elif symbol == pygame.K_SPACE:
            self.jumping = False
        elif symbol == pygame.K_LSHIFT:
            self.crouch = False
        elif symbol == pygame.K_c:
            self.fov_offset += 60.0
    
    def get_focused_block(self):
        """在准星下方的方块周围绘制黑色边界。

        """
        vector = get_sight_vector(*self.rotation)
        block = self.world.hit_test(self.position, vector)[0]
        if block:
            texture = self.block_data[self.world.world[block]]
            x, y, z = block
            new_vertices = texture.model.vertices.copy()
            new_vertices[:, 0, 0] += x
            new_vertices[:, 1, 0] += y
            new_vertices[:, 2, 0] += z
            model = WorldModel(self.block_data.texture_manager, texture.model.uv_vertices, texture.model.uv_indices, 1)
            model.vertices = new_vertices
            model.indices = texture.model.indices
            model.uv_index = texture.tex_indices_triangle
            return model, block
        return None, None

    def hit_test_screen(self, model_old):
        vertices = model_old.vertices[:, :3, 0]
        x, y, z = self.position
        dx, dy, dz = self.get_sight_vector()
        n = (vertices[0, 2] - z) / dz
        if n < 0:
            return -114514, -114514
        res_x, res_y = x + n * dx, y + n * dy
        max_x, min_x = max(vertices[:, 0]), min(vertices[:, 0])
        max_y, min_y = max(vertices[:, 1]), min(vertices[:, 1])
        return 1000 * (res_x - min_x)/(max_x - min_x), 700 * (max_y - res_y)/(max_y - min_y)
