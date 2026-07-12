from random import *
from time import *
def fun(line):
    for i in range(len(line)):
        print("\r"+line[0:i+1],end="")
        sleep(0.1)
    print()
fun("\033[1;33m请按随机1~10下回车……\033[1;34m我也不知道——是随机。")
ran = randint(1,10)
for x in range(ran):
    input("")
fun("解密中……")
sleep(1.5)
ha = input("解密密码：")
if ha != "":
    print("快离开！☠")
else:
    ma = input("")
    if ma != " ":
        print("快离开！☠")
    else:
        da = input("")
        if da != "       ":
            print("快离开！☠")
        else:
            fun("\033[1;36m欢迎！")
            score = 0
            fun("***********挑战速算，获得积分***********")
            print("\033[1;31m一题一分(+)，答错清零！\033[1;0m")
            ji_fen = input("加=1 1题1分/减=2 1题2分/乘=3 1题5分")
            if ji_fen == "1":
                num = int(input("你想挑战的题目数量是："))
                fun("3秒后开始")
                sleep(5-2)
                for i in range(num):
                    n1 = randint(1,1000)
                    n2 = randint(1,1000)
                    g = n1+n2
                    print("第",i+1,"道题为：\n",n1,'+',n2,'=')
                    c = int(input('你的答案为：'))
                    if g == c:
                        print("\033[1;32m√")
                        score += 1
                    else:
                        print("\033[1;31m×")
                        score = 0
            if ji_fen == "2":
                num = int(input("你想挑战的题目数量是："))
                fun("3秒后开始")
                sleep(5-2)
                for i in range(num):
                    n1 = randint(1,1000)
                    n2 = randint(1,1000)
                    g = n1-n2
                    print("第",i+1,"道题为：\n",n1,'-',n2,'=')
                    c = int(input('你的答案为：'))
                    if g == c:
                        print("\033[1;32m√")
                        score += 2
                    else:
                        print("\033[1;31m×")
                        score = 0
            if ji_fen == "3":
                num = int(input("你想挑战的题目数量是："))
                fun("3秒后开始")
                sleep(5-2)
                for i in range(num):
                    n1 = randint(1,100)
                    n2 = randint(1,1000)
                    g = n1*n2
                    print("第",i+1,"道题为：\n",n1,'*',n2,'=')
                    c = int(input('你的答案为：'))
                    if g == c:
                        print("\033[1;32m√")
                        score += 5
                    else:
                        print("\033[1;31m×")
                        score = 0
            print("你的积分数^")
            print("\n       ***积分商城***  ")
            print("手枪：5个积分，\n船模：10个积分,\n飞机：20个积分")
            print("你的积分数是：……")
            if score >= 5:
                print("可换：1手枪")
            elif score >= 10:
                print("可换：1手枪/2船模")
            elif score >= 20:
                print("可换：1手枪/2船模/3飞机")
            else:
                print("积分不足!")
                
            
            y = int(input("输序号，拿奖品！"))
            #换奖品！！！
            if y == "1":
                if score >= 5:
                    print("手枪到！")
                    score = score - 5
                else:
                    print("不足")
            elif y == "2":
                if score >= 10:
                    print("船模到！")
                    score = score - 10
                else:
                    print("不足")
            elif y == "3":
                if score >= 20:
                    print("飞机到！")
                    score = score - 20
                else:
                    print("不足")
            else:
                print("不足！")
        print("\033[1;3m\033[1;4m\033[1;2m好了，还剩",score,"分！")
                        
                

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        