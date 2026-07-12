import pygame
import time


class SelectedManager:
    def __init__(self, rect):
        self.rect: pygame.Rect = rect

        self.is_selecting = False  # 这仅仅表示是否在选中状态的拖动中
        self.begin = [0, 0]
        self.end = [0, 0]

        self.last_update = time.time()

    def set_begin(self, pos):
        self.begin[0], self.begin[1] = pos[0], pos[1]
        self.end[0], self.end[1] = pos[0], pos[1]

    def set_end(self, pos):
        self.end[0], self.end[1] = pos[0], pos[1]

    def stop_selected(self):
        self.is_selecting = False
        self.set_begin((0, 0))

    def line_is_selecting(self, line_index):
        if self.begin == self.end:
            return False
        begin_row, end_row = min(self.begin[0], self.end[0]), max(self.begin[0], self.end[0])
        return begin_row <= line_index <= end_row

    @property
    def has_selection(self):  # 内部是否有选中的文字
        return self.begin != self.end
