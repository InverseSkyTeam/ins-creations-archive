import pygame


class FontManager:
    def __init__(self, font_regular, font_bold, font_mono):
        self.font_regular_name = font_regular
        self.font_bold_name = font_bold
        self.font_mono_name = font_mono
        self.font_regular_cache = {}  # 一般字体
        self.font_bold_cache = {}  # 粗体
        self.font_mono_cache = {}  # 等款字体
    
    def get_regular_font(self, size):
        if size in self.font_regular_cache:
            return self.font_regular_cache[size]
        _font = pygame.font.Font(self.font_regular_name, size)
        self.font_regular_cache[size] = _font
        return _font
    
    def get_bold_font(self, size):
        if size in self.font_bold_cache:
            return self.font_bold_cache[size]
        _font = pygame.font.Font(self.font_bold_name, size)
        self.font_bold_cache[size] = _font
        return _font
    
    def get_mono_font(self, size):
        if size in self.font_mono_cache:
            return self.font_mono_cache[size]
        _font = pygame.font.Font(self.font_mono_name, size)
        self.font_mono_cache[size] = _font
        return _font
    
    def get_font(self, font_size, font_style):
        if 'code' in font_style:  # 等宽代码体:
            font = self.get_mono_font(font_size)
        elif 'strong' in font_style:  # 粗体
            font = self.get_bold_font(font_size)
        else:
            font = self.get_regular_font(font_size)
        font.set_italic('em' in font_style)
        font.set_strikethrough('s' in font_style)
        return font
        
