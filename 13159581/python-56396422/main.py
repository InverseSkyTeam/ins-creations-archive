import pygame,sys
pygame.init()

size = width,height = 600,400
bg = (0,0,0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("demo")
event_text = []

font = pygame.font.Font(None,20)
line_height = font.get_linesize()

position = 0
screen.fill(bg)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type != pygame.MOUSEMOTION:
            screen.blit(font.render(str(event),True,(0,255,0)),(0,position))
            position+=line_height
        if position>height:
            position = 0
            screen.fill(bg)
    pygame.display.flip()