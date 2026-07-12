import pygame,sys,random,time,requests,bs4,random
'''
核心部分:
    1.歌曲网址列表
    2.封装随机函数
    3.封装寻找函数
    4.封装下载函数
'''
mlist=["蜂鸟","起风了","纪念","See you again","半生雪","好好学习","年少有为","Dream it possble","Lemon tree","踏山河","黎明前的黑暗","稻香","像你这样的朋友",
  "成都","星河","我从崖边跌落","你的答案","明天你好","森林狂想曲","不说再见","Counting stars","Something just like this","雾里","平凡之路","无名之辈","The nights","七月上",
  "少年中国说","骁","说书人","走马","分手快乐","Remember our summer","曹操"]

urllist=[
    "https://livefile.xesimg.com/programme/python_assets/0329cd2e3b6ccdf9a4182b41636bfab5.mp3",
    "https://livefile.xesimg.com/programme/python_assets/f078e89ff0919ec893fe542e9bedbbdf.mp3",
    "https://livefile.xesimg.com/programme/python_assets/1f10162b6d0622ccc8571be387d80ae7.mp3",
    "https://livefile.xesimg.com/programme/python_assets/a309ecb47f1fbd63736588ef50f81af2.mp3",
    "https://livefile.xesimg.com/programme/python_assets/9d7aa7f2719c5beb999064e11da89156.mp3",
    "https://livefile.xesimg.com/programme/python_assets/6e271152f054985ac916091837174d04.mp3",
    "https://livefile.xesimg.com/programme/python_assets/74a36f21fb591a3c093b40e9bbd1b58e.mp3",
    "https://livefile.xesimg.com/programme/python_assets/cb2d96eff08958c294c8003f023d9ecb.mp3",
    "https://livefile.xesimg.com/programme/python_assets/7c8c42da9a7fcd0e377a9f016faf5732.mp3",
    "https://livefile.xesimg.com/programme/python_assets/da47602351f7f71aea8c1e88de587411.mp3",
    "https://livefile.xesimg.com/programme/python_assets/568df931385e5d2dfd9ed9d71a51feb6.mp3",
    "https://livefile.xesimg.com/programme/python_assets/8d7f5fccdbf3a8ee3c8ec5b613a969bc.mp3",
    "https://livefile.xesimg.com/programme/python_assets/de44942ee488f051b7e2c74161fa6116.mp3",
    "https://livefile.xesimg.com/programme/python_assets/5af571f454b5e60a050725ffb8c7edf0.mp3",
    "https://livefile.xesimg.com/programme/python_assets/272ca5c0244b68096c79182b66f55dce.mp3",
    "https://livefile.xesimg.com/programme/python_assets/66be2501de4dac88a17faa2e787a9bc0.mp3",
    "https://livefile.xesimg.com/programme/python_assets/c413a59407100320b8f9da233b35f938.mp3",
    "https://livefile.xesimg.com/programme/python_assets/691d7aa4845e767ee0e43112bbaa6b5b.mp3",
    "https://livefile.xesimg.com/programme/python_assets/2ad55bfeed073787138ff194d55e6f21.mp3",
    "https://livefile.xesimg.com/programme/python_assets/d799c2b30379c17257a973878cf37a5b.mp3",
    "https://livefile.xesimg.com/programme/python_assets/c413bde7403e0dfefb3855dadb531188.mp3",
    "https://livefile.xesimg.com/programme/python_assets/e58d3babaa101a57876c4b59945dd274.mp3",
    "https://livefile.xesimg.com/programme/python_assets/e836f25320d1b9756d80ef4147516117.mp3",
    "https://livefile.xesimg.com/programme/python_assets/c7a27a32748c3de971587119838a78a1.mp3",
    "https://livefile.xesimg.com/programme/python_assets/be283811795b87e04c13d0b3712c1953.mp3",
    "https://livefile.xesimg.com/programme/python_assets/97911a392d3adab53053bfedc2d3251e.mp3",
    "https://livefile.xesimg.com/programme/python_assets/dd9fd710bf78b291bc63861a335588f6.mp3",
    "https://livefile.xesimg.com/programme/python_assets/8d77363c5cda55073da6c1f8f1ea5fb9.mp3",
    "https://livefile.xesimg.com/programme/python_assets/59cb9943ec54097255b9534f0aeae64c.mp3",
    "https://livefile.xesimg.com/programme/python_assets/63304dff35f103b4252ace7c348a4ffa.mp3",
    "https://livefile.xesimg.com/programme/python_assets/f404a9b1ab64b9a75765fcd74af778e5.mp3",
    "https://livefile.xesimg.com/programme/python_assets/209a414137eebf4444004a3c74e40fb9.mp3",
    "https://livefile.xesimg.com/programme/python_assets/9585b095fe7ace0ddf0b56e1e0306428.mp3",
    "https://livefile.xesimg.com/programme/python_assets/31dbb8ef2bffa556d44aa24306e0ce1f.mp3"
        ]

def suiji():
    a=random.randint(0,33)
    return(mlist[a])
def suiurl(str):
    return mlist.index(str)
def payin(url):
    head = {
        "Referer": "https://icourse.xesimg.com",
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11",
    }
    response = requests.get(url, headers= head )

    a=chr(random.randint(97,122))
    b=chr(random.randint(97,122))
    c=chr(random.randint(97,122))
    d=chr(random.randint(97,122))
    e=chr(random.randint(97,122))
    f=chr(random.randint(97,122))
    file_name="yzx{music__"+a+b+c+d+e+f+"__}.mp3"
    with open(file_name,"wb") as file:
        file.write(response.content)
    return file_name
'''
GUI部分:
'''
dqq=''
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("The Random Music")
main_rect1=pygame.Rect(140,185,420,90)
main_rect2=pygame.Rect(140,310,420,90)
mf=pygame.font.Font("font.ttf",30)
it=pygame.font.Font("font.ttf",25)
title_mf=pygame.font.Font("font.ttf",35)
title_mt=title_mf.render("随Ran机dom Mus音ic乐",True,(50,50,50))
mt=title_mf.render(suiji(),True,(50,50,50))
m0=it.render("空格以切换曲目:",True,(50,50,50))
m1=mf.render("当前曲目:",True,(50,50,50))
m2=mf.render(dqq,True,(50,50,50))
m3=mf.render("随机列表:",True,(50,50,50))
t1=time.time()
count=0
m=0
dangqian=''
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN :
            if  m==1:
                m=0
    t2=time.time()

    if  round(t2-t1)==2 :
        m=0
    if(count%100==0 and m==0):
        dangqian=suiji()

    mt=title_mf.render(dangqian,True,(50,50,50))
    m2=title_mf.render(dqq,True,(50,50,50))

    if event.type==pygame.KEYDOWN:
        if  m==0 :
            m=1
            dqq=dangqian
            pygame.mixer.music.load(payin(urllist[suiurl(dangqian)]))
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(1)
            t1=time.time()
            count=0


    screen.fill((165,215,255))
    pygame.draw.rect(screen,(60,210,210),main_rect1,0)
    pygame.draw.rect(screen,(60,210,210),main_rect2,0)
    screen.blit(mt,(160,340))
    screen.blit(m1,(160,180))
    screen.blit(m2,(160,220))
    screen.blit(m3,(160,310))
    screen.blit(title_mt,(150,60))
    screen.blit(m0,(250,110))
    count+=1
    if count>=100:
        count=0
    pygame.display.update()
