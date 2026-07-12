from xes.ext import *
from xes.AIspeak import *
speak("你好，我是你的天气小助手")
speak("请输入需要查询温度的城市：")
city = input("请输入需要查询温度的城市：")
for i in range(7):
    t = air_temp(city,i)
    print("查询到",city,"未来第",i,"天的温度为：",t)
    if t >= 35:
        print("温度过高,不建议外出")
    if t >= 15 and t < 35:
        print("温度偏高,建议外出穿衬衫")
    if t >= 15 and t < 25:
        print("温度偏低,建议外出穿外套")
    if t >= 5 and t < 15:
        print("温度低,建议外出穿羽绒服")
    if t < 5:
        print("温度过低,不建议外出")