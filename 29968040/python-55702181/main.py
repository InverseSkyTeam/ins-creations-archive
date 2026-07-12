import pygame
import sys
from cubic_bezier import CubicBezier
from keyframes import KeyFrames
import time

pygame.init()
w, h = 800, 600
screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)

clock = pygame.time.Clock()
ease = CubicBezier(0.25, 0.1, 0.25, 1)
key_frames = KeyFrames(ease).add_frames(0.0, 0.7).add_frames(0.45, 1.05).add_frames(0.8, 0.95).add_frames(1.0, 1.0)

img = pygame.image.load('ac-congrats.png').convert_alpha()
img = pygame.transform.smoothscale(img, (472, 439))
img_w, img_h = img.get_size()

start_time = time.time()

while 1:
    FPS = str(round(clock.get_fps()))
    pygame.display.set_caption('fps:' + FPS)
    pygame_events = pygame.event.get()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            w, h = screen.get_size()
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_time = time.time()

    screen.fill((255,)*3)
    t = time.time() - start_time
    if t <= 0.3:  # 动画第一阶段
        data = key_frames.solve(t / 0.3)
        new_img = pygame.transform.smoothscale(img, (img_w * data, img_h * data))
        screen.blit(new_img, new_img.get_rect(center=(w // 2, h // 2)))
    elif 0.3 < t <= 0.3 + 3:  # 第二阶段，停留 3s
        screen.blit(img, img.get_rect(center=(w // 2, h // 2)))
    elif 0.3 + 3 < t <= 0.3 + 3 + 0.15:  # 第三阶段，缓慢消失
        t1 = ease.Solve((t - 0.3 - 3) / 0.15)
        data = 1 + (0.5 - 1) * t1
        data1 = 255 + (0 - 255) * t1
        new_img = pygame.transform.smoothscale(img, (img_w * data, img_h * data))
        new_img.set_alpha(data1)
        screen.blit(new_img, new_img.get_rect(center=(w // 2, h // 2)))

    pygame.display.flip()
    clock.tick(114514)
