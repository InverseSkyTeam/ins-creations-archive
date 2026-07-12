import sys
sys.setrecursionlimit(3000)

# 不会报错
all = 99
string = 'def a1():'
for i in range(2,all+1):
    string += '\n'+'    '*(i-1)+'def a'+str(i)+'():'
string += '\n'+'    '*all+'b=666'
exec(string)

# 才100层就逝世了
all = 100
string = 'def a1():'
for i in range(2,all+1):
    string += '\n'+'    '*(i-1)+'def a'+str(i)+'():'
string += '\n'+'    '*all+'b=666'
exec(string)