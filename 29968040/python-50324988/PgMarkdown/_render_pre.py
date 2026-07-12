import pygame
import bs4


# 用于存储代码样式
css_style = {'hll': {'background-color': '#ffffcc'}, 'highlight': {'background': '#ffffff'}, 'c': {'color': '#177500'}, 'err': {'color': '#000000'}, 'k': {'color': '#A90D91'}, 'l': {'color': '#1C01CE'}, 'n': {'color': '#000000'}, 'o': {'color': '#000000'}, 'ch': {'color': '#177500'}, 'cm': {'color': '#177500'}, 'cp': {'color': '#633820'}, 'cpf': {'color': '#177500'}, 'c1': {'color': '#177500'}, 'cs': {'color': '#177500'}, 'kc': {'color': '#A90D91'}, 'kd': {'color': '#A90D91'}, 'kn': {'color': '#A90D91'}, 'kp': {'color': '#A90D91'}, 'kr': {'color': '#A90D91'}, 'kt': {'color': '#A90D91'}, 'ld': {'color': '#1C01CE'}, 'm': {'color': '#1C01CE'}, 's': {'color': '#C41A16'}, 'na': {'color': '#836C28'}, 'nb': {'color': '#A90D91'}, 'nc': {'color': '#3F6E75'}, 'no': {'color': '#000000'}, 'nd': {'color': '#000000'}, 'ni': {'color': '#000000'}, 'ne': {'color': '#000000'}, 'nf': {'color': '#000000'}, 'nl': {'color': '#000000'}, 'nn': {'color': '#000000'}, 'nx': {'color': '#000000'}, 'py': {'color': '#000000'}, 'nt': {'color': '#000000'}, 'nv': {'color': '#000000'}, 'ow': {'color': '#000000'}, 'mb': {'color': '#1C01CE'}, 'mf': {'color': '#1C01CE'}, 'mh': {'color': '#1C01CE'}, 'mi': {'color': '#1C01CE'}, 'mo': {'color': '#1C01CE'}, 'sa': {'color': '#C41A16'}, 'sb': {'color': '#C41A16'}, 'sc': {'color': '#2300CE'}, 'dl': {'color': '#C41A16'}, 'sd': {'color': '#C41A16'}, 's2': {'color': '#C41A16'}, 'se': {'color': '#C41A16'}, 'sh': {'color': '#C41A16'}, 'si': {'color': '#C41A16'}, 'sx': {'color': '#C41A16'}, 'sr': {'color': '#C41A16'}, 's1': {'color': '#C41A16'}, 'ss': {'color': '#C41A16'}, 'bp': {'color': '#5B269A'}, 'fm': {'color': '#000000'}, 'vc': {'color': '#000000'}, 'vg': {'color': '#000000'}, 'vi': {'color': '#000000'}, 'vm': {'color': '#000000'}, 'il': {'color': '#1C01CE'}}


def get_style(name):
    # 获取样式的颜色，获取不到就是黑色
    if name in css_style and 'color' in css_style[name]:
        return css_style[name]['color']
    else:
        return 63, 63, 63


def calc_colors(opaque_color, transparent_color):
    opaque_r, opaque_g, opaque_b = opaque_color
    alpha = transparent_color[3]
    result_r = ((1 - alpha) * opaque_r + alpha * transparent_color[0])
    result_g = ((1 - alpha) * opaque_g + alpha * transparent_color[1])
    result_b = ((1 - alpha) * opaque_b + alpha * transparent_color[2])

    return int(result_r), int(result_g), int(result_b)


class PreCode:
    def __init__(self, code, font_size, data, max_width):
        # print(code)
        self.data = data
        self.max_width = max_width  # 最大宽度
        self.render_queue: list = []  # 绘制队列
        self.font_size = font_size  # 字体大小
        self.font = pygame.font.SysFont('SimHei', round(font_size))  # 加载字体
        self.line_height = 1.5*font_size
        self.width = 0
        self.height = self.read(0, 0, code)[1]
        self.width += data.padding_left + data.padding_right
        self.contentScrollLength = 0  # 内容滚动的距离
        self.scrollbarLength = 0  # 滚动条滚动的距离
        self.scroll_color_normal = calc_colors((255, 255, 255), (0, 0, 0, 0.25))  # 滚动条颜色
        self.scroll_color_hover = calc_colors((255, 255, 255), (0, 0, 0, 0.4))  # 鼠标悬停颜色
        self.scroll_color = self.scroll_color_normal
        self.scroll_dragging = False  # 是否在拖动滚动条
        self.x, self.y = None, None
        if self.width > max_width:
            self.scrollbar = pygame.Rect(0, 0, max_width / self.width * max_width, 5)
        else:
            self.scrollbar = None

    def scrollbarLength_contentScrollLength(self, scrollbarLength):
        return (self.width - self.max_width) / (self.max_width - self.scrollbar.width) * scrollbarLength

    def render(self, screen, x, y, pygame_events, mouse_x, mouse_y, yy, hh):
        if self.scrollbar is None:
            self.scrollbarLength = self.contentScrollLength = 0
        self.x, self.y = x, y
        sf = pygame.Surface((self.max_width, self.height), pygame.SRCALPHA)
        for i in self.render_queue:
            rx, ry = i[1][0]+self.data.padding_left-self.contentScrollLength, i[1][1]
            if rx > self.max_width or y+ry > yy+hh or y+ry+i[0].get_height() < yy:  # 剪枝，当渲染位置不在渲染区域内直接跳过
                continue
            sf.blit(i[0], (rx, ry))
        screen.blit(sf, (x, y))
        if self.scrollbar is not None:
            self.scrollbar.x, self.scrollbar.y = x + self.scrollbarLength, y+self.height+self.data.padding_bottom-self.scrollbar.height
            self.scrollbar.x = max(self.x, min(self.x + self.max_width - self.scrollbar.width, self.scrollbar.x))
            self.contentScrollLength = self.scrollbarLength_contentScrollLength(self.scrollbar.x - self.x)
            self.scrollbarLength = self.scrollbar.x - self.x
            if self.scrollbar.collidepoint(mouse_x, mouse_y) or self.scroll_dragging:
                self.scroll_color = self.scroll_color_hover
            else:
                self.scroll_color = self.scroll_color_normal
            pygame.draw.rect(screen, self.scroll_color, self.scrollbar, border_radius=2)
            for event in pygame_events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.scrollbar is not None and self.scrollbar.collidepoint(mouse_x, mouse_y):
                            self.scroll_dragging = True
                if event.type == pygame.MOUSEMOTION:
                    if self.scroll_dragging:
                        self.scrollbar.move_ip(event.rel[0], 0)
                        self.scrollbar.x = max(self.x, min(self.x + self.max_width - self.scrollbar.width, self.scrollbar.x))
                        self.contentScrollLength = self.scrollbarLength_contentScrollLength(self.scrollbar.x - self.x)
                        self.scrollbarLength = self.scrollbar.x - self.x
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.scroll_dragging = False

    def read(self, x, y, code, style=None):
        for i, block in enumerate(code):
            if isinstance(block, bs4.element.NavigableString):
                txt = str(block).split('\n')
                for j in range(len(txt)):
                    if len(txt[j]) and txt[j][-1] == '\r':
                        txt[j] = txt[j][:-1]
                for j in txt[:-1]:
                    code_sf = self.font.render(j, True, get_style(style))
                    self.render_queue.append([code_sf, (x, y + (self.line_height - code_sf.get_height()) / 2)])
                    x += code_sf.get_width()
                    self.width = max(self.width, x)
                    x = 0
                    y += self.line_height
                code_sf = self.font.render(txt[-1], True, get_style(style))
                self.render_queue.append([code_sf, (x, y + (self.line_height - code_sf.get_height()) / 2)])
                x += code_sf.get_width()
                self.width = max(self.width, x)
            else:
                x, y = self.read(x, y, block.contents, block.get('class')[0])
        return x, y
