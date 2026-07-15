import pygame
import sys

print(f"Python {sys.version}")

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    screen.blit(font.render("Hello Pygame-CE!", True, (255, 0, 0)), (20, 20))
    screen.blit(font.render(f"We're using Python {sys.version}！", True, (255, 0, 0)), (20, 60))
    screen.blit(font.render(f"We're using Pygame-CE {pygame.version.ver}", True, (255, 0, 0)), (20, 100))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
