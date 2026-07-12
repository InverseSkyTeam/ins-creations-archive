#使用所学知识，让计算机自动出题，完成100以内减法的练习程序吧！
#1.补充第18行代码，将保存在answer中的字符串转换成数字。
#2.补充第20-25行代码，判断答案正误，注意要满足嵌套要求哦~

#[小提示]可以使用play_mp3()播放音乐哦！
#欢快音乐：baba.mp3、lala.mp3、lulu.mp3
#悲伤音乐：try again.mp3、oh no.mp3、goodbye.mp3

from random import *
from xes.ext import *
for i in range(10):
    n = randint(50, 100)
    m = randint(0, 50)
    a = 0
    b = 0
    print("题目:", n, "-", m)
    answer = input("请输入答案：")
    #(1)将保存在answer中的字符串转换成数字
    answer = int(answer)
    #(2)判断答案正误，注意要满足嵌套要求哦
    if answer == n - m:
        print("答对啦！")
        play_mp3("baba.mp3")
        a = a + 1
        b = b + 1
    else:
        print("T_T答错了")
        b = 0
        play_mp3("try again.mp3")
print("您一共错了" + a + "题,combo乘" + b)