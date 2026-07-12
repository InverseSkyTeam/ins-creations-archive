from files.lib import cloudlib as clib
import tkinter as tk
import time

name = input('输入你的社区名:')

class MainApp(object):
    def __init__(self,username):
        self.name = 'mainapp'
        self.username = username
        self.root = tk.Tk()
        # self.root.configure(background='black')
        self.root.geometry('1080x640+100+11')
        self.root.iconbitmap('files/image/cloud_icon.ico')
        self.root.title('INS-Chat V0.5')
        self.movefront()
        
        self.leftframe = tk.Frame(self.root,bd=3,bg='white',relief='groove')
        self.leftframe.pack(side='left',fill='both',expand=True)
        self.rightframe = tk.Frame(self.root,bg='white',relief='flat')
        self.rightframe.pack(side='right',fill='both')
        self.righttopframe = tk.Frame(self.rightframe,bd=3,relief='groove')
        self.righttopframe.pack(fill='both')
        self.rightbottomframe = tk.Frame(self.rightframe,bd=3,relief='groove')
        self.rightbottomframe.pack(side='bottom',fill='both',expand=True)
        
        tk.Label(self.leftframe,text=self.username+'在线上').pack()
        
        self.chattextbox = tk.Text(self.righttopframe,font=('楷体',16),
        height=25,relief='flat',cursor='arrow',bg='white',state='disable')
        self.chattextbox.pack(fill='both')
        
        self.sendtextbox = tk.Text(self.rightbottomframe,font=('楷体',15),
        width=70,height=5,relief='flat',bg='white')
        self.sendtextbox.pack(side='left',fill='y')
        self.sendbutton = tk.Button(self.rightbottomframe,bd=0,relief='flat',
        font=('楷体',20,'bold'),text='   发 送   ',bg='lightgreen',
        activebackground='lightskyblue',activeforeground='black',
        highlightthickness=0,cursor='hand2',command=self.send)
        self.sendbutton.pack(side='right',fill='y',expand=True)
        
    def movefront(self):
        self.root.lift()
        self.root.attributes('-topmost',True)
        self.root.attributes('-topmost',False)
    
    def run(self):
        self.root.mainloop()
    
    # 云端操作
    def send(self):
        content = time.strftime('[%Y-%m-%d %H:%M:%S]')+self.username+':'+self.sendtextbox.get('1.0','end')
        self.chattextbox['state'] = 'normal'
        self.chattextbox.insert('end',content)
        self.save()
    
    def save(self):
        content = self.chattextbox.get('1.0','end')
        self.chattextbox['state'] = 'disable'
        clib.save_to_cloud('逆天聊-历史消息-小轩端#01',content,12907647)
    
    def clear(self):  # 聊天软件管理员用的函数
        clib.save_to_cloud('逆天聊-历史消息-小轩端#01','',12907647)
    
    def load(self):
        content = clib.read_from_cloud('逆天聊-历史消息-小轩端#01',12907647)
        self.chattextbox['state'] = 'normal'
        self.chattextbox.delete('1.0','end')
        self.chattextbox.insert('1.0',content)
        self.chattextbox['state'] = 'disable'

INSchatapp = MainApp(name)
# INSchatapp.clear()
INSchatapp.load()
INSchatapp.run()