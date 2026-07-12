import pygame


def render_data(screen, x, y, data):
    for i in data:
        screen.blit(i['surface'], (x+i['pos'][0], y+i['pos'][1]))


def render_table(self, screen, data, pos):
    width = [max([data[line][lie][0] for line in range(len(data))]) for lie in range(len(data[0]))]
    height = [max([dd[1] for dd in line]) for line in data]
    x, y = pos
    for new_y, h in enumerate(height):
        for new_x, w in enumerate(width):
            self_data = data[new_y][new_x]
            pygame.draw.rect(screen, (221, 221, 221), pygame.Rect(x, y, w+2+13*2, h+2+6*2), width=1)
            offset_x = 0
            if self_data[3] == 'text-align: center;':
                offset_x = (w-self_data[0])//2
            if self_data[3] == 'text-align: right;':
                offset_x = w-self_data[0]
            render_data(screen, x+1+13+offset_x, y+1+6+(h-self_data[1])//2, self_data[2])
            x += w+1+13*2
        x = pos[0]
        y += h+1+6*2
