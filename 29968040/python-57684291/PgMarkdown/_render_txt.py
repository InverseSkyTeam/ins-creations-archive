import pygame


def binary_render(font, txt, width, width1):
    # 二分渲染文字
    l, r = 0, len(txt)
    while l < r:
        mid = (l+r)//2
        if font.size(txt[:mid+1])[0] > width:
            r = mid
        else:
            l = mid + 1
    if width == width1 and l == 0:
        return min(len(txt), 1)
    return l


def render_txt_new(self, start_x, start_y, end_x, line_start_x,
                   text, font_size: int, font_color, font_style, href=None):
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
    font = self.font.get_font(font_size, font_style)  # 设置字体
    text = text.replace('\n', ' ')  # 把换行替换为空格
    line_height = font_size * 1.5  # 行高

    x, y = start_x, start_y  # 起始 x, y 坐标
    if start_x == line_start_x or (len(self.line_buffer) == 0 or self.line_buffer[0][0] is None):
        self.line_buffer[0] = [start_x, start_y]  # 这个是这一行第一个块，强制初始化

    if end_x == 2147483647:  # 无需换行
        self.line_buffer.append({
            'name': 'text',
            'surface': font.render(text, True, font_color),
            'height': line_height,  # 元素的实际占用高度
            'href': href,
            'hover': href and font.render(text, True, self.color_href_hover)
        })
        return x + font.size(text)[0], y

    # 开始渲染
    while True:
        length = binary_render(font, text, end_x - x, end_x - start_x)
        if length == len(text):
            break
        self.line_buffer.append({
            'name': 'text',
            'surface': font.render(text[:length], True, font_color),
            'height': line_height,
            'href': href,
            'hover': href and font.render(text[:length], True, self.color_href_hover),
        })
        line_new_height = self.return_line()  # 绘制一整行
        x = line_start_x  # 重设 x 坐标
        y += line_new_height  # 更新 y 坐标
        self.line_buffer = [[x, y]]  # 清空行缓冲
        text = text[length:]
    self.line_buffer.append({
        'name': 'text',
        'surface': font.render(text, True, font_color),
        'height': line_height,
        'href': href,
        'hover': href and font.render(text, True, self.color_href_hover),
    })
    return x + font.size(text)[0], y


def render_txt_old(self, start_x, start_y, end_x, line_start_x,
                   text, font_size: int, font_color, font_style, href=None):
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
    font = self.font.get_font(font_size, font_style)  # 设置字体
    text = text.replace('\n', ' ')  # 把换行替换为空格
    line_height = font_size * 1.5  # 行高

    current_line = ""  # 缓存文字
    x, y = start_x, start_y  # 起始 x, y 坐标
    if start_x == line_start_x or (len(self.line_buffer) == 0 or self.line_buffer[0][0] is None):
        self.line_buffer[0] = [start_x, start_y]  # 这个是这一行第一个块，强制初始化

    # 开始渲染
    for word in text:
        if end_x == 2147483647:
            current_line = text
            break
        temp_line = current_line + word if current_line != "" else word  # 加入一个新字符
        if font.size(temp_line)[0] > end_x - x:  # 当加入这个字符后要换行
            # 把最后一块字符加入 line-buffer 里
            self.line_buffer.append({
                'name': 'text',
                'surface': font.render(current_line, True, font_color),
                'height': line_height,
                'href': href,
                'hover': href and font.render(current_line, True, self.color_href_hover),
            })
            line_new_height = self.return_line()  # 绘制一整行
            x = line_start_x  # 重设 x 坐标
            y += line_new_height  # 更新 y 坐标
            self.line_buffer = [[x, y]]  # 清空行缓冲
            current_line = word
        else:
            current_line = temp_line
    # 在最后一块没有换行，直接加入行缓冲区内
    self.line_buffer.append({
        'name': 'text',
        'surface': font.render(current_line, True, font_color),
        'height': line_height,
        'href': href,
        'hover': href and font.render(current_line, True, self.color_href_hover),
    })
    return x + font.size(current_line)[0], y


render_txt = render_txt_new
