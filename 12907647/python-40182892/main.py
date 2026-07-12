import tkinter as tk
import threading

submittext = ''
submittype = 0

def runwin(code):
    win = tk.Tk()
    win.title('程序运行分窗口')
    win.configure(background='black')
    win.geometry('1200x700+50+20')
    def free():
        pass
    def execute():                # 屎山来喽~~~~~~~
        t['state'] = 'normal'
        def print(*value,sep=' ',end='\n'):
            for i in range(len(value)):
                t.insert('end',value[i])
                if i < len(value)-1:
                    t.insert('end',sep)
            t.insert('end',end)
        def input(value=''):
            def submit():
                global submittext,submittype
                submittext = inputentry.get()
                submittype = 1
            global submittext,submittype
            print(value)
            print('[StdIn]:',end='')
            inputentry['state'] = 'normal'
            inputbutton['command'] = submit
            t['state'] = 'disable'
            while not submittype:
                try:
                    win.update()
                except:
                    break
            submittype = 0
            t['state'] = 'normal'
            inputbutton['command'] = free
            inputentry['state'] = 'disable'
            print(submittext)
            return submittext
            
        execute_globals = globals()
        execute_locals = locals()
        try:
            exec(code,execute_globals,execute_locals)
        except:
            t.insert('end','\n\n[System]:Error\nGot an except!!!')
        t.insert('end','\n\n[System]:End Code.')
        t['state'] = 'disable'
    
    t = tk.Text(win,bg='black',fg='white',bd=5,state='disable',font=('楷体',13))
    t.pack(fill='both',expand=True)
    inputentry = tk.Entry(win,bg='green',state='disable')
    inputentry.pack(fill='both',expand=True,side='left')
    inputbutton = tk.Button(win,bg='#ffeca9',text='确认提交输入内容',command=free)
    inputbutton.pack(fill='both',side='right')
    executingthread = threading.Thread(target=execute)
    executingthread.setDaemon(True)
    executingthread.start()
    
    win.mainloop()


code = r'''
import time
print('开始测试')
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