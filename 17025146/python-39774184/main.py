import sys  
sys.setrecursionlimit(2000)

def a(n):
    print(n)
    a(n + 1)
a(0)