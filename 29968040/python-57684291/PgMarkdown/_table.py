import pygame
import webbrowser as wb
from .util.scroll_bar import HScrollBar


def render_data(screen, x, y, data, mouse_pos, mouse_pressed, rect):
    token = None
    for i in data:
        idx, idy = x + i['pos'][0], y + i['pos'][1]
        if i['href'] and pygame.Rect(idx, idy, i['surface'].get_width(), i['surface'].get_height()).collidepoint(mouse_pos) and pygame.Rect(0, 0, *rect.size).collidepoint(mouse_pos):
            token = i['href'].token
            if mouse_pressed:
                i['href'].open()
    for i in data:
        idx, idy = x+i['pos'][0], y+i['pos'][1]
        if idx > screen.get_width() or idy > screen.get_height():
            continue
        if idx+i['surface'].get_width() < 0 or idy+i['surface'].get_height() < 0:
            continue
        if i['href'] and i['href'].token == token:
            screen.blit(i['hover'], (idx, idy))
            continue
        screen.blit(i['surface'], (idx, idy))


class Table:
    def __init__(self, font_size, data, max_width, height):
        self.data = data
        self.font_size = font_size
        self.max_width = max_width
        self.height = height
        self.data_width = [max([data[line][lie]['rect'].w for line in range(len(data))]) for lie in range(len(data[0]))]
        self.data_height = [max([dd['rect'].h for dd in line]) for line in data]
        self.width = sum([i+13*2+1 for i in self.data_width])+1
        self.rect = pygame.Rect(0, 0, self.max_width, self.height)
        self.scroll = HScrollBar(self.rect)
        self.scroll.update_content_length(self.width)
        self.back_queue = []
        self.text_queue = []
        self.read_data()
    
    def read_data(self):
        x, y = 0, 0
        for new_y, h in enumerate(self.data_height):
            for new_x, w in enumerate(self.data_width):
                self_data = self.data[new_y][new_x]
                self.back_queue.append(pygame.Rect(x, y, w + 2 + 13 * 2, h + 2 + 6 * 2))
                self_rect = pygame.Rect(x + 1 + 13, y + 1 + 6, w, h)
                if self_data['style'] == 'text-align:left':
                    self_data['rect'].midleft = self_rect.midleft
                if self_data['style'] == 'text-align:center':
                    self_data['rect'].center = self_rect.center
                if self_data['style'] == 'text-align:right':
                    self_data['rect'].midright = self_rect.midright
                self.text_queue.append([self_data['surface'], self_data['rect']])
                x += w + 1 + 13 * 2
            x = 0
            y += h + 1 + 6 * 2

    def render_table(self, pos, mouse_pos, mouse_pressed):
        screen = pygame.Surface((self.max_width, self.height), pygame.SRCALPHA)
        for rect in self.back_queue:
            pygame.draw.rect(screen, (221, 221, 221), rect.move(pos), width=1)
        for text in self.text_queue:
            render_data(screen, *text[1].move(pos).topleft, text[0], mouse_pos, mouse_pressed, self.rect)
        return screen

    def render(self, screen, x, y, pygame_events, mouse_x, mouse_y):
        self.rect.x, self.rect.y = x, y
        self.scroll.update_rect(self.rect)
        mouse_pressed = 0
        for event in pygame_events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pressed = 1
        table_sf = self.render_table((-self.scroll.offset, 0), (mouse_x - x, mouse_y - y), mouse_pressed)
        screen.blit(table_sf, (x, y))
        self.scroll.render(screen)
        self.scroll.handle_event(pygame_events)
