# coding:utf-8

# cloud-import------------------------------------------------
from files.lib import cloudlib as clib, textbreaker as tb
# local-import------------------------------------------------
from tkinter import messagebox,filedialog
from threading import Thread
from xes import sms
import webbrowser as wb
import tkinter as tk
import requests
import random
import time
import sys
import os
import re

# setinit{
# print(clib.read_from_cloud('逆天聊-用户信息-小轩端#01',12907647))
# clib.save_to_cloud('逆天聊-历史消息-小轩端#01','',12907647)
# clib.save_to_cloud('逆天聊-用户信息-小轩端#01','[]',12907647)
# clib.save_to_cloud('逆天聊-聊天中心-小轩端#01',"{'逆天聊公共群':{'master':'小轩','weedier-master':[],'user':[]}}",12907647)
# clib.save_to_cloud('逆天聊-文件海洋-小轩端#01','{}',12907647)
# }
try:
    import ntpath
except:
    osname = 'mac'
else:
    osname = 'win'
# clib.save_to_cloud('逆天聊-文件海洋-小轩端#_逆天聊公共群','{}',12907647)
# clib.save_to_cloud('逆天聊-文件海洋-小轩端#_逆天团队[INS]','{}',12907647)
# name = input('输入你的社区名:')
name = ''
group = '逆天聊公共群'
alluserinfo = False
def getfilesize(f):return sum(sum(os.path.getsize(os.path.join(parent, file)) for file in files) for parent, dirs, files in os.walk(f))
def getfilesize2(f):return os.path.getsize(f)
def setfilesize(size,unit='KB'):return round(size/float(1024**{'B':0,'KB':1,'MB':2,'GB':3,'TB':4,'PB':5,'EB':6,'ZB':7,'YB':8}[unit]),2)

def mkdir(path):
    import os
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False
if osname == 'win':
    save_file_path = os.path.expanduser("~/应用程序/InverseSkyChat").replace('\\','/')
    mkdir(save_file_path)
else:
    save_file_path = 'Library/InverseSkyChat'

class LoginApp(object):
    def __init__(self):
        self.name = 'userloginapp'
        self.root = tk.Tk()
        self.root.iconbitmap('files/image/cloud_icon.ico')
        self.root.title('云登录')
        self.root.configure(background='#2d2d2d')
        self.movefront()
        
        def submitlogin():
            global name,alluserinfo
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
            alluserinfo = userinfo
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
                if e2.get().replace(' ','').replace('\t','') == '':
                    messagebox.showinfo('提示','密码不得为空')
                    return 0
                if len(e2.get()) < 4:
                    messagebox.showinfo('提示','密码不得少于4位')
                    return 0
                if len(e2.get()) > 256:
                    messagebox.showinfo('提示','密码不得多于256位')
                    return 0
                if e2.get() != e3.get():
                    messagebox.showinfo('提示','确认密码不一致')
                    return 0
                if e1.get().replace(' ','').replace('\t','') == '':
                    messagebox.showinfo('提示','用户名不得为空')
                    return 0
                user_list = eval(clib.read_from_cloud('逆天聊-用户信息-小轩端#01',12907647))
                # admin->master->weekmaster->user->look
                # mascot
                pwd = tb.sha2(e2.get())
                user_info = {'user':e1.get(),'password':pwd,'TEL-num':'','permission':'user','id':clib.get_id(clib.get_cookies())}
                
                for i in user_list:
                    if i['user'] == e1.get():
                        messagebox.showinfo('提示','该用户已存在')
                        return 0
                user_list.append(user_info)
                clib.save_to_cloud('逆天聊-用户信息-小轩端#01',str(user_list),12907647)
                
                groups = eval(clib.read_from_cloud('逆天聊-聊天中心-小轩端#01',12907647))
                groups['逆天聊公共群']['user'].append(e1.get())
                clib.save_to_cloud('逆天聊-聊天中心-小轩端#01',str(groups),12907647)
                
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
    def __init__(self,userinfo):
        self.name = 'myselfapp'
        self.userinfo = userinfo
        self.verificationmsg = ''
        self.username = self.userinfo['user']
        self.userpwd = self.userinfo['password']
        self.usertel = self.userinfo['TEL-num']
        self.usertel = '暂无' if self.usertel == '' else self.usertel
        self.userid = self.userinfo['id']
        self.root = tk.Tk()
        self.root.iconbitmap('files/image/cloud_icon.ico')
        self.root.title('逆天聊-个人中心')
        self.root.geometry('788x600+160+60')
        self.root.resizable(0, 0)
        self.root.configure(background='#e1e1e1')
        self.movefront()
        
        def bindtel():
            telnum = e1.get()
            if len(telnum) != 11:
                messagebox.showinfo('提示','手机号必须为11位')
                return 0
            if not re.findall('^1[3-9]\d{9}$',telnum):
                messagebox.showinfo('提示','手机号格式错误')
                return 0
            if messagebox.askyesno('问题','是否现在发送验证码?\n验证码在关闭个人中心之前有效'):
                self.verificationmsg = '验证码:'+''.join([chr(random.choice([random.randint(48,57),random.randint(65,90),random.randint(97,122)])) for i in range(random.randint(6,12))])
                print(self.verificationmsg)
                self.telnum = telnum
                # Thread(target=sms.send_msg,args=[self.telnum,self.verificationmsg]).start()
        def submit_verification():
            if self.verificationmsg == '':
                messagebox.showwarning('警告','还未获取验证码')
                return 0
            if e2.get() != self.verificationmsg.split(':')[1]:
                messagebox.showwarning('警告','验证码错误，请重试')
                return 0
            user_list = eval(clib.read_from_cloud('逆天聊-用户信息-小轩端#01',12907647))
            for i in user_list:
                if i['user'] == self.username:
                    i['TEL-num'] = self.telnum
                    self.usertel = self.telnum
                    l['text'] = '我的手机号:'+self.usertel
                    break
            user_list = str(user_list)
            clib.save_to_cloud('逆天聊-用户信息-小轩端#01',user_list,12907647)
            messagebox.showinfo('提示','验证通过，手机号已绑定')
        
        tk.Label(self.root,bg='#bbbbbb',width=39,anchor='w',bd=3,
                 text=self.username+'的个人中心',relief='solid',
                 font=('楷体',30)).grid(row=0,column=0,columnspan=2)
        l = tk.Label(self.root,text='我的手机号:'+self.usertel,font=('楷体',16))
        l.grid(row=1,column=0,columnspan=2)
        tk.Button(self.root,text='绑定手机号',width=20,font=('楷体',20),command=bindtel).grid(row=2,column=0)
        e1 = tk.Entry(self.root,width=20,font=('楷体',35))
        e1.grid(row=2,column=1)
        tk.Button(self.root,text='确认验证码',width=20,font=('楷体',20),command=submit_verification).grid(row=3,column=0)
        e2 = tk.Entry(self.root,width=20,font=('楷体',35))
        e2.grid(row=3,column=1)
        tk.Label(self.root,text='我的xes-id:'+self.userid,font=('楷体',16)).grid(row=4,column=0,columnspan=2)
        
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
        self.root.title('逆天聊 V1.1')
        self.movefront()
        
        self.leftframe = tk.Frame(self.root,bd=3,relief='groove',bg='#adadad')
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
        self.opencentrebutton = tk.Button(self.leftframe,bd=0,relief='flat',
            font=('楷体',20,'bold'),text='进入个人中心',bg='lightskyblue',
            activebackground='lightgreen',activeforeground='black',
            highlightthickness=0,cursor='hand2',command=self.opencentre)
        self.opencentrebutton.pack(side='top',fill='x')
        self.addgroupbutton = tk.Button(self.leftframe,bd=0,relief='flat',
            font=('楷体',20,'bold'),text='创建一个群聊',bg='lightyellow',
            activebackground='lightgreen',activeforeground='black',
            highlightthickness=0,cursor='hand2',command=self.addgroup)
        self.addgroupbutton.pack(side='top',fill='x')
        self.addotherbutton = tk.Button(self.leftframe,bd=0,relief='flat',
            font=('楷体',20,'bold'),text='添加群或朋友',bg='lightgreen',
            activebackground='lightyellow',activeforeground='black',
            highlightthickness=0,cursor='plus',command=self.addother)
        self.addotherbutton.pack(side='top',fill='x')
        
        self.sy = tk.Scrollbar(self.righttopframe)
        self.sy.pack(side='right',fill='y')
        self.chattextbox = tk.Text(self.righttopframe,font=('楷体',17),
            width=70,height=20,relief='flat',cursor='arrow',bg='white',
            state='disable',yscrollcommand=self.sy.set)
        self.chattextbox.pack(side='left',fill='y',expand=True)
        self.sy.config(command=self.chattextbox.yview)
        
        self.emojibutton = tk.Button(self.rightbottommenuframe,bd=1,relief='groove',highlightthickness=0,
            font=('楷体',8,'bold'),text='表情',cursor='hand2',command=self.open_emoji_window)
        self.emojibutton.pack(side='left')
        self.urlbutton = tk.Button(self.rightbottommenuframe,bd=1,relief='groove',highlightthickness=0,
            font=('楷体',8,'bold'),text='链接',cursor='hand2',command=self.open_url_window)
        self.urlbutton.pack(side='left')
        self.filebutton = tk.Button(self.rightbottommenuframe,bd=1,relief='groove',highlightthickness=0,
            font=('楷体',8,'bold'),text='文件',cursor='hand2',command=self.open_file_window)
        self.filebutton.pack(side='left')
        self.configbutton = tk.Button(self.rightbottommenuframe,bd=1,relief='groove',highlightthickness=0,
            font=('楷体',8,'bold'),text='设置与管理',cursor='hand2',command=self.open_config_window)
        self.configbutton.pack(side='left')
        
        self.sendtextbox = tk.Text(self.rightbottomframe,font=('楷体',12),
           width=94,height=9,relief='flat',bg='#f1f1f1',undo=True)
        self.sendtextbox.pack(side='left',fill='y')
        self.sendbutton = tk.Button(self.rightbottomframe,bd=0,relief='flat',
            font=('楷体',16,'bold'),text=' 发送 \n(Ctrl+S)',bg='lightgreen',
            activebackground='lightskyblue',activeforeground='black',
            highlightthickness=0,cursor='hand2',command=self.send)
        self.sendbutton.pack(side='right',fill='y',expand=True)
        self.chattextboxinsertpos = '1.0'
        
        self.btnscmd = {}
        self.update_group()
        
        # 撤回
        # self.chattextbox.bind('<Button-3>',lambda event:print(event))
        self.sendtextbox.bind('<Control-s>',self.send)

    def update_group(self):
        allgroups = eval(clib.read_from_cloud('逆天聊-聊天中心-小轩端#01',12907647))
        for self.i in allgroups:
            the_group = allgroups[self.i]
            if (('pricate' not in self.i) and (the_group['master'] == self.username or self.username in the_group['weedier-master'] or self.username in the_group['user'])) or ('pricate' in self.i and self.username in the_group['user']):
                self.reali = self.i 
                if 'pricate' in self.i:
                    self.i = the_group['user']
                    self.i = self.i[0] if self.i[1] == self.username else self.i[1]
                exec('''
global changegroupcmd,changebgcmd
def changegroupcmd(i=self.i,reali=self.reali,do=self.load_at_once):
    global group
    group = reali
    do()
    messagebox.showinfo("提示","您已经切换到:"+i)
''')
                if not (self.i in self.btnscmd):
                    self.btnscmd[self.i] = [changegroupcmd,tk.Button(self.leftframe,bd=1,relief='groove',cursor='hand2',font=('楷体',14,'bold'))]
        for i in self.btnscmd:
            self.btnscmd[i][1]['text'] = i
            self.btnscmd[i][1]['command'] = self.btnscmd[i][0]
            self.btnscmd[i][1].pack(side='top',fill='x')

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
	        self.sendtextbox.insert('insert','表情:{'+string+'}')
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
            t = self.urle.get()
            if ('https://' not in t) and ('http://' not in t) and ('ftp://' not in t) and ('ws://' not in t) and ('wss://' not in t):
                messagebox.showinfo('提示','请输入完整网址，前面的https/http/ftp/ws/wss不要漏了')
                return 0
            self.sendtextbox.insert('insert','链接:{'+self.urle.get()+'}')
            self.url_window.destroy()
        self.urlb = tk.Button(self.url_window,text='一件嵌入链接',command=urlbcmd)
        self.urlb.pack()
        
    def open_file_window(self):
        self.file_window = tk.Toplevel(self.root)
        self.file_window.iconbitmap('files/image/cloud_icon.ico')
        self.file_window.title('发送文件')
        # self.file_window.geometry('300x60')
        self.file_window.attributes('-topmost',True)
        def file_upload():
            selectfile = tk.filedialog.askopenfilename()
            if not selectfile:
                return False
            if os.path.isdir(selectfile):
                gfs = getfilesize(selectfile)
            else:
                gfs = getfilesize2(selectfile)
            if setfilesize(gfs,'MB') > 41:    # 约数后，这里的40要改为41，以防误差
                messagebox.showinfo('提示','上传文件过大，请上传<40MB的文件')
                return False
            self.fname = time.strftime('{%Y-%m-%d %H:%M:%S ')+selectfile.split('/')[-1]+'}'
            def up():
                url = clib.upfile(selectfile)
                dic = eval(clib.read_from_cloud('逆天聊-文件海洋-小轩端#_'+group,12907647))
                dic[self.fname] = url
                clib.save_to_cloud('逆天聊-文件海洋-小轩端#_'+group,str(dic),12907647)
            Thread(target=up).start()
            self.file_upload_lbl['text'] = '文件路径：' + selectfile
        def file_send():
            text = self.file_upload_lbl['text'][5:]
            if '/' not in text:
                messagebox.showinfo('提示','还未上传文件')
            else:
                self.sendtextbox.insert('insert','文件:'+self.fname)
                self.file_window.destroy()
        self.file_upload_btn = tk.Button(self.file_window,text='上传本地文件(需要一些时间)',command=file_upload)
        self.file_upload_lbl = tk.Label(self.file_window,text='文件路径：未上传')
        self.file_upload_ok_btn = tk.Button(self.file_window,text='一键嵌入文件(需要等待文件路径完整后)',command=file_send)
        self.file_upload_btn.grid(row=0,column=0)
        self.file_upload_lbl.grid(row=0,column=1)
        self.file_upload_ok_btn.grid(row=1,column=0,columnspan=2)
    
    def open_config_window(self):
        self.config_window = tk.Toplevel(self.root)
        self.config_window.iconbitmap('files/image/cloud_icon.ico')
        self.config_window.title('群设置与管理')
        self.config_window.geometry('500x350')
        
        mygroupinfo = eval(clib.read_from_cloud('逆天聊-聊天中心-小轩端#01',12907647))[group]
        
        if 'pricate' in group:
            tk.Label(self.config_window,text='私聊不能进行群设置').pack()
            return 0
        if not ((mygroupinfo['master'] == self.username) or (self.username in mygroupinfo['weedier-master'])):
            tk.Label(self.config_window,text='您的权限还不够更多地设置管理该群，如有必要请联系群主升级权限').pack()
            return 0
        
        def invite():
            person = e.get()
            is_in_userdict = 0
            users = eval(clib.read_from_cloud('逆天聊-用户信息-小轩端#01',12907647))
            for i in users:
                if i['user'] == person:
                    is_in_userdict = 1
                    break
            if not is_in_userdict:
                messagebox.showinfo('提示','邀请失败\n该用户不存在')
                return is_in_userdict   # return 0,这里是故意玩
            if person in mygroupinfo['user'] or person in mygroupinfo['weedier-master'] or person == mygroupinfo['master']:
                messagebox.showinfo('提示','该用户已经在群里了')
                return 0
            if messagebox.askyesno('确认邀请','确认要邀请['+person+']入群吗?'):
                centre = eval(clib.read_from_cloud('逆天聊-聊天中心-小轩端#01',12907647))
                centre[group]['user'].append(person)
                clib.save_to_cloud('逆天聊-聊天中心-小轩端#01',str(centre),12907647)
            else:
                return 0
            self.finalcontent += '[(系统-防伪)'+time.strftime('%Y-%m-%d %H:%M:%S')+']系统:\n'+self.username+'邀请了'+person+'进群\n'+'-'*67+'\n'
            self.save()
            messagebox.showinfo('提示','邀请成功')
            
        tk.Label(self.config_window,text='管理').grid(row=0,column=0)
        tk.Label(self.config_window,text='群成员:'+str(mygroupinfo).replace('weedier-master','副群主/管理员').replace('master','群主').replace('user','普通成员'),wraplength=400).grid(row=1,column=0,columnspan=2)
        e = tk.Entry(self.config_window)
        e.grid(row=2,column=0)
        tk.Button(self.config_window,text='邀请此成员加入',command=invite).grid(row=2,column=1)
    
    def addgroup(self):
        self.addgroup_window = tk.Toplevel(self.root)
        self.addgroup_window.iconbitmap('files/image/cloud_icon.ico')
        self.addgroup_window.title('创建群聊')
        self.addgroup_window.attributes('-topmost',True)
        def addgroupbtn():
            title = e.get()
            if title.replace(' ','').replace('\t','') == '':
                messagebox.showinfo('提示','群名称不得为空')
                return 0
            if 'pricate' in title:
                messagebox.showinfo('错误','群名称内不得包含"pricate"，否则会使程序错误')
                return 0
            if len(title) < 2:
                messagebox.showinfo('提示','群名称至少要2个字符')
                return 0
            if len(title) > 16:
                messagebox.showinfo('提示','群名称至多只能有16个字符')
                return 0
            groups = eval(clib.read_from_cloud('逆天聊-聊天中心-小轩端#01',12907647))
            for i in groups:
                if i == title:
                    messagebox.showinfo('提示','该群已存在，群主是'+groups[i]['master']+'，不可重复创建\n如有疑问请联系该群群主')
                    return 0
            newgroupinfo = {'master':self.username,'weedier-master':[],'user':[]}
            groups[title] = newgroupinfo
            clib.save_to_cloud('逆天聊-聊天中心-小轩端#01',str(groups),12907647)
            clib.save_to_cloud('逆天聊-历史消息-小轩端#_'+title,'',12907647)
            clib.save_to_cloud('逆天聊-文件海洋-小轩端#_'+title,'{}',12907647)
            self.update_group()
            messagebox.showinfo('提示','该群创建成功，您是该群的群主\n您拥有该群最高权限、特权与责任\n尊敬的群主，您可以邀请别人到你的群了~')
            
        tk.Label(self.addgroup_window,text='请注意，您正在创建一个群聊，你将成为群主\n群主是可以管理群的人，是一群之主\n如群出现问题而非个人出现问题\n群主将承担一切责任\n但是，群主可以享受一定特权',fg='red').pack()
        tk.Label(self.addgroup_window,text='请在下面的输入框中输入群名',fg='blue').pack()
        e = tk.Entry(self.addgroup_window)
        e.pack()
        tk.Button(self.addgroup_window,text='确认创建此群(需要约3-6秒)',fg='green',relief='solid',bd=2,cursor='heart',command=addgroupbtn).pack()
        
    def addother(self):
        self.addother_window = tk.Toplevel(self.root)
        self.addother_window.iconbitmap('files/image/cloud_icon.ico')
        self.addother_window.title('添加')
        self.addother_window.attributes('-topmost',True)
        def addotherbtn():
            friend = e.get()
            if friend.replace(' ','').replace('\t','') == '':
                messagebox.showinfo('提示','对方名字不得为空')
                return 0
            if friend == self.username:
                messagebox.showinfo('提示','不能添加自己，你是来搞笑的吗')
                return 0
            for i in self.btnscmd:
                if self.btnscmd[i][1]['text'] == friend:
                    messagebox.showinfo('提示','已经添加过此好友')
                    return 0
            is_in_userdict = 0
            users = eval(clib.read_from_cloud('逆天聊-用户信息-小轩端#01',12907647))
            for i in users:
                if i['user'] == friend:
                    is_in_userdict = 1
                    break
            if not is_in_userdict:
                messagebox.showinfo('提示','邀请失败\n该用户不存在')
                return is_in_userdict
            groups = eval(clib.read_from_cloud('逆天聊-聊天中心-小轩端#01',12907647))
            pgroups = {i:groups[i] for i in groups if 'pricate' in i}
            title = 'pricate'+str(int(max(pgroups).replace('pricate',''))+1)
            # title = 'pricate1'
            newgroupinfo = {'user':[self.username,friend]}
            groups[title] = newgroupinfo
            clib.save_to_cloud('逆天聊-聊天中心-小轩端#01',str(groups),12907647)
            clib.save_to_cloud('逆天聊-历史消息-小轩端#_'+title,'',12907647)
            clib.save_to_cloud('逆天聊-文件海洋-小轩端#_'+title,'{}',12907647)
            self.update_group()
            messagebox.showinfo('提示','添加成功')
            
        tk.Label(self.addother_window,text='请在下面的输入框中输入朋友的名字',fg='blue').pack()
        e = tk.Entry(self.addother_window)
        e.pack()
        tk.Button(self.addother_window,text='确认添加好友(需要6-15秒，私密聊天创建与判断时间较长)',fg='green',relief='solid',bd=2,cursor='heart',command=addotherbtn).pack()
        
    def movefront(self):
        self.root.lift()
        self.root.attributes('-topmost',True)
        self.root.attributes('-topmost',False)
        
    def run(self):
        Thread(target=self.load).start()
        self.root.mainloop()
        self.running = False
        sys.exit()
    
    
    
    '''☁</cloud/>操作'''
    def send(self,event=None):
        got = self.sendtextbox.get('1.0','end')
        if got.replace(' ','').replace('\t','').replace('\n','').replace('\r','') == '':
            messagebox.showinfo('提示','不得输入空信息')
            return 0
        # 发送限制框架
        for i in ['傻逼','lj','sb','wdnmd']:
            if i in got:
                messagebox.showwarning('警告','禁止发送不良信息，否则会被封号')
                return 0
        if len(got) > 1000:
            messagebox.showinfo('警告','发送信息不得超过1000字，刷屏会被封号，请发送文档')
            return 0
        content = time.strftime('[%Y-%m-%d %H:%M:%S]')+self.username+':\n'+got
        self.finalcontent += content+'-'*67+'\n'
        self.save()
        self.sendtextbox.delete('1.0','end')
        self.running = 'starting'
        self.load_at_once()

    def read_file(self,name):
        url = eval(clib.read_from_cloud('逆天聊-文件海洋-小轩端#_'+group,12907647))[name]
        if messagebox.askyesno('提问','是否使用网页版查看?\n如文件较大，如音视频文件，建议点击“是”\n选择“否”则下载到本地查看'):
            wb.open(url)
            return True
        response = requests.get(url)
        try:
            response.encoding = response.apparent_encoding
        except:
            response.encoding = 'ANSI'
        t = response.text
        type_ = 'text'
        if chr(65533) in t:
            type_ = 'content'
            t = response.content
        newname = ' '.join(name.split()[2:])[:-1]
        if type_ == 'text':
            with open(newname,'w') as f:
                f.write(t)
                f.close()
        else:
            with open(newname,'wb') as f:
                f.write(t)
                f.close()
        # if osname == 'win':
        os.system('start "" "'+newname+'"')
        
    def save(self,filetype='normal'):
        # content = self.chattextbox.get('1.0','end')
        # print(content)
        clib.save_to_cloud('逆天聊-历史消息-小轩端#_'+group,self.finalcontent,12907647)
        
    def clear(self):
        clib.save_to_cloud('逆天聊-历史消息-小轩端#_'+group,'',12907647)
        
    def load(self):
        self.finalcontent = clib.read_from_cloud('逆天聊-历史消息-小轩端#_'+group,12907647)
        while self.running:
            self.load_at_once()
            if self.running == 'starting':
                self.running = 'running'
            
        # print('ends')
        # sys.exit()
    
    def load_at_once(self):
        newcontent = clib.read_from_cloud('逆天聊-历史消息-小轩端#_'+group,12907647)
        if self.finalcontent != newcontent or self.running == 'starting':
            self.finalcontent = newcontent
            self.chattextbox['fg'] = self.chattextbox['bg']
            self.chattextbox['state'] = 'normal'
            self.chattextbox.delete('1.0','end')
            self.chattextbox.insert('1.0',self.finalcontent)
            # self.chattextbox.delete('end-1l','end')
            
            # 文件转换按钮
            commandlist = []
            indexlist = []
            textlist = []
            while 1:
                self.indexstart = self.chattextbox.search('文件:{','1.0')
                if not self.indexstart:
                    break
                self.indexend = self.chattextbox.search('}',self.indexstart)
                self.text1 = self.chattextbox.get(self.indexstart+'+4c',self.indexend)
                self.chattextbox.delete(self.indexstart,self.indexend+'+1c')
                exec("""
global commandbtn
def commandbtn(target=self.read_file,name='{'+self.text1+'}'):
    Thread(target=target,args=[name]).start()
""")                
                textlist.append(self.text1)
                commandlist.append(commandbtn)
                indexlist.append(self.indexstart)
            for i in range(len(commandlist)):
                self.btn = tk.Button(self.chattextbox,text=textlist[i],cursor='hand2',bd=2,relief='groove',fg='green',command=commandlist[i])
                self.chattextbox.window_create(indexlist[i],window=self.btn)
            
            commandlist = []
            indexlist = []
            textlist = []
            while 1:
                self.indexstart = self.chattextbox.search('链接:{','1.0')
                if not self.indexstart:
                    break
                self.indexend = self.chattextbox.search('}',self.indexstart)
                self.text2 = self.chattextbox.get(self.indexstart+'+4c',self.indexend)
                self.chattextbox.delete(self.indexstart,self.indexend+'+1c')
                exec("""
global commandbtn2
def commandbtn2(name=self.text2):
    wb.open(name)
""")                
                textlist.append(self.text2)
                commandlist.append(commandbtn2)
                indexlist.append(self.indexstart)
            for i in range(len(commandlist)):
                self.btn2 = tk.Button(self.chattextbox,text=textlist[i],cursor='hand2',bd=2,relief='groove',fg='blue',command=commandlist[i])
                self.chattextbox.window_create(indexlist[i],window=self.btn2)
            
            while 1:
                self.indexstart = self.chattextbox.search('表情:{','1.0')
                if not self.indexstart:
                    break
                self.indexend = self.chattextbox.search('}',self.indexstart)
                self.text3 = self.chattextbox.get(self.indexstart+'+4c',self.indexend)
                self.chattextbox.delete(self.indexstart,self.indexend+'+1c')
                def commandbtn3():
                    pass
                try:
                    p = tk.PhotoImage(file='files/image/INSemoji/'+self.text3+'.png')
                except:
                    p = tk.PhotoImage(file='files/image/逆天团队logo.png')
                self.btn3 = tk.Button(self.chattextbox,image=p,cursor='hand2',bd=2,relief='groove',command=commandbtn3)
                self.btn3.image = p
                self.chattextbox.window_create(self.indexstart, window=self.btn3)
            
            self.chattextbox.delete('end-1l','end')
            self.chattextbox.see('end')
            self.chattextbox['state'] = 'disable'
            self.chattextbox['fg'] = 'black'
    
    '''个人中心'''
    def opencentre(self):
        myapp = MyselfApp(alluserinfo)
        myapp.run()

loginapp = LoginApp()
loginapp.run()
if name != '':
    INSchatapp = MainApp(name)
    print('loading...')
    INSchatapp.run()