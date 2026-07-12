import pygame
from .tool import Tool


class KeyBoard:  # 内置键盘事件，不可更改
    def __init__(self, tool):
        self.tool: Tool = tool
        self.selected_manager = self.tool.selected_manager
        self.cursor = self.tool.cursor

    def handle_key_backspace(self):  # 处理 backspace 键
        if self.selected_manager.has_selection:
            self.tool.delete_selected_text()
            return
        self.cursor.delete_char()
        self.tool.move_cursor_in_rect()

    def handle_key_delete(self):  # 处理 delete 键
        if self.selected_manager.has_selection:
            self.tool.delete_selected_text()
            return
        if self.cursor.is_last_line() and self.cursor.is_line_end():  # 在最后一行末尾
            return
        self.handle_key_right()  # 光标右移
        self.handle_key_backspace()  # 删除字符
        self.tool.move_cursor_in_rect()

    def handle_key_left(self):
        if self.selected_manager.has_selection:
            begin, end = self.selected_manager.begin.copy(), self.selected_manager.end.copy()
            self.selected_manager.stop_selected()
            if max(begin, end) == list(self.cursor.get_cursor_pos()):
                self.cursor.set_cursor_pos(*min(begin, end))
        else:
            self.cursor.cursor_left()
        self.tool.move_cursor_in_rect()

    def handle_key_right(self):
        if self.selected_manager.has_selection:
            begin, end = self.selected_manager.begin.copy(), self.selected_manager.end.copy()
            self.selected_manager.stop_selected()
            if min(begin, end) == list(self.cursor.get_cursor_pos()):
                self.cursor.set_cursor_pos(*max(begin, end))
        else:
            self.cursor.cursor_right()
        self.tool.move_cursor_in_rect()

    def handle_key_up(self):
        if self.selected_manager.has_selection:
            begin, end = self.selected_manager.begin.copy(), self.selected_manager.end.copy()
            self.selected_manager.stop_selected()
            if max(begin, end) == list(self.cursor.get_cursor_pos()):
                self.cursor.set_cursor_pos(*min(begin, end))
                self.tool.move_cursor_in_rect()
                return
        self.cursor.cursor_up()
        self.tool.move_cursor_in_rect()

    def handle_key_down(self):
        if self.selected_manager.has_selection:
            begin, end = self.selected_manager.begin.copy(), self.selected_manager.end.copy()
            self.selected_manager.stop_selected()
            if min(begin, end) == list(self.cursor.get_cursor_pos()):
                self.cursor.set_cursor_pos(*max(begin, end))
                self.tool.move_cursor_in_rect()
                return
        self.cursor.cursor_down()
        self.tool.move_cursor_in_rect()

    def handle_event(self, event):
        if event.mod & pygame.KMOD_SHIFT:
            return
        if event.key == pygame.K_BACKSPACE:
            self.handle_key_backspace()
        elif event.key == pygame.K_DELETE:
            self.handle_key_delete()
        elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
            if self.selected_manager.has_selection:
                self.tool.delete_selected_text()
            if self.tool.multi_lines:
                self.cursor.add_line_break_char()
            self.tool.move_cursor_in_rect()
        elif event.key == pygame.K_LEFT:
            self.handle_key_left()
        elif event.key == pygame.K_RIGHT:
            self.handle_key_right()
        elif event.key == pygame.K_UP:
            self.handle_key_up()
        elif event.key == pygame.K_DOWN:
            self.handle_key_down()
