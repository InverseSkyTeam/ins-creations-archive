print('点进源码')
print(Ellipsis)
print(...)
print(str(...))
print(...,...)
print({...})
def a():
    ...
print(a,...)
n = [1,2,3]
n.append(n)
print(n)
print(n[3])
print(n[3][3])
print(n[3][3][3][3][3][3][3][3][3][3][3][3][3][3])
print(n[3][3][3][3][3][3][3][3][3][3][3][3][3][2])
n.remove(1)
n.remove(2)
n.remove(3)
print(n[0][0])
print([[...]][0][0])
n = [n[0][0] for i in range(10)]
print(n)
print(n[3]+n[1]+n[4]+n[1]+n[5]+n[9]+n[2]+n[6])
print(n[0][1][2][5][0][1][8][9][6][4][3][7][8][8][5][6][0][3][1][0])
print(n[:][0:][:-2][0])
n[-1] = ...
n[...] = ...
print(n)
print(1)
print(666)
print('坏掉了')