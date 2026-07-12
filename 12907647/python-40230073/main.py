import tkinter as tk
import threading
import CCP

def runwin2(languge,code,stdin):
    win = tk.Tk()
    win.title('程序运行分窗口-CCP解释器')
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


languge = '你要的语言（必须下方复制）'
'''
语言：
C(GCC 7.4.0)
C(GCC 8.3.0)
C(GCC 9.2.0)
C#(Mono 6.6.0.161)
C++(GCC 7.4.0)
C++(GCC 8.3.0)
C++(GCC 9.2.0)
Python(2.7.17)
Python(3.8.1)
C(Clang 7.0.1)
C++(Clang 7.0.1)
'''

code = '''
这里写你的代码
这里写你的代码
这里写你的代码
'''

stdin = '''
这里写你运行中需要输入的数据组
这里写你运行中需要输入的数据组
这里写你运行中需要输入的数据组
'''

"""
# 示例：
languge = 'Python(2.7.17)'

# 注：python2的版本都是用raw_input不是input，而且每次只能读入一行，等于cpp的getline
code = '''
raw_input()
print(raw_input())
for i in range(100):
    print(111)
'''

stdin = '''
666
'''
"""

runwin2(languge,code,stdin)

