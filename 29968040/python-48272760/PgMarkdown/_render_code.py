from . import _html_label
import pygame


def render_code(self, font_normal_size: int, font_size: int, font_style: list, code: str):
    """
    初步绘制内联代码块
    :param self: MarkdownRenderer类
    :param font_normal_size: 根节点的字体（单位为 px ）
    :param font_size: 代码块父节点的字体（单位为 px ）
    :param font_style: 字体的样式（是否加粗、斜体等）
    :param code: 代码
    :return: 渲染后的画布
    """
    label = _html_label.code()
    data = label.data

    self_font_size: int = data.convert_units(label.font_size, font_size, font_normal_size)  # 代码块内字体大小
    data.calc_style(self_font_size, font_normal_size)  # 计算边框、背景等样式
    font = self.set_font(self_font_size, font_style)  # 设置字体

    code_surface = font.render(code, True, (0, 0, 0))
    sf_left = data.margin_left + data.border_left_width + data.padding_left
    sf_right = data.margin_right + data.border_right_width + data.padding_right
    sf_top = data.border_top_width + data.padding_top
    sf_bottom = data.padding_bottom + data.border_bottom_width
    sf_width = sf_left + code_surface.get_width() + sf_right - data.margin_right - data.margin_left
    surface = pygame.Surface((sf_left + code_surface.get_width() + sf_right,
                              sf_top + code_surface.get_height() + sf_bottom),
                             pygame.SRCALPHA)
    pygame.draw.rect(surface, data.background_color,
                     (data.margin_left, data.margin_top, sf_width,
                      data.padding_top + code_surface.get_height() + data.padding_bottom),
                     border_radius=2)
    pygame.draw.rect(surface, data.border_left_color,
                     (data.margin_left, data.margin_top, sf_width,
                      data.padding_top + code_surface.get_height() + data.padding_bottom),
                     width=data.border_left_width, border_radius=2)
    surface.blit(code_surface, (data.margin_left + data.border_left_width + data.padding_left,
                                data.border_top_width+data.padding_top))
    return surface


def render_code_to_screen(self, x, y, end_x, line_start_x, font_size, font_style, block):
    """
    把内联代码块绘制到 screen(line-buffer) 里
    :param self: MarkdownRenderer类
    :param x: 当前行起始的 x 坐标
    :param y: 当前行起始的 y 坐标
    :param end_x: 结束 x 坐标
    :param line_start_x: 下一行起始的 x 坐标
    :param font_size: 代码块父节点的字体（单位为 px ）
    :param font_style: 字体的样式（是否加粗、斜体等）
    :param block: 当前的标签数据
    :return: 渲染完成后的x,y
    """
    code_surface = self.render_code(self.font_normal_size, font_size, font_style, block.contents[0])
    csf_width, csf_height = code_surface.get_width(), code_surface.get_height()
    if x != line_start_x and x + csf_width > end_x:  # 这个代码块不是这一行第一个字符，而且这个代码块宽度超长
        last_line_height = self.return_line()  # 强制闭合上一行
        x = line_start_x  # 重设 x 坐标
        y += last_line_height  # 更新 y 坐标
        self.line_buffer = [[x, y, 0], ['code', code_surface, font_size * 1.5, None]]  # 清空行缓冲
    else:
        if x == line_start_x or (len(self.line_buffer) == 0 or self.line_buffer[0][0] is None):
            self.line_buffer = [[x, y, 0]]
        self.line_buffer.append(['code', code_surface, font_size * 1.5, None])
    x += csf_width
    return x, y


def render_pre_code(self, text, font_size, font_style, line_height, start_x, start_y):
    if text[-1] == '\n':
        text = text[:-1]
    text = text.split('\n')
    font = self.set_font(font_size, font_style)
    line_height *= font_size
    x, y = start_x, start_y
    # surface = pygame.Surface((end_x-start_x, self.h), pygame.SRCALPHA)

    for word in text:
        font_surface = font.render(word, True, (0, 0, 0))
        # self.text_screen.blit(font_surface, (x, y + (line_height - font_surface.get_height()) / 2))
        self.render_queue_text_screen.append([font_surface, (x, y + (line_height - font_surface.get_height()) / 2), None])
        y += line_height
    return x, y
