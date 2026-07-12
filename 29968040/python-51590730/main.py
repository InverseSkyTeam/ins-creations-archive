from render import render, Model
import pygame
import sys
import numpy as np

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

model = Model(filename="data/african_head/african_head.obj",
              texture_filename="data/african_head/african_head_diffuse.tga")
model1 = Model(filename="data/african_head/african_head_eye_inner.obj",
               texture_filename="data/african_head/african_head_eye_inner_diffuse.tga")
# model2 = Model(filename="data/floor.obj", texture_filename="data/floor_diffuse.tga")

angle_x = 0.0
angle_y = 0.0
scale = 1.0
mouse_dragging = False
mode = 1  # 是否开启线框模式
O2 = False  # 是否开启背面剔除

while 1:
    pygame.display.set_caption('fps:' + str(round(clock.get_fps())))
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
    zbuffer = np.full(screen.get_size(), np.inf, dtype=np.float64)
    render(
        model,
        height=600,
        width=600,
        screen=screen,
        zbuffer=zbuffer,
        angle_x=angle_x,
        angle_y=angle_y,
        scale=scale,
        mode=mode,
        O2=O2
    )
    render(
        model1,
        height=600,
        width=600,
        screen=screen,
        zbuffer=zbuffer,
        angle_x=angle_x,
        angle_y=angle_y,
        scale=scale,
        mode=mode,
        O2=O2
    )

    pygame.display.flip()
    clock.tick(114514)
