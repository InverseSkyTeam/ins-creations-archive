import pygame,sys,tkinter,tkinter.filedialog
def upload():
    selectFileName = tkinter.filedialog.askopenfilename(title='选择图片')
    return selectFileName
pygame.init()
screen = pygame.display.set_mode((300,300))
img = pygame.image.load("yzx.ico")
pygame.display.set_icon(img) # 可以填img
pygame.display.set_caption("yzx{像素化头像}choose")
try:
    st1 = pygame.image.load(str(upload())).convert()
except:
    st1 = pygame.image.load("zuoye.jpg").convert()
bst1=pygame.transform.scale(st1,(6,6)).convert()
pygame.mixer.music.load("时代少年团-无尽的冒险.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
try:
    mf=pygame.font.SysFont("kaiti",20)
    mf1=pygame.font.SysFont("方正舒体",17)
except:
    mf=pygame.font.SysFont("kaittc",20)
    mf1=pygame.font.SysFont("kaittf",17)
mt=mf.render("选择模式:",True,(75,75,75))
mtt=mf1.render("Press ButtonA 主图像在上",True,(75,75,75))
mttt=mf1.render("Press ButtonB 主图像在下",True,(75,75,75))
'''
t1=mf1.render("1.#include <bits/stdc++.h>",True,(50,50,50))
t2=mf1.render("2.using namespace std;",True,(50,50,50))
t3=mf1.render("3.int main(){ ",True,(50,50,50))
t4=mf1.render("4.    cout<<\"Hello World.\"",True,(50,50,50))
t5=mf1.render("5.    return 0;}",True,(50,50,50))
'''
n=0
count=0
while(n!=1 or n!=2):
    if n==0:
        screen.fill((230,230,230))
        screen.blit(mt,(30,100))
        screen.blit(mtt,(30,125))
        screen.blit(mttt,(30,150))
    elif count==0:
        screen.fill((255,255,255))
        count+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                print("hhhh")
                n=1
                break
            if event.key==pygame.K_b:
                print("hhhh")
                n=2
                break
    if n==1:
        st1.set_alpha(5)
        st1=pygame.transform.scale(st1,(300,300))
        bst1=pygame.transform.scale(st1,(6,6))
    elif n==2:
        st1=pygame.transform.scale(st1,(300,300))
        bst1=pygame.transform.scale(st1,(6,6)).convert()
        bst1.set_alpha(5)
    pygame.display.update()
    if n==0:
        continue
    if n==1:
        print(1)
        #screen.fill((255,255,255))
        for i in range(0,300,10):
            for j in range(0,300,10):
                screen.blit(bst1,(i,j))
        screen.blit(st1,(0,0))
        '''
        screen.blit(t1,(20,10))
        screen.blit(t2,(20,29))
        screen.blit(t3,(20,48))
        screen.blit(t4,(20,67))
        screen.blit(t5,(20,86))
        '''
    elif n==2:
        #screen.fill((255,255,255))
        screen.blit(st1,(0,0))
        for i in range(0,300,10):
            for j in range(0,300,10):
                screen.blit(bst1,(i,j))

    pygame.display.update()
#别往下翻