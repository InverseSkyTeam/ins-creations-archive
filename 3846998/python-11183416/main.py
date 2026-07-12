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
    if a%29 == 0 and b%29 == 0:
        a=a/29
        b=b/29
        c=c*29
        d=d/29
    if a%31 == 0 and b%31 == 0:
        a=a/31
        b=b/31
        c=c*31
        d=d/31
    if a%37 == 0 and b%37 == 0:
        a=a/37
        b=b/37
        c=c*37
        d=d/37
    if a%41 == 0 and b%41 == 0:
        a=a/41
        b=b/41
        c=c*41
        d=d/41
    if a%47 == 0 and b%47 == 0:
        a=a/47
        b=b/47
        c=c*47
        d=d/47
    if a%53 == 0 and b%53 == 0:
        a=a/53
        b=b/53
        c=c*53
        d=d/53
    if a%59 == 0 and b%59 == 0:
        a=a/59
        b=b/59
        c=c*59
        d=d/59
    if a%61 == 0 and b%61 == 0:
        a=a/61
        b=b/61
        c=c*61
        d=d/61
    if a%67 == 0 and b%67 == 0:
        a=a/67
        b=b/67
        c=c*67
        d=d/67
print("最大公因数是：",c)
print("最小公倍数是：",d)
