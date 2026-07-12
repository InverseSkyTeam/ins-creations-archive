#参考案例
# name = input ("有个人叫：" )
# where = input ("他在哪：")
# what = input ("做了什么？")
# speak(name + "是世界上最聪明的人。他正在"+ where + "。如果"+ what +"，就会被奖励金币100000000000枚。")

#1、补充input语句，实现输入回答的功能
#2、补充speak语句中的内容，注意使用字符串拼接
#3、还可以写一写你的新年祝福、新年愿望，等等
#还可以试试写成故事制造机哟，也可以参考上面的案例哦~

from xes.AIspeak import *
setmode("boy")
speak("你是谁？")
a = input("你是谁：")
speak("你好" + a)
speak("我是你的聊天机器人")
speak("你觉得你的战斗值有多少？")
b = input("你觉得你的战斗值有多少：")
speak("你竟然有" + b + "战斗值！")
speak("你觉得可能吗，天猫精灵？")
setmode("girl")
speak("我觉得不太可能。")
speak("我们可能耳朵听错了，要求返厂维修一下吧！")
setmode("boy")
speak("再见！")
setmode("girl")
speak("再见！")