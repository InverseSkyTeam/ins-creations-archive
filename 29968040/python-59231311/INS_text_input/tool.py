from .scroll_bar import VScrollBar, HScrollBar
from .font_renderer import FontRenderer
from .cursor import Cursor
from .selected_manager import SelectedManager
from .cursor_blink import CursorBlink
import time


class Tool:  # 一些基础功能的封装
    def __init__(self, rect, v_scroll, h_scroll, font, cursor, selected_manager, cursor_blink, multi_lines):
        self.rect = rect
        self.vScroll: VScrollBar = v_scroll
        self.hScroll: HScrollBar = h_scroll
        self.font: FontRenderer = font
        self.cursor: Cursor = cursor
        self.cursor_blink: CursorBlink = cursor_blink
        self.selected_manager: SelectedManager = selected_manager
        self.multi_lines: bool = multi_lines

    def _move_cursor_in_rect(self, cx, cy):  # 把光标限制在可视区域里
        sx, sy = -self.hScroll.offset, -self.vScroll.offset
        x, y = cx + sx, cy + sy
        new_x = min(max(x, 0), self.rect.width - (6 if self.multi_lines else 1))
        new_y = min(max(y, 0), self.rect.height - self.font.line_height)
        dis_x, dis_y = new_x - x, new_y - y
        self.hScroll.update_content_offset(-sx - dis_x)
        self.vScroll.update_content_offset(-sy - dis_y)

    def move_cursor_in_rect(self):  # 把光标限制在可视区域里
        cx, cy = self.cursor.get_screen_pos()
        self._move_cursor_in_rect(cx, cy)
        self.cursor_blink.create_new_cycle()  # 只要出现此操作，就一定要保证光标处于显示状态

    def delete_selected_text(self):
        begin, end = self.selected_manager.begin.copy(), self.selected_manager.end.copy()
        self.selected_manager.stop_selected()
        self.cursor.set_cursor_pos(*min(begin, end))
        self.cursor.delete_text(begin, end)
        self.move_cursor_in_rect()

    def set_cursor_screen_pos(self, rect, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        if self.vScroll.scroll_dragging or self.hScroll.scroll_dragging:
            return

        # 计算鼠标相对于文本区域的位置
        relative_x = mouse_x - rect.x + self.hScroll.offset
        relative_y = mouse_y - rect.y + self.vScroll.offset

        self.cursor.set_screen_pos(relative_x, relative_y if self.multi_lines else 0)

    def selected_event_update(self, mouse_pos):
        if not self.selected_manager.is_selecting:
            return
        if (time.time() - self.selected_manager.last_update) <= 1 / 45:
            return
        self.set_cursor_screen_pos(self.rect, mouse_pos)
        self.move_cursor_in_rect()  # 很妙，这意味着超出范围越远，滚动越快
        self.selected_manager.set_end(self.cursor.get_cursor_pos())
        self.selected_manager.last_update = time.time()
