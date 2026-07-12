#请补充程序，制作一个单词翻译小程序。
from xes.AIspeak import *
#1、修改第4、5行的参数，可以个性化设置小助手的声音、语速
setmode("boy")
setspeed(1)
speak("你好，我是你的翻译小助手")
speak("请输入需要翻译的内容")
#2、请在下一行补充输入语句，完成输入功能
a = input("请输入单词：")
speak(a)
b = translate(a)
#3、请在下一行补充输出翻译结果的语句，注意翻译内容保存在变量b中~
print("翻译结果：", b)
speak(b)