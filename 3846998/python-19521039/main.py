a=int(input('第一个数:'))
b=int(input('第二个数:'))
c=a*b
d=1
for i in range(2,a*b):
    while 1:
        if a%i==0 and b%i==0:
            d=d*i
            c=c/i
            a=a/i
            b=b/i
        else:
            break
print('最小公倍数是',c,'最大公因数是',d)