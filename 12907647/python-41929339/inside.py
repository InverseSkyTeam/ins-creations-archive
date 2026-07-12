[行数索引] 3-main.py | 282 keywords.py | 609 coderunner.py | 762 CCP.py | 867 末尾

main.py

from tkinter import (messagebox,filedialog,ttk)
from PIL import (Image, ImageTk)
from keywords import *
from time import *
import tkinter as tk
import coderunner
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
fileMenu.add_command(label='运行(开发中)',command=runcode,accelerator='Ctrl+R')
fileMenu.add_command(label='打开(未开发)',command=lambda:print('敬请期待'),accelerator='Ctrl+O')
fileMenu.add_command(label='保存(未开发)',command=lambda:print('敬请期待'),accelerator='Ctrl+S')
fileMenu.add_command(label='模板(开发中)',command=lambda:print('敬请期待'),accelerator='Ctrl+T')
changecodeMenu = tk.Menu(menuBar,tearoff=0,background='lightyellow')
menuBar.add_cascade(label="编辑",menu=changecodeMenu)
changecodeMenu.add_command(label='查找(未开发)',command=lambda:print('敬请期待'),accelerator='Ctrl+F')
changecodeMenu.add_command(label='计算选中表达式',command=evalcode,accelerator='Ctrl+Shift+C')
helpMenu = tk.Menu(menuBar,tearoff=0,background='lightgreen')
menuBar.add_cascade(label="帮助",menu=helpMenu)
helpMenu.add_command(label='关于(未开发)',command=lambda:print('敬请期待'))

CodeEditBox.bind('<Return>',enterindent)
CodeEditBox.bind('<Tab>',addindent)
CodeEditBox.bind('<BackSpace>',backindent)
root.bind('<Control-r>',runcode)
root.bind('<Control-C>',evalcode)

root.protocol("WM_DELETE_WINDOW", callback)

root.after(10,linecount)
root.after(10,lightword)
root.after(10,useindent)
root.after(10,easyedit)

# while True:
#     try:
#         root.update()
#     except:
#         break
root.mainloop()   # 循环效率过低，50行就卡了；after线程更好








keywords.py:

modelblocks = {
    1: r'''# Code Block Id: 1
# Code Line: 11
import random as r
print(666,"Hello World!",end="\t")
print(r.randint(1,100),True)
name = input('What\'s your name?')
print('Hi,'+str(name)+'!')
if name == 'ins小轩':
    print('欢迎大佬!!!',666,sep='  ')
print()
print('test-end')''',
    2: r'''# Code Block Id: 2
# Code Line: 3
print("hello world!")''',
    3: r'''# Code Block Id: 3
# Code Line: 25
def do():
    pass
def do2():
    ...
def do3():
    return
do(); do2()
print(bool((do(3)+1 is False)-1))
print(1+2j)
if 0:
    print(1j)
else:
    print(666)
for i in range(3):
    print(i)
a = 10
while True:
    print(a)
    a += 2
    if a > 51 and a%4 == 0:
        print('OK')
        break
print("The End",end='!!!')''',
}

codetypelist = [
    'Python(默认,3.11.1,内置运行版)',
    'Python(3.8.1)',
    'Python(2.7.17)',
    'C(GCC 9.2.0)',
    'C(GCC 8.3.0)',
    'C(GCC 7.4.0)',
    'C(Clang 7.0.1)',
    'C++(GCC 9.2.0)',
    'C++(GCC 8.3.0)',
    'C++(GCC 7.4.0)',
    'C++(Clang 7.0.1)',
    'C#(Mono 6.6.0.161)',
]

keydict = {
    'ArithmeticError': '#d22e1e',
    'AssertionError': '#d22e1e',
    'AttributeError': '#d22e1e',
    'BaseException': '#a25f03',
    'BlockingIOError': '#d22e1e',
    'BrokenPipeError': '#d22e1e',
    'BufferError': '#d22e1e',
    'BytesWarning': '#d28f1e',
    'ChildProcessError': '#d22e1e',
    'ConnectionAbortedError': '#d22e1e',
    'ConnectionError': '#d22e1e',
    'ConnectionRefusedError': '#d22e1e',
    'ConnectionResetError': '#d22e1e',
    'DeprecationWarning': '#d28f1e',
    'EOFError': '#d22e1e',
    'Ellipsis': '#b061e5',
    'EnvironmentError': '#d22e1e',
    'Exception': '#d22e1e',
    'False': '#b061e5',
    'FileExistsError': '#d22e1e',
    'FileNotFoundError': '#d22e1e',
    'FloatingPointError': '#d22e1e',
    'FutureWarning': '#d28f1e',
    'GeneratorExit': '#a25f03',
    'IOError': '#d22e1e',
    'ImportError': '#d22e1e',
    'ImportWarning': '#d28f1e',
    'IndentationError': '#d22e1e',
    'IndexError': '#d22e1e',
    'InterruptedError': '#d22e1e',
    'IsADirectoryError': '#d22e1e',
    'KeyError': '#d22e1e',
    'KeyboardInterrupt': '#a25f03',
    'LookupError': '#d22e1e',
    'MemoryError': '#d22e1e',
    'ModuleNotFoundError': '#d22e1e',
    'NameError': '#d22e1e',
    'None': '#b061e5',
    'NotADirectoryError': '#d22e1e',
    'NotImplemented': '#888888',
    'NotImplementedError': '#d22e1e',
    'OSError': '#d22e1e',
    'OverflowError': '#d22e1e',
    'PendingDeprecationWarning': '#d28f1e',
    'PermissionError': '#d22e1e',
    'ProcessLookupError': '#d22e1e',
    'RecursionError': '#d22e1e',
    'ReferenceError': '#d22e1e',
    'ResourceWarning': '#d28f1e',
    'RuntimeError': '#d22e1e',
    'RuntimeWarning': '#d28f1e',
    'StopAsyncIteration': '#a25f03',
    'StopIteration': '#a25f03',
    'SyntaxError': '#d22e1e',
    'SyntaxWarning': '#d28f1e',
    'SystemError': '#d22e1e',
    'SystemExit': '#a25f03',
    'TabError': '#d22e1e',
    'TimeoutError': '#d22e1e',
    'True': '#b061e5',
    'TypeError': '#d22e1e',
    'UnboundLocalError': '#d22e1e',
    'UnicodeDecodeError': '#d22e1e',
    'UnicodeEncodeError': '#d22e1e',
    'UnicodeError': '#d22e1e',
    'UnicodeTranslateError': '#d22e1e',
    'UnicodeWarning': '#d28f1e',
    'UserWarning': '#d28f1e',
    'ValueError': '#d22e1e',
    'Warning': '#d28f1e',
    'WindowsError': '#d22e1e',
    'ZeroDivisionError': '#d22e1e',
    '__build_class__': '#888888',
    '__debug__': '#888888',
    '__doc__': '#888888',
    '__import__': '#888888',
    '__loader__': '#888888',
    '__name__': '#888888',
    '__package__': '#888888',
    '__spec__': '#888888',
    'abs': '#888888',
    'all': '#888888',
    'any': '#888888',
    'ascii': '#888888',
    'bin': '#888888',
    'bool': '#888888',
    'breakpoint': '#888888',
    'bytearray': '#888888',
    'bytes': '#888888',
    'callable': '#888888',
    'chr': '#888888',
    'classmethod': '#888888',
    'compile': '#888888',
    'complex': '#888888',
    'copyright': '#888888',
    'credits': '#888888',
    'delattr': '#888888',
    'dict': '#888888',
    'dir': '#888888',
    'divmod': '#888888',
    'enumerate': '#888888',
    'eval': '#888888',
    'exec': '#888888',
    'exit': '#888888',
    'filter': '#888888',
    'float': '#888888',
    'format': '#888888',
    'frozenset': '#888888',
    'getattr': '#888888',
    'globals': '#888888',
    'hasattr': '#888888',
    'hash': '#888888',
    'help': '#888888',
    'hex': '#888888',
    'id': '#888888',
    'input': 'purple',
    'int': '#888888',
    'isinstance': '#888888',
    'issubclass': '#888888',
    'iter': '#888888',
    'len': '#888888',
    'license': '#888888',
    'list': '#888888',
    'locals': '#888888',
    'map': '#888888',
    'max': '#888888',
    'memoryview': '#888888',
    'min': '#888888',
    'next': '#888888',
    'object': '#888888',
    'oct': '#888888',
    'open': '#888888',
    'ord': '#888888',
    'pow': '#888888',
    'print': 'purple',
    'property': '#888888',
    'quit': '#888888',
    'range': '#888888',
    'repr': '#888888',
    'reversed': '#888888',
    'round': '#888888',
    'set': '#888888',
    'setattr': '#888888',
    'slice': '#888888',
    'sorted': '#888888',
    'staticmethod': '#888888',
    'str': '#888888',
    'sum': '#888888',
    'super': '#888888',
    'tuple': '#888888',
    'type': '#888888',
    'vars': '#888888',
    'zip': '#888888',
    'and': '#1f1ed2',
    'as': '#1f1ed2',
    'assert': '#1f1ed2',
    'async': '#1f1ed2',
    'await': '#1f1ed2',
    'break': '#1f1ed2',
    'class': '#1f1ed2',
    'continue': '#1f1ed2',
    'def': '#1f1ed2',
    'del': '#1f1ed2',
    'elif': '#1f1ed2',
    'else': '#1f1ed2',
    'except': '#1f1ed2',
    'finally': '#1f1ed2',
    'for': '#1f1ed2',
    'from': '#1f1ed2',
    'global': '#1f1ed2',
    'if': '#1f1ed2',
    'import': '#1f1ed2',
    'in': '#1f1ed2',
    'is': '#1f1ed2',
    'lambda': '#1f1ed2',
    'nonlocal': '#1f1ed2',
    'not': '#1f1ed2',
    'or': '#1f1ed2',
    'pass': '#1f1ed2',
    'raise': '#1f1ed2',
    'return': '#1f1ed2',
    'try': '#1f1ed2',
    'while': '#1f1ed2',
    'with': '#1f1ed2',
    'yield': '#1f1ed2',
    '...': '#b061e5',
    'debugger': 'red',
    'self': '#11bbbb',
    'cls': '#11bbbb',
    'match':'#ce94a1',
    'case':'#ce94a1',
    '+': '#666666',
    '-': '#666666',
    '*': '#666666',
    '/': '#666666',
    '=': '#666666',
    '|': '#666666',
    '\\': '#666666',
    '!=': '#666666',
    '@': '#666666',
    '#': '#666666',
    '$': '#666666',
    '%': '#666666',
    '^': '#666666',
    '&': '#666666',
    '?': '#666666',
    ':': '#666666',
    ';': '#666666',
    '<': '#666666',
    '>': '#666666',
    ',': '#666666',
    '.': '#666666',
    '~': '#666666',
    '0': '#cea822',
    '1': '#cea822',
    '2': '#cea822',
    '3': '#cea822',
    '4': '#cea822',
    '5': '#cea822',
    '6': '#cea822',
    '7': '#cea822',
    '8': '#cea822',
    '9': '#cea822',
    '(': 'brown',
    ')': 'brown',
    '[': 'brown',
    ']': 'brown',
    '{': 'brown',
    '}': 'brown',
    '\'': 'green',
    '"': 'green',
    r'\n': '#11bbbb',
    r'\t': '#11bbbb',
    r'\r': '#11bbbb',
    r'\b': '#11bbbb',
    r'\a': '#11bbbb',
    r'\\': '#11bbbb',
    r'\v': '#11bbbb',
    r'\"': '#11bbbb',
    r'\'': '#11bbbb',
}

symbolshowlist = [
    '+','-','*','/','(',')','=',
    '[',']','{','}','|','\\',
    '!=','@','#','$','%','^','&','?',
    '\'','\"',
    ':',';','<','>',',','.',
    '~',
    ' ','','\n',
    r'\n',r'\t',r'\r',r'\b',r'\"',r"\'",r'\a',r'\\',r'\v',
    '0','1','2','3','4','5','6','7','8','9',
]














coderunner.py

import tkinter as tk
import traceback
import threading
import CCP

submittext = ['' for i in range(2000)]
submittype = [0 for i in range(2000)]

def runwin(code,rwid):
    win = tk.Tk()
    win.title('程序运行分窗口-LCP本地解释器')
    win.configure(background='black')
    win.geometry('1200x700+50+20')
    def free():
        pass
    def callback():
        win.destroy()
    def execute(rwid):                # 屎山来喽~~~~~~~
        t['state'] = 'normal'
        def print(*value,sep=' ',end='\n'):
            for i in range(len(value)):
                t.insert('end',value[i])
                if i < len(value)-1:
                    t.insert('end',sep)
            t.insert('end',end)
        def input(value='',rwid=rwid):
            def submit(rwid=rwid):
                global submittext,submittype
                submittext[rwid] = inputentry.get()
                submittype[rwid] = 1
            global submittext,submittype
            print(value)
            print('[StdIn]:',end='')
            inputentry['state'] = 'normal'
            inputbutton['command'] = submit
            t['state'] = 'disable'
            while not submittype[rwid]:
                try:
                    win.update()
                except:
                    break
            submittype[rwid] = 0
            t['state'] = 'normal'
            inputbutton['command'] = free
            inputentry['state'] = 'disable'
            return submittext[rwid]
            
        execute_globals = globals()
        execute_locals = locals()
        t.insert('end','[System]:Start running code.WindowRunID is '+str(rwid)+'\n')
        try:
            exec(code,execute_globals,execute_locals)
        except:
            try:
                t.insert('end','\n\n[System]:Error\nGot an except!!!\n')
                t.insert('end','Error msg:\n')
                t.insert('end',traceback.format_exc())
            except:
                return
        t.insert('end','\n\n[System]:End Code.')
        t['state'] = 'disable'
    
    f1 = tk.Frame(win)
    f1.pack(side='top',expand=True,fill='both')
    f2 = tk.Frame(win)
    f2.pack(side='bottom',fill='both')
    t = tk.Text(f1,bg='black',fg='white',bd=5,state='disable',font=('楷体',13))
    t.pack(side='left',fill='both',expand=True)
    s = tk.Scrollbar(f1)
    s.pack(side='right',fill='y')
    s.config(command=t.yview)
    t.config(yscrollcommand=s.set)
    inputentry = tk.Entry(f2,bg='green',state='disable')
    inputentry.pack(fill='both',expand=True,side='left')
    inputbutton = tk.Button(f2,bg='#ffeca9',text='确认提交输入内容',command=free)
    inputbutton.pack(fill='both',side='right')
    executingthread = threading.Thread(target=execute,args=[rwid])
    executingthread.setDaemon(True)
    executingthread.start()
    
    win.protocol("WM_DELETE_WINDOW", callback)
    win.mainloop()



def runwin2(languge,code,stdin):
    win = tk.Tk()
    win.title('程序运行分窗口-CCP云上解释器')
    win.configure(background='black')
    win.geometry('1200x700+50+20')
    
    def execute(languge,code,stdin):
        t['state'] = 'normal'
        t.insert('end','[System]:Start running...')
        t['state'] = 'disable'
        runner = CCP.BejsonRun()
        rundic = runner.run(languge,code,stdin)
        t['state'] = 'normal'
        t.insert('end','\n[MessageBox]:Running State:'+rundic['state'])
        t.insert('end','\n[MessageBox]:Running Message:'+rundic['msg'])
        t.insert('end','\n[MessageBox]:Running Error:\n'+rundic['error'])
        t.insert('end','\n[System]:Compile Out:\n'+rundic['co'])
        t.insert('end','\n[System]:Stdout:\n'+rundic['stdout'])
        t.insert('end','\n\n[System]:End running.')
        t['state'] = 'disable'
    
    t = tk.Text(win,bg='black',fg='white',bd=5,state='disable',font=('楷体',13))
    t.pack(side='left',fill='both',expand=True)
    s = tk.Scrollbar(win)
    s.pack(side='right',fill='y')
    s.config(command=t.yview)
    t.config(yscrollcommand=s.set)
    executingthread = threading.Thread(target=execute,args=(languge,code,stdin))
    executingthread.setDaemon(True)
    executingthread.start()
    
    win.mainloop()
    



if __name__ == "__main__":
    code = r'''
import time,tkinter as t
print('开始测试')
r = t.Tk()
r.mainloop()
while True:
    x = input('在下方输入你想输入的(输入e终止一切):')
    for i in range(3):
        print(i+1,x,'关于这个我知道了!')
    if x == 'e':
        break
    time.sleep(1)
print('再见！')
    '''
    runwin(code)














CCP.py

# 原创吴宇航
# 感谢副室长吴宇航对逆天团队的巨大贡献。

import requests
import base64
import json

class BejsonRun():
    def __init__(self):
        self.headers = {
            "authority": "runcode.bejson.com",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://www.bejson.com",
            "referer": "https://www.bejson.com/",
            "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Microsoft Edge\";v=\"103\", \"Chromium\";v=\"103\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62"
        }
        self.langdict = {
            'C(GCC 7.4.0)': 48,
            'C(GCC 8.3.0)': 49,
            'C(GCC 9.2.0)': 50,
            'C#(Mono 6.6.0.161)': 51,
            'C++(GCC 7.4.0)': 52,
            'C++(GCC 8.3.0)': 53,
            'C++(GCC 9.2.0)': 54,
            'Python(2.7.17)': 70,
            'Python(3.8.1)': 71,
            'C(Clang 7.0.1)': 75,
            'C++(Clang 7.0.1)': 76,
        }

    def getToken(self,code,languge,stdin):
        params = {
            'action': 'get_token'
        }
        data = {
            'source_code': code,
            'language_id': str(languge),
            'command_line_arguments': '',
            'stdin': stdin
        }
        res = requests.post(
            'https://runcode.bejson.com/try_run',
            params=params,
            headers=self.headers,
            data=data
        )
        token = json.loads(res.text)['token']
        return token

    def getResult(self,token):
        params = {
            "action": "get_result",
            "token": token
        }
        while True:
            res = requests.get(
                "https://runcode.bejson.com/try_run",
                headers=self.headers,
                params=params
            )
            result = json.loads(res.text)
            if result['status']['description'] not in ['In Queue','Processing']:
                break
        return result

    def runCode(self,languge,code,stdin):
        token = self.getToken(code,languge,stdin)
        results = self.getResult(token)
        return results
    
    def translate(self,code):
        return eval(str(base64.b64decode(code))[1:])
    
    def translate_all(self,data,stdin):
        stdout = data['stdout']
        error = data['stderr']
        msg = data['message']
        co = data['compile_output']
        return {
            'stdin': stdin,
            'stdout': 'Nothing' if not stdout else self.translate(stdout),
            'error': 'Nothing' if not error else self.translate(error),
            'msg': 'Nothing' if not msg else self.translate(msg),
            'co': 'Nothing' if not co else self.translate(co),
            'state': data['status']['description'],
        }

    def run(self,languge,code,stdin):
        langid = self.langdict[languge]
        jsondata = self.runCode(langid,code,stdin)
        dictdata = self.translate_all(jsondata,stdin)
        return dictdata

if __name__ == '__main__':
    runner = BejsonRun()
    print(runner.run(languge='Python(3.8.1)',code='print(1)',stdin=''))