import random
a = random.randint(1,50)
num = 0
while True:
    b = input("请猜一个1-50之间的整数")
    num = num + 1
    b = int(b)
    if b > a:
        print("猜大了")
    elif b < a:
        print("猜小了")
    else:
        print("猜对了")
        break
print("猜测次数：",num)