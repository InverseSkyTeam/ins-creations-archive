print('解压图片文件中，请稍等')
import zipfile
with zipfile.ZipFile('Reanim.zip', 'r') as zip_ref:  # 解压骨骼动画图片
    zip_ref.extractall('./')
print('图片文件解压成功')
from PIL import Image
import numpy as np
import pygame, sys, math, data
from numba import jit, prange, njit


# TODO: 左键换动作，右键换僵尸
act_num  = 0
anim_data, act_data, act_name = None, None, None
tx_r, tx_g, tx_b = 1.0, 1.0, 1.0  # 0.95, 0.47, 1.44
num = 0  # 当前在哪一帧
up, down = -1, -1  # 当前动画的起始和结束帧数
Zombie_reanim_name = ['Zombie_catapult', 'Zombie_football', 'Zombie_gargantuar', 'Zombie_paper', 'Zombie_yeti', 'DoomShroom']
Zombie_num = 0
reanims = data.open_reanims(Zombie_reanim_name)


@jit(nopython=True)
def fun_numba(args, x, y):
    x, y = args[0] * x + args[2] * y + args[4], args[1] * x + args[3] * y + args[5]
    return [x, y]


@jit(nopython=True)
def calc_colors_numba(opaque_color, transparent_color, tx_r, tx_g, tx_b, alpha):
    opaque_r, opaque_g, opaque_b = opaque_color
    alpha = transparent_color[3]*alpha/255
    result_r = ((1 - alpha) * opaque_r + alpha * max(min(transparent_color[0] * tx_r, 255), 0))
    result_g = ((1 - alpha) * opaque_g + alpha * max(min(transparent_color[1] * tx_g, 255), 0))
    result_b = ((1 - alpha) * opaque_b + alpha * max(min(transparent_color[2] * tx_b, 255), 0))

    return np.array([int(result_r), int(result_g), int(result_b)])


@jit(nopython=True)
def canvas_transform_numba(screen: np.ndarray, image: np.ndarray, args: np.ndarray, tx_r, tx_g, tx_b, name, alpha):
    if name == 'Zombie_paper_paper':
        tx_r, tx_g, tx_b = 1.0, 1.0, 1.0
    w, h = image.shape[1], image.shape[0]  # 变换前的大小
    div_num = args[0] * args[3] - args[1] * args[2]
    size = list(zip(fun_numba(args, 0, 0),
                    fun_numba(args, 0, h-1),
                    fun_numba(args, w-1, h-1),
                    fun_numba(args, w-1, 0)))
    new_w, new_h = math.ceil(max(size[0]))+1, math.ceil(max(size[1]))+1
    for x in prange(min(new_w, screen.shape[0])):
        for y in prange(min(new_h, screen.shape[1])):
            new_x, new_y = ((x - args[4]) * args[3] - (y - args[5]) * args[2]) / div_num, \
                           (args[0] * (y - args[5]) - args[1] * (x - args[4])) / div_num
            if new_x < 0 or new_x >= w or new_y < 0 or new_y >= h:
                continue
            screen[x, y] = calc_colors_numba(screen[x, y], image[int(new_y), int(new_x)], tx_r, tx_g, tx_b, alpha)


def init_reanim(zname):
    global anim_data, act_data, act_name, act_num, up, down, num
    anim_data, act_data, act_name = reanims[zname]
    act_num = 0
    up, down = act_data[act_name[act_num]]
    num = up


def next_act():
    global act_num, up, down, num, act_name
    act_num += 1
    act_num %= len(act_name)
    up, down = act_data[act_name[act_num]]
    num = up


pygame.init()
init_reanim(Zombie_reanim_name[Zombie_num])
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
while True:
    pygame.display.set_caption('fps:' + str(round(clock.get_fps())))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                next_act()
            if event.button == 3:
                Zombie_num += 1
                Zombie_num %= len(Zombie_reanim_name)
                init_reanim(Zombie_reanim_name[Zombie_num])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # 魅惑
                tx_r, tx_g, tx_b = 0.95, 0.47, 1.44
            if event.key == pygame.K_2:  # 蓝色蒙版,减速效果
                tx_r, tx_g, tx_b = 0.5, 0.5, 2.0
            if event.key == pygame.K_3:  # 减速+加亮效果
                tx_r, tx_g, tx_b = 1.08, 1.08, 1.91
            if event.key == pygame.K_4:  # 魅惑，加亮效果
                tx_r, tx_g, tx_b = 1.46, 1.0, 1.68
            if event.key == pygame.K_0:  # 无效果
                tx_r, tx_g, tx_b = 1.0, 1.0, 1.0
    screen.fill((255, 255, 255))
    self_data = anim_data[num]
    for i in self_data:
        canvas_transform_numba(pygame.surfarray.pixels3d(screen), i[0],
                               np.array([i[1], i[2], i[3], i[4], i[5] + 75, i[6] + 75]),
                               tx_r, tx_g, tx_b, i[7], i[8])
    pygame.display.update()
    clock.tick(30)
    num += 1
    if num == down+1:
        num = up

