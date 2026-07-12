from xes.ext import *
from time import *
a = input("请输入你想发送消息的电话号码：")
b = int(a)
c = input("请输入你想发送消息的内容：")
while True:
    t = strftime("%H:%M:%S")
    sleep(1)
    print(t)
    if t == "17:34:00":
        send_msg(b,c)