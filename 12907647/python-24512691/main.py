from sys import *
from os import *

print('Windows CMD\n小轩版 1.1\n\n功能新增：dc=回到上一级目录 dc_first回到原目录 dc_all 回至C盘\n')
user_home = path.expanduser('~')

while True:
    print(user_home,end='')
    text = input('>')
    
    try:
        if text[0] == 'c' and text[1] == 'd':
            user_home += '\\'+text[3::]
    except:
        print('cmd1.1-error:x2 - 字符数<1 - x1-1 to\nfile error x2-1cmd\n修复完毕')
    if text == 'exit' or text == 'quit':
        exit()
    if text == 'dc':
        user_home = '\\'.join(user_home.split('\\')[0:-1])
    if text == 'dc_first':
        user_home = path.expanduser('~')
    if text == 'dc_all':
        user_home = 'C:'
    if user_home == '':
        user_home = 'C:'
        print('cmd1.1-error:无法断开C盘')
    
    text = popen(text)
    print(text.read().replace('CMD.EXE','小轩python-cmd'))