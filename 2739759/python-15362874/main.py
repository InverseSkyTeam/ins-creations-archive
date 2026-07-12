import moviepy.editor
import tkinter
from moviepy.editor import *
root = tkinter.Tk()
root.geometry("900x350")
root.title("Python局域网通讯")
root.resizable(False,False)
def movie():
    # clip = VideoFileClip('v1.mp4')
    # clip= clip.resize(newsize=(1280,720))
    # clip.preview()
    import os
    os.system("v1.mp4")
def k():
    import pygame,sys
    pygame.init()
    try:
        import ntpath # 如果成功，那么是Windows
        FONTNAME = "Simhei"
        del ntpath
    except ImportError: # 如果失败，是MacOS
        FONTNAME = "heititf"
    pygame.display.set_caption("Mac工作室logo")
    clip = VideoFileClip('logo.gif')
    clip= clip.resize(newsize=(1280,720))
    clip.preview()
    screen = pygame.display.set_mode((1280,720))
    logo = pygame.image.load("logo_img.png")
    logo = pygame.transform.scale(logo,(1280,720))
    for i in range(300):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255,255,255))
        screen.blit(logo,(-1,-1))
        screen.blit(pygame.font.SysFont(FONTNAME,50).render("Mac工作室",True,(0,0,0)),(550,575.0))
        screen.blit(pygame.font.SysFont(FONTNAME,20).render("极致、极爱、极简",True,(0,0,0)),(580,625.0))
        pygame.display.update()
    pygame.quit()
    import tkinter as tk
    import socket
    import sys
    from threading import Thread
    def p():
        root = tk.Tk()
        root.config(bg="red")
        HOST = socket.gethostname()
        PORT = 3001
        BUFSIZ = 1024
        ADDR = (w.get(), PORT)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(ADDR)
        
        
        def recv(cs):
            while 1:
                lb.insert("end", ":".join(map(str, cs.getsockname())) + "：" + cs.recv(BUFSIZ).decode())
        
        
        def send():
            s.sendall(send_box.get().encode())
            lb.insert("end", "我：" + send_box.get())
            send_box.delete("0","end")
        
        
        def over():
            root.destroy()
            sys.exit()
        
        
        
        root.protocol("WM_DELETE_WINDOW",over)
        lb = tk.Listbox(root, width=100, height=30)
        lb.pack(pady=5,padx=5)
        send_box = tk.Entry(root, width=90)
        send_box.pack(pady=5, padx=5, side="left")
        send_button = tk.Button(root,text="发送",width=8,command=send)
        send_button.pack(padx=5, pady=5, side="right")
        Thread(target=recv, args=(s,)).start()
        root.mainloop()
    r = tk.Tk()
    r.title("局域网通讯——客户端")
    w = tk.Entry(r,width = 20)
    w.grid(row = 0,column = 0)
    a = tk.Button(r,text = "请输入服务端电脑的IP地址，点我提交",command = p)
    a.grid(row = 0,column = 1)
def f():
    import pygame,sys
    pygame.init()
    try:
        import ntpath # 如果成功，那么是Windows
        FONTNAME = "Simhei"
        del ntpath
    except ImportError: # 如果失败，是MacOS
        FONTNAME = "heititf"
    pygame.display.set_caption("Mac工作室logo")
    clip = VideoFileClip('logo.gif')
    clip= clip.resize(newsize=(1280,720))
    clip.preview()
    screen = pygame.display.set_mode((1280,720))
    logo = pygame.image.load("logo_img.png")
    logo = pygame.transform.scale(logo,(1280,720))
    for i in range(300):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((255,255,255))
        screen.blit(logo,(-1,-1))
        screen.blit(pygame.font.SysFont(FONTNAME,50).render("Mac工作室",True,(0,0,0)),(550,575.0))
        screen.blit(pygame.font.SysFont(FONTNAME,20).render("极致、极爱、极简",True,(0,0,0)),(580,625.0))
        pygame.display.update()
    pygame.quit()
    import socket
    import sys
    import tkinter as tk
    from threading import Thread
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 3001))
    s.listen(5)
    g_conn = []
    
    
    def con():
        while 1:
            cs, addr = s.accept()
            print("{} is connecting".format(str(addr)))
            g_conn.append(cs)
            tl = Thread(target=recv, args=(cs,))
            tl.start()
    
    
    def recv(cs):
        while 1:
            txt = cs.recv(1024).decode()
            for i in g_conn:
                if i != cs:
                    i.sendall(txt.encode())
    
            lb.insert("end", ":".join(map(str, cs.getsockname())) + "：" + txt)
    
    
    def del_window():
        root.destroy()
        sys.exit(0)
    
    
    def send():
        for i in g_conn:
            i.sendall(send_box.get().encode())
        lb.insert("end", "我：" + send_box.get())
        send_box.delete("0","end")
    
    
    root = tk.Tk()
    root.config(bg="red")
    lb = tk.Listbox(root, width=100, height=30)
    lb.pack(padx=5, pady=5)
    send_box = tk.Entry(root, width=90)
    send_box.pack(pady=5, padx=5, side="left")
    send_button = tk.Button(root,text="发送",width=8,command=send)
    send_button.pack(padx=5, pady=5, side="right")
    Thread(target=con).start()
    root.mainloop()
word = tkinter.Label(root,text = "Python局域网通讯",font = ("kaiti",70))
word.pack()
button1 = tkinter.Button(root,text = "观看视频",command = movie)
button1.pack()     
button2 = tkinter.Button(root,text = "局域网通讯——客户端",command = k)
button2.pack()     
button3 = tkinter.Button(root,text = "局域网通讯——服务端",command = f)
button3.pack()
root.mainloop()