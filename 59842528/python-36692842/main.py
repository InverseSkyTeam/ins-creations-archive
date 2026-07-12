import pygame,sys,random,time
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("排序算法可视化")
normalstyle = pygame.font.Font("HYTiaoTiaoTiJ.ttf",40)





class ViewSort:
    def __init__(self,arr,sx,sy,width,maxnum):
        self.arr = arr
        self.sx = sx
        self.sy = sy
        self.width = width
        self.maxheight = maxnum*7
        self.normalstyle = pygame.font.Font("HYTiaoTiaoTiJ.ttf",20)
    def show(self,screen):
        x=self.sx
        y=self.sy
        width=self.width
        maxheight=self.maxheight
        rectlist=[]
        numlist=[]
        for i in range(len(self.arr)):
            rectlist.append(pygame.Rect(x,y+maxheight-self.arr[i]*5,width,self.arr[i]*5))
            if i%2==0:
                numlist.append([self.normalstyle.render(str(self.arr[i]),True,(240,240,240)),x,y+maxheight+20])
            else:
                numlist.append([self.normalstyle.render(str(self.arr[i]),True,(10,10,10)),x,y+maxheight+20])
            x+=(width*2)
        for i in range(len(rectlist)):
            if i%2==0:
                pygame.draw.rect(screen,(240,240,240),rectlist[i],0)
                screen.blit(numlist[i][0],(numlist[i][1],numlist[i][2]))
            else:
                pygame.draw.rect(screen,(10,10,10),rectlist[i],0)
                screen.blit(numlist[i][0],(numlist[i][1],numlist[i][2]))
class Btn:
    def __init__(self,name,x,y,MPv):
        self.x = x+10
        self.y = y+5
        self.name =name
        self.MPval =MPv
        self.rect=pygame.Rect(x,y,125,45)
        self.normalstyle = pygame.font.Font("HYTiaoTiaoTiJ.ttf",25)
        self.text = self.normalstyle.render(name,True,(50,50,50))
    def Blit(self,screen):
        global MP
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen,(134,149,165),self.rect,0)
            screen.blit(self.text,(self.x,self.y))
            if event.type==pygame.MOUSEBUTTONDOWN:
                MP=self.MPval
        else:
            pygame.draw.rect(screen,(224,214,199),self.rect,0)
            screen.blit(self.text,(self.x,self.y))
            
            
btnlist=[]
unorderedlist=[]
sortnamelist=["冒泡排序","选择排序","插入排序","快速排序"]
for i in range(10):
    unorderedlist.append(random.randint(10,75))
btnx,btny,sumofbtn = 60,150,0
for i in range(len(sortnamelist)):
    btnlist.append(Btn(sortnamelist[i],btnx,btny,i+1))
    sumofbtn+=1
    if sumofbtn%3==0:
        btny+=80
        btnx=60
    else:
        btnx+=165
    
MP=0
A = ViewSort(unorderedlist,100,350,20,25)  
B = ViewSort(unorderedlist,100,350,20,25)  
C = ViewSort(unorderedlist,100,350,20,25)  








while True:
    screen.fill((133,161,248))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if MP==0:
        screen.blit(normalstyle.render("Python排序算法",True,(10,10,10)),(170,80))
        for i in btnlist:
            i.Blit(screen)
        pygame.display.update()
    if MP==1:
        A.show(screen)
        for i in range(len(unorderedlist)):
            isOK=True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            for j in range(len(unorderedlist)-i-1):
                if A.arr[j]>A.arr[j+1] :
                    temp=A.arr[j]
                    A.arr[j]=A.arr[j+1]
                    A.arr[j+1]=temp
                    isOK = False
                screen.fill((133,161,248))
                screen.blit(normalstyle.render("冒泡排序",True,(10,10,10)),(220,80))
                A.show(screen)
                pygame.display.update()
                pygame.time.wait(300)
            if isOK:
                break
            screen.blit(normalstyle.render("冒泡排序",True,(10,10,10)),(220,80))
            pygame.display.update()
            
        unorderedlist=[]
        for i in range(10):
            unorderedlist.append(random.randint(10,75))
        A.arr=unorderedlist
        MP=0
    if MP==2:
        B.show(screen)
        for i in range(len(unorderedlist)-1):
            max=0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            for j in range(len(unorderedlist)-i):
                if B.arr[j]>B.arr[max]:
                    max=j
                    pygame.time.wait(300)
            temp=B.arr[len(unorderedlist)-1-i]
            B.arr[len(unorderedlist)-1-i]=B.arr[max]
            B.arr[max]=temp
            screen.fill((133,161,248))
            screen.blit(normalstyle.render("选择排序",True,(10,10,10)),(220,80))
            B.show(screen)
            pygame.display.update()
            pygame.time.wait(300)
            screen.blit(normalstyle.render("选择排序",True,(10,10,10)),(220,80))
            pygame.display.update()
        unorderedlist=[]
        for i in range(10):
            unorderedlist.append(random.randint(10,75))
        B.arr=unorderedlist
        MP=0 
    if MP==3:
        C.show(screen)
        for i in range(1,len(unorderedlist)):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            j=i
            while C.arr[j]<C.arr[j-1] and j>=1:
                temp=C.arr[j-1]
                C.arr[j-1]=C.arr[j]
                C.arr[j]=temp
                screen.fill((133,161,248))
                screen.blit(normalstyle.render("插入排序",True,(10,10,10)),(220,80))
                C.show(screen)
                pygame.display.update()
                pygame.time.wait(300)
                j-=1
            screen.blit(normalstyle.render("插入排序",True,(10,10,10)),(220,80))
            pygame.display.update()
        unorderedlist=[]
        for i in range(10):
            unorderedlist.append(random.randint(10,75))
        C.arr=unorderedlist
        MP=0 
    
    pygame.display.update()
