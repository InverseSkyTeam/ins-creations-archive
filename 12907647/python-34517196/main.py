'''
彩蛋1:206行
'''
from time import *
import sys,random,math

def clear():
    print('\033[2J\033[100A\033[3J\033[100A'*8)

print('''In Ball World [Version 0.0.2 -Aplha]
Build 49
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
sleep(0.2)
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
print(player_name)
sleep(0.03)
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
        print('按')
        sleep(0.03)
        clear()
        print('五')
        sleep(0.03)
        clear()
        print('孓')
        sleep(0.03)
        clear()
        print(player_name)
        sleep(0.03)
        clear()
        print('H?')
        sleep(0.03)
        clear()
        print('colorful egg')
        sleep(0.03)
        clear()
        print('In Ball World 2022 小轩')
        sleep(0.03)
        clear()
        print('对不起，刚刚出现了bug，我已经修复了。请你不要再破坏游戏了')
        break
print('按下按钮后，你发现四周突然亮了起来')