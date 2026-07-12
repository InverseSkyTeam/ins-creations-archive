import pygame
import copy


def calc_colors(opaque_color, transparent_color):
    opaque_r, opaque_g, opaque_b = opaque_color
    alpha = transparent_color[3]
    result_r = ((1 - alpha) * opaque_r + alpha * transparent_color[0])
    result_g = ((1 - alpha) * opaque_g + alpha * transparent_color[1])
    result_b = ((1 - alpha) * opaque_b + alpha * transparent_color[2])

    return int(result_r), int(result_g), int(result_b)


def render_linear_gradient_rect(screen, color_a, color_b, rect):
    precision = 25
    color_temp = copy.deepcopy(list(color_a))
    num = rect.w // precision
    r_c, g_c, b_c = (color_b[0] - color_a[0])//num, (color_b[1] - color_a[1])//num, (color_b[2] - color_a[2])//num
    for i in range(num):
        temp_rect = pygame.Rect(rect.x + precision * i, rect.y, precision, rect.h)
        pygame.draw.rect(screen, color_temp, temp_rect)
        color_temp[0] += r_c
        color_temp[1] += g_c
        color_temp[2] += b_c

def draw_alpha_rect(screen, color, rect):
    sf = pygame.Surface((rect[-2], rect[-1]), pygame.SRCALPHA)
    pygame.draw.rect(sf, color, (0, 0, rect[-2], rect[-1]), border_radius=3)
    screen.blit(sf, (rect[0], rect[1]))
