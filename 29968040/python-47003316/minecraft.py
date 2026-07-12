from __future__ import division  # 如果是python2,需要导入精确除法
import pygame  # 导入pygame库用于游戏开发
import sys  # 导入sys库用于与Python解释器进行交互
import math  # 导入math库用于处理数学运算
import random  # 导入random库用于生成随机数
import time  # 导入time库用于时间相关操作
from collections import deque  # 导入deque库用于创建双向队列
from pyglet import image  # 导入pyglet库用于图像处理
from pyglet.gl import *  # 导入pyglet库的OpenGL模块
from pyglet.graphics import TextureGroup  # 导入pyglet库的纹理组模块
from pyglet.window import key, mouse  # 导入pyglet库的键盘和鼠标模块
from noise_gen import NoiseGen  # 导入自定义的噪声生成类
import numpy as np
from numpy import arange

pygame.mixer.init()  # 初始化音频模块
pygame.mixer.music.load("Minecraft-c418.mp3")  # 加载音乐文件
pygame.mixer.music.play(10, 20)  # 播放音乐，循环播放10次，从第20秒开始播放
pygame.key.stop_text_input()

TICKS_PER_SEC = 60  # 游戏每秒更新的次数

# 方块加载的扇区大小
SECTOR_SIZE = 100

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

if sys.version_info[0] >= 3:  # 如果Python版本大于等于3
    xrange = range  # 将range函数赋值给xrange，以保持向后兼容性

def cube_vertices(x, y, z, n):
    """返回位置为x，y，z，长宽为2*n的立方体的顶点坐标。"""
    return [
        x - n, y + n, z - n, x - n, y + n, z + n, x + n, y + n, z + n, x + n, y + n, z - n,  # 顶面
        x - n, y - n, z - n, x + n, y - n, z - n, x + n, y - n, z + n, x - n, y - n, z + n,  # 底面
        x - n, y - n, z - n, x - n, y - n, z + n, x - n, y + n, z + n, x - n, y + n, z - n,  # 左侧面
        x + n, y - n, z + n, x + n, y - n, z - n, x + n, y + n, z - n, x + n, y + n, z + n,  # 右侧面
        x - n, y - n, z + n, x + n, y - n, z + n, x + n, y + n, z + n, x - n, y + n, z + n,  # 前面
        x + n, y - n, z - n, x - n, y - n, z - n, x - n, y + n, z - n, x + n, y + n, z - n,  # 后面
    ]


def tex_coord(x, y, n=4):
    """返回指定纹理的边界顶点。"""
    m = 1.0 / n
    dx = x * m
    dy = y * m
    return dx, dy, dx + m, dy, dx + m, dy + m, dx, dy + m


def tex_coords(top, bottom, side):
    """返回顶部、底部和侧面的纹理正方形列表。"""
    top = tex_coord(*top)
    bottom = tex_coord(*bottom)
    side = tex_coord(*side)
    result = []
    result.extend(top)
    result.extend(bottom)
    result.extend(side * 4)
    return result


TEXTURE_PATH = 'texture.png'  # 纹理路径

GRASS = tex_coords((1, 0), (0, 1), (0, 0))  # 草地纹理
SAND = tex_coords((1, 1), (1, 1), (1, 1))  # 沙子纹理
BRICK = tex_coords((2, 0), (2, 0), (2, 0))  # 砖块纹理
STONE = tex_coords((2, 1), (2, 1), (2, 1))  # 石块纹理
WOOD = tex_coords((3, 1), (3, 1), (3, 1))  # 木材纹理
LEAF = tex_coords((3, 0), (3, 0), (3, 0))  # 叶子纹理
WATER = tex_coords((0, 2), (0, 2), (0, 2))  # 水纹理
DIRT = tex_coords((0, 1), (0, 1), (0, 1))  # 泥土纹理

#FACES列表表示每个面法向量指向的方向，每个元组的三个数分别表示法向量指向位置的xyz
#比如第一个元组的第二个数是1，表示这个面法向量指向y轴正半轴，即顶面
FACES = [
    (0, 1, 0),
    (0, -1, 0),
    (-1, 0, 0),
    (1, 0, 0),
    (0, 0, 1),
    (0, 0, -1),
]


def normalize(position):
    """将任意精度的position坐标转换成block坐标。"""

    x, y, z = position
    x, y, z = (int(round(x)), int(round(y)), int(round(z)))
    return (x, y, z)

def sectorize(position):
    """返回表示给定位置`position`所在领域的元组。

    参数
    ----------
    position : 长度为3的元组

    返回值
    -------
    sector : 长度为3的元组

    """
    x, y, z = normalize(position)  # 将位置规范化
    x, y, z = x // SECTOR_SIZE, y // SECTOR_SIZE, z // SECTOR_SIZE  # 根据SECTOR_SIZE将位置转换为领域坐标
    return (x, 0, z)


class Model(object):

    def __init__(self):

        # 一个Batch是批量渲染的顶点列表集合。
        self.batch = pyglet.graphics.Batch()

        # 一个TextureGroup管理一个OpenGL纹理。
        self.group = TextureGroup(image.load(TEXTURE_PATH).get_texture())

        # 从位置映射到该位置处方块的纹理的映射。
        # 这定义了当前世界中的所有方块。
        self.world = {}

        # 和`world`相同的映射，但只包含显示的方块。
        self.shown = {}

        # 从位置映射到所有显示的方块的pyglet `VertextList`的映射。
        self._shown = {}

        # 从领域映射到该领域内的位置列表。
        self.sectors = {}

        # 简单的函数队列实现。队列由_show_block()和_hide_block()方法调用填充。
        self.queue = deque()

        self._initialize()

    def _initialize(self):
        """通过放置所有方块来初始化世界。

        """
        print("开始生成世界")
        gen = NoiseGen(452692)

        n = 128  # 世界的大小
        y = 0  # 初始y高度
        
        print('初始化地形高度')
        heightMap = np.zeros((n,n))
        for x in arange(n):
            for z in arange(n):
                heightMap[x,z] = int(gen.getHeight(x, z))
        print('地形高度初始化完成')
        
        # 生成世界
        for x in arange(n):
            for z in arange(n):
                h = heightMap[x,z]
                if (h < 15):
                    for y in arange(1, max(int(h/2),2)):
                        self.add_block((x, y, z), STONE, immediate=False)
                    for y in arange(max(int(h/2),2), 15):
                        self.add_block((x, y, z), WATER, immediate=False)
                    continue
                #if (h < 18):
                #    self.add_block((x, h, z), SAND, immediate=False)
                self.add_block((x, h, z), GRASS, immediate=False)
                for y in arange(h - 1, 0, -1):
                    self.add_block((x, y, z), STONE, immediate=False)
                # 可能在这个位置(x, z)添加树
                if (h > 20):
                    if random.randrange(0, 1000) > 990:
                        treeHeight = random.randrange(5, 7)
                        # 树干
                        for y in arange(h + 1, h + treeHeight):
                            self.add_block((x, y, z), WOOD, immediate=False)
                        # 树叶
                        leafh = h + treeHeight
                        for lz in arange(z + -2, z + 3):
                            for lx in arange(x + -2, x + 3): 
                                for ly in arange(3):
                                    self.add_block((lx, leafh + ly, lz), LEAF, immediate=False)
        print("世界生成完成")
    def hit_test(self, position, vector, max_distance=8):
        """从当前位置进行视线搜索。如果遇到方块，则返回该方块以及视线上的前一个方块。
        如果没有找到方块，则返回None，None。

        参数
        ----------
        position : 长度为3的元组
            要检查可见性的位置(x, y, z)。
        vector : 长度为3的元组
            视线向量。
        max_distance : 整数
            搜索碰撞的最大距离（单位：方块）。

        """
        m = 8
        x, y, z = position
        dx, dy, dz = vector
        previous = None
        for _ in xrange(max_distance * m):
            key = normalize((x, y, z))
            if key != previous and key in self.world:
                return key, previous
            previous = key
            x, y, z = x + dx / m, y + dy / m, z + dz / m
        return None, None

    def exposed(self, position):
        """如果给定的`position`在所有6个面都被方块包围，则返回False，否则返回True。

        """
        x, y, z = position
        for dx, dy, dz in FACES:
            if (x + dx, y + dy, z + dz) not in self.world:
                return True
        return False

    def add_block(self, position, texture, immediate=True):
        """将带有给定纹理和位置的方块添加到世界中。
    
        参数
        ----------
        position：长度为3的元组
            要添加的方块的(x, y, z)位置。
        texture：长度为3的列表
            纹理方块的坐标。使用`tex_coords()`生成。
        immediate：bool
            是否立即绘制方块。
    
        """
        if position in self.world:
            self.remove_block(position, immediate)
        self.world[position] = texture
        self.sectors.setdefault(sectorize(position), []).append(position)
        if immediate:
            if self.exposed(position):
                self.show_block(position)
            self.check_neighbors(position)
        
    def remove_block(self, position, immediate=True):
        """删除给定位置处的方块。
    
        参数
        ----------
        position：长度为3的元组
            要删除的方块的(x, y, z)位置。
        immediate：bool
            是否立即从画布中移除方块。
    
        """
        del self.world[position]
        self.sectors[sectorize(position)].remove(position)
        if immediate:
            if position in self.shown:
                self.hide_block(position)
            self.check_neighbors(position)
    
    def check_neighbors(self, position):
        """检查“position”周围的所有方块，并确保它们的可视状态是准确的。
        这意味着隐藏未显示的方块，并显示所有暴露的方块。通常在添加或删除方块后使用。
    
        """
        x, y, z = position
        for dx, dy, dz in FACES:
            key = (x + dx, y + dy, z + dz)
            if key not in self.world:
                continue
            if self.exposed(key):
                if key not in self.shown:
                    self.show_block(key)
            else:
                if key in self.shown:
                    self.hide_block(key)
    
    def show_block(self, position, immediate=True):
        """显示给定位置处的方块。这个方法假设方块已经使用add_block()方法添加了。
    
        参数
        ----------
        position：长度为3的元组
            要显示的方块的(x, y, z)位置。
        immediate：bool
            是否立即显示方块。
    
        """
        texture = self.world[position]
        self.shown[position] = texture
        if immediate:
            self._show_block(position, texture)
        else:
            self._enqueue(self._show_block, position, texture)
    
    def _show_block(self, position, texture):
        """show_block()方法的私有实现。
    
        参数
        ----------
        position：长度为3的元组
            要显示的方块的(x, y, z)位置。
        texture：长度为3的列表
            纹理方块的坐标。使用`tex_coords()`生成。
    
        """
        x, y, z = position
        vertex_data = cube_vertices(x, y, z, 0.5)
        texture_data = list(texture)
        # 创建顶点列表
        # FIXME：可能应该使用add_indexed()替代
        self._shown[position] = self.batch.add(24, GL_QUADS, self.group,
            ('v3f/static', vertex_data),
            ('t2f/static', texture_data))
    
    def hide_block(self, position, immediate=True):
        """隐藏给定位置处的方块。隐藏不会从世界中移除方块。
    
        参数
        ----------
        position：长度为3的元组
            要隐藏的方块的(x, y, z)位置。
        immediate：bool
            是否立即从画布中移除方块。
    
        """
        self.shown.pop(position)
        if immediate:
            self._hide_block(position)
        else:
            self._enqueue(self._hide_block, position)
    
    def _hide_block(self, position):
        """hide_block()方法的私有实现。
    
        """
        self._shown.pop(position).delete()
    
    def show_sector(self, sector):
        """确保需要显示的给定区块中的所有方块都绘制到画布上。
    
        """
        for position in self.sectors.get(sector, []):
            if position not in self.shown and self.exposed(position):
                self.show_block(position, False)
    
    def hide_sector(self, sector):
        """确保需要隐藏的给定区块中的所有方块都从画布中移除。
    
        """
        for position in self.sectors.get(sector, []):
            if position in self.shown:
                self.hide_block(position, False)
    
    def change_sectors(self, before, after):
        """从“before”区块移动到“after”区块。区块是世界的连续x、y子区域。区块用于加速世界渲染。
    
        """
        before_set = set()
        after_set = set()
        pad = 4
        for dx in xrange(-pad, pad + 1):
            for dy in [0]:  # xrange(-pad, pad + 1):
                for dz in xrange(-pad, pad + 1):
                    if dx ** 2 + dy ** 2 + dz ** 2 > (pad + 1) ** 2:
                        continue
                    if before:
                        x, y, z = before
                        before_set.add((x + dx, y + dy, z + dz))
                    if after:
                        x, y, z = after
                        after_set.add((x + dx, y + dy, z + dz))
        show = after_set - before_set
        hide = before_set - after_set
        for sector in show:
            self.show_sector(sector)
        for sector in hide:
            self.hide_sector(sector)
    
    def _enqueue(self, func, *args):
        """将“func”添加到内部队列中。
    
        """
        self.queue.append((func, args))
    
    def _dequeue(self):
        """从内部队列中弹出顶部函数并调用它。
    
        """
        func, args = self.queue.popleft()
        func(*args)
    
    def process_queue(self):
        """在定期休息的同时处理整个队列。这样可以使游戏循环顺利运行。
        队列包含对_show_block()和_hide_block()的调用，所以如果add_block()或remove_block()使用immediate=False调用，应该调用该方法。
    
        """
        start = time.process_time()
        while self.queue and time.process_time() - start < 1.0 / TICKS_PER_SEC:
            self._dequeue()
    
    def process_entire_queue(self):
        """处理整个队列，没有休息。
    
        """
        while self.queue:
            self._dequeue()

class Window(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        # 是否独占鼠标的窗口
        self.exclusive = False

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

        # 屏幕中央的准星
        self.reticle = None

        # 在y(向上)方向的速度
        self.dy = 0

        # 玩家可以放置的方块列表。按数字键循环选择。
        self.inventory = [BRICK, GRASS, SAND, WOOD, LEAF,DIRT]

        # 用户可以放置的当前方块。按数字键循环选择。
        self.block = self.inventory[0]

        # 便捷的数字键列表。
        self.num_keys = [
            key._1, key._2, key._3, key._4, key._5,
            key._6, key._7, key._8, key._9, key._0]

        # 处理世界的模型实例。
        self.model = Model()

        # 在画布左上角显示的标签。
        self.label = pyglet.text.Label('', font_name='Arial', font_size=18,
            x=10, y=self.height - 10, anchor_x='left', anchor_y='top',
            color=(0, 0, 0, 255))

        # 这个调用将`update()`方法安排在TICKS_PER_SEC时调用一次。
        # 这是主游戏事件循环。
        pyglet.clock.schedule_interval(self.update, 1.0 / TICKS_PER_SEC)

    def set_exclusive_mouse(self, exclusive):
        """如果`exclusive`为True，则游戏将捕获鼠标；如果为False，则游戏将忽略鼠标。"""
        super(Window, self).set_exclusive_mouse(exclusive)
        self.exclusive = exclusive

    def get_sight_vector(self):
        """返回当前视线向量，指示玩家的朝向。"""
        x, y = self.rotation
        # y范围从-90到90，或从-pi/2到pi/2，因此m范围从0到1，
        # 当平行于地面向前看时，m为1，正对正上或正下时为0。
        m = math.cos(math.radians(y))
        # dy范围从-1到1，在正对下方时为-1，在正对上方时为1。
        dy = math.sin(math.radians(y))
        dx = math.cos(math.radians(x - 90)) * m
        dz = math.sin(math.radians(x - 90)) * m
        return (dx, dy, dz)

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
            dy = 0.0
            dx = 0.0
            dz = 0.0
        return (dx, dy, dz)

    def update(self, dt):
        """这个方法被pyglet的时钟重复调用。

        参数
        ----------
        dt : 浮点数
            自上次调用以来的时间变化量。

        """
        self.model.process_queue()
        sector = sectorize(self.position)
        if sector != self.sector:
            self.model.change_sectors(self.sector, sector)
            if self.sector is None:
                self.model.process_entire_queue()
            self.sector = sector
        m = 8
        dt = min(dt, 0.2)
        for _ in arange(m):
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
        p = list(position)
        np = normalize(position)
        self.collision_types = {"top": False, "bottom": False, "right": False, "left": False}
        for face in FACES:  # 检查所有周围的方块
            for i in xrange(3):  # 按照每个维度单独检查
                if not face[i]:
                    continue
                # 你在这个维度上的重叠程度。
                d = (p[i] - np[i]) * face[i]
                if d < pad:
                    continue
                for dy in xrange(height):  # 检查每个高度
                    op = list(np)
                    op[1] -= dy
                    op[i] += face[i]
                    if tuple(op) not in self.model.world:
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
    
    def on_mouse_press(self, x, y, button, modifiers):
        """ 当鼠标按下时调用。请参阅 pyglet 文档以获取按钮和修改键的映射。
    
        参数
        ----------
        x, y : int
            鼠标点击的坐标。如果鼠标被捕获，则始终为屏幕中心。
        button : int
            表示被点击的鼠标按钮的数字。1 = 左键，4 = 右键。
        modifiers : int
            表示鼠标按钮被按下时按下的任何修改键的数字。
    
        """
        if self.exclusive:
            vector = self.get_sight_vector()
            block, previous = self.model.hit_test(self.position, vector)
            if (button == mouse.RIGHT) or \
                    ((button == mouse.LEFT) and (modifiers & key.MOD_CTRL)):
                # 在 OSX 上，control + left click = right click。
                if previous:
                    self.model.add_block(previous, self.block)
            elif button == pyglet.window.mouse.LEFT and block:
                texture = self.model.world[block]
                if texture != STONE:
                    self.model.remove_block(block)
        else:
            self.set_exclusive_mouse(True)
    
    def on_mouse_motion(self, x, y, dx, dy):
        """ 当玩家移动鼠标时调用。
    
        参数
        ----------
        x, y : int
            鼠标点击的坐标。如果鼠标被捕获，则始终为屏幕中心。
        dx, dy : float
            鼠标的移动距离。
    
        """
        if self.exclusive:
            m = 0.15
            x, y = self.rotation
            x, y = x + dx * m, y + dy * m
            y = max(-90, min(90, y))
            self.rotation = (x, y)
    
    def on_key_press(self, symbol, modifiers):
        """ 当玩家按下键时调用。请参阅 pyglet 文档以获取键的映射。
    
        参数
        ----------
        symbol : int
            表示被按下的键的数字。
        modifiers : int
            表示在鼠标按钮被点击时按下的任何修改键的数字。
    
        """
        if symbol == key.W:
            self.strafe[0] -= 1
        elif symbol == key.S:
            self.strafe[0] += 1
        elif symbol == key.A:
            self.strafe[1] -= 1
        elif symbol == key.D:
            self.strafe[1] += 1
        elif symbol == key.C:
            self.fov_offset -= 60.0#望远镜模式（自己编的，作者没玩过mc）
        elif symbol == key.SPACE:
            self.jumping = True
        elif symbol == key.ESCAPE:
            self.set_exclusive_mouse(False)
        elif symbol == key.LSHIFT:
            self.crouch = True#潜行
            if self.sprinting:
                self.fov_offset -= SPRINT_FOV
                self.sprinting = False
        elif symbol == key.R:
            if not self.crouch:
                if not self.sprinting:
                    self.fov_offset += SPRINT_FOV
                self.sprinting = True#疾跑
        elif symbol == key.TAB:
            self.flying = not self.flying
        elif symbol in self.num_keys:
            index = (symbol - self.num_keys[0]) % len(self.inventory)
            self.block = self.inventory[index]

    def on_key_release(self, symbol, modifiers):
        """当玩家释放一个键时调用。symbol代表按下的键，modifiers代表其他同时按下的修饰键。
    
        参数
        ----------
        symbol : int
            表示被按下的键的数字
        modifiers : int
            表示同时按下的修饰键的数字
    
        """
        if symbol == key.W:
            self.strafe[0] += 1
        elif symbol == key.S:
            self.strafe[0] -= 1
        elif symbol == key.A:
            self.strafe[1] += 1
        elif symbol == key.D:
            self.strafe[1] -= 1
        elif symbol == key.SPACE:
            self.jumping = False
        elif symbol == key.LSHIFT:
            self.crouch = False
        elif symbol == key.C:
            self.fov_offset += 60.0
    
    def on_resize(self, width, height):
        """当窗口被调整为新的`width`和`height`时调用。
    
        """
        # 标签
        self.label.y = height - 10
        # 准星
        if self.reticle:
            self.reticle.delete()
        x, y = self.width // 2, self.height // 2
        n = 10
        self.reticle = pyglet.graphics.vertex_list(4,
            ('v2i', (x - n, y, x + n, y, x, y - n, x, y + n))
        )
    
    def set_2d(self):
        """配置OpenGL为2D绘图模式。
    
        """
        width, height = self.get_size()
        glDisable(GL_DEPTH_TEST)
        viewport = self.get_viewport_size()
        glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, max(1, width), 0, max(1, height), -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
    
    def set_3d(self):
        """配置OpenGL为3D绘图模式。
    
        """
        width, height = self.get_size()
        glEnable(GL_DEPTH_TEST)
        viewport = self.get_viewport_size()
        glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(PLAYER_FOV + self.fov_offset, width / float(height), 0.1, 60.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        x, y = self.rotation
        glRotatef(x, 0, 1, 0)
        glRotatef(-y, math.cos(math.radians(x)), 0, math.sin(math.radians(x)))
        x, y, z = self.position
        if self.crouch:
            glTranslatef(-x, -y+0.2, -z)
        else:
            glTranslatef(-x, -y, -z)
    
    def on_draw(self):
        """由pyglet调用，绘制画布。
    
        """
        self.clear()
        self.set_3d()
        glColor3d(1, 1, 1)
        self.model.batch.draw()
        self.draw_focused_block()
        self.set_2d()
        self.draw_label()
        self.draw_reticle()
    
    def draw_focused_block(self):
        """在准星下方的方块周围绘制黑色边界。
    
        """
        vector = self.get_sight_vector()
        block = self.model.hit_test(self.position, vector)[0]
        if block:
            x, y, z = block
            vertex_data = cube_vertices(x, y, z, 0.51)
            glColor3d(0, 0, 0)
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
            pyglet.graphics.draw(24, GL_QUADS, ('v3f/static', vertex_data))
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    
    def draw_label(self):
        """在屏幕左上角绘制标签。
    
        """
        x, y, z = self.position
        self.label.text = '%02d (%.2f, %.2f, %.2f) %d / %d' % (
            pyglet.clock.get_fps(), x, y, z,
            len(self.model._shown), len(self.model.world))
        self.label.draw()
    
    def draw_reticle(self):
        """在屏幕中央绘制准星。
    
        """
        glColor3d(0, 0, 0)
        self.reticle.draw(GL_LINES)


def setup_fog():
    """配置OpenGL雾效果属性。

    """
    # 启用雾效。雾效会“将雾颜色与每个栅格化的像素片段的着色结果混合”。
    glEnable(GL_FOG)
    # 设置雾颜色。
    glFogfv(GL_FOG_COLOR, (GLfloat * 4)(0.5, 0.69, 1.0, 1))
    # 表示我们对渲染速度和质量没有偏好。
    glHint(GL_FOG_HINT, GL_DONT_CARE)
    # 指定用于计算混合因子的方程式。
    glFogi(GL_FOG_MODE, GL_LINEAR)
    # 雾开始和结束的距离。开始和结束距离越接近，雾在雾区域内越浓密。
    glFogf(GL_FOG_START, 40.0)
    glFogf(GL_FOG_END, 60.0)


def setup():
    """OpenGL基本配置。

    """
    # 设置天空的颜色，以rgba表示。
    glClearColor(0.5, 0.69, 1.0, 1)
    # 启用背面剔除（不渲染）--即对于你来说不可见的面。
    glEnable(GL_CULL_FACE)
    # 将纹理缩小/放大函数设置为GL_NEAREST（曼哈顿距离最近）到指定的纹理坐标。GL_NEAREST“通常比GL_LINEAR更快，
    # 但是它可以产生具有更锐利边缘的纹理图像，因为纹理元素之间的过渡不那么平滑。”
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    setup_fog()


def main():
    window = Window(width=1300, height=730, caption='Minecraft', resizable=True)
    # 隐藏鼠标光标并防止鼠标离开窗口。
    window.set_exclusive_mouse(False)
    setup()
    pyglet.app.run()

main()
