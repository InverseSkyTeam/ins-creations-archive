from tkinter import *
from cf import mkdir,cf_live_path

pwdtype = 0
mkpath=cf_live_path
mkdir(mkpath)
mybook = {}

root = Tk()
root.title('个人中心登录 小轩制作 5.0 无bug')
root.geometry('500x300+500+400')

def button_command():
    global e1,e2,mybook
    t1 = e1.get()
    t2 = e2.get()
    try:
        with open('D:/system_jhxc/my_user/msg.txt','r') as f:
            mybook = eval(f.read())
            if t1 == mybook['user'] and t2 == mybook['password']:
                mybook['score'] += 10
                mybook['copper'] += 1
                mybook['usetime'] += 1
            else:
                ml['text'] = '账户或密码错误，请仔细检查！'
    except:
        with open('D:/system_jhxc/my_user/msg.txt','w') as f:
            mybook = "{'user':'"+t1+"','password':'"+t2+"','level':0,'score':0,'gold_coin':0,'silver_coin':0,'copper':0,'usetime':0}"
            f.write(mybook)
            mybook = eval(mybook)
    else:
        if mybook['score'] < 10:
            mybook['level'] = 0
        elif mybook['score'] < 20:
            mybook['level'] = 1
        elif mybook['score'] < 30:
            mybook['level'] = 2
        elif mybook['score'] < 50:
            mybook['level'] = 3
        elif mybook['score'] < 70:
            mybook['level'] = 4
        elif mybook['score'] < 100:
            mybook['level'] = 5
        elif mybook['score'] < 150:
            mybook['level'] = 6
        elif mybook['score'] < 200:
            mybook['level'] = 7
        elif mybook['score'] < 300:
            mybook['level'] = 8
        elif mybook['score'] < 400:
            mybook['level'] = 9
        elif mybook['score'] < 500:
            mybook['level'] = 10
        elif mybook['score'] < 700:
            mybook['level'] = 11
        elif mybook['score'] < 1000:
            mybook['level'] = 12
        elif mybook['score'] < 1500:
            mybook['level'] = 13
        elif mybook['score'] < 2000:
            mybook['level'] = 14
        elif mybook['score'] < 3000:
            mybook['level'] = 15
        elif mybook['score'] < 5000:
            mybook['level'] = 16
        elif mybook['score'] < 7000:
            mybook['level'] = 17
        elif mybook['score'] < 10000:
            mybook['level'] = 18
        else:
            mybook['level'] = 19
        if t1 == mybook['user'] and t2 == mybook['password']:
            with open('D:/system_jhxc/my_user/msg.txt','w') as f:
                f.write(str(mybook))
    finally:
        f.close()
        if t1 == mybook['user'] and t2 == mybook['password']:
            root.destroy()

def button_pwd():
    global pwdtype,e2
    if pwdtype == 0:
        pwdtype = 1
    else:
        pwdtype = 0
    if pwdtype == 0:
        e2['show'] = '*'
    else:
        e2['show'] = '·'

Label(root,text='{0}| |个人中心登录| |{1}'.format(' '*9,' '*10),fg=r'blue',bg=r'orange',font=('楷体',20)).grid(row=0,column=0,columnspan=2)
Label(root,text='用户名:',font=('楷体',15)).grid(row=1,column=0)
Label(root,text='密码:',font=('楷体',15)).grid(row=2,column=0)

e1 = Entry(root,font=('楷体',15),width=40)
e1.grid(row=1,column=1)

e2 = Entry(root,font=('楷体',15),width=40,show="*")
e2.grid(row=2,column=1)

Button(root,command=button_pwd,text='更换密码风格(共二种)',bg='blue',fg='white',font=('楷体',15),border=5).grid(row=3,column=0,columnspan=2)
Button(root,command=button_command,text='                      提交                        ',bg='lightskyblue',font=('楷体',15),border=5).grid(row=4,column=0,columnspan=2)

ml = Label(root,text='这可能是我目前最好的一次布局',fg='yellowgreen',bg='black')
ml.grid(row=5,column=0,columnspan=2)

root.mainloop()


# 累计----------------------------------------------------------

from tlabel import *
try:
    main_user(mybook)
except:
    print('登录失效')