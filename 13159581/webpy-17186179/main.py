from xes.AIspeak import *
from AIface import *
print("欢迎使用网校最强大最完美的智能美颜相机")
print("3,2,1,开始拍照")
speak("欢迎使用网校最强大最完美的智能美颜相机")
speak("3,2,1,开始拍照")

#1、请取消第9或第10行的注释，选择你使用的照片获取方式
a = "王立松.jpg"
a = getPicture()
show(a)

print("你想使用相机的哪种功能？1变老人2变小孩3变男生4变女生5动漫化6笑容指数7悲伤指数8年龄9鉴定物体")
#speak("你想使用相机的哪种功能？1变老人2变小孩3变男生4变女生5动漫化6笑容指数7悲伤指数8年龄9鉴定物体")

#2、修改下一行的数字，设置自己的录音时长，不要超过10秒哦
ans = getSound(2)
print(ans)

#3、补充第32行的完整的or条件
#4、也可以尝试把happy()、sad()、age()、see()等功能加入你的相机哟
#以下为参考代码
#n = happy(a)
#print(n)

if ("一" in ans)  or ("1" in ans) :
    print("变老人")
    speak("变老人")
    p = old(a)
    show(p)

#请补充完整的or条件
if  ("二" in ans)  or ("2" in ans):
    print("变小孩")
    speak("变小孩")
    p = young(a)
    show(p)

if ("三" in ans)  or ("3" in ans) :
    print("变男生")
    speak("变男生")
    p = boy(a)
    show(p)

if ("四" in ans)  or ("4" in ans) :
    print("变女生")
    #speak("变女生")
    p = girl(a)
    show(p)

if  ("五" in ans)  or ("5" in ans) :
    print("动漫化")
    speak("动漫化")
    p = Animation(a)
    show(p)
if  ("六" in ans)  or ("6" in ans) :
    p = happy(a)
    show(p)
if  ("七" in ans)  or ("7" in ans) :
    p = sad(a)
    show(p)
if  ("八" in ans)  or ("8" in ans) :
    p = age(a)
    show(p)
if  ("九" in ans)  or ("9" in ans) :
    p = see(a)
    show(p)
