import pygame


def render_txt(self, start_x, start_y, end_x, line_start_x,
               text, font_size: int, font_color, font_style, is_href, href=None):
    """
    绘制普通文字
    :param self: MarkdownRenderer类
    :param start_x: 当前行起始的 x 坐标
    :param start_y: 当前行起始的 y 坐标
    :param end_x: 结束 x 坐标
    :param line_start_x: 下一行起始的 x 坐标
    :param text: 渲染的文字
    :param font_size: 渲染的字体大小（单位为 px ）
    :param font_color: 渲染的字体颜色
    :param font_style: 渲染的字体样式
    :param is_href: 是否是链接
    :param href: 链接
    :return: 渲染最后一行的结束 x 坐标, 渲染后最后一行的起始 y 坐标
    """
    font = self.set_font(font_size, font_style)
    text = text.replace('\n', ' ')
    line_height = font_size * 1.5

    current_line = ""
    x, y = start_x, start_y
    if start_x == line_start_x or (len(self.line_buffer) == 0 or self.line_buffer[0][0] is None):
        self.line_buffer[0] = [start_x, start_y, 0]  # 这个是这一行第一个块，强制初始化
    for word in text:
        temp_line = current_line + word if current_line != "" else word
        if font.size(temp_line)[0] > end_x - x:  # 再加新字符就要换行了
            # 把最后一块字符加入 line-buffer 里
            self.line_buffer.append(['text', font.render(current_line, True, font_color), line_height, href])
            if is_href:
                self.line_buffer[-1].append(font.render(current_line, True, self.color_href_hover))
            line_new_height = self.return_line()  # 绘制一整行
            x = line_start_x  # 重设 x 坐标
            y += line_new_height  # 更新 y 坐标
            self.line_buffer = [[x, y, 0]]  # 清空行缓冲
            current_line = word
        else:
            current_line = temp_line
    # 在最后一块没有换行，直接加入行缓冲区内
    self.line_buffer.append(['text', font.render(current_line, True, font_color), line_height, href])
    if is_href:
        self.line_buffer[-1].append(font.render(current_line, True, self.color_href_hover))
    return x + font.size(current_line)[0], y
