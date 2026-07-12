import pygame,sys
pygame.init()
input('回车开始，留意窗口，按任意键退出')
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
print('啦啦啦啦啦！')
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print('\n\n\033[38;2;230;230;0m小轩的程序运行完毕\033[8m\033[?25l')
            pygame.quit()
            sys.exit()
    screen.fill((0,0,255))
    pygame.display.update()