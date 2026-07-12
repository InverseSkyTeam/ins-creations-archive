a=''
while True:
    b=input()
    if b=="programingend" or b=="end":
        break
    a=a+'\n'+b
try:
    exec(a)
except:
    print("您的代码有问题！")