from tkinter import messagebox as msg
import pygame,sys,random,os,webbrowser as w,tkinter as tk,shutil

root = tk.Tk()
root.title('小轩电脑0.4')
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

real_system_site = os.path.expanduser("~")
system_site = real_system_site+'/学而思直播/code/cache/asset/小轩电脑/C/User/system'
system_site2 = '../小轩电脑/C/User/system'

try:
    with open(system_site+'/prove/the_prove.txt','r') as f:
        if f.read() != 'installed 0.4 Edition.':
            shutil.rmtree('../小轩电脑')
            part = 'install'
        else:
            part = 'main'
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
            with open('../小轩电脑/C/User/Admin/desktop/'+name,'w',encoding='utf-8') as f:
                f.write(textbox.get('0.0', 'end'))
            f.close()
            file_size = sum(sum(os.path.getsize(os.path.join(parent, file)) for file in files) for parent, dirs, files in os.walk(r'../小轩电脑'))/1024/1024
            txt_window.destroy()
        else:
            txt_window.destroy()
    sbar_y = tk.Scrollbar(txt_window)
    sbar_y.pack(side=tk.RIGHT,fill=tk.Y)
    textbox = tk.Text(txt_window,font=('黑体',15),yscrollcommand=sbar_y.set)
    try:
        with open('../小轩电脑/C/User/Admin/desktop/'+name,'r',encoding='utf-8') as f:
            text_list = f.read()
        f.close()
    except:
        text_list = ''
    textbox.insert('end',text_list)
    sbar_y.config(command=textbox.yview)
    textbox.pack()
    txt_window.protocol("WM_DELETE_WINDOW",txt_callback)

class File(object):
    def __init__(self,name,ty,pos,img='../小轩电脑/C/User/system/icon/未知格式文件.png'):
        self.name = name
        self.ty = ty
        self.text = self.name + self.ty
        if self.ty == '.txt':
            self.img = pygame.transform.scale(pygame.image.load('../小轩电脑/C/User/system/icon/文本文档.png'),(100,100))
        else:
            self.img = pygame.transform.scale(pygame.image.load(img),(100,100))
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
    findfilelist = os.listdir('../小轩电脑/C/User/Admin/desktop')
    filelist = []
    for i in range(len(findfilelist)):
        i_ip = findfilelist[i].split('.')
        filelist.append(File(i_ip[0],'.'+i_ip[1],(i%4*300,i//4*200+71)))
    file_size = sum(sum(os.path.getsize(os.path.join(parent, file)) for file in files) for parent, dirs, files in os.walk(r'../小轩电脑'))/1024/1024
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
                    mkdir('../小轩电脑/C/User/Admin/desktop')
                    mkdir('../小轩电脑/C/User/system/icon')
                    mkdir('../小轩电脑/C/User/system/prove')
                    copy_file('file/icon', '../小轩电脑/C/User/system/icon')
                    with open(system_site+'/prove/the_prove.txt','w') as f:
                        f.write('installed 0.4 Edition.')
                    f.close()
                    with open('../小轩电脑/C/User/Admin/desktop/my computer.txt','w') as f:
                        f.write('小轩电脑0.4 Edition 家庭版 -8MB')
                    f.close()
                    with open('../小轩电脑/C/User/Admin/desktop/abc.txt','w') as f:
                        f.write('这里可以打字！')
                    f.close()
                    with open('../小轩电脑/C/User/Admin/desktop/happy.txt','w') as f:
                        f.write('开心每一天！！！')
                    f.close()
                    with open('../小轩电脑/C/User/Admin/desktop/fly.txt','w') as f:
                        f.write('可以放飞自我，但不要过度哦~')
                    f.close()
                    with open('../小轩电脑/C/User/Admin/desktop/tip.txt','w') as f:
                        f.write('建议每次使用5分钟以内哦~')
                    f.close()
                    with open('../小轩电脑/C/User/Admin/desktop/next.txt','w') as f:
                        f.write('下一个版本：小轩电脑0.4专业版')
                    f.close()
                    update_all()
                    part = 'install_ok'
        screen.fill((255,255,255))
        show_text('衷心感谢您选择小轩系统！',pos=(11,11))
        show_text('安装完成后，您将得到小轩电脑0.4Edition家庭版',pos=(11,41))
        show_text('将会在(C:)盘的学而思软件-编程目录进行安装',pos=(11,71))
        show_text('在此过程中，请不要关闭程序或者关闭您的电脑',pos=(11,101))
        show_text('确保无误就按下空格键开始安装吧！',pos=(11,131))
        show_text('祝您使用愉快！',pos=(11,161))
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
        show_text('版本：小轩电脑0.4Edition',pos=(11,41))
        pygame.display.update()
        try:root.update()
        except:sys.exit()
    
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
                            if i_types[0] == '.txt':txt_w(i_types[1])
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    root.title('删除系统')
                    part = '删除系统'
        screen.fill((65,255,255))
        show_text('小轩电脑0.4 | '+str(round(file_size,2))+'MB/8MB',pos=(11,11))
        show_text('='*80,pos=(0,41))
        for i in filelist:
            i.draw()
        show_text('按下DELETE键删除系统',color=(0,0,0),pos=(11,750))
        if file_size > 8:
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
        show_text('错误问题：file_size > 8MB',color=(255,255,255),pos=(11,41))
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
                    root.title('回退到小轩电脑0.3Edition')
                    part = '回退'
                if event.key == pygame.K_n:
                    root.title('小轩电脑0.4')
                    part = 'main'
        screen.fill((100,100,100))
        show_text('在删除系统之前请三思！',color=(255,255,255),pos=(11,11))
        show_text('小轩电脑0.4:请不我删除我好吗？(O_O)呜呜呜(T_T)',color=(255,255,255),pos=(11,41))
        show_text('删除后，系统将回退到上一个最新发布版本(0.3)',color=(255,255,255),pos=(11,71))
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
                    shutil.rmtree('../小轩电脑')
                    w.open('https://code.xueersi.com/home/project/detail?lang=code&pid=28744363&version=offline&form=python&langType=python')
                    sys.exit()
                if event.key == ord('7'):
                    root.title('小轩电脑0.4')
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
        show_text('按下键盘选择您的答案，并在评论区回复！',color=(255,255,255),pos=(11,171))
        show_text('按下1：兼容性太差，我要回退！',color=(255,255,255),pos=(11,210))
        show_text('按下2：性能太垃圾，我要回退！',color=(255,255,255),pos=(11,240))
        show_text('按下3：用都用不了，我要回退！',color=(255,255,255),pos=(11,270))
        show_text('按下4：UI布局难受，我要回退！',color=(255,255,255),pos=(11,300))
        show_text('按下5：安全性不高，我要回退！',color=(255,255,255),pos=(11,330))
        show_text('按下6：各方面都烂，我要回退！',color=(255,255,255),pos=(11,360))
        show_text('按下7：搞错了，我还是重返小轩电脑0.4家庭版吧',color=(255,255,255),pos=(11,390))
        show_text('按下8：都垃圾，干脆一个都不用！！！',color=(255,255,255),pos=(11,420))
        pygame.display.update()
        try:root.update()
        except:sys.exit()