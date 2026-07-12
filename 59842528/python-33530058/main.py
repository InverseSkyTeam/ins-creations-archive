import requests
import bs4
import time
import pygame,sys



def fr_la(a1,a2,a3,b1,b2,b3):
    if a1>b1:
        return '>'
    elif a1==b1:
        if a2>b2:
            return '>'
        elif a2==b2:
            if(a3>b3):
                return '>'
            elif a3==b3:
                return '='
    return '<'



flag=[]



try:
    head = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
    }
    time.sleep(0.3)

    url = "https://tiyu.baidu.com/beijing2022/home/tab/%E5%A5%96%E7%89%8C%E6%A6%9C/from/pc"

    res = requests.get(url, headers=head)
    soup = bs4.BeautifulSoup(res.text, "lxml")


    c=0

    for i in range(0,68,1):

        flag.append([])

    c=0

    for m in range(0,68):
        class_name="national-name m-c-line-clamp"+str(m)
        data = soup.find_all("div", class_=class_name)
        if data!=[]:
            for n in data:
                flag[c].append(data[c].text)
                c+=1
    c=0

    for m in range(0,4):
        class_name="medal-list-item m-c-gap-inner-top m-c-gap-inner-bottom medal-rank-"+str(m)
        data2 = soup.find_all("div", class_=class_name)
        class_name="num"
        for n in data2:
            data3 = n.find_all("div", class_=class_name)
            if data3!=[]:
                for n in data3:
                    flag[c].append(n.text)
                c+=1
    for m in range(4,68):
        class_name="medal-list-item m-c-gap-inner-top m-c-gap-inner-bottom m-c-line-bottom medal-rank-"+str(m)

        data2 = soup.find_all("div", class_=class_name)

        class_name="num"
        for n in data2:
            data3 = n.find_all("div", class_=class_name)
            if data3!=[]:
                for n in data3:#正确
                    flag[c].append(n.text)
                c+=1
except:
    print("由于百度该网站的停止开放\n我将用这网站关闭前的数据作为呈现\n")
    for i in range(0,68,1):
        flag.append([])
    n=0
    with open("冬奥奖牌榜.txt", "r", encoding="UTF-8") as file:
        for line in file.readlines():
            line = line.strip('\n')
            #去掉列表中每一个元素的换行符
            lista=line.split()
            flag[n]=lista
            n+=1

pygame.init()
screen = pygame.display.set_mode((1240,725),pygame.NOFRAME)
pygame.display.set_caption("|2022BEIJING|")
bg = pygame.transform.scale(pygame.image.load("bg.png"),(1240,725))
ifont1=pygame.font.Font("布丁.ttf",35)
ifont2=pygame.font.Font("布丁.ttf",22)
ifont3=pygame.font.Font("布丁.ttf",26)

itext1=ifont1.render(" |北京冬奥会|实时情况",True,(100,100,100))
itext2=ifont1.render(" |BEIJING.2022| 一起向未来",True,(100,100,100))

itext3=ifont2.render("",True,(100,100,100))
itext4=ifont1.render(time.strftime("%Y.%m.%d %H:%M:%S"),True,(100,100,100))

numof=1

pygame.mixer.music.load("准备好一起向未来.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.15)
win=pygame.mixer.Sound("wow.flac")
temp=[]
#win.play()
bbb=99
yinl=0.15
x=50-600

try:
    with open("冬奥奖牌榜.txt", "w", encoding="UTF-8") as file:
        for i in range(len(flag)):
            if(flag[i]!=[]):
                for j in range(len(flag[i])):
                    file.write(str(flag[i][j] )+"  ")
                file.write("\n")
except:
    print("由于百度该网站的停止开放\n我将用这网站关闭前的数据作为呈现\n")


while True:
    bbb+=1
    pygame.mixer.music.set_volume(yinl)
    try:
        url = "https://tiyu.baidu.com/beijing2022/home/tab/%E5%A5%96%E7%89%8C%E6%A6%9C/from/pc"
        res = requests.get(url, headers=head)
        soup = bs4.BeautifulSoup(res.text, "lxml")

        c=0

        for m in range(0,68):
            class_name="national-name m-c-line-clamp"+str(m)
            data = soup.find_all("div", class_=class_name)
            if data!=[]:

                for n in data:
                    flag[c][0]=data[c].text
                    c+=1

        c=0

        for m in range(0,4):
            class_name="medal-list-item m-c-gap-inner-top m-c-gap-inner-bottom medal-rank-"+str(m)
            data2 = soup.find_all("div", class_=class_name)
            class_name="num"
            for n in data2:
                data3 = n.find_all("div", class_=class_name)
                if data3!=[]:
                    d=1
                    for n in data3:
                        flag[c][d]=n.text
                        d+=1
                    d=1

                    c+=1

        for m in range(4,68):
            class_name="medal-list-item m-c-gap-inner-top m-c-gap-inner-bottom m-c-line-bottom medal-rank-"+str(m)

            data2 = soup.find_all("div", class_=class_name)

            class_name="num"
            for n in data2:
                data3 = n.find_all("div", class_=class_name)
                if data3!=[]:
                    d=1
                    for n in data3:

                        flag[c][d]=n.text
                        d+=1

                    c+=1

        if bbb%100==0:
            print(time.strftime("%Y.%m.%d %H:%M:%S"))
            print('--------------------------------------------')
            for i in range(len(flag)):
                if(flag[i]!=[]):
                    for j in range(len(flag[i])):
                        print(flag[i][j],end=" ")

                    #print("\n")
            bbb=0
            print('--------------------------------------------')
    except:
        t=1






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_DOWN:
                if yinl<=100:
                    yinl-=0.05
            if event.key == pygame.K_UP:
                if yinl>=0:
                    yinl+=0.05


    screen.fill((255,255,255))
    screen.blit(bg,(0,0))
    screen.blit(itext1,(25,40))
    screen.blit(itext2,(25,85))
    itext4=ifont3.render("刷新时间："+time.strftime("%Y.%m.%d %H:%M:%S"),True,(120,170,120))
    screen.blit(itext4,(800,100))
    x=50-600

    for i in range(0,68):
        if(i%2==0):
            x=50-600
        if i==67:
            numof=1
        if flag[i]!=[] and len(flag[i]) >4:
            if i>0 :
                if fr_la(flag[i][1],flag[i][2],flag[i][3],flag[i-1][1],flag[i-1][2],flag[i-1][3])=='=':
                    numof-=1
                else:
                    numof=i+1
            itext3=ifont2.render(str(numof)+" "+flag[i][0]+"  |金牌："+flag[i][1]+"  |银牌："+flag[i][2]+"  |铜牌："+flag[i][3]+"  |共计："+flag[i][4],True,(100,100,100))
            if(flag[i][0]=='中国'):
                itext3=ifont2.render(str(numof)+" "+flag[i][0]+"  |金牌："+flag[i][1]+"  |银牌："+flag[i][2]+"  |铜牌："+flag[i][3]+"  |共计："+flag[i][4],True,(210,105,30))
            if(i==0):
                itext3=ifont2.render(str(numof)+" "+flag[i][0]+"  |金牌："+flag[i][1]+"  |银牌："+flag[i][2]+"  |铜牌："+flag[i][3]+"  |共计："+flag[i][4],True,(255,100,100))
            if(i==1):
                itext3=ifont2.render(str(numof)+" "+flag[i][0]+"  |金牌："+flag[i][1]+"  |银牌："+flag[i][2]+"  |铜牌："+flag[i][3]+"  |共计："+flag[i][4],True,(255,165,50))
            if(i==2):
                itext3=ifont2.render(str(numof)+" "+flag[i][0]+"  |金牌："+flag[i][1]+"  |银牌："+flag[i][2]+"  |铜牌："+flag[i][3]+"  |共计："+flag[i][4],True,(255,250,205))
            numof+=1


            x+=600
            screen.blit(itext3,(x,150+i//2*40))

    pygame.display.update()