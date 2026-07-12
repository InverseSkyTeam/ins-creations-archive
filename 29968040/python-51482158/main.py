from render import render, Model
import pygame, sys
pygame.init()
screen = pygame.display.set_mode((600, 600))

model = Model("res/african_head.obj", texture_filename="res/african_head_diffuse.tga")
model1 = Model("res/floor.obj", texture_filename="res/floor_diffuse.tga")
clock = pygame.time.Clock()
num = 0
scale = 1
add = 0.05
x, y, z = 1, 1, 3
while 1:
    pygame.display.set_caption('fps:' + str(round(clock.get_fps())))
    pygame_events = pygame.event.get()
    for event in pygame_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                z -= 0.1
            elif event.key == pygame.K_a:
                x -= 0.1
            elif event.key == pygame.K_s:
                z += 0.1
            elif event.key == pygame.K_d:
                x += 0.1
            elif event.key == pygame.K_UP:
                y -= 0.1
            elif event.key == pygame.K_DOWN:
                y += 0.1

    screen.fill((255, 255, 255))
    render(
        model1,
        height=600,
        width=600,
        screen=screen,
        angleX=0,
        angleY=0,
        scale=scale,
        x=x,y=y,z=z
    )
    render(
        model,
        height=600,
        width=600,
        screen=screen,
        angleX=0,
        angleY=0,
        scale=scale,
        x=x,y=y,z=z
    )
    pygame.display.flip()
    clock.tick(114514)
    num += add
