# 基于AS版创造
from tkinter import messagebox as msg
from xes.common import *
from time import *
import pygame,sys,random,os,shutil
import tkinter as tk,webbrowser as w
import opencv_film_player as ofp

root = tk.Tk()
root.title('小轩电脑1s')
# root.geometry('1400x900+120+60')
# root.geometry('800x600+120+60')
root.geometry('1200x800+120+60')
# pgw = tk.Frame(root,width = 1400, height = 900)
# pgw = tk.Frame(root,width = 800, height = 600)
pgw = tk.Frame(root,width = 1200, height = 800)
pgw.pack()
os.environ['SDL_WINDOWID'] = str(pgw.winfo_id())
# screen = pygame.display.set_mode((1400,900),pygame.NOFRAME)
# screen = pygame.display.set_mode((800,600),pygame.NOFRAME)
pygame.init()
screen = pygame.display.set_mode((1200,800),pygame.NOFRAME)

try:import ntpath
except:font = pygame.font.SysFont('kaittf', 30);font2 = pygame.font.SysFont('kaittf', 18)
else:font = pygame.font.SysFont('kaiti', 30);font2 = pygame.font.SysFont('kaiti', 18);del ntpath

def show_text(text,color=(0,0,0),pos=(0,0),font=font):
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
        try:
            shutil.copyfile(os.path.join(old_path, file), os.path.join(new_path, file))
        except:
            mkdir(new_path+'/'+file)
            copy_file(old_path+'/'+file, new_path+'/'+file)

def get_time():
    nowY = str(localtime()[0])
    nowM = str(localtime()[1])
    nowD = str(localtime()[2])
    nowh = localtime()[3]
    nowm = localtime()[4]
    nows = localtime()[5]
    wday = localtime()[6]
    if nowh == 24:nowh = 0
    if nowh > 12:nowh -= 12
    nowh = str(nowh)
    if nowm >= 10:nowm2 = str(nowm)
    else:nowm2 = '0'+str(nowm)
    if nows >= 10:nows2 = str(nows)
    else:nows2 = '0'+str(nows)
    if wday == 0:weekday = '周一'
    elif wday == 1:weekday = '周二'
    elif wday == 2:weekday = '周三'
    elif wday == 3:weekday = '周四'
    elif wday == 4:weekday = '周五'
    elif wday == 5:weekday = '周六'
    elif wday == 6:weekday = '周日'
    else:weekday = '未知星期，请反馈作者'
    return [nowY,nowM,nowD,nowh,nowm2,nows2,weekday]

def dataload(emoji_str):
	return ''.join(c if c <= '\uffff' else ''.join(chr(x) for x in struct.unpack('>2H', c.encode('utf-16be'))) for c in emoji_str)
def getinfo(id):
	s = requests.Session()
	headers = {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'Cookie': 'xesId=b524835904a4a420cba3dde34890bade; user-select=scratch;  xes_run_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIuY29kZS54dWVlcnNpLmNvbSIsImF1ZCI6Ii5jb2RlLnh1ZWVyc2kuY29tIiwiaWF0IjoxNjAxODA5NDcxLCJuYmYiOjE2MDE4MDk0NzEsImV4cCI6MTYwMTgyMzg3MSwidXNlcl9pZCI6bnVsbCwidWEiOiJNb3ppbGxhXC81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXRcLzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZVwvODUuMC40MTgzLjEyMSBTYWZhcmlcLzUzNy4zNiBFZGdcLzg1LjAuNTY0LjY4IiwiaXAiOiIxMTIuNDkuNzIuMTc1In0.9bXcb813GhSPhoUJkezZpV8O50ynm0hhYvszNyczznQ; prelogid=ef8f6d12febabf75bf9599744b73c6f5; xes-code-id=87f66376f1afd34f70339baeca61b7a1.8dbd833da9122d69a17f91054066dbb3; X-Request-Id=82f1c3968c8ff01ee151a0413f56aa84; Hm_lpvt_a8a78faf5b3e92f32fe42a94751a74f1=1601809487', 'Host': 'code.xueersi.com', 'Proxy-Connection': 'keep-alive', 'Referer': 'http://code.xueersi.com/space/11909587', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.68'}
	total = json.loads(dataload(s.get("http://code.xueersi.com/api/space/profile?user_id=" + str(id), headers=headers).text))["data"]
	return total["realname"]
try:
    num=getCookies().index("stu_id=")+7
    id=""
    for i in range(num,num+111):
        if getCookies()[i]!=";":
            id=id+getCookies()[i]
        else:
            break
    username = str(getinfo(id))
except:
    username = '游客'

real_system_site = os.path.expanduser("~").replace('\\','/')
# system_site = real_system_site+'/学而思直播/code/cache/小轩电脑/C/User/system'
system_site = '../../小轩电脑/C/User/system'
user_site = '../../小轩电脑/C/User/Admin'
desktop_site = user_site + '/desktop'

class Loading_line(object):
    def __init__(self,fool_load='\033[1;31m█\033[0m',real_load='\033[1;32m█\033[0m',length=100,edge=('|','-|')):
        self.length = length
        self.left_edge = edge[0]
        self.right_edge = edge[1]
        self.fool_load = fool_load
        self.real_load = real_load
    def do(self,text='加载中...',ca=4,wait=(1,5)):
        import time,random
        self.tip = text
        for self.i in range(int(self.length/ca)+1):
            print(self.tip)
            print(self.left_edge+(self.real_load*self.i)+(self.fool_load*(int(self.length/ca)-self.i))+self.right_edge,end=' ')
            if self.i != 0 and self.i != self.length/ca:
                print(str(self.i*ca+random.randint(-1,1))+'%')
            else:
                print(str(self.i*ca)+'%')
            time.sleep(random.randint(wait[0],wait[1])/100)
            self.clear()
        print(self.tip+'(100%)')
        time.sleep(0.4)
    def clear(self):
        print('\033[2J\033[100A\033[3J\033[100A')
loading_line = Loading_line()
loading_line.do('loading files...',8)
loading_line.do('update system......',8)
loading_line.do('update desktop',8)
loading_line.do('前置系统结构启动...',8)
print('请留意，可能弹出弹窗！')

try:
    with open(system_site+'/prove/the_prove.txt','r',encoding='utf-8') as f:
        if f.read() == 'New installed 1s Edition.':
            part = 'main'
            f.close()
        else:
            ask = input('检测到您拥有小轩电脑的以前版本~\n这个版本已经是GUI，非CUI版本\n但是更新到此版本需要卸载它！\n输入OK将您的文件存到一个文件夹，并放在桌面上\n输入其他则不保存\n如有重要文件，最好在选择之前备份一份文件，或上传到云端')
            if ask == 'OK' or ask == 'Ok' or ask == 'oK' or ask == 'ok' or ask == '拿捏':
                mkdir(real_system_site+'/desktop/小轩电脑旧版文件')
                copy_file(desktop_site, real_system_site+'/desktop/小轩电脑旧版文件')
                f.close()
            shutil.rmtree('../../小轩电脑')
            part = 'install'
            loading_line = Loading_line()
            loading_line.do('loading files...')
            loading_line.do('update system......',2)
            loading_line.do('update desktop',8)
            loading_line.do('restart...',8)
            loading_line.do('内置系统结构安装完成...',8)
            print('稍等一下...马上给您最新体验...马上就好...')
            sleep(0.5)
            print('海内存知己，天涯若比邻。')
            sleep(0.5)
            print('准备完成，点击任务栏上的最小化窗口')
except:
    try:
        with open('../小轩电脑/C/User/system/prove/the_prove.txt','r',encoding='utf-8') as f:
            shutil.rmtree('../小轩电脑')
            part = 'install'
        f.close()
    except:        part = 'install'

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

def attribute_open(filename,filetype):
    global username
    attribute_window = tk.Toplevel(root)
    attribute_window.title(filename+'.'+filetype+'的[*属性]')
    def exit_attribute_window():
        attribute_window.destroy()
    file_attribute_info_title = tk.Label(attribute_window,text=filename+'.'+filetype+'的属性:')
    file_attribute_info1 = tk.Label(attribute_window,text='文件名:'+filename)
    file_attribute_info2 = tk.Label(attribute_window,text='文件类型/后缀/扩展名:'+filetype)
    file_attribute_info3 = tk.Label(attribute_window,text='控制权:用户'+username+'与管理员'+username)
    file_attribute_info4 = tk.Label(attribute_window,text='文件加密:未加密')
    file_attribute_info5 = tk.Label(attribute_window,text='使用占用:几乎无占用')
    file_attribute_info6 = tk.Label(attribute_window,text='没有更多可以对这个文件解释的了。\n请见谅。')
    file_attribute_info_title.pack()
    file_attribute_info1.pack()
    file_attribute_info2.pack()
    file_attribute_info3.pack()
    file_attribute_info4.pack()
    file_attribute_info5.pack()
    file_attribute_info6.pack()
    exit_button = tk.Button(attribute_window,text='关闭"'+filename+'.'+filetype+'的[*属性]"窗口',command=exit_attribute_window)
    exit_button.pack()

def rename(name,Ff3=False):
    rename_window = tk.Toplevel(root)
    rename_window.title('重命名文件')
    def check_button_ok():
        global desktop_site
        try:
            if Ff3:
                os.rename(name,desktop_site+'/'+Entry.get())
            else:
                os.rename(name,desktop_site+'/'+Entry.get()+'.'+name.split('.')[-1])
        except:
            print('\ / : * ? " < > |')
            print('这些符号都是非法命名，请不要再取这样(包含已上符号)的名字')
        update_all()
        rename_window.destroy()
    Label = tk.Label(rename_window,text='命名的字符数范围必须在1-6个之间哦~')
    Entry = tk.Entry(rename_window)
    OK_button = tk.Button(rename_window,text='确定',command=check_button_ok)
    Canel_button = tk.Button(rename_window,text='取消')
    Label.pack()
    Entry.pack()
    OK_button.pack()

class File(object):
    def __init__(self,name,ty,pos,img='../../小轩电脑/C/User/system/icon/未知格式文件.png'):
        self.name = name
        self.ty = ty
        self.text = self.name + self.ty
        if self.ty == '.txt':
            self.img = pygame.transform.scale(pygame.image.load('../../小轩电脑/C/User/system/icon/文本文档.png'),(60,60))
        elif self.ty == '.png':
            self.img = pygame.transform.scale(pygame.image.load('../../小轩电脑/C/User/system/icon/图片png文件.png'),(60,60))
        elif self.ty == '.jpg':
            self.img = pygame.transform.scale(pygame.image.load('../../小轩电脑/C/User/system/icon/图片jpg文件.png'),(60,60))
        elif self.ty == '.mp3':
            self.img = pygame.transform.scale(pygame.image.load('../../小轩电脑/C/User/system/icon/音乐文件.png'),(60,60))
        elif self.ty == '.wav':
            self.img = pygame.transform.scale(pygame.image.load('../../小轩电脑/C/User/system/icon/音效文件.png'),(60,60))
        elif self.ty == '.exe':
            self.img = pygame.transform.scale(pygame.image.load('../../小轩电脑/C/User/system/icon/可执行文件.png'),(60,60))
        elif self.ty == '.Ff3':
            self.img = pygame.transform.scale(pygame.image.load('../../小轩电脑/C/User/system/icon/Ff3文件.png'),(60,60))
        else:
            self.img = pygame.transform.scale(pygame.image.load(img),(60,60))
        self.rect = self.img.get_rect()
        self.rect.topleft = pos
    def draw(self):
        screen.blit(self.img,self.rect)
        show_text(self.text,pos=self.rect.bottomleft,font=font2)
    def hit(self,pos):
        if self.rect.collidepoint(pos):
            return [self.ty,self.text]
        else:
            return False

class RightList(object):
    def __init__(self,pos,type_='type-normal'):
        self.show = False
        self.posx = pos[0]
        self.posy = pos[1]
        self.underpos = (self.posx+3,self.posy+3)
        self.buttonlist = []
        self.type = type_
        if self.type == 'type-normal':
            self.buttonlist.append((pygame.Rect(0,0,200,18),'打开',(238,238,238)))
            self.buttonlist.append((pygame.Rect(0,0,200,18),'重命名',(238,238,238)))
            self.buttonlist.append((pygame.Rect(0,0,200,18),'属性',(238,238,238)))
            self.buttonlist.append((pygame.Rect(0,0,200,18),'删除',(255,111,111)))
        else:
            self.buttonlist.append((pygame.Rect(0,0,200,18),'刷新',(238,238,238)))
            self.buttonlist.append((pygame.Rect(0,0,200,18),'新建文件夹',(238,238,238)))
            self.buttonlist.append((pygame.Rect(0,0,200,18),'关机',(180,180,180)))
            self.buttonlist.append((pygame.Rect(0,0,200,18),'卸载系统',(255,111,111)))
        self.rect = pygame.Rect(self.underpos,(200,len(self.buttonlist)*20))
    def draw(self):
        if self.show:
            pygame.draw.rect(screen,(80,80,80),self.rect,0)
            for self.button in range(len(self.buttonlist)):
                self.buttonlist[self.button][0].topleft = (self.posx,self.posy+20*self.button)
                pygame.draw.rect(screen,self.buttonlist[self.button][2],self.buttonlist[self.button][0],0)
                show_text(self.buttonlist[self.button][1],(40,40,40),(self.posx,self.posy+20*self.button),font2)

class TaskBar(object):
    def __init__(self):
        self.rect = pygame.Rect(0,750,1200,50)
        self.color = (220,230,225)
        self.show = True
        self.time_get = ''
        self.date = '0/0/0'
        self.time = '0:00:00'
        self.day = '未知'
    def new_time(self):
        self.time_get = get_time()
        self.date = '/'.join(self.time_get[:3])
        self.time = ':'.join(self.time_get[3:6])
        self.day = self.time_get[-1]
    def draw(self,update=False):
        if update:self.new_time()
        pygame.draw.rect(screen,self.color,self.rect,0)
        show_text(self.date+'  '+self.time+'  '+self.day,pos=(400,750))

def update_all():
    global file_size,filelist
    findfilelist = os.listdir('../../小轩电脑/C/User/Admin/desktop')
    filelist = []
    for i in range(len(findfilelist)):
        try:
            i_ip = findfilelist[i].split('.')
            filelist.append(File(i_ip[0],'.'+i_ip[1],(30+i//6*150,80+i%6*100)))
        except:
            filelist.append(File(i_ip[0],'.Ff3',(30+i//6*150,80+i%6*100)))
    file_size = sum(sum(os.path.getsize(os.path.join(parent, file)) for file in files) for parent, dirs, files in os.walk(r'../../小轩电脑'))/1024/1024
    pygame.display.flip()

if part == 'main':
    update_all()
    ofp.play('file/startfilms/小轩电脑1.0开机动画.mp4')
else:
    ofp.play('file/startfilms/逆天工作室动态logo.mp4')
    ofp.play('file/startfilms/小轩电脑1s开机动画.mp4')
rightlist = RightList((0,0))
taskbar = TaskBar()
colorful_egg = 0
Starting = True



while 1:
    while part == 'install':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mkdir(desktop_site)
                    mkdir('../../小轩电脑/C/User/system/icon')
                    mkdir('../../小轩电脑/C/User/system/start')
                    mkdir('../../小轩电脑/C/User/system/prove')
                    mkdir('../../小轩电脑/C/User/system/help')
                    copy_file('file/icon', '../../小轩电脑/C/User/system/icon')
                    copy_file('file/startfilms', '../../小轩电脑/C/User/system/start')
                    copy_file('file/help', '../../小轩电脑/C/User/system/help')
                    copy_file('file/files', desktop_site)
                    with open(system_site+'/prove/the_prove.txt','w',encoding='utf-8') as f:
                        f.write('New installed 1s Edition.')
                    f.close()
                    with open(desktop_site+'/info.txt','w',encoding='utf-8') as f:
                        f.write('小轩电脑1.0+Edition(1s)正式版 32MB\n开心每一天^_^')
                    f.close()
                    update_all()
                    install_ok_setup_image_index = 0
                    part = 'install_ok'
        screen.fill((255,255,255))
        show_text('感谢您选择小轩电脑!',pos=(11,11))
        show_text('小轩电脑持续发布',pos=(11,41))
        show_text('您将直接升级体验 小轩电脑 1s Edition!',pos=(11,71))
        show_text('将会在C盘学而思安装',pos=(11,101))
        show_text('请注意，要确保您的C盘至少拥有50MB的空间',color=(255,30,111),pos=(11,141))
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
                    if install_ok_setup_image_index < 7:
                        install_ok_setup_image_index += 1
                        install_ok_setup_image_value = pygame.image.load('../../小轩电脑/C/User/system/help/用户介绍-'+str(install_ok_setup_image_index)+'.png')
                    else:
                        part = 'install config'
                        config_progress = 1
        screen.fill((65,255,255))
        show_text('安装完成！空格键下一页(右面也是空格)',pos=(11,11))
        show_text('版本：小轩电脑1s Edition',pos=(11,41))
        if install_ok_setup_image_index > 0:
            screen.blit(install_ok_setup_image_value,(0,0))
        pygame.display.update()
        try:root.update()
        except:sys.exit()
    
    while part == 'install config':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if config_progress == 1:
                    if event.key == pygame.K_SPACE:
                        with open(system_site+'/start/sys_config_bgcolor.txt','w',encoding='utf-8') as f:
                            f.write('backgroundcolor=(150,170,230)')
                        f.close()
                        update_all()
                        config_progress = 2
                    if event.key == ord('a'):
                        with open(system_site+'/start/sys_config_bgcolor.txt','w',encoding='utf-8') as f:
                            f.write('backgroundcolor=(65,255,255)')
                        f.close()
                        update_all()
                        config_progress = 2
                    if event.key == ord('b'):
                        with open(system_site+'/start/sys_config_bgcolor.txt','w',encoding='utf-8') as f:
                            f.write('backgroundcolor=(66,255,66)')
                        f.close()
                        update_all()
                        config_progress = 2
                    if event.key == ord('c'):
                        with open(system_site+'/start/sys_config_bgcolor.txt','w',encoding='utf-8') as f:
                            f.write('backgroundcolor=(255,150,50)')
                        f.close()
                        update_all()
                        config_progress = 2
                    if event.key == ord('d'):
                        with open(system_site+'/start/sys_config_bgcolor.txt','w',encoding='utf-8') as f:
                            f.write('backgroundcolor=(233,255,255)')
                        f.close()
                        update_all()
                        config_progress = 2
                else:
                    if event.key == ord('a'):
                        with open(system_site+'/start/sys_config_username.txt','w',encoding='utf-8') as f:
                            f.write('username="'+username+'"')
                        f.close()
                        update_all()
                        part = 'main'
                    if event.key == ord('b'):
                        with open(system_site+'/start/sys_config_username.txt','w',encoding='utf-8') as f:
                            f.write('username="'+real_system_site.split('/')[-1]+'"')
                        f.close()
                        update_all()
                        part = 'main'
                    if event.key == ord('c'):
                        with open(system_site+'/start/sys_config_username.txt','w',encoding='utf-8') as f:
                            f.write('username="一只小极客"')
                        f.close()
                        update_all()
                        part = 'main'
                    if event.key == ord('d'):
                        with open(system_site+'/start/sys_config_username.txt','w',encoding='utf-8') as f:
                            f.write('username="人生真谛"')
                        f.close()
                        update_all()
                        part = 'main'
        if config_progress == 1:
            screen.fill((0,0,0))
            show_text('请选择背景颜色：',color=(255,255,255),pos=(11,11))
            show_text('1.青色(老式,按a)',color=(65,255,255),pos=(11,41))
            show_text('2.温馨(默认,按空格)',color=(150,170,230),pos=(11,71))
            show_text('3.绿色(诡异,按b)',color=(66,255,66),pos=(11,101))
            show_text('4.橙色(活力,按c)',color=(255,150,50),pos=(11,131))
            show_text('5.白净(朴素,按d)',color=(233,255,255),pos=(11,161))
        else:
            screen.fill((255,255,255))
            show_text('设置用户名：',pos=(11,11))
            show_text('1.'+username+'(编程社区,按a)',pos=(11,41))
            show_text('2.'+real_system_site.split('/')[-1]+'(用户名源,按b)',pos=(11,71))
            show_text('3.一只小极客(流行,按c)',pos=(11,101))
            show_text('4.人生真谛(流行,按d)',pos=(11,131))
        pygame.display.update()
        try:root.update()
        except:sys.exit()
    
    if part == 'main' and Starting:
        open_t = time()
        colorful_egg_ok = pygame.image.load(system_site+'/icon/彩蛋.jpg')
        Starting = False
        with open(system_site+'/start/sys_config_bgcolor.txt','r',encoding='utf-8') as f:
            exec(f.read())
        f.close()
        with open(system_site+'/start/sys_config_username.txt','r',encoding='utf-8') as f:
            exec(f.read())
        f.close()
    
    while part == 'main':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in filelist:
                        i_types = i.hit(event.pos)
                        if i_types and (not rightlist.show):
                            if i_types[0] == '.txt':
                                txt_w(i_types[1])
                            elif i_types[0] == '.Ff3':
                                os.system('start '+real_system_site+r'/学而思直播/code/cache//小轩电脑/C/User/Admin/desktop/'+i.name)
                            else:
                                os.system('start '+real_system_site+r'/学而思直播/code/cache//小轩电脑/C/User/Admin/desktop/'+i.text)
                    for i in rightlist.buttonlist:
                        if i[0].collidepoint(event.pos) and rightlist.show and rightlist.type=='type-normal':
                            if i[1] == '打开':
                                if rightlist.show.split('.')[1] == 'txt':
                                    txt_w(rightlist.show)
                                elif rightlist.show.split('.')[1] == 'Ff3':
                                    os.system('start '+real_system_site+r'/学而思直播/code/cache//小轩电脑/C/User/Admin/desktop/'+rightlist.show.split('.')[0])
                                else:
                                    os.system('start '+real_system_site+r'/学而思直播/code/cache//小轩电脑/C/User/Admin/desktop/'+rightlist.show)
                            if i[1] == '重命名':
                                if rightlist.show.split('.')[1] == 'Ff3':
                                    rename(desktop_site+'/'+rightlist.show.split('.')[0],True)
                                else:
                                    rename(desktop_site+'/'+rightlist.show)
                                update_all()
                                rightlist.show = False
                            if i[1] == '属性':
                                attribute_open(rightlist.show.split('.')[0],rightlist.show.split('.')[1])
                                update_all()
                                rightlist.show = False
                            if i[1] == '删除':
                                if rightlist.show.split('.')[1] == 'Ff3':
                                    shutil.rmtree(desktop_site+'/'+rightlist.show.split('.')[0])
                                else:
                                    os.remove(desktop_site+'/'+rightlist.show)
                                update_all()
                                rightlist.show = False
                        if i[0].collidepoint(event.pos) and rightlist.show and rightlist.type=='type-desktop':
                            if i[1] == '刷新':
                                update_all()
                                print(' - 刷新成功')
                                rightlist.show = False
                            if i[1] == '新建文件夹':
                                xx = 1
                                while not mkdir(desktop_site+'/新建文件夹'+str(xx)):
                                    xx += 1
                                update_all()
                                rightlist.show = False
                            if i[1] == '关机':
                                update_all()
                                part = '关机'
                                rightlist.show = False
                            if i[1] == '卸载系统':
                                root.title('删除系统')
                                part = '删除系统'
                                rightlist.show = False
                    rightlist.show = False
                if event.button == 3:
                    not_hit = 0
                    for i in filelist:
                        if i.hit(event.pos):
                            rightlist = RightList(event.pos)
                            rightlist.show = i.text
                        else:
                            not_hit += 1
                    if not_hit == len(filelist):
                        rightlist = RightList(event.pos,'type-desktop')
                        rightlist.show = 'desktop'
            if event.type == pygame.KEYDOWN:
                if colorful_egg != 'opened':
                    if event.key == ord('p'):
                        colorful_egg += 1
                        if colorful_egg == 3:
                            print('你好像知道了些什么')
                        elif colorful_egg == 4:
                            print('听说有一个彩蛋')
                        elif colorful_egg == 5:
                            print('马上就要打开密码，触发彩蛋了；；；')
                        elif colorful_egg == 6:
                            print('多点一次，彩蛋与你擦肩而过！！！')
                    if event.key == ord('o'):
                        print('恭喜触发内置彩蛋！！！')
                        if colorful_egg == 5:
                            colorful_egg = 'opened'
                    if event.key == ord('s'):
                        if taskbar.show:
                            taskbar.show = False
                        else:
                            taskbar.show = True
                    
        screen.fill(backgroundcolor)
        if colorful_egg == 'opened':
            screen.blit(colorful_egg_ok,(0,50))
        try:
            if time() - open_t >= 0.1:
                open_sound = pygame.mixer.Sound(desktop_site+'/开机音效.wav')
                open_sound.play()
                del open_t
        except:
            pass
        show_text('小轩电脑1s | 存储:'+str(round(file_size,3))+'MB/46MB',pos=(11,11))
        if colorful_egg != 'opened':show_text('='*80,pos=(0,41))
        for i in filelist:
            i.draw()
        if colorful_egg != 'opened':show_text('右键文件或桌面打开右键菜单,按s开关任务栏',color=(0,0,0),pos=(11,700))
        else:show_text('右键文件或桌面打开右键菜单,按s开关任务栏',color=(255,255,255),pos=(11,700))
        if rightlist.show:
            rightlist.draw()
        if taskbar.show:taskbar.draw(True)
        if file_size > 46:
            part = 'BLUESCREEN'
        pygame.display.update()
        try:root.update()
        except:sys.exit()
    
    while part == 'BLUESCREEN':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,240))
        show_text('Error:内存溢出',color=(255,255,255),pos=(11,11))
        show_text('错误问题：file_size > 46MB',color=(255,255,255),pos=(11,41))
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
                    root.title('小轩电脑1s')
                    part = 'main'
        screen.fill((100,100,100))
        show_text('在此之前请三思！',color=(255,255,255),pos=(11,11))
        show_text('小轩电脑1s(1.0+):请不我删除我好吗？(O_O)呜呜呜(T_T)',color=(255,255,255),pos=(11,41))
        show_text('系统将回退到上一个发布版本',color=(255,255,255),pos=(11,71))
        show_text('使用起来将会不方便/慢/卡/垃圾',color=(255,255,255),pos=(11,101))
        show_text('您确定要卸载此系统吗？',color=(255,255,255),pos=(11,141))
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
                if event.key == ord('1'):
                    shutil.rmtree('../../小轩电脑')
                    w.open('https://code.xueersi.com/home/project/detail?lang=code&pid=30865834&version=offline&form=python&langType=python')
                    sys.exit()
                if event.key == ord('2'):
                    root.title('小轩电脑1s')
                    part = 'main'
                if event.key == ord('3'):
                    root.title('出现错误')
                    part = 'BLUESCREEN'
        screen.fill((0,0,0))
        show_text('最后一次警告',color=(255,255,255),pos=(11,11))
        show_text('系统即将被删除',color=(255,255,255),pos=(11,41))
        show_text('即将回退到小轩电脑AS Edition',color=(255,255,255),pos=(11,71))
        show_text('使用起来将会更不方便，更慢，更卡，更垃圾',color=(255,255,255),pos=(11,101))
        show_text('您确定要回退吗？',color=(255,255,255),pos=(11,141))
        show_text('按下键盘选择您的答案，并把原因在评论区回复！',color=(255,255,255),pos=(11,171))
        show_text('按下1：我要回退！',color=(255,255,255),pos=(11,210))
        show_text('按下2：搞错了，我还是返回吧',color=(255,255,255),pos=(11,240))
        show_text('按下3：都垃圾，干脆一个都不用！',color=(255,255,255),pos=(11,270))
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
                    sleep(0.4)
                    print('''
显示引擎内容--------------->>>>>
- 显示 - 磁盘与驱动器(1):
     磁盘    状态：良好
 ——————————————————————————————————————————————
 +-+—+———————————————+—++—+———————————————+—+-+
 |-+—+———————————————+—++—+———————————————+—+-|
 |-|—+——————————————|—|||—+——————————————|—||-|
 |-|—|—████████████+|—|||—|—████████████+|—||-|
 |-|—|—█  █   █   █+|—|||—|—████████████+|—||-|
 |-|—|—████████████+|—|||—|—████████████+|—||-|
 |-|—+——————————————|—|||—+——————————————|—||-|
 |-+—+———————————————+—++—+———————————————+—+-|
 |-+—+———————————————+—++—+———————————————+—+-|
 |-|—+——————————————|—|||—+——————————————|—||-|
 |-|—|—████████████+|—|||—|—████████████+|—||-|
 |-|—|—██ █   █  ██+|—|||—|—█          █+|—||-|
 |-|—|—████████████+|—|||—|—████████████+|—||-|
 |-|—+——————————————|—|||—+——————————————|—||-|
 |-+—+———————————————+—++—+———————————————+—+-|
 +-+—+———————————————+—++—+———————————————+—+-+
 ——————————————————————————————————————————————
 
 *磁盘名称 C:
 **args-Software:磁盘命名: 小轩电脑系统1s(1.0+)本地磁盘(C:/)

磁盘/组件正常关闭
''')
                    sleep(0.2)
                    os.system('start cmd')
                    sleep(0.15)
                    print('完成endpy中...')
                    sleep(0.1)
                    print('完成system中...')
                    sleep(0.3)
                    print('刷新...')
                    sleep(0.09)
                    print('保存并刷新应该保存的设置')
                    sleep(1.11)
                    print('关机完成')
                    pygame.quit()
                    sys.exit()
        screen.fill((100,110,130))
        show_text('你保存的编辑与更改已经转入存储，请放心',pos=(11,11))
        show_text('按下空格键关机(关闭“小轩电脑1.0+”),E键取消',pos=(11,41))
        pygame.display.update()
        try:root.update()
        except:sys.exit()