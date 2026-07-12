import pygame
from functools import lru_cache as cache


class AD:
    def __init__(self):
        self.img = pygame.image.load('ad.jpg').convert()
    
    @cache(maxsize=32)
    def get_img(self, w, h):
        return pygame.transform.smoothscale(self.img, (w, h))
    
    def render(self, screen, w, h):
        img_w, img_h = self.img.get_size()
        scale = max(w / img_w, h / img_h)
        new_width = int(img_w * scale)
        new_height = int(img_h * scale)
        new_img = self.get_img(new_width, new_height)
        screen.blit(new_img, new_img.get_rect(center=(w//2, h//2)))
