a=int(input("数1："))
b=int(input("数2："))
c=1
d=a*b
for i in range(a*b+1):
    if a%2 == 0 and b%2 == 0:
        a=a/2
        b=b/2
        c=c*2
        d=d/2
    if a%3 == 0 and b%3 == 0:
        a=a/3
        b=b/3
        c=c*3
        d=d/3
    if a%5 == 0 and b%5 == 0:
        a=a/5
        b=b/5
        c=c*5
        d=d/5
    if a%7 == 0 and b%7 == 0:
        a=a/7
        b=b/7
        c=c*7
        d=d/7
    if a%11 == 0 and b%11 == 0:
        a=a/11
        b=b/11
        c=c*11
        d=d/11
    if a%13 == 0 and b%13 == 0:
        a=a/13
        b=b/13
        c=c*13
        d=d/13
    if a%17 == 0 and b%17 == 0:
        a=a/17
        b=b/17
        c=c*17
        d=d/17
    if a%19 == 0 and b%19 == 0:
        a=a/19
        b=b/19
        c=c*19
        d=d/19
    if a%23 == 0 and b%23 == 0:
        a=a/23
        b=b/23
        c=c*23
        d=d/23
print("最大公因数是：",c)
print("最小公倍数是：",d)
