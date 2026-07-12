from tkinter import messagebox
from save_file import *
from time import *
import tkinter as tk
import tkinter.filedialog
import os
import random
import 中文

mkpath="D:\\system_jhxc\\python_file"
mkdir(mkpath)

colorList = ['red','blue','black','white','orange','green','yellow','purple','skyblue','pink','lightskyblue']

errors = {"Syntax": "发现错误：等级/低级错误：优先检查：中英文；冒号、括号是否缺少；结构完整 等~",
"Type": "发现错误：等级/低级错误：您的程序中存在TypeError类型异常，检查您的数据类型输入是否准确，需不需要进行转换/字典的键值 等~",
"Value": "发现错误：等级/低级错误：您的程序中存在ValueError值错误，检查您需不需要进行转换/字典的键值 等~",
"Name": "发现错误：等级/超低级错误：NameError（命名错误）请检查您变量等的调用哦~",
"Attribute": "发现错误：等级/低级错误：Attribute（属性错误），请检查您的函数及成员等的调用哦~",
"Index&Key": "发现错误：等级/低级错误：您的程序中出现了下标异常，请检查您的下标使用；查看数据的错误，键值错误，如KeyError,IndexError~",
"IndentationError": "发现错误：等级/超低级错误：IndentationError：缩进有问题，仔细检查~",
"ImportError": "发现错误：等级/低级错误：ImportError：导入的库有问题，检查库的拼写与安装~",
"OS": "发现错误：等级/高级错误：出现操作系统相关异常~",
"Warn": "发现错误：等级/中级错误：您的程序中存在警告，请修复~",
"Others": "您的程序中有些非常见的异常哦！请您仔细检查！我没有安排此错误~"}

def bgcolorf():
    global colorList
    a1 = random.choice(colorList)
    while a1 == textbox['bg'] or a1 == textbox['fg']:
        a1 = random.choice(colorList)
    textbox['bg'] = a1
    a2 = random.choice(colorList)
    while a2 == bgcolorbutton['bg'] or a2 == bgcolorbutton['fg']:
        a2 = random.choice(colorList)
    bgcolorbutton['bg'] = a2

def fgcolorf():
    global colorList
    b1 = random.choice(colorList)
    while b1 == textbox['bg'] or b1 == textbox['fg']:
        b1 = random.choice(colorList)
    textbox['fg'] = b1
    b2 = random.choice(colorList)
    while b2 == bgcolorbutton['bg'] or b2 == bgcolorbutton['fg']:
        b2 = random.choice(colorList)
    bgcolorbutton['fg'] = b2

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
    except NameError:
        error = errors["Name"]
        messagebox.showerror('error:错误',error)
    except AttributeError:
        error = errors["Attribute"]
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
        ask_mode = messagebox.askyesno('a question','若无拼写错误，是否要安装此库？（如果是拼写错误或不要安装点击否）')
        if ask_mode:
            ask_is_ok = messagebox.askyesno('a question','已经对目前代码存档点击是，没有则点击否（如果未存档却点击了“是”，您将付出代价）')
            if ask_is_ok:
                root.destroy()
                exec(ptextbox)
            else:
                messagebox.showinfo('温馨提示','温馨提示:请先存档哦，不然代码会丢掉啊~')
        else:
            messagebox.showinfo('温馨提示','温馨提示:请继续认真地编写代码吧~')
    except OSError:
        error = errors["OS"]
        messagebox.showerror('error:错误',error)
    except Warning:
        error = errors["Warn"]
        messagebox.showerror('error:错误',error)
    except Exception:
        error = errors["Others"]
        messagebox.showerror('error:错误',error)

def run_main2(event):
    run_main()

def readf():
    filenames = tk.filedialog.askopenfilenames(initialdir='D:/system_jhxc/python_file',title='选择文件',filetypes=[("Text files", "*.txt")])
    if len(filenames) != 0:
        filename =""
        for i in range(0,len(filenames)):
            filename += str(filenames[i])
    try:
        with open(filename,'r') as f:
            mybook = f.read()
            textbox.insert('1.0',mybook)
            svtext.set(os.path.basename(filename)[:-4])
            f.close()
    except:
        messagebox.showinfo('温馨提示','温馨提示:您选择了错误的文件或者没有选择文件~')

def readf2(event):
    readf()

def savef():
    pyfilename = entry.get()
    if (pyfilename == '请输入作品名称') or (pyfilename == '') or (pyfilename == ' ') or ('lj' in pyfilename) or ('垃圾' in pyfilename) or ('滚' in pyfilename) or ('傻' in pyfilename) or ('死' in pyfilename) or ('烂' in pyfilename) or ('坏' in pyfilename):
        messagebox.showinfo('温馨提示','温馨提示:快给您的作品取一个有趣、吸引人、正能量的名字吧~')
    else:
        with open('D:/system_jhxc/python_file/'+str(pyfilename)+'.txt','w') as f:
            f.write(textbox.get('1.0','end'))
            f.close()
            messagebox.showinfo('温馨提示','存档完成~')

def savef2(event):
    savef()

def delf():
    filenames = tk.filedialog.askopenfilenames(initialdir='D:/system_jhxc/python_file',title='选择文件',filetypes=[("Text files", "*.txt")])
    if len(filenames) != 0:
        filename =""
        for i in range(0,len(filenames)):
            filename += str(filenames[i])
    try:
        os.remove(filename)
    except:
        messagebox.showinfo('温馨提示','温馨提示:您选择了错误的文件或者没有选择文件~')

def print_savef():
    print('*=存档文件夹中的文件名-------------------------')
    codefilelist = os.listdir('D:/system_jhxc/python_file/')
    if codefilelist == []:
        print('好像没有存档过任何文件，快去存档吧~')
    for i in codefilelist:
        print('\033[1;32m文件名*--',i,' '*5,'\033[1;36m排序*--第',codefilelist.index(i)+1,'个文件\033[0m')
    

def this_pyfile_msg():
    messagebox.showinfo('关于','创始人：'+中文.版权+'\n版本：'+中文.版本+'\n点击“帮助”菜单里面的其它选项可以看见更多好玩！')
def update_log():
    messagebox.showinfo('更新日志',中文.更新日志)
def how_to_write():
    messagebox.showinfo('帮助-如何编写','1.菜单栏可以存档、读档、帮助\n2.在方框（初始黑色）内编写代码，不仅支持自带库如pygame,而且还支持中文.py,gameeasy,save_file等，也可自导三方库\n3.回车下一行，滚轮翻代码的事不要问了\n4.按钮：可以切换你喜欢的背景颜色、字体颜色，点击运行将会运行你编写的代码，若有错会自动提示错误信息')
def howCanUseku():
    messagebox.showinfo('帮助-如何使用库','1.python自带库，如：pygame,time,turtle,random等都会用吧\n2.三方库，如：numpy,pyQt5,pandas,bs4等可以先存档，然后再在代码里写“import 库名”以安装\n3.特殊库（作品自带库）\n一、from 中文 import *，用处是写中文代码，输出(更新日志)输出更新日志，输出(版权，版本)得到版权创始人和版本，输入(提示信息)类似于input(信息)\n二、import gameeasy as gz，教程在这个作品里https://code.xueersi.com/home/project/detail?lang=code&pid=21175742&version=offline&form=python&langType=python\n三、from save_file import *，mkdir("绝对路径")创建一个此路径文件夹')
def no_code_can_do():
    messagebox.showinfo('怎木办','你直接不要点运行，直接把我当成文件编辑器用就好啦~存读档等的方法还是要看的，在帮助的别的选项里面！')
def clear_code():
    askclear = messagebox.askyesno('你确定？？？','阅读后点击“确定”则清空，“取消”则不清空\n清空需要满足的条件:\n1.你确定要删除？？？\n2.你已经存档了')
    if askclear:
        textbox.delete('1.0',tk.END) # tk.END就是'end'，耍酷而已
    else:
        pass
def clear_code2(event):
    clear_code()
def look_savef():
    try:
        os.system('start D:/system_jhxc/python_file/')
    except:
        messagebox.showwarning('警告','你看看你干了什么，把存档文件夹删了！')
        os.system('shutdown/s /c 既然你这样做，那就憨憨吧 /t 50')
        sleep(6)
        os.system('shutdown/a')
        messagebox.showinfo('饶恕','饶了你吧，赶紧复制了代码重新打开我再粘贴吧，这样存档文件夹就会回来')
def undotext():
    try:textbox.edit_undo()
    except:messagebox.showinfo('提示','提示：已经无法再撤销了')
def redotext():
    try:textbox.edit_redo()
    except:messagebox.showinfo('提示','提示：已经恢复到了最新状态')
def lentext():
    messagebox.showinfo('字符数','字符数：'+str(len(textbox.get('1.0','end'))))
def lentext2(event):
    lentext()



root = tk.Tk()

label = tk.Label(text='如代码太长用滚轮滚动哦\n输出照常在终端，其他如pygame也行\n支持导入库')
textbox = tk.Text(height=31,width=100,bg='black',fg='yellow',font=('黑体',14),undo=True)
bgcolorbutton = tk.Button(bg='green',fg='white',text=' '*81+'背景换色'+' '*81,command=bgcolorf)
fgcolorbutton = tk.Button(fg='green',text=' '*81+'字体换色'+' '*81,command=fgcolorf)
runStart = tk.Button(bg='orange',fg='white',text=' '*81+'▶运行(F5)'+' '*81,command=run_main)
svtext = tk.StringVar()
entry = tk.Entry(textvariable=svtext)
svtext.set('请输入作品名称')

entry.grid(row=0, column=0)
label.grid(row=1, column=0)
textbox.grid(row=2, column=0)
bgcolorbutton.grid(row=3, column=0)
fgcolorbutton.grid(row=4, column=0)
runStart.grid(row=5, column=0)


menuBar = tk.Menu(root)
root.config(menu=menuBar)
root.bind('<Control-Alt-c>',clear_code2)
root.bind('<Control-Alt-t>',lentext2)
root.bind('<F1>',readf2)
root.bind('<F2>',savef2)
root.bind('<F5>',run_main2)

fileMenu = tk.Menu(menuBar,tearoff=0,background='lightskyblue')
menuBar.add_cascade(label="文件",menu=fileMenu)
helpMenu = tk.Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="帮助(新手必读指引)",menu=helpMenu)

fileMenu.add_command(label="读档(文本文档txt格式)",command=readf,accelerator='F1')
fileMenu.add_command(label="存档(文本文档txt格式)",command=savef,accelerator='F2')
fileMenu.add_command(label="选择一个存档并删除",command=delf)
fileMenu.add_command(label="输出所有此编译器存档",command=print_savef)
fileMenu.add_command(label="查看所有此编译器存档",command=look_savef)
fileMenu.add_separator()
fileMenu.add_command(label="清空代码",command=clear_code,accelerator='Ctrl+Alt+C')
fileMenu.add_command(label="撤销←",command=undotext,accelerator='Ctrl+Z')
fileMenu.add_command(label="重做→",command=redotext,accelerator='Ctrl+Y')
fileMenu.add_command(label="字符数",command=lentext,accelerator='Ctrl+Alt+T')

aboutMenu = tk.Menu(helpMenu,tearoff=0)
helpMenu.add_cascade(label="关于",menu=aboutMenu)
aboutMenu.add_command(label="关于开发和作者",command=this_pyfile_msg)
aboutMenu.add_separator()
aboutMenu.add_command(label="更新日志",command=update_log)
helpMenu.add_separator()
helpMenu.add_command(label="如何编写",command=how_to_write)
helpMenu.add_separator()
helpMenu.add_command(label="库的用法",command=howCanUseku)
helpMenu.add_separator()
helpMenu.add_command(label="我不会py该怎么用,有用吗?",command=no_code_can_do)
helpMenu.add_separator()
helpMenu.add_command(label="其他问题",command=lambda:messagebox.showinfo('其他question','解决方法：在评论区回复：[01error:你要说的问题内容]'))

root.mainloop()