from tkinter import (messagebox,filedialog,simpledialog)
from PIL import Image, ImageTk
from time import *
import tkinter as tk
import random
import shutil
import sys
import os

def mkdir(path):
    import os
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False

def copy_file(old_path, new_path):
    for file in os.listdir(old_path):
        try:
            shutil.copyfile(os.path.join(old_path, file), os.path.join(new_path, file))
        except:
            mkdir(new_path+'/'+file)
            copy_file(old_path+'/'+file, new_path+'/'+file)

try:
    import pyautogui as pag
except:
    print('请稍等，正在安装pyautogui库...(大约需要20秒)')
    try:
        os.system('pip install pip -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade')
        os.system('pip install pyautogui -i https://pypi.tuna.tsinghua.edu.cn/simple')
        import pyautogui as pag
    except:
        print('对不起，安装失败。正在尝试将库源文件复制到本地...(最多需要3秒)')
        copy_file('pyautogui','../'*5+'学而思直播/code/site-packages/pyautogui')
        copy_file('pymsgbox','../'*5+'学而思直播/code/site-packages/pymsgbox')
        copy_file('pyperclip','../'*5+'学而思直播/code/site-packages/pyperclip')
        import pyautogui as pag
        print('安装成功！')

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
    if back_ground == '#0a0a0a':
        close_button['fg'] = 'white'
    else:
        close_button['fg'] = 'black'

def change_on_hovering2(event):
    iconic_button['bg'] = 'grey'
    iconic_button['fg'] = 'lightgreen'

def return_to_normal_state2(event):
    iconic_button['bg'] = back_ground
    if back_ground == '#0a0a0a':
        iconic_button['fg'] = 'white'
    else:
        iconic_button['fg'] = 'black'

def iconic_window():
    root.overrideredirect(False)
    root.state('iconic')

def to_overrideredirect_window():
    if root.state() == 'normal':
        root.overrideredirect(True)
    else:
        root.overrideredirect(False)

def file_button_down():
    fileMenu.post(root.winfo_x()+70,root.winfo_y()+40)

def operation_button_down():
    operationMenu.post(root.winfo_x()+70,root.winfo_y()+80)

def config_button_down():
    configMenu.post(root.winfo_x()+70,root.winfo_y()+120)

def undotext():
    try:textbox.edit_undo()
    except:messagebox.showinfo('提示','提示：已经撤销至最初状态')

def redotext():
    try:textbox.edit_redo()
    except:messagebox.showinfo('提示','提示：已经恢复至最新状态')

def cuttext():
    pag.hotkey('ctrl','x')

def copytext():
    pag.hotkey('ctrl','c')

def pastetext():
    pag.hotkey('ctrl','v')

def all_select():
    pag.hotkey('ctrl','a')

def clear_all(event=None):
    textbox.delete('1.0','end')

def insert_commentheader():
    textbox.insert('1.0',"# coding:utf-8\n'''\n作品名：一个有点憨的程序\n作者:编程游侠\n出品时间:"+strftime('%Y/%m/%d %H:%M:%S',localtime())+"\n版权:(c)Copyright. xxx工作室xxx 保留所有权利\n作品介绍:我写了个寂寞~\n质量:A+\n'''\n")

def insert_commentline():
    textbox.insert('insert',"# comment codes\n")

def insert_commenttext():
    textbox.insert('insert',"'''\ncomment codes\ncomment codes\ncomment codes\n'''\n")

def insert_empty_lines():
    textbox.insert('insert',"\n\n\n")

def insert_text_box():
    textbox.insert('insert',"'''\n+-------------------------+\n|1.需要处理bug            |\n|2.赶紧更新               |\n|3.                       |\n+-------------------------+\n'''\n")

def insert_function():
    textbox.insert('insert',"def fun(param=True):\n    return param\n")

def insert_variable():
    textbox.insert('insert',"variable = True\n")

def insert_if():
    textbox.insert('insert',"if event:\n    pass\nelif event2:\n    pass\nelse:\n    pass\n")

def insert_while():
    textbox.insert('insert',"while event:\n    pass\nfor i in lib:\n    print(i)\n")

def insert_class():
    textbox.insert('insert',"class People(object):\n    def __init__(self,param=True):\n        self.name = param\n    def hello(self):\n        return 'hello,'+self.name+'!'\n")

def change_theme():
    global back_ground
    if back_ground == "#0a0a0a":
        back_ground = "white"
        title_name1['fg'] = 'black'
        back_ground = '#dadada'
        iconic_button['fg'] = 'black'
        close_button['fg'] = 'black'
        fileButton['fg'] = 'black'
        operationButton['fg'] = 'black'
        configButton['fg'] = 'black'
        window['bg'] = '#efefef'
        textbox['bg'] = 'white'
        textbox['fg'] = 'black'
        linebox['bg'] = '#cecece'
        linebox['fg'] = 'black'
    else:
        back_ground = "#0a0a0a"
        title_name1['fg'] = 'lightgreen'
        iconic_button['fg'] = 'white'
        close_button['fg'] = 'white'
        fileButton['fg'] = 'white'
        operationButton['fg'] = 'white'
        configButton['fg'] = 'white'
        window['bg'] = '#2d2d2d'
        textbox['bg'] = 'black'
        textbox['fg'] = 'white'
        linebox['bg'] = '#3e3e3e'
        linebox['fg'] = 'white'
    title_bar['bg'] = back_ground
    title_bar['highlightcolor'] = back_ground
    iconic_button['bg'] = back_ground
    close_button['bg'] = back_ground
    title_name1['bg'] = back_ground
    title_name2['bg'] = back_ground
    title_name3['bg'] = back_ground
    title_icon['bg'] = back_ground
    operation_area['bg'] = back_ground
    editing_area['bg'] = back_ground
    fileButton['bg'] = back_ground
    operationButton['bg'] = back_ground
    configButton['bg'] = back_ground

def change_alpha():
    alphavalue = simpledialog.askstring(title='设置',prompt='设置窗体透明度(0~1之间)')
    root.attributes('-alpha',alphavalue)

def counttext(event):
    lines = textbox.get('1.0','end').count('\n')
    lines = '\n'.join([str(i) for i in list(range(round(lines*sbar_y.get()[0])+1,round(lines*sbar_y.get()[1]+1)))])
    linebox.delete('1.0','end')
    linebox.insert('1.0',lines)

def download_lib():
    dlname = simpledialog.askstring(title='下载第三方库',prompt='第三方库名称')
    print('正在下载'+dlname+'库...\n若直接弹出"库检测结束"，即拼写错误')
    try:
        os.system('pip install '+dlname+' -i https://pypi.tuna.tsinghua.edu.cn/simple')
    except:
        print('安装失败!')
    else:
        print('安装安成!')
        try:
            exec('import '+dlname)
        except:
            print('导入失败，或许安装路径出现冲突，或许导入名称有所不同，请自行尝试!')
        else:
            print('导入无问题!')
        finally:
            print('导入检测结束')
    finally:
        print('库检测结束')

def runcode(event=None):
    textcode = textbox.get('1.0','end')
    try:
        exec(textcode,globals(),locals())
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
            os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple '+lib)
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

def callback():
    if messagebox.askyesno('关闭','您确定要关闭[IdealXes IDE]吗?'):
        root.destroy()
    else:
        pass

# main
back_ground = "#0a0a0a"

root = tk.Tk()
root.state('normal')
root.overrideredirect(True)
root.attributes('-topmost',True)

root.geometry('1280x780+100+11')

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
                         command=callback)

title_name1 = tk.Label(title_bar,text='IdealXes',font=('楷体',11,'bold'),bg=back_ground,fg='lightgreen')
title_name2 = tk.Label(title_bar,text='IDE',font=('楷体',11,'bold'),bg=back_ground,fg='orange')
title_name3 = tk.Label(title_bar,text='V0.8',font=('楷体',11,'bold'),bg=back_ground,fg='#ff5166')
icon = ImageTk.PhotoImage(Image.open("IXcodelogo.png"))
title_icon = tk.Button(title_bar,bg=back_ground,image=icon,
                       bd=3,highlightthickness=0,
                       command=lambda:messagebox.showinfo('提示','IdealXes项目\n版权：\n参与人物：\n吴宇航\n小轩\n何嘉晨\n冀厚锦\n富兰克林\n袁梓轩\n等\n参与团队：\n逆天工作室\n参考文献不少于6000条\n版权所有，侵权必究'))

window = tk.Frame(root,bg="#2d2d2d",highlightthickness=0)
operation_area = tk.Frame(window,bg=back_ground,width=60)
operation_area.pack(side='left',fill='y')
program_title = tk.Entry(window,textvariable=tk.StringVar(value='请输入作品名称'),width=50)
program_title.pack(side='top')
editing_area = tk.Frame(window,bg=back_ground)
editing_area.pack(side='right')

fileButton = tk.Button(operation_area,bg=back_ground,
                       fg='white',text='文件',bd=0,
                       font=('楷体',18,'bold'),relief='sunken',
                       highlightthickness=0,
                       activebackground='lightskyblue',
                       activeforeground='blue',
                       command=file_button_down)
fileButton.pack(side='top',fill='both')
operationButton = tk.Button(operation_area,bg=back_ground,
                       fg='white',text='操作',bd=0,
                       font=('楷体',18,'bold'),relief='sunken',
                       highlightthickness=0,
                       activebackground='lightgreen',
                       activeforeground='green',
                       command=operation_button_down)
operationButton.pack(side='top',fill='both')
configButton = tk.Button(operation_area,bg=back_ground,
                       fg='white',text='设置',bd=0,
                       font=('楷体',18,'bold'),relief='sunken',
                       highlightthickness=0,
                       activebackground='lightyellow',
                       activeforeground='#8e7437',
                       command=config_button_down)
configButton.pack(side='top',fill='both')
fileMenu = tk.Menu(operation_area,tearoff=0,background='lightskyblue')
fileMenu.add_command(label='运行',command=runcode,accelerator='F5')
operationMenu = tk.Menu(operation_area,tearoff=0,background='lightgreen')
operationInsertMenu = tk.Menu(operationMenu,tearoff=0,background='green',foreground='white')
operationInsertMenu.add_command(label='作品注释头',command=insert_commentheader)
operationInsertMenu.add_command(label='注释代码行',command=insert_commentline)
operationInsertMenu.add_command(label='注释代码段',command=insert_commenttext)
operationInsertMenu.add_command(label='空行代码段',command=insert_empty_lines)
operationInsertMenu.add_command(label='文本框',command=insert_text_box)
operationInsertMenu.add_separator()
operationInsertMenu.add_command(label='函数',command=insert_function)
operationInsertMenu.add_command(label='变量',command=insert_variable)
operationInsertMenu.add_command(label='分支语句',command=insert_if)
operationInsertMenu.add_command(label='循环语句',command=insert_while)
operationInsertMenu.add_command(label='类',command=insert_class)
operationMenu.add_cascade(label='插入...',menu=operationInsertMenu)
operationMenu.add_separator()
operationMenu.add_command(label='全选',command=copytext,accelerator='Ctrl+A')
operationMenu.add_command(label='剪切',command=cuttext,accelerator='Ctrl+X')
operationMenu.add_command(label='复制',command=copytext,accelerator='Ctrl+C')
operationMenu.add_command(label='粘贴',command=pastetext,accelerator='Ctrl+V')
operationMenu.add_command(label='撤销',command=undotext,accelerator='Ctrl+Z')
operationMenu.add_command(label='重做',command=redotext,accelerator='Ctrl+Y')
operationMenu.add_command(label='清空',command=clear_all,accelerator='Ctrl+DEL')
configMenu = tk.Menu(operation_area,tearoff=0,background='lightyellow')
configMenu.add_command(label='切换主题',command=change_theme)
configMenu.add_command(label='设置透明度',command=change_alpha)
configMenu.add_command(label='下载第三方库',command=download_lib)

sbar_y = tk.Scrollbar(editing_area)
sbar_y.pack(side='right',fill='y')
sbar_x = tk.Scrollbar(editing_area,orient=tk.HORIZONTAL)
sbar_x.pack(side='bottom',fill='x')
linebox = tk.Text(editing_area,height=25,width=5,bg='#3e3e3e',fg='white',font=('楷体',20),insertbackground='#3e3e3e')
linebox.pack(side='left',fill='y')
textbox = tk.Text(editing_area,height=25,width=60,bg='black',fg='white',font=('楷体',20),
                  undo=True,wrap = 'none',insertbackground='lightskyblue',
                  yscrollcommand=sbar_y.set,xscrollcommand=sbar_x.set)
textbox.pack(side='right',fill='y')
sbar_y.config(command=textbox.yview)
sbar_x.config(command=textbox.xview)

title_bar.pack(fill='x')
title_icon.pack(side='left')
title_name1.pack(side='left')
title_name2.pack(side='left')
title_name3.pack(side='left')
close_button.pack(side='right')
iconic_button.pack(side='right')
window.pack(expand=True, fill='both')

root.bind('<Key>',counttext)
root.bind('<Control-v>',counttext)
root.bind('<Button-1>',counttext)
root.bind('<MouseWheel>',counttext)
root.bind("<B1-Motion>",counttext)
root.bind('<F5>',runcode)
root.bind('<Control-Delete>',clear_all)
title_bar.bind("<B1-Motion>", move_window)
title_bar.bind("<Button-1>", get_pos)
close_button.bind('<Enter>', change_on_hovering)
close_button.bind('<Leave>', return_to_normal_state)
iconic_button.bind('<Enter>', change_on_hovering2)
iconic_button.bind('<Leave>', return_to_normal_state2)
linebox.bind('<Key>',lambda event:'stop')

root.protocol("WM_DELETE_WINDOW", callback)

while True:
    try:
        to_overrideredirect_window()
        root.update()
    except:
        break