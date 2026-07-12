import pygame
import pygame.locals
import pygame.key
from .scroll_bar import VScrollBar, HScrollBar
from .font_renderer import FontRenderer
from .event_manager import EventManager
from .renderer import Renderer
from .cursor import Cursor
from .selected_manager import SelectedManager
from .select_menu import SelectMenu
from .tool import Tool
from .keyboard import KeyBoard
from .shortcut import Shortcut
from .cursor_blink import CursorBlink


class TextInput:
    text_input_group = []

    def __init__(self, screen_rect, font, font_size, font_color, line_height, rect, init_text, multi_lines=True) -> None:
        # 是否是多行文本框
        self.multi_lines = multi_lines
        if not self.multi_lines:
            init_text = init_text.replace('\n', ' ')

        # 字体
        self.font = FontRenderer(font, font_size, font_color, line_height)

        # 位置
        self.rect: pygame.Rect = rect  # 输入框的 Rect

        # 光标以及文字存储
        self.cursor = Cursor(init_text, self.font)
        self.cursor_blink = CursorBlink()  # 光标闪动
        self.selected_manager = SelectedManager(self.rect)
        self.select_menu = SelectMenu(self.selected_manager, screen_rect)

        # 滚动条
        self.vScroll = VScrollBar(self.rect)
        self.hScroll = HScrollBar(self.rect)

        # 基本功能的封装
        self.tool = Tool(self.rect, self.vScroll, self.hScroll,
                         self.font, self.cursor, self.selected_manager,
                         self.cursor_blink, self.multi_lines)

        # 内置键盘事件
        self.keyboard = KeyBoard(self.tool)

        self.shortcut = Shortcut(self.tool, self.select_menu)

        # 事件处理
        self.event = EventManager(self, self.tool, self.select_menu, self.keyboard, self.shortcut)

        # 渲染
        self.render = Renderer(self.tool, self.event, self.select_menu)

        self.text_input_group.append(self)

    def display(self, screen, mouse_pos):
        self.select_menu.update()
        self.render.render(screen, self.rect, mouse_pos)

    def debug(self):
        width = [self.font.pre_render_string(string) for string in self.cursor.text]
        assert self.cursor.line_width == width
        assert self.cursor.max_line_width == max(width)

    def handle_events(self, events, mouse_pos):
        cx, cy = self.cursor.get_screen_pos()
        tx = self.rect.x - self.hScroll.offset + cx
        ty = self.rect.y - self.vScroll.offset + cy + self.font.line_height
        if self.event.focus:
            pygame.key.set_text_input_rect(pygame.Rect(tx, ty, 1000, 40))
        self.event.handle_events(events, mouse_pos)
