num=0
a=int(input("你想要几以内的质数？"))
for i in range(2,a+1):
    is_prime=True
    for j in range(2,i+1):
        if i%j==0 and i/j>1:
            is_prime=False
    if is_prime:
        print(i)
        num=num+1
print(a,"以内共有",num,"个质数")