import pygame
from .tool import Tool
from .select_menu import SelectMenu
from .keyboard import KeyBoard
from .shortcut import Shortcut


class EventManager:
    def __init__(self, parent, tool, select_menu, keyboard, shortcut):
        self.parent = parent
        self.tool: Tool = tool
        self.rect = tool.rect
        self.vScroll = tool.vScroll
        self.hScroll = tool.hScroll
        self.cursor = tool.cursor
        self.selected_manager = tool.selected_manager
        self.select_menu: SelectMenu = select_menu
        self.keyboard: KeyBoard = keyboard
        self.shortcut: Shortcut = shortcut

        self.focus = False
        pygame.key.stop_text_input()

        self.ime_editing_text = ""  # 输入法文字
        self.ime_editing_pos = 0  # 输入法光标位置

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

    def handle_key_board(self, event):
        if event.type == pygame.TEXTEDITING:  # 输入法事件
            if self.selected_manager.has_selection:
                self.tool.delete_selected_text()
            self.ime_editing_text = event.text
            self.ime_editing_pos = event.start
            self.tool.move_cursor_in_rect()
        elif event.type == pygame.TEXTINPUT:  # 普通输入事件，但输入法完毕后也会触发此事件
            if self.selected_manager.has_selection:
                self.tool.delete_selected_text()
            self.ime_editing_text = ""  # 清空输入法文字
            self.ime_editing_pos = 0
            self.cursor.add_string(event.text)  # 添加文本
            self.tool.move_cursor_in_rect()
        elif event.type == pygame.KEYDOWN:
            self.shortcut.handle_event(event)
            self.keyboard.handle_event(event)

    def set_focus(self, mode):
        self.focus = mode
        if self.focus:
            for text_input in self.parent.text_input_group:
                if text_input == self.parent:
                    continue
                text_input.event.set_focus(False)
            pygame.key.start_text_input()
        else:
            self.select_menu.close_menu()
            pygame.key.stop_text_input()

    def on_mouse_down(self, event):
        self.stop_ime_edinting()
        self.set_focus(self.rect.collidepoint(event.pos))

        if not self.focus or self.is_scroll:
            return

        if event.button == 1:
            if self.select_menu.is_menu_visible and self.select_menu.rect.collidepoint(event.pos):
                self.select_menu.on_mouse_down(event.pos)
            else:
                self.select_menu.close_menu()
                if not self.selected_manager.is_selecting:
                    self.tool.set_cursor_screen_pos(self.rect, event.pos)
                    self.selected_manager.is_selecting = True
                    self.selected_manager.set_begin(self.cursor.get_cursor_pos())
                    pygame.key.stop_text_input()
        elif event.button == 3 and self.rect.collidepoint(event.pos):
            if not self.selected_manager.has_selection:
                self.tool.set_cursor_screen_pos(self.rect, event.pos)
            self.stop_ime_edinting()
            self.select_menu.open_menu(*event.pos)

    def handle_events(self, events, mouse_pos):
        if not pygame.key.get_focused():
            self.set_focus(False)

        self.vScroll.handle_event(events, self.rect, on_scroll_func=self.select_menu.close_menu)
        self.hScroll.handle_event(events, on_scroll_func=self.select_menu.close_menu)

        if not self.select_menu.is_menu_visible:
            self.tool.selected_event_update(mouse_pos)

        for event in events:
            if self.focus and not self.select_menu.is_menu_visible:
                self.handle_key_board(event)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button <= 3:
                self.on_mouse_down(event)
            elif event.type == pygame.MOUSEBUTTONUP and not self.is_scroll and self.selected_manager.is_selecting:
                self.selected_manager.is_selecting = False
                pygame.key.start_text_input()
