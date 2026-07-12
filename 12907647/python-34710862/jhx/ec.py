from time import *
import jieba
import sys
name = 'easy code - python to jhx /-V0.1.1'

def all_replace(newtext,*reword):
    for group in reword:
        newtext = newtext.replace(group[0],group[1])
    return newtext

def pt(*text,time=None,end='\n',interval=' ',carry_color=True,is_input=False,move={'left':0,'right':0,'up':0,'down':0},word_interval='无间隔'):
    '''
pt函数更新日志：
start        开始写代码，搭建环境，删除img1.png
0.1          达到yzy(https://code.xueersi.com编程社区曾经的大佬)
             的成效，颜色代码数超过yzy，代码可读性提升，
             把all_replace单独打包并避免和关键字重名
0.2          修复rgb，增加功能参数carry_color，把“黑”改为“暗”，
             “白”改为“银”，添加#act行动类颜色代码
0.3          更新ss级别代码运行结束色,增加参数move等光标类属性
0.4          增加了is_input
0.5          增加了如何隐藏光标、显示光标，s级别颜色和属性，换
             行（水），优化整体，修复参数，做了这个好玩的更新
             日志，更新sys写入。增加move的判断和报错。
0.6          修复光标类属性，多增加一些转义符。
0.7          添加参数智能分词，默认值无间隔，可以调控是否用空格
             来间隔每个词组。如选智能分词，任何颜色代码无效！
0.8          更新使用
0.8X         转入jhx.ec库
0.9          待更~
    '''
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

def clear():
    print('\033[2J\033[00H\033[100A\033[2J\033[100A\033[3J'+'\033[2J\033[100A\033[3J\033[100A'*8+'\033c\033[2J'*11)

def rgb10to16(r=64,g=64,b=64,plus=True):
    r = str(hex(r))[2:]
    if len(r) == 1:r = '0'+r
    g = str(hex(g))[2:]
    if len(g) == 1:r = '0'+r
    b = str(hex(b))[2:]
    if len(b) == 1:r = '0'+r
    value = r+g+b
    if plus:
        return '#'+value
    return value

def get_kil(k,l):
    '''get key in two-dimensional-list'''
    for i in range(len(l)):
        try:
            return str(i)+','+str(l[i].index(k))
        except:
            pass
    return 'Not found'

def hl_to_ll(l,times):
    '''high list to low list(^_^降维打击)'''
    times = int(times)
    if times == 2:
        return [j for i in l for j in i]
    else:
        return hl_to_ll([[j] if type(j) == int else j for i in l for j in i],times-1)

hl_to_ll_example1 = hl_to_ll([[0,1,[[3,4],[2,7,3,[[4,1],[6]],8]]],[2,3,[1,[2,5],3]]],3)
hl_to_ll_example2 = hl_to_ll([[0,1,[[3,4],[2,7,3,[[4,[6,[8,[['ha'],['s',['l','INS jhx']],11]]]],[6]],8]]],[2,3,[1,[2,5],3]]],11)

# 打乱列表
def upset(l):
    s = []
    while l != []:
        x = random.choice(l)
        l.remove(x)
        s.append(x)
    return s