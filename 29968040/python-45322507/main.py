import pygame,sys,text_input_box as txt
import time
txt.laoliu()
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("pygame多行文本输入（支持中文）")
txt1=txt.TextInput((20,20),'ttf.ttf',24)
import os
pygame.key.start_text_input()
input_rect = pygame.Rect(80, 80, 320, 40)
pygame.key.set_text_input_rect(input_rect)#这个好像没用？

while True:
    events=pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    txt1.update(events)
    screen.fill((255,255,255))
    if txt1.get_txt(0)==[''] and txt1.get_txt(1)=='':
        screen.blit(txt1.draw_one('在这里输入',(255//2,255//2,255//2),False),(20,20))
    txt1.render_txt(screen,int(time.time()*2)%2)
    pygame.display.update()