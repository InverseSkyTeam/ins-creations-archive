import tkinter as tk
import random
from os import *
from time import *
from ctypes import *
from win32api import GetSystemMetrics
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

print('''\033[1;31m+------------------+
|      合同书      |
|1.不管发生什么，乙|
|方都不能追究甲方的|
|责任！            |
|                  |
|2.乙方的电脑可能会|
|爆炸，愚人！      |
|                  |
|3.乙方不会恨甲方，|
|和平共处，友好相待|
|哦~！点赞！       |
|                  |
|                  |
|甲方：            |
|小轩              |
|乙方：(下方签字)  |''')
input('|')
print('+------------------+')
sleep(1.5)

for i in range(150):
    system('start')
    windll.user32.SetCursorPos(random.randint(0, width), random.randint(0, height))
system('start C:')
system('shutdown/s /c 你的电脑已被黑客入侵，愚人节快乐! /t 35')
sleep(3.5)

root = tk.Tk()
root.attributes('-fullscreen', True)
root.wm_attributes('-topmost', True)

frame = tk.Frame(root, bg='darkblue')
frame.pack(fill='both', expand=True)

label = tk.Label(frame,text='Error\nTrojan horse virus invaded your computer\n360 antivirus software and system protection measures are invalid\nNameError with “小轩” to Error - xiaoxuanError\nshutdown▂\nError with xiaoxuan the virus,be chGAF,awfujhmawf the virus!\nbad list for 248 \n your computer is BIG BANG for boom\nstyle 404\nGo Error start!\nError mouse you see.▃',fg='white',bg='darkblue',font=['楷体',20])
label.place(x=0,y=0)

root.mainloop()