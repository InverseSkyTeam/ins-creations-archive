import sys
from time import *
def clear():
    print('\033[2J\033[100A')
    print('\033[3J\033[100A')
def 黄(times=1,e='open'):
    if e == 'open':
        print('\033[1;43m \033[0m'*times,end='')
    elif e == 'close':
        print('\033[1;43m \033[0m'*times)
    else:
        print('渲染文字错误：参数只能是"open"或"close"，来决定文尾是否空行(Render_font Error:The parameter can only be "open" or "close" to determine whether the trailer is empty or not)')
        if input('输入y继续，其他终止程序') == 'y':
            pass
        else:
            sys.exit()
def 红(times=1,e='open'):
    if e == 'open':
        print('\033[1;41m \033[0m'*times,end='')
    elif e == 'close':
        print('\033[1;41m \033[0m'*times)
    else:
        print('渲染文字错误：参数只能是"open"或"close"，来决定文尾是否空行(Render_font Error:The parameter can only be "open" or "close" to determine whether the trailer is empty or not)')
        if input('输入y继续，其他终止程序') == 'y':
            pass
        else:
            sys.exit()
def 绿(times=1,e='open'):
    if e == 'open':
        print('\033[1;42m \033[0m'*times,end='')
    elif e == 'close':
        print('\033[1;42m \033[0m'*times)
    else:
        print('渲染文字错误：参数只能是"open"或"close"，来决定文尾是否空行(Render_font Error:The parameter can only be "open" or "close" to determine whether the trailer is empty or not)')
        if input('输入y继续，其他终止程序') == 'y':
            pass
        else:
            sys.exit()
def logo1():
    黄(times=64,e='close')
    for i in range(8):
        黄(times=2);绿(times=2);绿(times=2);黄(times=2)
    print(end='\n')
    for i in range(8):
        黄(times=2);绿(times=2);绿(times=2);黄(times=2)
    print(end='\n')
    黄(times=64,e='close')
    print('''\033[7m宇宙工作室忒棒    此为logo    室长小轩    满站宇宙    6666666666\033[1;41m
    +——————————————————————————————————————————————————————————+
    |    Space$$$$$             A                  CCCCCCCC    |
    |    $                     A A              CCC            |
    |    $                    A   A          CCC               |
    |    office$$$$          AAAAAAA         CCC               |
    |             $         A       A        CCC               |
    |             $        A         A          CCC            |
    |    $$$$$$$$$$       A           A            CCCCCCCC    |
    +——————————————————————————————————————————————————————————+
\033[0m''',end='')
    黄(times=64,e='close')
    for i in range(8):
        黄(times=2);绿(times=2);绿(times=2);黄(times=2)
    print(end='\n')
    for i in range(8):
        黄(times=2);绿(times=2);绿(times=2);黄(times=2)
    print(end='\n')
    黄(times=64,e='close')
def logo2():
    黄(times=64,e='close')
    for i in range(8):
        黄(times=2);绿(times=2);绿(times=2);黄(times=2)
    print(end='\n')
    for i in range(8):
        黄(times=2);绿(times=2);绿(times=2);黄(times=2)
    print(end='\n')
    黄(times=64,e='close')
    print('''\033[7m宇宙工作室忒棒    此为logo    室长小轩    满站宇宙    6666666666\033[1;31m
    +——————————————————————————————————————————————————————————+
    |    Space$$$$$             A                  CCCCCCCC    |
    |    $                     A A              CCC            |
    |    $                    A   A          CCC               |
    |    office$$$$          AAAAAAA         CCC               |
    |             $         A       A        CCC               |
    |             $        A         A          CCC            |
    |    $$$$$$$$$$       A           A            CCCCCCCC    |
    +——————————————————————————————————————————————————————————+
\033[0m''',end='')
    黄(times=64,e='close')
    for i in range(8):
        黄(times=2);绿(times=2);绿(times=2);黄(times=2)
    print(end='\n')
    for i in range(8):
        黄(times=2);绿(times=2);绿(times=2);黄(times=2)
    print(end='\n')
    黄(times=64,e='close')
def logo():
    clear()
    logo1()
    sleep(0.2)
    clear()
    logo2()
    sleep(0.2)