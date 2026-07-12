from typing import List
from .font_renderer import FontRenderer


class TextManager:
    def __init__(self, text: str, font: FontRenderer):
        self.text: List[str] = text.split('\n')  # 输入的普通文字

        self.font: FontRenderer = font
        self.line_width = self.font.pre_render_text(text)  # 存储每一行行宽
        self.max_line_width = max(self.line_width)  # 最大行宽（动态维护）

    @staticmethod
    def is_first_line(row):  # 光标是否在第一行
        return row == 0

    def is_last_line(self, row):  # 光标是否在最后一行
        return row == len(self.text) - 1

    @staticmethod
    def is_line_start(column):  # 光标是否在某一行的开始
        return column == 0

    def is_line_end(self, row, column):  # 光标是否在某一行的末尾
        return column == len(self.text[row])

    def get_line_width(self, row):  # 返回某行的宽度（像素）
        return self.line_width[row]

    def remove_line_break_char(self, row):  # 删除某行开头的换行符
        assert not self.is_first_line(row)  # 须确保不是第一行

        current_row = row - 1

        self.text[current_row] += self.text.pop(row)  # 合并两行内容
        self.line_width[current_row] += self.line_width.pop(row)  # 合并行宽

        self.max_line_width = max(self.line_width[current_row], self.max_line_width)  # 重新计算最大宽度
        return current_row

    def remove_char(self, row, column):  # 删除某位置前的普通字符
        assert not self.is_line_start(column)  # 须确保不是一行的开头

        current_col = column - 1

        char_code = self.text[row][current_col]
        self.text[row] = (
            self.text[row][:current_col] +
            self.text[row][column:]
        )  # 去除这个字符

        self.line_width[row] -= self.font.pre_render_string(char_code)
        self.max_line_width = max(self.line_width)  # TODO: 时间复杂度高

        return row, current_col, char_code   # 删除后光标应处于的位置，以及删除的字符

    def add_line_break_char(self, row, column):  # 在光标处添加换行符
        # 获取光标前后的文本
        before_cursor_text = self.text[row][:column]
        after_cursor_text = self.text[row][column:]

        # 更新当前行的文本为光标前的部分
        self.text[row] = before_cursor_text
        self.line_width[row] = self.font.pre_render_string(before_cursor_text)

        # 在新行插入光标后的文本
        self.text.insert(row + 1, after_cursor_text)
        self.line_width.insert(row + 1, self.font.pre_render_string(after_cursor_text))

        self.max_line_width = max(self.line_width)  # TODO: 时间复杂度高

    def add_string(self, row, column, string):  # 添加文本（单行）
        current_line = self.text[row]
        self.text[row] = current_line[:column] + string + current_line[column:]

        string_width = self.font.pre_render_string(string)
        self.line_width[row] += string_width
        self.max_line_width = max(self.line_width[row], self.max_line_width)
        return string_width
