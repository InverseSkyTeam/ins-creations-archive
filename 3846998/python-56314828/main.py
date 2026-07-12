"""
除pygame-ce文档外几乎没有参考任何资料写成
"""

import pygame
import os, sys

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("fndrawer.py")
s_width = screen.get_width()
s_height = screen.get_height()
need_quit = False
clock = pygame.Clock()
dt = 0
center_x, center_y = 0, 0
zoom = 1
font = pygame.font.SysFont("Consolas", 15)


def render_font(text: str):
    return font.render(text, True, "black")


def shift(x, y):
    return (x - center_x) * zoom + s_width / 2, (-y - center_y) * zoom + s_height / 2


def coord_add(a, b):
    return a[0] + b[0], a[1] + b[1]


funcs = [
    lambda x: x,
    lambda x: x * x,
    lambda x: x + 1 / x,
    lambda x: x * x * x,
]


while not need_quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            need_quit = True
    
    screen.fill("white")

    # pygame.draw.circle(screen, "black", (center_x, center_y), 10)
    # pygame.draw.circle(screen, "white", (center_x, center_y), 9)

    # x-axis
    pygame.draw.line(screen, "black", shift(-200, 0), shift(200, 0))
    pygame.draw.line(screen, "black", shift(200, 0), coord_add(shift(200, 0), (-5, 5)))
    pygame.draw.line(screen, "black", shift(200, 0), coord_add(shift(200, 0), (-5, -5)))
    screen.blit(render_font("x"), coord_add(shift(200, 0), (5, -7.5)))
    # y-axis
    pygame.draw.line(screen, "black", shift(0, 150), shift(0, -150))
    pygame.draw.line(screen, "black", shift(0, 150), coord_add(shift(0, 150), (-5, 5)))
    pygame.draw.line(screen, "black", shift(0, 150), coord_add(shift(0, 150), (5, 5)))
    screen.blit(render_font("y"), coord_add(shift(0, 150), (-3.75, -20)))
    # 0-point
    screen.blit(render_font("0"), coord_add(shift(0, 0), (-10, 2.5)))
    # texts
    mode_text = render_font("Zoom: %.2f, Center: (%.2f, %.2f)"%(zoom, center_x, center_y))
    screen.blit(mode_text, (5, 380))
    # graphs
    for f in funcs:
        last = None
        dx = 2
        x = -2000
        while x <= 2000:
            try:
                y = f(x / 100)
                if last is not None:
                    last_draw = last[0] / 10, last[1] * 10
                    cur_draw = x / 10, y * 10
                    # print(x)
                    pygame.draw.line(screen, "black", shift(*last_draw), shift(*cur_draw))
                last = x, y
            except:
                y = 0
                last = None
            x += dx

    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_k]:
        center_y -= 300 * dt / zoom
    if keys[pygame.K_j]:
        center_y += 300 * dt / zoom
    if keys[pygame.K_h]:
        center_x -= 300 * dt / zoom
    if keys[pygame.K_l]:
        center_x += 300 * dt / zoom
    if keys[pygame.K_q]:
        need_quit = True
    if keys[pygame.K_MINUS]:
        if zoom - dt * 3 > 0.5:
            zoom -= dt * 3
    if keys[pygame.K_EQUALS]:
        zoom += dt * 3

    dt = clock.tick(60) / 1000
    # print(dt)
    
pygame.quit()
