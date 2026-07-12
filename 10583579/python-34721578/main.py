from tkinter import filedialog, messagebox
import websocket
import json
import sys
import requests
from xes import uploader
from time import *
from PIL import Image, ImageTk
import tkinter as tk
# import random
# import os


class XesIde:  # 类名可以改一下
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

        def get_pos(event):
            global xwin, ywin
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
            fileMenu.post(root.winfo_x() + 55, root.winfo_y() + 40)

        def operation_button_down():
            operationMenu.post(root.winfo_x() + 55, root.winfo_y() + 80)

        def undotext():
            try:
                self.textbox.edit_undo()
            except:
                messagebox.showinfo('提示', '提示：已经撤销至最初状态')

        def redotext():
            try:
                self.textbox.edit_redo()
            except:
                messagebox.showinfo('提示', '提示：已经恢复至最新状态')

        def runcode(event=None):
            textcode = self.textbox.get('1.0', 'end')
            try:
                exec(textcode)
            except SyntaxError as e:
                error = str(e) + '\n' + errors["Syntax"]
                messagebox.showerror('发生错误', error)
            except TypeError as e:
                error = str(e) + '\n' + errors["Type"]
                messagebox.showerror('发生错误', error)
            except ValueError as e:
                error = str(e) + '\n' + errors["Value"]
                messagebox.showerror('发生错误', error)
            except NameError as e:
                error = str(e) + '\n' + errors["Name"]
                messagebox.showerror('发生错误', error)
            except AttributeError as e:
                error = str(e) + '\n' + errors["Attribute"]
                messagebox.showerror('发生错误', error)
            except (IndexError, KeyError) as e:
                error = str(e) + '\n' + errors["Index&Key"]
                messagebox.showerror('发生错误', error)
            except IndentationError as e:
                error = str(e) + '\n' + errors["IndentationError"]
                messagebox.showerror('发生错误', error)
            except ImportError as e:
                error = str(e) + '\n' + errors["ImportError"]
                messagebox.showerror('发生错误', error)
                question = messagebox.askyesno('问题', '是否安装此库？')
                if question:
                    lib = str(e).split(' ')[-1].split('\'')[1]
                    os.system('pip install ' + lib)
            except OSError as e:
                error = str(e) + '\n' + errors["OS"]
                messagebox.showerror('发生错误', error)
            except Warning as e:
                error = str(e) + '\n' + errors["Warn"]
                messagebox.showerror('发生错误', error)
            except RuntimeError as e:
                error = str(e) + '\n' + errors["Runtime"]
                messagebox.showerror('发生错误', error)
            except MemoryError as e:
                error = str(e) + '\n' + errors["Memory"]
                messagebox.showerror('发生错误', error)
            except ArithmeticError as e:
                error = str(e) + '\n' + errors["Calc"]
                messagebox.showerror('发生错误', error)
            except UnicodeError as e:
                error = str(e) + '\n' + errors["Encode"]
                messagebox.showerror('发生错误', error)
            except UnboundLocalError as e:
                error = str(e) + '\n' + errors["unfind"]
                messagebox.showerror('发生错误', error)
            except Exception as e:
                error = str(e) + '\n' + errors["Others"]
                messagebox.showerror('发生错误', error)
        def find_project():
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
            return dic
        def show():
            dic = find_project()
            for i in dic:
                exec(f"")
        def read_code(i,event=None):
            input_name.delete(0,tk.END)
            input_name.insert('0',i.split('/')[-1][:-3])
            self.textbox.delete('1.0','end')
            with open(i,'r',encoding='utf-8') as f:
                content = f.read()
            self.textbox.insert('end',content)
        def open_doc(event=None):
            self.filename = filedialog.askopenfilenames(defaultextension='.py',
                                                        filetypes=[("Python files", "*.py;*.pyw"), 
                                                                   ("All files", "*")])
            icon = ImageTk.PhotoImage(Image.open("python.png"))
            self.l = []
            for i in self.filename:
                p_name = i.split("/")[-1]
                self.l.append(tk.Label(self.project_area,text = p_name,compound= 'left',image = icon,bg="#2d2d2d",fg="white",font=("微软雅黑",10)))
                self.l[self.filename.index(i)].image = icon
                self.l[self.filename.index(i)].pack(pady=3)
            for i in self.l:
                i.bind_all('<Double-Button-1>',read_code(self.filename[self.l.index(i)]))
        # main
        back_ground = "#0a0a0a"

        root = tk.Tk()
        root.state('normal')
        root.overrideredirect(True)
        root.lift()
        root.attributes('-topmost', True)
        root.attributes('-topmost', False)

        root.geometry('1280x780+100+1')
        self.word = tk.StringVar()
        title_bar = tk.Frame(root, bg=back_ground, relief='ridge', bd=1, padx=0,
                             highlightcolor=back_ground,
                             highlightthickness=0)

        iconic_button = tk.Button(title_bar, text='—',  # text='︾',
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

        title_window = 'Python编辑器'
        title_name = tk.Label(title_bar, text=title_window, bg=back_ground, fg='white')
        input_name = tk.Entry(title_bar, textvariable=self.word, highlightcolor='Blue', highlightthickness=1, width=25)
        input_name.insert(0,"untitled")
        project_name = tk.Label(title_bar, text='作品名称 ', bg=back_ground, fg='white')
        icon = ImageTk.PhotoImage(Image.open("IXcodelogo.png"))
        title_icon = tk.Button(title_bar, bg=back_ground, image=icon,
                               bd=3, highlightthickness=0,
                               command=lambda: messagebox.showinfo('提示', '别捏我呀~'))

        window = tk.Frame(root, bg="#2d2d2d", highlightthickness=0)
        operation_area = tk.Frame(window, bg=back_ground, width=60)
        operation_area.pack(side='left', fill='y')
        # tk.Entry(tile_bar, textvariable=self.word, highlightcolor='Blue', highlightthickness=1, width=25).pack(side='top',fill='both')
        editing_area = tk.Frame(window, bg=back_ground)
        editing_area.pack(side='right')
        zhanwei = tk.Frame(window, bg="#2d2d2d", width=20).pack(side='left', fill='y')
        self.project_area = tk.Frame(window, bg="#2d2d2d", width=320)
        self.project_area.pack(side='left', fill='y')
        fileButton = tk.Button(operation_area, bg=back_ground,
                               fg='white', text='文件', bd=0,
                               font='bold', relief='sunken',
                               highlightthickness=0,
                               activebackground='lightskyblue',
                               activeforeground='blue',
                               command=file_button_down)
        fileButton.pack(side='top', fill='both')
        operationButton = tk.Button(operation_area, bg=back_ground,
                                    fg='white', text='操作', bd=0,
                                    font='bold', relief='sunken',
                                    highlightthickness=0,
                                    activebackground='lightgreen',
                                    activeforeground='black',
                                    command=operation_button_down)
        operationButton.pack(side='top', fill='both')
        fileMenu = tk.Menu(operation_area, tearoff=0, background='lightskyblue')
        fileMenu.add_command(label='运行[此功能正在完善]', command=runcode, accelerator='F5')
        fileMenu.add_command(label='从本地打开', command=open_doc, accelerator='Ctrl+O')
        fileMenu.add_command(label='保存到云端',command=self.save_in_cloud,accelerator='Ctrl+S')
        fileMenu.add_command(label='另存为',command=self.save_as,accelerator='Ctrl+Shift+S')
        operationMenu = tk.Menu(operation_area, tearoff=0, background='lightgreen')
        operationMenu.add_command(label='撤销', command=undotext, accelerator='Ctrl+Z')
        operationMenu.add_command(label='重做', command=redotext, accelerator='Ctrl+Y')
        sbar_y = tk.Scrollbar(editing_area)
        sbar_y.pack(side='right', fill='y')
        sbar_x = tk.Scrollbar(editing_area, orient=tk.HORIZONTAL)
        sbar_x.pack(side='bottom', fill='x')
        self.textbox = tk.Text(editing_area, height=26, width=60, bg='black', fg='white', font=('楷体', 20),
                          undo=True, wrap='none', insertbackground='lightskyblue',
                          yscrollcommand=sbar_y.set, xscrollcommand=sbar_x.set)
        self.textbox.insert("end", 'print("hello world")')
        self.textbox.pack()
        sbar_y.config(command=self.textbox.yview)
        sbar_x.config(command=self.textbox.xview)
        python_image = ImageTk.PhotoImage(Image.open("python.png"))
        self.project = tk.Label(self.project_area,text = self.word.get()+'.py',compound= 'left',image = python_image,bg="#2d2d2d",fg="white",font=("微软雅黑",10))
        self.project.image = python_image
        self.project.pack()

        title_bar.pack(fill='x')
        title_icon.pack(side='left')
        title_name.pack(side='left')
        close_button.pack(side='right')
        iconic_button.pack(side='right')
        input_name.pack(side='right')
        project_name.pack(side='right')
        window.pack(expand=True, fill='both')

        root.bind('<F5>', runcode)
        root.bind("<Control-s>", self.save_in_cloud)
        root.bind("<Control-o>", open_doc)
        root.bind("<Control-Shift-S>",self.save_as)
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
    
    def save_as(self,event=None):
        content,name = self.textbox.get("1.0",'end-1c'),self.word.get()
        savefilename = filedialog.asksaveasfilename(defaultextension='.py',
                                                    filetypes=[("Python files", "*.py;*.pyw"), ("Text files", "*.txt"),
                                                               ("All files", "*")])
        if savefilename != '':
            try:
                with open(savefilename, 'w', encoding='utf-8') as file:
                    file.write(content)
            except Exception as e:
                print(str(e))  # 方便查看错误
            else:
                print(strftime('[%Y-%m-%d %H:%M:%S]') + 'Save as file successful,path  ' + savefilename)
                messagebox.showinfo('提示', '代码文件成功导出至' + savefilename)
    def save_in_cloud(self,event=None):
        try:
            if time() - self.t > 5:
                content,name = self.textbox.get("1.0",'end-1c'),self.word.get()
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
                self.ws.close()
                self.t = time()
            else:
                print('每两次操作限制5秒间隔，请稍后再试，还需等待',round(5-time()+self.t,2),'秒')
        except Exception as e:
            print(e)
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
        print("代码:")
        print("".join(nrs.split("\r")))

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
    


IDE = XesIde()
#IDE.read_from_cloud(IDE.word.get())