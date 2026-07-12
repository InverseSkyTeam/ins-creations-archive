import pygame
import pygame.locals
import pygame.key
from .scroll_bar import VScrollBar, HScrollBar
from .font_renderer import FontRenderer
from .text_manager import TextManager
from .event_manager import EventManager
from .renderer import Renderer
from .cursor import Cursor
from .selected_manager import SelectedManager
from .select_menu import SelectMenu


class TextInput:
    def __init__(self, font, font_size, font_color, line_height, rect, init_text) -> None:
        # 字体
        self.font = FontRenderer(font, font_size, font_color, line_height)

        # 位置
        self.rect: pygame.Rect = rect  # 输入框的 Rect

        # 光标以及文字存储
        self.text = TextManager(init_text, self.font)
        self.cursor = Cursor(self.text)
        self.selected_manager = SelectedManager(self.rect)
        self.select_menu = SelectMenu(self.selected_manager)

        # 滚动条
        self.vScroll = VScrollBar(self.rect)
        self.hScroll = HScrollBar(self.rect)

        # 事件处理
        self.event = EventManager(self.rect, self.vScroll, self.hScroll, self.font,
                                  self.cursor, self.selected_manager, self.select_menu)

        # 渲染
        self.render = Renderer(self.text, self.vScroll, self.hScroll, self.event,
                               self.font, self.cursor, self.selected_manager, self.select_menu)

        self.select_menu.set_button_data({
            '复制': self.event.handle_copy,
            '粘贴': self.event.handle_paste,
            '全选': self.event.handle_select_all,
            '剪切': self.event.handle_cut
        })

    def display(self, screen, mouse_pos):
        self.render.render(screen, self.rect, mouse_pos)

    def debug(self):
        width = [self.font.pre_render_string(string) for string in self.text.text]
        assert self.text.line_width == width
        assert self.text.max_line_width == max(width)

    def handle_events(self, events, mouse_pos):
        cx, cy = self.cursor.get_screen_pos()
        tx = self.rect.x - self.hScroll.offset + cx
        ty = self.rect.y - self.vScroll.offset + cy + self.font.line_height
        pygame.key.set_text_input_rect(pygame.Rect(tx, ty, 1000, 40))
        self.event.handle_events(events, mouse_pos)
