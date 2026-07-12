import pygame
import sys
import numpy as np
from numba import njit

pygame.init()
screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
font_title = pygame.font.SysFont("SimHei", 25)


def pygame_render():
    for x in range(0, 700, 3):
        for y in range(0, 500, 3):
            pygame.draw.rect(screen, (int(x*0.3), int(y*0.3), int(x*0.3)), (x, y, 3, 3))


@njit
def np_render(np_screen):
    for x in range(0, 700, 3):
        for y in range(0, 500, 3):
            np_screen[x:x+3, y:y+3] = np.array([int(x*0.3), int(y*0.3), int(x*0.3)], dtype=np.uint8)


mode = True
x = font_title.render('pygame绘制', True, (255,)*3)
y = font_title.render('np+numba绘制', True, (255,)*3)
while True:
    pygame.display.set_caption('fps:' + str(round(clock.get_fps())))
    mouse_pressed = pygame.mouse.get_pressed()[0]
    mouse_pos = pygame.mouse.get_pos()
    pygame_events = pygame.event.get()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mode = not mode
    if mode:
        pygame_render()
        screen.blit(x, (0, 0))
    else:
        screen_np = pygame.surfarray.pixels3d(screen)
        np_render(screen_np)
        del screen_np
        screen.blit(y, (0, 0))
    pygame.display.update()
    clock.tick(114514)
