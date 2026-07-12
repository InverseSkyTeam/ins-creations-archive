import pygame
import sys
import time

size = [(350, 550), (600, 800), (1200, 1200)]
print('请选择模式：')
print('1：低性能模式（适合手机和学习机）')
print('2：中性能模式（适合配置一般的机器）')
print('3：高性能模式（如果你是电脑，放心大胆用）')
mode = input('请输入（输入数字序号）：')
try:
    width, height = size[int(mode) - 1]
except:
    width, height = size[0]

import draw_lib

import ball_run
import image_manager
import anim_manager
from score_number import ScoreNumber
from finish_window import FinishWindow

pygame.init()
print_fps = False

# width, height = 600, 800
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


# ball_run.load_sound()
ball_run.newBall(0)
ball_run.width, ball_run.height = width, height - 80

background = pygame.image.load('icon/bottomBack.png')
score_number = ScoreNumber(10, 20, 40)
finish_window = FinishWindow(width, height)
bottom_bg = draw_lib.scale_img(background, width, 80)
dash_line = pygame.image.load('icon/dash_line.png')


def draw():
    screen.blit(bottom_bg, (0, height - 80))
    screen.blit(dash_line, (0, ball_run.lineDashY - 2))
    image_manager.draw(screen)
    score_number.draw(screen)
    if ball_run.finish == 2:
        finish_window.draw(screen)

while True:
    # pygame.display.set_caption('fps:' + str(round(clock.get_fps())))
    screen.fill((0xFF, 0xE8, 0x9D))
    ball_run.currentBallMove1(pygame.mouse.get_pos()[0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not ball_run.finish and ball_run.currentBallStartDown():
                ball_run.newBall(event.pos[0])
            elif ball_run.finish == 2:
                ball_run.finish = 0
                ball_run.score = 0
                ball_run.newBall(event.pos[0])
    a = time.time()
    ball_run.process()
    # b = time.time()
    anim_manager.update_all()
    # c = time.time()
    draw()
    d = time.time()
    if print_fps:
        print(1 / max((d - a), 1 / 114514))
    # print(b-a, c-b, d-c)
    
    pygame.display.update()
    clock.tick(60)
