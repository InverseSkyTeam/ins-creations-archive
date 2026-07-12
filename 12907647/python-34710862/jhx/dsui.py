from tkinter import messagebox
import tkinter as tk,sys
name = 'INS jhx DreamSky simple easy GUI maker-V0.09'

def nonefunction():
    pass

class DreamSkyUI_Error(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return str(self.msg)

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.setup()
    def setup(self,title='DSUI Window',site='100,50',size='800,600',bg='#4e4e4e',movefront=True):
        self.title = title
        self.site = site.split(',')
        self.size = size.split(',')
        self.bgcolor = bg
        self.root.title(self.title)
        self.root.geometry(self.size[0]+'x'+self.size[1]+'+'+self.site[0]+'+'+self.site[1])
        self.root.configure(background=self.bgcolor)
        self.movefront()
    def setatt(self,style,value):
        self.root.attributes('-'+style,value)
    def movefront(self):
        self.lift()
        self.setatt('topmost',True)
        self.setatt('topmost',False)
    def lift(self):
        self.root.lift()
    def loop(self,tp='keep'):
        if tp == 'keep':
            self.root.mainloop()
        elif tp == 'new':
            try:
                self.root.update()
            except:
                sys.exit()
        else:
            raise DreamSkyUI_Error('apploop 函数的tp参数必须是字符串keep或者new')

class TextLabel(tk.Label):
    def __init__(self,app,text='标签',bg='#4e4e4e',fg='white',font=('楷体',18),bd=3,height=0,width=0,cursor='arrow',relief='flat'):
        try:
            self.approot = app.root
        except:
            self.approot = app
        super().__init__(self.approot,text=text,bg=bg,fg=fg,font=font,bd=bd,height=height,width=width,cursor=cursor,relief=relief)
        self.pack()

class Button(tk.Button):
    def __init__(self,app,text='按钮',bg='black',fg='white',font=('楷体',18),bd=3,height=0,width=0,command=nonefunction,relief='raised',state='normal',activebackground='lightgreen',activeforeground='black'):
        try:
            self.approot = app.root
        except:
            self.approot = app
        super().__init__(self.approot,text=text,bg=bg,fg=fg,font=font,bd=bd,height=height,width=width,command=command,relief=relief,state=state,activebackground=activebackground,activeforeground=activeforeground)
        self.pack()

class Entry(tk.Entry):
    def __init__(self,app,bg='white',fg='black',font=('楷体',18),bd=3,width=15,relief='sunken',exselect=True,insertbackground='blue',cursor=None,justify='left',show=None):
        try:
            self.approot = app.root
        except:
            self.approot = app
        super().__init__(self.approot,bg=bg,fg=fg,font=font,bd=bd,width=width,relief=relief,exportselection=exselect,insertbackground=insertbackground,cursor=cursor,justify=justify,show=show)
        self.pack()

class TextBox(tk.Text):
    def __init__(self,app,bg='white',fg='black',text='文本',font=('楷体',18),bd=3,width=15,height=10,relief='sunken',undo=True,wrap='char',cursor=None,state='normal',yscrollcommand=None,xscrollcommand=None):
        try:
            self.approot = app.root
        except:
            self.approot = app
        super().__init__(self.approot,bg=bg,fg=fg,font=font,bd=bd,width=width,height=height,relief=relief,undo=undo,wrap=wrap,cursor=cursor,state=state,yscrollcommand=yscrollcommand,xscrollcommand=xscrollcommand)
        self.insert('1.0',text)
        self.pack()
    def clear_all(self):
        self.delete(1.0, 'end')

class Frame(tk.Frame):
    def __init__(self,app,bg='grey',bd=3,width=300,height=200,relief='sunken',cursor=None):
        try:
            self.approot = app.root
        except:
            self.approot = app
        super().__init__(self.approot,bg=bg,bd=bd,width=width,height=height,relief=relief,cursor=cursor)
        self.pack()