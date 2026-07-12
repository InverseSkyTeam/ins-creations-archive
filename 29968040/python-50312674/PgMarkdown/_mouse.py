import pygame
import webbrowser as wb


def handle_url(self, mouse_x, mouse_y):
    for i in self.render_queue_text_screen_temp:
        if i['name'] != 'pre':
            x, y = i['pos'][0], i['pos'][1] - self.contentScrollLength
            if i['href'] and pygame.Rect(x, y, i['surface'].get_width(), i['surface'].get_height()).collidepoint(
                    (mouse_x, mouse_y)):
                i['href'].open()


def handle_mouse_input(self, pygame_events, mouse_x, mouse_y, mouse_pressed):
    if self.scrollbar is not None and self.scrollbar.collidepoint(mouse_x, mouse_y) or self.scroll_dragging:
        self.scroll_color = self.scroll_color_hover
    else:
        self.scroll_color = self.scroll_color_normal
    for event in pygame_events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 and self.scrollbar is not None:
                self.handle_scroll(50)
            if event.button == 5 and self.scrollbar is not None:
                self.handle_scroll(-50)
            if event.button == 1:
                if self.scrollbar is not None and self.scrollbar.collidepoint(mouse_x, mouse_y):
                    self.scroll_dragging = True
                self.handle_url(mouse_x, mouse_y)
        if event.type == pygame.MOUSEMOTION:
            if self.scroll_dragging:
                self.scrollbar.move_ip(0, event.rel[1])
                self.scrollbar.y = max(self.y, min(self.y + self.h - self.scrollbar.height, self.scrollbar.y))
                self.contentScrollLength = self.scrollbarLength_contentScrollLength(self.scrollbar.y - self.y)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.scroll_dragging = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F12:
                self.debug = 1
