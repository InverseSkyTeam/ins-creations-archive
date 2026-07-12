import pygame,sys
pygame.init()
FONTNAME = "kaiti"
screen = pygame.display.set_mode((511,720))
pygame.display.set_caption("圣诞快乐")
img = pygame.image.load("bgp.jpg")
pygame.mixer.music.load("bgm.mp3")
pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    screen.blit(img,(0,0))
    pygame.display.update()