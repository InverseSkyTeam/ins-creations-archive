import pygame,sys
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("我的作品")




s = pygame.sprite.Sprite()
s.image = pygame.transform.scale(pygame.image.load('A.png'),(350,350))
s.rect = pygame.Rect(300,150,350,350)

c = pygame.sprite.Sprite()
c.image = pygame.transform.scale(pygame.image.load('B.png'),(200,200))
c.rect = pygame.Rect(0,0,100,100)
cx,cy=0,0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            cy=cy-0.6
        if event.key == pygame.K_DOWN:
            cy=cy+0.6
        if event.key == pygame.K_LEFT:
            cx=cx-0.6
        if event.key == pygame.K_RIGHT:
            cx=cx+0.6
    screen.fill((255,255,255))
    screen.blit(s.image, s.rect)
    c.rect = pygame.Rect(cx,cy,100,100)
    
    if pygame.sprite.collide_mask(s, c)==None:
        print("Sprite-mask:NO-Collide")
        if c.rect.colliderect(s.rect):
            print("Rect:Collide")
    else:
        print(pygame.sprite.collide_mask(s, c))
    '''
    print(pygame.sprite.collide_circle(s, c))
    print("RECT:",pygame.sprite.collide_rect(s, c))
    '''
    screen.blit(c.image, c.rect)
    pygame.display.update()