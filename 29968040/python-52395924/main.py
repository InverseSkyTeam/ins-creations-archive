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

from render import render, Model, ModelNew, render_new
import pygame
import sys
import numpy as np

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 11)

model = Model(filename="data/african_head/african_head.obj",
              texture_filename="data/african_head/african_head_diffuse.tga")
model1 = Model(filename="data/african_head/african_head_eye_inner.obj",
               texture_filename="data/african_head/african_head_eye_inner_diffuse.tga")
model2 = Model(filename="data/floor.obj", texture_filename="data/floor_diffuse.tga", div_num=1.001)
model3 = Model(filename="data/other/axe.obj", texture_filename="data/other/axe.tga")
model4 = Model(filename="data/other/jinx.obj", texture_filename="data/other/jinx.tga")
model5 = Model(filename="data/other/monkey.obj", texture_filename="data/other/monkey.png")
model7 = ModelNew("data/ht/hutao.obj", 10)

models = [[model, model1, model2], [model3], [model4], [model5], [model7]]
index = 0


def normalize(v):
    # 归一化操作
    unit = np.linalg.norm(v)
    if unit == 0:
        return np.zeros(3, dtype=np.float64)
    return v / unit

angle_x = 0.0
angle_y = 0.0
scale = 1.0
mouse_dragging = False
O2 = False  # 是否开启背面剔除
tx, ty, tz = 0, 0, 0

z_buffer = np.full(screen.get_size(), np.inf, dtype=np.float64)
FPS_list = []
light_dirs = [normalize(np.array([1, 1, 1], dtype=np.float64)),
              normalize(np.array([0, 0, -1], dtype=np.float64))]

while 1:
    FPS = str(round(clock.get_fps()))
    pygame.display.set_caption('fps:' + FPS)
    pygame_events = pygame.event.get()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_dragging = True
            if event.button == 4:
                scale += 0.1 * scale
                scale = min(scale, 10.0)
            if event.button == 5:
                scale -= 0.1 * scale
                scale = max(0.1, scale)
        if event.type == pygame.MOUSEMOTION:
            if mouse_dragging:
                angle_x += event.rel[1]/300
                angle_y += (-event.rel[0])/100
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_dragging = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                O2 = not O2
            if event.key == pygame.K_LEFT:
                index -= 1
                index %= len(models)
            if event.key == pygame.K_RIGHT:
                index += 1
                index %= len(models)
    screen.fill((255, 255, 255))
    z_buffer[:, :] = np.inf
    for _model in models[index]:
        if isinstance(_model, ModelNew):
            render_new(
                _model,
                height=600,
                width=600,
                screen=screen,
                zbuffer=z_buffer,
                angle_x=angle_x,
                angle_y=angle_y+np.pi,
                scale=scale,
                O2=O2,
                tx=tx,
                ty=ty,
                tz=tz,
                light_dirs = light_dirs
            )
            continue
        render(
            _model,
            height=600,
            width=600,
            screen=screen,
            zbuffer=z_buffer,
            angle_x=angle_x,
            angle_y=angle_y,
            scale=scale,
            O2=O2,
            tx=tx,
            ty=ty,
            tz=tz
        )
    pygame.display.flip()
    clock.tick(114514)
