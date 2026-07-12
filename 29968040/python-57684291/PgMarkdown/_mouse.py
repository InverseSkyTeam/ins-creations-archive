import pygame
import webbrowser as wb


def handle_url(self, mouse_pos):
    for i in self.render_queue_text_screen_temp:
        if i['name'] == 'pre':
            continue
        pos = (i['pos'][0], i['pos'][1] - self.scroll.offset)
        if i['href'] and i['surface'].get_rect(topleft=pos).collidepoint(mouse_pos):
            i['href'].open()


def handle_mouse_input(self, pygame_events):
    for event in pygame_events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.handle_url(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F12:
                self.debug = 1
