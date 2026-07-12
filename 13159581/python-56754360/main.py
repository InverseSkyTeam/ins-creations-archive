import pygame,os
from pygame.locals import *
pygame.init()

x=0
y=0
def collide_color(aSurface,aRect,aColor):
    pixel=pygame.PixelArray(aSurface)#锁定aSurface,将各点颜色保存在2维数组
    aPixel=pixel[aRect.x:aRect.x+aRect.width,aRect.y:aRect.y+aRect.height]
    pygame.PixelArray.close(pixel) #解锁aSurface并删除数组,上句得到数组切片
    try:
        return aColor in aPixel#指定颜色在切片中返回真,两者颜色应同为rgb或rgba
    except:
        return 0

background_list = os.listdir("./地图")
index = 0
size = width,height = 600,400
bg = (255,255,255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("demo")
speed = [0,0]

clock = pygame.time.Clock()
background_image = pygame.image.load('./地图/'+background_list[index]).convert()
over = pygame.image.load("over.png").convert()
xuan = pygame.image.load("xuan.png").convert()
position = xuan.get_rect()
l_head = pygame.transform.flip(xuan,True,False)
r_head = xuan
#screen.blit(xuan,xuan.get_rect().move([0,300]))

boola = True
running=True
while running:
    FPS = str(round(clock.get_fps()))
    pygame.display.set_caption('fps:' + FPS)
    # x = 1
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False
    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_a] or key_pressed[K_LEFT]:
        x -= 0.5
        xuan=l_head
    if key_pressed[K_d] or key_pressed[K_RIGHT]:
        x += 0.5
        xuan=r_head

    position.x+=x
    x = 0.9*x

    if collide_color(background_image,position,(0,0,0)):
        position.y+=-1
        if collide_color(background_image,position,(0,0,0)):
            position.y+=-1
            if collide_color(background_image,position,(0,0,0)):
                position.y+=-1
                if collide_color(background_image,position,(0,0,0)):
                    position.y+=-1
                    if collide_color(background_image,position,(0,0,0)):
                        position.y+=-1
                        if collide_color(background_image,position,(0,0,0)):
                            if key_pressed[K_w] or key_pressed[K_UP]:
                                if x>0:
                                    x = -6
                                else:
                                    x = 6
                                y = -13
                            else:
                                x = x*-1.3
                                position.x+=x
                                x = 0
                            position.x+=x/5

    #y+=0.5
    #position = position.move([0,y])
    y+=0.5
    position.y+=y
    if collide_color(background_image,position,(0,0,0)):
        y*=-0.25
        position.y+=y
        if collide_color(background_image,position,(0,0,0)):
            position.y+=y
            if collide_color(background_image,position,(0,0,0)):
                position.y+=y
                if collide_color(background_image,position,(0,0,0)):
                    position.y+=y
    position.y+=1
    if collide_color(background_image,position,(0,0,0)):
        if key_pressed[K_w] or key_pressed[K_UP]:
            y = -13
    position.y+=-1

    #screen.fill(bg)
    if collide_color(background_image,position,(227,227,227)) and position.left>=0: 
        position.top,position.left = (0,0)
    if collide_color(background_image,position,(255,0,0)) and position.left>=0:
        position.top,position.left = (0,0)
    if collide_color(background_image,position,(240,250,10)) and position.left>=0: 
        y=-15
    if position.top<0:
        position.top,position.left = (0,0)
    if position.right>width:
        if index+1!=len(background_list):
            position.top,position.left = (0,0)
            index+=1
            background_image = pygame.image.load("./地图/"+background_list[index]).convert()
        else:
            background_image = over
            boola = False
    if position.left<0:
        position.left=0
    if position.bottom>height:
        position.top,position.left = (0,0)
    screen.blit(background_image, (0, 0))
    if boola:
        screen.blit(xuan,position)
    pygame.display.flip()
    #print(collide_color(background_image,position,pygame.Color('black')))

    clock.tick(30)

pygame.quit()