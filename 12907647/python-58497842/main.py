import pygame
import random
import time
import sys

pygame.init()
font = {
    30: pygame.font.SysFont('kaiti', 30),
    40: pygame.font.SysFont('kaiti', 40),
}
def show_text(text, color=(0, 0, 0), pos=(0, 0), size=40, center=1):
    s = font[size].render((text), True, color)
    screen.blit(s, (int(pos[0] - s.get_width() * center / 2), int(pos[1] - s.get_height() * center / 2)))

pygame.display.set_caption('INS逆天团队 舒尔特方格')
screen = pygame.display.set_mode((615, 630))



table_size = 5

def generate_table(size):
    standard_list = list(range(1, size * size + 1))
    game_list = []
    while standard_list:
        element = random.choice(standard_list)
        game_list.append(element)
        standard_list.remove(element)
    return game_list

table = generate_table(table_size)
block_size = 600 // table_size
progress = 0
total_progress = table_size * table_size
started = 0
record = 0



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                col = int(event.pos[0] / block_size)
                row = int(event.pos[1] / block_size)
                num = table[row * table_size + col]
                if num == progress + 1:
                    progress = num
                    if progress == total_progress:
                        started = 0
                        record = time.time() - t1
        if event.type == pygame.KEYDOWN:
            if event.key == ord('r') and not record:
                started = 1
                t1 = time.time()
    
    screen.fill((111, 255, 255))
    if started or record:
        for each in range(len(table)):
            num = table[each]
            block = pygame.Rect(each % table_size * block_size, each // table_size * block_size, block_size, block_size)
            pygame.draw.rect(screen, (0, 0, 0), block, 3)
            show_text(str(num), pos=block.center)
    
    pygame.draw.line(screen, (128, 128, 128), (0, 615), (500, 615), 30)
    pygame.draw.line(screen, (0, 233, 111), (0, 615), (int(500 * progress / total_progress), 615), 30)
    show_text(f'进度 {progress}/{total_progress} ({progress * 100 / total_progress:.2f}%)', pos=(0, 600), size=30, center=0)
    show_text(f'{time.time()-t1:.2f}s' if started else f'{record:.2f}s', (255, 0, 0), (500, 600), 30, 0)
    
    pygame.display.update()