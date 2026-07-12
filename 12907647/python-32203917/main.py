r = int(input("输入rgb红色(r)值(0-255):"))
g = int(input("输入rgb绿色(g)值(0-255):"))
b = int(input("输入rgb蓝色(b)值(0-255):"))
t = 0
new = round((r+g+b)/3)
newf = 255-new
newd = round((new + newf) / 2)
print('按A查看原图，按B查看新图(真正的灰度图)，按C查看新图的反色，按D查看B和C的平均值')
print(r,g,b,'转化为',new,new,new)
import pygame,sys
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("灰度转换器")
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                t = 0
            if event.key == ord('b'):
                t = 1
            if event.key == ord('c'):
                t = 2
            if event.key == ord('d'):
                t = 3
    if t == 0:
        screen.fill((r,g,b))
    elif t == 1:
        screen.fill((new,new,new))
    elif t == 2:
        screen.fill((newf,newf,newf))
    else:
        screen.fill((newd,newd,newd))
    pygame.display.update()