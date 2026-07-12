import pygame
import webbrowser as wb


def return_line(self):
    # 把行缓冲区里的东西绘制出来
    if len(self.line_buffer) <= 1:
        return 0
    x, y, offest_y = self.line_buffer[0]  # line_buffer 的第一个元素是这一行的起始位置以及偏移位置
    y += offest_y
    line_buffer = self.line_buffer[1:]
    line_height = max([i[2] for i in line_buffer])  # 最大行高
    if self.render_num:
        num_x = x-5-self.render_num.get_width()
        num_y = y + (line_height - self.render_num.get_height()) / 2
        # self.text_screen.blit(self.render_num, (num_x, num_y))
        self.render_queue_text_screen.append([self.render_num, (num_x, num_y), None])
        self.render_num = None
    for i, sf in enumerate(line_buffer):
        new_x, new_y = x, y + (line_height - sf[1].get_height()) / 2
        '''if sf[3] and self.mouse_pressed and \
           pygame.Rect(new_x, new_y, sf[1].get_width(), sf[1].get_height()).collidepoint((self.mouse_x, self.mouse_y)):
            wb.open(sf[3])'''
        # self.text_screen.blit(sf[1], [new_x, new_y])
        self.render_queue_text_screen.append([sf[1], (new_x, new_y), sf[3]])
        x += sf[1].get_width()
    return offest_y + line_height


def render_br(self, x, y, line_start_x):
    # 强制换行，用于br标签
    last_line_height = self.return_line()  # 强制闭合上一行
    x = line_start_x  # 重设 x 坐标
    y += last_line_height  # 更新 y 坐标
    self.line_buffer = [[x, y, 0]]  # 清空 line-buffer
    return x, y
