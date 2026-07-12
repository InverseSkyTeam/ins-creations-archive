import pygame


def render_inline_LaTeX(self, x, y, end_x, line_start_x, font_size, block):
    """
    把内联LaTeX绘制到 screen(line-buffer) 里
    :param self: MarkdownRenderer类
    :param x: 当前行起始的 x 坐标
    :param y: 当前行起始的 y 坐标
    :param end_x: 结束 x 坐标
    :param line_start_x: 下一行起始的 x 坐标
    :param font_size: 代码块父节点的字体（单位为 px ）
    :param block: 当前的标签数据
    :return: 渲染完成后的x,y
    """
    LaTeX_surface = self.in_line_LaTeX[str(block.contents[0])]  # 获取已经预加载的公式图片
    if font_size / self.font_normal_size != 1:  # 当前字体大小不是正常大小
        LaTeX_width, LaTeX_height = LaTeX_surface.get_width(), LaTeX_surface.get_height()
        LaTeX_surface = pygame.transform.smoothscale(LaTeX_surface,
                                                     (round(LaTeX_width * font_size / self.font_normal_size),
                                                      round(LaTeX_height * font_size / self.font_normal_size)))
    LaTeX_width, LaTeX_height = LaTeX_surface.get_width(), LaTeX_surface.get_height()
    if x != line_start_x and x + LaTeX_width > end_x:  # 这个代码块不是这一行第一个字符，而且这个代码块宽度超长
        last_line_height = self.return_line()  # 强制闭合上一行
        x = line_start_x  # 重设 x 坐标
        y += last_line_height  # 更新 y 坐标
        self.line_buffer = [
            [x, y, 0],
            {
                'name': 'LaTeX',
                'surface': LaTeX_surface,
                'height': max(font_size * 1.5, LaTeX_height),
                'href': None,
                'hover': None
            }
        ]
    else:
        if x == line_start_x or (len(self.line_buffer) == 0 or self.line_buffer[0][0] is None):
            self.line_buffer = [[x, y, 0]]
        self.line_buffer.append({
            'name': 'LaTeX',
            'surface': LaTeX_surface,
            'height': max(font_size * 1.5, LaTeX_height),
            'href': None,
            'hover': None
        })
    x += LaTeX_width
    return x, y
