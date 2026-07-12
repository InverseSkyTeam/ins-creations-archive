from tkinter import messagebox as msg
import tkinter as tk
import pygame,sys,random,os,webbrowser as w

root = tk.Tk()
root.title('小轩电脑0.2')
root.geometry('1200x800+120+60')
pgw = tk.Frame(root,width = 1200, height = 800)
pgw.pack()
os.environ['SDL_WINDOWID'] = str(pgw.winfo_id())

pygame.init()
screen = pygame.display.set_mode((1400,900),pygame.NOFRAME)

try:import ntpath
except:font = pygame.font.SysFont('kaittf', 30)
else:font = pygame.font.SysFont('kaiti', 30);del ntpath

def show_text(text,color=(0,0,0),pos=(0,0)):
    screen.blit(font.render((text),True,color),pos)

part = 'main'
file_size = sum(sum(os.path.getsize(os.path.join(parent, file)) for file in files) for parent, dirs, files in os.walk(r'C：'))/1024

def txt_w(name):
    txt_window = tk.Toplevel(root)
    txt_window.title(name)
    def txt_callback():
        global file_size
        mb = msg.askyesno(title='问题', message='您要保存此文档吗？')
        if mb:
            with open(name,'w') as f:
                f.write(textbox.get('0.0', 'end'))
            f.close()
            file_size = sum(sum(os.path.getsize(os.path.join(parent, file)) for file in files) for parent, dirs, files in os.walk(r'C：'))/1024
            txt_window.destroy()
        else:
            txt_window.destroy()
    sbar_y = tk.Scrollbar(txt_window)
    sbar_y.pack(side=tk.RIGHT,fill=tk.Y)
    textbox = tk.Text(txt_window,font=('黑体',15),yscrollcommand=sbar_y.set)
    try:
        with open(name,'r') as f:
            text_list = f.read()
        f.close()
    except:
        if name == 'abc.txt':
            text_list = 'abc\n123\n你可以在这里打字！\n小轩电脑'
        elif name == 'abc2.txt':
            text_list = '这里也是txt文本文档，只要是文档都可以打字'
        elif name == 'my computer.txt':
            text_list = '逆天工作室©2015-2022 小轩电脑©2021,2022 -0.2 Edition -20KB'
        else:
            text_list = ''
    textbox.insert('end',text_list)
    sbar_y.config(command=textbox.yview)
    textbox.pack()
    txt_window.protocol("WM_DELETE_WINDOW",txt_callback)

class File(object):
    def __init__(self,name,ty,img,pos):
        self.name = name
        self.ty = ty
        self.text = self.name + self.ty
        self.img = pygame.transform.scale((pygame.image.load(img)),(100,100))
        self.rect = self.img.get_rect()
        self.rect.topleft = pos
    def draw(self):
        screen.blit(self.img,self.rect)
        show_text(self.text,pos=self.rect.bottomleft)
    def hit(self,pos):
        if self.rect.collidepoint(pos):
            return [self.ty,self.text]
        else:
            return False

txt_file1 = File('abc','.txt','C：/system/icon/文本文档.png',(0,71))
txt_file2 = File('abc2','.txt','C：/system/icon/文本文档.png',(300,71))
txt_file3 = File('a text file','.txt','C：/system/icon/文本文档.png',(600,71))
computer_txt_file = File('my computer','.txt','C：/system/icon/文本文档.png',(900,71))

while True:
    while part == 'main':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    get1 = txt_file1.hit(event.pos)
                    get2 = txt_file2.hit(event.pos)
                    get3 = txt_file3.hit(event.pos)
                    get4 = computer_txt_file.hit(event.pos)
                    if get1:txt_w(get1[1])
                    if get2:txt_w(get2[1])
                    if get3:txt_w(get3[1])
                    if get4:txt_w(get4[1])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    root.title('删除系统')
                    part = '删除系统'
        screen.fill((65,255,255))
        show_text('小轩电脑0.2 | '+str(round(file_size+1,2))+'KB/20KB',pos=(11,11))
        show_text('='*80,pos=(0,41))
        txt_file1.draw()
        txt_file2.draw()
        txt_file3.draw()
        computer_txt_file.draw()
        show_text('按下DELETE键可以删除系统哦~',color=(0,0,0),pos=(11,750))
        if file_size > 19:
            part = 'BLUESCREEN'
        pygame.display.update()
        try:root.update()
        except:sys.exit()
    
    while part == 'BLUESCREEN':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,170))
        show_text('Error:内存溢出',color=(255,255,255),pos=(11,11))
        show_text('错误问题：file_size > 20',color=(255,255,255),pos=(11,41))
        show_text('错误代码：Out Of Memory',color=(255,255,255),pos=(11,71))
        pygame.display.update()
        try:root.update()
        except:sys.exit()
    
    while part == '删除系统':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    root.title('回退到小轩电脑0.07Edition')
                    part = '回退'
                if event.key == pygame.K_n:
                    root.title('小轩电脑0.2')
                    part = 'main'
        screen.fill((100,100,100))
        show_text('在删除系统之前请三思！',color=(255,255,255),pos=(11,11))
        show_text('小轩电脑0.2Edition:请不我删除我好吗？(O_O)呜呜呜(T_T)',color=(255,255,255),pos=(11,41))
        show_text('删除后，系统将回退到上一个发布版本的最新版本(0.07)',color=(255,255,255),pos=(11,71))
        show_text('使用起来将会更不方便，更慢，更卡，更垃圾',color=(255,255,255),pos=(11,101))
        show_text('您确定要删除此系统吗？',color=(255,255,255),pos=(11,141))
        show_text('按下Y(yes)或者N(no)',color=(255,255,255),pos=(11,171))
        pygame.display.update()
        try:root.update()
        except:sys.exit()
    
    while part == '回退':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == ord('1') or event.key == ord('2') or event.key == ord('3') or event.key == ord('4') or event.key == ord('5') or event.key == ord('6'):
                    w.open('https://code.xueersi.com/home/project/detail?lang=code&pid=28744440&version=offline&form=python&langType=python')
                    sys.exit()
                if event.key == ord('7'):
                    root.title('小轩电脑0.2')
                    part = 'main'
                if event.key == ord('8'):
                    root.title('出现错误')
                    part = 'BLUESCREEN'
        screen.fill((0,0,0))
        show_text('最后一次警告',color=(255,255,255),pos=(11,11))
        show_text('系统已经被删除',color=(255,255,255),pos=(11,41))
        show_text('即将回退到小轩电脑0.07Edition',color=(255,255,255),pos=(11,71))
        show_text('使用起来将会更不方便，更慢，更卡，更垃圾',color=(255,255,255),pos=(11,101))
        show_text('您确定要回退吗？',color=(255,255,255),pos=(11,141))
        show_text('按下键盘选择您的答案！',color=(255,255,255),pos=(11,171))
        show_text('按下1：兼容性太差，我要回退！',color=(255,255,255),pos=(11,210))
        show_text('按下2：性能太垃圾，我要回退！',color=(255,255,255),pos=(11,240))
        show_text('按下3：用都用不了，我要回退！',color=(255,255,255),pos=(11,270))
        show_text('按下4：UI布局难受，我要回退！',color=(255,255,255),pos=(11,300))
        show_text('按下5：安全性不高，我要回退！',color=(255,255,255),pos=(11,330))
        show_text('按下6：各方面都烂，我要回退！',color=(255,255,255),pos=(11,360))
        show_text('按下7：搞错了，我还是重返小轩电脑0.2吧',color=(255,255,255),pos=(11,390))
        show_text('按下8：都垃圾，干脆一个都不用！！！',color=(255,255,255),pos=(11,420))
        pygame.display.update()
        try:root.update()
        except:sys.exit()