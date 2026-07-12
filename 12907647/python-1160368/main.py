import time 
import random
def fun(line):
    for i in range(len(line)):
        print("\r"+line[0:i+1],end="")
        time.sleep(0.1)
    print()


time.sleep(1)
scale=30
print("\033[1;32m加载中",end='')
time.sleep(0.5)

print()

for i in range(scale+1):
    aaa = '='*i
    bbb = '-'*(scale-i)
    ccc =(i/scale)*100
    print("\r\033[1;32m{:^3.0f}%[{}>>{}]".format(ccc,aaa,bbb),end='')
    time.sleep(0.2)