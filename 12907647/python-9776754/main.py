import pygame,sys,random,tkinter as tk,webbrowser as web

print('1.此为参赛作品，我是‘宇宙工作室’的室长小轩')
print('2.参赛-2020欢度国庆')
print('3.我酷狗无法下载我和我的祖国歌曲，被我直接爬来啦，酷狗音乐版权所有，图片也爬到的')
print('4.若出现一个黑色的窗口，关掉它有惊喜')
input('能做到的敲回车进入pygame')
import spaceSign

pygame.init()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("参赛-2020欢度国庆")
bg = pygame.transform.smoothscale(pygame.image.load("天安门.jpg"),(1000,800))
pygame.mixer.music.load('我和我的祖国.mp3')  # BGM
pygame.mixer.music.play(-1)
part = 1

try:import ntpath             # 检测系统
except:osingxing = 'MacOs';font = pygame.font.SysFont('kaittf', 40)
else:osingxing = 'Windows';font = pygame.font.SysFont('kaiti', 40);del ntpath

a = font.render('国',True,(10,20,255))
b = font.render('接我',True,(10,255,10))
c = font.render('别接',True,(255,21,25))
coins = 0
POS = [0,0]
bDict = {}
for i in range(30):
    bx = random.randint(0,760)
    by = random.randint(-1600,-40)
    r = pygame.Rect(bx, by, 80, 40)
    bDict[i] = [b, bx, by, r]
cDict = {}
for i in range(15):
    cx = random.randint(0,760)
    cy = random.randint(-1600,-40)
    r = pygame.Rect(cx, cy, 80, 40)
    cDict[i] = [c, cx, cy, r]

while True:
    while part == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                POS = event.pos
                try:
                    for i in bDict:
                        if bDict[i][3].collidepoint(POS):
                            del bDict[i]
                            coins += 1
                except:
                    pass
                try:
                    for x in cDict:
                        if cDict[x][3].collidepoint(POS):
                            cDict = {}
                            bDict = {}
                except:
                    pass
        pygame.mouse.set_visible(False)
        screen.blit(bg,(0,0))
        screen.blit(a,POS)
        try:
            for i in bDict:
                screen.blit(bDict[i][0],(bDict[i][1],bDict[i][2]))
                bDict[i][2] += 1
                bDict[i][3] = pygame.Rect(bDict[i][1], bDict[i][2], 80, 40)
                if bDict[i][2] >= 760:
                    del bDict[i]
        except:
            pass
        try:
            for x in cDict:
                screen.blit(cDict[x][0],(cDict[x][1],cDict[x][2]))
                cDict[x][2] += 1
                cDict[x][3] = pygame.Rect(cDict[x][1], cDict[x][2], 80, 40)
                if cDict[x][2] >= 760:
                    del cDict[x]
        except:
            pass
        if bDict == {}:
            part = 2
        pygame.display.update()
    
    while part == 2:
        def help1():
            label1['text'] = '''
            　　中国在经历了鸦片战争，
            　　甲午中日战争等丧权辱国的事件后，
            　　唤醒了一部分的人，
            　　他们思考为何中华民族会从泱泱大国转变为了受尽欺凌的国家，
            　　他们为中华民族的复兴尽着努力，
            　　有失败有挫折有着无法想像的磨难，
            　　这期间经历的艰辛是我们这一代人所不能体会到的，
            　　八国联军的侵华，日本的侵略，
            　　都是在考验着我们国人的意志，
            　　在这期间我们的共产党诞生，
            　　他们带领着国人在抗争的道路上前进，
            　　在抗日战争胜利后，中国共产党为争取和平民主做出了很大努力，
            　　但是国民党政府在美帝国主义支持下悍然发动内战。
            　　中国共产党领导人民进行了三年多的解放战争，
            　　这中间有我们耳熟能详的红军长征，
            　　中国共产党领导中国人民经过北伐战争、
            　　土地革命战争、抗日战争和全国解放战争四个阶段，
            　　终于在1948年推翻了以蒋介石为首的国民党政府在中国大陆的统治，
            　　取得了新民主主义革命的胜利。
            　　在1949年第一届中国人民政协会的召开，
            　　表明了中国人民民主革命的伟大胜利。
            　　1949年10月1日，在毛主席的宣告中中华人民共和国成立，
            　　这一天被认为是新中国的崛起发展的标志日子，
            　　是中华民族人们翻身当家作主的好日子，
            　　于是在中央人民政府的一致同意下，
            　　在毛主席的赞同中由全国政协提议的
            　　《关于中华人民共和国国庆日的决议》被通过，
            　　每一年的10月1日就确定为中华民族的国庆节。
            　　今年中秋节与国庆节同一天！
            　　对于中华民族而言，
            　　国庆节的习俗免不了的就是阅兵仪式，
            　　自从1949年毛主席宣布新中国成立，并有兵队的展示后，
            　　往后的阅兵仪式就成了国庆佳节的必备节目，也就成了一种习俗。
            　　由于国庆节是中国人民的法定假日，无论是小孩，大人还是老年人，
            　　这一天都是属于休息状态，很多家庭会选择在国庆节除外旅游或逛街，
            　　而在这节日很多商场亦会打出折扣等优惠活动，这个节日里，
            　　你能感受到的就是一片喜庆祥和的气氛。
            　　最后，祝大家国庆快乐！
            　　'''
        def help2():
            web.open('https://code.xueersi.com/home/project/detail?lang=code&pid=9785648&version=webpy&form=python&langType=python')
        root = tk.Tk()
        root.geometry('800x600')
        button1 = tk.Button(root,text='了解国庆节（请全屏查看）',bg='yellow',command=help1)
        button2 = tk.Button(root,text='了解了，下一个部分',bg='orange',command=help2)
        label1 = tk.Label(root,text='点击了解国庆节展开（祝大家国庆快乐！）',bg='yellow',font=('楷体',15))
        button1.pack()
        button2.pack()
        label1.place(x=0,y=60)
        root.mainloop()