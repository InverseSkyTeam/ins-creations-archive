from typing import Callable
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
free_datas = [[]]
lines = []
mouse_down = False
width = 2


class Button:
    def __init__(self, screen: pygame.Surface, obj: pygame.Surface, left: int, top: int, func, args=()):
        self.screen, self.obj, self.func, self.args = screen, obj, func, args
        self.left, self.top = left, top
        self.rect = self.obj.get_rect()

        self.rect.left = self.left
        self.rect.top = self.top

    def check(self, pos: tuple):
        if self.rect.collidepoint(pos):
            self.func(*self.args)
            return True
        return False

    def draw(self):
        self.screen.blit(self.obj, self.rect)


pygame.font.init()
font = pygame.font.SysFont("Consola", 30)

FREE, DRAWLINE = "FREE", "DRAWLINE"
mode = FREE


def set_mode_free():
    global mode
    mode = FREE


def set_mode_drawline():
    global mode
    mode = DRAWLINE
    lines.append([])


button_1 = Button(screen, font.render("Set mode: FREE", True, (0, 0, 0)), 200, 400, set_mode_free)
button_2 = Button(screen, font.render("Set mode: DRAWLINE", True, (0, 0, 0)), 400, 400, set_mode_drawline)

while True:
    for event in pygame.event.get():
        if mode == FREE:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not button_1.check(pygame.mouse.get_pos()) and not button_2.check(pygame.mouse.get_pos()):
                    free_datas[-1].append(pygame.mouse.get_pos())
                    mouse_down = True
            elif event.type == pygame.MOUSEMOTION:
                if mouse_down:
                    free_datas[-1].append(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                free_datas.append([])
                mouse_down = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if free_datas:
                        free_datas.pop(len(free_datas) - 2)
                    if not free_datas:
                        free_datas = [[]]
        if mode == DRAWLINE:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not button_1.check(pygame.mouse.get_pos()) and not button_2.check(pygame.mouse.get_pos()):
                    lines[-1].append(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if lines and lines[-1]:
                        lines[-1].pop()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    for i in free_datas:
        if i == []:
            pass
        elif len(i) == 1:
            pygame.draw.circle(screen, (0, 0, 0), i[0], width)
        else:
            for j in range(len(i) - 1):
                pygame.draw.line(screen, (0, 0, 0), i[j], i[j+1], width)

    for i in lines:
        if i == []:
            pass
        elif len(i) == 1:
            pygame.draw.circle(screen, (0, 0, 0), i[0], width)
        else:
            for j in range(len(i) - 1):
                pygame.draw.line(screen, (0, 0, 0), i[j], i[j+1], width)

    button_1.draw()
    button_2.draw()

    screen.blit(font.render("Mode: " + mode, True, (0, 0, 0)), (300, 500))

    pygame.display.flip()
