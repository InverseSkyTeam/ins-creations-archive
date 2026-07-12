import typing as t
from numba import jit, njit, prange
import pygame
from PIL import Image, ImageColor


class Canvas:
    def __init__(self, height=500, width=500, screen=None):
        self.height, self.width = height, width
        self.img = pygame.surfarray.pixels3d(screen)  # Image.new("RGBA", (self.height, self.width), (0, 0, 0, 0))
        self.img1 = screen
