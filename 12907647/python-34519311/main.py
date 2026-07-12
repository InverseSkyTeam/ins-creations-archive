'''
彩蛋1:206行
'''
from time import *
import sys,random,math

def clear():
    print('\033[2J\033[100A\033[3J\033[100A'*8)

print('''In Ball World [Version 0.0.6 -Aplha]
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
 -| 0.3 KB
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

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN|pygame.NOFRAME)
screen_w,screen_h = screen.get_size()
pygame.display.set_caption("In Ball World-2D")

screen_border = pygame.Rect(10,10,screen_w-20,screen_h-20)

try:import ntpath
except:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)")
else:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)")
finally:pass

class Ball(object):
    def __init__(self,name,color,site=(0,0),size=(100,90),speed=10):
        self.name = name
        self.move_dir = ['stop','stop']
        self.size = size
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(site[0],site[1],self.size[0],self.size[1])
        self.eye_rect = pygame.Rect(self.rect.right-int(self.size[0]/3),self.rect.top+int(self.size[1]/4),int(self.size[0]/6),int(self.size[1]/6))
    def move(self):
        if self.move_dir[0] == 'left':
            self.rect.x -= self.speed
            self.eye_rect.topleft = (self.rect.left+int(self.size[0]/3),self.rect.top+int(self.size[1]/4))
        if self.move_dir[0] == 'right':
            self.rect.x += self.speed
            self.eye_rect.topleft = (self.rect.right-int(self.size[0]/3),self.rect.top+int(self.size[1]/4))
        if self.move_dir[1] == 'up':
            self.rect.y -= self.speed
            self.eye_rect.topleft = (self.rect.right-int(self.size[0]/3),self.rect.top+int(self.size[1]/4))
        if self.move_dir[1] == 'down':
            self.rect.y += self.speed
            self.eye_rect.topleft = (self.rect.right-int(self.size[0]/3),self.rect.top+int(self.size[1]/4))
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

class Player(Ball):
    def __init__(self,name,color,site=(0,0),size=(100,90),speed=10):
        super().__init__(name,color,site,size,speed)

class TalkBox:
    def __init__(self,color=(255,255,255),size=(1000,200)):
        self.color = color
        self.rect = pygame.Rect(((screen_w-size[0])/2,(screen_h-size[1])/10*9),size)
    def draw(self,ball,text):
        pygame.draw.rect(screen,self.color,self.rect,5)
        b = pygame.Rect(0,0,ball.rect.width,ball.rect.height)
        b.center = (self.rect.left+self.rect.height/2,self.rect.top+self.rect.height/2)
        beye = pygame.Rect(0,0,ball.eye_rect.width,ball.eye_rect.height)
        beye.topleft = (b.right-int(b.width/3),b.top+int(b.height/4))
        pygame.draw.ellipse(screen,ball.color,b,0)
        pygame.draw.ellipse(screen,(0,0,0),beye,0)
        pygame.draw.line(screen,self.color,(self.rect.left+self.rect.height,self.rect.top),(self.rect.left+self.rect.height,self.rect.bottom),5)
        show_text(text,(255,255,255),(self.rect.left+self.rect.height+5,self.rect.top+5),20)

player = Player(player_name,like['color'],(screen_w/2-50,screen_h/2-45))
whiteball = Ball('小白球',(238,238,238),(screen_w+20,screen_h/2),(20,20),5)
talkbox = TalkBox()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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
    whiteball.go(player)
    whiteball.draw()
    player.move()
    player.draw()
    if whiteball.is_hit(player):
        talkbox.draw(whiteball,'你好，我是小白球！[未完待续]')
    pygame.display.update()
    clock.tick(60)