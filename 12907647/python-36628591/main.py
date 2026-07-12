print('请时刻注意终端与窗口')
print('加载中...')
import INSsimple
import cloudlib
import tkinter as tk

d = eval(cloudlib.read_from_cloud('cloudaitdb',12907647))
count = 0
ask = ''

root = tk.Tk()
root.title('小轩聊天AI-GUI 公测数据采集')
root.geometry('600x400+300+100')

def answered():
    global answer,ask
    ask = e.get()
    if ask.replace(' ','') == '':
        print('不得为空')
        return 0
    if ask in d:
        t.delete('1.0','end')
        t.insert('1.0','得到的回答:'+d[ask])
    else:
        t.delete('1.0','end')
        t.insert('end','恭喜，你的问题不在云数据库中，接下来的问题将有机会使你的数据采集至数据集')
        t.insert('end','\n正在查找近似答案\n')
        answer = d[INSsimple.find_max_close_word(ask,d)]
        t.insert('end',answer)
        l.grid(row=2,column=0)
        b1.grid(row=2,column=1)
        b2.grid(row=2,column=2)

def y():
    global count,d,answer
    l.grid_forget()
    b1.grid_forget()
    b2.grid_forget()
    d[ask] = answer
    count += 1
    print('谢谢，您已经贡献'+str(count)+'条，可以继续参与')
def n():
    l.grid_forget()
    b1.grid_forget()
    b2.grid_forget()
    t.delete('1.0','end')
    t.insert('1.0','请在下方输入框输入该问题对应的回答')
    e2.grid(row=2,column=0)
    b3.grid(row=2,column=1)
def okk():
    global count,d
    d[ask] = e2.get()
    e2.grid_forget()
    b3.grid_forget()
    count += 1
    print('谢谢，您已经贡献'+str(count)+'条，可以继续参与')
def saveokkkkk():
    global count,d
    root.destroy()
    cloudlib.save_to_cloud('cloudaitdb',str(d),12907647)
    if count:
        print('你的数据保存完毕，感谢你的贡献')
        print('你的预览成员号码:',count,'\n请回复至评论区')

tk.Label(root,text='你想说:',font=('楷体',20)).grid(row=0,column=0)
e = tk.Entry(root,font=('楷体',17),width=20)
e.grid(row=0,column=1)
tk.Button(root,bd=2,text='  确定  ',font=('楷体',15),command=answered).grid(row=0,column=2)
t = tk.Text(root,width=85,height=15)
t.grid(row=1,column=0,columnspan=3)
t.insert('1.0','暂无回答\n该作品将保存预览成员，严禁设置辱骂、无意义等对话，大家一起公测，保持良好氛围，如发现将以社区公约处理、开发者滥用处理。无用信息每周末统计一次。\n第1次统一：小轩单人制作。\n第2次统一：多人存储ok，扫除垃圾语料[小轩保存到本地]\n')
t.insert('end','第3次统一：同第二次，小轩一共贡献65条数据，修改40条数据，贡献占一半左右\n')
l = tk.Label(root,text='是否对该回答满意:',font=('楷体',20))

b1 = tk.Button(root,bd=2,text='满意',font=('楷体',20),command=y)
b2 = tk.Button(root,bd=2,text='不满意',font=('楷体',20),command=n)

e2 = tk.Entry(root,font=('楷体',17),width=20)
b3 = tk.Button(root,bd=2,text='输入完成',font=('楷体',20),command=okk)

tk.Button(root,bd=2,text='保存我所做的一切更改',font=('楷体',20),command=saveokkkkk).grid(row=3,column=0,columnspan=3)

root.mainloop()