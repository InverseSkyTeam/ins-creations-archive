import zipfile
with zipfile.ZipFile('reanim.zip', 'r') as zip_ref:  # 解压骨骼动画图片
    zip_ref.extractall('./reanim')

from PIL import Image
import numpy as np
import pygame, sys, math, data
from numba import jit, prange, njit
# TODO: 修改act_num的值（0到3）或点击屏幕，可以切换动作
act_num = 0


@jit(nopython=True)
def fun_numba(args, x, y, move_skew):
    x, y = args[0] * x + args[2] * y + args[4], args[1] * x + args[3] * y + args[5]
    x += args[6] * y + move_skew
    return [x, y]


@jit(nopython=True)
def calc_colors_numba(opaque_color, transparent_color):
    opaque_r, opaque_g, opaque_b = opaque_color
    alpha = transparent_color[3]/255
    result_r = ((1 - alpha) * opaque_r + alpha * transparent_color[0])
    result_g = ((1 - alpha) * opaque_g + alpha * transparent_color[1])
    result_b = ((1 - alpha) * opaque_b + alpha * transparent_color[2])

    return np.array([int(result_r), int(result_g), int(result_b)])


@jit(nopython=True)
def canvas_transform_numba(screen: np.ndarray, image: np.ndarray, args: np.ndarray):
    w, h = image.shape[1], image.shape[0]  # 变换前的大小
    move_skew = -args[6] * (args[3] * (h - 1) + args[5] - 1)
    div_num = args[0] * args[3] - args[1] * args[2]
    size = list(zip(fun_numba(args, 0, 0, move_skew),
                    fun_numba(args, 0, h-1, move_skew),
                    fun_numba(args, w-1, h-1, move_skew),
                    fun_numba(args, w-1, 0, move_skew)))
    new_w, new_h = math.ceil(max(size[0]))+1, math.ceil(max(size[1]))+1
    for x in prange(min(new_w, screen.shape[0])):
        for y in prange(min(new_h, screen.shape[1])):
            new_x, new_y = x - move_skew - y * args[6], y
            new_x, new_y = ((new_x - args[4]) * args[3] - (new_y - args[5]) * args[2]) / div_num, \
                           (args[0] * (new_y - args[5]) - args[1] * (new_x - args[4])) / div_num
            if new_x < 0 or new_x >= w or new_y < 0 or new_y >= h:
                continue
            screen[x, y] = calc_colors_numba(screen[x, y], image[int(new_y), int(new_x)])


anim_data = data.anim_data


pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
up, down = [(0, 20), (21, 50), (51, 86), (87, 104)][act_num]
num = up
while True:
    pygame.display.set_caption('fps:' + str(round(clock.get_fps())))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            act_num += 1
            act_num %= 4
            up, down = [(0, 20), (21, 50), (51, 86), (87, 104)][act_num]
            num = up
    screen.fill((255, 255, 255))
    self_data = anim_data[num]
    for i in self_data:
        canvas_transform_numba(pygame.surfarray.pixels3d(screen), i[0],
                               np.array([i[1], i[2], -i[3], i[4], i[5] + 25, i[6] + 25, -i[7]]))
    pygame.display.update()
    clock.tick(30)
    if num != 104:
        num += 1
    if num == down+1:
        num = up

