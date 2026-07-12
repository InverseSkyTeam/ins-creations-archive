import tkinter as tk,random
from 中文 import *
from tkinter import messagebox

colorList = ['red','blue','black','white','orange','green','yellow','purple','skyblue','pink','lightskyblue']

errors = {"Syntax": "发现错误：等级/低级错误：优先检查：中英文；冒号、括号是否缺少；结构完整 等~",
"Type": "发现错误：等级/低级错误：您的程序中存在TypeError类型异常，检查您的数据类型输入是否准确，需不需要进行转换/字典的键值 等~",
"Value": "发现错误：等级/低级错误：您的程序中存在ValueError值错误，检查您需不需要进行转换/字典的键值 等~",
"Name&Attribute": "发现错误：等级/超低级错误：NameError（命名错误）或Attribute（属性错误），请检查您的变量、函数及成员等的调用哦~",
"Index&Key": "发现错误：等级/低级错误：您的程序中出现了下标异常，请检查您的下标使用；查看数据的错误，键值错误，如KeyError,IndexError~",
"IndentationError": "发现错误：等级/超低级错误：IndentationError：缩进有问题，仔细检查~",
"ImportError": "发现错误：等级/低级错误：ImportError：导入的库有问题，检查库的拼写与安装~",
"OS": "发现错误：等级/高级错误：出现操作系统相关异常~",
"Warn": "发现错误：等级/中级错误：您的程序中存在警告，请修复~",
"Others": "您的程序中有些非常见的异常哦！请您仔细检查！我没有安排此错误~"}

def bgcolorf():
    global colorList
    textbox['bg'] = random.choice(colorList)
    bgcolorbutton['bg'] = random.choice(colorList)
def fgcolorf():
    global colorList
    textbox['fg'] = random.choice(colorList)
    fgcolorbutton['fg'] = random.choice(colorList)
def run_main():
    ptextbox = textbox.get('1.0',tk.END)
    try:
        exec(ptextbox)
    except SyntaxError:
        error = errors["Syntax"]
        messagebox.showerror('error:错误',error)
    except TypeError:
        error = errors["Type"]
        messagebox.showerror('error:错误',error)
    except ValueError:
        error = errors["Value"]
        messagebox.showerror('error:错误',error)
    except (NameError, AttributeError):
        error = errors["Name&Attribute"]
        messagebox.showerror('error:错误',error)
    except (IndexError, KeyError):
        error = errors["Index&Key"]
        messagebox.showerror('error:错误',error)
    except IndentationError:
        error = errors["IndentationError"]
        messagebox.showerror('error:错误',error)
    except ImportError:
        error = errors["ImportError"]
        messagebox.showerror('error:错误',error)
    except OSError:
        error = errors["OS"]
        messagebox.showerror('error:错误',error)
    except Warning:
        error = errors["Warn"]
        messagebox.showerror('error:错误',error)
    except Exception:
        error = errors["Others"]
        messagebox.showerror('error:错误',error)
    

root = tk.Tk()
label = tk.Label(text='如代码太长用滚轮滚动哦\n输出照常在终端，其他如pygame也行\n支持导入库')
textbox = tk.Text(height=31,width=100,bg='black',fg='yellow',font=('黑体',14))
bgcolorbutton = tk.Button(bg='green',fg='white',text=' '*81+'背景换色'+' '*81,command=bgcolorf)
fgcolorbutton = tk.Button(fg='green',text=' '*81+'字体换色'+' '*81,command=fgcolorf)
runStart = tk.Button(bg='orange',fg='white',text=' '*83+'▶运行'+' '*83,command=run_main)
label.grid(row=0, column=0)
textbox.grid(row=1, column=0)
bgcolorbutton.grid(row=2, column=0)
fgcolorbutton.grid(row=3, column=0)
runStart.grid(row=4, column=0)
root.mainloop()