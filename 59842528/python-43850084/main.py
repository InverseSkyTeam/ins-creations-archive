import pygame,sys,time
pygame.init()
screen = pygame.display.set_mode((900,500))
pygame.display.set_caption("曲谱滚动器")
times = 120
fps = 50

pu = pygame.image.load("1.jpg").convert()
x,y = pu.get_width(),pu.get_height()
pu = pygame.transform.scale(pu,(900,x/900*500))

speed = pu.get_height()/times/50
print(speed)
ny = 0

t1 = time.time()
t2= time.time()
counter = 0  

while t2-t1 < 1/50:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    t2= time.time()
    counter += 1
    pygame.display.update()
    
newcounter = 0  
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   
    if newcounter%counter==0 :
        ny-=2*speed
        if ny <= -pu.get_height():
            ny = 0
        newcounter = 0
    
    screen.fill((255,255,255))
    screen.blit(pu,(0,ny))
    
    newcounter+=1
    
    pygame.display.update()