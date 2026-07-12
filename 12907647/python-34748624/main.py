from tkinter import (messagebox,filedialog,simpledialog)
from PIL import (Image, ImageTk)
from time import *
import tkinter as tk
import subprocess
import traceback
import websocket
import requests
import uploader
import random
import shutil
import json
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

def newimport(modelname):
    errordict = {"wx":"wxPython","cv2":"opencv-python","win32api":"pywin32","win32gui":"pywin32","win32con":"pywin32","webview":"pywebview"}
    try:
        exec(f"import {modelname}")
        print("导入成功！")
    except:
        if modelname in errordict:
            modelname1 = errordict[modelname]
        else:
            modelname1 = modelname
        module_path =  os.path.expanduser("~/学而思直播/code/site-packages")
        mn_path = os.path.join(module_path, modelname1)
        subprocess.check_output([sys.executable, "-m", "pip", "uninstall", modelname1, "-y"])
        if os.path.exists(mn_path):
            shutil.rmtree(mn_path)
        print('开始安装')
        subprocess.check_output([sys.executable, "-m", "pip", "install", modelname1, "-t", module_path, "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"])
        exec(f"import {modelname}")
        print("安装成功！")

try:
    import pyautogui as pag
except:
    print('请稍等，正在安装pyautogui库...(大约需要20秒)')
    newimport('pyautogui')
    import pyautogui as pag
pyfilepath = os.path.expanduser("~/学而思直播/code/exe/IdealXesIDE/files").replace('\\','/')
mkdir(pyfilepath)



class XesIDE:
    '''本地服务'''
    def __init__(self):
        self.t = time()
        
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
        
        self.keyworddict = {
            '0':'#0626dc',
            '1':'#0626dc',
            '2':'#0626dc',
            '3':'#0626dc',
            '4':'#0626dc',
            '5':'#0626dc',
            '6':'#0626dc',
            '7':'#0626dc',
            '8':'#0626dc',
            '9':'#0626dc',
            'True':'orange',
            'False':'orange',
            'def':'cyan',
            'return':'cyan',
            'class':'cyan',
            'raise':'cyan',
            'assert':'cyan',
            'global':'cyan',
            'if':'cyan',
            'elif':'cyan',
            'else':'cyan',
            'while':'cyan',
            'break':'cyan',
            'continue':'cyan',
            'in':'cyan',
            'is':'cyan',
            'and':'orange',
            'or':'orange',
            'not':'orange',
            'import':'#010aff',
            'from':'#010aff',
            'nonlocal':'cyan',
            'async':'cyan',
            'del':'cyan',
            'try':'cyan',
            'except':'cyan',
            'finally':'cyan',
            'with':'orange',
            'as':'orange',
            'pass':'lightgreen',
            'lambda':'cyan',
            'for':'cyan',
            'await':'cyan',
            'yield':'cyan',
            'input':'grey',
            'int':'grey',
            'str':'grey',
            'float':'grey',
            'complex':'grey',
            'list':'grey',
            'tuple':'grey',
            'dict':'grey',
            'set':'grey',
            'apply':'grey',
            'ascii':'grey',
            'abs':'grey',
            'any':'grey',
            'all':'grey',
            'bin':'grey',
            'sorted':'grey',
            'len':'grey',
            'Exception':'red',
            'debugger':'red',
            'Error':'red',
            'NameError':'red',
            'SyntaxError':'red',
            'UnboundLocalError':'red',
            'UnicodeError':'red',
            'RuntimeError':'red',
            'ArithmeticError':'red',
            'MemoryError':'red',
            'Warning':'red',
            'OSError':'red',
            'TypeError':'red',
            'ValueError':'red',
            'IndexError':'red',
            'IndentationError':'red',
            'sys':'lightgreen',
            'system':'lightgreen',
            'os':'lightgreen',
            '.':'purple',
            '"':'green',
            '\'':'green',
            '+':'grey',
            '-':'grey',
            '*':'grey',
            '/':'grey',
            '//':'grey',
            '**':'grey',
            '%':'grey',
            '|':'grey',
            '&':'grey',
            '^':'grey',
            '@':'orange',
            'max':'grey',
            'min':'grey',
            'eval':'red',
            'exec':'red',
            'pow':'grey',
            'round':'grey',
            'print':'purple',
            'self':'#01ffac',
            'cls':'#01ffac',
            'match':'purple',
            'case':'purple',
        }
        
        def get_pos(event):
            global xwin,ywin
            xwin = event.x
            ywin = event.y
        
        def move_window(event):
            self.root.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')
        
        def change_on_hovering(event):
            self.close_button['bg'] = 'red'
            self.close_button['fg'] = 'lightgreen'
        
        def return_to_normal_state(event):
            self.close_button['bg'] = self.back_ground
            if self.back_ground == '#0a0a0a':
                self.close_button['fg'] = 'white'
            else:
                self.close_button['fg'] = 'black'
        
        def change_on_hovering2(event):
            self.iconic_button['bg'] = 'grey'
            self.iconic_button['fg'] = 'lightgreen'
        
        def return_to_normal_state2(event):
            self.iconic_button['bg'] = self.back_ground
            if self.back_ground == '#0a0a0a':
                self.iconic_button['fg'] = 'white'
            else:
                self.iconic_button['fg'] = 'black'
        
        def iconic_window():
            self.root.overrideredirect(False)
            self.root.state('iconic')
        
        def file_button_down():
            self.fileMenu.post(self.root.winfo_x()+70,self.root.winfo_y()+40)
        
        def operation_button_down():
            self.operationMenu.post(self.root.winfo_x()+70,self.root.winfo_y()+80)
        
        def config_button_down():
            self.configMenu.post(self.root.winfo_x()+70,self.root.winfo_y()+120)
        
        def undotext():
            try:self.textbox.edit_undo()
            except:messagebox.showinfo('提示','提示：已经撤销至最初状态')
        
        def redotext():
            try:self.textbox.edit_redo()
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
            self.textbox.delete('1.0','end')
        
        def insert_commentheader():
            self.textbox.insert('1.0',"# coding:utf-8\n'''\n作品名：一个有点憨的程序\n作者:编程游侠\n出品时间:"+strftime('%Y/%m/%d %H:%M:%S',localtime())+"\n版权:(c)Copyright. xxx工作室xxx 保留所有权利\n作品介绍:我写了个寂寞~\n质量:A+\n'''\n")
        
        def insert_commentline():
            self.textbox.insert('insert',"# comment codes\n")
        
        def insert_commenttext():
            self.textbox.insert('insert',"'''\ncomment codes\ncomment codes\ncomment codes\n'''\n")
        
        def insert_empty_lines():
            self.textbox.insert('insert',"\n\n\n")
        
        def insert_text_box():
            self.textbox.insert('insert',"'''\n+-------------------------+\n|1.需要处理bug            |\n|2.赶紧更新               |\n|3.                       |\n+-------------------------+\n'''\n")
        
        def insert_function():
            self.textbox.insert('insert',"def fun(param=True):\n    return param\n")
        
        def insert_variable():
            self.textbox.insert('insert',"variable = True\n")
        
        def insert_if():
            self.textbox.insert('insert',"if event:\n    pass\nelif event2:\n    pass\nelse:\n    pass\n")
        
        def insert_while():
            self.textbox.insert('insert',"while event:\n    pass\nfor i in lib:\n    print(i)\n")
        
        def insert_class():
            self.textbox.insert('insert',"class People(object):\n    def __init__(self,param=True):\n        self.name = param\n    def hello(self):\n        return 'hello,'+self.name+'!'\n")
        
        def change_theme():
            if self.back_ground == "#0a0a0a":
                self.back_ground = "white"
                title_name1['fg'] = 'black'
                self.back_ground = '#dadada'
                self.iconic_button['fg'] = 'black'
                self.close_button['fg'] = 'black'
                fileButton['fg'] = 'black'
                operationButton['fg'] = 'black'
                configButton['fg'] = 'black'
                self.window['bg'] = '#efefef'
                self.textbox['bg'] = 'white'
                self.textbox['fg'] = 'black'
                self.outbox['bg'] = 'white'
                self.outbox['fg'] = 'black'
                self.linebox['bg'] = '#cecece'
                self.linebox['fg'] = 'black'
            else:
                self.back_ground = "#0a0a0a"
                title_name1['fg'] = 'lightgreen'
                self.iconic_button['fg'] = 'white'
                self.close_button['fg'] = 'white'
                fileButton['fg'] = 'white'
                operationButton['fg'] = 'white'
                configButton['fg'] = 'white'
                self.window['bg'] = '#2d2d2d'
                self.textbox['bg'] = 'black'
                self.textbox['fg'] = 'white'
                self.outbox['bg'] = 'black'
                self.outbox['fg'] = 'white'
                self.linebox['bg'] = '#3e3e3e'
                self.linebox['fg'] = 'white'
            self.title_bar['bg'] = self.back_ground
            self.title_bar['highlightcolor'] = self.back_ground
            self.iconic_button['bg'] = self.back_ground
            self.close_button['bg'] = self.back_ground
            self.program_title['highlightbackground'] = self.back_ground
            title_name1['bg'] = self.back_ground
            title_name2['bg'] = self.back_ground
            title_name3['bg'] = self.back_ground
            title_icon['bg'] = self.back_ground
            operation_area['bg'] = self.back_ground
            editing_area['bg'] = self.back_ground
            fileButton['bg'] = self.back_ground
            operationButton['bg'] = self.back_ground
            configButton['bg'] = self.back_ground
        
        def change_alpha():
            alphavalue = simpledialog.askstring(title='设置',prompt='设置窗体透明度(0~1之间)')
            self.root.attributes('-alpha',alphavalue)
        
        
        
        def download_lib():
            dlname = simpledialog.askstring(title='下载第三方库',prompt='第三方库名称')
            print('正在下载'+dlname+'库...')
            try:
                newimport(dlname)
            except:
                print('安装失败!')
            else:
                print('安装安成!')
                try:
                    exec('import '+dlname)
                except:
                    print('导入失败')
                else:
                    print('导入无问题!')
                finally:
                    print('导入检测结束')
            finally:
                print('库检测结束')
        
        def runcode(event=None):
            self.outbox['state'] = 'normal'
            self.outbox.delete('1.0','end')
            self.outbox['state'] = 'disabled'
            textcode = self.textbox.get('1.0','end')
            textcode = textcode.replace('print','self.newprint').replace('input','self.newinput')
            try:
                exec(textcode,globals(),locals())
            except SyntaxError as e:
                error = str(e) + '\n' + errors["Syntax"]
                messagebox.showerror('发生错误',error)
                msg = '\n'*2+traceback.format_exc()
                self.newprint(msg)
            except TypeError as e:
                error = str(e) + '\n' + errors["Type"]
                messagebox.showerror('发生错误',error)
                msg = '\n'*2+traceback.format_exc()
                self.newprint(msg)
            except ValueError as e:
                error = str(e) + '\n' + errors["Value"]
                messagebox.showerror('发生错误',error)
                msg = '\n'*2+traceback.format_exc()
                self.newprint(msg)
            except NameError as e:
                error = str(e) + '\n' + errors["Name"]
                messagebox.showerror('发生错误',error)
                msg = '\n'*2+traceback.format_exc()
                self.newprint(msg)
            except AttributeError as e:
                error = str(e) + '\n' + errors["Attribute"]
                messagebox.showerror('发生错误',error)
                msg = '\n'*2+traceback.format_exc()
                self.newprint(msg)
            except (IndexError, KeyError) as e:
                error = str(e) + '\n' + errors["Index&Key"]
                messagebox.showerror('发生错误',error)
                msg = '\n'*2+traceback.format_exc()
                self.newprint(msg)
            except IndentationError as e:
                error = str(e) + '\n' + errors["IndentationError"]
                messagebox.showerror('发生错误',error)
                msg = '\n'*2+traceback.format_exc()
                self.newprint(msg)
            except ImportError as e:
                msg = '\n'*2+traceback.format_exc()
                self.newprint(msg)
                error = str(e) + '\n' + errors["ImportError"]
                messagebox.showerror('发生错误',error)
                question = messagebox.askyesno('问题','是否安装此库？')
                if question:
                    lib = str(e).split(' ')[-1].split('\'')[1]
                    try:
                        newimport(lib)
                    except:
                        messagebox.showwarning('警告','安装失败')
            except OSError as e:
                error = str(e) + '\n' + errors["OS"]
                messagebox.showerror('发生错误',error)
                msg = '\n'*2+traceback.format_exc()
                self.newprint(msg)
            except Warning as e:
                error = str(e) + '\n' + errors["Warn"]
                messagebox.showerror('发生错误',error)
                msg = '\n'*2+traceback.format_exc()
                self.newprint(msg)
            except RuntimeError as e:
                error = str(e) + '\n' + errors["Runtime"]
                messagebox.showerror('发生错误',error)
                msg = '\n'*2+traceback.format_exc()
                self.newprint(msg)
            except MemoryError as e:
                error = str(e) + '\n' + errors["Memory"]
                messagebox.showerror('发生错误',error)
                msg = '\n'*2+traceback.format_exc()
                self.newprint(msg)
            except ArithmeticError as e:
                error = str(e) + '\n' + errors["Calc"]
                messagebox.showerror('发生错误',error)
                msg = '\n'*2+traceback.format_exc()
                self.newprint(msg)
            except UnicodeError as e:
                error = str(e) + '\n' + errors["Encode"]
                messagebox.showerror('发生错误',error)
                msg = '\n'*2+traceback.format_exc()
                self.newprint(msg)
            except UnboundLocalError as e:
                error = str(e) + '\n' + errors["unfind"]
                messagebox.showerror('发生错误',error)
                msg = '\n'*2+traceback.format_exc()
                self.newprint(msg)
            except Exception as e:
                error = str(e) + '\n' + errors["Others"]
                messagebox.showerror('发生错误',error)
                msg = '\n'*2+traceback.format_exc()
                self.newprint(msg)
        
        def callback():
            if messagebox.askyesno('关闭','您确定要关闭[IdealXes IDE]吗?'):
                self.root.destroy()
            else:
                pass
        
        # main
        self.back_ground = "#0a0a0a"
        
        self.root = tk.Tk()
        self.root.state('normal')
        self.root.overrideredirect(True)
        self.root.attributes('-topmost',True)
        self.root.geometry('1280x780+100+11')
        
        self.root.after(10,self.ff)
        
        self.title_bar = tk.Frame(self.root, bg=self.back_ground, relief='ridge', bd=1, padx=0,
                             highlightcolor=self.back_ground, 
                             highlightthickness=0)
        
        self.iconic_button = tk.Button(self.title_bar, text='—', # text='︾',
                                  bg=self.back_ground, padx=5, pady=3,
                                  bd=0, font='bold', fg='white',
                                  activebackground='lightskyblue',
                                  activeforeground='white',
                                  highlightthickness=0,
                                  cursor='hand2',
                                  command=iconic_window)
        
        self.close_button = tk.Button(self.title_bar, text='×',
                                 bg=self.back_ground, padx=5, pady=3, 
                                 bd=0, font='bold', fg='white',
                                 activebackground='#ff1e5e',
                                 activeforeground='white', 
                                 highlightthickness=0,
                                 cursor='hand2',
                                 command=callback)
        
        title_name1 = tk.Label(self.title_bar,text='IdealXes',font=('楷体',11,'bold'),bg=self.back_ground,fg='lightgreen')
        title_name2 = tk.Label(self.title_bar,text='IDE',font=('楷体',11,'bold'),bg=self.back_ground,fg='orange')
        title_name3 = tk.Label(self.title_bar,text='Version 1.1正式版',font=('楷体',11,'bold'),bg=self.back_ground,fg='#ff5166')
        self.icon = ImageTk.PhotoImage(Image.open("IXcodelogo.png"))
        title_icon = tk.Button(self.title_bar,bg=self.back_ground,image=self.icon,
                               bd=3,highlightthickness=0,cursor='hand2',
                               command=lambda:messagebox.showinfo('提示','IdealXes项目\n版权：\n参与人物：\n吴宇航\n小轩\n何嘉晨\n冀厚锦\n富兰克林\n袁梓轩\n等\n参与团队：\n逆天工作室\n参考文献不少于6000条\n版权所有，侵权必究'))
        
        self.window = tk.Frame(self.root,bg="#2d2d2d",highlightthickness=0)
        operation_area = tk.Frame(self.window,bg=self.back_ground,width=60)
        operation_area.pack(side='left',fill='y')
        self.stringvar = tk.StringVar(value='请输入作品名称')
        self.program_title = tk.Entry(self.window,highlightcolor='lightgreen',highlightbackground=self.back_ground,highlightthickness=2,textvariable=self.stringvar,width=50)
        self.program_title.pack(side='top')
        out_area = tk.Frame(self.window,bg=self.back_ground)
        out_area.pack(side='right')
        editing_area = tk.Frame(self.window,bg=self.back_ground)
        editing_area.pack(side='right')
        
        fileButton = tk.Button(operation_area,bg=self.back_ground,
                               fg='white',text='文件',bd=0,
                               font=('楷体',18,'bold'),relief='sunken',
                               highlightthickness=0,
                               activebackground='lightskyblue',
                               activeforeground='blue',
                               cursor='hand2',
                               command=file_button_down)
        fileButton.pack(side='top',fill='both')
        operationButton = tk.Button(operation_area,bg=self.back_ground,
                               fg='white',text='操作',bd=0,
                               font=('楷体',18,'bold'),relief='sunken',
                               highlightthickness=0,
                               activebackground='lightgreen',
                               activeforeground='green',
                               cursor='hand2',
                               command=operation_button_down)
        operationButton.pack(side='top',fill='both')
        configButton = tk.Button(operation_area,bg=self.back_ground,
                               fg='white',text='设置',bd=0,
                               font=('楷体',18,'bold'),relief='sunken',
                               highlightthickness=0,
                               activebackground='lightyellow',
                               activeforeground='#8e7437',
                               cursor='hand2',
                               command=config_button_down)
        configButton.pack(side='top',fill='both')
        self.fileMenu = tk.Menu(operation_area,tearoff=0,background='lightskyblue')
        self.fileMenu.add_command(label='运行',command=runcode,accelerator='F5')
        self.fileMenu.add_command(label='保存到云端',command=self.save_in_cloud,accelerator='Ctrl+S')
        self.fileMenu.add_command(label='保存到本地',command=self.save_as,accelerator='Ctrl+Shift+S')
        self.fileMenu.add_command(label='从云端打开',command=self.open_cloud,accelerator='Ctrl+O')
        self.fileMenu.add_command(label='从本地打开',command=self.open_from_local,accelerator='Ctrl+Shift+O')
        self.operationMenu = tk.Menu(operation_area,tearoff=0,background='lightgreen')
        self.operationInsertMenu = tk.Menu(self.operationMenu,tearoff=0,background='green',foreground='white')
        self.operationInsertMenu.add_command(label='作品注释头',command=insert_commentheader)
        self.operationInsertMenu.add_command(label='注释代码行',command=insert_commentline)
        self.operationInsertMenu.add_command(label='注释代码段',command=insert_commenttext)
        self.operationInsertMenu.add_command(label='空行代码段',command=insert_empty_lines)
        self.operationInsertMenu.add_command(label='文本框',command=insert_text_box)
        self.operationInsertMenu.add_separator()
        self.operationInsertMenu.add_command(label='函数',command=insert_function)
        self.operationInsertMenu.add_command(label='变量',command=insert_variable)
        self.operationInsertMenu.add_command(label='分支语句',command=insert_if)
        self.operationInsertMenu.add_command(label='循环语句',command=insert_while)
        self.operationInsertMenu.add_command(label='类',command=insert_class)
        self.operationMenu.add_cascade(label='插入...',menu=self.operationInsertMenu)
        self.operationMenu.add_separator()
        self.operationMenu.add_command(label='全选',command=copytext,accelerator='Ctrl+A')
        self.operationMenu.add_command(label='剪切',command=cuttext,accelerator='Ctrl+X')
        self.operationMenu.add_command(label='复制',command=copytext,accelerator='Ctrl+C')
        self.operationMenu.add_command(label='粘贴',command=pastetext,accelerator='Ctrl+V')
        self.operationMenu.add_command(label='撤销',command=undotext,accelerator='Ctrl+Z')
        self.operationMenu.add_command(label='重做',command=redotext,accelerator='Ctrl+Y')
        self.operationMenu.add_command(label='清空',command=clear_all,accelerator='Ctrl+DEL')
        self.configMenu = tk.Menu(operation_area,tearoff=0,background='lightyellow')
        self.configMenu.add_command(label='切换主题',command=change_theme)
        self.configMenu.add_command(label='设置透明度',command=change_alpha)
        self.configMenu.add_command(label='下载第三方库',command=download_lib)
        
        self.sbar_y = tk.Scrollbar(editing_area)
        self.sbar_y.pack(side='right',fill='y')
        self.sbar_x = tk.Scrollbar(editing_area,orient=tk.HORIZONTAL)
        self.sbar_x.pack(side='bottom',fill='x')
        self.linebox = tk.Text(editing_area,height=30,width=5,bg='#3e3e3e',fg='white',font=('楷体',17),insertbackground='#3e3e3e',cursor='arrow')
        self.linebox.pack(side='left',fill='y')
        self.textbox = tk.Text(editing_area,height=30,width=50,bg='black',fg='white',font=('楷体',17),
                          undo=True,wrap = 'none',insertbackground='lightskyblue',
                          yscrollcommand=self.sbar_y.set,xscrollcommand=self.sbar_x.set)
        self.textbox.pack(side='right',fill='y')
        self.sbar_y.config(command=self.textbox.yview)
        self.sbar_x.config(command=self.textbox.xview)
        self.counttext()
        
        for i in self.keyworddict:
            self.textbox.tag_config(i,foreground=self.keyworddict[i])
        
        self.sbar_y2 = tk.Scrollbar(out_area)
        self.sbar_y2.pack(side='right',fill='y')
        self.outbox = tk.Text(out_area,height=30,width=40,bg='black',fg='white',font=('楷体',17),yscrollcommand=self.sbar_y2.set,state='disabled')
        self.outbox.pack(side='left',fill='y')
        self.sbar_y2.config(command=self.outbox.yview)
        
        self.title_bar.pack(fill='x')
        title_icon.pack(side='left')
        title_name1.pack(side='left')
        title_name2.pack(side='left')
        title_name3.pack(side='left')
        self.close_button.pack(side='right')
        self.iconic_button.pack(side='right')
        self.window.pack(expand=True, fill='both')
        
        self.root.bind('<Key>',self.counttext)
        self.root.bind('<Control-v>',self.counttext)
        self.root.bind('<Control-s>', self.save_in_cloud)
        self.root.bind('<Control-S>', self.save_as)
        self.root.bind('<Control-o>', self.open_cloud)
        self.root.bind('<Control-O>', self.open_from_local)
        self.root.bind('<Button-1>',self.counttext)
        self.root.bind('<MouseWheel>',self.counttext)
        self.root.bind('<B1-Motion>',self.counttext)
        self.root.bind('<F5>',runcode)
        self.root.bind('<Control-Delete>',clear_all)
        self.title_bar.bind('<B1-Motion>', move_window)
        self.title_bar.bind('<Button-1>', get_pos)
        self.close_button.bind('<Enter>', change_on_hovering)
        self.close_button.bind('<Leave>', return_to_normal_state)
        self.iconic_button.bind('<Enter>', change_on_hovering2)
        self.iconic_button.bind('<Leave>', return_to_normal_state2)
        
        self.root.protocol("WM_DELETE_WINDOW", callback)
    
    def run(self):
        while True:
            try:
                self.to_overrideredirect_window()
                self.root.update()
            except:
                break
    
    def to_overrideredirect_window(self):
        if self.root.state() == 'normal':
            self.root.overrideredirect(True)
        else:
            self.root.overrideredirect(False)
    
    def counttext(self,event=None):
        lines = self.textbox.get('1.0','end').count('\n')
        lines = '\n'.join([str(i) for i in list(range(round(lines*self.sbar_y.get()[0])+1,round(lines*self.sbar_y.get()[1]+1)))])
        self.linebox.delete('1.0','end')
        self.linebox.insert('1.0',lines)
    
    def newprint(self,*text,end='\n'):
        self.outbox['state'] = 'normal'
        for i in text:
            self.outbox.insert('end',i)
            self.outbox.insert('end',' ')
        self.outbox.insert('end',end)
        self.outbox['state'] = 'disabled'
    
    def newinput(self,text='',end='\n'):
        self.newprint(text,end='')
        askt = simpledialog.askstring(title=' ',prompt='输入')
        if askt == None:
            askt = ''
        self.newprint('<Input:"'+askt+'">')
        return askt
    
    def search(self,t,w,tag):
        pos = '1.0'
        while True:
            idx = t.search(w, pos, 'end')
            if not idx:
                break
            pos = '{}+{}c'.format(idx, len(w))
            t.tag_add(tag, idx, pos)
    
    def ff(self):
        for i in self.keyworddict:
            self.textbox.tag_remove(i,'1.0','end')
            self.search(self.textbox, i, i)
        self.root.after(10,self.ff)
    
    def save_as(self,event=None):
        content,name = self.textbox.get("1.0",'end-1c'),self.program_title.get()
        savefilename = filedialog.asksaveasfilename(initialdir=pyfilepath,initialfile=name,title='另存为',defaultextension='.py',filetypes=[("Python files", "*.py;*.pyw"), ("Text files", "*.txt"),("所有文件", "*")])
        if savefilename != '':
            try:
                with open(savefilename, 'w', encoding='utf-8') as file:
                    file.write(content)
                    file.close()
            except Exception as e:
                print(str(e))  # 方便查看错误
            else:
                print(strftime('[%Y-%m-%d %H:%M:%S]')+'\nSave as file successful\npath:'+savefilename)
                print('代码文件成功导出至'+savefilename)
    
    def open_from_local(self,event=None):
        if messagebox.askokcancel('从云端打开','选择文件后，内容将会覆盖当前代码\n确定要这样做么？'):
            openfilename = filedialog.askopenfilenames(initialdir=pyfilepath,title='另存为',defaultextension='.py',filetypes=[("Python files", "*.py;*.pyw"), ("Text files", "*.txt"),("所有文件", "*")])[0]
            if openfilename != '':
                with open(openfilename, 'r', encoding='utf-8') as file:
                    openfilecontent = file.read()
                    file.close()
                self.textbox.delete('1.0','end')
                self.textbox.insert('1.0',openfilecontent)
                self.stringvar.set(openfilename.split('/')[-1].split('.')[0])
    
    
    
    '''云端服务'''
    def save_in_cloud(self,event=None):
        if self.program_title.get() == '':
            messagebox.showinfo('提示','标题不能为空')
            return False
        if '&' in self.program_title.get():
            messagebox.showinfo('提示','标题中不能含有特殊符号“&”。(可用and | / \ 、 和 与 同 等代表)')
            return False
        try:
            if time() - self.t > 5:
                content,name = self.textbox.get("1.0",'end-1c'),self.program_title.get()
                # project_id=20553603
                with open(name + ".txt", "w", encoding="utf-8") as f:
                    f.write(content)
                f.close()
                self.ws = websocket.create_connection('wss://api.xueersi.com/codecloudvariable/ws:80', timeout=5)
                # 使用云端存档
                myuploader = uploader.XesUploader()
                hashtext = myuploader.upload(name + ".txt").replace("https://livefile.xesimg.com/programme/python_assets/",
                                                                    "").replace(".txt", "")
                for n in range(1, 6):
                    c = eval('{"method":"set","user":' + '"' + str(
                        self.get_id()) + '"' + ',"project_id":"20553603","name":"☁ ' + name + str(
                        n) + '",' + '"value"' + ':' + str(n) + str(int(hashtext, 16))[(n - 1) * 8:n * 8] + "}")
                    self.ws.send(json.dumps(c))  # 转json并上传#这里因为数据太大会被xes取近似数所以截断存储，懒得写那么多字典，所以直接eval
                    # print(self.ws.recv())
                self.ws.close()
                self.t = time()
                messagebox.showinfo('提示','保存成功')
                return True
            else:
                messagebox.showinfo('提示','每两次操作限制10秒间隔，请稍后再试，还需等待'+str(round(10-time()+self.t,2))+'秒')
        except Exception as e:
            print(e)
        return False
    
    def read_from_cloud(self, filename):
        message = {
            "method": "handshake",
            "user": str(self.get_id()),
            "project_id": "20553603"  # 填作品id
        }
        ws = websocket.create_connection(f'wss://api.xueersi.com/codecloudvariable/ws:80', timeout=30)
        dic = {}
        while True:
            ws.send(json.dumps(message))
            r = ws.recv()
            value = str(json.loads(r)['value'])
            name = str(json.loads(r)['name'])
            if name in dic:
                break
            dic[name] = value
        value1 = dic[f"\u2601 {filename}1"][1:]
        value2 = dic[f"\u2601 {filename}2"][1:]
        value3 = dic[f"\u2601 {filename}3"][1:]
        value4 = dic[f"\u2601 {filename}4"][1:]
        value5 = dic[f"\u2601 {filename}5"][1:]
        nr = value1 + value2 + value3 + value4 + value5
        nr = hex(int(nr))[2:]
        head1 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        }
        zh = nr
        response = requests.get("https://livefile.xesimg.com/programme/python_assets/" + zh + ".txt",
                                headers=head1).content
        nrs = response.decode("utf-8")
        return "".join(nrs.split("\r"))
    
    def open_cloud(self,event=None):
        t = self.program_title.get()  # "t" is title
        if messagebox.askokcancel('从云端打开','即将根据您输入的作品名('+t+')读取内容\n内容将会覆盖当前代码\n确定要这样做么？'):
            try:
                t = self.read_from_cloud(t)  # "t" is text
            except:
                messagebox.showinfo('提示','没有这个作品啦~\nㄟ( ▔_ ▔ )ㄏ')
                return False
            else:
                self.textbox.delete('1.0','end')
                self.textbox.insert('1.0',t)
                self.counttext()
                return True
        else:
            return False
    
    # 获取cookie
    def get_cookies(self):
        cookies = ""
        if len(sys.argv) > 1:
            try:
                cookies = json.loads(sys.argv[1])["cookies"]
            except:
                print("未登录")
                sys.exit(0)
        return cookies
    
    # 爬取你的id
    def get_id(self):
        cookie = self.get_cookies()
        id = ''
        for i in cookie.split(";"):
            id = i[8:] if i[1:7] == "stu_id" else id
        return id

ide = XesIDE()
ide.run()