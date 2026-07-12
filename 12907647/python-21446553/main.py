from time import *;from random import *;from data import *
def ptc(text,time):print(text);sleep(time);print('\033[100A\033[2J\033[100A\033[3J')
for i in range(1,101):ptc('加载main.py file text {} %...'.format(i),0.03 if i!=99 else 0.6)
for i in range(1,101):ptc('加载python解释器 {} %...'.format(i),0.01 if i!=48 else 0.9)
for i in range(1,101):ptc('加载IMPORTANT-LOAD file {} %...'.format(i),choice([uniform(0.01,0.1) for p in range(20)]+[0.4,0.6]))
for i in range(1,61):ptc('玩命加载中 '+str(i%7*'.'),0.08)
for i in range(1,10):print('loading...');ptc('\033[1;41m  \033[1;42m  \033[1;43m  \n\033[1;44m  \033[1;49m  \033[1;46m  \n\033[1;47m  \033[1;45m  \033[2;47m  \033[0m',0.2);print('loading...');ptc('\033[1;45m  \033[1;43m  \033[1;41m  \n\033[1;42m  \033[1;47m  \033[1;44m  \n\033[1;46m  \033[2;47m  \033[49m  \033[0m',0.2)
run_data_info(ptc)