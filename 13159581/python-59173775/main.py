from tkinter import *
from tkinter import filedialog, messagebox,simpledialog
from tkinter import ttk
import idlelib.colorizer as idc
import idlelib.percolator as idp
import traceback
import os
import uploader as ul
import requests as r
from PIL import Image,ImageTk
import os
import keyboard
import threading

class CIDE:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("CIDE V1.5")
        self.tk.geometry("498x450+600+10")
        # self.tk.overrideredirect(True)
        # self.tk.attributes("-topmost",True)
        self.tk.iconphoto(False,PhotoImage(file=".\\icon.gif"))
        self.tk.protocol("WM_DELETE_WINDOW", self.callback)

        # self.title_frame = Frame(self.tk)
        # self.title_label = Label(self.title_frame,bg="grey",height=2,fg="lightgreen",text="CIDE　　  　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　")
        # self.title_label.grid(row=0,sticky=W)
        # self.title_label.bind("<B1-Motion>", self.move_window)
        # self.title_label.bind('<Button-1>', self.get_pos)
        # self.title_close = Button(self.title_frame,bg="grey",text="×",bd=0,font='blod',activebackground='#ff1e5e',activeforeground='white',fg="white",pady=3,command=self.callback,cursor='hand2',highlightthickness=0)
        # self.title_close.grid(row=0,sticky=E)
        # self.title_frame.pack()

        self.frame1 = Frame(self.tk)
        self.yscrollbar = Scrollbar(self.frame1)
        self.text = Text(self.frame1, height=23, width=500,font=(None,12))
        self.yscrollbar.pack(side=RIGHT, fill=Y)
        self.text.pack()
        self.yscrollbar.config(command=self.text.yview)
        self.text.insert(END, "print(\"Hello World!\")")
        self.configCodeHighlight(self.text)
        self.text.config(yscrollcommand=self.yscrollbar.set)
        self.frame1.pack()

        self.frame2 = Frame(self.tk)
        self.b1 = ttk.Button(self.frame2, width=300, text="运行", command=self.threadaaaa)
        self.b1.pack()

        ttk.Button(self.frame2, width=300, text="保存", command=self.save).pack()

        ttk.Button(self.frame2, width=300, text="打开", command=self.open).pack()

        self.frame2.pack()

    '''本地操作'''
    def configCodeHighlight(self,component: Text):
        idc.color_config(self.text)
        p = idp.Percolator(self.text)
        d = idc.ColorDelegator()
        p.insertfilter(d)
    def aaaa(self):
        
        # def hhhh():
        #     self.newprint("\n按回车关闭窗口")
        #     keyboard.add_hotkey('enter', self.frame3.destroy)
        def print(*value,sep=' ',end='\n'):
            self.outtext['state'] = 'normal'
            for i in range(len(value)):
                self.outtext.insert('end',value[i])
                if i < len(value)-1:
                    t.insert('end',sep)
            self.outtext.insert('end',end)
            self.outtext['state'] = 'disabled'
        def input(value=''):
            print(value,end='')
            is_function_finished = BooleanVar()
            is_function_finished.set(False)
            submittext = ""  
            def on_key_press(event):
                nonlocal is_function_finished
                nonlocal  submittext 
                text = event.widget
                # 获取当前光标位置
                line, column = map(int, text.index("insert").split('.'))
                # 获取当前行的内容
                current_line_content = text.get("{}.0".format(line), "{}.end".format(line))
                # 如果是Backspace按下且当前行为空，阻止删除
                if event.keysym == "BackSpace":
                    if (not current_line_content.strip().replace(value,"")):
                        return "break"
                    else:
                        submittext = submittext[:-1]
                        last_char_index = 'end-1c'
                        self.outtext.delete(last_char_index)
                elif event.keysym == "Return":
                    is_function_finished.set(True)
                else:
                    submittext += event.char
                    # self.outtext.insert('end', event.char)
            self.outtext['state'] = 'normal'

            self.outtext.bind("<Key>", on_key_press)
            # submittext = ''
            # submittype = 0
            # def submit(event):
            #     global submittext
            #     global submittype
            #     # 获取当前光标位置
            #     line_number = self.outtext.index("insert").split(".")[0]
            #     # 获取整行内容
            #     line_content = self.outtext.get("{}.0".format(line_number), "{}.end".format(line_number))
            #     submittext=line_content.replace(value,"")
            #     submittype=1
            #     self.outtext['state'] = 'disabled'
            # print(value)
            # self.outtext.bind("<Return>",submit)
            # while submittype==0:
            #     pass
            self.frame3.wait_variable(is_function_finished)
            self.outtext.unbind("<Key>")
            self.outtext["state"] = "disabled"
            return submittext

        self.frame3 = Toplevel(self.tk)
        self.frame3.geometry("500x230+0+200")
        
        # self.title_close.grid(row=0, sticky=E)
        # self.title_frame.pack()
        self.frame3.title("CIDE运行分窗口")
        self.yscrollbar2 = Scrollbar(self.frame3)
        self.outtext = Text(self.frame3,height=200,font=(False,14),bg="black",fg="white",insertbackground="white")
        self.outtext['state'] = 'disabled'
        self.yscrollbar2.pack(side=RIGHT, fill=Y)
        self.outtext.pack()
        self.yscrollbar2.config(command=self.outtext.yview)
        self.outtext.config(yscrollcommand=self.yscrollbar2.set)
        self.outtext['state'] = 'normal'
        self.outtext.delete('1.0', 'end')
        self.outtext['state'] = 'disabled'
        t = self.text.get(1.0, END)
        #t = t.replace('print','self.newprint').replace('input','self.newinput')
        try:
            # with open("D:\\maincode.py", "w", encoding="utf-8") as fn:
            #     fn.write(t + "\ninput(\"按回车退出\")")
            # os.system("start D:\\maincode.py")
            exec(t,globals(),locals())
        except Exception as b:
            bug = traceback.format_exc()
            print(bug)
        finally:
            #hhhh()
            try:
                self.frame3.mainloop()
            except:
                pass

    def threadaaaa(self):
        threading.Thread(target=self.aaaa).start()

    def save(self):
        try:
            t = self.text.get(1.0, END)
            f = filedialog.asksaveasfile(defaultextension=".py")
            f.write(t + "\ninput(\"按回车退出\")")
        except:
            messagebox.showinfo('提示', '保存失败')
        else:
            messagebox.showinfo('提示', '保存成功')
    def open(self):
        path = filedialog.askopenfilename(initialdir="C:\\")
        with open(path,"r",encoding="UTF-8") as file:
            self.text.delete("1.0", "end")
            self.text.insert(END,file.read())

    def get_pos(self,event):
        global xwin, ywin
        xwin = event.x
        ywin = event.y
    def move_window(self,event):
        self.tk.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')

    def move_window2(self,event):
        self.frame3.geometry(f'+{event.x_root - xwin}+{event.y_root - ywin}')

    def callback(self):
        if messagebox.askyesno('关闭', '您确定要关闭CIDE吗?'):
            self.tk.destroy()
            os._exit(200)
        else:
            pass


ide = CIDE()
ide.tk.mainloop()
