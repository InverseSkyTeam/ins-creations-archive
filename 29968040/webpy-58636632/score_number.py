import ball_run
import pygame
import pygame.image
import pygame.transform


class ScoreNumber:
    def __init__(self, x, y, height):
        self.x, self.y = x, y
        self.img = pygame.image.load('icon/number1.png')
        _w, _h = self.img.get_size()
        self.img = pygame.transform.smoothscale(self.img, (round(_w / _h * height), height))
        self.w = self.img.get_width() / 10
        self.h = self.img.get_height()
    
    def get_sf(self, num):
        sf = pygame.Surface((round(self.w), self.h), pygame.SRCALPHA)
        sf.blit(self.img, (round(-num * self.w), 0))
        return sf.convert_alpha()
    
    def draw(self, screen):
        x = self.x
        for n in str(ball_run.score):
            sf = self.get_sf(int(n))
            screen.blit(sf, (x, self.y))
            x += self.w - 5
    
    def get_size(self):
        text_len = len(str(ball_run.score))
        return self.w * text_len - 5 * max(text_len - 1, 0), self.h
        