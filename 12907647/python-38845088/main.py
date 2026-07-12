import tkinter as tk
from keywords import *
root = tk.Tk()

root.geometry('1200x700+50+20')
root.configure(background='#444444')
root.title('INS-IDE α-3 非常垃圾')
root.resizable(0,0)

LeftFrame = tk.Frame(root,bg='#111111',width=150)
LeftFrame.pack(side='left',fill='y')
RightFrame = tk.Frame(root)
RightFrame.pack(side='right',fill='y')
CodeEditBox = tk.Text(RightFrame,width=80,height=30,font=('楷体',15))
CodeEditBox.pack(fill='x',side='bottom')

menuBar = tk.Menu(root)
root.config(menu=menuBar)

fileMenu = tk.Menu(menuBar,tearoff=0,background='lightskyblue')
menuBar.add_cascade(label="占位的电摇小子",menu=fileMenu)

for i in keydict:
    CodeEditBox.tag_config(i,foreground=keydict[i])
stringlist = []
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
                idx2 = t.search(w, pos, 'end')+'+1c'
                if w == '"':
                    strws += 1
                else:
                    strws2 += 1
                try:
                    if (strws%2==1 and w == '"') or (strws2%2==1 and w == "'"):
                        strw = t.get(idx,idx2)
                        stringlist.append(strw)
                        t.tag_config(strw,foreground='green')
                        t.tag_add(tag, idx, idx2)
                except:
                    t.tag_add(tag, idx, pos)
            else:
                t.tag_add(tag, idx, pos)

def lightword():
    global keydict,stringlist,strws,strws2
    for i in stringlist:
        CodeEditBox.tag_delete(i)
    stringlist = []
    strws = 0
    strws2 = 0
    for i in keydict:
        CodeEditBox.tag_remove(i,'1.0','end')
        search(CodeEditBox, i, i)

toenterindent = 0
def enterindent(e):
    global toenterindent
    if CodeEditBox.get('end-2c','end-1c') == ':':
        # CodeEditBox.insert('end','    ')
        toenterindent = 1

tobackindent = 0
def backindent(e):
    global tobackindent
    if CodeEditBox.get('end-5c','end-1c') == '    ':
        tobackindent = 1

def useindent():
    global toenterindent,tobackindent
    if toenterindent:
        CodeEditBox.insert('end','    ')
        toenterindent = 0
    if tobackindent:
        CodeEditBox.delete('end-4c','end-1c')
        tobackindent = 0

CodeEditBox.bind('<Return>',enterindent)
CodeEditBox.bind('<BackSpace>',backindent)


while True:
    try:
        lightword()
        useindent()
        root.update()
    except:
        break