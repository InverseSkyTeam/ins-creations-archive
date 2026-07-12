from .text_manager import TextManager
import itertools
import bisect


class Cursor(TextManager):  # 带指针的文本管理器
    def __init__(self, text: str, font):
        super().__init__(text, font)
        
        self.row, self.column = 0, 0  # 指针在文本框中的行、列位置
        self.x, self.y = 0, 0  # 指针在文本框中渲染时的位置

    def get_cursor_text(self):  # 获取光标右边的一个字符
        return self.text[self.row][self.column]

    def get_cursor_left_text(self):  # 获取光标左边的一个字符
        return self.text[self.row][self.column - 1]

    def get_cursor_pos(self):  # 获取光标在文本中坐标
        return self.row, self.column

    def get_screen_pos(self):  # 获取光标在画布中坐标
        return self.x, self.y

    def set_cursor_pos(self, row, column):  # 设置光标在文本中坐标
        self.row, self.column = row, column  # 必须保证二者是合法的
        current_text = self.text[self.row]
        text_width = [self.font.rendered_text_width[char] for char in current_text]
        self.x = sum(text_width[:column])
        self.y = row * self.font.line_height

    def get_last_cursor_pos(self):  # 获取光标在文本末尾时的位置
        return len(self.text) - 1, len(self.text[-1])

    def set_last_cursor_pos(self):  # 光标移到文本末尾
        self.row, self.column = self.get_last_cursor_pos()
        self.x = self.line_width[-1]
        self.y = self.row * self.font.line_height

    def set_screen_pos(self, x, y):  # 设置光标在屏幕中坐标
        # 计算鼠标相对于文本区域的位置
        relative_x = x
        relative_y = y

        # 计算光标行的位置
        line_index = relative_y // self.font.line_height

        # 特殊情况
        if line_index >= len(self.text):
            self.row, self.column = len(self.text) - 1, len(self.text[-1])
            self.y = (len(self.text) - 1) * self.font.line_height
            self.x = self.line_width[self.row]
            return
        if line_index < 0:
            self.row = self.column = self.x = self.y = 0
            return

        # 设置光标行位置
        self.row = line_index
        self.y = line_index * self.font.line_height

        # 计算光标在该行的列位置
        current_text = self.text[self.row]
        text_width = [self.font.rendered_text_width[char] for char in current_text]
        text_width_acc = list(itertools.accumulate(text_width))
        col = bisect.bisect_right(text_width_acc, relative_x)

        if col >= len(text_width):
            self.column = len(current_text)
            self.x = self.line_width[line_index]
        elif col < 0:
            self.column = self.x = 0
        else:
            left = relative_x - (text_width_acc[col] - text_width[col])
            right = text_width_acc[col] - relative_x
            # print(left, right)
            if left < right:
                self.column = col
                self.x = text_width_acc[col] - text_width[col]
            else:
                self.column = col + 1
                self.x = text_width_acc[col]

    def is_first_line(self):  # 光标是否在第一行
        return self._is_first_line(self.row)

    def is_last_line(self):  # 光标是否在最后一行
        return self._is_last_line(self.row)

    def is_line_start(self):  # 光标是否在某一行的开始
        return self._is_line_start(self.column)

    def is_line_end(self):  # 光标是否在某一行的末尾
        return self._is_line_end(self.row, self.column)

    def cursor_last_line(self):  # 光标移到上一行末尾
        if not self.is_first_line():
            self.row -= 1  # 光标上移
            self.y -= self.font.line_height

            self.column = len(self.text[self.row])  # 光标移到这一行末尾
            self.x = self.line_width[self.row]

        return self.row, self.column

    def cursor_next_line(self):  # 光标移到下一行开头
        if not self.is_last_line():
            self.row += 1  # 光标下移
            self.y += self.font.line_height

            self.column = 0  # 光标移到这一行开头
            self.x = 0

        return self.row, self.column

    def cursor_left(self):  # 光标左移
        if self.is_line_start():  # 光标在一行开头
            self.cursor_last_line()
        else:
            self.column -= 1  # 光标左移
            self.x -= self.font.rendered_text_width[self.get_cursor_text()]

        return self.row, self.column

    def cursor_right(self):  # 光标右移
        if self.is_line_end():  # 光标在这一行末尾
            self.cursor_next_line()
        else:
            self.x += self.font.rendered_text_width[self.get_cursor_text()]
            self.column += 1  # 光标右移

        return self.row, self.column

    def cursor_up(self):  # 光标上移
        if not self.is_first_line():  # 光标不在第一行
            self.row -= 1  # 光标上移
            self.y -= self.font.line_height

            self.set_screen_pos(self.x, self.y)

        return self.row, self.column

    def cursor_down(self):  # 光标下移
        if not self.is_last_line():  # 光标不在最后一行
            self.row += 1  # 光标下移
            self.y += self.font.line_height

            self.set_screen_pos(self.x, self.y)

        return self.row, self.column

    def delete_char(self):
        if self.is_line_start() and self.is_first_line():
            return
        if not self.is_line_start():
            self.row, self.column, del_char = self.remove_char(self.row, self.column)
            self.x -= self.font.rendered_text_width[del_char]
            return

        self.column = len(self.text[self.row - 1])
        self.x = self.line_width[self.row - 1]

        self.y -= self.font.line_height
        self.row = self.remove_line_break_char(self.row)  # 删除换行符

    def add_string(self, string):
        self.x += self._add_string(self.row, self.column, string)
        self.column += len(string)

    def add_line_break_char(self):
        self._add_line_break_char(self.row, self.column)
        self.cursor_next_line()

    def add_text(self, text):
        lines = text.split('\n')
        if len(lines) == 1:
            self.add_string(lines[0])
            return
        width = self._add_text(self.row, self.column, lines)
        self.column = len(lines[-1])
        self.x = width

        self.row += len(lines) - 1
        self.y += (len(lines) - 1) * self.font.line_height
