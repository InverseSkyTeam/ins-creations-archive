import numpy as np
import pygame, sys, math

def draw_math_function(screen, expr, rect, steps = 10, color = (0, 0, 0), width = 3, limited = True):
    p = []
    for x in np.arange(-rect.width / 2, rect.width / 2, steps):
        real_x = rect.centerx + x
        real_y = rect.centery - eval(expr, globals(), locals())
        if rect.top <= real_y < rect.bottom or (not limited):
            p.append((real_x, real_y))
    pygame.draw.lines(screen, color, False, p, width)

pygame.init()
screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
l = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    
    l += 0.005
    draw_math_function(screen, '30*math.sin(x/30+l)', pygame.Rect(100, 200, 500, 100), color = (0, 0, 255))
    draw_math_function(screen, '30*math.cos(x/30+l*2)', pygame.Rect(100, 200, 500, 100), color = (0, 255, 0))
    draw_math_function(screen, '(x**2+x*(abs(12-l%24)-6)*10)//10', pygame.Rect(250, 0, 200, 500), 5, (255, 0, 0), 5)
    draw_math_function(screen, '1/(abs(x)+1)*1000', pygame.Rect(0, 0, 700, 500))
    pygame.draw.circle(screen, (255, 255, 0), (350, 250), l/3%0.5*300, 6)
    pygame.display.update()

    clock.tick()
    pygame.display.set_caption('fps:' + str(round(clock.get_fps())))