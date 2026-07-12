import pygame,sys
pygame.init()
screen = pygame.display.set_mode((580,918))
pygame.display.set_caption("预告")
myImg = pygame.image.load("伊始.jpg")
try:
    import ntpath # 如果成功，那么是Windows
    FONTNAME = "kaiti"
    del ntpath
except ImportError: # 如果失败，是MacOS
    FONTNAME = "kaittf"
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    screen.blit(myImg,(0,0))
    screen.blit(pygame.font.SysFont(FONTNAME,40).render("starter",True,(255,255,255)),(220,409))
    screen.blit(pygame.font.SysFont(FONTNAME,40).render("伊始",True,(255,255,255)),(250,469))
    pygame.display.update()