import sys
sys.setrecursionlimit(150000)

a = []
for i in range(20000):
    new = []
    new.append(a[:])
    a = new[:]
print(len(str(a))//2)