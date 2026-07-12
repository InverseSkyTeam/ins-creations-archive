from .merge_surface import MergeSurface
import pygame.image


class BallData:
    def __init__(self, radius, cor, img, merge_img):
        self.radius = radius
        self.cor = cor
        self.img = pygame.image.load(img)
        self.merge_img = MergeSurface(pygame.image.load(merge_img), radius)
