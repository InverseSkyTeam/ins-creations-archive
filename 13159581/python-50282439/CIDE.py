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
        self.tk.geometry("498x490+600+10")
        self.tk.overrideredirect(True)
        self.tk.attributes("-topmost",True)
        self.tk.iconphoto(False,PhotoImage(file=".\\icon.gif"))

        self.title_frame = Frame(self.tk)
        self.title_label = Label(self.title_frame,bg="grey",height=2,fg="lightgreen",text="CIDE　　  　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　")
        self.title_label.grid(row=0,sticky=W)
        self.title_label.bind("<B1-Motion>", self.move_window)
        self.title_label.bind('<Button-1>', self.get_pos)
        self.title_close = Button(self.title_frame,bg="grey",text="×",bd=0,font='blod',activebackground='#ff1e5e',activeforeground='white',fg="white",pady=3,command=self.callback,cursor='hand2',highlightthickness=0)
        self.title_close.grid(row=0,sticky=E)
        self.title_frame.pack()

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

        self.menub1 = ttk.Menubutton(self.frame2,text="                                                      保存文件",width=300)
        self.menub1.pack()
        self.menu = Menu(self.menub1,tearoff=False)
        self.menu.add_command(label="本地保存",command=self.save)
        self.menu.add_command(label="云端保存", command=self.cloud_save)
        self.menub1.config(menu=self.menu)

        self.b4 = ttk.Menubutton(self.frame2, text="                                                      打开文件", width=300)
        self.b4.pack()
        self.menu2 = Menu(self.b4, tearoff=False)
        self.menu2.add_command(label="本地代码打开", command=self.open)
        self.menu2.add_command(label="云端代码打开", command=self.cloud_run)
        self.b4.config(menu=self.menu2)

        self.frame2.pack()

    '''本地操作'''
    def configCodeHighlight(self,component: Text):
        idc.color_config(self.text)
        p = idp.Percolator(self.text)
        d = idc.ColorDelegator()
        p.insertfilter(d)
    def aaaa(self):
        def hhhh():
            self.newprint("\n按回车关闭窗口")
            keyboard.add_hotkey('enter', self.frame3.destroy)
        self.frame3 = Toplevel(self.tk)
        self.frame3.geometry("500x230+0+200")
        self.frame3.overrideredirect(True)
        self.title_frame = Frame(self.frame3)
        self.title_label = Label(self.title_frame, bg="grey", height=2, fg="lightgreen",
                                 text="CIDE运行分窗口　 　　　　　　　　　　　　 　　　　　　　　　　　　　　　　　　　　")
        self.title_label.grid(row=0, sticky=W)
        self.title_label.bind("<B1-Motion>", self.move_window2)
        self.title_label.bind('<Button-1>', self.get_pos)
        self.title_close = Button(self.title_frame, bg="grey", text="×", bd=0, font='blod', activebackground='#ff1e5e',
                                  activeforeground='white', fg="white", pady=3, command=self.frame3.destroy, cursor='hand2',
                                  highlightthickness=0)
        self.title_close.grid(row=0, sticky=E)
        self.title_frame.pack()
        self.frame3.title("CIDE运行分窗口")
        self.yscrollbar2 = Scrollbar(self.frame3)
        self.outtext = Text(self.frame3,height=200,font=(False,14),bg="black",fg="white")
        self.outtext['state'] = 'disabled'
        self.yscrollbar2.pack(side=RIGHT, fill=Y)
        self.outtext.pack()
        self.yscrollbar2.config(command=self.outtext.yview)
        self.outtext.config(yscrollcommand=self.yscrollbar2.set)
        self.outtext['state'] = 'normal'
        self.outtext.delete('1.0', 'end')
        self.outtext['state'] = 'disabled'
        t = self.text.get(1.0, END)
        t = t.replace('print','self.newprint').replace('input','self.newinput')
        try:
            # with open("D:\\maincode.py", "w", encoding="utf-8") as fn:
            #     fn.write(t + "\ninput(\"按回车退出\")")
            # os.system("start D:\\maincode.py")
            exec(t,globals(),locals())
        except Exception as b:
            bug = traceback.format_exc()
            bug = bug.replace('self.newprint','print').replace('self.newinput','input')
            try:
                self.newprint(bug)
            except:
                pass
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
        else:
            pass

    def newprint(self,*text,end='\n'):
        self.outtext['state'] = 'normal'
        for i in text:
            self.outtext.insert('end',i)
            self.outtext.insert('end',' ')
        self.outtext.insert('end',end)
        self.outtext['state'] = 'disabled'

    def newinput(self, text='', end='\n'):
        self.newprint(text, end='')
        askt = simpledialog.askstring(title=' ', prompt='输入')
        if askt == None:
            askt = ''
        return askt

    '''云端操作'''
    def cloud_save(self):
        def abcde():
            uploader = ul.XesUploader()
            path = "C:\\"+e2.get()+".py"
            f = open(path,"w")
            f.write(self.text.get(1.0,END))
            f.close()
            url = uploader.uploadAbsolutePath(path)
            ct.insert(END, "文件的路径是：" + url)
        top = Toplevel()
        label = Label(top,text="请输入要云端保存的文件名:")
        e2 = ttk.Entry(top)
        cb = ttk.Button(top,text="提交",command=abcde)
        ct = Text(top)
        label.pack()
        e2.pack()
        cb.pack()
        ct.pack()


    def cloud_run(self):
        def bbbbbbbb():
            try:
                url = e1.get()
                #print(url)
                head = {
                    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
                }
                res = r.get(url, headers=head)
                res.encoding = res.apparent_encoding
                self.text.delete("1.0", "end")
                self.text.insert(END, res.text)
            except:
                messagebox.showinfo(message="输入网址有误")
        get_url = Toplevel()
        get_url.geometry("200x100")
        Label(get_url,text="请输入文件路径:")
        e1 = ttk.Entry(get_url,width=150)
        e1.pack()
        Label(get_url,text="注意，云端打开有可能导致代码出错，请谨慎使用")
        ttk.Button(get_url,text="确认",command=bbbbbbbb).pack()

ide = CIDE()
ide.tk.mainloop()
