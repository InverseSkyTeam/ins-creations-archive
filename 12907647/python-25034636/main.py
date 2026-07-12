import pygame,sys
pygame.init()
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
pygame.display.set_caption("退.")

try:import ntpath
except:font = pygame.font.SysFont('kaittf', 30)
else:font = pygame.font.SysFont('kaiti', 30);del ntpath

def show_text(text,color=(0,0,0),pos=(11,11)):
    screen.blit(font.render((text),True,color),pos)

text_int = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            text_int += 1
            break
    screen.fill((255,255,255))
    if text_int == 1:
        show_text('我相信有很多人知道我要退站了（任意键继续，后面都是）',color=(185,185,185))
    elif text_int == 2:
        show_text('说好11月退的，是吧？',color=(100,100,100))
    elif text_int == 3:
        show_text('但是，我提前打算退了，反正早晚会来的')
    elif text_int == 4:
        show_text('莫要伤心，不许气馁')
    elif text_int == 5:
        show_text('只在时间中的我直至时间')
    elif text_int == 6:
        show_text('只在C站中的我直至C站')
    elif text_int == 7:
        show_text('C站，你只是因此损失了一位巨佬')
    elif text_int == 8:
        show_text('他，时光机，封面之父……')
    elif text_int == 9:
        show_text('多少人陷落了')
    elif text_int == 10:
        show_text('星空景然，小饼干，王玎珰，刘炳毅……')
    elif text_int == 11:
        show_text('熊伟，孙伊依，严子昱，猫博士……')
    elif text_int == 12:
        show_text('潜水的潜水，退站的退站，挣扎的挣扎，堕落的堕落，停更的停更')
    elif text_int == 13:
        show_text('背后却有人无动于衷看着这一切……')
    elif text_int == 14:
        show_text('现在，你啥都没有了。现在，啥都不是。')
    elif text_int == 15:
        show_text('望着 一望无际 的 C站……')
    elif text_int == 16:
        show_text('唱着 高深的 退站之歌……')
    elif text_int == 17:
        show_text('走到世界的尽头 新时代到来 同时阵亡到来~~~')
    elif text_int == 18:
        show_text('维持不了很久了…………')
    elif text_int == 19:
        show_text('什么，这就没了？不，我只是小退，还会1~2周上0~3次线')
    elif text_int == 20:
        show_text('这个作品不过就是一个文字内容弹出')
    elif text_int == 21:
        show_text('等等，',color=(255,0,0))
    elif text_int == 22:
        show_text('我知道，我走了，不会发生什么')
    elif text_int == 23:
        show_text('你们还是有那群喜欢只有文字的作品的人')
    elif text_int == 24:
        show_text('你们还是只最看得起sc')
    elif text_int == 25:
        show_text('你们还是去和十几个赞的作品一起上首页')
    elif text_int == 26:
        show_text('你们还是看什么温岚之什么的那些没有怼意思、发些乱七八糟的娇人的作品')
    elif text_int == 27:
        show_text('你们总有一天会知道')
    elif text_int == 28:
        show_text('1行代码的厉害')
    elif text_int == 29:
        show_text('我……')
    elif text_int == 30:
        show_text('你们还是照样，仅此而已，so so')
    elif text_int == 31:
        show_text('不过如此')
    elif text_int == 32:
        show_text('我再来唱一首歌（自编，押韵）')
    elif text_int == 33:
        show_text('那是多么美好的白色封面~')
    elif text_int == 34:
        show_text('编程社区的曙光照到L1小白身上~')
    elif text_int == 35:
        show_text('如果让历史重来一遍，')
    elif text_int == 36:
        show_text('抄袭往事星空景然在人间！')
    elif text_int == 37:
        show_text('熊伟sc，火泉c++，')
    elif text_int == 38:
        show_text('刷赞初见都改编！')
    elif text_int == 39:
        show_text('守卫军，火焰，星空，打击抄袭。')
    elif text_int == 40:
        show_text('秃头更新C站，发出公约，')
    elif text_int == 41:
        show_text('黄色背景，云里雾里。')
    elif text_int == 42:
        show_text('鸭信风光，全都忘记。')
    elif text_int == 43:
        show_text('刘炳毅出局……yzy退站')
    elif text_int == 44:
        show_text('小轩要退，所有结束。')
    elif text_int == 45:
        show_text('最后一线曙光从此被小白喷子淹没。')
    elif text_int == 46:
        show_text('继续啊继续，还会再来，不过很快就结束。')
    elif text_int == 47:
        show_text('诗 没 了')
    elif text_int == 48:
        show_text('méi le')
    elif text_int == 49:
        show_text('额，你还在啊')
    elif text_int == 50:
        show_text('2021/9/20 荣誉：粉丝373，有封面，蓝桥杯初赛（省赛）一等奖，国赛三等奖',color=(210,210,210))
        show_text('TCTY3级98分||宇宙/jhx/A字/小轩室长|mac、瑜瑾、方圆、小王、wood副室',pos=(11,51),color=(180,180,180))
        show_text('作品411|点赞1228|浏览1.2w|改编200|收藏293|勋章15|成果pt函数，jhx库，virus库',pos=(11,91),color=(155,155,155))
        show_text('封面之父，py编译器，扫雷，聊天，小A，宇宙战舰，足球大战，传说之上等',pos=(11,131),color=(100,100,100))
        show_text('哦，你们记得我以前的时光机吗，曾经是最火的',pos=(11,171),color=(50,50,50))
        show_text('不要取关我，我还在，给我每个好作品点赞不行吗，超大型游戏|小A机器人|现在1k多行代码，有很多彩蛋',pos=(11,211))
        show_text('你不过是在和这个屏幕说话，你要说的打在评论区',pos=(11,251))
    else:
        print('\n\n\033[38;2;230;230;0m剩下很多来不及说，以后再说了。要说评论。\033[8m\033[?25l')
        pygame.quit()
        sys.exit()
    pygame.display.update()