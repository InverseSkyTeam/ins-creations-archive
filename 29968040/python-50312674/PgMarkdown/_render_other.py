import pygame
import webbrowser as wb


def return_line(self):
    # 把行缓冲区里的东西绘制出来
    if len(self.line_buffer) <= 1:
        return 0
    x, y = self.line_buffer[0]  # line_buffer 的第一个元素是这一行的起始位置以及偏移位置
    line_buffer = self.line_buffer[1:]
    line_height = max([i['height'] for i in line_buffer])  # 最大行高
    text_height = max([(0 if i['name'] == 'img' else i['height']) for i in line_buffer])
    y += (line_height - text_height)

    if self.render_num:  # 绘制无序列表前的圆点
        num_x = x-5-self.render_num.get_width()
        num_y = y + (text_height - self.render_num.get_height()) / 2
        self.render_queue_text_screen.append({
            'name': 'text',
            'surface': self.render_num,
            'pos': (num_x, num_y),
            'href': None,
            'hover': None
        })
        self.render_num = None

    for i, sf in enumerate(line_buffer):
        new_x, new_y = x, y + (text_height - sf['surface'].get_height()) / 2  # 绘制位置在该行正中间
        if sf['name'] == 'img': new_x, new_y = x, y + text_height - sf['img_height'];
        self.render_queue_text_screen.append({
            'name': 'surface',
            'surface': sf['surface'],
            'pos': (new_x, new_y),
            'href': sf['href'],
            'hover': sf['hover']
        })
        x += sf['surface'].get_width()  # 更新 x 坐标
    return line_height


def render_br(self, x, y, line_start_x):
    # 强制换行，用于br标签
    last_line_height = self.return_line()  # 强制闭合上一行
    x = line_start_x  # 重设 x 坐标
    y += last_line_height  # 更新 y 坐标
    self.line_buffer = [[x, y]]  # 清空 line-buffer
    return x, y
