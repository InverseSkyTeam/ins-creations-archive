import pygame
import webbrowser as wb


def render_data(screen, x, y, data, mouse_x, mouse_y, mouse_pressed):
    for i in data:
        idx, idy = x+i['pos'][0], y+i['pos'][1]
        if idx > screen.get_width() or idy > screen.get_height():
            continue
        if idx+i['surface'].get_width() < 0 or idy+i['surface'].get_height() < 0:
            continue
        if i['href'] and pygame.Rect(idx, idy, i['surface'].get_width(), i['surface'].get_height()) \
           .collidepoint((mouse_x, mouse_y)):
            screen.blit(i['hover'], (idx, idy))
            if mouse_pressed:
                wb.open(i['href'])
            continue
        screen.blit(i['surface'], (idx, idy))


def calc_colors(opaque_color, transparent_color):
    opaque_r, opaque_g, opaque_b = opaque_color
    alpha = transparent_color[3]
    result_r = ((1 - alpha) * opaque_r + alpha * max(min(transparent_color[0], 255), 0))
    result_g = ((1 - alpha) * opaque_g + alpha * max(min(transparent_color[1], 255), 0))
    result_b = ((1 - alpha) * opaque_b + alpha * max(min(transparent_color[2], 255), 0))

    return int(result_r), int(result_g), int(result_b)


class Table:
    def __init__(self, font_size, data, max_width, height):
        self.data = data
        self.font_size = font_size
        self.max_width = max_width
        self.height = height
        self.data_width = [max([data[line][lie][0] for line in range(len(data))]) for lie in range(len(data[0]))]
        self.data_height = [max([dd[1] for dd in line]) for line in data]
        self.width = sum([i+13*2+1 for i in self.data_width])+1
        self.contentScrollLength = 0  # 内容滚动的距离
        self.scrollbarLength = 0  # 滚动条滚动的距离
        self.scroll_color_normal = calc_colors((255, 255, 255), (0, 0, 0, 0.25))  # 滚动条颜色
        self.scroll_color_hover = calc_colors((255, 255, 255), (0, 0, 0, 0.4))  # 鼠标悬停颜色
        self.scroll_color = self.scroll_color_normal
        self.scroll_dragging = False  # 是否在拖动滚动条
        if self.width > max_width:
            self.scrollbar = pygame.Rect(0, 0, max_width / self.width * max_width, 5)
        else:
            self.scrollbar = None

    def scrollbarLength_contentScrollLength(self, scrollbarLength):
        return (self.width - self.max_width) / (self.max_width - self.scrollbar.width) * scrollbarLength

    def render_table(self, pos, mouse_x, mouse_y, mouse_pressed):
        screen = pygame.Surface((self.max_width, self.height), pygame.SRCALPHA)
        data = self.data
        width = self.data_width
        height = self.data_height
        x, y = pos
        for new_y, h in enumerate(height):
            for new_x, w in enumerate(width):
                self_data = data[new_y][new_x]
                pygame.draw.rect(screen, (221, 221, 221), pygame.Rect(x, y, w + 2 + 13 * 2, h + 2 + 6 * 2), width=1)
                offset_x = 0
                if self_data[3] == 'text-align: center;':
                    offset_x = (w - self_data[0]) // 2
                if self_data[3] == 'text-align: right;':
                    offset_x = w - self_data[0]
                render_data(screen, x + 1 + 13 + offset_x, y + 1 + 6 + (h - self_data[1]) // 2, self_data[2],
                            mouse_x, mouse_y, mouse_pressed)
                x += w + 1 + 13 * 2
            x = pos[0]
            y += h + 1 + 6 * 2
        return screen

    def render(self, screen, pos, pygame_events, mouse_x, mouse_y):
        if self.scrollbar is None:
            self.scrollbarLength = self.contentScrollLength = 0
        mouse_pressed = 0
        for event in pygame_events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pressed = 1
        if self.scrollbar is not None:
            self.scrollbar.x, self.scrollbar.y = pos[0] + self.scrollbarLength, pos[1]+self.height-self.scrollbar.height
            self.scrollbar.x = max(pos[0], min(pos[0] + self.max_width - self.scrollbar.width, self.scrollbar.x))
            self.contentScrollLength = self.scrollbarLength_contentScrollLength(self.scrollbar.x - pos[0])
            self.scrollbarLength = self.scrollbar.x - pos[0]
            for event in pygame_events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.scrollbar is not None and self.scrollbar.collidepoint(mouse_x, mouse_y):
                            self.scroll_dragging = True
                if event.type == pygame.MOUSEMOTION:
                    if self.scroll_dragging:
                        self.scrollbar.move_ip(event.rel[0], 0)
                        self.scrollbar.x = max(pos[0], min(pos[0] + self.max_width - self.scrollbar.width, self.scrollbar.x))
                        self.contentScrollLength = self.scrollbarLength_contentScrollLength(self.scrollbar.x - pos[0])
                        self.scrollbarLength = self.scrollbar.x - pos[0]
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.scroll_dragging = False
        table_sf = self.render_table((-self.contentScrollLength, 0), mouse_x - pos[0], mouse_y - pos[1], mouse_pressed)
        screen.blit(table_sf, pos)
        if self.scrollbar is not None:
            if self.scrollbar.collidepoint(mouse_x, mouse_y) or self.scroll_dragging:
                self.scroll_color = self.scroll_color_hover
            else:
                self.scroll_color = self.scroll_color_normal
            pygame.draw.rect(screen, self.scroll_color, self.scrollbar, border_radius=2)
