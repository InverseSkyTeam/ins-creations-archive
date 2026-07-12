def prime(a):
    if a==1 or a==0:
        return(False)
    for i in range(2,a):
        if a%i==0 and a/i!=1:
            return(False)
    return(True)
print(prime(int(input("请输入要判断是不是质数的数："))))