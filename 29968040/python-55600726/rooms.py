from window import Window
import pygame
from scroll_bar import VScrollBar
from util import scale_img


CARD_SIZE = int(224 * 0.875), int(256 * 0.875)
COVER_SIZE = CARD_SIZE[0], int(CARD_SIZE[1] * (168 / 256))
TEXT_SIZE = int(CARD_SIZE[0] * (192 / 224)), int(CARD_SIZE[1] * (22 + 8 + 16) / 256)
CARD_MARGIN = 20, 14


all_rooms = [
    {'title': '默认房间', 'name': '黄羿杰', 'project': '25311041'}
]


class Rooms:
    def __init__(self, w, h):
        self.state = '大厅'
        self.room: Window = None
        self.content_rect = pygame.Rect(int(w * 0.05), int(h * 0.1), int(w * 0.9), int(h * 0.87))
        self.scroll = VScrollBar(self.content_rect)

        self.cover = scale_img(pygame.image.load('data/cover/default-cover.png'), *COVER_SIZE)
        self.card_title_font = pygame.font.SysFont('SimHei', int(TEXT_SIZE[1] * 16/(22 + 8 + 16)) + 2)
        self.card_name_font = pygame.font.SysFont('SimHei', int(TEXT_SIZE[1] * 12/(22 + 8 + 16)) + 2)

    @staticmethod
    def draw_header(screen, w, h):
        rect = pygame.Rect(0, 0, w, h * 0.07)
        font = pygame.font.SysFont('SimHei', int(rect.h * 0.7))

        screen.fill((255,) * 3, rect)
        txt = font.render('联机大厅', True, (53,) * 3)
        screen.blit(txt, txt.get_rect(center=rect.center))

    def draw_card(self, sf, x, y, title, name):
        sf.blit(self.cover, (x, y))
        text_rect = pygame.Rect((x, y + COVER_SIZE[1], CARD_SIZE[0], CARD_SIZE[1] - COVER_SIZE[1]))
        pygame.draw.rect(sf, (255,) * 3, text_rect, border_bottom_right_radius=8, border_bottom_left_radius=8)
        text_sf = pygame.Surface(TEXT_SIZE, pygame.SRCALPHA)
        card_title = self.card_title_font.render(title, True, (33, 40, 49))
        text_sf.blit(card_title, (0, int(TEXT_SIZE[1] * 3 / (22 + 8 + 16))))
        card_name = self.card_name_font.render(name, True, (133, 140, 150))
        text_sf.blit(card_name, (0, int(TEXT_SIZE[1] * 32 / (22 + 8 + 16))))
        sf.blit(text_sf, text_sf.get_rect(center=text_rect.center))

    def draw_content(self, screen):
        sf = pygame.Surface(self.content_rect.size, pygame.SRCALPHA)
        # sf.fill((255, 255, 255))

        x, y = 0, -self.scroll.offset
        for i in range(len(all_rooms)):
            if x + CARD_SIZE[0] > sf.get_width():
                x, y = 0, y + CARD_SIZE[1] + CARD_MARGIN[1]
            self.draw_card(sf, x, y, all_rooms[i]['title'], all_rooms[i]['name'])
            x += CARD_SIZE[0] + CARD_MARGIN[0]

        self.scroll.update_content_length(y + self.scroll.offset + CARD_SIZE[1] + CARD_MARGIN[1])

        self.scroll.render(sf)
        screen.blit(sf, self.content_rect)

    def draw(self, screen, w, h):
        if self.state == '房间':
            self.room.draw(screen, w, h)
            return
        screen.fill((245, 247, 250))
        self.draw_header(screen, w, h)
        self.draw_content(screen)

    def collide(self, pos):
        x, y = 0, -self.scroll.offset
        for i in range(len(all_rooms)):
            if x + CARD_SIZE[0] > self.content_rect.w:
                x, y = 0, y + CARD_SIZE[1] + CARD_MARGIN[1]
            if pygame.Rect(x, y, *CARD_SIZE).collidepoint(pos):
                return i
            x += CARD_SIZE[0] + CARD_MARGIN[0]

    def update_self(self, pygame_events, w, h):
        for event in pygame_events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                new_pos = event.pos[0] - self.content_rect.x, event.pos[1] - self.content_rect.y
                if self.scroll.scroll_rect.collidepoint(new_pos):
                    continue
                res = self.collide(new_pos)
                if res is None:
                    continue
                self.get_into_room(all_rooms[res]['project'], w, h)
            if event.type == pygame.VIDEORESIZE:
                w, h = event.w, event.h
                self.content_rect = pygame.Rect(int(w * 0.05), int(h * 0.1), int(w * 0.9), int(h * 0.87))
                self.scroll.update_rect(self.content_rect)
        self.scroll.handle_event(pygame_events)

    def update(self, pygame_events, w, h):
        if self.state == '房间':
            self.room.update(pygame_events)
            for event in pygame_events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    self.exit_room()
            return
        self.update_self(pygame_events, w, h)

    def get_into_room(self, project, w, h):
        if self.state != '大厅':
            return
        self.room = Window(w, h, project=project)
        self.state = '房间'

    def exit_room(self):
        if self.state != '房间':
            return
        self.room.exit()
        self.state = '大厅'

    def exit(self):
        if self.state == '房间':
            self.room.exit()
