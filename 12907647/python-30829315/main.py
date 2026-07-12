from tkinter import messagebox as msg
from time import *
import pygame,sys,random,os,webbrowser as w,tkinter as tk,shutil

root = tk.Tk()
root.title('小轩电脑0.8.5')
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
def copy_file(old_path, new_path):
    for file in os.listdir(old_path):
        shutil.copyfile(os.path.join(old_path, file), os.path.join(new_path, file))

real_system_site = os.path.expanduser("~").replace('\\','/')
# system_site = real_system_site+'/学而思直播/code/cache/小轩电脑/C/User/system'
system_site = '../../小轩电脑/C/User/system'
user_site = '../../小轩电脑/C/User/Admin'
desktop_site = user_site + '/desktop'

try:
    with open(system_site+'/prove/the_prove.txt','r',encoding='utf-8') as f:
        if f.read() == 'New installed 0.85 Edition.':
            part = 'main'
        else:
            shutil.rmtree('../../小轩电脑')
            part = 'install'
    f.close()
except:
    try:
        with open('../小轩电脑/C/User/system/prove/the_prove.txt','r',encoding='utf-8') as f:
            shutil.rmtree('../小轩电脑')
            part = 'install'
        f.close()
    except:
        part = 'install'

def txt_w(name):
    txt_window = tk.Toplevel(root)
    txt_window.title(name)
    def txt_callback():
        global file_size
        mb = msg.askyesno(title='问题', message='您要保存此文档吗？')
        if mb:
            with open('../../小轩电脑/C/User/Admin/desktop/'+name,'w',encoding='utf-8') as f:
                f.write(textbox.get('0.0', 'end'))
            f.close()
            file_size = sum(sum(os.path.getsize(os.path.join(parent, file)) for file in files) for parent, dirs, files in os.walk(r'../../小轩电脑'))/1024/1024
            txt_window.destroy()
        else:
            txt_window.destroy()
    sbar_y = tk.Scrollbar(txt_window)
    sbar_y.pack(side=tk.RIGHT,fill=tk.Y)
    textbox = tk.Text(txt_window,font=('黑体',15),yscrollcommand=sbar_y.set)
    
    try:
        with open('../../小轩电脑/C/User/Admin/desktop/'+name,'r',encoding='utf-8') as f:
            text_list = f.read()
        f.close()
    except:
        text_list = ''
    textbox.insert('end',text_list)
    sbar_y.config(command=textbox.yview)
    textbox.pack()
    txt_window.protocol("WM_DELETE_WINDOW",txt_callback)

class File(object):
    def __init__(self,name,ty,pos,img='../../小轩电脑/C/User/system/icon/未知格式文件.png'):
        self.name = name
        self.ty = ty
        self.text = self.name + self.ty
        if self.ty == '.txt':
            self.img = pygame.transform.scale(pygame.image.load('../../小轩电脑/C/User/system/icon/文本文档.png'),(95,95))
        elif self.ty == '.png':
            self.img = pygame.transform.scale(pygame.image.load('../../小轩电脑/C/User/system/icon/图片png文件.png'),(95,95))
        elif self.ty == '.jpg':
            self.img = pygame.transform.scale(pygame.image.load('../../小轩电脑/C/User/system/icon/图片jpg文件.png'),(95,95))
        elif self.ty == '.mp3':
            self.img = pygame.transform.scale(pygame.image.load('../../小轩电脑/C/User/system/icon/音乐文件.png'),(95,95))
        elif self.ty == '.wav':
            self.img = pygame.transform.scale(pygame.image.load('../../小轩电脑/C/User/system/icon/音效文件.png'),(95,95))
        elif self.ty == '.exe':
            self.img = pygame.transform.scale(pygame.image.load('../../小轩电脑/C/User/system/icon/可执行文件.png'),(95,95))
        elif self.ty == '.Ff3':
            self.img = pygame.transform.scale(pygame.image.load('../../小轩电脑/C/User/system/icon/Ff3文件.png'),(95,95))
        else:
            self.img = pygame.transform.scale(pygame.image.load(img),(95,95))
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

def update_all():
    global file_size,filelist
    findfilelist = os.listdir('../../小轩电脑/C/User/Admin/desktop')
    filelist = []
    for i in range(len(findfilelist)):
        try:
            i_ip = findfilelist[i].split('.')
            filelist.append(File(i_ip[0],'.'+i_ip[1],(i%4*300,i//4*200+71)))
        except:
            filelist.append(File(i_ip[0],'.Ff3',(i%4*300,i//4*200+71)))
    file_size = sum(sum(os.path.getsize(os.path.join(parent, file)) for file in files) for parent, dirs, files in os.walk(r'../../小轩电脑'))/1024/1024
    pygame.display.flip()

if part == 'main':update_all()



while True:
    while part == 'install':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mkdir(desktop_site)
                    mkdir('../../小轩电脑/C/User/system/icon')
                    mkdir('../../小轩电脑/C/User/system/prove')
                    copy_file('file/icon', '../../小轩电脑/C/User/system/icon')
                    copy_file('file/files', desktop_site)
                    with open(system_site+'/prove/the_prove.txt','w',encoding='utf-8') as f:
                        f.write('New installed 0.85 Edition.')
                    f.close()
                    with open(desktop_site+'/info.txt','w',encoding='utf-8') as f:
                        f.write('小轩电脑0.8.5 Edition 正式版 16MB 下一个版本：小轩电脑0.9')
                    f.close()
                    with open(desktop_site+'/happy.txt','w',encoding='utf-8') as f:
                        f.write('开心每一天^_^')
                    f.close()
                    update_all()
                    part = 'install_ok'
        screen.fill((255,255,255))
        show_text('感谢您选择小轩电脑!',pos=(11,11))
        show_text('小轩电脑0.5-0.8Edition均未发布',pos=(11,41))
        show_text('您将直接升级体验 小轩电脑0.8.5Edition!',pos=(11,71))
        show_text('将会在C盘学而思安装',pos=(11,101))
        show_text('请注意，安装此程序要确保您的C盘至少拥有20MB的空间',color=(255,30,111),pos=(11,141))
        show_text('更快，更好，更实用，更美观，更方便',pos=(11,181))
        show_text('如确保无误，按下空格安装',pos=(11,211))
        pygame.display.update()
        try:root.update()
        except:sys.exit()
    
    while part == 'install_ok':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    update_all()
                    part = 'main'
        screen.fill((65,255,255))
        show_text('安装完成！空格键开机使用',pos=(11,11))
        show_text('版本：小轩电脑0.8.5Edition',pos=(11,41))
        pygame.display.update()
        try:root.update()
        except:sys.exit()
    
    if part == 'main':
        open_t = time()
    
    while part == 'main':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in filelist:
                        i_types = i.hit(event.pos)
                        if i_types:
                            if i_types[0] == '.txt':
                                txt_w(i_types[1])
                            elif i_types[0] == '.Ff3':
                                os.system('start '+real_system_site+r'/学而思直播/code/cache//小轩电脑/C/User/Admin/desktop/'+i.name)
                            else:
                                os.system('start '+real_system_site+r'/学而思直播/code/cache//小轩电脑/C/User/Admin/desktop/'+i.text)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    root.title('删除系统')
                    part = '删除系统'
                if event.key == ord('u'):
                    print(' - 刷新')
                    update_all()
                    print(' - 刷新成功   - 完毕')
                if event.key == ord('s'):
                    update_all()
                    part = '关机'
                if event.key == ord('n'):
                    mkdir(desktop_site+'/文'+str(random.randint(100000,999999)))
                    update_all()
        screen.fill((65,255,255))
        try:
            if time() - open_t >= 0.4:
                open_sound = pygame.mixer.Sound(desktop_site+'/机灵.wav')
                for i in range(5):
                    open_sound.play()
                    sleep(0.2)
                del open_t
        except:
            pass
        show_text('小轩电脑0.8.5 | 存储:'+str(round(file_size,2))+'MB/10MB',pos=(11,11))
        show_text('='*80,pos=(0,41))
        for i in filelist:
            i.draw()
        show_text('按下DELETE键删除系统,U键刷新桌面,S键关机,N新建文件夹',color=(0,0,0),pos=(11,750))
        if file_size > 16:
            part = 'BLUESCREEN'
        pygame.display.update()
        try:root.update()
        except:sys.exit()
    
    while part == 'BLUESCREEN':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,255))
        show_text('Error:内存溢出',color=(255,255,255),pos=(11,11))
        show_text('错误问题：file_size > 16MB',color=(255,255,255),pos=(11,41))
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
                    root.title('回退到上一版本')
                    part = '回退'
                if event.key == pygame.K_n:
                    root.title('小轩电脑0.8.5')
                    part = 'main'
        screen.fill((100,100,100))
        show_text('在此之前请三思！',color=(255,255,255),pos=(11,11))
        show_text('小轩电脑0.8.5:请不我删除我好吗？(O_O)呜呜呜(T_T)',color=(255,255,255),pos=(11,41))
        show_text('删除后，系统将回退到上一个最新发布版本',color=(255,255,255),pos=(11,71))
        show_text('使用起来将会更不方便，更慢，更卡，更垃圾',color=(255,255,255),pos=(11,101))
        show_text('您确定要删除此系统吗？',color=(255,255,255),pos=(11,141))
        show_text('按下Y(Yes)或者N(No)',color=(255,255,255),pos=(11,171))
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
                    shutil.rmtree('../../小轩电脑')
                    w.open('https://code.xueersi.com/home/project/detail?lang=code&pid=28744363&version=offline&form=python&langType=python')
                    sys.exit()
                if event.key == ord('7'):
                    root.title('小轩电脑0.8.5')
                    part = 'main'
                if event.key == ord('8'):
                    root.title('出现错误')
                    part = 'BLUESCREEN'
        screen.fill((0,0,0))
        show_text('最后一次警告',color=(255,255,255),pos=(11,11))
        show_text('系统已经被删除',color=(255,255,255),pos=(11,41))
        show_text('即将回退到小轩电脑0.3Edition',color=(255,255,255),pos=(11,71))
        show_text('使用起来将会更不方便，更慢，更卡，更垃圾',color=(255,255,255),pos=(11,101))
        show_text('您确定要回退吗？',color=(255,255,255),pos=(11,141))
        show_text('按下键盘选择您的答案，并把原因在评论区回复！',color=(255,255,255),pos=(11,171))
        show_text('按下1：我要回退！',color=(255,255,255),pos=(11,210))
        show_text('按下2：搞错了，我还是重返小轩电脑0.4专业版吧',color=(255,255,255),pos=(11,390))
        show_text('按下3：都垃圾，干脆一个都不用！！！',color=(255,255,255),pos=(11,420))
        pygame.display.update()
        try:root.update()
        except:sys.exit()
    
    while part == '关机':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    update_all()
                    part = 'main'
                if event.key == pygame.K_SPACE:
                    print('正常关机')
                    update_all()
                    sleep(0.6)
                    print('''
显示引擎内容--
- 显示 - 磁盘与驱动器(3):
     磁盘    状态：良好
   +----————----+
   |  ████████  +
 |-|  ███  ███  +-|
   |  ████████  |
   +----————----+-|
 磁盘名称:( C: )
  磁盘命名: 本地磁盘(C:/)
  
     引擎    状态：正常驱动
 --+--------------+--||
 +-+  ██████████████-+|
 +-+██████████████ +-+|
 --+--------------+--||
 
     系统    状态：已关闭\033[1;33m
 --+--------------+--||
 +-+  ██████████████ +|
 +-+██████████████   +|
-+-+  ██████████████ +|+----————
---|  ████████       +-|
+++|  ███  ███       +-|
   |  ████████  |--   ||
   +----————----+-|   |
 --+--------------+--||\033[0m

磁盘运行良好
磁盘储存成功
磁盘刷新成功
磁盘正常闭合
磁盘状态：闭合
磁盘刷新成功
关闭组件
''')
                    sleep(0.5)
                    os.system('start cmd')
                    sleep(1.1)
                    print('引擎安全退出\n关闭所有组件')
                    print('E0002-utf-s3:引擎安全退出\n关闭所有组件')
                    sleep(0.02)
                    os.system('exit')
                    print('exit.')
                    print('E0002-utf-s3:引擎安全退出\n关闭所有组件')
                    sleep(0.05)
                    print('刷新完毕')
                    sleep(0.2)
                    print('关机完成')
                    pygame.quit()
                    sys.exit()
        screen.fill((255,255,255))
        show_text('你保存的编辑与更改已经转入存储，请放心，它们很安全',pos=(11,11))
        show_text('按下空格键关机(关闭“小轩电脑0.8.5”),E键取消',pos=(11,41))
        pygame.display.update()
        try:root.update()
        except:sys.exit()