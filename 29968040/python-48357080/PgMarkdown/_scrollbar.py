import pygame


def render_scroll(self):
    if self.scrollbar is not None:
        pygame.draw.rect(self.screen, self.scroll_color, self.scrollbar, border_radius=2)


def contentScrollLength_scrollbarLength(self, contentScrollLength):
    return contentScrollLength * (self.h - self.scrollbar.height) / (self.render_height - self.h)


def scrollbarLength_contentScrollLength(self, scrollbarLength):
    return (self.render_height - self.h) / (self.h - self.scrollbar.height) * scrollbarLength


def handle_mouse_scroll(self, mouse_y):
    new_y = mouse_y - self.offest_y
    self.scrollbar.y = max(self.y, min(self.y + self.h - self.scrollbar.height, new_y))
    self.contentScrollLength = self.scrollbarLength_contentScrollLength(self.scrollbar.y - self.y)


def handle_scroll(self, height):
    self.contentScrollLength -= height
    self.contentScrollLength = max(0, min(self.contentScrollLength, self.render_height - self.h))
    self.scrollbar.y = self.contentScrollLength_scrollbarLength(self.contentScrollLength) + self.y
