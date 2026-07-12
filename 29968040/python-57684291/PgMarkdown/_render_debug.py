import pygame
from . import _html_label
import numpy as np


def calc_colors(opaque_color, transparent_color):
    opaque_r, opaque_g, opaque_b = opaque_color
    alpha = transparent_color[3] / 255
    result_r = ((1 - alpha) * opaque_r + alpha * transparent_color[0])
    result_g = ((1 - alpha) * opaque_g + alpha * transparent_color[1])
    result_b = ((1 - alpha) * opaque_b + alpha * transparent_color[2])

    return int(result_r), int(result_g), int(result_b)


def draw_dashed_rect(screen, color, rect, width):
    # pygame.draw.rect(screen, color, rect, width)
    screen_np = pygame.surfarray.pixels3d(screen)

    x, y, w, h = rect
    x1 = np.arange(x, x+w-1)
    x2 = np.full(h-1, x+w-1)
    x3 = np.arange(x+w-1, x, -1)
    x4 = np.full(h-1, x)

    y1 = np.full(w-1, y)
    y2 = np.arange(y, y+h-1)
    y3 = np.full(w-1, y+h-1)
    y4 = np.arange(y+h-1, y, -1)

    xs = np.concatenate((x1, x2, x3, x4))
    ys = np.concatenate((y1, y2, y3, y4))

    arr = np.full(len(xs), True)
    arr[3::4] = False
    arr[2::4] = False

    screen_np[xs[arr], ys[arr]] = np.array(color)


def convert(num):
    if num == 0:
        return '-'
    return str(num)


def render_debug_sf(data: _html_label.Label, content_size, font, font_size, font_color):
    attrs = ['margin_top', 'margin_right', 'margin_bottom', 'margin_left',
             'border_top_width', 'border_right_width', 'border_bottom_width', 'border_left_width',
             'padding_top', 'padding_right', 'padding_bottom', 'padding_left']
    attrs_sf = {}
    attrs_name = ['margin', 'border', 'padding', 'content']
    colors = [(246, 178, 107, int(0.66 * 255)),
              (255, 229, 153, int(0.66 * 255)),
              (147, 196, 125, int(0.55 * 255)),
              (111, 168, 220, int(0.66 * 255))]
    content_width, content_height = content_size

    sum_width = 0
    for i, name in enumerate(attrs):
        attr_sf = font.render(convert(eval(f'data.{name}')), True, font_color)
        attrs_sf[name.replace('_width', '')] = attr_sf
        if '_left' in name or '_right' in name:
            sum_width += attr_sf.get_width()

    content_sf = font.render(str(f'{content_width} x {content_height}'), True, font_color)

    sf_width = max(content_sf.get_width() + 3 * 4 + 1 * 2, 100) + 3 * 12 + 1 * 6 + sum_width
    sf_height = font_size * 7 + 3 * 16 + 1 * 8
    sf = pygame.Surface((sf_width, sf_height), pygame.SRCALPHA)
    pygame.draw.rect(sf, (0, 0, 0, int(255 * 0.3)), (0, 0, sf_width, sf_height), border_radius=3)

    x, y, end_x, end_y = 3, 3, sf_width - 3, sf_height - 3
    for i in range(3):
        pygame.draw.rect(sf, calc_colors((255,) * 3, colors[i]), (x, y, end_x - x, end_y - y))
        if i != 1:
            draw_dashed_rect(sf, (0, ) * 3, (x, y, end_x - x, end_y - y), width=1)
        else:
            pygame.draw.rect(sf, (0, ) * 3, (x, y, end_x - x, end_y - y), width=1)
        left = attrs_sf[attrs_name[i] + '_left']
        right = attrs_sf[attrs_name[i] + '_right']
        top = attrs_sf[attrs_name[i] + '_top']
        bottom = attrs_sf[attrs_name[i] + '_bottom']
        sf.blit(left, (x + 4, (sf_height - font_size) // 2))
        sf.blit(right, (end_x - 4 - right.get_width(), (sf_height - font_size) // 2))
        sf.blit(top, ((sf_width - top.get_width()) // 2, y + 4))
        sf.blit(bottom, ((sf_width - bottom.get_width()) // 2, end_y - 4 - font_size))
        sf.blit(font.render(attrs_name[i], True, font_color), (x + 4 + 5, y + 4))

        x += 1 + 3 + attrs_sf[attrs_name[i] + '_left'].get_width() + 3
        y += 1 + 3 + font_size + 3
        end_x -= 1 + 3 + attrs_sf[attrs_name[i] + '_right'].get_width() + 3
        end_y -= 1 + 3 + font_size + 3

    pygame.draw.rect(sf, calc_colors((255,) * 3, colors[-1]), (x, y, end_x - x, end_y - y))
    pygame.draw.rect(sf, (0,) * 3, (x, y, end_x - x, end_y - y), width=1)
    sf.blit(content_sf, ((sf_width - content_sf.get_width()) // 2, (sf_height - font_size) // 2))

    return sf
