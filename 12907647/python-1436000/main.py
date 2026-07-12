from random import *
from time import *
def fun(line):
    for x in range(len(line)):
        print("\r"+line[0:x+1],end='')
        sleep(0.1)
def clear():
    print("\033[1000A\033[2J",end='')
fun("\033[1;36mJ·hx产品！飞翔公司抄袭、伪劣、错误！")
sleep(0.9999)
clear()
fun("\033[1;4m我编的书！\033[1;0m")
fun("装在口袋里的爸爸：超级护身符")
clear()
print("666!")
fun("你的角色：\033[1;36m杨歌。")
sleep(0.5)
fun("请按3下空格，游戏马上开始！！！")
for y in range(3):
    input("按！")
clear()
fun("")
print("      ")
fun("                       ")
clear()
fun("所有护身符已造完！")
print("爸爸拿着一个闪电护身符，刷一下闪电飞出！（其他你也知道！）爸爸做出超能护身符，全能了！")
input("说句赞叹的话：")
clear()
fun("爸爸：那当然？！")
fun("一天，一个小偷来到你家，你怎么办？")
clear()
fun("机器建议：用护身符隐身，再把他冲成落汤鸡！")
a = input("1=机器建议 2=自己的方案")
if a == "1":
    fun("")
elif a == "2":
    input("你的方案：")
else:
    fun("没有此选项！")
fun("他叫“有鬼啊！”落荒而逃，自首去了！")
clear()
print("             ")
fun("             ")
clear()