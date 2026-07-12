import pygame
import itertools
import bisect
from .tool import Tool
from .event_manager import EventManager
from .util import surface_concatenate
from .select_menu import SelectMenu


SELECTED_COLOR = (0xb5, 0xd5, 0xff)


class Renderer:
    def __init__(self, tool, event, select_menu):
        self.tool: Tool = tool
        self.vScroll = tool.vScroll
        self.hScroll = tool.hScroll
        self.event: EventManager = event
        self.font = tool.font
        self.cursor = tool.cursor
        self.cursor_blink = tool.cursor_blink
        self.selected_manager = tool.selected_manager
        self.select_menu: SelectMenu = select_menu

    def get_ime_editing_surface(self):
        if self.event.is_ime_editing():
            return self.font.render_underline_text(self.event.ime_editing_text, self.event.ime_editing_pos)
        return pygame.Surface((0, self.font.font_size), pygame.SRCALPHA), 0

    def render_cursor(self, surface, sx, sy, ime_editing_pos, line_index):
        if line_index != self.cursor.row or not self.event.focus:
            return
        # sx: 当前行起始 x 坐标    sy: 当前行起始 y 坐标  （均相对显示区域）
        offset_x, offset_y = self.cursor.get_screen_pos()
        cursor_x = sx + offset_x + ime_editing_pos
        if ime_editing_pos != 0:
            self.tool._move_cursor_in_rect(offset_x + ime_editing_pos, offset_y)
        if self.cursor_blink.get_blink:
            pygame.draw.line(surface, (0,) * 3, (cursor_x, sy), (cursor_x, sy + self.font.line_height - 1))

    def render_img_editing(self, line_index, ime_editing, text_width, text_surface):  # 绘制输入法候选框文字
        cursor_row, cursor_col = self.cursor.get_cursor_pos()
        if line_index != cursor_row or not self.event.is_ime_editing():
            return

        if 0 <= cursor_col < len(text_width):
            text_width[cursor_col] += ime_editing.get_width()
            text_surface[cursor_col] = surface_concatenate(ime_editing, text_surface[cursor_col])
        else:  # 该行为空或光标在该行末尾
            text_width.append(ime_editing.get_width())
            text_surface.append(ime_editing)

    @staticmethod
    def get_col_x(col, text_width_acc):  # 获取某行中，光标在col时的x坐标
        if col == 0:
            return 0
        return text_width_acc[col - 1]

    def draw_selected_rect(self, surface, sx, ex, y):
        if sx > ex:
            return
        pygame.draw.rect(surface, SELECTED_COLOR, (sx, y, ex-sx, self.font.line_height))

    def render_selected(self, surface, sx, sy, text_width_acc, line_index):
        if not self.selected_manager.line_is_selecting(line_index):
            return
        begin, end = self.selected_manager.begin, self.selected_manager.end
        begin, end = (begin, end) if begin <= end else (end, begin)
        s_x = sx + self.get_col_x(begin[1], text_width_acc) if line_index == begin[0] else 0
        e_x = sx + self.get_col_x(end[1], text_width_acc) if line_index == end[0] else surface.get_width()

        self.draw_selected_rect(surface, s_x, e_x, sy)

    def render_string(self, surface, text, x, y, line_index, ime_editing, ime_editing_pos):
        offset_height = self.font.offset_height  # 渲染时的偏移量
        text_width = [self.font.rendered_text_width[char] for char in text]
        text_surface = [self.font.rendered_text_surface[char] for char in text]

        self.render_img_editing(line_index, ime_editing, text_width, text_surface)

        text_width_acc = list(itertools.accumulate(text_width))
        s_index = bisect.bisect_left(text_width_acc, -x)
        e_index = min(bisect.bisect_left(text_width_acc, surface.get_width() - x, s_index) + 1, len(text_width_acc))

        self.render_selected(surface, x, y, text_width_acc, line_index)

        surface.blits((text_surface[i], (x + text_width_acc[i] - text_width[i], y + offset_height))
                      for i in range(s_index, e_index))

        self.render_cursor(surface, x, y, ime_editing_pos, line_index)

    def render(self, screen, rect, mouse_pos):
        cache_surface = pygame.Surface(rect.size, pygame.SRCALPHA)  # 缓存渲染结果的画布
        
        hidden_lines_num = self.vScroll.offset // self.font.line_height  # 被隐藏的行数
        hidden_lines_height = hidden_lines_num * self.font.line_height  # 被隐藏的行的总高度
        remain_lines_num = len(self.cursor.text) - hidden_lines_num  # 剩余的行数
        
        x, y = -self.hScroll.offset, -self.vScroll.offset + hidden_lines_height  # 文字在渲染区域内的左上角纵坐标（渲染起始纵坐标）
        
        show_lines_num = min((rect.h - y) // self.font.line_height + 1, remain_lines_num)  # 能被显示的行数
        end_line_index = hidden_lines_num + show_lines_num
        
        ime_editing, ime_editing_pos = self.get_ime_editing_surface()

        for i in range(hidden_lines_num, end_line_index):
            self.render_string(cache_surface, self.cursor.text[i], x, y, i, ime_editing, ime_editing_pos)
            y += self.font.line_height

        max_width = max(self.cursor.max_line_width,
                        self.cursor.get_line_width(self.cursor.row) + ime_editing.get_width())

        self.vScroll.update_content_length(len(self.cursor.text) * self.font.line_height)
        self.hScroll.update_content_length(max_width+1)
        self.vScroll.render(cache_surface)
        self.hScroll.render(cache_surface)
        screen.blit(cache_surface, rect)

        self.select_menu.render(screen, mouse_pos)
