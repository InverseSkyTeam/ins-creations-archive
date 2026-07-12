import pygame,sys,time
import requests
import bs4,random
import webbrowser

pygame.init()
screen = pygame.display.set_mode((1050,500))
pygame.display.set_caption("作品大全")


def downloadimage(url,name):
    
    head = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
    }
    res = requests.get(url, headers=head)
    with open(name+".png","wb") as file:
        file.write(res.content)
        



allz={"|竹|＆青云智能机器人" : "https://livefile.xesimg.com/programme/assets/f1dc0c5b39def97b852b1bf3e6b6f99d.jpg" , 
"yzx＆本草纲目-字符化IMAGE库" : "https://livefile.xesimg.com/programme/assets/d9cdc95843865a8e990f3dd79d1ad138.jpg" , 
"回忆录" : "https://livefile.xesimg.com/programme/assets/de2221d985a80e57be385897c2ca506b.jpg" , 
"IdealXes项目XesAnalysis" : "https://livefile.xesimg.com/programme/assets/67412cd9e2abc1614b38dde31e807ef1.jpg" ,
"|YZX|离奇消失的作品" : "https://livefile.xesimg.com/programme/assets/ba96db2e4bba8aef24bd33235ee77e07.jpg" ,
"竹のPython排序算法可视化" : "https://livefile.xesimg.com/programme/assets/fd69605e74cf7568321b1afce72ff9e2.jpg" ,
"博客评论设置成功！" : "https://livefile.xesimg.com/programme/assets/dfc3fd072d1a47c03a9fd4d912425fbe.jpg" , "Github的API" : "https://livefile.xesimg.com/programme/assets/7ab9f695a22d9a6d18ee5a60897e3818.jpg" , "Python实现栈&队列" : "https://livefile.xesimg.com/programme/assets/9d8edc0eb28f1781098a165a188f9cb5.jpg" , "竹の|文字游戏|" : "https://livefile.xesimg.com/programme/assets/946a560ce48c8b61c322fdec8eab96e6.jpg" , "API-获取你作品的一切" : "https://livefile.xesimg.com/programme/assets/2653bb272bafcec08f5b51c50548a2da.jpg" , "BEIJING.奖牌榜|2冬0奥2会2|.爬虫" : "https://livefile.xesimg.com/programme/assets/2a147ff39401beeea834bf3767d54489.jpg" , "竹＆像素化头像(正方形)}2.0" : "https://livefile.xesimg.com/programme/assets/fe768a1da96040a99663bbd5f96d33a6.jpg" , "毕业季" : "https://livefile.xesimg.com/programme/assets/280160ca82c8bd8fc8f994c0d5a60a28.jpg" , "竹＆手速 - 鼠标双击" : "https://livefile.xesimg.com/programme/assets/b29959da2d69f4d27d5c95078b158299.jpg" , "竹＆红包冲突Version2.1" : "https://livefile.xesimg.com/programme/assets/dbd4e5a03c072e3281f8670cf756c807.jpg" , "竹の招人了" : "https://livefile.xesimg.com/programme/assets/d21c3611b2e7b7f0484b51476a777615.jpg" , "Hexo部署博客" : "https://livefile.xesimg.com/programme/assets/30dfddb343be767f5fde339684b57b11.jpg" , "IdealXes项目CloudCodeRun" : "https://livefile.xesimg.com/programme/assets/2444881a1d1ec318461ffa1acd032fde.jpg" , " |BEIJING冬残奥|.奖牌和获奖人爬取" : "https://livefile.xesimg.com/programme/assets/02e792e9d3ea53af63dad3fe19907112.jpg" , "yzx{Random Music}" : "https://livefile.xesimg.com/programme/assets/7e67bb02cb2e97ed5232ad5bfb7c43f8.jpg" , "竹の作业之下UnderThe Homework" : "https://livefile.xesimg.com/programme/assets/3eb9fcd1edcf0695735d67206e4719d9.jpg" , "竹＆手速 - 鼠标单击" : "https://livefile.xesimg.com/programme/assets/923b48243c712264168c491da5f92d70.jpg" , " 竹＆色彩1.01游戏" : "https://livefile.xesimg.com/programme/assets/382cb08ce3ce99f5498a3af7a2264afb.jpg" , "Sprite精灵实现Pygame精细碰撞" : "https://livefile.xesimg.com/programme/assets/35d36490b3bf7e910919f9d820d99fc3.jpg" , "Hexo部署博客的我的答疑解难在评论区" : "https://livefile.xesimg.com/programme/assets/5c2f4c8f6e4448c383f3e13948142140.jpg" , "|竹|招聘の启示" : "https://livefile.xesimg.com/programme/assets/bf5f38a3d43f0c286e549e245cfefb42.jpg" , "＆竹|字符化VIDEO库发布-本草纲目" : "https://livefile.xesimg.com/programme/assets/e9ea9917341661b9bfc5e7ee0fcce666.jpg" , "春节.|新春恐龙|" : "https://livefile.xesimg.com/programme/assets/483bc754a29a7a076d26ae1c0d1734b5.jpg" , "ABOUT-MYSELF |yzx个人网页|" : "https://livefile.xesimg.com/programme/assets/2819a59e508e01fb75dcd6c18105a43f.jpg" 
    
}

allc={"|竹|＆青云智能机器人" : "https://code.xueersi.com/home/project/detail?lang=code&pid=34039541&version=offline&form=python&langType=python" , 
"yzx＆本草纲目-字符化IMAGE库" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33535660&version=offline&form=python&langType=python" , "竹の作品集" : "https://code.xueersi.com/home/project/detail?lang=code&pid=36718523&version=offline&form=python&langType=python" , "Github的API" : "https://code.xueersi.com/home/project/detail?lang=code&pid=34116795&version=offline&form=python&langType=python" , "回忆录" : "https://code.xueersi.com/home/project/detail?lang=code&pid=36525263&version=offline&form=python&langType=python" , "IdealXes项目XesAnalysis" : "https://code.xueersi.com/home/project/detail?lang=code&pid=34685995&version=offline&form=python&langType=python" , "|YZX|离奇消失的作品" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33348919&version=offline&form=python&langType=python" , "竹のPython排序算法可视化" : "https://code.xueersi.com/home/project/detail?lang=code&pid=36692842&version=offline&form=python&langType=python" , "博客评论设置成功！" : "https://code.xueersi.com/home/project/detail?lang=code&pid=36681897&version=offline&form=python&langType=python" , "Python实现栈&队列" : "https://code.xueersi.com/home/project/detail?lang=code&pid=36547953&version=offline&form=python&langType=python" , "竹の|文字游戏|" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33542406&version=offline&form=python&langType=python" , "BEIJING.奖牌榜|2冬0奥2会2|.爬虫" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33530058&version=offline&form=python&langType=python" , "竹＆像素化头像(正方形)}2.0" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33361139&version=offline&form=python&langType=python" , "毕业季" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33360904&version=offline&form=python&langType=python" , "竹＆手速 -鼠标双击" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33360713&version=offline&form=python&langType=python" , "竹＆手速 - 鼠标单击" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33360422&version=offline&form=python&langType=python" , "竹＆红包冲突Version2.1" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33349309&version=offline&form=python&langType=python" , "竹の招人了" : "https://code.xueersi.com/home/project/detail?lang=code&pid=36711511&version=offline&form=python&langType=python" , "Sprite精灵实现Pygame精细碰撞" : "https://code.xueersi.com/home/project/detail?lang=code&pid=36709123&version=offline&form=python&langType=python" , "Hexo部署博客" : "https://code.xueersi.com/home/project/detail?lang=code&pid=36642597&version=offline&form=python&langType=python" , "API-获取你作品的一切" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33537858&version=offline&form=python&langType=python" , " |BEIJING冬残奥|.奖牌和获奖人爬取" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33530219&version=offline&form=python&langType=python" , "yzxの|迷-宫|" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33399150&version=offline&form=python&langType=python" , "yzx{Random Music}" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33398998&version=offline&form=python&langType=python" , " 竹＆色彩1.01游戏" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33360230&version=offline&form=python&langType=python" , "IdealXes项目CloudCodeRun" : "https://code.xueersi.com/home/project/detail?lang=code&pid=34968069&version=offline&form=python&langType=python" , "春节.|新春恐龙|" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33526119&version=offline&form=python&langType=python" , "ABOUT-MYSELF |yzx个人网页|" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33523535&version=offline&form=python&langType=python" , 
"yzxの|千-万-别-动|" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33399052&version=offline&form=python&langType=python" , 
"竹の作业之下UnderThe Homework" : "https://code.xueersi.com/home/project/detail?lang=code&pid=33360989&version=offline&form=python&langType=python" 
}





class Kuai:
    def __init__(self,name,x,y,file,url):
        self.x=x
        self.do=0
        self.y=y
        self.url=url
        self.font=pygame.font.Font("HYTiaoTiaoTiJ.ttf",19)
        self.text=self.font.render(name,True,(50,50,50))
        self.rect=pygame.Rect(x,y,150,90)
        self.image=pygame.transform.scale(pygame.image.load(file),(150,90))
    def show(self,screen):
        temp=self.y
        self.y=self.y+self.do
        self.rect=pygame.Rect(self.x,self.y,150,90)
        screen.blit(self.image,self.rect)
        screen.blit(self.text,(self.x,self.y+100))
        self.rect=pygame.Rect(self.x,self.y-self.do,150,90)
        self.y=temp
        if event.type==pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pygame.mouse.get_pos()):
            webbrowser.open(self.url)
klist=[]
filename=[]
xx,yy,count=50,80,0

screen.fill((255,255,255))

afont=pygame.font.Font("HYTiaoTiaoTiJ.ttf",39)
atext=afont.render("正在加载图片，这可能需要20秒",True,(50,50,50))

atext2=afont.render("我的作品集，上下箭头进行滚动,单击即可跳转",True,(50,50,50))
#screen.blit(atext,(200,100))

pygame.display.update()


for cup in allz.keys():
    if count%3==0 and count!=0:
        xx=50
        yy+=150
    elif count!=0:
        xx+=350
    count+=1
    # downloadimage(allz[cup],cup.replace('＆','o').replace('|','a'))
    try:
        klist.append(Kuai(cup,xx,yy,cup.replace('＆','o').replace('|','a')+".png",allc[cup]))
    except:
        klist.append(Kuai(cup,xx,yy,cup.replace('＆','o').replace('|','a')+".png",allz[cup]))


screen.fill((255,255,255))

scroll=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            scroll=scroll+2
        if event.key == pygame.K_DOWN:
            scroll=scroll-2
    screen.fill((255,255,255))
    screen.blit(atext2,(250,20+scroll))
    for i in klist:
        i.do=scroll
        i.show(screen)
    pygame.display.update()
    time.sleep(0.001)
    pygame.display.update()