from files.lib import cloudlib as clib
from files.lib import textbreaker as tb
from tkinter import messagebox
from threading import Thread
import webbrowser as wb
import tkinter as tk
import time
import sys

# setinit{
# clib.save_to_cloud('逆天聊-历史消息-小轩端#01','[]',12907647)
# clib.save_to_cloud('逆天聊-用户信息-小轩端#01','[]',12907647)
# clib.save_to_cloud('逆天聊-聊天中心-小轩端#01','{}',12907647)
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
            for i in user_list:
                if i['user'] == self.e1.get():
                    userinfo = i
                    username = i['user']
                    break
            if username == 'unnamed_user-not found':
                messagebox.showinfo('提示','未找到该用户，请先去注册')
                return 0
            if userinfo['password'] != tb.sha2(self.e2.get()):
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
                pwd = tb.sha2(e2.get())
                user_info = {'user':e1.get(),'password':pwd,'TEL-num':'','permission':'user'}
                
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

class MyselfApp(object):
    def _init__(self,username):
        self.name = 'myselfapp'
        self.username = username
        self.root = tk.Tk()
        self.root.iconbitmap('files/image/cloud_icon.ico')
        self.root.title('逆天聊-个人中心')
        self.movefront()
        
    def movefront(self):
        self.root.lift()
        self.root.attributes('-topmost',True)
        self.root.attributes('-topmost',False)
        
    def run(self):
        self.root.mainloop()

class MainApp(object):
    '''</local/>操作'''
    def __init__(self,username):
        self.name = 'mainapp'
        self.running = 'starting'
        self.username = username
        self.root = tk.Tk()
        # self.root.configure(background='white')
        self.root.geometry('1080x640+100+11')
        self.root.iconbitmap('files/image/cloud_icon.ico')
        self.root.title('逆天聊 [InverseSkyChat-ISC INS出品] Version 0.66s')
        self.movefront()
        
        self.leftframe = tk.Frame(self.root,bd=3,relief='groove')
        self.leftframe.pack(side='left',fill='both',expand=True)
        self.rightframe = tk.Frame(self.root,bg='white',relief='flat')
        self.rightframe.pack(side='right',fill='both')
        self.righttopframe = tk.Frame(self.rightframe,bd=3,relief='groove',bg='white')
        self.righttopframe.pack(fill='both')
        self.rightbottomframe = tk.Frame(self.rightframe,bd=3,relief='groove')
        self.rightbottomframe.pack(side='bottom',fill='both',expand=True)
        self.rightbottommenuframe = tk.Frame(self.rightbottomframe,bg='#dddddd')
        self.rightbottommenuframe.pack(fill='both',expand=True)
        
        # tk.Label(self.leftframe,text=self.username+'在线上').pack()
        
        self.sy = tk.Scrollbar(self.righttopframe)
        self.sy.pack(side='right',fill='y')
        self.chattextbox = tk.Text(self.righttopframe,font=('楷体',16),
            width=70,height=24,relief='flat',cursor='arrow',bg='white',
            state='disable',yscrollcommand=self.sy.set)
        self.chattextbox.pack(side='left',fill='y',expand=True)
        self.sy.config(command=self.chattextbox.yview)
        
        self.emojibutton = tk.Button(self.rightbottommenuframe,bd=1,relief='groove',highlightthickness=0,
            font=('楷体',8,'bold'),text='表情',cursor='hand2',command=self.open_emoji_window)
        self.emojibutton.pack(side='left')
        self.urlbutton = tk.Button(self.rightbottommenuframe,bd=1,relief='groove',highlightthickness=0,
            font=('楷体',8,'bold'),text='链接',cursor='hand2',command=self.open_url_window)
        self.urlbutton.pack(side='left')
        self.sendtextbox = tk.Text(self.rightbottomframe,font=('楷体',15),
            width=70,height=5,relief='flat',bg='white',undo=True)
        self.sendtextbox.pack(side='left',fill='y')
        self.sendbutton = tk.Button(self.rightbottomframe,bd=0,relief='flat',
            font=('楷体',20,'bold'),text='   发 送   ',bg='lightgreen',
            activebackground='lightskyblue',activeforeground='black',
            highlightthickness=0,cursor='hand2',command=self.send)
        self.sendbutton.pack(side='right',fill='y',expand=True)
        self.chattextboxinsertpos = '1.0'
        
        # 撤回
        # self.chattextbox.bind('<Button-3>',lambda event:print(event))
        self.chattextbox.bind('<Button-1>',self.check_url)
    
    def check_url(self,event):
        pos = self.chattextbox.index('current')
        linetext = self.chattextbox.get('1.0','end').split('\n')[int(str(pos).split('.')[0])-1]
        if ('[https://' in linetext):
            is_https = True
            linetext = linetext.split('[https://')
            linetext += linetext[1].split(']')
            linetext.remove(linetext[1])
            urlpos = [len(linetext[0])+1]
            urlpos.append(urlpos[0]+len(linetext[1])+8)
        elif '[http://' in linetext:
            is_https = False
            linetext = linetext.split('[http://')
            linetext += linetext[1].split(']')
            linetext.remove(linetext[1])
            urlpos = [len(linetext[0])+1]
            urlpos.append(urlpos[0]+len(linetext[1])+7)
        else:
            return 0
        if int(urlpos[0]) <= int(str(pos).split('.')[1]) <= int(urlpos[1]):
            if is_https:
                wb.open('https://'+linetext[1])
            else:
                wb.open('http://'+linetext[1])
    
    def open_emoji_window(self):
        self.emoji_window = tk.Toplevel(self.root)
        self.emoji_window.iconbitmap('files/image/cloud_icon.ico')
        self.emoji_window.title('表情')
        self.emoji_btn_texts = ['微笑','大笑','难过','大哭','笑哭',
                           '亲吻','害羞','喜欢','惊讶','无语',
                           '生气','愤怒','程序猿','思考','闭嘴',
                           '空位','空位','空位','空位','空位',
                           '空位','空位','空位','空位','空位',]
        self.emoji_btns = []
        def add_emoji(string):
	        self.sendtextbox.insert('insert','['+string+']')
        for i in range(len(self.emoji_btn_texts)):
            try:
                p = tk.PhotoImage(file='files/image/INSemoji/'+self.emoji_btn_texts[i]+'.png')
                b = tk.Button(self.emoji_window,image=p,font=('楷体',15),command=lambda string=self.emoji_btn_texts[i]:add_emoji(string))
                b.image = p
            except:
                b = tk.Button(self.emoji_window,text=self.emoji_btn_texts[i],font=('楷体',15),command=lambda string=self.emoji_btn_texts[i]:add_emoji(string))
            b.grid(row=i//5,column=i%5)
            self.emoji_btns.append(b)
    
    def open_url_window(self):
        self.url_window = tk.Toplevel(self.root)
        self.url_window.iconbitmap('files/image/cloud_icon.ico')
        self.url_window.title('嵌入链接')
        self.urle = tk.Entry(self.url_window,width=60)
        self.urle.pack()
        def urlbcmd():
            self.sendtextbox.insert('insert','☄超链接:['+self.urle.get()+']')
            self.url_window.destroy()
        self.urlb = tk.Button(self.url_window,text='一件嵌入链接',command=urlbcmd)
        self.urlb.pack()
    
    def movefront(self):
        self.root.lift()
        self.root.attributes('-topmost',True)
        self.root.attributes('-topmost',False)
    
    def run(self):
        Thread(target=self.load).start()
        self.root.mainloop()
        self.running = False
    
    
    
    '''☁</cloud/>操作'''
    def send(self):
        content = time.strftime('[%Y-%m-%d %H:%M:%S]')+self.username+':\n'+self.sendtextbox.get('1.0','end')
        self.chattextbox['state'] = 'normal'
        self.chattextbox.insert('end',content)
        self.chattextbox.insert('end','-'*70)
        self.save()
        self.chattextbox.see('end')
        self.chattextbox['state'] = 'disable'
        self.sendtextbox.delete('1.0','end')
    
    def save(self,filetype='normal'):
        contentlist = eval(clib.read_from_cloud('逆天聊-历史消息-小轩端#01',12907647))
        contentdic = {}
        content = self.chattextbox.get('1.0','end').split('-'*70)[-2]
        contentdic['time'] = content.split(']')[0][1:]
        if contentdic['time'][0] == '[':
            contentdic['time'] = contentdic['time'][1:]
        contentdic['name'] = content.split(']')[1].split(':')[0]
        contentdic['text'] = ':'.join(content.split(':')[3:])[1:-1]
        contentdic['filetype'] = filetype
        contentlist.append(contentdic)
        content = str(contentlist)
        clib.save_to_cloud('逆天聊-历史消息-小轩端#01',content,12907647)
    
    def clear(self):  # 聊天软件管理员用的函数
        clib.save_to_cloud('逆天聊-历史消息-小轩端#01','[]',12907647)
    
    def load(self):
        contentlist = eval(clib.read_from_cloud('逆天聊-历史消息-小轩端#01',12907647))
        while self.running:
            newcontentlist = eval(clib.read_from_cloud('逆天聊-历史消息-小轩端#01',12907647))
            if contentlist != newcontentlist or self.running == 'starting':
                contentlist = newcontentlist
                text = ''
                for i in contentlist:
                    if i['filetype'] == 'normal':
                        text += '['+i['time']+']'+i['name']+':\n'+i['text']+'\n'+'-'*70+'\n'
                    else:
                        print('检测到异常:传入了文件')
                self.chattextbox['state'] = 'normal'
                self.chattextbox.delete('1.0','end')
                self.chattextbox.insert('1.0',text)
                self.chattextbox.delete('end-1l','end')
                self.chattextbox.see('end')
                self.chattextbox['state'] = 'disable'
                if self.running == 'starting':
                    self.running = 'running'
        # print('ends')
        # sys.exit()

loginapp = LoginApp()
loginapp.run()
if name != '':
    INSchatapp = MainApp(name)
    # INSchatapp.clear()
    INSchatapp.run()