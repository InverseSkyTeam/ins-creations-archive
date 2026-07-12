import pygame


class FontRenderer:
    def __init__(self, font, font_size, font_color, line_height):
        self.font = font  # 字体
        self.font_size = font_size  # 字体大小
        self.font_color = font_color  # 字体颜色
        self.line_height = line_height  # 行高
        self.offset_height = (self.line_height - self.font.size('j')[1]) // 2

        self.rendered_text_surface = {}  # 缓存已渲染的文字的画布
        self.rendered_text_width = {}  # 缓存已渲染的文字的画布的宽度

    def pre_render_string(self, string):  # 预渲染单行文本，并存储进缓存，返回文本宽度
        width = 0
        for char in string:
            if char not in self.rendered_text_surface:
                self.rendered_text_surface[char] = self.font.render(char, True, self.font_color).convert_alpha()
                self.rendered_text_width[char] = self.rendered_text_surface[char].get_width()
            width += self.rendered_text_width[char]
        return width

    def pre_render_text(self, text):  # 预渲染多行文本，并存储进缓存，返回文本宽度
        return [self.pre_render_string(line) for line in text.split('\n')]

    def render_underline_text(self, text, pos):  # 绘制输入法候选框的文字（pos是光标位置）
        # 渲染文本
        text_surface = self.font.render(text, True, self.font_color)
        text_rect = text_surface.get_rect()

        # 绘制下划线
        pygame.draw.line(text_surface, (0, ) * 3, (0, text_rect.bottom - 1), (text_rect.right, text_rect.bottom - 1))

        return text_surface, max(self.font.size(text[:pos])[0] - 1, 0)
