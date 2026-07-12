#利用本节课学习的知识给敬老院的爷爷奶奶做一个提醒小程序。
#要求：
#1.完善时钟功能，每隔1秒钟显示当前时间；
#2.在每天08:00:00、12:00:00、20:00:00提醒喝水。

from time import *
from xes.ext import *

#(1)补充第10行代码，持续不断地输出时间
while True:
    clock = strftime("%H:%M:%S")
    print(clock)
    if clock == "08:00:00":
        print("喝水时间到啦！")
        #send_msg(136XXXX9649, "喝水时间到啦！")
    if clock == "12:00:00":
        print("喝水时间到啦！")
        #send_msg(136XXXX9649, "喝水时间到啦！")
    if clock == "20:00:00":
        print("喝水时间到啦！")
        #send_msg(136XXXX9649, "喝水时间到啦！")
    #(2)补充第23行代码，每隔1秒钟显示当前时间
    sleep(1)