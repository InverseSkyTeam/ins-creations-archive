import pygame, sys
import time
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('卡点记录仪')

font = pygame.font.SysFont('kaiti', 60)

start_time = 0
time_list = [0.00]
pygame.mixer.music.load('./bgm.mp3')



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            l = str(time_list)
            with open('record2.txt', 'w', encoding='utf-8') as f:
                f.write(l)
                f.close()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if not start_time:
                start_time = time.time()
                pygame.mixer.music.play(1)
            else:
                time_list.append(time.time() - start_time)
    
    screen.fill((255, 255, 255))
    screen.blit(font.render(f'{time_list[-1]}s', True, (0, 0, 0)), (10, 10))
    pygame.display.update()