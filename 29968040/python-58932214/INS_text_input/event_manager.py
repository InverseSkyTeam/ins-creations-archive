import pygame
from .scroll_bar import VScrollBar, HScrollBar
from .font_renderer import FontRenderer
from .cursor import Cursor


class EventManager:
    def __init__(self, rect, v_scroll: VScrollBar, h_scroll: HScrollBar, font, cursor):
        self.rect = rect
        self.vScroll: VScrollBar = v_scroll
        self.hScroll: HScrollBar = h_scroll
        self.font: FontRenderer = font
        self.cursor: Cursor = cursor

        self.focus = False
        pygame.key.stop_text_input()

        self.ime_editing_text = ""  # 输入法文字
        self.ime_editing_pos = 0  # 输入法光标位置

    def move_cursor_in_rect(self):  # 把光标限制在可视区域里
        cx, cy = self.cursor.get_screen_pos()
        sx, sy = -self.hScroll.offset, -self.vScroll.offset
        x, y = cx + sx, cy + sy
        new_x = min(max(x, 0), self.rect.width - 1)
        new_y = min(max(y, 0), self.rect.height - self.font.line_height)
        dis_x, dis_y = new_x - x, new_y - y
        self.hScroll.update_content_offset(-sx - dis_x)
        self.vScroll.update_content_offset(-sy - dis_y)

    def handle_key_backspace(self):  # 处理 backspace 键
        self.cursor.delete_char()
        self.move_cursor_in_rect()

    def handle_key_delete(self):  # 处理 delete 键
        if self.cursor.is_last_line() and self.cursor.is_line_end():  # 在最后一行末尾
            return
        self.handle_key_right()  # 光标右移
        self.handle_key_backspace()  # 删除字符
        self.move_cursor_in_rect()

    def handle_key_left(self):
        self.cursor.cursor_left()
        self.move_cursor_in_rect()

    def handle_key_right(self):
        self.cursor.cursor_right()
        self.move_cursor_in_rect()

    def handle_key_up(self):
        self.cursor.cursor_up()
        self.move_cursor_in_rect()

    def handle_key_down(self):
        self.cursor.cursor_down()
        self.move_cursor_in_rect()

    def is_ime_editing(self):  # 是否在使用输入法
        return self.ime_editing_text != '' or self.ime_editing_pos != 0

    def handle_events(self, events, rect):
        self.vScroll.handle_event(events)
        self.hScroll.handle_event(events)
        for event in events:
            if event.type == pygame.TEXTEDITING and self.focus:  # 输入法事件
                self.ime_editing_text = event.text
                self.ime_editing_pos = event.start
                self.move_cursor_in_rect()
            elif event.type == pygame.TEXTINPUT and self.focus:  # 普通输入事件，但输入法完毕后也会触发此事件
                self.ime_editing_text = ""  # 清空输入法文字
                self.ime_editing_pos = 0
                self.cursor.add_string(event.text)  # 添加文本
                self.move_cursor_in_rect()
            elif event.type == pygame.KEYDOWN and self.focus:
                if event.key == pygame.K_BACKSPACE:
                    self.handle_key_backspace()
                elif event.key == pygame.K_DELETE:
                    self.handle_key_delete()
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    self.cursor.add_line_break_char()
                    self.move_cursor_in_rect()
                elif event.key == pygame.K_LEFT:
                    self.handle_key_left()
                elif event.key == pygame.K_RIGHT:
                    self.handle_key_right()
                elif event.key == pygame.K_UP:
                    self.handle_key_up()
                elif event.key == pygame.K_DOWN:
                    self.handle_key_down()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in (4, 5):
                    continue
                self.set_focus(rect.collidepoint(event.pos) and event.button)
                if not self.focus:
                    continue
                if event.button == 1 and not self.vScroll.scroll_dragging and not self.hScroll.scroll_dragging:
                    self.set_cursor_screen_pos(rect, event.pos)

    def set_focus(self, focus):
        self.focus = focus
        if focus:
            pygame.key.start_text_input()
        else:
            pygame.key.stop_text_input()

    def set_cursor_screen_pos(self, rect, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        if self.vScroll.scroll_dragging or self.hScroll.scroll_dragging:
            return

        # 计算鼠标相对于文本区域的位置
        relative_x = mouse_x - rect.x + self.hScroll.offset
        relative_y = mouse_y - rect.y + self.vScroll.offset

        self.cursor.set_screen_pos(relative_x, relative_y)
