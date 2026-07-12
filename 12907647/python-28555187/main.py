import pygame,sys

pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("小轩电脑0.04")

try:import ntpath
except:font = pygame.font.SysFont('kaittf', 30)
else:font = pygame.font.SysFont('kaiti', 30);del ntpath

def show_text(text,color=(0,0,0),pos=(0,0)):
    screen.blit(font.render((text),True,color),pos)

abcr = pygame.Rect(0,71,1200,30)
return1 = pygame.Rect(0,11,1200,30)
Vr = pygame.Rect(0,101,1200,30)
part = 'main'
str1 = ''

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
                    if Vr.collidepoint(event.pos):
                        part = 'v'
        screen.fill((255,255,255))
        pygame.draw.rect(screen,(128,128,128),abcr,0)
        pygame.draw.rect(screen,(76,76,76),Vr,0)
        show_text('小轩电脑0.04 | '+str(110+len(str1))+'bit/128bit',color=(0,0,0),pos=(11,11))
        show_text('='*80,color=(0,0,0),pos=(0,41))
        show_text('abc.text',color=(0,0,0),pos=(0,71))
        show_text('V0.04 - 64 bit.txtf',color=(0,0,0),pos=(0,101))
        show_text('This is the xiaoxuan computer.',color=(0,0,0),pos=(0,131))
        show_text('None',color=(0,0,0),pos=(0,161))
        show_text('None',color=(0,0,0),pos=(0,191))
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    str1 += '    '
                elif event.key == pygame.K_BACKSPACE:
                    str1 = str1[:-1]
                else:
                    str1 += chr(event.key)
                if len(str1) > 18:
                    part = 'BLUESCREEN'
        screen.fill((255,255,255))
        pygame.draw.rect(screen,(128,128,128),return1,0)
        show_text('←return',color=(0,0,0),pos=(0,11))
        show_text('you can type some letters or numbers here',color=(0,0,0),pos=(0,41))
        show_text(str1,color=(0,0,0),pos=(0,71))
        pygame.display.update()
    while part == 'v':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if return1.collidepoint(event.pos):
                        part = 'main'
        screen.fill((255,255,255))
        pygame.draw.rect(screen,(76,76,76),return1,0)
        show_text('←return',color=(0,0,0),pos=(0,11))
        show_text('my computer -> .128bit .V0.04 .xiaoxuan .text .txtf .str .python .cut_.c_',color=(0,0,0),pos=(0,41))
        show_text(str1,color=(0,0,0),pos=(0,71))
        pygame.display.update()
    while part == 'BLUESCREEN':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,180))
        show_text('Error:内存溢出',color=(255,255,255),pos=(11,11))
        show_text('Except:Error- bit > 128-',color=(255,255,255),pos=(11,41))
        pygame.display.update()