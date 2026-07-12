import pygame,sys
pygame.init()
screen = pygame.display.set_mode((480,700))
pygame.display.set_caption("飞机大战")
bgImg = pygame.image.load('bg_1.jpg')
bgImg2 = pygame.image.load('bg_2.jpg')
heroImg = pygame.image.load('fly7.png')
hero_rect = pygame.Rect(210,600,66,80)
pygame.mixer.music.load('flysound.wav')
pygame.mixer.music.play(-1,0.0)
bg_y1 = 0
bg_y2 = -700
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero_rect.x = hero_rect.x-40
            elif event.key == pygame.K_RIGHT:
                hero_rect.x = hero_rect.x+40
            elif event.key == pygame.K_UP:
                hero_rect.y = hero_rect.y-40
            elif event.key == pygame.K_DOWN:
                hero_rect.y = hero_rect.y+40
while True:
    bg_y1 = bg_y1 + 30
    bg_y1 = bg_y1 + 30
    if bg_y1 >= 700:
        bg_y1 = -700
    if bg_y2 >= 700:
        bg_y2 = -700
    screen.blit(bgImg,(0,bg_y1))
    screen.blit(bgImg2,(0,bg_y2))
    #  #  #  #  #  #  #  #  #  #
    xes_20.Enemy(1,5)
    xes_20.Bullet(hero_rect ,3)
    xes_20.fight(screen,hero_rect)
    for enemy in xes_20.enemyList:
        enemy_rect = eneny['rect']
        if hero_rect.colliderect(enemy_rect):
            print('YOU DIED!')
            print('GAME OVER!')
    screen.blit(heroImg,hero_rect)
    pygame.display.update