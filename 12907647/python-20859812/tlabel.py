from tkinter import *

def main_user(mybook):
    user = Tk()
    user.title('个人中心信息')
    user.geometry('500x300+500+400')
    
    Label(user,text='你的用户名：'+mybook['user'],fg='blue').pack()
    Label(user,text='你的等级：{}'.format(mybook['level']),fg='blue').pack()
    Label(user,text='你的累计分数（来一次加10分，分值越多等级越大，下次出别的游戏能赢取更多）：{}'.format(mybook['score']),fg='blue').pack()
    Label(user,text='你的金币：{}'.format(mybook['gold_coin']),fg='blue').pack()
    Label(user,text='你的银币：{}'.format(mybook['silver_coin']),fg='blue').pack()
    Label(user,text='你的铜币：{}'.format(mybook['copper']),fg='blue').pack()
    Label(user,text='你的使用次数（注册时不计，登录时开记）：{}'.format(mybook['usetime']),fg='blue').pack()
    
    user.mainloop()