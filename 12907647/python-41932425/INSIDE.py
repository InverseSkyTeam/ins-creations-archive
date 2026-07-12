from tkinter import (messagebox,filedialog,ttk)
from keywords import *
from time import *
import tkinter as tk
import threading
import random
import sys
import os

root = tk.Tk()
root.geometry('1200x700+50+20')
root.configure(background='#444444')
root.title('INS-IDE α-5.5 智造框架 |Made In CHINA|')
root.resizable(0,0)

LeftFrame = tk.Frame(root,bg='#111111',width=100)
LeftFrame.pack(side='left',fill='y')
RightFrame = tk.Frame(root)
RightFrame.pack(side='right',fill='y')
MiddleFrame = tk.Frame(root,bg='grey')
MiddleFrame.pack(side='right',fill='both',expand=True)
InFrame1 = tk.Frame(MiddleFrame,bg='grey')
InFrame1.pack(fill='both',expand=True)
# InFrame2 = tk.Frame(MiddleFrame,bg='grey')
EasyEditFrame = tk.Frame(RightFrame)
EasyEditFrame.pack(fill='x',side='top')
CodeEditFrame = tk.Frame(RightFrame,bg='#dddddd')
CodeEditFrame.pack(fill='x',side='bottom')
LineBox = tk.Text(CodeEditFrame,width=5,height=30,
                  font=('楷体',15),bg='#ffeca9',
                  state='disable')
LineBox.grid(row=0,column=0)
CodeEditBox = tk.Text(CodeEditFrame,width=75,height=30,
                      font=('楷体',15),undo=True,wrap='none',
                      bg='#e6fff9')
CodeEditBox.grid(row=0,column=1)

tk.Label(InFrame1,text='输入标题(title)',width=32,border=1,bg='#fff8e9').pack()
tediter = tk.Entry(InFrame1,width=32,bg='#dfffe1')
tediter.pack()
tk.Label(InFrame1,text='\n',width=32,bg='grey').pack()
tk.Label(InFrame1,text='选择语言(languge)',width=32,border=3,bg='#fff8e9').pack()
LanCombo = ttk.Combobox(InFrame1,value=codetypelist,width=30,state='readonly')
LanCombo.set(codetypelist[0])
LanCombo.pack()
tk.Label(InFrame1,text='\n',width=32,bg='grey').pack()
tk.Label(InFrame1,text='输入数据(stdin)',width=32,border=2,bg='#fff8e9').pack()
SmallTextFrame = tk.Frame(InFrame1)
SmallTextFrame.pack()
StdinText = tk.Text(SmallTextFrame,width=30,height=10,bg='#dfffe1')
StdinText.pack(side='left',fill='both')
StdinTextys = tk.Scrollbar(SmallTextFrame)
StdinTextys.pack(side='right',fill='y')
StdinTextys.config(command=StdinText.yview)
StdinText.config(yscrollcommand=StdinTextys.set)
TextcountLabel = tk.Label(InFrame1,font=('楷体',13),bg='grey',fg='white')
TextcountLabel.pack()
TextcountLabel2 = tk.Label(InFrame1,font=('楷体',13),bg='grey',fg='white')
TextcountLabel2.pack()

codeedit_yscrollbar = tk.Scrollbar(CodeEditFrame,orient='vertical')
codeedit_xscrollbar = tk.Scrollbar(CodeEditFrame,orient='horizontal')
codeedit_yscrollbar.grid(row=0,column=2,sticky=tk.N+tk.S)
codeedit_xscrollbar.grid(row=1,column=1,sticky=tk.E+tk.W)
codeedit_yscrollbar.config(command=CodeEditBox.yview)
codeedit_xscrollbar.config(command=CodeEditBox.xview)
CodeEditBox.config(yscrollcommand=codeedit_yscrollbar.set)
CodeEditBox.config(xscrollcommand=codeedit_xscrollbar.set)

tmp = r'''# Code Block Id: 1
# Code Line: 11
import random as r
print(666,"Hello World!",end="\t")
print(r.randint(1,100),True)
name = input('What\'s your name?')
print('Hi,'+str(name)+'!')
if name == 'ins小轩':
    print('欢迎大佬!!!',666,sep='  ')
print()
print('test-end')'''
CodeEditBox.insert('1.0',tmp)

def callback():
    global rwid
    if len(CodeEditBox.get('1.0','end')) <= 30:   # 氵作/测试/玩玩的直接关闭
        root.destroy()
        return
    if rwid > 1900:
        to_close_info = '''感谢您本次的使用，您即将退出INS-IDE!
若保存好了代码，即可点击[是]退出/重启IDE，若未保存完毕，请点击[否]先保存，否则代码将会丢失!
编程愉快!'''
    else:
        to_close_info = '''您即将退出INS-IDE!
请您再次确认一遍，是否要退出？
若要退出，点击[是]，否则点击[否]
如果您真的要退出，请保存代码再走，否则下次来的时候代码将会丢失!
编程愉快!'''
    to_close = messagebox.askyesno('是否离开',to_close_info)
    if to_close:
        root.destroy()
    # else:
    #     return to_close

for i in keydict:
    CodeEditBox.tag_config(i,foreground=keydict[i])
strws = 0
strws2 = 0

def search(t,w,tag):
    global strw,strws,strws2,stringlist,numberlist
    pos = '1.0'
    while True:
        idx = t.search(w, pos, 'end')
        if not idx:
            break
        pos = '{}+{}c'.format(idx,len(w))
        left = '{}-1c'.format(idx)
        right = '{}+{}c'.format(idx,len(w)+1)
        if (t.get(left,idx) in symbolshowlist) and (t.get(pos,right) in symbolshowlist):
            t.tag_add(tag, idx, pos)
        if w in symbolshowlist:
            if w in ['"',"'"]:
                if t.get(left,idx) == '\\':
                    continue
                try:
                    idx2 = t.search(w, pos, 'end')+'+1c'
                    while t.get(idx2+'-2c',idx2+'-1c')== '\\':
                        idx2 = t.search(w, idx2, 'end')+'+1c'
                    if w == '"':
                        strws += 1
                    else:
                        strws2 += 1
                    if (strws%2==1 and w == '"') or (strws2%2==1 and w == "'"):
                        t.tag_add(tag, idx, idx2)
                except:
                    t.tag_add(tag, idx, pos)
            else:
                t.tag_add(tag, idx, pos)

def lightword():
    global keydict,strws,strws2
    strws = 0
    strws2 = 0
    for i in keydict:
        CodeEditBox.tag_remove(i,'1.0','end')
        search(CodeEditBox, i, i)
    root.after(60,lightword)

toenterindent = 0
def enterindent(e):
    global toenterindent
    if CodeEditBox.get('insert-1c','insert') == ':':
        toenterindent = 1

tobackindent = 0
def backindent(e):
    global tobackindent
    LineBox['state'] = 'normal'
    LineBox.insert('end','\n'+str(int(LineBox.get('1.0','end').split('\n')[-2])+1))
    LineBox['state'] = 'disable'
    if CodeEditBox.get('insert-4c','insert') == '    ':
        tobackindent = 1

toaddindent = 0
def addindent(e):
    global toaddindent
    toaddindent = 1

def useindent():
    global toenterindent,tobackindent,toaddindent
    if toenterindent:
        CodeEditBox.insert('insert','    ')
        toenterindent = 0
    if tobackindent:
        CodeEditBox.delete('insert-3c','insert')
        tobackindent = 0
    if toaddindent:
        CodeEditBox.delete('insert-1c','insert')
        CodeEditBox.insert('insert','    ')
        toaddindent = 0
    root.after(20,useindent)

def linecount():
    LineBox['state'] = 'normal'
    LineBox.delete('1.0','end')
    LineBox.insert('1.0','\n'.join([str(i) for i in range(1,len(CodeEditBox.get('1.0','end').split('\n')))]))
    LineBox.yview('moveto',codeedit_yscrollbar.get()[0])
    LineBox['state'] = 'disable'
    root.after(5,linecount)

def easyedit():
    # print(codeedit_yscrollbar.get())
    TextcountLabel['text'] = '总字数:'+str(len(CodeEditBox.get('1.0','end')))
    x = len(CodeEditBox.get('1.0','end') \
            .replace('\n','') \
            .replace('\r','') \
            .replace(' ','')
        )
    TextcountLabel2['text'] = '总字数(去空格、换行等):'+str(x)
    root.after(20,easyedit)

def evalcode(e=None):
    try:
        l = 'sel.first'
        r = 'sel.last'
        ans = str(eval(CodeEditBox.get(l,r)))
        anslen = len(ans)
        CodeEditBox.insert(l,ans)
        CodeEditBox.delete(l,r)
    except:
        return  # 错误：没有选中或者计算错误，下次编写

rwid = 0
def runcode(e=None):
    if LanCombo.get() == codetypelist[0]:
        global rwid
        rwid += 1
        if rwid > 1900:
            warninfo = '''注意！
您已开启本编辑器很久，运行次数已超过单次使用限制(1900次)
这导致积累的缓存过多，内存占用较大。无法继续运行。
提供的解决方案：
 1.复制代码，重启本IDE(关闭IDE，在编程社区编程入口重新打开)，粘贴代码
 2.云上保存此代码，下次再做
 3.在本地自己保存代码'''
            messagebox.showwarning('本次运行次数已用完',warninfo)
            return
        coderunner.runwin(code=CodeEditBox.get('1.0','end'),rwid=rwid)
    else:
        coderunner.runwin2(languge=LanCombo.get(),code=CodeEditBox.get('1.0','end'),stdin=StdinText.get('1.0','end'))

menuBar = tk.Menu(root)
root.config(menu=menuBar)

fileMenu = tk.Menu(menuBar,tearoff=0,background='lightskyblue')
menuBar.add_cascade(label="文件",menu=fileMenu)
fileMenu.add_command(label='运行(开发中)',command=lambda:print('该功能被限制'),accelerator='Ctrl+R')
fileMenu.add_command(label='打开(未开发)',command=lambda:print('该功能被限制'),accelerator='Ctrl+O')
fileMenu.add_command(label='保存(未开发)',command=lambda:print('该功能被限制'),accelerator='Ctrl+S')
fileMenu.add_command(label='模板(开发中)',command=lambda:print('该功能被限制'),accelerator='Ctrl+T')
changecodeMenu = tk.Menu(menuBar,tearoff=0,background='lightyellow')
menuBar.add_cascade(label="编辑",menu=changecodeMenu)
changecodeMenu.add_command(label='查找(未开发)',command=lambda:print('该功能被限制'),accelerator='Ctrl+F')
changecodeMenu.add_command(label='计算选中表达式',command=lambda:print('该功能被限制'),accelerator='Ctrl+Shift+C')
helpMenu = tk.Menu(menuBar,tearoff=0,background='lightgreen')
menuBar.add_cascade(label="帮助",menu=helpMenu)
helpMenu.add_command(label='关于(未开发)',command=lambda:print('该功能被限制'))

# CodeEditBox.bind('<Return>',enterindent)
# CodeEditBox.bind('<Tab>',addindent)
# CodeEditBox.bind('<BackSpace>',backindent)
# root.bind('<Control-r>',runcode)
# root.bind('<Control-C>',evalcode)

root.protocol("WM_DELETE_WINDOW", callback)

root.after(10,linecount)
root.after(10,lightword)
root.after(10,useindent)
root.after(10,easyedit)

root.mainloop()