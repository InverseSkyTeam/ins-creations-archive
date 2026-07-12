from random import *
from easygui import *
a = randint(1,10)
msg = "不妨猜一下陈锦奕心里想的是哪个数字(1~10)"
title = "数字小游戏"
guess = integerbox(msg,title,lowerbound=1,upperbound=10)
while True:
    if guess == a:
        msgbox("你怎么知道的？")
        break
    if guess > a:
        msgbox("猜大了！")
    if guess < a:
        msgbox("猜小了！")
    guess = integerbox(msg,title,lowerbound=1,upperbound=10)
msgbox("游戏结束,不玩啦^_^")