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
p=[]


try:
    head = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
    }
    time.sleep(0.3)

    url = "https://tiyu.baidu.com/beijing2022/home/tab/%E5%A5%96%E7%89%8C%E6%A6%9C/current/paralympic"

    res = requests.get(url, headers=head)
    soup = bs4.BeautifulSoup(res.text, "lxml")


    for i in range(0,68,1):

        flag.append([])


    class_name="national-name m-c-line-clamp1"
    data = soup.find_all("div", class_=class_name)
    for i in range(len(data)):
        flag[i].append(data[i].text)




    class_name="num"
    data2=soup.find_all("div", class_=class_name)

    c=0
    i=0
    for i in range (0,len(data2),4):
        flag[i//4].append(data2[i].text)
        flag[i//4].append(data2[i+1].text)
        flag[i//4].append(data2[i+2].text)
        flag[i//4].append(data2[i+3].text)


    url2="https://results.beijing2022.cn/beijing-2022/paralympic-games/zh/results/all-sports/npc-medalist-by-sport-china.htm"

    res2 = requests.get(url2, headers=head)
    soup2 = bs4.BeautifulSoup(res2.text, "lxml")

    for i in range(0,16,1):
        p.append([])

    class_name1="d-md-none"
    class_name3="StyleCenter"
    class_name4="medal-icon"

    d3=soup2.find_all("span", class_=class_name1)
    d5=soup2.find_all("td", class_=class_name3)
    d6=soup2.find_all("img", class_=class_name4)

    for i in range(len(d3)):
        d3[i]=d3[i].text
    for i in range(len(d5)):
        d5[i]=str(d5[i].text)[1:]
    for i in range(len(d6)):
        d6[i]=d6[i]["alt"]
        if(d6[i]=='1'): d6[i]='金牌'
        if(d6[i]=='2'): d6[i]='银牌'
        if(d6[i]=='3'): d6[i]='铜牌'

    for i in range(10):
        p[i].append(d3[i])
        p[i].append(d5[i])
        p[i].append(d6[i])

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
screen = pygame.display.set_mode((1240,800),pygame.NOFRAME)
pygame.display.set_caption("|2022BEIJING|")
bg = pygame.transform.scale(pygame.image.load("bg.png"),(1240,800))
ifont1=pygame.font.Font("布丁.ttf",35)
ifont2=pygame.font.Font("布丁.ttf",22)
ifont3=pygame.font.Font("布丁.ttf",26)
ifont4=pygame.font.Font("布丁.ttf",19)
ifont5=pygame.font.Font("布丁.ttf",15)

itext1=ifont1.render(" |北京冬残奥会|实时情况",True,(100,100,100))
itext2=ifont1.render(" |BEIJING.2022| 一起向未来",True,(100,100,100))

itext6=ifont1.render("|中国荣耀|   -------------------------------------------------------------------------",True,(200,100,100))
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
        url = "https://tiyu.baidu.com/beijing2022/home/tab/%E5%A5%96%E7%89%8C%E6%A6%9C/current/paralympic"
        res = requests.get(url, headers=head)
        soup = bs4.BeautifulSoup(res.text, "lxml")

        flag=[]

        for i in range(0,68,1):
            flag.append([])

        class_name="national-name m-c-line-clamp1"
        data = soup.find_all("div", class_=class_name)
        for i in range(len(data)):
            flag[i].append(data[i].text)



        class_name="num"
        data2=soup.find_all("div", class_=class_name)

        c=0
        i=0
        for i in range (0,len(data2),4):

            flag[i//4].append(data2[i].text)
            flag[i//4].append(data2[i+1].text)
            flag[i//4].append(data2[i+2].text)
            flag[i//4].append(data2[i+3].text)

        if bbb%100 == 0:
            print(time.strftime("%Y.%m.%d %H:%M:%S"))
            print('--------------------------------------------')
            for i in range(len(flag)):
                if(flag[i]!=[]):
                    for j in range(len(flag[i])):
                        print(flag[i][j],end=" ")

                    #print("\n")
            bbb=0
            print('--------------------------------------------')

        p=[]

        url2="https://results.beijing2022.cn/beijing-2022/paralympic-games/zh/results/all-sports/npc-medalist-by-sport-china.htm"

        res2 = requests.get(url2, headers=head)
        soup2 = bs4.BeautifulSoup(res2.text, "lxml")

        for i in range(0,16,1):
            p.append([])

        class_name1="d-md-none"
        class_name3="StyleCenter"
        class_name4="medal-icon"

        d3=soup2.find_all("span", class_=class_name1)
        d5=soup2.find_all("td", class_=class_name3)
        d6=soup2.find_all("img", class_=class_name4)

        for i in range(len(d3)):
            d3[i]=d3[i].text
        for i in range(len(d5)):
            d5[i]=str(d5[i].text)[1:]
        for i in range(len(d6)):
            d6[i]=d6[i]["alt"]
            if(d6[i]=='1'): d6[i]='金牌'
            if(d6[i]=='2'): d6[i]='银牌'
            if(d6[i]=='3'): d6[i]='铜牌'

        for i in range(10):
            p[i].append(d3[i])
            p[i].append(d5[i])
            p[i].append(d6[i])

    except:
        t=1
        print(t)








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
    screen.blit(itext6,(45,540))
    itext4=ifont3.render("刷新时间："+time.strftime("%Y.%m.%d %H:%M:%S"),True,(120,170,120))
    screen.blit(itext4,(775,90))
    screen.blit(itext4,(775,500))
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
            itext3=ifont4.render(str(numof)+" "+flag[i][0]+"  |金牌："+flag[i][1]+"  |银牌："+flag[i][2]+"  |铜牌："+flag[i][3]+"  |共计："+flag[i][4],True,(100,100,100))
            if(flag[i][0]=='中国'):
                itext3=ifont4.render(str(numof)+" "+flag[i][0]+"  |金牌："+flag[i][1]+"  |银牌："+flag[i][2]+"  |铜牌："+flag[i][3]+"  |共计："+flag[i][4],True,(210,105,30))
            if(i==0):
                itext3=ifont4.render(str(numof)+" "+flag[i][0]+"  |金牌："+flag[i][1]+"  |银牌："+flag[i][2]+"  |铜牌："+flag[i][3]+"  |共计："+flag[i][4],True,(255,100,100))
            if(i==1):
                itext3=ifont4.render(str(numof)+" "+flag[i][0]+"  |金牌："+flag[i][1]+"  |银牌："+flag[i][2]+"  |铜牌："+flag[i][3]+"  |共计："+flag[i][4],True,(255,165,50))
            if(i==2):
                itext3=ifont4.render(str(numof)+" "+flag[i][0]+"  |金牌："+flag[i][1]+"  |银牌："+flag[i][2]+"  |铜牌："+flag[i][3]+"  |共计："+flag[i][4],True,(255,250,205))
            numof+=1


            x+=600
            screen.blit(itext3,(x,140+i//2*40))
    for i in range(len(p)):
        if(i%2==0):
            x=50-600
        if p[i]!=[]:
            itext3=ifont4.render("|姓名："+p[i][0]+"|项目："+p[i][1]+" |奖牌："+p[i][2],True,(180,120,120))
            x+=600
            screen.blit(itext3,(x,600+i//2*40))
    pygame.display.update()