# 4.0
import time
print('前10000以内大约用0.6秒输出，前50000以内大约用17.5秒输出')
Number = int(input('版本：4.0\n输入一个数，判定在这个数以内的质数'))
print('\n\n\n\033[1;36m2',end=' ')
for i in range(3,Number,2):
    for j in range(3,i):
        if i % j == 0:break
    else:print(i,end=' ')