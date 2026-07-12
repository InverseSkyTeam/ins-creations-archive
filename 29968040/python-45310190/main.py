from PIL import Image
import numpy as np
import pygame, sys, math

def create_pos(a, b, c, d):
    #生成包围框（[a,b)[c,d)）里所有的坐标
    arr = np.mgrid[a:b, c:d].reshape(2, -1)
    return arr

def calc_new_size(a, b, c, d, e, f, w, h):
    fun = lambda x, y: np.array([a*x+c*y+e, b*x+d*y+f])
    pos = np.array([fun(0, 0), fun(0, h-1), fun(w-1, h-1), fun(w-1, 0)])
    return np.maximum(np.max(pos, axis = 0), 0).tolist()

def canvas_transform(screen, image, a, b, c, d, e, f):
    w, h = image.shape[1], image.shape[0]  # 变换前的大小
    new_w, new_h = calc_new_size(a, b, c, d, e, f, w, h)  # 变换后的大小
    new_w, new_h = math.ceil(new_w), math.ceil(new_h)
    div_num = a*d-b*c  # 提取相同的除数，减少计算时间
    all_x, all_y = create_pos(0, new_w, 0, new_h)
    new_x = ((all_x-e)*d-(all_y-f)*c)/div_num
    new_y = (a*(all_y-f)-b*(all_x-e))/div_num
    mask = (new_x >= 0) & (new_x < w) & (new_y >= 0) & (new_y < h)
    screen[all_x[mask], all_y[mask]] = image[new_y.astype(int)[mask], new_x.astype(int)[mask], :3]

pygame.init()
screen = pygame.display.set_mode((600,600))
image = np.array(Image.open("img1.png"))
a, b, c, d, e, f = 1, 0.3, -0.5, 1, 150, 10
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    canvas_transform(pygame.surfarray.pixels3d(screen), image, a, b, c, d, e, f)
    pygame.display.update()
