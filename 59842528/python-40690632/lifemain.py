SCRRENW = 780
SCREENSIZE = (SCRRENW,SCRRENW)

import random,pygame,sys,time

maps = []

class Modes():
    def __init__(self,name,pos,width,window):
        self.pos = pos
        self.name = name
        self.width = width
        self.image = pygame.transform.scale(pygame.image.load(name),(width,width))
        self.rect = pygame.Rect(pos[0],pos[1],width,width)
        self.towindows = window
    def showa(self):
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.width,self.width)
        screen.blit(self.image,self.rect)
        
    def showb(self,kuan):
        self.rect = pygame.Rect(self.pos[0]-kuan/2,self.pos[1]-kuan/2,self.width+kuan,self.width+kuan)
        self.image = pygame.transform.scale(pygame.image.load(self.name),(self.width+kuan,self.width+kuan))
        screen.blit(self.image,(self.pos[0]-kuan/2,self.pos[1]-kuan/2))
        self.image = pygame.transform.scale(pygame.image.load(self.name),(self.width,self.width))

    def show(self,kuan,cupofmouse):
        global windows,isFirstEnterTheModes
        if self.rect.collidepoint(cupofmouse)==False:
            self.showa()
            if event.type == pygame.MOUSEBUTTONDOWN:
                windows = self.towindows 
                print(self.name+"to:",windows)
                isFirstEnterTheModes =True
        else:
            self.showb(kuan)

class DanMu:
    def __init__(self,text,y,c=1,s=25):
        self.text = text
        self.y = y
        self.x = 0
        self.c = 0
        self.mostc = c 
        self.canshow = True
        self.kc = pygame.font.Font("./Fonts/Circle.otf",s).render(text,True,(100,100,100))
    def show(self):
        if self.canshow:
            screen.blit(self.kc,(self.x,self.y))
            self.x +=0.5
            if(self.x > SCRRENW):
                self.x = 0
                self.c += 1
                if(self.c>=self.mostc):
                    self.x = 2000
                    self.canshow = False

modeslist = []
tx = 100
ty = 180
modessize = int(SCRRENW/2-150)
namelist = ["Mode0.png","Mode1.png"]
for i in range(0,2):
    print(i+1)
    nameofm = "Modes/"+namelist[i]
    print(nameofm,100+i)
    
    if (i+1)%2 == 0:
        tx += (100+modessize)
    else :
        tx = 100
    print(nameofm,100+i,tx)    
    modeslist.append(Modes(nameofm,(tx,ty),modessize,100+i))

def initarr(n):
    newmap = []
    for i in range(n):
        litmap = []
        for j in range(n):
            litmap.append(0)
        newmap.append(litmap)
    return newmap

def initmaps(n,num):
    newmap = initarr(n)
    for i in range(num):
        newmap[random.randint(0,n-1)][random.randint(0,n-1)] = 1
    return newmap

def initcreatemaps(n):
    newmap = initarr(n)
    rectsize = int((SCREENSIZE[0]-60)/n)+0.5
    x = 10
    y = 10
    for i in range(n):
        y=10
        for j in range(n):
            newmap[i][j] = pygame.Rect(x,y,rectsize,rectsize)
            y+=rectsize
        x+=rectsize
    return newmap


def drawmaps(curp):
    arr = curp
    rectsize = int((SCREENSIZE[0]-60)/len(curp))+0.5
    x = 10
    y = 10
    for i in arr:
        y=10
        for j in i:
            if j==0:
                pygame.draw.rect(screen,(255,255,255),pygame.Rect(x,y,rectsize,rectsize),0)
                pygame.draw.rect(screen,(205,235,235),pygame.Rect(x,y,rectsize,rectsize),1)
                #pygame.draw.rect(screen,(0,0,0),pygame.Rect(x,y,rectsize,rectsize),1)
                #pygame.draw.rect(screen,(50,50,50),pygame.Rect(x,y,rectsize,rectsize),1)
                #noline
            elif j==1:
                pygame.draw.rect(screen,(0,0,0),pygame.Rect(x,y,rectsize,rectsize),0)
                pygame.draw.rect(screen,(205,235,235),pygame.Rect(x,y,rectsize,rectsize),1)
            y+=rectsize
        x+=rectsize
def changecreate(arr,count):
    global event
    a=arr
    c = count
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j].collidepoint(pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN:
                print(11111)
                if(c[i][j]==0):
                    c[i][j]=1
                elif(c[i][j]==1):
                    c[i][j]=0
    return c
def nextmaps(arr):
    size = len(arr)
    newmaps = initarr(size)
    wayx = [0,0,1,-1,1,1,-1,-1]
    wayy = [1,-1,0,0,1,-1,1,-1]
    for i in range(size):
        for j in range(size):
            lives = 0
            for m in range(8):
                nowx = i+wayx[m]
                nowy = j+wayy[m]
                if nowx >=0 and nowx<size and nowy >=0 and nowy<size :
                    if arr[nowx][nowy] == 1:
                        lives += 1
            if lives==2:
                newmaps[i][j] = arr[i][j]
            elif arr[i][j]==0:
                if lives==3:
                    newmaps[i][j] = 1
                else:
                    newmaps[i][j] = 0
            elif arr[i][j]==1:
                if lives!=2 and lives!=3:
                    newmaps[i][j] = 0
                else:
                    newmaps[i][j] = 1
    return newmaps

def middleBlit(strs,y,size,rgb=(0,0,0),pix=0):
    itf = pygame.font.Font("./Fonts/Circle.otf",size)
    it = itf.render(strs,True,rgb)
    sum = size*len(strs)/2.0
    screen.blit(it,(SCRRENW/2-sum/2+pix,y))





rainbow = []
for i in range(10000):
    rainbow.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
pixa = [0,0,-5,0,-15,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


def colorBlit1(strs,y, size ,rgb=rainbow,pix=0,fix=0):
    global screen
    x=SCRRENW/2-size*len(strs)/2/2+pix
    nx =  x
    for i in range(len(strs)):
        itf = pygame.font.Font("./Fonts/Circle.otf",size)
        it = itf.render(strs[i],True,rgb[i])
        screen.blit(it,(nx,y))
        nx+=size/(2-fix)
def colorBlit2(strs,y, size ,rgb=rainbow,pix=0,fix=0):
    x=SCRRENW/2-size*len(strs)/2/2+pix
    random.shuffle(rgb)
    global screen
    nx =  x
    for i in range(len(strs)):
        itf = pygame.font.Font("./Fonts/Circle.otf",size)
        it = itf.render(strs[i],True,rgb[i])
        screen.blit(it,(nx,y))
        nx+=size/(2-fix)



#arrs = initmaps(30,100)
pygame.init()
screen = pygame.display.set_mode((SCREENSIZE[0],SCREENSIZE[1]))
pygame.display.set_caption("LifeGame")
windows = 0 
'''
0 root 
1 choose px*px
2 choose lives
3 settings
4 choose mode

100 random mode
101 create mode
'''

font = pygame.font.Font("./Fonts/Circle.otf",100)
txfo = pygame.font.Font("./Fonts/Circle.otf",50)
text1=font.render("Life Game",True,(100,100,100))
text2=txfo.render("Press Space to begin",True,(100,100,100))
text3=pygame.font.Font("./Fonts/Circle.otf",50).render("Input the width Of the new Game",True,(100,100,100))
text4=txfo.render("Input the init lives Of the new Game",True,(100,100,100))
settings = pygame.transform.scale(pygame.image.load("Images/setting.png"),(50,50))
settingsrect = pygame.Rect(SCRRENW-60,10,50,50)
back = pygame.transform.scale(pygame.image.load("Images/back.png"),(50,50))
backrect = pygame.Rect(SCRRENW-60,SCRRENW-60,50,50)

#Merry Christmas Mr. Lawrence
pygame.mixer.music.load("./Medias/MerryChristmasMr.Lawrence.wav")
pygame.mixer.music.set_volume(0.08)
pygame.mixer.music.play(-1)

#settings

fps = 30
isFirstEnterTheModes = False
turns = 0
countofchangingcholor=0

textfps1 = txfo.render("FPS" +int(fps/5)*"·",True,(100,100,100))
textfps2 = txfo.render("Press F to turn up And Press S to turn down",True,(100,100,100))


d1 = DanMu("点击格子绘制，键盘→键进行生命迭代，esc键退出",random.randint(0,SCRRENW-20),c=2,s=20)

while True:

    #print("windows",windows)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if windows==0 and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                windows = 4
                num = 0

    screen.fill((235,235,235))
    

    if windows == 0:
        colorBlit1("Life",320,100,pix=-140)
        colorBlit1("Game",320,100,pix=100,fix=0.6)
        colorBlit1("Press Space to begin",430,50,pix=0)
        #screen.blit(text2,(165,430))
        
        countofchangingcholor+=1
        if countofchangingcholor%100==0:
            countofchangingcholor=0
            colorBlit2("Life",320,100,pix=-140)
            colorBlit2("Game",320,100,pix=100,fix=0.6)

    if windows == 1:
  
        middleBlit("Input the width Of the new Game",420,35)
        middleBlit("And Press Enter to make Sure",460,35)
        middleBlit(str(num),320,100)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    num = num//10
                if event.key == pygame.K_RETURN:
                    windows = 2
                    newgamewidth = num
                    num = 0
                    break
                if num <= 66:
                    if event.key == pygame.K_1:
                        num = num*10+1
                    if event.key == pygame.K_2:
                        num = num*10+2
                    if event.key == pygame.K_3:
                        num = num*10+3
                    if event.key == pygame.K_4:
                        num = num*10+4
                    if event.key == pygame.K_5:
                        num = num*10+5
                    if event.key == pygame.K_6:
                        num = num*10+6
                    if event.key == pygame.K_7:
                        num = num*10+7
                    if event.key == pygame.K_8:
                        num = num*10+8
                    if event.key == pygame.K_9:
                        num = num*10+9
                    if event.key == pygame.K_0:
                        num = num*10
    if windows == 2:

        top = newgamewidth

        #screen.blit(text3,(170,420))
        middleBlit("Input Init Lives Of the Game",420,35)
        middleBlit("And Press Enter to make Sure",460,35)
        #numtext = font.render(str(num),True,(100,100,100))
        #screen.blit(numtext,(SCRRENW/2-bits*50/2,320))
        middleBlit(str(num),320,100)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    num = num//10
                if event.key == pygame.K_RETURN:
                    windows = readytowindow
                    newgameinitlives = num
                    num = 0
                    arrs=[]
                    if readytowindow==101:
                        arrs= initcreatemaps(newgamewidth)
                        countmap = initarr(newgamewidth)
                    elif readytowindow==100:
                        arrs = initmaps(newgamewidth,newgameinitlives)
                    turns+=1
                    break
                if num <= top*top/10:
                    if event.key == pygame.K_1:
                        num = num*10+1
                    if event.key == pygame.K_2:
                        num = num*10+2
                    if event.key == pygame.K_3:
                        num = num*10+3
                    if event.key == pygame.K_4:
                        num = num*10+4
                    if event.key == pygame.K_5:
                        num = num*10+5
                    if event.key == pygame.K_6:
                        num = num*10+6
                    if event.key == pygame.K_7:
                        num = num*10+7
                    if event.key == pygame.K_8:
                        num = num*10+8
                    if event.key == pygame.K_9:
                        num = num*10+9
                    if event.key == pygame.K_0:
                        num = num*10

    if windows == 3:
        middleBlit("SETTINGS",32,80,pix=-5)
        screen.blit(back,backrect)
        colorBlit1("FPS:" +str(fps)+"[",130,40,pix=-240,fix=0.5)
        colorBlit1(int(fps/5)*"■"+ " ]",135,30,pix=-10,fix=1)
        colorBlit1("Press F to turn up And Press S to turn down",190,30,pix=10,fix=0)
        colorBlit1("[F键提高每秒迭代次数，S键调低每秒迭代次数]",230,30,pix=-150,fix=1)
        if backrect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
            print(lastwindow)
            windows = lastwindow 
            print(windows)
        countofchangingcholor+=1
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    if fps<=79:
                        fps+=1
                if event.key == pygame.K_s:
                    if fps>=2:
                        fps-=1
        if countofchangingcholor%100==0:
            countofchangingcholor=0
            colorBlit2("FPS:" +str(fps)+"[",130,40,pix=-240,fix=0.5)
            colorBlit2(int(fps/5)*"■",135,30,pix=-10,fix=1)

    if windows == 4:
        middleBlit("MODE",32,90,pix=-5)
        for i in modeslist:
            i.show(100,pygame.mouse.get_pos())

    if windows == 100:
        if isFirstEnterTheModes:
            last = []
            readytowindow = 100
            windows = 1
            isFirstEnterTheModes = False
        else:
            drawmaps(arrs)
            last.append(arrs)
            arrs = nextmaps(arrs)
            try:
                if arrs == last[-1] or arrs == last[-2] or arrs == last[-3]:
                    screen.fill((235,235,235))
                    drawmaps(initarr(newgamewidth))
                    middleBlit("The World 00"+str(turns),300,40)
                    middleBlit("Was died or Recycled",350,40) 
                    pygame.display.update()
                    time.sleep(3)
                    windows=0
            except:
                pass
            time.sleep(1/fps)
    #'''
    if windows == 101:
        if isFirstEnterTheModes:
            readytowindow = 101
            windows = 1
            isFirstEnterTheModes = False
        else:
            drawmaps(countmap)
            d1.show()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    countmap = nextmaps(countmap)
                if event.key == pygame.K_ESCAPE:
                    screen.fill((235,235,235))
                    drawmaps(initarr(newgamewidth))
                    middleBlit("The World 00"+str(turns)+" You Made",300,40)
                    middleBlit("Was Died,Recycled Or GivenUp",350,40) 
                    pygame.display.update()
                    time.sleep(3)
                    windows=0
            else:
                countmap = changecreate(arrs,countmap)
            time.sleep(1/fps)
    #'''    
    if windows!=3:
        screen.blit(settings,settingsrect)
        if settingsrect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
            lastwindow = windows
            windows = 3


    pygame.display.update()