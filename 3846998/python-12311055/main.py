a=int(input("目标高度:"))
b=int(input("爬树速度:"))
c=int(input("掉落速度:"))
d=0
e=0
while True:
    d=d+b
    e=e+1
    if d >= a :
        print("需要爬",e,"天")
        break
    d=d-c
    if d >= a :
        print("需要爬",e,"天")
        break