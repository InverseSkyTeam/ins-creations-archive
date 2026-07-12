import keyboard
import pygame,sys,random
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("我的作品")
class Game():
    
    def __init__(self,w,h,sw,sh):
        self.mapw =w
        self.maph =h
        self.sw =sw
        self.sh =sh
        self.safe = []
        self.hero = self.initHero()
        self.danger = []

    def addRec(self,recs):
        for i in recs:
            rec = Rectangle(i[0],i[1],i[2])
            if i[3]==1:
                self.safe.append(rec)
            else:
                self.danger.append(rec)
    def initHero(self):
        return Hero((0,40),40,(50,100,150))
    
    def showAll(self):
        for i in self.safe:
            i.show()
        for i in self.danger:
            i.show()
        self.hero.show()
        pygame.display.update()

    def clearAll(self):
        screen.fill((255,255,255))

    def cleanAndShow(self):
        self.showAll()
        #pygame.display.update()
        #self.clearAll()

    def isCollideSafe(self):
        for i in self.safe:
            if self.hero.rect.colliderect(i):
                return True
        return False

    def isCollideDanger(self):
        for i in self.danger:
            if self.hero.rect.colliderect(i):
                return True
        return False

    def heroChangeX(self,point):
        self.hero.x += point
        self.hero.updaterect()
        self.cleanAndShow()
    def heroChangeY(self,point):
        self.hero.y += point
        self.hero.updaterect()
        self.cleanAndShow()

    def heromove(self):
        global event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.hero.waittoadx -= 0.1
            if event.key == pygame.K_RIGHT:
                self.hero.waittoadx += 0.1 #y同比例缩小sc50倍 x同比例缩小sc10倍
        self.hero.waittoadx*=0.9

        self.hero.x += self.hero.waittoadx
        self.hero.updaterect()
        self.cleanAndShow()

        #if self.hero.isCollideSafe():
        if self.isCollideSafe():
            self.heroChangeY(-0.1)
            if self.isCollideSafe():
                self.heroChangeY(-0.1)
                if self.isCollideSafe():
                    self.heroChangeY(-0.1)
                    if self.isCollideSafe():
                        self.heroChangeY(-0.1)
                        if self.isCollideSafe():
                            self.heroChangeX(self.hero.waittoadx*-1)
                        
                        if event.type == pygame.KEYDOWN: 
                            if event.key == pygame.K_UP or event.key == pygame.K_w:
                                print(2)
                                if self.hero.waittoadx>0:
                                    self.hero.waittoadx = -0.1
                                else:
                                    self.hero.waittoadx = 0.1
                                self.hero.waittoady = -0.8
                            else:
                                self.hero.waittoadx = 0
        self.hero.waittoady += 0.05
        self.heroChangeY(self.hero.waittoady)     
        if self.isCollideSafe():
     
            self.heroChangeY(self.hero.waittoady*-0.1)  
            self.hero.waittoady=0 
        self.heroChangeY(-0.1)     
        if self.isCollideSafe():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    print(1)
                    self.hero.waittoady = -0.7
        self.heroChangeY(0.1) 

class Hero():
    def __init__(self,pos,w,color,kuan=10):
        self.x = pos[0] 
        self.y = pos[1]
        self.w = w
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,self.w,self.w)
        self.kuan = kuan
        self.waittoadx = 0
        self.waittoady = 0
    
    def show(self):
        pygame.draw.rect(screen,self.color,self.rect,0)
        pygame.draw.rect(screen,(self.color[0]-20,self.color[1]-20,self.color[2]-20),self.rect,5)
   
    def updaterect(self):
        self.rect = pygame.Rect(self.x,self.y,self.w,self.w)

class Rectangle(Game):
    def __init__(self,pos,wight,color,kuan=10):
        self.x = pos[0] 
        self.y = pos[1]
        self.w = wight[0]
        self.h = wight[1]
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.kuan = kuan
    def show(self):
        pygame.draw.rect(screen,self.color,self.rect,0)
        pygame.draw.rect(screen,(self.color[0]-20,self.color[1]-20,self.color[2]-20),self.rect,5)
    


game = Game(70,50,700,500)   
game.addRec([((0,470),(700,30),(73,172,211),1),((120,300),(30,50),(233,172,111),1)]) 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    game.showAll()
    game.heromove()
    pygame.display.update()