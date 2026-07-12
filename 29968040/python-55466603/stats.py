import pygame
import time
from numba import njit
import numpy as np


class Stats:
    def __init__(self, clock):
        self.clock = clock
        self.font = pygame.font.SysFont(['Helvetica', 'Arial', 'sans-serif'], 11, bold=True)
        self.min_fps, self.max_fps = 114514, -1
        self.start_time = time.time()
        self.fps_list = [30] * 74
        self.first_fps = True

        _sf = pygame.Surface((1, 1))
        _sf.fill((17, 17, 51))
        self.color = pygame.surfarray.array2d(_sf.convert())[0, 0]

    @staticmethod
    @njit(looplift=True)
    def render_graph(screen, fps_list, color):
        for i in range(len(fps_list)):
            screen[3+i, 15:15+fps_list[i]] = color

    def render(self, screen):
        curv_time = time.time()
        curv_fps = round(self.clock.get_fps())
        self.min_fps = min(self.min_fps, curv_fps)
        self.max_fps = max(self.max_fps, curv_fps)

        pygame.draw.rect(screen, (0, 0, 34), (0, 0, 80, 48))
        pygame.draw.rect(screen, (0, 255, 255), (3, 15, 74, 30))
        text = self.font.render(f'{curv_fps} FPS ({self.min_fps}-{self.max_fps})', True, (0, 255, 255))
        screen.blit(text, text.get_rect(midleft=(3, 15 // 2)))
        if curv_time > self.start_time + 1:
            self.start_time = curv_time
            self.fps_list.append(min(30, int(30 - (min(curv_fps, 100) / 100) * 30)))
            self.fps_list.pop(0)
        self.render_graph(pygame.surfarray.pixels2d(screen),
                          np.array(self.fps_list, dtype=np.uint8), self.color)
