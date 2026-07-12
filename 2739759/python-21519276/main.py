import pygame,sys,xes.ext,time
pygame.init()
screen = pygame.display.set_mode((800,259))
pygame.display.set_caption("预告")
myImg = pygame.image.load("word_img.JPG")
myDate = time.strftime("%Y-%m-%d", time.localtime())
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
    d = xes.ext.date_diff("2022-06-09",myDate)
    screen.blit(pygame.font.SysFont(FONTNAME,40).render(str(d)+"天"+str(24-time.localtime()[3]-1)+"时"+str(60-time.localtime()[4]-1)+"分"+str(60-time.localtime()[5])+"秒",True,(0,0,0)),(240,105))
    pygame.display.update()