import pygame
import webbrowser as wb


def handle_url(self, mouse_x, mouse_y):
    for i in self.render_queue_text_screen:
        if i[0] != 'pre':
            x, y = i[1][0], i[1][1] - self.contentScrollLength
            if i[2] and pygame.Rect(x, y, i[0].get_width(), i[0].get_height()).collidepoint(
                    (mouse_x, mouse_y)):
                wb.open(i[2])


def handle_mouse_input(self, pygame_events, mouse_x, mouse_y, mouse_pressed):
    for event in pygame_events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 and self.scrollbar is not None:
                self.handle_scroll(50)
            if event.button == 5 and self.scrollbar is not None:
                self.handle_scroll(-50)
            if event.button == 1:
                if self.scrollbar is not None and self.scrollbar.collidepoint(mouse_x, mouse_y):
                    self.scroll_dragging = True
                    self.offest_y = mouse_y - self.scrollbar.y
                self.handle_url(mouse_x, mouse_y)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.scroll_dragging = False
                self.offest_y = 0
    if mouse_pressed and self.scroll_dragging:
        self.handle_mouse_scroll(mouse_y)
