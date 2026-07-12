from .tool import Tool
from .select_menu import SelectMenu
from .clipboard import ClipBoard
from .util import mod_equal
import pygame


class Shortcut:
    def __init__(self, tool, select_menu):
        self.tool: Tool = tool
        self.selected_manager = self.tool.selected_manager
        self.cursor = self.tool.cursor
        self.select_menu: SelectMenu = select_menu

        self.shortcut = []

        self.add_shortcut(key=pygame.K_c, mod=pygame.KMOD_CTRL,
                          name='复制', func=self.handle_copy,
                          visible_in_normal_menu=False,
                          visible_in_select_menu=True)

        self.add_shortcut(key=pygame.K_v, mod=pygame.KMOD_CTRL,
                          name='粘贴', func=self.handle_paste,
                          visible_in_normal_menu=True,
                          visible_in_select_menu=True)

        self.add_shortcut(key=pygame.K_a, mod=pygame.KMOD_CTRL,
                          name='全选', func=self.handle_select_all,
                          visible_in_normal_menu=True,
                          visible_in_select_menu=True)

        self.add_shortcut(key=pygame.K_x, mod=pygame.KMOD_CTRL,
                          name='剪切', func=self.handle_cut,
                          visible_in_normal_menu=False,
                          visible_in_select_menu=True)

        self.add_shortcut(key=pygame.K_LEFT, mod=pygame.KMOD_SHIFT,
                          name='shift键+左键', func=self.shift_left,
                          visible_in_normal_menu=False,
                          visible_in_select_menu=False)

        self.add_shortcut(key=pygame.K_RIGHT, mod=pygame.KMOD_SHIFT,
                          name='shift键+右键', func=self.shift_right,
                          visible_in_normal_menu=False,
                          visible_in_select_menu=False)

        self.add_shortcut(key=pygame.K_UP, mod=pygame.KMOD_SHIFT,
                          name='shift键+上键', func=self.shift_up,
                          visible_in_normal_menu=False,
                          visible_in_select_menu=False)

        self.add_shortcut(key=pygame.K_DOWN, mod=pygame.KMOD_SHIFT,
                          name='shift键+下键', func=self.shift_down,
                          visible_in_normal_menu=False,
                          visible_in_select_menu=False)

    def add_shortcut(self, key, mod, name, func,
                     visible_in_normal_menu, visible_in_select_menu):
        self.shortcut.append({
            'key': key,
            'mod': mod or pygame.KMOD_NONE,
            'func': func,
        })

        if visible_in_normal_menu:
            self.select_menu.add_normal_menu_button(name, func)
        if visible_in_select_menu:
            self.select_menu.add_select_menu_button(name, func)

    def handle_copy(self):  # 复制
        if not self.selected_manager.has_selection:
            return
        begin, end = self.selected_manager.begin.copy(), self.selected_manager.end.copy()
        text = self.cursor.get_text(begin, end)
        ClipBoard.copy(text)
        self.select_menu.close_menu()

    def handle_paste(self):  # 粘贴
        if self.selected_manager.has_selection:
            self.tool.delete_selected_text()
        text = ClipBoard.paste()
        if not self.tool.multi_lines:
            text.replace('\n', ' ')
        self.cursor.add_text(text)
        self.tool.move_cursor_in_rect()
        self.select_menu.close_menu()

    def handle_select_all(self):  # 全选
        self.selected_manager.set_begin((0, 0))
        self.selected_manager.set_end(self.cursor.get_last_cursor_pos())
        self.cursor.set_last_cursor_pos()
        self.select_menu.close_menu()

    def handle_cut(self):  # 剪切
        self.handle_copy()
        if self.selected_manager.has_selection:
            self.tool.delete_selected_text()
        self.tool.move_cursor_in_rect()
        self.select_menu.close_menu()

    def shift_left(self):
        if not self.selected_manager.has_selection:
            self.selected_manager.set_begin(self.cursor.get_cursor_pos())
        self.cursor.cursor_left()
        self.selected_manager.set_end(self.cursor.get_cursor_pos())
        self.tool.move_cursor_in_rect()

    def shift_right(self):
        if not self.selected_manager.has_selection:
            self.selected_manager.set_begin(self.cursor.get_cursor_pos())
        self.cursor.cursor_right()
        self.selected_manager.set_end(self.cursor.get_cursor_pos())
        self.tool.move_cursor_in_rect()

    def shift_up(self):
        if not self.selected_manager.has_selection:
            self.selected_manager.set_begin(self.cursor.get_cursor_pos())
        self.cursor.cursor_up()
        self.selected_manager.set_end(self.cursor.get_cursor_pos())
        self.tool.move_cursor_in_rect()

    def shift_down(self):
        if not self.selected_manager.has_selection:
            self.selected_manager.set_begin(self.cursor.get_cursor_pos())
        self.cursor.cursor_down()
        self.selected_manager.set_end(self.cursor.get_cursor_pos())
        self.tool.move_cursor_in_rect()

    def handle_event(self, event):
        for shortcut in self.shortcut:
            if mod_equal(event.mod, shortcut['mod']) and event.key == shortcut['key']:
                shortcut['func']()
