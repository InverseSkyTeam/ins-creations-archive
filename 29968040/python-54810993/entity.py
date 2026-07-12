import math
import collider

FLYING_ACCEL = (0,   0, 0)  # 飞行加速度
GRAVITY_ACCEL = (0, -32, 0)  # 重力加速度

# 这些值都来源于Minecraft，但乘以20（因为Minecraft运行在20 TPS）

FRICTION = (20,  20,  20)  # 摩擦力

DRAG_FLY = (5,   5,   5)  # 飞行阻力
DRAG_JUMP = (1.8,   0, 1.8)  # 跳跃阻力
DRAG_FALL = (1.8, 0.4, 1.8)  # 下落阻力


class Entity:  # 实体类
    def __init__(self, world):
        self.world = world

        # 物理变量

        self.jump_height = 1.25  # 跳跃高度
        self.flying = False  # 是否飞行

        self.position = [0, 80, 0]  # 位置
        self.rotation = [-math.tau / 4, 0]  # 旋转角度

        self.old_position = tuple(self.position)
        self.old_rotation = tuple(self.rotation)

        self.step = 1  # 步长

        self.velocity = [0.0, 0.0, 0.0]  # 速度
        self.accel = [0, 0, 0]  # 加速度

        # 碰撞变量

        self.width = 0.6  # 宽度
        self.height = 1.8  # 高度

        self.collider = collider.Collider()  # 碰撞箱
        self.grounded = False  # 是否在地面上

    def update_collider(self):  # 更新碰撞箱
        x, y, z = self.position

        self.collider.x1 = x - self.width / 2
        self.collider.x2 = x + self.width / 2

        self.collider.y1 = y
        self.collider.y2 = y + self.height

        self.collider.z1 = z - self.width / 2
        self.collider.z2 = z + self.width / 2

    def teleport(self, pos):  # 传送
        self.position = list(pos)
        self.velocity = [0.0, 0.0, 0.0]  # 防止碰撞

    def jump(self, height=None):
        if not self.grounded:  # 当在空中无法进行跳跃时，不能执行跳跃
            return

        if height is None:
            height = self.jump_height

        self.velocity[1] = math.sqrt(2 * height * -GRAVITY_ACCEL[1])

    @property
    def friction(self):
        if self.flying:
            return DRAG_FLY
        elif self.grounded:
            return FRICTION
        elif self.velocity[1] > 0:
            return DRAG_JUMP
        return DRAG_FALL

    def update(self, delta_time):
        self.step = 1
        self.old_position = tuple(self.position)
    
        # 应用输入的加速度，并考虑摩擦/阻力

        self.velocity = [v + a * f * delta_time for v, a, f in zip(self.velocity, self.accel, self.friction)]
        self.accel = [0, 0, 0]

        # 计算碰撞

        self.update_collider()
        self.grounded = False

        for _ in range(3):
            adjusted_velocity = [v * delta_time for v in self.velocity]  # 计算加速度
            vx, vy, vz = adjusted_velocity

            # 找出所有可能发生碰撞的方块
            # 这一步被称为 “broad-phasing 算法”

            step_x = 1 if vx > 0 else -1
            step_y = 1 if vy > 0 else -1
            step_z = 1 if vz > 0 else -1

            steps_xz = int(self.width / 2)
            steps_y = int(self.height)

            x, y, z = map(int, self.position)
            cx, cy, cz = [int(x + v) for x, v in zip(self.position, adjusted_velocity)]

            potential_collisions = []

            for i in range(x - step_x * (steps_xz + 1), cx + step_x * (steps_xz + 2), step_x):
                for j in range(y - step_y * (steps_y + 2), cy + step_y * (steps_y + 3), step_y):
                    for k in range(z - step_z * (steps_xz + 1), cz + step_z * (steps_xz + 2), step_z):
                        pos = (i, j, k)
                        num = self.world.get_block_number(pos)

                        if not num:
                            continue

                        for _collider in self.world.block_types[num].colliders:
                            entry_time, normal = self.collider.collide(_collider + pos, adjusted_velocity)

                            if normal is None:
                                continue

                            potential_collisions.append((entry_time, normal))

            # 获取第一个碰撞

            if not potential_collisions:
                break

            entry_time, normal = min(potential_collisions, key=lambda _x: _x[0])
            entry_time -= 0.001

            if normal[0]:
                self.velocity[0] = 0
                self.position[0] += vx * entry_time
            
            if normal[1]:
                self.velocity[1] = 0
                self.position[1] += vy * entry_time

            if normal[2]:
                self.velocity[2] = 0
                self.position[2] += vz * entry_time

            if normal[1] == 1:
                self.grounded = True

        self.position = [x + v * delta_time for x, v in zip(self.position, self.velocity)]  # 更新实体位置

        # 应用重力加速度

        gravity = (GRAVITY_ACCEL, FLYING_ACCEL)[self.flying]
        self.velocity = [v + a * delta_time for v, a in zip(self.velocity, gravity)]

        # 应用摩擦/阻力

        self.velocity = [v - min(v * f * delta_time, v, key=abs) for v, f in zip(self.velocity, self.friction)]

        # 再次更新碰撞箱，确保在函数外部可以依赖实体的碰撞器

        self.update_collider()
