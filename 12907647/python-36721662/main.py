'''
彩蛋1:209行
'''
from time import *
import sys,random,math

def clear():
    print('\033[2J\033[100A\033[3J\033[100A'*8)

print('''In Ball World [Version 0.1.1 -Aplha]
Build 111
(c)INS-jhx Copyright. All right reserved.


Welcome to the Game <In Ball World>!
Language:English
Type "help" to show the helpbook.

''')
while input('do >>') != 'help':
    print('unknow command.')
print('Hello,my friend!')
print('Comands---------')
print('''[view]view somthing to play
[quit]quit the game
[exit]same with the [quit]
[next]same with the [view]
''')
while True:
    key = input('do >>')
    if key == 'view' or key == 'next':
        break
    elif key == 'exit' or key == 'quit':
        sys.exit()
print('plays------')
print('installed - [In Ball World 2022]')
print('commands------')
print('[run]run the game[In Ball World 2022]')
while input('do >>') != 'run':
    print('unknow command.')
print('(loading In Ball World 2022)')
for i in range(11):
    print('.',end='')
    sleep(random.randint(1,4)/20)
sleep(1)
clear()
sleep(0.16)
print(' start the game{-}')

like = {}

sleep(0.4)
print('''
---      +---       | | |   |  |       |  |  
 |       |   \      | | |   |  |       |  |  
 |       |   /  __  | | \   |  /       |  |  
 | | --  |---  /  \ | |  |  | |     | -|  |  
 | |/  \ |   \|    || |  \  | /  /-\|/ |/-|  
 | |   | |   /\    /| |   | | |  | ||  || |  
---|   | |---  ---/\| |   \/ \/  \_/|  |\-/\ 
''')
sleep(0.23)
print('''
      +—————+ +——————+ +—————+ +—————+ 
            | |      |       |       | 
            | |      |       |       | 
      +—————+ |      | +—————+ +—————+ 
      |       |      | |       |       
      |       |      | |       |       
      +—————+ +——————+ +—————+ +—————+ 

[In Ball World 2022]
Thank you for your install!
 -| game might be change
 -| English
 -| 204.9 KB
 -| DOS:Python
 -| Author:INS Team jhx(XiaoXuan)
 -| game long:about 3 hours
 -| will configue your likes
-------------------------------------
Config:
[language]
1.English(It\'s not opening now)
2.Chinese(简 体 中 文)

Input 1(X) or 2(OK) to choose your language:
''')

while input('Input >>') != '2':
    print('unknow language.')
print('Config Chinese Language...')
sleep(0.27)
clear()
print('''配置：
你最喜欢的颜色：
[蓝色]可选择
[红色]可选择
[黄色]可选择
[绿色]可选择
[青色]可选择
''')
while True:
    key = input('Input >>')
    if key in ['蓝色','红色','黄色','绿色','青色']:
        like['color'] = key
        break
    else:
        print('我未曾设置这个颜色，请重新输入')
print('颜色配置成功')
sleep(0.3)
print('初始情节配置成功')
sleep(0.1)
print('背景配置成功')
sleep(0.06)
print('配置设置成功')
player_name = input('我如何称呼您？')
print('亲爱的伙伴'+player_name+'你好，我是小轩')
print('感谢你对这个游戏的支持。')
print('我们马上开始。')
sleep(2.6)
clear()
sleep(0.15)
print(':)')
sleep(0.6)
clear()
print('在2022年端午节假期的最后一天，小学毕业考试十几天前的晚上，你昏昏睡去')
print('''梦中，你梦到了你在电脑前编程，在B站上刷视频
你也梦到了体育课上的角逐，模拟考考得名列前茅
你继续做梦，梦到你变为了一个小球。
你两脚移动，轻灵地飞向天空，撞烂了几座高大的建筑。
又过了一段时间，你飞了很远，进入了一个令人摸不着头脑的迷宫
越飞越黑，最后你只能摸索着走迷宫
''')
input('回车继续走迷宫>>')
site_xy = [1,1]
while True:
    clear()
    print('x坐标：',site_xy[0],'y坐标：',site_xy[1])
    print('如果你很久没有找到线索，或许你应该走得远一点')
    if abs(site_xy[0])+abs(site_xy[1]) > 8:
        print('你找到了一张提示纸条，上面写着:x,y=(-2,5)')
    if site_xy[0] == -2 and site_xy[1] == 5:
        print('你看到了地上的文字，上面写着:x,y=(3,-1)')
    if site_xy[0] == 3 and site_xy[1] == -1:
        site_xy[0] = -4
        site_xy[1] = 4
        print('你被传送到了另一个地方，请向后走4步，再向右走2步')
    if site_xy[0] == -2 and site_xy[1] == 0:
        print('你看到了微弱的光线，原来有一个洞，是否跳进去？')
        if input('Y=是，否则则默认不是') == 'Y':
            break
        else:
            print('你被传送到了x,y=(10,10)')
            site_xy[0] = 10
            site_xy[1] = 10
    go = input('请输入\na向左走 | 向右走d\nw向前走 | s向后走')
    if go == 'a':
        site_xy[0] -= 1
    elif go == 'd':
        site_xy[0] += 1
    elif go == 'w':
        site_xy[1] += 1
    elif go == 's':
        site_xy[1] -= 1
    else:
        print('[Error_03]无效指令')
        sleep(1)

colorfuleggs = []

# 正片开始
clear()
print('输入sys.game继续')
while input('do >>') != 'sys.game':
    print('请输入sys.game')
clear()
sleep(0.2)
print('In Ball World 2022\n'*50)
sleep(0.4)
clear()
print('你进入了洞口，亮光消失了，转而变得灰暗')
sleep(0.1)
print('你发现你正在自由落体，极快的速度让你晕眩，',end='')
sleep(0.4)
print('然而，',end='')
input('回车以继续>>')
clear()
print('你双脚落地，安然无恙。你摸到一边有一个按钮，要按下去吗？')
key = 0
while input('1要 | 2不要(输入数字以选择)') != '1':
    key += 1
    if key <= 3:
        print('什么也没发生，只是过了一点时间')
    elif key <= 5:
        print('什么也没发生，不要再浪费时间了')
    elif key <= 7:
        print('你为什么要这样？千万不能继续发呆了')
    elif key <= 10:
        print('在黑暗中发呆不是什么好事，快按下去吧')
    elif key == 11:
        print('听我的吧！快输入1')
    elif key == 12:
        print('我好心设计了这些东西，而你却不听我的话。')
    elif key == 13:
        print('我看见你的行为，真的伤心极了，',end='')
        sleep(0.6)
        print(player_name)
        sleep(0.6)
        clear()
        print(('按'+random.randint(1,10)*' ')*1200)
        sleep(0.06)
        clear()
        print(('五'+random.randint(1,10)*' ')*1200)
        sleep(0.06)
        clear()
        print(('孓'+random.randint(1,10)*' ')*1200)
        sleep(0.06)
        clear()
        print((player_name+'  ')*200)
        sleep(0.06)
        clear()
        print('H?')
        sleep(0.06)
        clear()
        print('colorful egg '*200)
        sleep(0.06)
        clear()
        print('In Ball World 2022 小轩\n'*50)
        sleep(0.06)
        clear()
        print('对不起，刚刚出现了bug，我已经修复了。请你不要再破坏游戏了')
        colorfuleggs.append('1')
        break
print('\033[7m按下按钮后，你发现四周突然亮了起来\n可是你累了……')
day = 1
input('回车睡觉>>')
clear()
sleep(2)
print('\033[7m\033[40m'+' '*3000)
sleep(0.5)
print('\033[47m'+' '*3000)
sleep(0.8)
clear()
print('\033[0m\033[40m你醒了')
sleep(0.3)



# pygame 2D正片开始
import pygame
pygame.init()

if like['color'] == '蓝色' or like['color'] == 'blue':
    like['color'] = (0,11,255)
if like['color'] == '红色' or like['color'] == 'red':
    like['color'] = (255,3,45)
if like['color'] == '黄色' or like['color'] == 'yellow':
    like['color'] = (255,235,11)
if like['color'] == '绿色' or like['color'] == 'green':
    like['color'] = (4,255,11)
if like['color'] == '青色' or like['color'] == 'cyan':
    like['color'] = (11,255,255)
day = 2

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN|pygame.NOFRAME)
screen_w,screen_h = screen.get_size()

pygame.display.set_caption("In Ball World-2D")

screen_border = pygame.Rect(10,10,screen_w-20,screen_h-20)

try:import ntpath
except:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)")
else:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)")
finally:pass

class Ball(object):
    def __init__(self,name,color,site=(0,0),size=(100,90),speed=10,hp=100):
        self.t = time()
        self.name = name
        self.move_dir = ['stop','stop']
        self.size = size
        self.color = color
        self.speed = speed
        self.fullhp = hp
        self.HP = hp
        self.rect = pygame.Rect(site[0],site[1],self.size[0],self.size[1])
        self.eye_rect = pygame.Rect(self.rect.right-int(self.size[0]/3),self.rect.top+int(self.size[1]/4),int(self.size[0]/6),int(self.size[1]/6))
        self.hprect = pygame.Rect(self.rect.x,self.rect.y-6,100,5)
        self.hpfillrect = pygame.Rect(self.rect.x,self.rect.y-6,100,5)
    def set_eye(self,dir='right'):
        if dir == 'right':
            self.eye_rect.topleft = (self.rect.right-int(self.size[0]/3),self.rect.top+int(self.size[1]/4))
        else:
            self.eye_rect.topleft = (self.rect.left+int(self.size[0]/3),self.rect.top+int(self.size[1]/4))
    def move(self):
        if self.move_dir[0] == 'left':
            self.rect.x -= self.speed
            self.set_eye('left')
        if self.move_dir[0] == 'right':
            self.rect.x += self.speed
            self.set_eye()
        if self.move_dir[1] == 'up':
            self.rect.y -= self.speed
            self.set_eye()
        if self.move_dir[1] == 'down':
            self.rect.y += self.speed
            self.set_eye()
    def slow_move(self,wait=0.15):
        if time() - self.t > wait:
            self.t = time()
            self.move()
    def hitwall(self,screen_border):
        if self.rect.left < screen_border.left:
            self.rect.left = screen_border.left
            self.set_eye()
        if self.rect.right > screen_border.right:
            self.rect.right = screen_border.right
            self.set_eye()
        if self.rect.top < screen_border.top:
            self.rect.top = screen_border.top
            self.set_eye()
        if self.rect.bottom > screen_border.bottom:
            self.rect.bottom = screen_border.bottom
            self.set_eye()
    def go(self,ball):
        if self.rect.x < ball.rect.x:
            self.move_dir[0] = 'right'
        elif self.rect.x > ball.rect.x:
            self.move_dir[0] = 'left'
        else:
            self.move_dir[0] = 'stop'
        if self.rect.y < ball.rect.y:
            self.move_dir[1] = 'down'
        elif self.rect.y > ball.rect.y:
            self.move_dir[1] = 'up'
        else:
            self.move_dir[1] = 'stop'
        if self.is_hit(ball):
            self.move_dir = ['stop','stop']
        self.move()
    def is_hit(self,ball):
        if self.rect.colliderect(ball.rect):
            return True
        return False
    def draw(self):
        pygame.draw.ellipse(screen,self.color,self.rect,0)
        pygame.draw.ellipse(screen,(0,0,0),self.eye_rect,0)
    def showhp(self):
        self.hprect.topleft = (self.rect.x,self.rect.y-6)
        self.hpfillrect.topleft = (self.rect.x,self.rect.y-6)
        self.hpfillrect.width = 100*self.HP/self.fullhp
        pygame.draw.rect(screen,(255,0,0),self.hprect,0)
        pygame.draw.rect(screen,(0,255,0),self.hpfillrect,0)

class Player(Ball):
    def __init__(self,name,color,site=(0,0),size=(100,90),speed=10):
        super().__init__(name,color,site,size,speed,120)

class TalkBox:
    def __init__(self,color=(255,255,255),size=(1000,200)):
        self.color = color
        self.rect = pygame.Rect(((screen_w-size[0])/2,(screen_h-size[1])/10*9),size)
        self.sur = pygame.Surface((self.rect.width,self.rect.height))
        self.sur.set_alpha(160)
        self.sur.fill((80,80,80))
        self.namerect = pygame.Rect(self.rect.left,self.rect.bottom+5,self.rect.height,20)
    def hit(self,pos):
        if self.rect.collidepoint(pos):
            return True
        return False
    def draw(self,ball,text,text2='',text3=''):
        screen.blit(self.sur,self.rect)
        pygame.draw.rect(screen,self.color,self.rect,5)
        b = pygame.Rect(0,0,ball.rect.width,ball.rect.height)
        b.center = (self.rect.left+self.rect.height/2,self.rect.top+self.rect.height/2)
        beye = pygame.Rect(0,0,ball.eye_rect.width,ball.eye_rect.height)
        beye.topleft = (b.right-int(b.width/3),b.top+int(b.height/4))
        pygame.draw.ellipse(screen,ball.color,b,0)
        pygame.draw.ellipse(screen,(0,0,0),beye,0)
        
        pygame.draw.line(screen,self.color,(self.rect.left+self.rect.height,self.rect.top),(self.rect.left+self.rect.height,self.rect.bottom),5)
        texttopleft = (self.rect.left+self.rect.height+5,self.rect.top+5)
        show_text(text,(255,255,255),texttopleft,20)
        show_text(text2,(255,255,255),(texttopleft[0],texttopleft[1]+20),20)
        show_text(text3,(255,255,255),(texttopleft[0],texttopleft[1]+40),20)
        pygame.draw.rect(screen,(255,255,255),self.namerect,0)
        show_text(ball.name,(0,0,0),self.namerect,20)

player = Player(player_name,like['color'],(screen_w/2-50,screen_h/2-45))
whiteball = Ball('小白球',(238,238,238),(screen_w+20,screen_h/2),(20,20),5,40)
smallBlue = Ball('小蓝',(0,11,255),(screen_w/2+50,screen_h/2-30),(50,45),8)
smallBlue.set_eye('left')
smallGreen = Ball('小绿',(3,255,11),(screen_w/2-230,screen_h/2+20),(45,43),6,160)
whiteballlist = [Ball('小球',random.choice([(238,238,238),(238,238,238),(150,150,150),(0,0,0)]),(random.randint(100,screen_w-200),random.randint(100,screen_h-150)),(20,20),random.randint(1,7),25) for i in range(60)]
enemylist = [Ball('敌人小球',(181,181,181),(random.randint(screen_w-360,screen_w-130),random.randint(80,screen_h-100)),(35,32),5,60) for i in range(60)]
talkbox = TalkBox()
talkword = '你好，我是小白球！[点击继续]'
talkword2 = ''
talkword3 = ''
talkball = smallGreen
key1 = False
key2 = False
key3 = False
clock = pygame.time.Clock()
part = '球界入口'

ring = pygame.mixer.Sound('./警报提示音.wav')
ring.set_volume(0.6)

while True:
    while part == '球界入口':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if whiteball.is_hit(player):
                        if talkbox.hit(event.pos):
                            if talkword == '你好，我是小白球！[点击继续]':
                                talkword = '欢迎来到小球世界！[继续点击继续]'
                            elif talkword == '欢迎来到小球世界！[继续点击继续]':
                                talkword = '这里有许多新奇的东西'
                            elif talkword == '这里有许多新奇的东西':
                                talkword = '一起来冒险吧！'
                            elif talkword == '一起来冒险吧！':
                                talkword = '这样，我先带你去见小蓝。'
                            elif talkword == '这样，我先带你去见小蓝。':
                                talkword = '他知道球界的很多事，一起去玩玩嘛'
                            elif talkword == '他知道球界的很多事，一起去玩玩嘛':
                                talkword = '跟我来！'
                            elif talkword == '跟我来！':
                                talkword = ''
                                whiteball.move_dir = ['right','stop']
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_dir[0] = 'left'
                if event.key == pygame.K_RIGHT:
                    player.move_dir[0] = 'right'
                if event.key == pygame.K_UP:
                    player.move_dir[1] = 'up'
                if event.key == pygame.K_DOWN:
                    player.move_dir[1] = 'down'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.move_dir[0] = 'stop'
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.move_dir[1] = 'stop'
        screen.fill((40,40,40))
        pygame.draw.rect(screen,(255,255,255),screen_border,5)
        if talkword != '':
            whiteball.go(player)
        else:
            if whiteball.rect.right < screen_border.right - 3:
                whiteball.move()
            else:
                if whiteball.is_hit(player):
                    player.rect.x = screen_border.top
                    player.set_eye()
                    whiteball.rect.topleft = (31,51)
                    whiteball.set_eye()
                    talkword = '你好，'+player.name+'！[点击继续]'
                    part = '会见小蓝'
        whiteball.draw()
        player.move()
        if player.rect.left < screen_border.left:
            player.rect.left = screen_border.left
            player.set_eye()
        if player.rect.top < screen_border.top:
            player.rect.top = screen_border.top
            player.set_eye()
        if player.rect.bottom > screen_border.bottom:
            player.rect.bottom = screen_border.bottom
            player.set_eye()
        player.draw()
        if whiteball.is_hit(player) and talkword != '':
            talkbox.draw(whiteball,talkword)
        pygame.display.update()
        clock.tick(60)
    
    while part == '会见小蓝':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if smallBlue.is_hit(player):
                        if talkbox.hit(event.pos):
                            if talkword == '你好，'+player.name+'！[点击继续]':
                                talkword = '你一定很好奇我是怎么知道你的名字的'
                            elif talkword == '你一定很好奇我是怎么知道你的名字的':
                                talkword = '这里是小球世界'
                                talkword2 = '我会把这里的一些事介绍给你听'
                            elif talkword == '这里是小球世界':
                                talkword = '你会发现很多小球都很开心，无忧无虑'
                                talkword2 = '没错，我们国家的小球都很和谐'
                                talkword3 = '这是因为我们的国家已经十一年没有战争了'
                            elif talkword == '你会发现很多小球都很开心，无忧无虑':
                                talkword = '对了，远一些的地方有60多个小球在听呢！'
                                talkword2 = ''
                                talkword3 = ''
                            elif talkword == '对了，远一些的地方有60多个小球在听呢！':
                                talkword = '咳咳，我们以后互相帮助'
                            elif talkword == '咳咳，我们以后互相帮助':
                                talkword = '小球世界的故事很古老，发生在3×10^10^1000年前'
                            elif talkword == '小球世界的故事很古老，发生在3×10^10^1000年前':
                                talkword = '可能这个数字大到惊掉你的下巴，但，这是真的'
                            elif talkword == '可能这个数字大到惊掉你的下巴，但，这是真的':
                                talkword = '那时，在03070014183297-x03-f=3030304号宇宙中，有一个神级文明'
                                talkword2 = '神级文明中出现了一个叫{无法显示符号}的人，或许叫外星人，翻译为Cut·Fluk·BLACK'
                                talkword3 = '他与他的朋友Beta·Lucky·Fire共同创造出一个大型游戏盒，富有哲理，深受大家喜爱。'
                            elif talkword == '那时，在03070014183297-x03-f=3030304号宇宙中，有一个神级文明':
                                talkword = '其中一种“小球盒”从此宇宙中掉出来了。于是“小球盒”普及于4.5×10^10^64个宇宙'
                                talkword2 = '在宇宙的不断衍生与毁灭中，其中一个小球盒飘出一个二级宇宙，进入了一个六级宇宙'
                                talkword3 = '接着来到一个五级宇宙，又进入四级的…终于，在约8.5×10^10^6年前进入一个二级宇宙'
                            elif talkword == '其中一种“小球盒”从此宇宙中掉出来了。于是“小球盒”普及于4.5×10^10^64个宇宙':
                                talkword = '随着时间推移，它在137.6亿多年前进入了一个新生不久的普通宇宙，这就是我们的宇宙'
                                talkword2 = '在61亿年前，小球盒抛下一张太空纸条，至今无人知晓它的位置。11亿年前来到太阳系'
                                talkword3 = '3亿年前，它来到地球轨道；4000万年前，它来到地球表面；'
                            elif talkword == '随着时间推移，它在137.6亿多年前进入了一个新生不久的普通宇宙，这就是我们的宇宙':
                                talkword = '800万年前，它自我创编完全完成，并新生300万亿个小球。40万年前，共有6×10^14个小球'
                                talkword2 = '很快小球开始了战争，在三万年前共有4000亿个小球存活着；从公元6000年开始，我们'
                                talkword3 = '开始接收地球消息，并每隔一段时间吸纳一批人进来。吸进来的人，要靠自己的能力'
                            elif talkword == '800万年前，它自我创编完全完成，并新生300万亿个小球。40万年前，共有6×10^14个小球':
                                talkword = '有的人会猝然长逝；有的人会留下，有的人会回家，而在小球世界度过的时间不会影响'
                                talkword2 = '人类世界。公元141年，我们拥有840万领土单位的……什么？哦，我忘了告诉你，领土'
                                talkword3 = '单位是衡量国家领土的，1单位是10平方千米。我们以前是840万单位的简并益国。'
                            elif talkword == '有的人会猝然长逝；有的人会留下，有的人会回家，而在小球世界度过的时间不会影响':
                                talkword = '可惜在公元894年，我们分裂成竹兰国、间距国、势并国、乐兴国、皿视国与益叶国。'
                                talkword2 = '后来益叶国灭掉了乐兴国，为“益乐国”，其他四国则被灭。公元1024年，浮空国'
                                talkword3 = '势如破竹攻打我们，到1234年仅余844个单位，后又挽回439个单位。'
                            elif talkword == '可惜在公元894年，我们分裂成竹兰国、间距国、势并国、乐兴国、皿视国与益叶国。':
                                talkword = '结果在1996年，一个炸毛球炸了我国，我们被轰到小球盒左下角，仅剩14个单位。'
                                talkword2 = '后来国球过少，又内乱，只有半个单位了……又被几个小国夹击，在2004年，我们'
                                talkword3 = '成为罕见“超小国”——1%个单位，11年前更加缩微，只有1/618个单位。'
                            elif talkword == '结果在1996年，一个炸毛球炸了我国，我们被轰到小球盒左下角，仅剩14个单位。':
                                talkword = '这几年我们还在不断抛弃土地。你一定会帮我们重建大国的吧？哦，那就好。'
                                talkword2 = '什么，你问我游戏规则是什么？这晚点回答。有其他人类吗？有，一定有的。'
                                talkword3 = '如何获胜回家？听说要统一全国，实际上……好吧，没有人成功过。'
                            elif talkword == '这几年我们还在不断抛弃土地。你一定会帮我们重建大国的吧？哦，那就好。':
                                talkword = '哎，你怎么不说话了？全球界有1亿单位。不过也有人说，需要打破结界。'
                                talkword2 = '什么，结界是什么？待会再讲，我来回答第一个问题，游戏规则。'
                                talkword3 = '很快，会有人攻击我们，你要帮我们打败他们，否则你会一起灭亡。'
                            elif talkword == '哎，你怎么不说话了？全球界有1亿单位。不过也有人说，需要打破结界。':
                                talkword = '你想造一件东西，会比现实简单十倍百倍，有的时候你想象它就行了。'
                                talkword2 = '除此之外，我们另有资源，这些规则你也会慢慢体验！既来之则安之~但愿…'
                                talkword3 = ''
                            elif talkword == '你想造一件东西，会比现实简单十倍百倍，有的时候你想象它就行了。':
                                talkword = '先休息吧，剩下的我们都会安排好的'
                                talkword2 = ''
                            elif talkword == '先休息吧，剩下的我们都会安排好的':
                                talkword = '哈喽，我是小绿[点击继续]'
                                part = '睡觉'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_dir[0] = 'left'
                if event.key == pygame.K_RIGHT:
                    player.move_dir[0] = 'right'
                if event.key == pygame.K_UP:
                    player.move_dir[1] = 'up'
                if event.key == pygame.K_DOWN:
                    player.move_dir[1] = 'down'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.move_dir[0] = 'stop'
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.move_dir[1] = 'stop'
        screen.fill((40,40,40))
        pygame.draw.rect(screen,(255,255,255),screen_border,5)
        whiteball.draw()
        player.move()
        player.hitwall(screen_border)
        player.draw()
        smallBlue.draw()
        if whiteball.is_hit(player):
            talkbox.draw(whiteball,'那就是小蓝，快去吧')
        if smallBlue.is_hit(player):
            talkbox.draw(smallBlue,talkword,talkword2,talkword3)
        pygame.display.update()
        clock.tick(60)
    
    while part == '睡觉':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    day += 1
                    if day == 3:
                        smallBlue.rect.y -= 200
                        smallBlue.rect.x += 200
                        smallBlue.set_eye('left')
                        part = '会见小绿'
                    elif day == 4:
                        cangooutcountry = 0
                        smallBlue.rect.y = 100
                        smallBlue.rect.x = player.rect.x
                        smallBlue.set_eye()
                        smallGreen.rect.bottom = screen_h-100
                        smallGreen.rect.x = player.rect.x
                        smallGreen.set_eye()
                        part = '领土边缘'
                    elif day == 5:
                        part = '初次危机'
                        talkball = smallBlue
                        ring.play(-1)
                    elif day == 6:
                        part = '内部休息日'  # 认识小红小轮子、结界等
                    elif day == 7:
                        part = '第二次危机'
                    elif day == 8:
                        part = ''
                    elif day == 9:
                        part = ''
                    elif day == 10:
                        part = ''
                    elif day == 11:
                        part = ''
                    elif day == 12:
                        part = ''
                    elif day == 13:
                        part = ''
                    elif day == 14:
                        part = ''
        screen.fill((11,11,11))
        show_text('第'+str(day)+'天 你在睡梦中，按N开始下一天的旅程',(255,255,255),(11,11),40)
        pygame.display.update()
        clock.tick(30)
    
    while part == '会见小绿':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if talkbox.hit(event.pos):
                        if talkball == smallGreen:
                            if talkword == '哈喽，我是小绿[点击继续]':
                                talkword = '看，60多个小球在和我们开会'
                            elif talkword == '看，60多个小球在和我们开会':
                                talkball = player
                                talkword = '啊对对对，I see.'
                            elif talkword == '我攻击远不如小蓝，但我防御极强，是我们国最强防手':
                                talkword = '哦对了，大家别吵了，人类朋友，我想认识你一下'
                            elif talkword == '哦对了，大家别吵了，人类朋友，我想认识你一下':
                                talkword = '[招手]原来你是'+player.name+'啊！这名字不错！'
                            elif talkword == '[招手]原来你是'+player.name+'啊！这名字不错！':
                                talkword = '我们小球通晓你们人类的好多语言呢！'
                            elif talkword == '我们小球通晓你们人类的好多语言呢！':
                                talkball = player
                                talkword = '[挠了挠头]厉害！益乐国……'
                            elif talkword == '[害羞][微笑]后来分别改为“小益乐国”“尘欲国”“益彻国”':
                                talkword = '时至今日，叫做“益微国”了'
                            elif talkword == '时至今日，叫做“益微国”了':
                                talkword = '益微国有不少敌人，不远。有几个国家和我们共存与4个单位之中'
                            elif talkword == '益微国有不少敌人，不远。有几个国家和我们共存与4个单位之中':
                                talkword = '有稍远的浮空国、玻璃球国，近的有大绿国、灰球国等，旁边有几波土匪球'
                            elif talkword == '有稍远的浮空国、玻璃球国，近的有大绿国、灰球国等，旁边有几波土匪球':
                                talkword = '或许干掉土匪球很麻烦'
                            elif talkword == '或许干掉土匪球很麻烦':
                                talkball = player
                                talkword = '我最好先逛逛，认识地形、小球们。对了，你们有作战准备吗？'
                        elif talkball == player:
                            if talkword == '啊对对对，I see.':
                                talkword = '我们现在处境咋样？'
                            elif talkword == '我们现在处境咋样？':
                                talkball = whiteballlist[0]
                                talkword = '我们哪，很危险了啦。我们国家一共有430个小球'
                                talkword2 = '其中只有150多个明白危险，其中又只有80个重视危险'
                            elif talkword == '[挠了挠头]厉害！益乐国……':
                                talkball = smallGreen
                                talkword = '[害羞][微笑]后来分别改为“小益乐国”“尘欲国”“益彻国”'
                            elif talkword == '我最好先逛逛，认识地形、小球们。对了，你们有作战准备吗？':
                                talkword = '[听到“时刻准备着!”，笑不活了]竟然搬出少先队员的话来'
                            elif talkword == '[听到“时刻准备着!”，笑不活了]竟然搬出少先队员的话来':
                                talkword = '学人类界还是有那么一茬问题，[严肃]接下来干正事'
                            elif talkword == '学人类界还是有那么一茬问题，[严肃]接下来干正事':
                                talkword = '好的，各回各家，我就先逛一天了。'
                            elif talkword == '好的，各回各家，我就先逛一天了。':
                                part = '睡觉'
                                talkword = ''
                                talkball = smallBlue
                        elif talkball == whiteballlist[0]:
                            if talkword == '我们哪，很危险了啦。我们国家一共有430个小球':
                                talkword = '小蓝还不是我们国家最强的。还有几个球更强，比如小绿'
                                talkword2 = ''
                            elif talkword == '小蓝还不是我们国家最强的。还有几个球更强，比如小绿':
                                talkball = smallBlue
                                talkword = '用不着你多嘴！！！小绿只是...'
                        elif talkball == smallBlue:
                            if talkword == '用不着你多嘴！！！小绿只是...':
                                talkball = smallGreen
                                talkword = '我攻击远不如小蓝，但我防御极强，是我们国最强防手'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_dir[0] = 'left'
                if event.key == pygame.K_RIGHT:
                    player.move_dir[0] = 'right'
                if event.key == pygame.K_UP:
                    player.move_dir[1] = 'up'
                if event.key == pygame.K_DOWN:
                    player.move_dir[1] = 'down'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.move_dir[0] = 'stop'
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.move_dir[1] = 'stop'
        screen.fill((50,55,50))
        pygame.draw.rect(screen,(250,250,250),screen_border,5)
        for i in whiteballlist:
            i.move_dir = [random.choice(['left','right']),random.choice(['up','down'])]
            i.slow_move()
            i.hitwall(screen_border)
            i.draw()
        player.move()
        player.hitwall(screen_border)
        player.draw()
        smallGreen.draw()
        smallBlue.draw()
        talkbox.draw(talkball,talkword,talkword2,talkword3)
        pygame.display.update()
        clock.tick(60)
    
    while part == '领土边缘':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if talkbox.hit(event.pos):
                        if talkword == '哈喽！[点击继续(最后一次提示)]':
                            talkword = '今天是你来球界的第四天了'
                        elif talkword == '今天是你来球界的第四天了':
                            talkword = '你终于发现了这里，我们差点忘了介绍'
                        elif talkword == '你终于发现了这里，我们差点忘了介绍':
                            talkword = '看到那条红色的线了吧？'
                        elif talkword == '看到那条红色的线了吧？':
                            talkword = '这就是领土边缘，我们的国界线'
                        elif talkword == '这就是领土边缘，我们的国界线':
                            talkword = '我们跨出国界线就可以占领领土，可以试试'
                            cangooutcountry = 1
                        elif talkword == 'OK啦，你成功占领了领土':
                            talkword = '你可以退回来，还能再占领'
                        elif talkword == '你可以退回来，还能再占领':
                            talkword = '这土地会显示占领值，你离得远不必看清'
                        elif talkword == '这土地会显示占领值，你离得远不必看清':
                            talkword = '占领值是从-6到6，代表占领的程度'
                        elif talkword == '占领值是从-6到6，代表占领的程度':
                            talkword = '显然，-6是敌方完全占领，反之亦然'
                        elif talkword == '显然，-6是敌方完全占领，反之亦然':
                            talkword = '没占领或平衡就是0，我们称其为“黑地砖”'
                        elif talkword == '没占领或平衡就是0，我们称其为“黑地砖”':
                            talkword = '它同样说明了占领方是谁'
                        elif talkword == '它同样说明了占领方是谁':
                            talkword = '每块地砖的大小是0.25平方米'
                        elif talkword == '每块地砖的大小是0.25平方米':
                            talkword = '为了履行公约，移动通畅，我们不碰一些地砖'
                        elif talkword == '为了履行公约，移动通畅，我们不碰一些地砖':
                            talkword = '哦对了，这是小轮子造的夺砖开关'
                        elif talkword == '哦对了，这是小轮子造的夺砖开关':
                            talkword = '小轮子是小球科学家。这个开关请随身携带'
                        elif talkword == '小轮子是小球科学家。这个开关请随身携带':
                            talkword = '关掉它，你走就不会夺走地砖了'
                        elif talkword == '关掉它，你走就不会夺走地砖了':
                            talkword = '好了，再熟悉熟悉这里吧'
                        elif talkword == '好了，再熟悉熟悉这里吧':
                            part = '睡觉'
                            talkword = '啊，听，警报声！！！'
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_dir[0] = 'left'
                if event.key == pygame.K_RIGHT:
                    player.move_dir[0] = 'right'
                if event.key == pygame.K_UP:
                    player.move_dir[1] = 'up'
                if event.key == pygame.K_DOWN:
                    player.move_dir[1] = 'down'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.move_dir[0] = 'stop'
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.move_dir[1] = 'stop'
        screen.fill((60,60,60))
        pygame.draw.rect(screen,(245,245,245),screen_border,5)
        if talkword:
            smallBlue.draw()
            smallGreen.draw()
        player.move()
        player.hitwall(screen_border)
        if player.rect.right > screen_w - 55:
            if not cangooutcountry:
                player.rect.right = screen_w - 55
            if talkword == '':
                talkword = '哈喽！[点击继续(最后一次提示)]'
        if player.rect.right < screen_w - 11:
            pygame.draw.line(screen,(255,11,11),(screen_w-50,screen_border.top),(screen_w-50,screen_border.bottom),3)
        elif cangooutcountry != 2:
            cangooutcountry = 2
            talkword = 'OK啦，你成功占领了领土'
        player.draw()
        if talkword:
            talkbox.draw(talkball,talkword)
        pygame.display.update()
        clock.tick(60)
    
    while part == '初次危机':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if talkbox.hit(event.pos):
                        if talkword == '啊，听，警报声！！！':
                            talkword = '有敌人要来了'
                        elif talkword == '有敌人要来了':
                            talkword = '我们赶紧进入状态吧'
                        elif talkword == '我们赶紧进入状态吧':
                            part = '初次危机-战斗界面'
                            player.rect.x = screen_border.left+20
                            player.rect.centery = screen_h/2
                            player.set_eye()
                            smallGreen.rect.topleft = player.rect.topleft
                            smallGreen.rect.y += 160
                            smallGreen.set_eye()
                            smallBlue.rect.topleft = player.rect.topleft
                            smallBlue.rect.y -= 120
                            smallBlue.set_eye()
                            for i in whiteballlist:
                                i.rect.topleft = player.rect.topleft
                                i.rect.y += random.randint(-260,260)
                                i.rect.x += random.randint(-10,150)
                                i.set_eye()
                            ring.stop()
                            t = time()
                            r = random.randint(11,22)/10
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_dir[0] = 'left'
                if event.key == pygame.K_RIGHT:
                    player.move_dir[0] = 'right'
                if event.key == pygame.K_UP:
                    player.move_dir[1] = 'up'
                if event.key == pygame.K_DOWN:
                    player.move_dir[1] = 'down'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.move_dir[0] = 'stop'
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.move_dir[1] = 'stop'
        screen.fill((65,65,65))
        pygame.draw.rect(screen,(243,243,243),screen_border,5)
        player.move()
        player.hitwall(screen_border)
        player.draw()
        smallBlue.draw()
        if talkword:
            talkbox.draw(talkball,talkword)
        pygame.display.update()
        clock.tick(60)
    
    while part == '初次危机-战斗界面':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_dir[0] = 'left'
                if event.key == pygame.K_RIGHT:
                    player.move_dir[0] = 'right'
                if event.key == pygame.K_UP:
                    player.move_dir[1] = 'up'
                if event.key == pygame.K_DOWN:
                    player.move_dir[1] = 'down'
                if event.key == ord('a'):
                    for e in enemylist:
                        e.HP -= random.randint(0,3)
                        if e.HP <= 0:
                            enemylist.remove(e)
                if event.key == ord('s'):
                    for i in whiteballlist:
                        if i.HP < i.fullhp:
                            i.HP += 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.move_dir[0] = 'stop'
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.move_dir[1] = 'stop'
        screen.fill((66,66,66))
        pygame.draw.rect(screen,(243,243,243),screen_border,5)
        if time() - t > r:
            t = time()
            r = random.randint(11,22)/10
            for i in whiteballlist:
                i.HP -= random.randint(0,3)
                if i.HP <= 0:
                    whiteballlist.remove(i)
            for e in enemylist:
                if e.HP < e.fullhp:
                    e.HP += 1
        for i in whiteballlist:
            i.move_dir = [random.choice(['left','right']),random.choice(['up','down'])]
            i.slow_move()
            i.hitwall(screen_border)
            i.draw()
            i.showhp()
        for e in enemylist:
            e.move_dir = [random.choice(['left','right']),random.choice(['up','down'])]
            e.slow_move()
            e.hitwall(screen_border)
            e.draw()
            e.showhp()
        player.move()
        player.hitwall(screen_border)
        player.draw()
        player.showhp()
        smallBlue.draw()
        smallBlue.showhp()
        smallGreen.draw()
        smallGreen.showhp()
        if not enemylist:
            part = '初次危机-获胜'
            talkball = smallGreen
            talkword = '耶，我们赢了！！！'
        show_text('a攻击,s防守',color=(243,243,243),pos=(screen_w/2-110,screen_h-100),size=40)
        pygame.display.update()
        clock.tick(60)
    
    while part == '初次危机-获胜':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if talkbox.hit(event.pos):
                        if talkword == '耶，我们赢了！！！':
                            talkword = '这是你带领我们打赢的第一场仗'
                        elif talkword == '这是你带领我们打赢的第一场仗':
                            talkword = '很快我们就会让你见到小轮子和小红的'
                        elif talkword == '很快我们就会让你见到小轮子和小红的':
                            talkword = '好了，我们回去吧'
                        elif talkword == '好了，我们回去吧':
                            part = '钥匙1的路'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_dir[0] = 'left'
                if event.key == pygame.K_RIGHT:
                    player.move_dir[0] = 'right'
                if event.key == pygame.K_UP:
                    player.move_dir[1] = 'up'
                if event.key == pygame.K_DOWN:
                    player.move_dir[1] = 'down'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.move_dir[0] = 'stop'
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.move_dir[1] = 'stop'
        screen.fill((66,66,66))
        pygame.draw.rect(screen,(243,243,243),screen_border,5)
        player.move()
        player.hitwall(screen_border)
        player.draw()
        smallBlue.draw()
        smallGreen.draw()
        if talkword:
            talkbox.draw(talkball,talkword)
        pygame.display.update()
        clock.tick(60)
    
    while part == '钥匙1的路':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_dir[0] = 'left'
                if event.key == pygame.K_RIGHT:
                    player.move_dir[0] = 'right'
                if event.key == pygame.K_UP:
                    player.move_dir[1] = 'up'
                if event.key == pygame.K_DOWN:
                    player.move_dir[1] = 'down'
                if event.key == ord('z'):
                    key1 = True
                    part = '睡觉'
                if event.key == ord('x'):
                    part = '睡觉'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.move_dir[0] = 'stop'
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.move_dir[1] = 'stop'
        screen.fill((68,68,68))
        pygame.draw.rect(screen,(240,240,240),screen_border,5)
        player.move()
        player.hitwall(screen_border)
        player.draw()
        show_text('你看到了一把钥匙，按z拾取，按x直接离开',color=(243,243,243),pos=(screen_w/2-380,screen_h-100),size=40)
        pygame.display.update()
        clock.tick(60)