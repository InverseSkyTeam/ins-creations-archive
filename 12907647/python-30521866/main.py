import pygame,sys
pygame.init()
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
pygame.display.set_caption("空中站台2")

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
        show_text('欢迎来到……（键盘按任意键继续，后面都是）',color=(185,185,185))
    elif text_int == 2:
        show_text('空中站台2',color=(100,100,100))
    elif text_int == 3:
        show_text('点击右边的“退.”作品查看空中站台1')
    elif text_int == 4:
        show_text('站台停稳了！')
    elif text_int == 5:
        show_text('只在时间中的我直至时间')
    elif text_int == 6:
        show_text('只在C站中的我直至C站')
    elif text_int == 7:
        show_text('我又来了！')
    elif text_int == 8:
        show_text('我不知道上次来站台的人有没有来这里')
    elif text_int == 9:
        show_text('但是这没关系')
    elif text_int == 10:
        show_text('反对我的，请平息下来')
    elif text_int == 11:
        show_text('支持我的，也请不要激动')
    elif text_int == 12:
        show_text('屏幕面前的你，如果平静下来了，就按任意键继续吧')
    elif text_int == 13:
        show_text('其实，一大堆人支持xxx，要么是假的，要么三分钟热度')
    elif text_int == 14:
        show_text('支持yzy!')
    elif text_int == 15:
        show_text('支持syy!')
    elif text_int == 16:
        show_text('支持wdd!')
    elif text_int == 17:
        show_text('支持小轩!')
    elif text_int == 18:
        show_text('什么玩意儿啊…………')
    elif text_int == 19:
        show_text('我，第一次见到社区，2018/12')
    elif text_int == 20:
        show_text('第二次，2019/1')
    elif text_int == 21:
        show_text('2018年那阵子连个python也没有')
    elif text_int == 22:
        show_text('后来有了也不能发布')
    elif text_int == 23:
        show_text('我们都还幼稚，都还纯真，连个人主页也没有')
    elif text_int == 24:
        show_text('那是还是熊伟时代')
    elif text_int == 25:
        show_text('现在知道熊伟的，站起来！在评论区打出来！')
    elif text_int == 26:
        show_text('这样可以证明你至多2019年就来了社区！')
    elif text_int == 27:
        show_text('以前只有编程社区，没有C站。')
    elif text_int == 28:
        show_text('后来社区搞大了，变成了C站，于是就复杂了起来')
    elif text_int == 29:
        show_text('不会编程的也来编程社区了……')
    elif text_int == 30:
        show_text('一天到晚的小白、喷子、键盘侠、吃瓜群众')
    elif text_int == 31:
        show_text('大不大的谈神马***(额……)')
    elif text_int == 32:
        show_text('我告诉火焰工作室的每一个人')
    elif text_int == 33:
        show_text('新火焰工作室其实是个幌子')
    elif text_int == 34:
        show_text('本来就是要驱使你们再来重建火焰')
    elif text_int == 35:
        show_text('我只带走了几个对你们来说没用的，对我有用的')
    elif text_int == 36:
        show_text('但其实，剩下的人一点技术含量都没有')
    elif text_int == 37:
        show_text('AUSNC，蒋博文，pyj,fhh，呵呵，wdd我希望你们找些有用的人吧')
    elif text_int == 38:
        show_text('最后，我再点一些名字、工作室，是C站曾经的知名人物')
    elif text_int == 39:
        show_text('scratch先来！')
    elif text_int == 40:
        show_text('熊伟 刘东亿 吴振发')
    elif text_int == 41:
        show_text('c++！')
    elif text_int == 42:
        show_text('火泉 张子辰（张余辰仔细看看，别笑）')
    elif text_int == 43:
        show_text('最后python')
    elif text_int == 44:
        show_text('星空景然 小饼干 严子昱 刘炳毅')
    elif text_int == 45:
        show_text('说实话，刘炳毅没啥大的技术含量')
    elif text_int == 46:
        show_text('他蓝桥杯中级组，自吹自擂说想考高级组，结果初赛没有过')
    elif text_int == 47:
        show_text('王玎珰（星空景王，那时还是一个四阶魔方的头像，我没记错吧）')
    elif text_int == 48:
        show_text('你来编程社区比我晚大半年，你的技术含量不错')
    elif text_int == 49:
        show_text('但是你后来发了很多氵作，特别是没有GUI或者pygame')
    elif text_int == 50:
        show_text('但是Blaze Computer5.3还挺香，但有很多小bug')
    elif text_int == 51:
        show_text('pyj 符汉衡 编程水平都很菜，不瞒我说，承认吧')
    elif text_int == 52:
        show_text('孙伊依，短暂爆火，就别装逼了')
    elif text_int == 53:
        show_text('严子昱，真·大佬。但是因为C站太差而退站')
    elif text_int == 54:
        show_text('不知道有没有人记得他的duckchat')
    elif text_int == 55:
        show_text('现在，')
    elif text_int == 56:
        show_text('我有一句话：说别人在炫耀的人，自己连炫耀的资本都没有')
    elif text_int == 57:
        show_text('不要嫉妒别人！建议好，喷不好！没有技术含量的人才一起喷大佬！')
    elif text_int == 58:
        show_text('这咋还压上韵了…………………………………………')
    elif text_int == 59:
        show_text('真正的编程大佬，像我一样自信地说：“我会编程。”吧！')
    elif text_int == 60:
        show_text('在C站待过2年及以下的人，其中99.9%的人都是玩的')
    elif text_int == 61:
        show_text('接下来开始哲学！')
    elif text_int == 62:
        show_text('问自己的梦想是为了什么，问到不太会回答为止。')
    elif text_int == 63:
        show_text('原来你发现，实现梦想最终是为了快乐。')
    elif text_int == 64:
        show_text('好好快乐吧！')
    elif text_int == 65:
        show_text('然后，我们所做的一切都是没用，证明这个话太多了，这里不说了')
    elif text_int == 66:
        show_text('那么为什么我们要做？就是为了体验！')
    elif text_int == 67:
        show_text('所以理论上来说，任何事都=快乐，我们无论怎样，')
    elif text_int == 68:
        show_text('都会达到命运的终点。但是为了体验，不要不切实际。')
    elif text_int == 69:
        show_text('所以，看到这里，那些没有技术含量的人有什么好说的？')
    elif text_int == 70:
        show_text('我又有什么好说的？')
    elif text_int == 71:
        show_text('等等，还有一件事',color=(255,0,0))
    elif text_int == 72:
        show_text('点开改编，移到200行代码！（先别着急，看完我的话）',color=(255,0,0))
    elif text_int == 73:
        show_text('之后有问题在评论区问我',color=(255,0,0))
    else:
        print('\n\n\033[38;2;230;230;0m剩下很多来不及说，以后再说了。要说评论。\033[8m\033[?25l')
        pygame.quit()
        sys.exit()
    pygame.display.update()

























# 欢迎你的到来，请翻到500行代码







































































































































































































# 附言：
'''
请查看素材区
1.png+2.png
什么玩意儿，下面一帮自称编程牛逼的小喽啰再给王玎珰好评和赞！
程序都报错了
还好我指出
什么垃圾玩意儿？！？！？！

链接：https://code.xueersi.com/home/project/detail?lang=code&pid=30452098&version=offline&form=python&langType=python

6.png
pyj说抄袭可耻，支持，但他却自己抄袭，见
3-5.png
抄袭李官阳的，看我的评论；而且5.png有明显的版权！下面竟然还有称赞！！！

链接：https://code.xueersi.com/home/project/detail?lang=code&pid=30486896&version=offline&form=python&langType=python

火焰的团员互相自我欺骗。。。找点有用的人吧。。。还有别的事就不提了。还喷我
'''








































































#           竖着看
#TODO       | 请
#作答区域   | 翻
#TODO       | 到
#作答区域   | 第
#TODO       | 4
#作答区域   | 0
#TODO       | 0
#作答区域   | 行
#TODO       | 代
#作答区域   | 码