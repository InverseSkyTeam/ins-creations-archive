import os
import sys
def get_py_path():
    return sys.executable
def install_library():
    try:
        import numba
    except ImportError:
        print("检测到环境尚未配置完全，正在自动配置（第一次运行常见）")
        import subprocess
        try:
            subprocess.check_call([get_py_path(), '-m', 'pip', 'install', "numba==0.56.4"])
            print("\n环境配置成功！请重新运行程序\033[8m;")
            sys.exit(0)
        except subprocess.CalledProcessError:
            print("\n环境配置失败！\033[8m;")
            sys.exit(1)
install_library()

from render import render, Model, CubeModel, ModelNew, render_new
from fps import render_fps
import pygame
import sys
import numpy as np

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 11)

model13 = ModelNew("data/kq/刻晴.obj", 10)

angle_x = 0.0
angle_y = np.pi
scale = 1.0
mouse_dragging = False
mode = 1  # 是否开启线框模式
O2 = False  # 是否开启背面剔除
tx, ty, tz = 0, 0, 0

z_buffer = np.full(screen.get_size(), np.inf, dtype=np.float64)
FPS_list = []

while 1:
    FPS = str(round(clock.get_fps()))
    pygame.display.set_caption('fps:' + FPS)
    # FPS_list.append(int(30*(1-min(round(clock.get_fps()), 120)/120)))
    pygame_events = pygame.event.get()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_dragging = True
            if event.button == 4:
                scale += 0.1
                scale = min(scale, 2.0)
            if event.button == 5:
                scale -= 0.1
                scale = max(0.1, scale)
        if event.type == pygame.MOUSEMOTION:
            if mouse_dragging:
                angle_x += event.rel[1]/300
                angle_y += (-event.rel[0])/100
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_dragging = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                mode = not mode
            if event.key == pygame.K_o:
                O2 = not O2

    screen.fill((255, 255, 255))
    z_buffer[:, :] = np.inf
    render_new(
        model13,
        height=600,
        width=600,
        screen=screen,
        zbuffer=z_buffer,
        angle_x=angle_x,
        angle_y=angle_y,
        mode=mode,
        scale=scale,
        O2=O2,
        tx=tx,
        ty=ty,
        tz=tz
    )
    '''pygame.draw.rect(screen, (0, 0, 34), (0, 0, 80, 48))
    pygame.draw.rect(screen, (17, 17, 51), (3, 15, 74, 30))
    screen.blit(font.render(FPS + ' FPS', True, (0, 255, 255)), (3, 2))
    render_fps(screen, np.array(FPS_list, dtype=np.uint8))'''

    pygame.display.flip()
    clock.tick(114514)
