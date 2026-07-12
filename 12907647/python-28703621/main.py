from tkinter import messagebox as msg
import tkinter as tk
import pygame,sys,random,os

root = tk.Tk()
root.title('小轩电脑0.06')
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

def txt_w(name):
    global file_size
    txt_window = tk.Toplevel(root)
    txt_window.title(name)
    def txt_callback():
        mb = msg.askyesno(title='问题', message='您要保存此文档吗？')
        if mb:
            with open(name,'w') as f:
                f.write(textbox.get('0.0', 'end'))
            f.close()
            file_size = sum(sum(os.path.getsize(os.path.join(parent, file)) for file in files) for parent, dirs, files in os.walk(r'../'))//1024
            txt_window.destroy()
        else:
            pass
    sbar_y = tk.Scrollbar(txt_window)
    sbar_y.pack(side=tk.RIGHT,fill=tk.Y)
    textbox = tk.Text(txt_window,font=('黑体',15),yscrollcommand=sbar_y.set)
    try:
        with open(name,'r') as f:
            text_list = f.read()
        f.close()
    except:
        if name == 'abc.txt':
            text_list = 'abc\n12345\n你可以在这里打字！\n小轩电脑'
        elif name == 'my computer.txt':
            text_list = '小轩电脑 -16KB -0.06'
        else:
            text_list = ''
    textbox.insert('end',text_list)
    sbar_y.config(command=textbox.yview)
    textbox.pack()
    txt_window.protocol("WM_DELETE_WINDOW",txt_callback)

abcr = pygame.Rect(0,71,1200,30)
Vr = pygame.Rect(0,101,1200,30)
part = 'main'
file_size = sum(sum(os.path.getsize(os.path.join(parent, file)) for file in files) for parent, dirs, files in os.walk(r'./'))//1024

while True:
    while part == 'main':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if abcr.collidepoint(event.pos):
                        txt_w('abc.txt')
                    if Vr.collidepoint(event.pos):
                        txt_w('V0.04 - 64 bit.txt')
        screen.fill((65,255,255))
        pygame.draw.rect(screen,(128,128,128),abcr,0)
        pygame.draw.rect(screen,(76,76,76),Vr,0)
        show_text('小轩电脑0.06 | '+str(3+file_size)+'KB/16KB',color=(0,0,0),pos=(11,11))
        show_text('='*80,color=(0,0,0),pos=(0,41))
        show_text('abc.txt',color=(0,0,0),pos=(0,71))
        show_text('abc2.txt',color=(0,0,0),pos=(0,101))
        show_text('my computer.txt',color=(0,0,0),pos=(0,131))
        show_text('这是小轩电脑0.06',color=(255,255,255),pos=(0,161))
        show_text('None',color=(0,0,0),pos=(0,191))
        pygame.display.flip()
        try:
            root.update()
        except:
            sys.exit()
    while part == 'BLUESCREEN':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,180))
        show_text('Error:内存溢出',color=(255,255,255),pos=(11,11))
        try:
            root.update()
        except:
            sys.exit()