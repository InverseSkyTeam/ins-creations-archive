import pygame,sys,random,time
pygame.init()

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
screenw, screenh = screen.get_width(), screen.get_height()
bgimage = pygame.image.load('逆天.png')
mouseimages = [pygame.image.load('鼠标.png')]
mouseimages.append(pygame.transform.rotate(mouseimages[0],30))
mouseimage = mouseimages[0]

if screenw != 1920 or screenh != 1080:
    print('检测到显示器分辨率不是1920x1080，暂时不支持这种体验。可以尝试虚拟机。')
    pygame.quit()
    sys.exit()

try:import ntpath
except:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)")
else:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)")
finally:pass

class Text:
    def __init__(self,text,color=(0,0,0),pos=(0,0),size=30):
        self.set(text,color,pos,size)
    def set(self,text=0,color=0,pos=0,size=0):
        if text:
            self.text = text
        if color:
            self.color = color
        if pos:
            self.pos = pos
        if size:
            self.size = size
    def draw(self):
        show_text(self.text,self.color,self.pos,self.size)

class Button:
    def __init__(self,pos,text,leng):
        self.rect = pygame.Rect(pos,(leng,30))
        self.bg = (255,255,255)
        self.tp = False
        self.text = text
    def hit(self,p):
        if self.rect.collidepoint(p):
            self.bg = (200,200,231)
        else:
            self.bg = (255,255,255)
    def draw(self):
        pygame.draw.rect(screen,self.bg,self.rect,0)
        pygame.draw.rect(screen,(255,11,11),self.rect,2)
        show_text(self.text,(255,0,0),self.rect)

class Loadline:
    def __init__(self,pos):
        self.rect = pygame.Rect(pos,(500,50))
        self.own = pygame.Rect(pos,(0,50))
        self.success = False
    def go_on(self):
        if self.own.width < 415:
            self.own.width += random.randint(0,3)
        elif 466 < self.own.width < 476:
            if random.randint(1,35) == 1:
                self.own.width += random.randint(2,3)
        else:
            if random.randint(1,6) == 1:
                self.own.width += random.randint(1,2)
        if self.own.width > 500:
            self.own.width = 500
            self.success = True
    def draw(self):
        pygame.draw.rect(screen,(0,255,0),self.own,0)
        pygame.draw.rect(screen,(255,0,0),self.rect,2)
        if self.success:
            show_text('100% Complete'.format(round(self.own.width/5,1)),(255,0,0),self.rect)
        else:
            show_text('{}%'.format(round(self.own.width/5,1)),(255,0,0),self.rect)

class Area:
    def __init__(self,pos,size,title):
        self.rect = pygame.Rect(pos,size)
        self.titlerect = pygame.Rect((pos[0],pos[1]-30),(size[0],30))
        self.title = Text(title,(11,168,245),(self.rect.x,self.rect.y-30))
        self.includes = {}
    def include(self,name,obj):
        self.includes[name] = obj
    def son(self):
        return self.includes
    def draw(self):
        pygame.draw.rect(screen,(255,255,255),self.titlerect,0)
        pygame.draw.rect(screen,(11,168,245),self.titlerect,3)
        pygame.draw.rect(screen,(11,168,245),self.rect,3)
        self.title.draw()
        for i in self.includes:
            self.includes[i].draw()

loadlinearea = Area((50,190),(600,80),'全球逆天装置准备与载入 Ready Process')
loadlinearea.include('gobtn',Button((loadlinearea.rect.x+2,loadlinearea.rect.y+25),'>>',30))
loadlinearea.include('load',Loadline((loadlinearea.rect.x+50,loadlinearea.rect.y+15)))
timearea = Area((50,350),(500,50),'地球日期与时间 Earth DateTime')
timearea.include('time',Text('显示准备中...',pos=(timearea.rect.x+3,timearea.rect.y+10),color=(0,255,0)))
AIarea = Area((50,480),(510,200),'人工智能状态 AI State')
AIarea.include('t1',Text('INS-AT 中国-逆天',pos=(AIarea.rect.x+3,AIarea.rect.y+5),color=(255,255,255)))
AIarea.include('t2',Text('MOSS(550W) 中国-中科院',pos=(AIarea.rect.x+3,AIarea.rect.y+45),color=(255,255,255)))
AIarea.include('t3',Text('ChatSydney70 美国-OpenAI',pos=(AIarea.rect.x+3,AIarea.rect.y+85),color=(255,255,255)))
AIarea.include('t4',Text('Tsar-XB 俄罗斯-中央机械研究院',pos=(AIarea.rect.x+3,AIarea.rect.y+125),color=(255,255,255)))
AIarea.include('t5',Text('God-Free 联合国',pos=(AIarea.rect.x+3,AIarea.rect.y+165),color=(255,255,255)))
for i in range(1,6):
    AIarea.include('b'+str(i),Button((AIarea.rect.x+440,AIarea.rect.y-35+40*i),'启动',leng=60))

pygame.mixer.music.load('开启新征程2.mp3')
pygame.mixer.music.play(-1)
pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            loadlinearea.son()['gobtn'].hit(event.pos)
            for i in range(1,6):
                AIarea.son()['b'+str(i)].hit(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseimage = mouseimages[1]
            if loadlinearea.son()['gobtn'].rect.collidepoint(event.pos):
                loadlinearea.son()['gobtn'].tp = True
            for i in range(1,6):
                if AIarea.son()['b'+str(i)].rect.collidepoint(event.pos):
                    AIarea.son()['b'+str(i)].text = '启动' if AIarea.son()['b'+str(i)].text == '停机' else '停机'
        if event.type == pygame.MOUSEBUTTONUP:
            mouseimage = mouseimages[0]
    screen.fill((0,0,0))
    screen.blit(bgimage,(0,0))
    loadlinearea.draw()
    timearea.draw()
    AIarea.draw()
    if loadlinearea.son()['gobtn'].tp and not loadlinearea.son()['load'].success:
        loadlinearea.son()['load'].go_on()
    timearea.son()['time'].set(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()+1621919810.114514)))
    screen.blit(mouseimage,pygame.mouse.get_pos())
    pygame.display.update()