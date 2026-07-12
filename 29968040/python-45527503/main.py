import pygame,sys,pygame.gfxdraw,pic
from PIL import Image
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("我的作品")
myImg = Image.open('img1 (1).png')

move=0
p=[[5,5],
[5,365],
[545,365],
[545,5]]
def circle_collidepoint(mouse_pos,center,r):
    return pygame.Rect(center[0]-r,center[1]-r,2*r,2*r).collidepoint(mouse_pos)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    if pygame.mouse.get_pressed()[0]:
        pos=pygame.mouse.get_pos()
        if not move:
            for i in range(4):
                if circle_collidepoint(pos,p[i],6):
                    move=i+1
                    break
        else:
            p[move-1]=pos
    else:
        move=0
    pic.calc_img(p[0],p[1],p[2],p[3],myImg,screen)
    pygame.draw.circle(screen, (0,0,0), p[0], 6)
    pygame.draw.circle(screen, (0,0,0), p[1], 6)
    pygame.draw.circle(screen, (0,0,0), p[2], 6)
    pygame.draw.circle(screen, (0,0,0), p[3], 6)
    pygame.display.update()