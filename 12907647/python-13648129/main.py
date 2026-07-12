import pygame,sys,time
pygame.init()
pygame.display.set_caption("我的作品")
myImg = pygame.image.load("image\封面大型翻车现场.png")
myImg2 = pygame.image.load("image\一个个点开.png")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen = pygame.display.set_mode((1300,700))
    screen.fill((255,255,255))
    screen.blit(myImg,(0,0))
    pygame.display.update()
    time.sleep(3)
    screen = pygame.display.set_mode((1300,800))
    screen.fill((255,255,255))
    screen.blit(myImg2,(0,0))
    pygame.display.update()
    time.sleep(3)