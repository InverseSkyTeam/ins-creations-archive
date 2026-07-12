import pygame,sys,random

pygame.init()
screen = pygame.display.set_mode((1000,600))

try:import ntpath
except:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)")
else:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)")
finally:pass

class Ground:
    def __init__(self,x,y,c,length):
        self.rect = pygame.Rect(x,y,length,length)
        self.color = c

# rectlist = [Ground(i,j,(0,0,0),1) for i in range(800) for j in range(600)]
# rectlist = [Ground(i*2,j*2,(0,0,0),2) for i in range(400) for j in range(300)]
# rectlist = [Ground(i*5,j*5,(0,0,0),5) for i in range(160) for j in range(120)]
# rectlist = [Ground(i*10,j*10,(0,0,0),10) for i in range(80) for j in range(60)]
# rectlist = [Ground(i*20,j*20,(0,0,0),20) for i in range(40) for j in range(30)]
rectlist = [Ground(i*50,j*50,(180,180,180),50) for i in range(16) for j in range(12)]
mouseleftbutton_isdown = False
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseleftbutton_isdown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseleftbutton_isdown = False
    screen.fill((255,255,255))
    if mouseleftbutton_isdown == True:
        for i in rectlist:
            if i.rect.collidepoint(event.pos):
                i.color = (111,255,255)
    for i in rectlist:
        pygame.draw.rect(screen,i.color,i.rect,0)
    show_text(str(round(clock.get_fps(),1))+'/FPS',(0,0,0),(811,11),40)
    pygame.display.update()
    clock.tick()