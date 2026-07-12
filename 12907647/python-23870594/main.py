from time import *
import sys

def all_replace(newtext,*reword):
    for group in reword:
        newtext = newtext.replace(group[0],group[1])
    return newtext

def pt(*text,time=0.05,end='\n',interval=' ',carry_color=True):
    text_all = ""
    
    for group in range(len(text)):
        if group == len(text) - 1:
            text_all += str(text[group])
        else:
            text_all += str(text[group]) + interval
    
    if carry_color == False:
        text_all += '#act复原'
    
    text_all = all_replace(text_all,
    ("#act清屏","\033[2J\033[00H\033[100A\033[2J\033[100A\033[3J"),
    ("#act复原","\033[0m"),
    ("#act斜体","\033[4m"),
    ("#act关闭斜体","\033[24m"),
    ("#act下划线","\033[4m"),
    ("#act关闭下划线","\033[24m"),
    ("#act反色","\033[7m"),
    ("#act关闭反色","\033[27m"),
    ("#act隐藏","\033[8m"),
    ("#act显示","\033[28m"),
    ("#rgbcolor:","\033[38;2;"),
    ("#rgbbgcolor:","\033[48;2;"),
    ("#scolor橙","\033[38;2;230;130;0m"),
    ("#bgscolor橙","\033[48;2;230;130;0m"),
    ("#scolor粉","\033[38;2;230;130;150m"),
    ("#bgscolor粉","\033[48;2;230;130;150m"),
    ("#color暗","\033[30m"),
    ("#color红","\033[31m"),
    ("#color绿","\033[32m"),
    ("#color黄","\033[33m"),
    ("#color蓝","\033[34m"),
    ("#color紫","\033[35m"),
    ("#color青","\033[36m"),
    ("#color银","\033[37m"),
    ("#color2暗","\033[1;30m"),
    ("#color2红", "\033[1;31m"),
    ("#color2绿", "\033[1;32m"),
    ("#color2黄", "\033[1;33m"),
    ("#color2蓝", "\033[1;34m"),
    ("#color2紫", "\033[1;35m"),
    ("#color2青", "\033[1;36m"),
    ("#color2银", "\033[1;37m"),
    ("#color3暗","\033[2;30m"),
    ("#color3红", "\033[2;31m"),
    ("#color3绿", "\033[2;32m"),
    ("#color3黄", "\033[2;33m"),
    ("#color3蓝", "\033[2;34m"),
    ("#color3紫", "\033[2;35m"),
    ("#color3青", "\033[2;36m"),
    ("#color3银", "\033[2;37m"),
    ("#bgcolor暗","\033[40m"),
    ("#bgcolor红","\033[41m"),
    ("#bgcolor绿","\033[42m"),
    ("#bgcolor黄","\033[43m"),
    ("#bgcolor蓝","\033[44m"),
    ("#bgcolor紫","\033[45m"),
    ("#bgcolor青","\033[46m"),
    ("#bgcolor银","\033[47m"),
    ("#bgcolor2暗","\033[1;40m"),
    ("#bgcolor2红", "\033[1;41m"),
    ("#bgcolor2绿", "\033[1;42m"),
    ("#bgcolor2黄", "\033[1;43m"),
    ("#bgcolor2蓝", "\033[1;44m"),
    ("#bgcolor2紫", "\033[1;45m"),
    ("#bgcolor2青", "\033[1;46m"),
    ("#bgcolor2银", "\033[1;47m"),
    ("#bgcolor3暗","\033[2;40m"),
    ("#bgcolor3红", "\033[2;41m"),
    ("#bgcolor3绿", "\033[2;42m"),
    ("#bgcolor3黄", "\033[2;43m"),
    ("#bgcolor3蓝", "\033[2;44m"),
    ("#bgcolor3紫", "\033[2;45m"),
    ("#bgcolor3青", "\033[2;46m"),
    ("#bgcolor3银", "\033[2;47m"))
    
    if time == None:
        sys.stdout.write(text_all)
        sys.stdout.flush()
    else:
        for one_letter in text_all:
            sys.stdout.write(one_letter)
            sys.stdout.flush()
            sleep(time)
    sys.stdout.write(end)

pt('小轩有史以来最大作')
pt('              预计1.5~3.2k行代码')
pt('python')
pt('              pygame')
pt('html')
pt('              爬虫')
pt('人工智能')
pt('              三方库')
pt('tk')
pt('              os')
pt('小A机器人——震撼来袭！\n（有人：来个怼啊，现在才更新到0.5k行代码）')
pt('预告完——就怪了')
pt('#scolor橙这个作品会有很多彩蛋，等待玩家发掘')
pt('这个作品不是一下就能玩完的（甚至要爆肝/doge），所以有存档点')
pt('         有多种玩法')
pt('憨憨',carry_color=False)
pt('什……什么？你问我我是怎么输出橙色字体的？')
pt('那是我写的pt函数，现在才0.3(这个作品用的2.0)版，我会到时候发的，不要急')
pt('已经突破yzy的print.(doge，但是真的)')
pt('8 8 6...',time=0.5)