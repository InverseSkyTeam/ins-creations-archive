# 方法来自小轩从网上搜集的结果
# 对绑定方法进行优化
import tkinter as tk, win32gui
import pygame,sys,os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'

root = tk.Tk()
root.geometry('600x600')
root.title('tkinter with pygame2+')
pygame.init()
screen = pygame.display.set_mode((500,500))

f = tk.Frame(root,width=500,height=500)
f.pack()

pygamewid = pygame.display.get_wm_info()['window']
tkframewid = f.winfo_id()
win32gui.SetParent(pygamewid,tkframewid)

def change():
    screen.fill((0,0,int(entry.get())))

entry = tk.Entry(root)
button = tk.Button(root,text='切换pygame整数蓝色值到以上值(0<=值<=255)',command=change)
entry.pack()
button.pack()

while True:
    try:
        root.update()
    except:
        print('感谢体验。同时致以yzy解决tk和pygame2+无法绑定的问题（代码简单易懂')
        print('GUI界的融合。没有解决不了的问题')
        print('甚至解决了pygame和tkinter的光标争夺问题等。也很简便。sdl麻烦一边去（')
        print('坏处是只能用于windows，因为这是windows的系统函数调用的句柄绑定，mac需要其它库')
        print('这是《pygame2+不能嵌入tkinter窗口？GUI界和系统底层api函数操控句柄配合的力量》作品。')
        break
    pygame.display.update()
    pygame.time.delay(50)