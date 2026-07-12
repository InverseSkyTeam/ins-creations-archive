import pygame
import math
import numpy as np
import time
import sys

value = 0
use_np = True  # 是否启用加速模式（numpy）

class Effect:
    @staticmethod
    def fisheye_processor(image: pygame.Surface, value):
        if value == 0:
            return image
        value = max(0, 1 + value / 100)
        width, height = image.get_size()
        center = 0.5

        distorted_image = image.copy()
        
        for x in range(width):
            dx = x / (width - 1) - center
            dx2 = dx ** 2
            for y in range(height):
                dy = y / (height - 1) - center
                distance = math.sqrt(dx2 + dy**2)
                if distance < center:
                    r = distance / center
                    theta = math.atan2(dy, dx)
                    distortion_radius = r ** value * center
                    distorted_x = int(
                        (center + distortion_radius * math.cos(theta)) * (width - 1)
                    )
                    distorted_y = int(
                        (center + distortion_radius * math.sin(theta)) * (height - 1)
                    )
                    if 0 <= distorted_x < width and 0 <= distorted_y < height:
                        distorted_image.set_at((x, y), image.get_at((distorted_x, distorted_y)))

        return distorted_image
        
    @staticmethod
    def fisheye_processor_np(image: pygame.Surface, value):
        if value == 0:
            return image
        value = max(0, 1 + value / 100)
        width, height = image.get_size()
        center = 0.5

        distorted_image = image.copy()
        src = np.array(image.get_view("1"), copy=False)
        dst = np.array(distorted_image.get_view("1"), copy=False)
        
        pos_x, pos_y = np.mgrid[:width, :height]
        np_dx = pos_x / (width - 1) - center
        np_dy = pos_y / (height - 1) - center
        np_distance = np.sqrt(np_dx ** 2 + np_dy ** 2)
        np_distortion_radius = (np_distance / center) ** value * center
        np_theta = np.arctan2(np_dy, np_dx)
        np_distorted_x = ((center + np_distortion_radius * np.cos(np_theta)) * (width - 1)).astype(np.int32)
        np_distorted_y = ((center + np_distortion_radius * np.sin(np_theta)) * (height - 1)).astype(np.int32)

        mask = (np_distance < center) & (0 <= np_distorted_x) & (np_distorted_x < width) & (0 <= np_distorted_y) & (np_distorted_y < height)
        dst[(pos_y * width + pos_x)[mask]] = src[(np_distorted_y * width + np_distorted_x)[mask]]

        return distorted_image


pygame.init()


w, h = 298, 398
screen = pygame.display.set_mode((w, h))

clock = pygame.time.Clock()

img = pygame.image.load('可多1.png').convert_alpha()

while True:
    FPS = str(round(clock.get_fps()))
    pygame.display.set_caption('fps:' + FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    if use_np:
        screen.blit(Effect.fisheye_processor_np(img, value), (50, 50))
    else:
        screen.blit(Effect.fisheye_processor(img, value), (50, 50))
    value += 1
    pygame.display.update()
    clock.tick(114514)
