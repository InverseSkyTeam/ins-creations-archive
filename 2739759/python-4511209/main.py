import random
d = 0
a = int(input("\033[1;43m\033[1;31m你要发多少钱￥的红包？（点击方框后再输入（请勿输入小数））"))
print("最后一个人会领到负数红包")
old = 0
while True:
    b = input("要领红包请按回车")
    if d < a:
        c = random.randint(1,a)
        s = str(c)
        print("你共领了"+s+"￥")
        old = old+c
    if d >= a:
        c = a-old
        s = str(c)
        print("你共领了"+s+"￥")
        break
    d = old