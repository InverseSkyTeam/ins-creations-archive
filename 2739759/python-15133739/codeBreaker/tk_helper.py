from codeBreaker.Breaker import (作品访问器,作品访问器2)
def show_data(title,url):
    import tkinter as tk
    t1 = '作品名：'+str(作品访问器.作品名称(url))
    t2 = '作者名：'+str(作品访问器.作者(url))
    t3 = '赞：'+str(作品访问器.喜欢(url))
    t4 = '浏览：'+str(作品访问器.观看(url))
    t5 = '作品说明：'+str(作品访问器.作品说明(url))[0:5]+'...'
    t6 = '踩：'+str(作品访问器.踩(url))
    t7 = '发布时间：'+str(作品访问器.发布时间(url))
    t8 = '更改时间：'+str(作品访问器.更改时间(url))
    t9 = '收藏：'+str(作品访问器.收藏(url))
    ut1 = '输出源码'
    ut2 = '输出作品说明'
    ut3 = '作者主页'
    ut4 = '作者头像源'
    ut5 = '代码多少'
    root = tk.Tk()
    root.title(title)
    root.geometry('666x440')
    l = tk.Listbox(root,width = 82,height= 2)
    def ud1():
        l.delete(0,tk.END)
        l.insert(0,作品访问器.源码(url)+'\n\n\n')
    def ud2():
        l.delete(0,tk.END)
        l.insert(0,作品访问器.作品说明(url)+'\n\n\n')
    def ud3():
        l.delete(0,tk.END)
        l.insert(0,作品访问器.作者主页(url)+'\n\n\n')
    def ud4():
        l.delete(0,tk.END)
        l.insert(0,作品访问器.作者头像源(url)+'\n\n\n')
    def ud5():
        l.delete(0,tk.END)
        l.insert(0,作品访问器2.代码多少(url)+'\n\n\n')
    b1 = tk.Label(root,text=t1)
    b1.pack()
    b2 = tk.Label(root,text=t2)
    b2.pack()
    b3 = tk.Label(root,text=t3)
    b3.pack()
    b4 = tk.Label(root,text=t4)
    b4.pack()
    b5 = tk.Label(root,text=t5)
    b5.pack()
    b6 = tk.Label(root,text=t6)
    b6.pack()
    b7 = tk.Label(root,text=t7)
    b7.pack()
    b8 = tk.Label(root,text=t8)
    b8.pack()
    b9 = tk.Label(root,text=t9)
    b9.pack()
    u1 = tk.Button(root,text=ut1,command=ud1)
    u1.pack()
    if len(ut2) > 5:
        u2 = tk.Button(root,text=ut2,command=ud2)
        u2.pack()
    u3 = tk.Button(root,text=ut3,command=ud3)
    u3.pack()
    u4 = tk.Button(root,text=ut4,command=ud4)
    u4.pack()
    u5 = tk.Button(root,text=ut5,command=ud5)
    u5.pack()
    l.pack()
    root.mainloop()