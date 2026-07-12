import pygame,sys

pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("小轩电脑0.01")

try:import ntpath
except:font = pygame.font.SysFont('kaittf', 30)
else:font = pygame.font.SysFont('kaiti', 30);del ntpath

def show_text(text,color=(0,0,0),pos=(0,0)):
    screen.blit(font.render((text),True,color),pos)

abcr = pygame.Rect(0,71,1200,30)
return1 = pygame.Rect(0,71,1200,30)
part = 'main'

while True:
    while part == 'main':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if abcr.collidepoint(event.pos):
                        part = 'abc'
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(150,150,150),abcr,0)
        show_text("小轩电脑0.01",color=(255,255,255),pos=(11,11))
        show_text("="*80,color=(255,255,255),pos=(0,41))
        show_text("abc(abc文档，单击打开).act_text.txt.df",color=(255,255,255),pos=(0,71))
        show_text("None",color=(255,255,255),pos=(0,101))
        show_text("None",color=(255,255,255),pos=(0,131))
        show_text("None",color=(255,255,255),pos=(0,161))
        show_text("None",color=(255,255,255),pos=(0,191))
        pygame.display.update()
    while part == 'abc':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if return1.collidepoint(event.pos):
                        part = 'main'
        screen.fill((255,255,255))
        pygame.draw.rect(screen,(150,150,150),return1,0)
        show_text("0123456789",color=(0,0,0),pos=(11,11))
        show_text("abc Chinese English 666 xiaoxuan-computer-V0",color=(0,0,0),pos=(0,41))
        show_text("←return",color=(0,0,0),pos=(0,71))
        pygame.display.update()