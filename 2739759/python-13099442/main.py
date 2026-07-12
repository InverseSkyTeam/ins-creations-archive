import tkinter as tk
from tkinter.colorchooser import *

# 创建颜色选择函数
def colorselect():
	global color             # 设置全局变量
	colors = askcolor()
	  # 设置color的颜色（R, G, B）, 因为在后面会传入只能传入整数，所以这里利用int() 进行四舍五入
	color = (int(colors[0][0]),int(colors[0][1]),int(colors[0][2])) 
	choosedcolor.set(str(color))         # 设置choosedcolor 变量的值

# 创建绘制函数
def paint(event):
    x1, y1 = event.x, event.y
    x2, y2 = event.x, event.y
    w.create_oval(x1, y1, x2, y2, fill='#%02x%02x%02x' %color, outline='#%02x%02x%02x' %color)  # 设置颜色为colorchooser所选择的

root = tk.Tk()

color = (0,0,0)
choosedcolor = tk.StringVar()
choosedcolor.set(str(color))   # 设置初始颜色

tk.Label(root, text="自由涂鸦").pack(padx=10,pady=10)

frame1 = tk.Frame(root)
tk.Button(frame1, text="选择颜色", relief='flat',command=colorselect).pack(side='left',padx=3, pady=3)
tk.Label(frame1, textvariable=choosedcolor).pack(side='left',padx=3, pady=3)
frame1.pack(anchor='w')

w = tk.Canvas(root, width=400, height=200)
w.pack()

w.bind("<B1-Motion>", paint)   # 绘制函数绑定鼠标左键

tk.Button(root, text="清除屏幕", command=(lambda a='all':w.delete(a))).pack(padx=5, pady=5)

root.mainloop()