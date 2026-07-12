# print('\033[1;31m')
print('Ideal Xes(IX)计划 编辑器Version0.7')
# print('#手动变量或热度调到0对优秀作品是没有用的，真正的优秀永远不会褪色，只有嫉妒的毒焰会腐蚀没有技术的人#')
# print('此致，敬礼\033[0m')

from tkinter import (messagebox,filedialog)
from time import *
from PIL import Image, ImageTk
import tkinter as tk
import random
import pip
import os

errors = {
"Syntax": "发现错误：代码格式问题，检查中英文；冒号、括号是否缺少；结构是否完整等",
"Type": "发现错误：程序中存在类型异常，请检查您的数据类型是否准确等",
"Value": "发现错误：取值错误，请检查字典的键值调用等",
"Name": "发现错误：命名错误，请检查您变量、函数等的调用以及拼写错误",
"Attribute": "发现错误：属性错误，请检查函数、类与成员等的调用",
"Index&Key": "发现错误：程序中出现下标异常，请检查下表及键",
"IndentationError": "发现错误：缩进有问题，请仔细检查",
"ImportError": "发现错误：导入的库有问题，请检查库的拼写与安装",
"OS": "发现错误：出现操作系统相关异常",
"Warn": "发现错误：程序中存在未处理的警告",
"Runtime": "发现错误：程序中存在时间超限错误，请优化代码，检查递归及堆栈",
"Memory": "发现错误：程序内存溢出，请优化代码，避免死循环",
"Calc": "发现错误：程序计算错误，需检查极限运算、除数是否为0、数据过大等问题",
"Encode": "发现错误：编码异常，请查看代码中的异常编码",
"unfind": "发现错误：赋值前引用了其他函数内的局部变量",
"Others": "程序中出现未预料到的异常，请您仔细检查",
}

def get_pos(event):
    global xwin,ywin
    xwin = event.x
    ywin = event.y

def move_window(event):
    root.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')

def change_on_hovering(event):
    close_button['bg'] = 'red'
    close_button['fg'] = 'lightgreen'

def return_to_normal_state(event):
    close_button['bg'] = back_ground
    close_button['fg'] = 'white'

def change_on_hovering2(event):
    iconic_button['bg'] = 'grey'
    iconic_button['fg'] = 'lightgreen'

def return_to_normal_state2(event):
    iconic_button['bg'] = back_ground
    iconic_button['fg'] = 'white'

def iconic_window():
    root.overrideredirect(False)
    root.state('iconic')

def to_overrideredirect_window():
    if root.state() == 'normal':
        root.overrideredirect(True)
    else:
        root.overrideredirect(False)

def file_button_down():
    fileMenu.post(root.winfo_x()+55,root.winfo_y()+40)

def operation_button_down():
    operationMenu.post(root.winfo_x()+55,root.winfo_y()+80)

def undotext():
    try:textbox.edit_undo()
    except:messagebox.showinfo('提示','提示：已经撤销至最初状态')

def redotext():
    try:textbox.edit_redo()
    except:messagebox.showinfo('提示','提示：已经恢复至最新状态')

def runcode(event=None):
    textcode = textbox.get('1.0','end')
    try:
        exec(textcode)
    except SyntaxError as e:
        error = str(e) + '\n' + errors["Syntax"]
        messagebox.showerror('发生错误',error)
    except TypeError as e:
        error = str(e) + '\n' + errors["Type"]
        messagebox.showerror('发生错误',error)
    except ValueError as e:
        error = str(e) + '\n' + errors["Value"]
        messagebox.showerror('发生错误',error)
    except NameError as e:
        error = str(e) + '\n' + errors["Name"]
        messagebox.showerror('发生错误',error)
    except AttributeError as e:
        error = str(e) + '\n' + errors["Attribute"]
        messagebox.showerror('发生错误',error)
    except (IndexError, KeyError) as e:
        error = str(e) + '\n' + errors["Index&Key"]
        messagebox.showerror('发生错误',error)
    except IndentationError as e:
        error = str(e) + '\n' + errors["IndentationError"]
        messagebox.showerror('发生错误',error)
    except ImportError as e:
        error = str(e) + '\n' + errors["ImportError"]
        messagebox.showerror('发生错误',error)
        question = messagebox.askyesno('问题','是否安装此库？')
        if question:
            lib = str(e).split(' ')[-1].split('\'')[1]
            os.system('pip install '+lib)
    except OSError as e:
        error = str(e) + '\n' + errors["OS"]
        messagebox.showerror('发生错误',error)
    except Warning as e:
        error = str(e) + '\n' + errors["Warn"]
        messagebox.showerror('发生错误',error)
    except RuntimeError as e:
        error = str(e) + '\n' + errors["Runtime"]
        messagebox.showerror('发生错误',error)
    except MemoryError as e:
        error = str(e) + '\n' + errors["Memory"]
        messagebox.showerror('发生错误',error)
    except ArithmeticError as e:
        error = str(e) + '\n' + errors["Calc"]
        messagebox.showerror('发生错误',error)
    except UnicodeError as e:
        error = str(e) + '\n' + errors["Encode"]
        messagebox.showerror('发生错误',error)
    except UnboundLocalError as e:
        error = str(e) + '\n' + errors["unfind"]
        messagebox.showerror('发生错误',error)
    except Exception as e:
        error = str(e) + '\n' + errors["Others"]
        messagebox.showerror('发生错误',error)

# main
back_ground = "#0a0a0a"

root = tk.Tk()
root.state('normal')
root.overrideredirect(True)
root.lift()
root.attributes('-topmost',True)
root.attributes('-topmost',False)

root.geometry('1280x780+100+1')

title_bar = tk.Frame(root, bg=back_ground, relief='ridge', bd=1, padx=0,
                     highlightcolor=back_ground, 
                     highlightthickness=0)

iconic_button = tk.Button(title_bar, text='—', # text='︾',
                          bg=back_ground, padx=5, pady=3,
                          bd=0, font='bold', fg='white',
                          activebackground='lightskyblue',
                          activeforeground='white',
                          highlightthickness=0,
                          command=iconic_window)

close_button = tk.Button(title_bar, text='×',
                         bg=back_ground, padx=5, pady=3, 
                         bd=0, font='bold', fg='white',
                         activebackground='#ff1e5e',
                         activeforeground='white', 
                         highlightthickness=0,
                         command=root.destroy)

title_window = 'IdealXes tk分支-辅助编辑器V0.6[INS-jhx] (awa-)'
title_name = tk.Label(title_bar, text=title_window, bg=back_ground, fg='white')
icon = ImageTk.PhotoImage(Image.open("IXcodelogo.png"))
title_icon = tk.Button(title_bar, bg=back_ground, image=icon,
                       bd=3,highlightthickness=0,
                       command=lambda:messagebox.showinfo('提示','别捏我呀~'))

window = tk.Frame(root, bg="#2d2d2d", highlightthickness=0)
operation_area = tk.Frame(window,bg=back_ground,width=60)
operation_area.pack(side='left',fill='y')
editing_area = tk.Frame(window,bg=back_ground)
editing_area.pack(side='right')

fileButton = tk.Button(operation_area,bg=back_ground,
                       fg='white',text='文件',bd=0,
                       font='bold',relief='sunken',
                       highlightthickness=0,
                       activebackground='lightskyblue',
                       activeforeground='blue',
                       command=file_button_down)
fileButton.pack(side='top',fill='both')
operationButton = tk.Button(operation_area,bg=back_ground,
                       fg='white',text='操作',bd=0,
                       font='bold',relief='sunken',
                       highlightthickness=0,
                       activebackground='lightgreen',
                       activeforeground='black',
                       command=operation_button_down)
operationButton.pack(side='top',fill='both')
fileMenu = tk.Menu(operation_area,tearoff=0,background='lightskyblue')
fileMenu.add_command(label='运行[此功能正在完善]',command=runcode,accelerator='F5')
operationMenu = tk.Menu(operation_area,tearoff=0,background='lightgreen')
operationMenu.add_command(label='撤销',command=undotext,accelerator='Ctrl+Z')
operationMenu.add_command(label='重做',command=redotext,accelerator='Ctrl+Y')

sbar_y = tk.Scrollbar(editing_area)
sbar_y.pack(side='right',fill='y')
sbar_x = tk.Scrollbar(editing_area,orient=tk.HORIZONTAL)
sbar_x.pack(side='bottom',fill='x')
textbox = tk.Text(editing_area,height=26,width=60,bg='black',fg='white',font=('楷体',20),
                  undo=True,wrap = 'none',insertbackground='lightskyblue',
                  yscrollcommand=sbar_y.set,xscrollcommand=sbar_x.set)
textbox.pack()
sbar_y.config(command=textbox.yview)
sbar_x.config(command=textbox.xview)

title_bar.pack(fill='x')
title_icon.pack(side='left')
title_name.pack(side='left')
close_button.pack(side='right')
iconic_button.pack(side='right')
window.pack(expand=True, fill='both')

root.bind('<F5>',runcode)
title_bar.bind("<B1-Motion>", move_window)
title_bar.bind("<Button-1>", get_pos)
close_button.bind('<Enter>', change_on_hovering)
close_button.bind('<Leave>', return_to_normal_state)
iconic_button.bind('<Enter>', change_on_hovering2)
iconic_button.bind('<Leave>', return_to_normal_state2)

while True:
    try:
        to_overrideredirect_window()
        root.update()
    except:
        break