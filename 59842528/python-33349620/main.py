import pygame,sys
from random import *

pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("2021圆吃圆")
bgImg0= pygame.image.load("bgp4.png")
bgImg=pygame.transform.scale(bgImg0,(700,700))
myFont = pygame.font.SysFont("kaiti", 37)
myFont1 = pygame.font.SysFont("kaiti", 60)
myFont2 = pygame.font.SysFont("kaiti", 52)
myFont3 = pygame.font.SysFont("kaiti", 40)
myText11 = myFont1.render("2021圆吃圆", True, (255, 255, 255))
myText22 = myFont2.render("任意键以开始", True, (255, 255, 255))
myText55 = myFont3.render("上下左右键控制大汤圆吃掉小汤圆", True, (255, 255, 255))
myText66 = myFont.render("在规定时间内进行挑战,只有一次机会加油", True, (255, 255, 255))


hero_x = 300      
hero_y = 300
hero_size = 66       #初始角色大小
score=0              #初始分数
times=25             #初始时间
level=0   
move=5               #移动速度
num=1
lin=0
flag=True
flag2=True
speed=[1,1]         
fruitList = []
save={}
rand=randint(0, 2)
font=pygame.font.SysFont(None,50)
sound1=pygame.mixer.Sound("eat.wav")
sound1.set_volume(0.2)
pygame.mixer.music.load("time.wav")
sound3=pygame.mixer.Sound("over.wav")
sound3.set_volume(0.7)
hero1 = pygame.image.load("h1.png")
hero2 = pygame.image.load("h2.png")
#hero3 = pygame.image.load("hero3.png")
heroImg = [hero1, hero2]
fruit10 = pygame.image.load("1.png")
fruit1=pygame.transform.scale(fruit10,(50,50))
fruit20 = pygame.image.load("2.png")
fruit2=pygame.transform.scale(fruit20,(50,50))
fruit30 = pygame.image.load("3.png")
fruit3=pygame.transform.scale(fruit30,(50,50))
fruit40 = pygame.image.load("4.png")
fruit4=pygame.transform.scale(fruit40,(50,50))
fruit50 = pygame.image.load("5.png")
fruit5=pygame.transform.scale(fruit50,(50,50))
gameover0= pygame.image.load("gameover.png")
gameover=pygame.transform.scale(gameover0,(300,300))
fruitImg = [fruit1, fruit2, fruit3, fruit4, fruit5]
hList=[hero1,hero2]
clock=pygame.time.Clock()
a=1
def fun(rect,a):
    speed=a
    if rect.left<0 or rect.right>700:
        speed[0]=-speed[0]
    if rect.top<0 or rect.bottom>700:
        speed[1]=-speed[1]
    return speed

def sun():
    global fruitImgs
    fruitImgs = pygame.transform.scale(fruitImg[randint(0, 4)], (40, 40))
    for i in range(randint(2,8)):
        fruitRect = pygame.Rect(randint(0,666),randint(0,666),40,40)
        fruitList.append(fruitRect)
    for i in fruitList:
        save[fruitList.index(i)]=[5,5]
sun() 


def nice(emoji_str):
    return ''.join(c if c <= '\uffff' else ''.join(chr(x) for x in struct.unpack('>2H', c.encode('utf-16be'))) for c in emoji_str)
def run_app(pid):
    pid=pid.split("&")[1].split("=")[1]
    import requests,time,random,os
    def load(url,name):
        import requests as req
        response = req.get(url)
        try:
            a=open(name,"wb")
            a.write(response.content)
            a.close()
        except:
            a=open(name,"w")
            a.write(response.text)
            a.close()
    def enter(k):
        url="http://code.xueersi.com/api/compilers/"+k+"?id="+k
        headers = {'Content-Type':'application/json'}
        a=requests.get(url=url, headers=headers)
        z=eval(a.text.replace("false","False").replace("true","True").replace("null","None"))
        return nice(z["data"]["xml"])
    def load_img(k):
        url="http://code.xueersi.com/api/compilers/"+k+"?id="+k
        headers = {'Content-Type':'application/json'}
        a=requests.get(url=url, headers=headers)
        z=eval(a.text.replace("false","False").replace("true","True").replace("null","None"))

        k=z["data"]["assets"]["assets"]
        for x in k:
            load(("https://livefile.xesimg.com/programme/python_assets/"+x["md5ext"]),x["name"])
    import time
    load_img(pid)
    time.sleep(1)
    clear_os()
    
    return enter(pid)
def clear_os():
    import sys
    sys.stdout.write("\033[2J\033[00H")

pygame.mixer.music.load("buttercup.mp3")
pygame.mixer.music.play(-1)
screen.blit(bgImg,(0,0))
while True:
    if a==1:
        screen.blit(myText11, (200, 110))
        screen.blit(myText22, (180, 500))
        
        screen.blit(myText55, (70, 260))
        screen.blit(myText66, (10, 380))
        

    pygame.display.update()
    clock.tick(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
            sys.exit()
    if event.type != pygame.KEYDOWN and a==1:        
        continue
    a=0
    press=pygame.key.get_pressed()
    if press[273]:
        hero_y = hero_y - move
    if press[274]:
        hero_y = hero_y + move
    if press[276]:
        hero_x = hero_x - move
    if press[275]:
        hero_x = hero_x + move
        
    heroImgs = pygame.transform.scale(choice(hList), (hero_size, hero_size))
    heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
    for n in fruitList:
        if heroRect.colliderect(n):
            sound1.play()
            score=score+1
            fruitList.remove(n)
            if hero_size<=280:
                hero_size=hero_size+5
                
    screen.blit(bgImg, (0, 0))
    screen.blit(heroImgs, (hero_x, hero_y))
    
    for rect in fruitList:
        a=fun(rect,save[fruitList.index(rect)])
        rect.x+=a[0]
        rect.y+=a[1]
        save[fruitList.index(rect)]=a
        screen.blit(fruitImgs, rect)
    key=level
    if fruitList==[] and flag:
        level=level+1
        sun() 
        
    num=num+1
    if times!=0:
        if num%50==0:
            times=times-1
            
    else:
        if flag:
            sound3.play()
        flag=False
        fruitList=[]
        
        screen.blit(gameover,(200,200))
        ft1_surf=font.render("Your final score is:"+str(score),1,(0,0,0))
        screen.blit(ft1_surf,[(screen.get_width()-ft1_surf.get_width())/2,160])
        
    if lin>0:
        screen.blit(font.render("                 + 6s",-1,(255,255,255)),(15,15))
    if times>=10:
        screen.blit(font.render("Time: "+str(times),-1,(255,255,255)),(15,15)) 
    else:
        if times!=0:
            if pygame.mixer.music.get_busy()==False:
                pygame.mixer.music.play() 
            if num%3==0 :
                screen.blit(font.render("Time: "+str(times),-1,(255,0,0)),(15,15)) 
    
  
    if key!=level:
        flag2=True
    if level%5==0 and flag2 and level!=0:
        lin=50
        times+=6
        flag2=not flag2
    lin=lin-1
    if hero_x<=0:
        hero_x=0
    if hero_x >=700-hero_size:
        hero_x=700-hero_size
    if hero_y<=0:
        hero_y=0
    if hero_y >=700-hero_size:
        hero_y=700-hero_size
    screen.blit(font.render("Level: "+str(level),-1,(0,0,0)),(15,620))  
    screen.blit(font.render("Score: "+str(score),-1,(0,0,0)),(15,655))
    pygame.display.update()
    