import math


# FPS限制
TICKS_PER_SEC = 60

# 区块大小
SECTOR_SIZE = 2

# 移动变量
WALKING_SPEED = 5  # 步行速度
FLYING_SPEED = 15  # 飞行速度
CROUCH_SPEED = 2  # 蹲伏速度
SPRINT_SPEED = 7  # 冲刺速度
SPRINT_FOV = SPRINT_SPEED / 2  # 冲刺时的视野增大

GRAVITY = 20.0  # 重力加速度
MAX_JUMP_HEIGHT = 1.0  # 最大跳跃高度
JUMP_SPEED = math.sqrt(2 * GRAVITY * MAX_JUMP_HEIGHT)  # 跳跃速度
TERMINAL_VELOCITY = 50  # 终端速度，即下落的最大速度

# 玩家变量
PLAYER_HEIGHT = 2  # 玩家身高
PLAYER_FOV = 80.0  # 玩家视野

MESH_SIZE = 32  # 一个物品格子的大小
MESH_BORDER_SIZE = 36  # 带边框的物品格子大小

FACES = [
    (0, 1, 0),
    (0, -1, 0),
    (-1, 0, 0),
    (1, 0, 0),
    (0, 0, 1),
    (0, 0, -1),
]
