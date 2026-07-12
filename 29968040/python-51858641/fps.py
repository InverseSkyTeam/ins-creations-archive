import pygame
from numba import njit
import numpy as np


@njit
def render_numba(screen, FPS_list):
    color = np.array([0, 255, 255], dtype=np.uint8)
    for i in range(74):
        if len(FPS_list) - 1 - i < 0:
            return
        height = FPS_list[len(FPS_list) - 1 - i]
        screen[77-i-1, 15+height:45] = color


def render_fps(screen, FPS_list):
    render_numba(pygame.surfarray.pixels3d(screen), FPS_list)
