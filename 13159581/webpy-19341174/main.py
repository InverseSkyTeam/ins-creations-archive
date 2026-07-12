from cartoon import *
from xeslib import *
# 请你修改第4行代码，选择你喜欢的音乐
music = playbgMusic("d.mp3")
music.play()

# 请你修改第8行代码，选择你喜欢的动作
c1 = ["M1.png", "M2.png", "M3.png", "M4.png","M5.png","M6.png"]

# 请你补充第12行代码，遍历列表c1
# ====================================================
for i in c1:
    pic(i)
    set("王富晓.png",4)
    set("王立松.png",5)
    set("张思晨.png",6)
    set("123.png", 2)
    set("456.png", 1)
    set("789.png", 3)
# ====================================================

# 请你修改第17行代码，选择合适的时间间隔
display(0.5,50) 