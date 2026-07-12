import pygame
import itertools
import bisect
from .text_manager import TextManager
from .scroll_bar import VScrollBar, HScrollBar
from .event_manager import EventManager
from .font_renderer import FontRenderer
from .cursor import Cursor
from .util import surface_concatenate


class Renderer:
    def __init__(self, text, v_scroll, h_scroll, event, font, cursor):
        self.text: TextManager = text
        self.vScroll: VScrollBar = v_scroll
        self.hScroll: HScrollBar = h_scroll
        self.event: EventManager = event
        self.font: FontRenderer = font
        self.cursor: Cursor = cursor

        self.cursor_pos = (0, 0)

    def get_ime_editing_surface(self):
        if self.event.is_ime_editing():
            return self.font.render_underline_text(self.event.ime_editing_text, self.event.ime_editing_pos)
        return pygame.Surface((0, self.font.font_size), pygame.SRCALPHA), 0

    def render_cursor(self, surface, x, y):
        pygame.draw.line(surface, (0,) * 3, (x, y), (x, y + self.font.line_height))

    def render_string(self, surface, text, x, y, line_index, ime_editing, ime_editing_pos):
        offset_height = self.font.offset_height  # 渲染时的偏移量
        text_width = [self.font.rendered_text_width[char] for char in text]
        text_surface = [self.font.rendered_text_surface[char] for char in text]

        cursor_row, cursor_col = self.cursor.get_cursor_pos()
        if line_index == cursor_row and self.event.is_ime_editing():
            if 0 <= cursor_col < len(text_width):
                text_width[cursor_col] += ime_editing.get_width()
                text_surface[cursor_col] = surface_concatenate(ime_editing, text_surface[cursor_col])
            else:
                text_width.append(ime_editing.get_width())
                text_surface.append(ime_editing)

        text_width_acc = list(itertools.accumulate(text_width))
        s_index = bisect.bisect_left(text_width_acc, -x)
        e_index = min(bisect.bisect_left(text_width_acc, surface.get_width() - x, s_index) + 1, len(text_width_acc))

        surface.blits((text_surface[i], (x + text_width_acc[i] - text_width[i], y + offset_height))
                      for i in range(s_index, e_index))

        if line_index == self.cursor.row and self.event.focus:
            offset_x, _ = self.cursor.get_screen_pos()
            cursor_x = x + offset_x + ime_editing_pos
            self.render_cursor(surface, cursor_x, y)

    def render(self, screen, rect):
        cache_surface = pygame.Surface(rect.size, pygame.SRCALPHA)  # 缓存渲染结果的画布
        
        hidden_lines_num = self.vScroll.offset // self.font.line_height  # 被隐藏的行数
        hidden_lines_height = hidden_lines_num * self.font.line_height  # 被隐藏的行的总高度
        remain_lines_num = len(self.text.text) - hidden_lines_num  # 剩余的行数
        
        x, y = -self.hScroll.offset, -self.vScroll.offset + hidden_lines_height  # 文字在渲染区域内的左上角纵坐标（渲染起始纵坐标）
        
        show_lines_num = min((rect.h - y) // self.font.line_height + 1, remain_lines_num)  # 能被显示的行数
        end_line_index = hidden_lines_num + show_lines_num
        
        ime_editing, ime_editing_pos = self.get_ime_editing_surface()

        for i in range(hidden_lines_num, end_line_index):
            self.render_string(cache_surface, self.text.text[i], x, y, i, ime_editing, ime_editing_pos)
            y += self.font.line_height

        max_width = max(self.text.max_line_width, self.text.get_line_width(self.cursor.row) + ime_editing.get_width())

        self.vScroll.update_content_length(len(self.text.text) * self.font.line_height)
        self.hScroll.update_content_length(max_width+1)
        self.vScroll.render(cache_surface)
        self.hScroll.render(cache_surface)
        screen.blit(cache_surface, rect)
