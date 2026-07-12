import pygame,sys,os,secret
pygame.init()
r = int(input("\033[1;31m请输入字幕雨颜色的red（r）值："))
g = int(input("\033[1;32m请输入字幕雨颜色的green（g）值："))
b = int(input("\033[1;34m请输入字幕雨颜色的blue（b）值："))
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("字幕雨")
secret.rain(screen,r,g,b)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()