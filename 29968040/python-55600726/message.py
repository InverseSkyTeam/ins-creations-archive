import pygame
import math
import time


class Message:
    def __init__(self):
        self.online_players = 0  # 在线人数
        self.messages = []
        self.rect = pygame.Rect((10, 70, 153, 174))
        self.font_size = 16
        self.line_height = 20
        self.font = pygame.font.SysFont('SimHei', self.font_size)
        self.last_time = time.time()

    def add_message(self, text):
        self.messages.append(text)
        self.last_time = time.time()

    def render(self, screen):
        if (time.time() - self.last_time) > 3:
            return
        bg_surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        # bg_surface.fill((255,) * 3)
        if len(self.messages) * self.line_height > self.rect.h:
            length = math.ceil(self.rect.h / self.line_height)
            y = self.rect.h - length * self.line_height
            for i in range(len(self.messages) - length, len(self.messages)):
                txt = self.font.render(self.messages[i], True, (255,) * 3)
                bg_surface.blit(txt, txt.get_rect(left=5, centery=y + self.line_height // 2))
                y += self.line_height
        else:
            y = 0
            for message in self.messages:
                txt = self.font.render(message, True, (255,) * 3)
                bg_surface.blit(txt, txt.get_rect(left=5, centery=y + self.line_height // 2))
                y += self.line_height

        screen.blit(bg_surface, self.rect)
