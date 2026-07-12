import math

HIT_RANGE = 3


class Hit_ray:
    def __init__(self, world, rotation, starting_position):
        self.world = world

        # 根据旋转角度获得射线单位向量
        # sqrt(ux ^ 2 + uy ^ 2 + uz ^ 2) 必须始终等于1
        self.vector = (
            math.cos(rotation[0]) * math.cos(rotation[1]),
            math.sin(rotation[1]),
            math.sin(rotation[0]) * math.cos(rotation[1])
        )
        
        # 点的位置
        self.position = list(starting_position)

        # 点当前所在的方块位置
        self.block = tuple(map(lambda x: int(round(x)), self.position))

        # 点已经行进的距离
        self.distance = 0

    # 'check' 和 'step' 如果击中返回'True'，否则返回'False'
    def check(self, hit_callback, distance, current_block, next_block):
        if self.world.get_block_number(next_block):
            hit_callback(current_block, next_block)
            return True
        else:
            self.position = list(map(lambda x: self.position[x] + self.vector[x] * distance, range(3)))
            self.block = next_block
            self.distance += distance
            return False

    def step(self, hit_callback):
        bx, by, bz = self.block

        # 点相对于方块中心的位置
        local_position = list(map(lambda _x: self.position[_x] - self.block[_x], range(3)))

        # 我们不希望处理负数，因此去掉符号
        # 这也很酷，因为这意味着我们不需要考虑射线向量的符号
        # 但是，我们需要记住哪些分量以后会是负数

        sign = [1, 1, 1]  # '1' 表示正数，'-1' 表示负数
        absolute_vector = list(self.vector)

        for component, element in enumerate(self.vector):
            sign[component] = 2 * (element >= 0) - 1
            absolute_vector[component] *= sign[component]
            local_position[component] *= sign[component]
        
        lx, ly, lz = local_position
        vx, vy, vz = absolute_vector

        # 计算交点
        # 我只详细介绍第一个分量(X)的数学原理，因为其余部分都很明显

        # 射线(r)通过该点的线 r ≡ (x - lx) / vx = (y - ly) / lz = (z - lz) / vz (参数方程)

        # +x 面 fx ≡ x = 0.5 (y和z可以是任意实数)
        # r ∩ fx ≡ (0.5 - lx) / vx = (y - ly) / vy = (z - lz) / vz

        # x: x = 0.5
        # y: (y - ly) / vy = (0.5 - lx) / vx 当且仅当 y = (0.5 - lx) / vx * vy + ly
        # z: (z - lz) / vz = (0.5 - lx) / vx 当且仅当 z = (0.5 - lx) / vx * vz + lz

        if vx:
            x = 0.5
            y = (0.5 - lx) / vx * vy + ly
            z = (0.5 - lx) / vx * vz + lz

            if -0.5 <= y <= 0.5 and -0.5 <= z <= 0.5:
                distance = math.sqrt((x - lx) ** 2 + (y - ly) ** 2 + (z - lz) ** 2)
                return self.check(hit_callback, distance, (bx, by, bz), (bx + sign[0], by, bz))

        if vy:
            x = (0.5 - ly) / vy * vx + lx
            y = 0.5
            z = (0.5 - ly) / vy * vz + lz

            if -0.5 <= x <= 0.5 and -0.5 <= z <= 0.5:
                distance = math.sqrt((x - lx) ** 2 + (y - ly) ** 2 + (z - lz) ** 2)
                return self.check(hit_callback, distance, (bx, by, bz), (bx, by + sign[1], bz))
        
        if vz:
            x = (0.5 - lz) / vz * vx + lx
            y = (0.5 - lz) / vz * vy + ly
            z = 0.5

            if -0.5 <= x <= 0.5 and -0.5 <= y <= 0.5:
                distance = math.sqrt((x - lx) ** 2 + (y - ly) ** 2 + (z - lz) ** 2)
                return self.check(hit_callback, distance, (bx, by, bz), (bx, by, bz + sign[2]))
