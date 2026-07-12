import pygame
import pygame.locals
import pygame.key
from ScrollBar import VScrollBar, HScrollBar


class TextInput:
    def __init__(self, font, font_size, font_color, line_height, rect, init_text) -> None:
        # 字体方面
        self.font = font  # 字体
        self.font_size = font_size  # 字体大小
        self.font_color = font_color  # 字体颜色
        self.line_height = line_height  # 行高

        # 文字存储
        self._ime_text = init_text.split('\n')  # 输入的普通文字
        self._ime_text_pos = [0, 0]  # 普通光标位置
        self._ime_editing_text = ""  # 输入法文字
        self._ime_editing_pos = 0  # 输入法光标位置

        # 渲染方面
        self.rect: pygame.Rect = rect  # 输入框的 Rect
        self.cache = {}  # 缓存已渲染的文字的画布
        self.cache_size = {}  # 缓存已渲染的文字的画布的大小

        # 滚动条
        self.vScroll = VScrollBar(self.rect)
        self.hScroll = HScrollBar(self.rect)

    def is_first_line(self):  # 该行是否是第一行
        return self._ime_text_pos[0] == 0

    def is_last_line(self):  # 是否是最后一行
        return self._ime_text_pos[0] == len(self._ime_text) - 1

    def is_line_start(self):  # 是否是某一行的开始
        return self._ime_text_pos[1] == 0

    def is_line_end(self):  # 是否是某一行的开始
        return self._ime_text_pos[1] == len(self._ime_text[self._ime_text_pos[0]])

    def is_ime_editing(self):  # 是否在使用输入法
        return self._ime_editing_text != '' or self._ime_editing_pos != 0

    def is_cursor_pos(self, i, j):  # 判断某个位置是否是光标位置
        return i == self._ime_text_pos[0] and j == self._ime_text_pos[1]

    def get_line_end_pos(self):  # 返回该行的最后一个光标的位置
        return len(self._ime_text[self._ime_text_pos[0]])

    def remove_line_break_char(self):  # 删除当前行开头（上一行结尾）的换行符
        current_line_index = self._ime_text_pos[0]
        if not self.is_first_line():
            self._ime_text_pos[0] = current_line_index = current_line_index - 1
            self._ime_text_pos[1] = self.get_line_end_pos()
            self._ime_text[current_line_index] += self._ime_text[current_line_index + 1]
            del self._ime_text[current_line_index + 1]

    def remove_char(self):  # 删除普通字符
        current_line_index = self._ime_text_pos[0]
        self._ime_text_pos[1] -= 1
        self._ime_text[current_line_index] = (
            self._ime_text[current_line_index][:self._ime_text_pos[1]] +
            self._ime_text[current_line_index][self._ime_text_pos[1] + 1:]
        )

    def add_line_break_char(self):
        current_line_index = self._ime_text_pos[0]
        before_cursor_text = self._ime_text[current_line_index][:self._ime_text_pos[1]]
        after_cursor_text = self._ime_text[current_line_index][self._ime_text_pos[1]:]

        self._ime_text[current_line_index] = before_cursor_text
        self._ime_text_pos[0] = current_line_index = current_line_index + 1
        self._ime_text_pos[1] = 0
        self._ime_text.insert(current_line_index, after_cursor_text)

    def add_text(self, text):  # 添加文本（单行）
        current_line_index = self._ime_text_pos[0]
        self._ime_text[current_line_index] = (
                self._ime_text[current_line_index][:self._ime_text_pos[1]]
                + text
                + self._ime_text[current_line_index][self._ime_text_pos[1]:]
        )
        self._ime_text_pos[1] += len(text)

    def handle_key_backspace(self):
        if len(self._ime_text) <= 0:  # 没有文字
            return
        if self.is_line_start():  # 位于一行开头
            self.remove_line_break_char()
        else:
            self.remove_char()

    def handle_key_delete(self):
        if self.is_last_line() and self.is_line_end():
            return
        self.handle_key_right()
        self.handle_key_backspace()

    def handle_key_left(self):
        if self.is_line_start() and self.is_first_line():
            return
        if self.is_line_start():
            self._ime_text_pos[0] -= 1
            self._ime_text_pos[1] = self.get_line_end_pos()
        else:
            self._ime_text_pos[1] -= 1

    def handle_key_right(self):
        if self.is_line_end() and self.is_last_line():
            return
        if self.is_line_end():
            self._ime_text_pos[0] += 1
            self._ime_text_pos[1] = 0
        else:
            self._ime_text_pos[1] += 1

    def handle_key_up(self):
        if self.is_first_line():
            return
        self._ime_text_pos[0] -= 1
        self._ime_text_pos[1] = min(self._ime_text_pos[1], self.get_line_end_pos())

    def handle_key_down(self):
        if self.is_last_line():
            return
        self._ime_text_pos[0] += 1
        self._ime_text_pos[1] = min(self._ime_text_pos[1], self.get_line_end_pos())

    def handle_events(self, events):
        self.vScroll.handle_event(events)
        self.hScroll.handle_event(events)
        for event in events:
            if event.type == pygame.TEXTEDITING:  # 输入法事件
                self._ime_editing_text = event.text
                self._ime_editing_pos = event.start
            elif event.type == pygame.TEXTINPUT:  # 普通输入事件，但输入法完毕后也是这个事件
                self._ime_editing_text = ""  # 清空输入法文字
                self._ime_editing_pos = 0
                self.add_text(event.text)  # 添加文本
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.handle_key_backspace()
                elif event.key == pygame.K_DELETE:
                    self.handle_key_delete()
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    self.add_line_break_char()
                elif event.key == pygame.K_LEFT:
                    self.handle_key_left()
                elif event.key == pygame.K_RIGHT:
                    self.handle_key_right()
                elif event.key == pygame.K_UP:
                    self.handle_key_up()
                elif event.key == pygame.K_DOWN:
                    self.handle_key_down()

    def render_char(self, char):
        if char in self.cache:
            return self.cache[char]
        self.cache[char] = self.font.render(char, True, self.font_color)
        self.cache_size[char] = self.cache[char].get_size()
        return self.cache[char]

    def get_char_size(self, char):
        return self.cache_size[char]

    def render_ime_editing_text(self):  # 绘制输入法文字
        offset_height = (self.line_height - self.font_size) // 2  # 渲染时的偏移量
        text_surface = self.font.render(self._ime_editing_text, True, self.font_color)
        x, y = self.font.size(self._ime_editing_text[:self._ime_editing_pos])[0]-1, 0

        surface = pygame.Surface((text_surface.get_width(), self.line_height), pygame.SRCALPHA)
        surface.blit(text_surface, (0, offset_height))
        pygame.draw.line(surface, (0,) * 3, (x, y), (x, y + self.line_height))
        pygame.draw.line(surface, (0,) * 3, (0, y + offset_height + self.font_size),
                                            (surface.get_width(), y + offset_height + self.font_size))
        return surface

    def render_cursor(self, surface, x, y):
        if self.is_ime_editing():
            ime_editing_surface = self.render_ime_editing_text()
            surface.blit(ime_editing_surface, (x, y))
            return ime_editing_surface.get_width()
        else:
            pygame.draw.line(surface, (0,) * 3, (x, y), (x, y + self.line_height))
            return 0

    def set_cursor_pos(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if not pygame.mouse.get_pressed()[0] or self.vScroll.scroll_dragging or self.hScroll.scroll_dragging \
                or not self.rect.collidepoint(mouse_x, mouse_y):
            return
        new_x, new_y = mouse_x - self.rect.x + self.hScroll.offset, mouse_y - self.rect.y + self.vScroll.offset
        if new_y // self.line_height >= len(self._ime_text):
            self._ime_text_pos[0] = len(self._ime_text) - 1
            self._ime_text_pos[1] = self.get_line_end_pos()
            return 
        self._ime_text_pos[0] = new_y // self.line_height

        length = 0
        for i, char in enumerate(self._ime_text[self._ime_text_pos[0]]):
            width = self.get_char_size(char)[0]
            if length <= new_x < length + width:
                self._ime_text_pos[1] = i + round((new_x - length) / width)
                return
            length += width
        self._ime_text_pos[1] = self.get_line_end_pos()

    def render(self, screen):
        hidden_lines_num = self.vScroll.offset // self.line_height  # 被隐藏的行数
        hidden_lines_height = hidden_lines_num * self.line_height  # 被隐藏的行的总高度
        offset_height = (self.line_height - self.font_size) // 2  # 渲染时的偏移量
        max_lines_num = min((self.rect.h + self.vScroll.offset - hidden_lines_height) // self.line_height + 1,
                            len(self._ime_text) - hidden_lines_num)  # 当前渲染区域内最大可显示的行数

        cache_surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)  # 缓存渲染结果的画布
        x, y, max_width = -self.hScroll.offset, -self.vScroll.offset + hidden_lines_height, 0

        for i in range(hidden_lines_num, hidden_lines_num + max_lines_num):
            for j in range(len(self._ime_text[i])):
                if self.is_cursor_pos(i, j):
                    x += self.render_cursor(cache_surface, x, y)
                cache_surface.blit(self.render_char(self._ime_text[i][j]), (x, y + offset_height))
                x += self.get_char_size(self._ime_text[i][j])[0]
            if self.is_cursor_pos(i, len(self._ime_text[i])):
                x += self.render_cursor(cache_surface, x, y)
            max_width = max(max_width, x+self.hScroll.offset)
            x = -self.hScroll.offset
            y += self.line_height

        self.vScroll.update_content_length(len(self._ime_text) * self.line_height)
        self.hScroll.update_content_length(max_width+1)
        self.vScroll.render(cache_surface)
        self.hScroll.render(cache_surface)
        screen.blit(cache_surface, self.rect)
        self.set_cursor_pos()
