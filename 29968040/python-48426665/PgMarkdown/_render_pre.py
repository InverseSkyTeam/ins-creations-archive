import pygame
import bs4


css_style = {'c': {'color': (64, 128, 128), 'font-style': 'italic'}, 'err': {'color': (255, 0, 0)}, 'k': {'color': (0, 128, 0), 'font-weight': 'bold'}, 'o': {'color': (102, 102, 102)}, 'ch': {'color': (64, 128, 128), 'font-style': 'italic'}, 'cm': {'color': (64, 128, 128), 'font-style': 'italic'}, 'cp': {'color': (188, 122, 0)}, 'cpf': {'color': (64, 128, 128), 'font-style': 'italic'}, 'c1': {'color': (64, 128, 128), 'font-style': 'italic'}, 'cs': {'color': (64, 128, 128), 'font-style': 'italic'}, 'gd': {'color': (160, 0, 0)}, 'ge': {'color': (0, 0, 0), 'font-style': 'italic'}, 'gr': {'color': (255, 0, 0)}, 'gh': {'color': (0, 0, 128), 'font-weight': 'bold'}, 'gi': {'color': (0, 160, 0)}, 'go': {'color': (136, 136, 136)}, 'gp': {'color': (0, 0, 128), 'font-weight': 'bold'}, 'gs': {'color': (0, 0, 128), 'font-weight': 'bold'}, 'gu': {'color': (128, 0, 128), 'font-weight': 'bold'}, 'gt': {'color': (0, 68, 221)}, 'kc': {'color': (0, 128, 0), 'font-weight': 'bold'}, 'kd': {'color': (0, 128, 0), 'font-weight': 'bold'}, 'kn': {'color': (0, 128, 0), 'font-weight': 'bold'}, 'kp': {'color': (0, 128, 0)}, 'kr': {'color': (0, 128, 0), 'font-weight': 'bold'}, 'kt': {'color': (176, 0, 64)}, 'm': {'color': (102, 102, 102)}, 's': {'color': (186, 33, 33)}, 'na': {'color': (125, 144, 41)}, 'nb': {'color': (0, 128, 0)}, 'nc': {'color': (0, 0, 255), 'font-weight': 'bold'}, 'no': {'color': (136, 0, 0)}, 'nd': {'color': (170, 34, 255)}, 'ni': {'color': (153, 153, 153), 'font-weight': 'bold'}, 'ne': {'color': (210, 65, 58), 'font-weight': 'bold'}, 'nf': {'color': (0, 0, 255)}, 'nl': {'color': (160, 160, 0)}, 'nn': {'color': (0, 0, 255), 'font-weight': 'bold'}, 'nt': {'color': (0, 128, 0), 'font-weight': 'bold'}, 'nv': {'color': (25, 23, 124)}, 'ow': {'color': (170, 34, 255), 'font-weight': 'bold'}, 'w': {'color': (187, 187, 187)}, 'mb': {'color': (102, 102, 102)}, 'mf': {'color': (102, 102, 102)}, 'mh': {'color': (102, 102, 102)}, 'mi': {'color': (102, 102, 102)}, 'mo': {'color': (102, 102, 102)}, 'sa': {'color': (186, 33, 33)}, 'sb': {'color': (186, 33, 33)}, 'sc': {'color': (186, 33, 33)}, 'dl': {'color': (186, 33, 33)}, 'sd': {'color': (186, 33, 33), 'font-style': 'italic'}, 's2': {'color': (186, 33, 33)}, 'se': {'color': (187, 102, 34), 'font-weight': 'bold'}, 'sh': {'color': (186, 33, 33)}, 'si': {'color': (187, 102, 136), 'font-weight': 'bold'}, 'sx': {'color': (0, 128, 0)}, 'sr': {'color': (187, 102, 136)}, 's1': {'color': (186, 33, 33)}, 'ss': {'color': (25, 23, 124)}, 'bp': {'color': (0, 128, 0)}, 'fm': {'color': (0, 0, 255)}, 'vc': {'color': (25, 23, 124)}, 'vg': {'color': (25, 23, 124)}, 'vi': {'color': (25, 23, 124)}, 'vm': {'color': (25, 23, 124)}, 'il': {'color': (102, 102, 102)}}


def get_style(name):
    if name in css_style:
        return css_style[name]['color']
    else:
        return 0, 0, 0


class PreCode:
    def __init__(self, code, font_size, data, max_width):
        self.data = data
        self.max_width = max_width
        self.render_queue: list = []
        self.font_size = font_size
        self.font = pygame.font.Font('HarmonyOS_Sans_SC_Regular.ttf', round(font_size))
        self.line_height = 1.5*font_size
        self.width = 0
        _, self.height = self.read(0, 0, code)
        self.width += data.padding_left + data.padding_right
        self.contentScrollLength = 0  # 内容滚动的距离
        self.scrollbarLength = 0  # 滚动条滚动的距离
        self.scroll_color = (153, 153, 153)
        self.offest_x = None
        self.scroll_dragging = False  # 是否在拖动滚动条
        self.x, self.y = None, None
        if self.width > max_width:
            self.scrollbar = pygame.Rect(0, 0, max_width / self.width * max_width, 5)
        else:
            self.scrollbar = None

    def scrollbarLength_contentScrollLength(self, scrollbarLength):
        return (self.width - self.max_width) / (self.max_width - self.scrollbar.width) * scrollbarLength

    def handle_mouse_scroll(self, mouse_x):
        new_x = mouse_x - self.offest_x
        self.scrollbar.x = max(self.x, min(self.x + self.max_width - self.scrollbar.width, new_x))
        self.contentScrollLength = self.scrollbarLength_contentScrollLength(self.scrollbar.x - self.x)
        self.scrollbarLength = self.scrollbar.x - self.x

    def render(self, screen, x, y, pygame_events, mouse_x, mouse_y, mouse_pressed, yy, hh):
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
            pygame.draw.rect(screen, self.scroll_color, self.scrollbar, border_radius=2)
            for event in pygame_events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.scrollbar is not None and self.scrollbar.collidepoint(mouse_x, mouse_y):
                            self.scroll_dragging = True
                            self.offest_x = mouse_x - self.scrollbar.x
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.scroll_dragging = False
                        self.offest_x = 0
            if mouse_pressed and self.scroll_dragging:
                self.handle_mouse_scroll(mouse_x)

    def read(self, x, y, code, style=None):
        for i, block in enumerate(code):
            if isinstance(block, bs4.element.NavigableString):
                txt = str(block).split('\n')
                for j in txt[:-1]:
                    code_sf = self.font.render(j, True, get_style(style))
                    self.render_queue.append([code_sf, (x, y + (self.line_height - code_sf.get_height()) / 2)])
                    x += code_sf.get_width()
                    self.width = max(self.width, x)
                    x = 0
                    y += self.line_height
                code_sf = self.font.render(txt[-1], True, get_style(style))
                # print(code_sf.get_width(), code_sf.get_height())
                self.render_queue.append([code_sf, (x, y + (self.line_height - code_sf.get_height()) / 2)])
                x += code_sf.get_width()
                self.width = max(self.width, x)
                # print(self.width)
            else:
                x, y = self.read(x, y, block.contents, block.get('class')[0])
        return x, y
