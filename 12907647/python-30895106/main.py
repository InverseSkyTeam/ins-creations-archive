##小轩输出法
from time import *
import jieba
import sys

def all_replace(newtext,*reword):
    for group in reword:
        newtext = newtext.replace(group[0],group[1])
    return newtext

def pt(*text,time=None,end='\n',interval=' ',carry_color=True,is_input=False,move={'left':0,'right':0,'up':0,'down':0},word_interval='无间隔'):
    text_all = ""
    
    for group in range(len(text)):
        if group == len(text) - 1:
            text_all += str(text[group])
        else:
            text_all += str(text[group]) + interval
    if word_interval == '智能分词':
        text_all = ' '.join(jieba.lcut(text_all))
    
    if carry_color == False:
        text_all += '#act复原'
    
    if type(move['left']) != int or type(move['right']) != int or type(move['up']) != int or type(move['down']) != int:
        raise TypeError("\033[1;31m这个字典参数{}的所有键值必须是整数类型！如{'left':0,'right':14,'up':2,'down':0}\033[0m")
    if move['left'] != 0:
        text_all += '\033['+str(move['left'])+'D'
    if move['right'] != 0:
        text_all += '\033['+str(move['right'])+'C'
    if move['up'] != 0:
        text_all += '\033['+str(move['up'])+'A'
    if move['down'] != 0:
        text_all += '\033['+str(move['down'])+'B'
    
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
    ("#sact隐藏光标","\033[?25l"),
    ("#sact显示光标","\033[?25h"),
    ("#sact换行","\n"),
    ("#sact缩进","    "),
    ("#sact大缩进","\t"),
    ("#sact右下一格","\v"),
    ("#rgbcolor:","\033[38;2;"),
    ("#rgbbgcolor:","\033[48;2;"),
    ("#scolor橙","\033[38;2;230;130;0m"),
    ("#bgscolor橙","\033[48;2;230;130;0m"),
    ("#scolor粉","\033[38;2;230;130;150m"),
    ("#bgscolor粉","\033[48;2;230;130;150m"),
    ("#sscolor代码运行结束色","\033[38;2;230;230;0m"),
    ("#bgsscolor代码运行结束色","\033[48;2;230;230;0m"),
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
    if is_input == True:
        input('')
    else:
        sys.stdout.write(end)

pt('''
最近，小轩做(作)了(死)一个实验
想看看自家电脑(win10顶配)物理内存卡爆会怎么样！！！
/doge
于是，小轩作死打开了python游戏编辑器
输入了以下代码:
回车继续：
''')
input()
pt('#act清屏')
pt('''import webbrowser as w
while True:
    w.open('https://baidu.com')

(见·图1)
然后，还傻逼式地点击了运行！！！
''',time=0.1)
input('各位猜猜后果，并且回车')
pt('#act清屏')
pt('''
然后呢，开始疯狂地跳出网页，CPU快速达到100%，温度上升到近40摄氏度！！！
内存明显还是上升（54%）
(见·图2)
(真·作死)

紧接着，内存开始爆满了
(见·图3)

后来，内存到了96%（电脑性能也忒好了吧），开始向磁盘存储
很快，C:盘爆减12GB（内存才8GB）
最后C:盘只剩128MB了，我以为要完蛋了，但仍旧想看看是怎么废了的
结果了，磁盘存储不放了，又回到内存上
内存爆到97%!!!!!!!!!!!!!!!!!!!!!!!!!!!!
勉强打开了任务管理器，发现垃圾360安全卫士用的CPU比1600多个网页还多！！！！！
所以奉劝大家别用垃圾360了！！！！！！！！！！！！！！！！！！！
(见·图4)

最后内存惨惨——98%!!!!!!!!
然后显示屏便加载不出来了！！！！
直接黑屏！！！(类似于bat里面0%|0%的后果!)
每黑6秒左右就有一次正常，显示了1秒又黑掉了
(关键时刻保持镇定，一定要等死！！！/doge)
突然，叮咚一声，弹出一个关键错误（还是显示win7的图标）
没看清楚就又黑了，然后我记得上面写着：
“Google无法正常显示网页,请查看内存状况”
笑死，还要查看状况？
那个时候连截图都截不了，所以没图…………
过了十几秒，竟然开始不断弹出错误弹窗
真好玩，真的和中病毒一样了！！！(不知道当时屏幕前的那位傻逼是怎么想的)
然后C盘和内存全部刷满，一直弹窗，结果悲剧了！！！
蓝瓶钙！！！蓝屏了！！！wc！！！
正当100%错误收集完毕时，没有重启，重新又回到弹窗和黑屏的界面！
然后换来换去！！！
最后，我无奈地按下(Ctrl+Alt+DEL)
结果在那个界面都一直弹窗
我好不容易按下Ctrl同时点击右下角电源，然后紧急重启
电脑就挂了
回车继续
''',time=0.01,is_input = True)
pt('''#act清屏
重启后，竟然好了，内存和磁盘都恢复了，没丢文件，再起打开Google时……
别笑喷，别笑喷，啊！
噗————————————————
不是你想的那样，听我说啊！
噗————————————————————
自己也笑了…………
(见·图5)
谷歌推荐重新打开那1600多个网页！！！！！！
噗——————————————————————————————————————————————————

这期糗事就分享到这里！！！
下次分享小轩使用win2000虚拟机怎么删掉系统的糗事！！！
（图1-5都在素材区，点改编观看！）
''')