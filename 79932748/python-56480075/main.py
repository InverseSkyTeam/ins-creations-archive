import numpy as np
import pygame, sys, math
import random

def draw_math_function(screen, expr, rect, steps = 10, color = (0, 0, 0), width = 3, limited = True, args={}):
    p = []
    for x in np.arange(-rect.width / 2, rect.width / 2, steps):
        real_x = rect.centerx + x
        real_y = rect.centery - eval(expr, globals(), {**locals(), **args})
        if rect.top <= real_y < rect.bottom or (not limited):
            p.append((real_x, real_y))
    pygame.draw.lines(screen, color, False, p, width)

class Function_awa:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 500, 500)
        self.tl = 0
        self.a = 1
        self.c = 0
    def follow(self, pos):
        self.rect.center = pos
    def draw(self):
        self.tl += 0.005
        self.a += 0.01
        self.c += random.randint(-1, 1)
        draw_math_function(screen, '30*math.sin(x/30+tl)', self.rect, color = (0, 0, 255), args = {'tl': self.tl})
        draw_math_function(screen, '30*math.cos(x/30+tl)', self.rect, color = (0, 255, 0), args = {'tl': self.tl})
        draw_math_function(screen, '((abs(12-a%24)-6)*x**2+x*(abs(12-tl%24)-6)*10)//10+c', self.rect, 5, (255, 0, 0), 5, args={'a': self.a, 'tl': self.tl, 'c': self.c})
        pygame.draw.circle(screen, (255, 255, 0), self.rect.center, self.tl/3%0.5*300, 6)

pygame.init()
screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
fa = Function_awa()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    fa.follow(pygame.mouse.get_pos())
    fa.draw()
    pygame.display.update()
    clock.tick()
    pygame.display.set_caption('fps:' + str(round(clock.get_fps())))