import pygame
from math import cos, sin, radians
import sys
from pygame.locals import *
import datetime
pygame.init()
screen_size = width, height = 520, 520
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('时间表盘')
bg = pygame.image.load('time.png').convert_alpha()
clock = pygame.time.Clock()
font = pygame.font.SysFont('kaiti', 14, bold=False)
lst_week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
normal_color = (239, 0, 0)
current_color = (0, 0, 255)


def draw_year(year):
    text = str(year) + '年'
    image = font.render(text, True, current_color)
    posX = width // 2 - 15
    posY = height // 2 - 12
    screen.blit(image, (posX, posY))


def draw_others(item, n, char, r):
    average_angle = 360 / n
    angle_offset = (item - 1) * average_angle
    for i in range(n):
        angle = average_angle * (i - 1) - angle_offset
        text = str(i) + char
        image = font.render(text, True, normal_color)
        if i == item:
            image = font.render(text, True, current_color)
        posX = int(cos(radians(-angle)) * r)
        posY = int(sin(radians(-angle)) * r)
        rotated_image = pygame.transform.rotate(image, angle)
        screen.blit(rotated_image, (posX + width //
                                    2 - 18, posY + height // 2 - 12))

def draw_others1(item, n, char, r):
    average_angle = 360 / n
    angle_offset = (item - 1) * average_angle
    for i in range(1,n+1):
        angle = average_angle * (i - 1) - angle_offset
        text = str(i) + char
        image = font.render(text, True, normal_color)
        if i == item:
            image = font.render(text, True, current_color)
        posX = int(cos(radians(-angle)) * r)
        posY = int(sin(radians(-angle)) * r)
        rotated_image = pygame.transform.rotate(image, angle)
        screen.blit(rotated_image, (posX + width //
                                    2 - 18, posY + height // 2 - 12))

def draw_week(weekday, lst_week):
    average_angle = 360 / 7
    angle_offset = (weekday - 3) * average_angle
    for i, c in enumerate(lst_week):
        angle = average_angle * i + angle_offset
        image = font.render(c, True, normal_color)
        if i == weekday:
            image = font.render(c, True, current_color)
        posX = int(cos(radians(-angle)) * 120)
        posY = int(sin(radians(-angle)) * 120)
        rotated_image = pygame.transform.rotate(image, angle)
        screen.blit(rotated_image, (posX + width //
                                    2 - 25, posY + height // 2 - 12))


def main():
    while True:
        day = datetime.datetime.today()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        screen.blit(bg, (0, 0))
        draw_year(day.year)
        draw_others1(day.month, 12, '月', 50)
        draw_others1(day.day, 31, '日', 80)
        draw_week(day.weekday(), lst_week)
        draw_others(day.hour, 24, '时', 165)
        draw_others(day.minute, 60, '分', 200)
        draw_others(day.second, 60, '秒', 230)
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
