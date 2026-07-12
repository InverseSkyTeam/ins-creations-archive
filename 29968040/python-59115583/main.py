import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((200, 200))

mask = pygame.Surface((200, 200), pygame.SRCALPHA)
pygame.draw.circle(mask, (255, 255, 255, 255), (100, 100), 100)

# 这是重点
img = pygame.image.load('草坪.jpg').convert_alpha()
img.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(img, (0, 0))
    pygame.display.flip()