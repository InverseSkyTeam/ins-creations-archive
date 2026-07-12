import typing as t
from numba import jit, njit, prange
import pygame
from PIL import Image, ImageColor

class Canvas:
    def __init__(self, filename=None, height=500, width=500, screen=None):
        self.filename = filename
        self.height, self.width = height, width
        self.img = pygame.surfarray.pixels3d(screen)  # Image.new("RGBA", (self.height, self.width), (0, 0, 0, 0))

    def draw(self, dots, color: t.Union[tuple, str]):
        if isinstance(color, str):
            color = ImageColor.getrgb(color)
        if isinstance(dots, tuple):
            dots = [dots]
        for dot in dots:
            self.img[dot[0], dot[1]] = color
