import pygame,sys,time
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("我的作品")
big = pygame.transform.scale(pygame.image.load("aunt.png"),(200,200)).convert_alpha()
small = pygame.transform.scale(pygame.image.load("mal.png"),(100,100)).convert_alpha()
rectbig=pygame.Rect(200,200,200,200)
rectsmall=pygame.Rect(0,0,100,100)
sx=0
sy=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            sy=sy-0.6
        if event.key == pygame.K_DOWN:
            sy=sy+0.6
        if event.key == pygame.K_LEFT:
            sx=sx-0.6
        if event.key == pygame.K_RIGHT:
            sx=sx+0.6
    rectsmall=pygame.Rect(sx,sy,100,100)
    maskbig=pygame.mask.from_surface(big)
    masksmall=pygame.mask.from_surface(small)
    offset=(int(200-sx),int(200-sy))
    if masksmall.overlap(maskbig,offset)!=None: # 已经碰撞
        print(masksmall.overlap(maskbig,offset))
    else:
        if rectsmall.colliderect(rectbig):
            print("Rect:Yes")
            
        print("Mask:NO-Collide")
    screen.fill((255,255,255))
    #pygame.draw.rect(screen,(50,50,50),rectsmall,0)
    #pygame.draw.rect(screen,(150,150,225),rectbig,0)
    screen.blit(big,rectbig)
    screen.blit(small,(sx,sy))
    #print(f"{sx},{sy}")
    time.sleep(0.01)
    pygame.display.update()