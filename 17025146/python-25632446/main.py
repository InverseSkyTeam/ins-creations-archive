from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os
import sys
try:
    import panda3d
except:
    messagebox.showinfo("提示","您还没有安装panda3d库，请先安装。")
    sys.exit(0)
apps = ["探险地下密室","方块世界","旋转熊猫","无尽隧道","星球大战","机器人拳击","棋盘","植树游戏","模拟太阳系","正方体","海上帆船","滚动小球","漫游郊外","灯光秀","音乐盒","高山风景","鼠标立方体"]
root = Tk()
root.title("Python 3D动画、游戏合集")
style = Style()
style.configure("Blue.Label", foreground="blue")
Label(text = "Python 3D动画、游戏合集",font = ("kaiti",20),style = "Blue.Label").pack()

def x1():
	os.system(f'"{sys.executable}" 探险地下密室.py')
def x2():
	os.system(f'"{sys.executable}" 方块世界.py')
def x3():
	os.system(f'"{sys.executable}" 旋转熊猫.py')
def x4():
	os.system(f'"{sys.executable}" 无尽隧道.py')
def x5():
	os.system(f'"{sys.executable}" 星球大战.py')
def x6():
	oos.system(f'"{sys.executable}" 机器人拳击.py')
def x7():
	os.system(f'"{sys.executable}" 棋盘.py')
def x8():
	os.system(f'"{sys.executable}" 植树游戏.py')
def x9():
	os.system(f'"{sys.executable}" 模拟太阳系.py')
def x10():
	os.system(f'"{sys.executable}" 正方体.py')
def x11():
	os.system(f'"{sys.executable}" 海上帆船.py')
def x12():
	os.system(f'"{sys.executable}" 滚动小球.py')
def x13():
	os.system(f'"{sys.executable}" 漫游郊外.py')
def x14():
	os.system(f'"{sys.executable}" 灯光秀.py')
def x15():
	os.system(f'"{sys.executable}" 音乐盒.py')
def x16():
	os.system(f'"{sys.executable}" 高山风景.py')
def x17():
	os.system(f'"{sys.executable}" 鼠标立方体.py')

for i in range(len(apps)):
	Button(text = apps[i],width = 50,command = eval("x{}".format(i + 1))).pack()
root.mainloop()