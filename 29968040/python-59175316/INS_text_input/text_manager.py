from typing import List
from .font_renderer import FontRenderer


class TextManager:
    def __init__(self, text: str, font: FontRenderer):
        self.text: List[str] = text.split('\n')  # 输入的普通文字

        self.font: FontRenderer = font
        self.line_width = self.font.pre_render_text(text)  # 存储每一行行宽
        self.max_line_width = max(self.line_width)  # 最大行宽（动态维护）

    def get_line_width(self, row):  # 返回某行的宽度（像素）
        return self.line_width[row]

    @staticmethod
    def _is_first_line(row):  # 光标是否在第一行
        return row == 0

    def _is_last_line(self, row):  # 光标是否在最后一行
        return row == len(self.text) - 1

    @staticmethod
    def _is_line_start(column):  # 光标是否在某一行的开始
        return column == 0

    def _is_line_end(self, row, column):  # 光标是否在某一行的末尾
        return column == len(self.text[row])

    def _add_line_break_char(self, row, column):  # 在光标处添加换行符
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

    def _add_string(self, row, column, string):  # 添加文本（单行）
        current_line = self.text[row]
        self.text[row] = current_line[:column] + string + current_line[column:]

        string_width = self.font.pre_render_string(string)
        self.line_width[row] += string_width
        self.max_line_width = max(self.line_width[row], self.max_line_width)
        return string_width

    def _add_text(self, row, column, lines):
        assert len(lines) > 1  # 需保证不止一行

        self._add_line_break_char(row, column)
        self._add_string(row, column, lines[0])

        width_last = self._add_string(row + 1, 0, lines[-1])
        if len(lines) == 2:
            return width_last

        mid_lines = lines[1: -1]
        self.text = self.text[:row + 1] + mid_lines + self.text[row + 1:]

        mid_lines_width = self.font.pre_render_text(mid_lines, False)
        self.line_width = self.line_width[:row + 1] + mid_lines_width + self.line_width[row + 1:]
        self.max_line_width = max(max(mid_lines_width), self.max_line_width)

        return width_last

    def remove_line_break_char(self, row):  # 删除某行开头的换行符
        assert not self._is_first_line(row)  # 须确保不是第一行

        current_row = row - 1

        self.text[current_row] += self.text.pop(row)  # 合并两行内容
        self.line_width[current_row] += self.line_width.pop(row)  # 合并行宽

        self.max_line_width = max(self.line_width[current_row], self.max_line_width)  # 重新计算最大宽度
        return current_row

    def remove_char(self, row, column):  # 删除某位置前的普通字符
        assert not self._is_line_start(column)  # 须确保不是一行的开头

        current_col = column - 1

        char_code = self.text[row][current_col]
        self.text[row] = (
            self.text[row][:current_col] +
            self.text[row][column:]
        )  # 去除这个字符

        self.line_width[row] -= self.font.pre_render_string(char_code)
        self.max_line_width = max(self.line_width)  # TODO: 时间复杂度高

        return row, current_col, char_code   # 删除后光标应处于的位置，以及删除的字符

    def delete_string(self, row, col1, col2, update_max_line_width=True):
        string = self.text[row][col1:col2]
        self.text[row] = (
                self.text[row][:col1] +
                self.text[row][col2:]
        )  # 去除这个字符

        self.line_width[row] -= self.font.pre_render_string(string)
        if update_max_line_width:
            self.max_line_width = max(self.line_width)  # TODO: 时间复杂度高

    def delete_text(self, begin, end):
        assert begin != end
        begin, end = min(begin, end), max(begin, end)

        if begin[0] == end[0]:
            self.delete_string(begin[0], begin[1], end[1])
            return

        row0, row1 = begin[0], end[0]
        col0, col1 = begin[1], end[1]

        self.delete_string(row0, col0, len(self.text[row0]), False)
        self.delete_string(row1, 0, col1, False)

        del self.text[row0 + 1: row1]
        del self.line_width[row0 + 1: row1]

        self.max_line_width = max(self.line_width)
        self.remove_line_break_char(row0 + 1)

    def get_text(self, begin, end):
        if begin == end:
            return ''

        begin, end = min(begin, end), max(begin, end)
        row0, row1 = begin[0], end[0]
        col0, col1 = begin[1], end[1]

        if row0 == row1:
            return self.text[row0][col0:col1]

        s = self.text[row0][col0:]
        e = self.text[row1][:col1]

        if row1 - row0 == 1:
            return s + '\n' + e

        mid = '\n'.join(self.text[row0 + 1: row1])
        return s + '\n' + mid + '\n' + e
