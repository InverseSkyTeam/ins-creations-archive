#26 27行
from time import *
from random import *
from os import *
from xes.ext import *
def clear():
    system('export TERM=xterm && clear')
speak('你好')
print('我叫国庆机器人')
print('大家可以叫我小庆！')
sleep(2.5)
clear()
print('第一环节：好运滚滚来 ☺')
print('难度系数：☆')
sleep(2)
print('准备红包雨！')
sleep(3)
clear()
for guoguoguoguoguo in range(8):
    print('\033[1;41m             ')
print('\033[1;0m准备：')
sleep(0.0625)
sleep(0.125)
sleep(0.25)
sleep(0.5)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>2019
sleep(0.0000000000000000000010000002019)
t1 = time()
input('回车开抢！')
t2 = time()
timeZongHe = t2 - t1
if timeZongHe <= 1:
    print('1000000!')
elif timeZongHe > 1 and timeZongHe <= 1.5:
    print('10000!')
elif timeZongHe > 1.5 and timeZongHe <= 2:
    print('100!')
elif timeZongHe > 2 and timeZongHe <= 3:
    print('10!')
elif timeZongHe > 3:
    print('手慢无!')
sleep(2)
print('红包结束~')
sleep(1)
clear()
print('第二阶段：字字字字')
print('视屏无难度！')
sleep(1)
clear()
print('\033[1;32m _____\033[1;0m    \033[1;32m_____')
print('\033[1;32m     /\033[1;0m    \033[1;32m|   |')
print('\033[1;32m    / \033[1;0m    \033[1;32m|   |')
print('\033[1;32m   /  \033[1;0m    \033[1;32m|   |')
print('\033[1;32m  /   \033[1;0m    \033[1;32m ———')
sleep(2)
clear()
print('第三阶段：题题题题题题题题题！')
print('难度系数：☆☆☆☆☆☾☾☾☾☾※※※※※◇○▽△♬☀☼☽☾☺☹')
sleep(2)
clear()
a = int(input('阅兵仪式第二个方队是：海:1/陆:2/空:3'))
if a != 1:
    print('海1是对的，你是错的')
else:
    print('对')
b = input('中华人民共和国是什么时候成立的？（注：格式：年-月-日 例：1997-5-28）')
if b == '1949-10-1':
    print('OK!')
else:
    print('是1949-10-1！')
sleep(2)
print('我爱祖国！')







