'''
发明者：小轩
库名：jhxGUI
- 一款快速[智]造GUI窗口的软件
- 封装tk 简洁方便 简单记代码
- 编译速度基本0改变
- 包装完整 不易拆碎
- 美化窗口 在一瞬间
'''

import tkinter as tk
import sys
root = None
GUIX = tk

def jhx_error(text):
    '''
    用来制造错误的函数
    使用者一般没有必要写
    实在要写
    jhx_error(错误信息)
    会终端提示，然后自行停止所有程序
    '''
    print('\033[1;32m'+text)
    sys.exit()

def start():
    global root
    root = tk.Tk()

def main():
    global root
    try:
        root.mainloop()
    except:
        jhx_error('jhx.mainloop error:没有start函数无法进行main循环')

def set(width=100,height=100,site_x=100,site_y=100,title='jhx_window',icon=None,bg='white',alpha=None):
    global root
    root.title(title)
    root.geometry(str(width)+'x'+str(height)+'+'+str(site_x)+'+'+str(site_y))
    root["background"] = bg
    if (icon != None) and (('.ico' in icon) or ('.icon' in icon)):
        root.iconbitmap(icon)
    if alpha != None:
        root.attributes("-alpha", alpha)

def add_text(text='一个憨憨的单词'):
    exec('label = tk.Label(root,text="'+text+'")')
    exec('label.pack()')
    return eval('label')

def add_button(text='按钮无敌',func=None):
    if func != None:
        exec('button = tk.Button(root,text="'+text+'",command="'+func+'")')
    else:
        exec('button = tk.Button(root,text="'+text+'")')
    exec('button.pack()')
    return eval('button')