from multiprocessing import Process
import pygame
pygame.init()

def open_window(title,size,color):
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    print(f'{title}开启')
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill(color)
        pygame.display.flip()

if __name__ == '__main__':
    print('开进程')
    w1 = Process(target=open_window,args=('window 1',(800,600),(255,255,255)))
    w2 = Process(target=open_window,args=('window 2',(900,700),(0,255,255)))
    w3 = Process(target=open_window,args=('window 3',(400,300),(0,0,0)))
    print('启动')
    w1.start()
    print('等待1s')
    pygame.time.delay(1000)
    w2.start()
    print('等待1s')
    pygame.time.delay(1000)
    w3.start()
    w1.join()
    w2.join()
    w3.join()
    print('<主进程结束>')

print(f'任意进程的标志: {__name__}')