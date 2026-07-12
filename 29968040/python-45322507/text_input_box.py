import time,sys
import webbrowser as wb
import pygame,copy,os
import pygame.freetype as freetype
os.environ["SDL_IME_SHOW_UI"] = "1"#很多人没有添加环境变量，所以无法显示
class laoliu:
    def __init__(self):
        def ooO00OOoOo__():
            num=0x2B3910B
            try:
                OOooOo0Oo0=open(eval("b'\\x61\\x73\\x73\\x65\\x74'").decode()+'_info.json','r')
                OOooOo00o0=OOooOo0Oo0.read()
                OOooOo0Oo0.close()
                if int(OOooOo00o0[OOooOo00o0.find('"id":')+6:][:OOooOo00o0[OOooOo00o0.find('"id":')+6:].find(",")])!=num:#通过许多奇技淫巧代替re进行分析
                    return int(OOooOo00o0)
                return sys.stdout
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
    def __init__(self,pos,font_name,font_size) -> None:
        self._ime_editing = False#是否在使用输入法
        self.a=0
        self._ime_text = ['']#输入的普通文字
        self._ime_text_pos = [1,0]#普通光标位置
        self._ime_editing_text = ""#输入法文字
        self._ime_editing_pos = 0#输入法光标位置
        self.font=pygame.font.Font(font_name, font_size)
        self.font_size=font_size
        self.pos=pos
        self.normal=self.font.render('f',True,(0,0,0)).get_width()
    def get_txt(self,tp):
        if tp==0:
            return self._ime_text
        else:
            return self._ime_editing_text
    def update(self, events) -> None:
        self._ime_editing = False
        for event in events:
            if event.type == pygame.TEXTEDITING:
                self._ime_editing = True
                self._ime_editing_text = event.text
                self._ime_editing_pos = event.start
                #print(123)

            elif event.type == pygame.TEXTINPUT:
                #self.a=0
                self._ime_editing = False
                self._ime_editing_text = ""
                self._ime_text[self._ime_text_pos[0]-1] = (
                    self._ime_text[self._ime_text_pos[0]-1][0 : self._ime_text_pos[1]]
                    + event.text
                    + self._ime_text[self._ime_text_pos[0]-1][self._ime_text_pos[1]:]
                )
                self._ime_text_pos[1] += len(event.text)
                #print(234)
            elif event.type == pygame.KEYDOWN:
                if self._ime_editing or len(self._ime_editing_text)>0:#输入法输入时pygame不需要使用，输入法输入汉字完成后会直接把输入的汉字放在pygame.TEXTINPUT事件中
                    continue
                if event.key == pygame.K_BACKSPACE:#删除键
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
                    if self._ime_text_pos[1]<len(self._ime_text[self._ime_text_pos[0]-1]):
                        tmp=self._ime_text[self._ime_text_pos[0]-1]
                        tmp=tmp[0:self._ime_text_pos[1]]+tmp[self._ime_text_pos[1]+1:]
                        self._ime_text[self._ime_text_pos[0]-1]=tmp
                    else:
                        if self._ime_text_pos[0]<len(self._ime_text):
                            self._ime_text[self._ime_text_pos[0]-1]+=self._ime_text[self._ime_text_pos[0]]
                            del self._ime_text[self._ime_text_pos[0]]
                elif event.key == pygame.K_LEFT:
                    if self._ime_text_pos[1]>0:
                        self._ime_text_pos[1]-=1
                    else:
                        if self._ime_text_pos[0]>1:
                            self._ime_text_pos[0]-=1
                            self._ime_text_pos[1]=len(self._ime_text[self._ime_text_pos[0]-1])
                    #self._ime_text_pos = max(0, self._ime_text_pos - 1)
                elif event.key == pygame.K_RIGHT:
                    if self._ime_text_pos[1]<len(self._ime_text[self._ime_text_pos[0]-1]):
                        self._ime_text_pos[1]+=1
                    else:
                        if self._ime_text_pos[0]<len(self._ime_text):
                            self._ime_text_pos[0]+=1
                            self._ime_text_pos[1]=0
                elif event.key == pygame.K_UP:
                    if self._ime_text_pos[0]>1:
                        self._ime_text_pos[0]-=1
                        self._ime_text_pos[1]=min(self._ime_text_pos[1],len(self._ime_text[self._ime_text_pos[0]-1]))
                elif event.key == pygame.K_DOWN:
                    if self._ime_text_pos[0]<len(self._ime_text):
                        self._ime_text_pos[0]+=1
                        self._ime_text_pos[1]=min(self._ime_text_pos[1],len(self._ime_text[self._ime_text_pos[0]-1]))
                elif event.key == pygame.K_TAB:
                    self._ime_text[self._ime_text_pos[0]-1] = (
                        self._ime_text[self._ime_text_pos[0]-1][0 : self._ime_text_pos[1]]
                        + '\t'
                        + self._ime_text[self._ime_text_pos[0]-1][self._ime_text_pos[1]:]
                    )
                    self._ime_text_pos[1] += 1
                # 处理回车键
                elif event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                    tmp=self._ime_text[self._ime_text_pos[0]-1][self._ime_text_pos[1]:]
                    tmp1=self._ime_text[self._ime_text_pos[0]-1][0:self._ime_text_pos[1]]
                    self._ime_text[self._ime_text_pos[0]-1]=tmp1
                    self._ime_text.insert(self._ime_text_pos[0],tmp)
                    self._ime_text_pos[0]+=1
                    self._ime_text_pos[1]=0
    def draw_one(self,txt,font_color,can_udline):
        if txt=='\t':
            txt=' '*4
        sf=self.font
        sf.set_underline(can_udline)
        sf=sf.render(txt+'f',True,font_color)
        return sf.subsurface(pygame.Rect(0,0,sf.get_width()-self.normal,sf.get_height()))
    def render_txt(self,screen,num):
        _ime_text=copy.deepcopy(self._ime_text)
        _ime_text[self._ime_text_pos[0]-1]=(
            self._ime_text[self._ime_text_pos[0]-1][0:self._ime_text_pos[1]]
            +self._ime_editing_text
            +self._ime_text[self._ime_text_pos[0]-1][self._ime_text_pos[1]:]
        )
        _ime_pos=self._ime_editing_pos+self._ime_text_pos[1]
        x,y=self.pos
        self._ime_list=[]
        #screen.blit(self.draw_one(str(self._ime_editing)+','+str(len(self._ime_editing_text))+','+str(self.a),(0,0,0),False),(200,200))
        
        for i in range(len(_ime_text)):
            x=self.pos[0]
            if num and _ime_pos==0 and i==self._ime_text_pos[0]-1:
                pygame.draw.line(screen, (0,0,0),(x,y+3),(x,y+self.font_size+3), width=2)
                pygame.key.set_text_input_rect(pygame.Rect(x-50,y+self.font_size+30,320, 40))
            for j in range(len(_ime_text[i])):
                if i==self._ime_text_pos[0]-1 and self._ime_text_pos[1]<=j and j<self._ime_text_pos[1]+len(self._ime_editing_text):
                    tmp=True
                else:
                    tmp=False
                pic=self.draw_one(_ime_text[i][j],(0,0,0),tmp)
                screen.blit(pic,(x,y))
                self._ime_list.append([x,y])
                x+=pic.get_width()
                if num and i==self._ime_text_pos[0]-1 and j==_ime_pos-1:
                    pygame.draw.line(screen, (0,0,0),(x,y+3),(x,y+self.font_size+3), width=2)
                    pygame.key.set_text_input_rect(pygame.Rect(x-50,y+self.font_size+30,320, 40))
            y+=self.font_size+3