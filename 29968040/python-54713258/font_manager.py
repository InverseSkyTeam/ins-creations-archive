import pygame


class FontManager:
    def __init__(self):
        self.font_cache = {}
    
    def SysFont(self, name, size):
        if name in self.font_cache and size in self.font_cache[name]:
            return self.font_cache[name][size]
        if name not in self.font_cache:
            self.font_cache[name] = {}
        _font = pygame.font.SysFont(name, size)
        self.font_cache[name][size] = _font
        return _font
    
    def Font(self, name, size):
        if name in self.font_cache and size in self.font_cache[name]:
            return self.font_cache[name][size]
        if name not in self.font_cache:
            self.font_cache[name] = {}
        _font = pygame.font.Font(name, size)
        self.font_cache[name] = {}
        self.font_cache[name][size] = _font
        return _font
