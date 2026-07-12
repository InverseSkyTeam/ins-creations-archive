import pygame
import time


class SelectedManager:
    def __init__(self, rect):
        self.rect: pygame.Rect = rect

        self.in_selected = False  # 这仅仅表示是否在选中的拖动中
        self.begin = [0, 0]
        self.end = [0, 0]

        self.last_update = time.time()

    def set_begin(self, pos):
        self.begin[0], self.begin[1] = pos[0], pos[1]
        self.end[0], self.end[1] = pos[0], pos[1]

    def set_end(self, pos):
        self.end[0], self.end[1] = pos[0], pos[1]

    def stop_selected(self):
        self.in_selected = False
        self.set_begin((0, 0))

    def event_update(self, mouse_pos, set_cursor_screen_pos, move_cursor_in_rect, get_cursor_pos):
        if not self.in_selected or (time.time() - self.last_update) <= 1 / 45:
            return
        set_cursor_screen_pos(self.rect, mouse_pos)
        move_cursor_in_rect()  # 很妙，这意味着超出范围越远，滚动越快
        self.set_end(get_cursor_pos())
        self.last_update = time.time()

    def line_in_selected(self, line_index):
        if self.begin == self.end:
            return False
        begin_row, end_row = min(self.begin[0], self.end[0]), max(self.begin[0], self.end[0])
        return begin_row <= line_index <= end_row

    @property
    def have_text(self):  # 内部是否有选中的文字
        return self.begin != self.end
