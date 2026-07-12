import zipfile
with zipfile.ZipFile('reanim.zip', 'r') as zip_ref:  # 解压骨骼动画图片
    zip_ref.extractall('./reanim')

from PIL import Image
import numpy as np
import pygame, sys, math, data
# TODO: 修改act_num的值（0到3），可以切换动作
act_num = 0


def create_pos(a, b, c, d):
    #生成包围框（[a,b)[c,d)）里所有的坐标
    arr = np.mgrid[a:b, c:d].reshape(2, -1)
    return arr


def calc_new_size(args, w, h, screen):
    a, b, c, d, e, f = args[0]
    fun = lambda x, y, a, b, c, d, e, f: np.array([a*x+c*y+e, b*x+d*y+f])
    pos = np.array([fun(0, 0, a, b, c, d, e, f), fun(0, h-1, a, b, c, d, e, f), fun(w-1, h-1, a, b, c, d, e, f), fun(w-1, 0, a, b, c, d, e, f)])
    for a1, b1, c1, d1, e1, f1 in args[1:]:
        for i in range(4):
            pos[i] = fun(pos[i][0], pos[i][1], a1, b1, c1, d1, e1, f1)
    # pygame.draw.polygon(screen, (255, 0, 0), pos)
    return np.maximum(np.max(pos, axis = 0), 0).tolist()


def calc_colors(opaque_color, transparent_color):
    opaque_r, opaque_g, opaque_b = opaque_color[:, 0], opaque_color[:, 1], opaque_color[:, 2]
    alpha = transparent_color[:, 3]/255
    result_r = ((1 - alpha) * opaque_r + alpha * transparent_color[:, 0]).astype(int)
    result_g = ((1 - alpha) * opaque_g + alpha * transparent_color[:, 1]).astype(int)
    result_b = ((1 - alpha) * opaque_b + alpha * transparent_color[:, 2]).astype(int)
    result_color = np.column_stack((result_r, result_g, result_b))

    return result_color


def canvas_transform(screen, image, args, sc):
    w, h = image.shape[1], image.shape[0]  # 变换前的大小
    fun = lambda x, y, a, b, c, d, e, f: np.array([a * x + c * y + e, b * x + d * y + f])
    a, b, c, d, e, f = args[0]
    _, y1 = fun(0, h - 1, a, b, c, d, e, f)
    a, b, c, d, e, f = args[1]
    args[1][4] = -(fun(0, y1 - 1, a, b, c, d, e, f)[0])
    new_size = calc_new_size(args, w, h, sc)  # 变换后的大小
    new_w, new_h = math.ceil(new_size[0])+1, math.ceil(new_size[1])+1
    new_w, new_h = min(new_w, screen.shape[0]), min(new_h, screen.shape[1])
    all_x, all_y = create_pos(0, new_w, 0, new_h)
    new_x, new_y = all_x, all_y
    for a, b, c, d, e, f in args[-1::-1]:
        div_num = a*d-b*c  # 提取相同的除数，减少计算时间
        new_x, new_y = ((new_x-e)*d-(new_y-f)*c)/div_num, \
                        (a*(new_y-f)-b*(new_x-e))/div_num
    mask = (new_x >= 0) & (new_x < w) & (new_y >= 0) & (new_y < h)
    screen[all_x[mask], all_y[mask]] = calc_colors(screen[all_x[mask], all_y[mask]], image[new_y.astype(int)[mask], new_x.astype(int)[mask]])


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
    screen.fill((255, 255, 255))
    self_data = anim_data[num]
    for i in self_data:
        # print(i[0])

        canvas_transform(pygame.surfarray.pixels3d(screen), i[0],
                         [[i[1], i[2], -i[3], i[4], i[5]+25, i[6]+25],
                          [1, 0, (-i[7] if i[7] is not None else 0), 1, 0, 0]], screen)

    '''screen.blit(pygame.image.load('img1.png'), (0, 0))
    canvas_transform(pygame.surfarray.pixels3d(screen), image1, \
                    ((1,0.5,-0.5,1,30,10),), screen)
    canvas_transform(pygame.surfarray.pixels3d(screen), image1, \
                    ((1,0.5,-0.5,1,30,10), (1,0.5,-0.5,1,30,10)), screen)
    '''
    pygame.display.update()
    clock.tick(30)
    if num != 104:
        num += 1
    if num == down+1:
        num = up

