import pygame.transform
import pygame


modelSize = 5


class MergeSurface:
    def __init__(self, img, radius):
        w = h = radius * 2.6
        self.data = [self.load_img(img, w, h, i) for i in range(5)]

    def load_img(self, img, w, h, index):
        scale = (modelSize - index) / modelSize
        w, h = int(w * scale), int(h * scale)
        _w, _h = round(w * 1.42), round(h * 1.42)
        sf = pygame.transform.scale(img, (w, h))
        res = pygame.Surface((_w, _h), pygame.SRCALPHA)
        res.blit(sf, ((_w - w) // 2, (_h - h) // 2))
        return res
