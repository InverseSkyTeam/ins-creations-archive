from files.lib import cloudlib as clib
from tkinter import messagebox
import tkinter as tk
import time
import hashlib

# setinit{
# clib.save_to_cloud('逆天聊-历史消息-小轩端#01','',12907647)
# clib.save_to_cloud('逆天聊-用户信息-小轩端#01','[]',12907647)
# }

# name = input('输入你的社区名:')
name = ''
class LoginApp(object):
    def __init__(self):
        self.name = 'userloginapp'
        self.root = tk.Tk()
        self.root.iconbitmap('files/image/cloud_icon.ico')
        self.root.title('云登录')
        self.root.configure(background='#2d2d2d')
        self.movefront()
        
        def submitlogin():
            global name
            user_list = eval(clib.read_from_cloud('逆天聊-用户信息-小轩端#01',12907647))
            username = 'unnamed_user-not found'
            print(user_list)
            for i in user_list:
                if i['user'] == self.e1.get():
                    userinfo = i
                    username = i['user']
                    break
            if username == 'unnamed_user-not found':
                messagebox.showinfo('提示','未找到该用户，请先去注册')
                return 0
            if userinfo['password'] != hashlib.sha256(self.e2.get().encode('utf-8')).hexdigest():
                messagebox.showinfo('提示','用户名或密码不正确，请再确认一遍')
                return 0
            name = userinfo['user']
            self.root.destroy()
        
        self.l1 = tk.Label(self.root,text='用户名',bg='#2d2d2d',fg='white',font=('楷体',20))
        self.l2 = tk.Label(self.root,text='密  码',bg='#2d2d2d',fg='white',font=('楷体',20))
        self.e1 = tk.Entry(self.root,font=('楷体',20),width=20)
        self.e2 = tk.Entry(self.root,font=('楷体',20),width=20,show='*')
        self.b = tk.Button(self.root,text='          登  录          ',font=('楷体',20),command=submitlogin)
        self.l = tk.Label(self.root,text='没有账户？点此注册一个！',bg='#2d2d2d',fg='lightskyblue',font=('楷体',15))
        self.l1.grid(row=0,column=0)
        self.l2.grid(row=1,column=0)
        self.e1.grid(row=0,column=1)
        self.e2.grid(row=1,column=1)
        self.b.grid(row=2,column=0,columnspan=2)
        
        def b1efun(event):
            self.l['fg']='red'
        def b1lfun(event):
            self.l['fg']='lightskyblue'
        def b1dfun(event):
            top = tk.Toplevel(self.root)
            top.title('注册云账户')
            top.iconbitmap('files/image/cloud_icon.ico')
            top.configure(background='#2d2d2d')
            def submitreg():
                if e2.get() != e3.get():
                    messagebox.showinfo('提示','确认密码不一致')
                    return 0
                if e1.get() == '' or e1.get() == ' ':
                    messagebox.showinfo('提示','用户名不得为空')
                    return 0
                user_list = eval(clib.read_from_cloud('逆天聊-用户信息-小轩端#01',12907647))
                # admin->master->weekmaster->user->look
                # mascot
                user_info = {'user':e1.get(),'password':hashlib.sha256(e2.get().encode('utf-8')).hexdigest(),'TEL-num':'','permission':'user'}
                for i in user_list:
                    if i['user'] == e1.get():
                        messagebox.showinfo('提示','该用户已存在')
                        return 0
                user_list.append(user_info)
                clib.save_to_cloud('逆天聊-用户信息-小轩端#01',str(user_list),12907647)
                messagebox.showinfo('提示','注册成功，请去登录')
                top.destroy()
                
            l1 = tk.Label(top,text='用 户 名',bg='#2d2d2d',fg='white',font=('楷体',20))
            l2 = tk.Label(top,text=' 密  码 ',bg='#2d2d2d',fg='white',font=('楷体',20))
            l3 = tk.Label(top,text='确认密码',bg='#2d2d2d',fg='white',font=('楷体',20))
            e1 = tk.Entry(top,font=('楷体',20),width=20)
            e2 = tk.Entry(top,font=('楷体',20),width=20)
            e3 = tk.Entry(top,font=('楷体',20),width=20,show='*')
            b = tk.Button(top,text='          注  册          ',font=('楷体',20),command=submitreg)
            l1.grid(row=0,column=0)
            l2.grid(row=1,column=0)
            l3.grid(row=2,column=0)
            e1.grid(row=0,column=1)
            e2.grid(row=1,column=1)
            e3.grid(row=2,column=1)
            b.grid(row=3,column=0,columnspan=2)
        
        self.l.bind('<Enter>',b1efun)
        self.l.bind('<Leave>',b1lfun)
        self.l.bind('<Button-1>',b1dfun)
        self.l.grid(row=3,column=0,columnspan=2)
        
    def movefront(self):
        self.root.lift()
        self.root.attributes('-topmost',True)
        self.root.attributes('-topmost',False)
    
    def run(self):
        self.root.mainloop()

class MainApp(object):
    def __init__(self,username):
        self.name = 'mainapp'
        self.username = username
        self.root = tk.Tk()
        # self.root.configure(background='black')
        self.root.geometry('1080x640+100+11')
        self.root.iconbitmap('files/image/cloud_icon.ico')
        self.root.title('逆天聊V0.6')
        self.movefront()
        
        self.leftframe = tk.Frame(self.root,bd=3,bg='white',relief='groove')
        self.leftframe.pack(side='left',fill='both',expand=True)
        self.rightframe = tk.Frame(self.root,bg='white',relief='flat')
        self.rightframe.pack(side='right',fill='both')
        self.righttopframe = tk.Frame(self.rightframe,bd=3,relief='groove',bg='white')
        self.righttopframe.pack(fill='both')
        self.rightbottomframe = tk.Frame(self.rightframe,bd=3,relief='groove')
        self.rightbottomframe.pack(side='bottom',fill='both',expand=True)
        self.rightbottommenuframe = tk.Frame(self.rightbottomframe,bg='#dddddd')
        self.rightbottommenuframe.pack(fill='both',expand=True)
        
        tk.Label(self.leftframe,text=self.username+'在线上').pack()
        
        self.sy = tk.Scrollbar(self.righttopframe)
        self.sy.pack(side='right',fill='y')
        self.chattextbox = tk.Text(self.righttopframe,font=('楷体',16),
            width=70,height=24,relief='flat',cursor='arrow',bg='white',
            state='disable',yscrollcommand=self.sy.set)
        self.chattextbox.pack(side='left',fill='y',expand=True)
        self.sy.config(command=self.chattextbox.yview)
        
        self.emojibutton = tk.Button(self.rightbottommenuframe,bd=0,relief='flat',
            font=('楷体',8,'bold'),text='表情',cursor='hand2',command=self.open_emoji_window)
        self.emojibutton.pack(side='left')
        self.sendtextbox = tk.Text(self.rightbottomframe,font=('楷体',15),
            width=70,height=5,relief='flat',bg='white',undo=True)
        self.sendtextbox.pack(side='left',fill='y')
        self.sendbutton = tk.Button(self.rightbottomframe,bd=0,relief='flat',
            font=('楷体',20,'bold'),text='   发 送   ',bg='lightgreen',
            activebackground='lightskyblue',activeforeground='black',
            highlightthickness=0,cursor='hand2',command=self.send)
        self.sendbutton.pack(side='right',fill='y',expand=True)
    
    def open_emoji_window(self):
        self.emoji_window = tk.Toplevel(self.root)
        self.emoji_window.iconbitmap('files/image/cloud_icon.ico')
        self.emoji_window.title('表情')
        self.emoji_btn_texts = ['微笑','大笑','难过','大哭','白眼',
                          '呲牙','鄙视','狡猾','偷瞄','羡慕',
                          '憨憨','狗头','闭嘴','亲吻','墙裂',
                          '去世','苦笑','偷笑','奸笑','喷饭',
                          '愤怒','苦闷','真棒','好的','拜拜',]
        self.emoji_btns = []
        def add_emoji(string):
	        self.sendtextbox.insert('insert','['+string+']')
        for i in range(len(self.emoji_btn_texts)):
            b = tk.Button(self.emoji_window,text=self.emoji_btn_texts[i],font=('楷体',15),command=lambda string=self.emoji_btn_texts[i]:add_emoji(string))
            b.grid(row=i//5,column=i%5)
            self.emoji_btns.append(b)
    
    def movefront(self):
        self.root.lift()
        self.root.attributes('-topmost',True)
        self.root.attributes('-topmost',False)
    
    def run(self):
        self.root.mainloop()
    
    # 云端操作
    def send(self):
        content = time.strftime('[%Y-%m-%d %H:%M:%S]')+self.username+':\n'+self.sendtextbox.get('1.0','end')
        self.chattextbox['state'] = 'normal'
        self.chattextbox.insert('end',content)
        self.chattextbox.insert('end','-'*70)
        self.save()
        self.chattextbox.see('end')
        self.chattextbox['state'] = 'disable'
        self.sendtextbox.delete('1.0','end')
    
    def save(self):
        content = self.chattextbox.get('1.0','end')
        clib.save_to_cloud('逆天聊-历史消息-小轩端#01',content,12907647)
    
    def clear(self):  # 聊天软件管理员用的函数
        clib.save_to_cloud('逆天聊-历史消息-小轩端#01','',12907647)
    
    def load(self):
        content = clib.read_from_cloud('逆天聊-历史消息-小轩端#01',12907647)
        self.chattextbox['state'] = 'normal'
        self.chattextbox.delete('1.0','end')
        self.chattextbox.insert('1.0',content)
        self.chattextbox.delete('end-1l','end')
        self.chattextbox.see('end')
        self.chattextbox['state'] = 'disable'

loginapp = LoginApp()
loginapp.run()

if name != '':
    INSchatapp = MainApp(name)
    # INSchatapp.clear()
    INSchatapp.load()
    INSchatapp.run()