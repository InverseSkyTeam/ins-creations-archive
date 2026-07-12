import pygame
import pygame.locals
import pygame.key
from .scroll_bar import VScrollBar, HScrollBar
from .font_renderer import FontRenderer
from .text_manager import TextManager
from .event_manager import EventManager
from .renderer import Renderer
from .cursor import Cursor


class TextInput:
    def __init__(self, font, font_size, font_color, line_height, rect, init_text) -> None:
        # 字体
        self.font = FontRenderer(font, font_size, font_color, line_height)

        # 光标以及文字存储
        self.text = TextManager(init_text, self.font)
        self.cursor = Cursor(self.text)

        # 位置
        self.rect: pygame.Rect = rect  # 输入框的 Rect

        # 滚动条
        self.vScroll = VScrollBar(self.rect)
        self.hScroll = HScrollBar(self.rect)

        # 事件处理
        self.event = EventManager(self.rect, self.vScroll, self.hScroll, self.font, self.cursor)

        # 渲染
        self.render = Renderer(self.text, self.vScroll, self.hScroll, self.event, self.font, self.cursor)

    def display(self, screen):
        self.render.render(screen, self.rect)

    def debug(self):
        ans = max(self.font.pre_render_string(string) for string in self.text.text)
        assert self.text.max_line_width == ans

    def handle_events(self, events):
        cursor_pos = self.rect.move(*self.render.cursor_pos).move(0, self.font.line_height).topleft
        pygame.key.set_text_input_rect(pygame.Rect(*cursor_pos, 320, 40))
        self.event.handle_events(events, self.rect)
