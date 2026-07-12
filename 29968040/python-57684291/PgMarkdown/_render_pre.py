import pygame
import bs4
from .util.pre_style import get_style
from .util.scroll_bar import HScrollBar


class PreCode:
    def __init__(self, code, font_size, data, max_width):
        self.data = data
        self.max_width = max_width  # 最大宽度
        self.render_queue: list = []  # 绘制队列
        self.font_size = font_size  # 字体大小
        self.font = pygame.font.Font('CHSansSC.ttf', round(font_size))  # 加载字体
        self.line_height = int(1.5*font_size)
        _, self.height, self.width = self.read(0, 0, code, 0)
        self.width += data.padding_left + data.padding_right
        self.rect = pygame.Rect(0, 0, self.max_width, self.height + data.padding_top + data.padding_bottom)
        self.scroll = HScrollBar(self.rect)
        self.scroll.update_content_length(self.width)

    def render(self, screen, x, y, pygame_events, max_h):
        self.rect.x, self.rect.y = x, y
        y += self.data.padding_top
        self.scroll.update_rect(self.rect)
        sf = pygame.Surface((self.max_width, self.height), pygame.SRCALPHA)
        for i in self.render_queue:
            rx, ry = i[1][0]+self.data.padding_left-self.scroll.offset, i[1][1]
            if rx > self.max_width or y+ry > max_h or y+ry+i[0].get_height() < 0:  # 当渲染位置不在渲染区域内直接跳过
                continue
            sf.blit(i[0], (rx, ry))
        screen.blit(sf, (x, y))
        self.scroll.render(screen)
        self.scroll.handle_event(pygame_events)
    
    def read_line(self, line, x, y, width, color):
        # 使用指定的字体渲染传入的文本行，并去除行尾的回车符（\r）
        code_sf = self.font.render(line.rstrip('\r'), True, color)
        
        # 将渲染后的文本添加到渲染队列，并使文本垂直居中
        self.render_queue.append([code_sf, (x, y + (self.line_height - code_sf.get_height()) / 2)])
        
        # 返回文本末尾的横坐标(new_x) 和当前整个代码块的最大宽度
        new_x = x + code_sf.get_width()
        return new_x, max(width, new_x)

    def read(self, x, y, code, width, style=None):
        # 遍历传入的代码块（可以是字符串或嵌套的标签）
        for i, block in enumerate(code):
            # 如果当前块是一个文本字符串，则处理文本
            if isinstance(block, bs4.element.NavigableString):
                # 将文本按换行符分割成多行
                txt = str(block).split('\n')
                
                # 获取文本样式的颜色
                color = get_style(style)
                
                # 渲染并显示文本的第一行
                x, width = self.read_line(txt[0], x, y, width, color)
                
                # 渲染其余的行，每一行需要增加y坐标（行高）
                for line in txt[1:]:
                    y += self.line_height  # 增加y坐标以显示下一行
                    x, width = self.read_line(line, 0, y, width, color)  # x重置为0，从新的一行开始
            else:
                # 如果当前块是一个标签元素，递归调用read方法处理其内容
                # 获取标签的类名（即标签的样式名）
                x, y, width = self.read(x, y, block.contents, width, block.get('class')[0])
        return x, y, width
