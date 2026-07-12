from easygui import *
a = buttonbox('                           大家说我长的帅吗？',image='图片.png',choices=('帅','不帅','!@#$%'))
title = "大家说我长的帅吗？"  
if a == "帅":
    msgbox("没错！")
else:
    while True:
        msgbox("弄坏你的电脑！！！")
