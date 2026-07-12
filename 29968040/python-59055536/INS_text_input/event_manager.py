import pygame
from .scroll_bar import VScrollBar, HScrollBar
from .font_renderer import FontRenderer
from .cursor import Cursor
from .selected_manager import SelectedManager
from .clipboard import ClipBoard
from .select_menu import SelectMenu


class EventManager:
    def __init__(self, rect, v_scroll: VScrollBar, h_scroll: HScrollBar, font, cursor, selected_manager, select_menu):
        self.rect = rect
        self.vScroll: VScrollBar = v_scroll
        self.hScroll: HScrollBar = h_scroll
        self.font: FontRenderer = font
        self.cursor: Cursor = cursor
        self.selected_manager: SelectedManager = selected_manager
        self.select_menu: SelectMenu = select_menu

        self.focus = False
        pygame.key.stop_text_input()

        self.ime_editing_text = ""  # 输入法文字
        self.ime_editing_pos = 0  # 输入法光标位置

    def move_cursor_in_rect(self):  # 把光标限制在可视区域里
        cx, cy = self.cursor.get_screen_pos()
        sx, sy = -self.hScroll.offset, -self.vScroll.offset
        x, y = cx + sx, cy + sy
        new_x = min(max(x, 0), self.rect.width - 6)
        new_y = min(max(y, 0), self.rect.height - self.font.line_height)
        dis_x, dis_y = new_x - x, new_y - y
        self.hScroll.update_content_offset(-sx - dis_x)
        self.vScroll.update_content_offset(-sy - dis_y)

    def delete_selected_text(self):
        begin, end = self.selected_manager.begin.copy(), self.selected_manager.end.copy()
        self.selected_manager.stop_selected()
        self.cursor.set_cursor_pos(*min(begin, end))
        self.cursor.text.delete_text(begin, end)
        self.move_cursor_in_rect()

    def handle_key_backspace(self):  # 处理 backspace 键
        if self.selected_manager.have_text:
            self.delete_selected_text()
            return
        self.cursor.delete_char()
        self.move_cursor_in_rect()

    def handle_key_delete(self):  # 处理 delete 键
        if self.selected_manager.have_text:
            self.delete_selected_text()
            return
        if self.cursor.is_last_line() and self.cursor.is_line_end():  # 在最后一行末尾
            return
        self.handle_key_right()  # 光标右移
        self.handle_key_backspace()  # 删除字符
        self.move_cursor_in_rect()

    def handle_key_left(self):
        if self.selected_manager.have_text:
            begin, end = self.selected_manager.begin.copy(), self.selected_manager.end.copy()
            self.selected_manager.stop_selected()
            if max(begin, end) == list(self.cursor.get_cursor_pos()):
                self.cursor.set_cursor_pos(*min(begin, end))
        else:
            self.cursor.cursor_left()
        self.move_cursor_in_rect()

    def handle_key_right(self):
        if self.selected_manager.have_text:
            begin, end = self.selected_manager.begin.copy(), self.selected_manager.end.copy()
            self.selected_manager.stop_selected()
            if min(begin, end) == list(self.cursor.get_cursor_pos()):
                self.cursor.set_cursor_pos(*max(begin, end))
        else:
            self.cursor.cursor_right()
        self.move_cursor_in_rect()

    def handle_key_up(self):
        if self.selected_manager.have_text:
            begin, end = self.selected_manager.begin.copy(), self.selected_manager.end.copy()
            self.selected_manager.stop_selected()
            if max(begin, end) == list(self.cursor.get_cursor_pos()):
                self.cursor.set_cursor_pos(*min(begin, end))
                self.move_cursor_in_rect()
                return
        self.cursor.cursor_up()
        self.move_cursor_in_rect()

    def handle_key_down(self):
        if self.selected_manager.have_text:
            begin, end = self.selected_manager.begin.copy(), self.selected_manager.end.copy()
            self.selected_manager.stop_selected()
            if min(begin, end) == list(self.cursor.get_cursor_pos()):
                self.cursor.set_cursor_pos(*max(begin, end))
                self.move_cursor_in_rect()
                return
        self.cursor.cursor_down()
        self.move_cursor_in_rect()

    def is_ime_editing(self):  # 是否在使用输入法
        return self.ime_editing_text != '' or self.ime_editing_pos != 0

    @property
    def is_scroll(self):  # 是否正在拖动滚动条
        return self.vScroll.scroll_dragging or self.hScroll.scroll_dragging

    def stop_ime_edinting(self):  # 强行停止输入法输入
        if self.is_ime_editing():
            pygame.key.stop_text_input()
            self.cursor.add_string(self.ime_editing_text)
            self.ime_editing_text = ""  # 清空输入法文字
            self.ime_editing_pos = 0
            pygame.key.start_text_input()

    def handle_copy(self):  # 复制
        if not self.selected_manager.have_text:
            return
        begin, end = self.selected_manager.begin.copy(), self.selected_manager.end.copy()
        text = self.cursor.text.get_text(begin, end)
        # print(text)
        ClipBoard.copy(text)
        self.select_menu.close_menu()

    def handle_paste(self):  # 粘贴
        if self.selected_manager.have_text:
            self.delete_selected_text()
        self.cursor.add_text(ClipBoard.paste())
        self.move_cursor_in_rect()
        self.select_menu.close_menu()

    def handle_select_all(self):  # 全选
        self.selected_manager.set_begin((0, 0))
        self.selected_manager.set_end(self.cursor.get_last_cursor_pos())
        self.cursor.set_last_cursor_pos()
        self.select_menu.close_menu()

    def handle_cut(self):  # 剪切
        self.handle_copy()
        if self.selected_manager.have_text:
            self.delete_selected_text()
        self.select_menu.close_menu()

    def handle_key_board(self, event):
        if event.type == pygame.TEXTEDITING:  # 输入法事件
            if not pygame.key.get_focused():  # 在关闭窗口时会触发此 TEXTEDITING 事件，可能是 pygame 的 bug?
                self.stop_ime_edinting()
                return
            if self.selected_manager.have_text:
                self.delete_selected_text()
            self.ime_editing_text = event.text
            self.ime_editing_pos = event.start
            self.move_cursor_in_rect()
        elif event.type == pygame.TEXTINPUT:  # 普通输入事件，但输入法完毕后也会触发此事件
            if self.selected_manager.have_text:
                self.delete_selected_text()
            self.ime_editing_text = ""  # 清空输入法文字
            self.ime_editing_pos = 0
            self.cursor.add_string(event.text)  # 添加文本
            self.move_cursor_in_rect()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.handle_key_backspace()
            elif event.key == pygame.K_DELETE:
                self.handle_key_delete()
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                if self.selected_manager.have_text:
                    self.delete_selected_text()
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
            elif event.mod & pygame.KMOD_CTRL:
                if event.key == pygame.K_a:
                    self.handle_select_all()
                elif event.key == pygame.K_v:
                    self.handle_paste()
                elif event.key == pygame.K_c:
                    self.handle_copy()
                elif event.key == pygame.K_x:
                    self.handle_cut()

    def on_mouse_down(self, event):
        if self.is_scroll:
            return
        if event.button == 1:
            if self.select_menu.show and self.select_menu.rect.collidepoint(event.pos):
                    self.select_menu.on_mouse_down(event.pos)
            else:
                if self.select_menu.show:
                    self.select_menu.close_menu()
                if not self.select_menu.show and not self.selected_manager.in_selected:
                    self.set_cursor_screen_pos(self.rect, event.pos)
                    self.selected_manager.in_selected = True
                    self.selected_manager.set_begin(self.cursor.get_cursor_pos())
        elif event.button == 3 and self.rect.collidepoint(event.pos):
            if not self.selected_manager.have_text:
                self.set_cursor_screen_pos(self.rect, event.pos)
            self.stop_ime_edinting()
            self.select_menu.close_menu()
            self.select_menu.open_menu(*event.pos)

    def handle_main_event(self, events):
        for event in events:
            if self.focus and not self.select_menu.show:
                self.handle_key_board(event)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button <= 3:
                self.stop_ime_edinting()
                self.focus = self.rect.collidepoint(event.pos)
                if self.focus:
                    pygame.key.start_text_input()
                    self.on_mouse_down(event)
                else:
                    self.select_menu.close_menu()
                    pygame.key.stop_text_input()
            elif event.type == pygame.MOUSEBUTTONUP and not self.is_scroll:
                self.selected_manager.in_selected = False

    def handle_events(self, events, mouse_pos):
        self.vScroll.handle_event(events, on_scroll_func=self.select_menu.close_menu)
        self.hScroll.handle_event(events, on_scroll_func=self.select_menu.close_menu)

        if not self.select_menu.show:
            self.selected_manager.event_update(
                mouse_pos, self.set_cursor_screen_pos,
                self.move_cursor_in_rect, self.cursor.get_cursor_pos
            )
        self.handle_main_event(events)

    def set_cursor_screen_pos(self, rect, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        if self.vScroll.scroll_dragging or self.hScroll.scroll_dragging:
            return

        # 计算鼠标相对于文本区域的位置
        relative_x = mouse_x - rect.x + self.hScroll.offset
        relative_y = mouse_y - rect.y + self.vScroll.offset

        self.cursor.set_screen_pos(relative_x, relative_y)
