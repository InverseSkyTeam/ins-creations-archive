#看最后一行代码
print("look!")
a = input("你想听故事吗？1=想！/2=不想！")
if a == "2":
    print("要听！")
if a == "1":
    print("好！")
import this
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
    "苍蝇":["6","天空","食血、肉和草","无危"]
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
        print("\033[1;32m你一共猜了",count-1,"\033[1;32m次。")
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
        
    clue = input("你猜错啦，输入1、2、3、4、look")
print("\033[1;32m还有！别走！")
friends= ['可多','小红','小明','小轩']
while True:
    print(friends)
    choice = input("加好友进群请按“+”，请人出群请按“-”，完成请按其他键：")
    if choice == "+":
        f = input("加谁？")
        friends.append(f)
    elif choice == "-":
        f = input("踢谁？（不要踢我！！！）")
        friends.remove(f)
    else:
        print(friends)
        break
food_list = ["\033[1;33m 0西冷牛扒","1美式烤鸡","2三文鱼","3意大利面","4牛排","5凯撒沙拉","6英式炸鱼排","7西兰花","8烤布丁","9草莓冰淇淋","10原味冰淇淋","11巧克力冰淇淋","12香草冰淇淋","13蘑菇汤","14玉米汤","15佐料","16果汁","17蛋汤炒绝味菜炒饭炒暴风","18饭","19菜","20汤","21零食","22三明治","23披萨","24奶茶"]
order = []
print("欢迎来到我们的餐厅！！！！！")
print("这是我们的菜单:",food_list)
choice = input("按A开始点菜：")
while True:
    if choice == "A":
        food_num = int(input("请输入想点菜品的序号(不可一次输入2个！！！):"))
        food_name = food_list[food_num]
        order.append(food_name)
        choice = input("继续点餐请输入A，删除菜品请输入B，停止点餐开始Eat请输入其他字符:")
    elif choice == "B":
        print("您点了这些菜品:",order)
        food_num = int(input("请输入想删除菜品的序号:"))
        food_name = food_list[food_num]
        order.remove(food_name)
        choice = input("继续点餐请输入A，删除菜品请输入B，停止点餐开始Eat请输入其他字符:")
    else:
        break
print("您点了这些菜:",order) 
print("\033[1;31m叮！")
password = input("\033[1;36m请设置密码。")
tn = input("请输入电话号码。")
zh = input("请输入账号。")
name = input("请输入姓名。")
nl = input("请输入年龄。")
csrq = input("请输入出生日期。")
nc = input("请输入昵称。")
yz = input("验证账号！")
yz2 = input("验证密码！")
yz3 = input("验证电话号码！")
yz4 = input("验证出生日期！")
yz5 = input("验证姓名！")
yz6 = input("验证昵称！")
yz7 = input("验证年龄！")
if yz == zh and yz2 == password and yz3 == tn and yz4 == csrq and yz5 == name and yz6 == nc and yz7 == nl:
    print("欢迎回来！！！！！",name,"!")
    print(nc,"您下载的《题目转转乐》已完成，快去看看吧！(由#99#5.502596知乎人emdjfh9908编程)")
    question = input("99*99=?    5805=1/9801=2/9701=3")
    while question != "2":
        print("错！再来一次吧!！")
    else:
        print("答对了！下一题！")
        question2 = input("太阳核心多少温度？    1600万度=1/16000度=2/800万度=3")
        while question2 != "1":
            print("错！再来一次吧!！")
        else:
            print("答对了！下一题！")
else:
    print("电脑已锁屏！")
print("\033[1;31m最后，最重要的环节：隐形代码！！！都不显示代码结束了！！！")
print("\033[1;8mlook,look,look,我的隐形代码厉害吧？！")
print("哈哈，感谢大家没有不耐烦！彩蛋！")
print("     *****   *****")
print("    ***************")
print("   *****************")
print("    ***************")
print("     *************")
print("      ***********")
print("       *********")
print("        *******")
print("         *****")
print("          ***")
print("           *")
print("求点赞！")
print("\033[1;32m现身请把147行的[1;8m改为[1;31m!!!")