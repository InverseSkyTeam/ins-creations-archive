import time 
import random
def fun(line):
    for i in range(len(line)):
        print("\r"+line[0:i+1],end="")
        time.sleep(0.1)
    print()
fun("\033[1;32m《##找神秘动物！》已下载完成，\033[1;34m好了！\033[1;35m")

time.sleep(1)
scale=30
print("\033[1;33m正在加载中！！！",end='')
time.sleep(0.5)

print()

for i in range(scale+1):
    aaa = '='*i
    bbb = '-'*(scale-i)
    ccc =(i/scale)*100
    print("\r\033[1;32m{:^3.0f}%[{}>>{}]".format(ccc,aaa,bbb),end='')
    time.sleep(0.3)
animals = {
    "熊猫":["4","陆地","食肉和草","易危"],
    "鸡":["2","陆地","食肉和草","无危"],
    "老虎":["4","陆地","食肉","濒危"],
    "蛇":["0","陆地","食肉","无危"],
    "鸽子":["2","天空","食草","无危"],
    "长颈鹿":["4","陆地","食草","易危"],
    "猫头鹰":["2","天空","食肉","濒危"],
    "海豚":["0","大海","食肉","濒危"],
    "海龟":["4","大海","食肉和草","濒危"],
    "蜜蜂":["6","天空","食草","无危"],
    "苍蝇":["6","陆地、天空","食血、肉和草","无危"]
}
a = random.choice(list(animals))
print("我LV.1!")
print("\033[1;36m动物家族里有熊猫、鸡、老虎、蛇、鸽子、长颈鹿、猫头鹰、海豚、海龟、蜜蜂、苍蝇！")
print("\033[1;32m小极客，到底哪个是神秘动物k呢？？？")
print("\033[1;31m")
clue = input("猜猜看！四条线索：1、2、3、4、look看答案，或直答，请写：")
guess = ""
count = 0
jin_bi = 0
while True:
    count = count + 1
    jin_bi = jin_bi + 2
    if clue == "1":
        print("\033[1;33m线索1：这只动物有",animals[a][0],"条腿。")
        guess = input("它是什么动物？")
    if clue == "2":
        print("\033[1;33m线索2：这只动物生活在",animals[a][1],"。")
        guess = input("它是什么动物？")
    if clue == "3":
        print("\033[1;33m线索3：这只动物的饮食：",animals[a][2],"。")
        guess = input("它是什么动物？")
    if clue == "4":
        print("\033[1;33m线索4：这只动物的保护等级是：",animals[a][3],"级。")
        guess = input("它是什么动物？")
    if clue == "look":
        print("\033[1;31m你没有猜对，正确答案是：",a,"\033[1;31m。")
        guess = input("\033[1;32m你一共猜了",count-1,"\033[1;32m次。")
        break
    if guess == a:
        print("\033[1;32m你真棒，猜对了！！！")
        time.sleep(1.258314159265358979386065463527861)
        print("\033[1;34m你一共用了",count,"\033[1;36m次猜对。")
        if count <= 4:
            print("奖励你一些金币！",jin_bi + 28,"个！\033[1;31m请点❤   ！")
            if jin_bi >= 3:
                print("well dowe!better!great job!!!!!!!!!!!")
            break
    if guess != a:
        print("\033[1A",end="")
        print("\033[K",end="")
        print("\033[1;31m输入正确,但答案错了！")
        print("\033[2A",end="")
        time.sleep(2)
        print
        continue
        break
    else:
        print("\033[1A",end="")
        print("\033[K",end="")
        print("\033[1;31m输入有误，请重新输入")
        print("\033[2A",end="")
        time.sleep(2)
        print
        continue
    break
    
    clue = input("你猜错啦，输入1、2、3、4、look")