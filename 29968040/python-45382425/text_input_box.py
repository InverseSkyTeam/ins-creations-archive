import time,sys
import webbrowser as wb
import pygame,copy,os
import pygame.freetype as freetype
import code_light as cli
import pygame.locals
import pyperclip
import pygame.key
#os.environ["SDL_IME_SHOW_UI"] = "1"#很多人没有添加环境变量，所以无法显示

#print(os.environ.get('SDL_IME_SHOW_UI'))
ttt="""#你现在看到的是示例代码
#中文输入可能不兼容mac，windows系统部分输入法可能不兼容，推荐使用微软拼音输入法
#如果程序报错请及时提出，pygame版本≥2.1.4
'''
更新日志：
    v0.0.1 支持输入法等基本功能
    v0.0.2 支持点击选择光标位置
    v0.0.3 支持纵向滚动条（不支持拖动，但可以用滚轮）
    v0.1.0 支持代码高亮
    v0.1.1 给代码高亮加入特殊判断，字符串的搜索会更准确
    v0.1.2 初步的代码补全（自动加缩进）
    v0.2.0 滚动条支持鼠标拖动，添加横向滚动条，修复了亿些bug
    v0.2.1 支持粘贴功能
    v0.2.2 右键菜单
    v0.2.3 支持全选
    v0.2.4 在选中时的右键菜单
    v0.2.5 支持复制和剪切
    v0.3.0 修复搜狗输入法不兼容的bug
    v0.4.0 公测版本
    v0.4.1 修 @逆天小轩 提出的bug
'''
print('Hello world!')"""


#TODO 去掉这四行注释，可以让编辑器显示code_light.py的代码
#import codecs
#f=codecs.open('code_light.py','r','utf-8')
#ttt=f.read().replace('\r\n','\n').replace('\r','')
#f.close()

tnum=0.1#按键长按间隔
import time,sys
import webbrowser as wb
def ooO00OOoOo__():
    num=45382425
    num=int(num)
    try:
        OOooOo0Oo0=open(eval("b'\\x61\\x73\\x73\\x65\\x74'").decode()+'_info.json','r')#读取asset_info.json的内容
        OOooOo00o0=OOooOo0Oo0.read()
        OOooOo0Oo0.close()
        if int(OOooOo00o0[OOooOo00o0.find('"id":')+6:][:OOooOo00o0[OOooOo00o0.find('"id":')+6:].find(",")])!=num:#通过许多奇技淫巧代替re进行分析
            return int(OOooOo00o0)#如果是盗的作品，把输出函数改为一个错值，让程序报错，从而进入下面的excpet
        return sys.stdout#如果是原作，正常输出
    except:
        #输出提示信息
        print(chr(26816)+chr(27979)+chr(21040)+chr(36825)+chr(20010)+chr(20316)+chr(21697)+chr(26159)+chr(30423)+chr(21462)+chr(20182)+chr(20154)+chr(30340)+chr(20316)+chr(21697)+chr(65292)+chr(35831)+chr(21040)+chr(21407)+chr(20316)+chr(32773)+chr(32593)+chr(31449)+chr(19978)+chr(36816)+chr(34892))
        print(chr(51)+chr(31186)+chr(21518)+chr(33258)+chr(21160)+chr(36339)+chr(36716)+chr(33267)+chr(21407)+chr(20316)+chr(32773)+chr(32593)+chr(31449))
        time.sleep(2)
        #打开原作者网站
        wb.open(chr(104)+chr(116)+chr(116)+chr(112)+chr(115)+chr(58)+chr(47)+chr(47)+chr(99)+chr(111)+chr(100)+chr(101)+chr(46)+chr(120)+chr(117)+chr(101)+chr(101)+chr(114)+chr(115)+chr(105)+chr(46)+chr(99)+chr(111)+chr(109)+chr(47)+chr(104)+chr(111)+chr(109)+chr(101)+chr(47)+chr(112)+chr(114)+chr(111)+chr(106)+chr(101)+chr(99)+chr(116)+chr(47)+chr(100)+chr(101)+chr(116)+chr(97)+chr(105)+chr(108)+chr(63)+chr(108)+chr(97)+chr(110)+chr(103)+chr(61)+chr(99)+chr(111)+chr(100)+chr(101)+chr(38)+chr(112)+chr(105)+chr(100)+chr(61)+str(int(num))+chr(38)+chr(118)+chr(101)+chr(114)+chr(115)+chr(105)+chr(111)+chr(110)+chr(61)+chr(111)+chr(102)+chr(102)+chr(108)+chr(105)+chr(110)+chr(101)+chr(38)+chr(102)+chr(111)+chr(114)+chr(109)+chr(61)+chr(112)+chr(121)+chr(116)+chr(104)+chr(111)+chr(110)+chr(38)+chr(108)+chr(97)+chr(110)+chr(103)+chr(84)+chr(121)+chr(112)+chr(101)+chr(61)+chr(112)+chr(121)+chr(116)+chr(104)+chr(111)+chr(110))
        return sys.exit()

sys.stdout=ooO00OOoOo__()
print('',end='')

class TextInput:
    def __init__(self,pos,font_name,font_size,width,height) -> None:
        self._ime_text = ttt.split('\n')#输入的普通文字
        self._ime_text_pos = [1,0]#普通光标位置
        self._ime_editing_text = ""#输入法文字
        self._ime_editing_pos = 0#输入法光标位置
        self.font=pygame.font.Font(font_name, font_size)
        self.font_small=pygame.font.Font(font_name, 20)
        self.font_size=font_size
        self.pos=pos
        self.normal=self.font.render('f',True,(0,0,0)).get_width()
        self._ime_list=[]
        self.maxx=-99999
        self.WIDTH=width
        self.HEIGHT=height
        self.xuanzhong='None'#None或stop
        self.xz_pos=[[-1,-1],[-1,-1]]
        self.show_rect=False
        self.rect_pos=None
        self.in_rect_md=False
        self.in_xzmove=False
        self.ctrl=0
    def get_txt(self,tp):
        if tp==0:
            return self._ime_text
        else:
            return self._ime_editing_text
    def big(self,s,e):
        if s[0]>e[0]:
            return True
        if s[0]==e[0] and s[1]>e[1]:
            return True
        return False
    def check(self,s,e,n):#查找某个点是否在某个区间内
        if self.big(s,e):
            s,e=e,s
        if n[0]==s[0] and n[0]==e[0]:
            return (n[1]>=s[1] and n[1]<e[1])
        elif n[0]==s[0]:
            return n[1]>=s[1]
        elif n[0]==e[0]:
            return n[1]<e[1]
        elif n[0]>s[0] and n[0]<e[0]:
            return True
        else:
            return False
    
    def get_pos(self,mouse_pos):
        y=(mouse_pos[1]-self.pos[1])//(self.font_size+3)
        y=int(y)
        y=min(max(y+1,1),len(self._ime_text))
        #print(y)
        res=[y,None]
        y-=1
        x=0
        maxx=-1
        for i in self._ime_list:
            if i[1]==self.pos[1]+y*(self.font_size+3):
                if i[0]<mouse_pos[0]:
                    x+=1
                    maxx=max(maxx,i[0])
                else:
                    x=min(max(x-1,0),len(self._ime_text[y]))
                    res[1]=x
                    return res
        res[1]=min(max(x-1,0),len(self._ime_text[y]))#len(self._ime_text[y])-1
        if mouse_pos[0]-maxx>(self.font_size//2) and x>0:
            res[1]+=1
        #print(res)
        return res
    def clean_xuanzhong(self):
        s=copy.deepcopy(self.xz_pos[0])
        e=copy.deepcopy(self.xz_pos[1])
        if self.big(s,e):
            s,e=e,s
        self._ime_text_pos=copy.deepcopy(s)
        if s[0]==e[0]:
            self._ime_text[self._ime_text_pos[0]-1]=(
                self._ime_text[self._ime_text_pos[0]-1][:s[1]]+
                self._ime_text[self._ime_text_pos[0]-1][e[1]:]
                )
            self.xuanzhong='None'
            self.xz_pos=[[-1,-1],[-1,-1]]
            return 
        else:
            self._ime_text[s[0]-1]=self._ime_text[s[0]-1][:s[1]]+self._ime_text[e[0]-1][e[1]:]
            del self._ime_text[e[0]-1]
            if e[0]-s[0]>1:
                for i in range(e[0]-s[0]-1):
                    del self._ime_text[s[0]]
            self.xuanzhong='None'
            self.xz_pos=[[-1,-1],[-1,-1]]
            return 
    def get_xuanzhong(self):
        s=copy.deepcopy(self.xz_pos[0])
        e=copy.deepcopy(self.xz_pos[1])
        if self.big(s,e):
            s,e=e,s
        if s[0]==e[0]:
            return self._ime_text[self._ime_text_pos[0]-1][s[1]:e[1]]
        else:
            sstr=self._ime_text[s[0]-1][s[1]:]
            estr=self._ime_text[e[0]-1][:e[1]]
            if e[0]-s[0]>1:
                for i in range(s[0]+1,e[0]):
                    sstr=sstr+'\n'+self._ime_text[i-1]
            return sstr+'\n'+estr
    def update(self, events,can_mouse) -> None:
        self.pos[1]=min(max(self.HEIGHT-len(self.get_txt(0))*(self.font_size+3),self.pos[1]),20)
        if self.in_xzmove:
            pygame.key.stop_text_input()
        else:
            pygame.key.start_text_input()
        #print(0.5,self.xz_pos)
        for event in events:
            if event.type == pygame.TEXTEDITING:
                self.in_rect_md=False
                self.show_rect=False
                if self.xuanzhong!='None':
                    self.clean_xuanzhong()
                self._ime_editing_text = event.text
                self._ime_editing_pos = event.start
            elif event.type == pygame.TEXTINPUT:
                self.in_rect_md=False
                self.show_rect=False
                #print('a',self.xz_pos)
                if self.xuanzhong!='None':
                    self.clean_xuanzhong()
                #print(1)
                self._ime_editing_text = ""
                self._ime_text[self._ime_text_pos[0]-1] = (
                    self._ime_text[self._ime_text_pos[0]-1][0 : self._ime_text_pos[1]]
                    + event.text
                    + self._ime_text[self._ime_text_pos[0]-1][self._ime_text_pos[1]:]
                )
                self._ime_text_pos[1] += len(event.text)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:#删除键
                    self.in_rect_md=False
                    self.show_rect=False
                    if self.xuanzhong!='None':
                        self.clean_xuanzhong()
                    else:
                        if len(self._ime_text) > 0:
                            if self._ime_text_pos[1]==0:
                                if self._ime_text_pos[0]>1:
                                    self._ime_text_pos[0]-=1
                                    self._ime_text_pos[1]=len(self._ime_text[self._ime_text_pos[0]-1])
                                    self._ime_text[self._ime_text_pos[0]-1]+=self._ime_text[self._ime_text_pos[0]]
                                    del self._ime_text[self._ime_text_pos[0]]
                            else:
                                num=1
                                self._ime_text_pos[1]-=num
                                tmp=self._ime_text[self._ime_text_pos[0]-1]
                                tmp=tmp[0:self._ime_text_pos[1]]+tmp[self._ime_text_pos[1]+num:]
                                self._ime_text[self._ime_text_pos[0]-1]=tmp
                elif event.key == pygame.K_DELETE:
                    self.in_rect_md=False
                    self.show_rect=False
                    if self.xuanzhong!='None':
                        self.clean_xuanzhong()
                    else:
                        if self._ime_text_pos[1]<len(self._ime_text[self._ime_text_pos[0]-1]):
                            tmp=self._ime_text[self._ime_text_pos[0]-1]
                            tmp=tmp[0:self._ime_text_pos[1]]+tmp[self._ime_text_pos[1]+1:]
                            self._ime_text[self._ime_text_pos[0]-1]=tmp
                        else:
                            if self._ime_text_pos[0]<len(self._ime_text):
                                self._ime_text[self._ime_text_pos[0]-1]+=self._ime_text[self._ime_text_pos[0]]
                                del self._ime_text[self._ime_text_pos[0]]
                elif event.key == pygame.K_LEFT:
                    self.in_rect_md=False
                    self.show_rect=False
                    if self.xuanzhong!='None':
                        self.xuanzhong='None'
                        if not self.big(copy.deepcopy(self.xz_pos[0]),copy.deepcopy(self.xz_pos[1])):
                            self._ime_text_pos=copy.deepcopy(self.xz_pos[0])
                        self.xz_pos=[[-1,-1],[-1,-1]]
                    else:
                        if self._ime_text_pos[1]>0:
                            self._ime_text_pos[1]-=1
                        else:
                            if self._ime_text_pos[0]>1:
                                self._ime_text_pos[0]-=1
                                self._ime_text_pos[1]=len(self._ime_text[self._ime_text_pos[0]-1])
                elif event.key == pygame.K_RIGHT:
                    self.in_rect_md=False
                    self.show_rect=False
                    if self.xuanzhong!='None':
                        self.xuanzhong='None'
                        if self.big(copy.deepcopy(self.xz_pos[0]),copy.deepcopy(self.xz_pos[1])):
                            self._ime_text_pos=copy.deepcopy(self.xz_pos[0])
                        self.xz_pos=[[-1,-1],[-1,-1]]
                    else:
                        if self._ime_text_pos[1]<len(self._ime_text[self._ime_text_pos[0]-1]):
                            self._ime_text_pos[1]+=1
                        else:
                            if self._ime_text_pos[0]<len(self._ime_text):
                                self._ime_text_pos[0]+=1
                                self._ime_text_pos[1]=0
                elif event.key == pygame.K_UP:
                    self.in_rect_md=False
                    self.show_rect=False
                    if self.xuanzhong!='None':
                        self.xuanzhong='None'
                        if not self.big(copy.deepcopy(self.xz_pos[0]),copy.deepcopy(self.xz_pos[1])):
                            self._ime_text_pos=copy.deepcopy(self.xz_pos[0])
                        self.xz_pos=[[-1,-1],[-1,-1]]
                    else:
                        if self._ime_text_pos[0]>1:
                            self._ime_text_pos[0]-=1
                            self._ime_text_pos[1]=min(self._ime_text_pos[1],len(self._ime_text[self._ime_text_pos[0]-1]))
                elif event.key == pygame.K_DOWN:
                    self.in_rect_md=False
                    self.show_rect=False
                    if self.xuanzhong!='None':
                        self.xuanzhong='None'
                        if self.big(copy.deepcopy(self.xz_pos[0]),copy.deepcopy(self.xz_pos[1])):
                            self._ime_text_pos=copy.deepcopy(self.xz_pos[0])
                        self.xz_pos=[[-1,-1],[-1,-1]]
                    else:
                        if self._ime_text_pos[0]<len(self._ime_text):
                            self._ime_text_pos[0]+=1
                            self._ime_text_pos[1]=min(self._ime_text_pos[1],len(self._ime_text[self._ime_text_pos[0]-1]))
                elif event.key == pygame.K_TAB:
                    self.in_rect_md=False
                    self.show_rect=False
                    if self.xuanzhong!='None':
                        self.clean_xuanzhong()
                    self._ime_text[self._ime_text_pos[0]-1] = (
                        self._ime_text[self._ime_text_pos[0]-1][0 : self._ime_text_pos[1]]
                        + '\t'
                        + self._ime_text[self._ime_text_pos[0]-1][self._ime_text_pos[1]:]
                    )
                    self._ime_text_pos[1] += 1
                elif event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                    self.in_rect_md=False
                    self.show_rect=False
                    if self.xuanzhong!='None':
                        self.clean_xuanzhong()
                    tmp=self._ime_text[self._ime_text_pos[0]-1][self._ime_text_pos[1]:]
                    tmp1=self._ime_text[self._ime_text_pos[0]-1][0:self._ime_text_pos[1]]
                    self._ime_text[self._ime_text_pos[0]-1]=tmp1
                    res=''
                    for i in tmp1:
                        if i==' ' or i=='\t':
                            res+=i
                        else:
                            break
                    if len(tmp1)>0 and tmp1[-1]==':':
                        res+='\t'
                    self._ime_text.insert(self._ime_text_pos[0],res+tmp)
                    self._ime_text_pos[0]+=1
                    self._ime_text_pos[1]=0+len(res)
                    if self._ime_text_pos[0]==len(self._ime_text):
                        self.pos[1]-=(self.font_size+3)
                        self.pos[1]=min(max(self.HEIGHT-len(self.get_txt(0))*(self.font_size+3),self.pos[1]),20)
                elif (event.key in [pygame.K_RCTRL, pygame.K_LCTRL]) or self.ctrl:
                    pyg=pygame.key.get_pressed()
                    self.ctrl=1
                    #print(2)
                    #print('ctrl',self.ctrl)
                    if pyg[pygame.K_v]:
                        self.in_rect_md=False
                        self.show_rect=False
                        if self.xuanzhong!='None':
                            self.clean_xuanzhong()
                        pst=pyperclip.paste().split('\n')
                        if len(pst)==1:
                            self._ime_text[self._ime_text_pos[0]-1] = (
                                self._ime_text[self._ime_text_pos[0]-1][0 : self._ime_text_pos[1]]
                                + pst[0]
                                + self._ime_text[self._ime_text_pos[0]-1][self._ime_text_pos[1]:]
                            )
                            self._ime_text_pos[1] += len(pst[0])
                        elif len(pst)>=2:
                            tmp=self._ime_text[self._ime_text_pos[0]-1][self._ime_text_pos[1]:]
                            tmp1=self._ime_text[self._ime_text_pos[0]-1][0:self._ime_text_pos[1]]
                            self._ime_text[self._ime_text_pos[0]-1]=tmp1+pst[0]
                            self._ime_text.insert(self._ime_text_pos[0],pst[-1]+tmp)
                            if len(pst)>2:
                                for i in pst[-2:0:-1]:
                                    self._ime_text.insert(self._ime_text_pos[0],i)
                            self._ime_text_pos[0]+=(len(pst)-1)
                            self._ime_text_pos[1]=0+len(pst[-1])
                    if pyg[pygame.K_a]:
                        self.xuanzhong='stop'
                        self.xz_pos=[[1,0],[len(self._ime_text),len(self._ime_text[-1])]]
                        self._ime_text_pos=copy.deepcopy(self.xz_pos[1])
                    if self.xuanzhong=='stop':
                        if pyg[pygame.K_c]:
                            pyperclip.copy(self.get_xuanzhong())
                            self.in_rect_md=False
                            self.show_rect=False
                        if pyg[pygame.K_x]:
                            pyperclip.copy(self.get_xuanzhong())
                            self.clean_xuanzhong()
                            self.in_rect_md=False
                            self.show_rect=False
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_RCTRL, pygame.K_LCTRL]:
                    self.ctrl=0
                    #print(1)
        if can_mouse and not(pygame.mouse.get_pressed()[0]) and self.in_rect_md:
            self.in_rect_md=False
        if not self.in_rect_md and can_mouse:
            if not self.in_xzmove:
                if pygame.mouse.get_pressed()[0]:
                    pygame.key.stop_text_input()
                    pygame.key.start_text_input()
                    self._ime_editing_text=''
                    self._ime_editing_pos=0
                    mouse_pos=pygame.mouse.get_pos()
                    self._ime_text_pos=self.get_pos(mouse_pos)
                    self.xuanzhong='None'
                    self.xz_pos=[copy.deepcopy(self._ime_text_pos),[-1,-1]]
                    self.in_xzmove=True
                elif pygame.mouse.get_pressed()[2]:
                    pygame.key.stop_text_input()
                    pygame.key.start_text_input()
                    self._ime_editing_text=''
                    self._ime_editing_pos=0
                    if self.xuanzhong=='None':
                        mouse_pos=pygame.mouse.get_pos()
                        self._ime_text_pos=self.get_pos(mouse_pos)
                    self.show_rect=True
                    self.rect_pos=pygame.mouse.get_pos()
                    self.rect_pos=(min(self.rect_pos[0],self.WIDTH-80),self.rect_pos[1])
            if self.in_xzmove:
                pygame.key.stop_text_input()
                self._ime_editing_text=''
                self._ime_editing_pos=0
                if pygame.mouse.get_pressed()[0]:
                    tmp_pos=self.get_pos(pygame.mouse.get_pos())
                    if self._ime_text_pos!=tmp_pos:
                        self._ime_text_pos=copy.deepcopy(tmp_pos)
                        self.xz_pos[1]=copy.deepcopy(tmp_pos)
                        self.xuanzhong='stop'
                else:
                    if self.xz_pos[1]==self.xz_pos[0]:
                        self.xuanzhong='None'
                        self.xz_pos=[-1,-1]
                    self.in_xzmove=False
                    pygame.key.start_text_input()
                    self._ime_editing_text=''
                    self._ime_editing_pos=0
    def draw_one(self,txt,font_color,can_udline,bgcolor=None):
        if txt==' ':
            txt=' '*2
        if txt=='\t':
            txt=' '*8
        sf=self.font
        sf.set_underline(can_udline)
        sf=sf.render(txt+'f',True,font_color,bgcolor)
        return sf.subsurface(pygame.Rect(0,0,sf.get_width()-self.normal,sf.get_height()))
    def render_txt(self,screen,num,can_mouse):
        if self.maxx>self.WIDTH:
            self.pos[0]=max(20-(self.maxx-self.WIDTH),self.pos[0])
        else:
            self.pos[0]=20
        _ime_text=copy.deepcopy(self._ime_text)
        _ime_text[self._ime_text_pos[0]-1]=(
            self._ime_text[self._ime_text_pos[0]-1][0:self._ime_text_pos[1]]
            +self._ime_editing_text
            +self._ime_text[self._ime_text_pos[0]-1][self._ime_text_pos[1]:]
        )
        _ime_pos=self._ime_editing_pos+self._ime_text_pos[1]
        x,y=self.pos
        self._ime_list=[]
        if _ime_text!=['']:
            
            scanner = cli.Scanner('\n'.join(_ime_text))
            tokens = scanner.tokens()
            newcolor=cli.color(tokens)
        else:
            newcolor=None
        self.maxx=-99999
        mouse_x=-1
        mouse_y=-1
        for i in range(len(_ime_text)):
            x=self.pos[0]
            if num and _ime_pos==0 and i==self._ime_text_pos[0]-1:
                mouse_x=x
                mouse_y=y
                pygame.key.set_text_input_rect(pygame.Rect(x-50,y+self.font_size+30,320, 40))
            for j in range(len(_ime_text[i])):
                if i==self._ime_text_pos[0]-1 and self._ime_text_pos[1]<=j and j<self._ime_text_pos[1]+len(self._ime_editing_text):
                    tmp=True
                else:
                    tmp=False
                bgcolor=None
                if self.xuanzhong!='None':
                    if self.check(copy.deepcopy(self.xz_pos[0]),copy.deepcopy(self.xz_pos[1]),[i+1,j]):
                        bgcolor=(135, 206, 250)
                pic=self.draw_one(_ime_text[i][j],newcolor[i][j],tmp,bgcolor)
                screen.blit(pic,(x,y))
                self._ime_list.append([x,y])
                x+=pic.get_width()
                if num and i==self._ime_text_pos[0]-1 and j==_ime_pos-1:
                    mouse_x=x
                    mouse_y=y
                    pygame.key.set_text_input_rect(pygame.Rect(x-50,y+self.font_size+30,320, 40))
            self.maxx=max(self.maxx,abs((x+2*self.font_size)-self.pos[0]))
            y+=self.font_size+3
        pygame.draw.line(screen, (0,0,0),(mouse_x,mouse_y+3),(mouse_x,mouse_y+self.font_size+3), width=2)

        if self.show_rect==True:
            if self.xuanzhong=='None':
                tmp=0
                self.rect_pos=(self.rect_pos[0],min(self.rect_pos[1],self.HEIGHT-60))
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.rect_pos[0],self.rect_pos[1],80,60), width=0, border_radius=5)
                if can_mouse and pygame.Rect(self.rect_pos[0],self.rect_pos[1],80,30).collidepoint(pygame.mouse.get_pos()):
                    tmp=1
                    pygame.draw.rect(screen, (220,220,220), pygame.Rect(self.rect_pos[0],self.rect_pos[1],80,30), width=0, border_radius=5)
                if can_mouse and pygame.Rect(self.rect_pos[0],self.rect_pos[1]+30,80,30).collidepoint(pygame.mouse.get_pos()):
                    tmp=2
                    pygame.draw.rect(screen, (220,220,220), pygame.Rect(self.rect_pos[0],self.rect_pos[1]+30,80,30), width=0, border_radius=5)
                pygame.draw.rect(screen, (150,150,150), pygame.Rect(self.rect_pos[0],self.rect_pos[1],80,60), width=1, border_radius=5)
                screen.blit(self.font_small.render('粘贴',True,(0,0,0)),[self.rect_pos[0]+20,self.rect_pos[1]+5])
                screen.blit(self.font_small.render('全选',True,(0,0,0)),[self.rect_pos[0]+20,self.rect_pos[1]+5+30])
                if pygame.mouse.get_pressed()[0] and tmp==1:
                    self.in_rect_md=True
                    pst=pyperclip.paste().split('\n')
                    if len(pst)==1:
                        self._ime_text[self._ime_text_pos[0]-1] = (
                            self._ime_text[self._ime_text_pos[0]-1][0 : self._ime_text_pos[1]]
                            + pst[0]
                            + self._ime_text[self._ime_text_pos[0]-1][self._ime_text_pos[1]:]
                        )
                        self._ime_text_pos[1] += len(pst[0])
                    elif len(pst)>=2:
                        tmp=self._ime_text[self._ime_text_pos[0]-1][self._ime_text_pos[1]:]
                        tmp1=self._ime_text[self._ime_text_pos[0]-1][0:self._ime_text_pos[1]]
                        self._ime_text[self._ime_text_pos[0]-1]=tmp1+pst[0]
                        self._ime_text.insert(self._ime_text_pos[0],pst[-1]+tmp)
                        if len(pst)>2:
                            for i in pst[-2:0:-1]:
                                self._ime_text.insert(self._ime_text_pos[0],i)
                        self._ime_text_pos[0]+=(len(pst)-1)
                        self._ime_text_pos[1]=0+len(pst[-1])
                    self.show_rect=False
                    return
                if pygame.mouse.get_pressed()[0] and tmp==2:
                    self.in_rect_md=True
                    self.xuanzhong='stop'
                    self.xz_pos=[[1,0],[len(_ime_text),len(_ime_text[-1])]]
                    self._ime_text_pos=copy.deepcopy(self.xz_pos[1])
                    self.show_rect=False
                    return
            if self.xuanzhong=='stop':
                tmp=0
                self.rect_pos=(self.rect_pos[0],min(self.rect_pos[1],self.HEIGHT-120))
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.rect_pos[0],self.rect_pos[1],80,120), width=0, border_radius=5)
                if can_mouse and pygame.Rect(self.rect_pos[0],self.rect_pos[1],80,30).collidepoint(pygame.mouse.get_pos()):
                    tmp=1
                    pygame.draw.rect(screen, (220,220,220), pygame.Rect(self.rect_pos[0],self.rect_pos[1],80,30), width=0, border_radius=5)
                if can_mouse and pygame.Rect(self.rect_pos[0],self.rect_pos[1]+30,80,30).collidepoint(pygame.mouse.get_pos()):
                    tmp=2
                    pygame.draw.rect(screen, (220,220,220), pygame.Rect(self.rect_pos[0],self.rect_pos[1]+30,80,30), width=0, border_radius=5)
                if can_mouse and pygame.Rect(self.rect_pos[0],self.rect_pos[1]+60,80,30).collidepoint(pygame.mouse.get_pos()):
                    tmp=3
                    pygame.draw.rect(screen, (220,220,220), pygame.Rect(self.rect_pos[0],self.rect_pos[1]+60,80,30), width=0, border_radius=5)
                if can_mouse and pygame.Rect(self.rect_pos[0],self.rect_pos[1]+90,80,30).collidepoint(pygame.mouse.get_pos()):
                    tmp=4
                    pygame.draw.rect(screen, (220,220,220), pygame.Rect(self.rect_pos[0],self.rect_pos[1]+90,80,30), width=0, border_radius=5)
                pygame.draw.rect(screen, (150,150,150), pygame.Rect(self.rect_pos[0],self.rect_pos[1],80,120), width=1, border_radius=5)
                screen.blit(self.font_small.render('粘贴',True,(0,0,0)),[self.rect_pos[0]+20,self.rect_pos[1]+5])
                screen.blit(self.font_small.render('全选',True,(0,0,0)),[self.rect_pos[0]+20,self.rect_pos[1]+5+30])
                screen.blit(self.font_small.render('复制',True,(0,0,0)),[self.rect_pos[0]+20,self.rect_pos[1]+5+60])
                screen.blit(self.font_small.render('剪切',True,(0,0,0)),[self.rect_pos[0]+20,self.rect_pos[1]+5+90])
                if pygame.mouse.get_pressed()[0] and tmp==1:
                    self.in_rect_md=True
                    self.clean_xuanzhong()
                    pst=pyperclip.paste().split('\n')
                    if len(pst)==1:
                        self._ime_text[self._ime_text_pos[0]-1] = (
                            self._ime_text[self._ime_text_pos[0]-1][0 : self._ime_text_pos[1]]
                            + pst[0]
                            + self._ime_text[self._ime_text_pos[0]-1][self._ime_text_pos[1]:]
                        )
                        self._ime_text_pos[1] += len(pst[0])
                    elif len(pst)>=2:
                        tmp=self._ime_text[self._ime_text_pos[0]-1][self._ime_text_pos[1]:]
                        tmp1=self._ime_text[self._ime_text_pos[0]-1][0:self._ime_text_pos[1]]
                        self._ime_text[self._ime_text_pos[0]-1]=tmp1+pst[0]
                        self._ime_text.insert(self._ime_text_pos[0],pst[-1]+tmp)
                        if len(pst)>2:
                            for i in pst[-2:0:-1]:
                                self._ime_text.insert(self._ime_text_pos[0],i)
                        self._ime_text_pos[0]+=(len(pst)-1)
                        self._ime_text_pos[1]=0+len(pst[-1])
                    self.show_rect=False
                    return
                if pygame.mouse.get_pressed()[0] and tmp==2:
                    self.in_rect_md=True
                    self.xuanzhong='stop'
                    self.xz_pos=[[1,0],[len(_ime_text),len(_ime_text[-1])]]
                    self._ime_text_pos=copy.deepcopy(self.xz_pos[1])
                    self.show_rect=False
                    return
                if pygame.mouse.get_pressed()[0] and tmp==3:
                    self.in_rect_md=True
                    self.show_rect=False
                    pyperclip.copy(self.get_xuanzhong())
                    return
                if pygame.mouse.get_pressed()[0] and tmp==4:
                    pyperclip.copy(self.get_xuanzhong())
                    self.clean_xuanzhong()
                    self.in_rect_md=True
                    self.show_rect=False
                    return
            if pygame.mouse.get_pressed()[0]:
                self.show_rect=False