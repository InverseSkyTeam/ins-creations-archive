import pygame,sys,random,time
pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("物理空间")
try:
    import ntpath # 如果成功，那么是Windows
    FONTNAME = "kaiti"
    del ntpath
except ImportError: # 如果失败，是MacOS
    FONTNAME = "kaittf"
startlist = [pygame.image.load("game_start_up.png"),pygame.image.load("game_start_down.png")]
startlist[1] = pygame.transform.scale(startlist[1],(300,50))
startlist[0] = pygame.transform.scale(startlist[0],(300,50))
startrect = pygame.Rect(490,550,300,50)
startimg = startlist[0]
mouse_x = 0
mouse_y = 0
class Ball():
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0,1230),-50,50,50)
        self.m = 10
        self.g = 9.8
        self.v = self.rect.h*self.rect.h
        self.ρ = 0.001
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.k = 0.7
        self.flag = 0
        self.distance = 360
        self.plus_x = random.randint(-4,4)
        self.f = 0.9
    def show(self):
        self.rect.y += self.m*self.g/10/2
        self.rect.x += self.plus_x
        if self.rect.y >= 670:
            self.flag = 1
            self.plus_x *= self.f
        if self.rect.x >= 1230 or self.rect.x < 0:
            self.plus_x = -self.plus_x
        if self.flag == 1:
            self.rect.y -= self.m*self.g/10
            if self.rect.y<(720-self.distance):
                self.distance *= self.k
                if self.distance<1:
                    self.distance = 0
                self.flag = 0
        pygame.draw.ellipse(screen,self.color,self.rect,0)
ball = Ball()
ball2 = Ball()
ball3 = Ball()
ball4 = Ball()
ball5 = Ball()
ball6 = Ball()
ball_list = [ball3,ball4,ball5,ball6]
x = 670
x2 = 670
huarect = pygame.Rect(760,219,20,20)
huarect2 = pygame.Rect(760,219,20,20)
def draw_rect(pos,width,height,lenth,color):
    x = pos[0]
    y = pos[1]
    rect = pygame.Rect(x,y,width,height)
    pygame.draw.rect(screen,color,rect,lenth)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_x,mouse_y = event.pos
        if startrect.collidepoint(mouse_x,mouse_y):
            startimg = startlist[1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    t1 = time.time()
                    while True:
                        t2 = time.time()
                        if t2-t1 >= 0.2:
                            ball_list.append(Ball())
                            ball_list[-1].rect.x = random.randint(0,1230)
                            ball_list[-1].rect.y = -50
                            t1 = time.time()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        screen.fill((0,0,0))
                        for i in ball_list:
                            i.show()
                            for j in ball_list:
                                if j!=i:
                                    if i.rect.colliderect(j.rect):
                                        if (i.plus_x >0 and j.plus_x <0) or (i.plus_x <0 and j.plus_x >0):
                                            i.plus_x = -i.plus_x
                                            j.plus_x = -j.plus_x
                                        else:
                                            i.plus_x = -i.plus_x
                        pygame.display.update()
        else:
            startimg = startlist[0]
    if ball.rect.colliderect(ball2.rect):
        if (ball.plus_x >0 and ball2.plus_x <0) or (ball.plus_x <0 and ball2.plus_x >0):
            ball.plus_x = -ball.plus_x
            ball2.plus_x = -ball2.plus_x
        else:
            ball.plus_x = -ball.plus_x
    screen.fill((0,0,0))
    ball.show()
    ball2.show()
    screen.blit(pygame.font.SysFont(FONTNAME,150).render("物理空间",True,(255,255,255)),(340,150))
    screen.blit(startimg,startrect)
    pygame.display.update()