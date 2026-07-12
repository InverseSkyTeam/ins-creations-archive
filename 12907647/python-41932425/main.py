from time import *
import tkinter as tk

root = tk.Tk()
root.title('爆杀郭燕铭展示器')
root.attributes('-topmost',True)

t = tk.Text(master=root,
            width=100,
            height=20,
            undo=True,
            state='normal',
            bg='black',
            fg='#0aff11',
            border=11,
            relief='groove',
            wrap='none',
            highlightthickness=2,
            highlightbackground='#0aff11',
            font=(
                '楷体',
                15,
                'normal'
                ),
            )
t.pack()

def push(text,pos):
    global t
    t.insert(pos,text)
    root.update()
def put(text,pos='end',wait=0.1):
    if type(text) == str:
        text = list(text)
    for i in text:
        push(i,pos)
        sleep(wait)
def clear():
    global t
    t.delete('1.0','end')
    root.update()

put('爆杀',wait=0.5)
put('郭燕铭')
put('展示器',wait=0.2)
sleep(0.6)
clear()
put(['你，','真的','比得过','我？'],wait=0.3)
put(['\n不过','尝试','也是','好的'],wait=0.3)
put('\n666')
put('\n那就用这个展示器')
put('看看我会不会用tk.Text',wait=0.05)
put('\n随便举个栗子 就爆杀')
put('\n随便写行代码 跨越十条街')
put('\n如果还嫌不够 你再写一个')
put('\n你真的 tk很好吗？')
sleep(1)
clear()
put('\n我写了五年UI')
put('\n我真的 tk不好吗？')
put('tk其实很简单\n但是\n很多人以为UI很难？！')
sleep(0.5)
clear()
put('你能倒过来，我也能倒过来',pos='0.0',wait=0.2)
sleep(0.3)
clear()
t['bg'] = 'white'
t['fg'] = 'blue'
put('你能换颜色，我也能换颜色',wait=0.2)
sleep(0.3)
clear()
t['font'] = ('楷体',10,'bold')
put('你会换字体，我也会换字体',wait=0.2)
sleep(0.3)
clear()
t['font'] = ('楷体',15,'normal')
t['border'] = 0
put('我还能去边框 这些都是亿点点属性')
put('''666
tk.Text + tag
 postion end-1c
-alpha topmost
!toplevel !frame
  !text !label !entry !listbox
I always global local nonlocal
  !button !canvas !checkbutton !menu
use thread and async is very good
  !menubutton !message !radiobutton !scrollbar
sth you do not know
  !scale !toplevel
N, NE, E, SE, S, SW, W, NW, or CENTER
~ttk tix filedialog
~dnd dialog messagebox
~colorchooser commondialog scrolledtext
~constants font tinui
想做GUI: tk - wx - pyqt - pygame
你眼熟几个？''',wait=0.01)
sleep(0.3)
clear()
a = 1
def cmd():
    global a
    a = 0
b = tk.Button(root,text='text里面插入按钮，点击继续',command=cmd)
t.window_create('end',window=b)
while a: root.update()
clear()
a = 1
p = tk.PhotoImage(file='./logo.png')
b = tk.Button(root,text='text里面插入按钮，点击继续',image=p,command=cmd)
t.window_create('end',window=b)
t.insert('end','这是一个压缩毛巾，它吸水变大变高（点击图片继续')
while a: root.update()
clear()
put('看到了吧，你的要求。我跟你说，我PIL都没用哈')
put('\n代码写的很乱，因为临时赶工的，比赛真好玩')
put('\n彩蛋：INS-IDE无功能版（有功能的库太多了不引入）（包含行数显示、高亮、滚动条同步、ttk等）')
sleep(1)
clear()
root.destroy()
# 无 缝 连 接
import INSIDE