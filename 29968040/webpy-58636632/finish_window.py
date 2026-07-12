import pygame
import pygame.image
import pygame.font
import pygame.transform
from score_number import ScoreNumber


class FontRender:
    def __init__(self, size):
        self.font = pygame.font.SysFont(['simhei', 'notosanscjk'], size)
    
    def render(self, text, color, spacing):
        sf = [self.font.render(i, True, color) for i in text]
        sizes = [i.get_size() for i in sf]
        _len = int(spacing * max(len(text) - 1, 0))
        _w = int(sum([int(s[0]) for s in sizes]))
        # print(_w, _len)
        w = _w + _len
        h = int(max([int(s[1]) for s in sizes]))
        new_sf = pygame.Surface((w, h), pygame.SRCALPHA)
        
        x = 0
        for i in range(len(sf)):
            _w, _h = sizes[i]
            _w, _h = int(_w), int(_h)
            new_sf.blit(sf[i], (x, (h - _h) // 2))
            x += _w + spacing
        return new_sf


class FinishWindow:
    def __init__(self, width, height):
        self.w, self.h = width, height
        self.bg = pygame.transform.scale(pygame.image.load('icon/bg.png'), (width, height))
        self.score_number = ScoreNumber(0, 0, 58)
        self.img = pygame.transform.smoothscale(pygame.image.load('icon/finish.png'), (58, 58))
        self.text2 = FontRender(40).render('游戏结束', (255, 255, 255), 28)
        self.text3 = FontRender(17).render('点击重新开始', (255, 255, 255), 5)

    def render_score(self):
        score_sf = pygame.Surface(self.score_number.get_size(), pygame.SRCALPHA)
        self.score_number.draw(score_sf)
        return score_sf

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))
        score = self.render_score()
        
        y1 = (self.h - 195) // 2
        y2 = y1 + 58 + 40
        y3 = y2 + 40 + 40
        
        x1 = (self.w - score.get_width() - self.img.get_width() - 20) // 2
        x2 = (self.w - self.text2.get_width()) // 2
        x3 = (self.w - self.text3.get_width()) // 2
        
        screen.blit(self.img, (x1, y1))
        screen.blit(score, (x1 + self.img.get_width() + 20, y1))
        screen.blit(self.text2, (x2, y2))
        screen.blit(self.text3, (x3, y3))
        
