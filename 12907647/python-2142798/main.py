import os
from time import *
from random import *
from xes.ext import *
def clear():
    os.system('export TERM=xterm && clear') 
def fun(line):
    for i in range(len(line)):
        print("\r"+line[0:i+1],end="")
        sleep(0.1)
    print()
print('病毒生成中')
sleep(2)
scale=30
print("\033[1;32m加载中",end='')
sleep(0.05)
print()
for i in range(scale+1):
    aaal = '\033[1;31m=\033[1;32m'*i
    bbbl = '-'*(scale-i)
    cccl =(i/scale)*100
    print("\r\033[1;32m{:^3.0f}%[{}>>{}]".format(cccl,aaal,bbbl),end='')
    sleep(0.05)
clear()
def jushi():
    sleep(1)
print('\033[33m\033[2;2m☠ ☠ ☠ ☠ ☠\033[2;0m')
jushi()
clear()
print('\033[33m☠ ☠ ☠ ☠ ☠\033[2;0m')
jushi()
clear()
print('\033[1;33m☠ ☠ ☠ ☠ ☠')
jushi()
clear()
chess_list = ['0 ','1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9',' 10',' 11','12',' 13',' 14',' 15']
def printChess():
    n = len(chess_list)
    for i in range(n):
        print(chess_list[i],end = '')
        if (i+1) % 4 == 0:
            print('\n')
print('<重力四子棋>')
printChess()
for i in range(16):
    if i % 2 == 0:
        num = int(input('A请输入:'))
        chess_list[num] = 'A '
    else:
        num = int(input('B请输入：'))
        chess_list[num] = 'B '
    clear()
    printChess()
    def win(n1,n2,n3,n4):
        if (chess_list[n1] == chess_list[n2] and chess_list[n1] == chess_list[n3] and chess_list[n1] == chess_list[n4] and chess_list[n2] == chess_list[n3] and chess_list[n2] == chess_list[n4] and chess_list[n3] == chess_list[n4] and chess_list[n4] == 'A'):
            return 'y'
        else:
            return 'n'
        
    if (win(0,1,2,3) == 'y' or win(4,5,6,7) == 'y' or win(8,9,10,11) == 'y' or win(12,13,14,15) == 'y'):
        fun('A获胜')
        break
    elif (win(0,4,8,12) == 'y' or win(1,5,9,13) == 'y' or win(2,6,10,14) == 'y' or win(3,7,11,15) == 'y'):
        fun('A获胜')
        break
    elif (win(0,5,10,15) == 'y' or win(4,6,9,12) == 'y' ):
        fun('A获胜')
        break
        
        
        
    def bbb(h1,h2,h3,h4):
        if (chess_list[h1] == chess_list[h2] and chess_list[h1] == chess_list[h3] and chess_list[h1] == chess_list[h4] and chess_list[h2] == chess_list[h3] and chess_list[h2] == chess_list[h4] and chess_list[h3] == chess_list[h4] and chess_list[h4] == 'B'):
            return 'v'
        else:
            return 'll'
        
    if (bbb(0,1,2,3) == 'v' or bbb(4,5,6,7) == 'v' or bbb(8,9,10,11) == 'v' or bbb(12,13,14,15) == 'v'):
        fun('B获胜')
        break
    elif (bbb(0,4,8,12) == 'v' or bbb(1,5,9,13) == 'v' or bbb(2,6,10,14) == 'v' or bbb(3,7,11,15) == 'v'):
        fun('B获胜')
        break
    elif (bbb(0,5,10,15) == 'v' or bbb(4,6,9,12) == 'v' ):
        fun('B获胜')
        break

            













