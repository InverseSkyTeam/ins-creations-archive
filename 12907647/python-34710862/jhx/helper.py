# helps for jhx
import pygame,sys,os
pygame.init()
os.chdir(os.path.dirname(os.path.abspath(__file__)))

screen = pygame.display.set_mode((1000,600))
pygame.display.set_icon(pygame.image.load('image/helpbookicon.png'))
pygame.display.set_caption('INS jhx python-helpbook')

try:import ntpath
except:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)")
else:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)")
finally:pass

bg = pygame.image.load('image/helpbookbg.png')
environment_and_foundation_p1 = pygame.image.load('image/helperimg/环境与基础-p1.png')

CVrect = pygame.Rect(250,100,500,50)
Helprect = pygame.Rect(250,200,500,50)
Exitrect = pygame.Rect(250,300,500,50)

y = 0
hy = 0
mp = (0,0)
part = '主界面'

studylist = [
    '环境与基础',
    '我就是帮助',    # 没错，就是我！！！
    '数学超高手',
    '万年老字典',
    '游戏与软件',
    '应用与布局',
    '文件操控帮',
    '其他牛逼库',
    ]
studyrectlist = []
for i in range(8):
    studyrectlist.append(pygame.Rect(300+300*(i%2),80+i*50,250,50))
# studyrectlist.append(pygame.Rect(250,10,200,50))
# studyrectlist.append(pygame.Rect(250,70,200,50))

while True:       # 这行代码显示了我的勤奋(while 1?)
    while part == '主界面':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                part = 'callback'
            if event.type == pygame.MOUSEMOTION:
                mp = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if CVrect.collidepoint(mp):
                        part = '库信息界面'
                    if Helprect.collidepoint(mp):
                        part = '库教程界面'
                        Exitrect.y = 500
                    if Exitrect.collidepoint(mp):
                        part = 'callback'
        screen.fill((255,255,255))
        screen.blit(bg,(0,0))
        show_text('INS-jhx库帮助',(0,0,255),(11,11),40)
        show_text('(C)Copyright.INS逆天团队-小轩(2021,2022)所有',(0,0,0),(275,29),20)    # 如果x=271会显得过于紧凑，y=40-11=29
        show_text('(V)Version.版本|0.7.5',(0,0,0),(740,29),20)
        
        if CVrect.collidepoint(mp):pygame.draw.rect(screen,(0,255,0),CVrect,0)
        else:pygame.draw.rect(screen,(200,200,200),CVrect,0)
        pygame.draw.rect(screen,(0,0,0),CVrect,3)
        show_text('库 信 息',(0,0,0),(420,105),40)
        if Helprect.collidepoint(mp):pygame.draw.rect(screen,(0,111,255),Helprect,0)
        else:pygame.draw.rect(screen,(200,200,200),Helprect,0)
        pygame.draw.rect(screen,(0,0,0),Helprect,3)
        show_text('库 教 程',(0,0,0),(420,205),40)
        if Exitrect.collidepoint(mp):pygame.draw.rect(screen,(255,66,50),Exitrect,0)
        else:pygame.draw.rect(screen,(200,200,200),Exitrect,0)
        pygame.draw.rect(screen,(0,0,0),Exitrect,3)
        show_text('退    出',(0,0,0),(420,Exitrect.y+5),40)
        
        pygame.display.update()
    
    while part == '库信息界面':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                part = '主界面'
            if event.type == pygame.MOUSEMOTION:
                mp = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Exitrect.collidepoint(mp):
                        part = '主界面'
        screen.fill((255,255,255))
        screen.blit(bg,(0,0))
        show_text('库信息',(0,111,0),(11,11),40)
        show_text('版权 INS-jhx(c)Copyright.2021,2022 /逆天团队 小轩 版权占比率100%',(0,0,255),(11,81),30)
        show_text('版本 V0.7.5.1418-download /build.317 /beta',(0,0,255),(11,111),30)
        show_text('为了更加简单的全面python而制作，除了语法以外，其他可以自成一门语言',(0,0,255),(11,141),30)
        show_text('叫做INS-jhx python,简称ijp',(0,0,255),(11,171),30)
        if Exitrect.collidepoint(mp):pygame.draw.rect(screen,(0,111,255),Exitrect,0)  # 懒了，exitrect改成了返回功能
        else:pygame.draw.rect(screen,(200,200,200),Exitrect,0)
        pygame.draw.rect(screen,(0,0,0),Exitrect,3)
        show_text('返回主页',(0,0,0),(420,305),40)
        pygame.display.update()
    
    while part == '库教程界面':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                part = '主界面'
                Exitrect.y = 300
            if event.type == pygame.MOUSEMOTION:
                mp = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Exitrect.collidepoint(mp):
                        part = '主界面'
                        Exitrect.y = 300
                    for i in range(8):
                        if studyrectlist[i].collidepoint(mp):
                            part = studylist[i]
                            y = 0
                            hy = 0
        screen.fill((255,255,255))
        screen.blit(bg,(0,0))
        show_text('库教程-选择你想学的内容',(0,11,255),(11,11),40)    # 11不是111，深蓝，为啥作者小轩那么喜欢1,11,111呢？不告诉你，偷翻源码的人！！！[doge]
        show_text('教程准备中~',(0,11,255),(11,81),40)
        for i in range(8):
            pygame.draw.rect(screen,(0,255,255),studyrectlist[i],0)
            show_text(studylist[i],(0,0,0),studyrectlist[i],50)
        if Exitrect.collidepoint(mp):pygame.draw.rect(screen,(0,111,255),Exitrect,0)   # 懒了x2
        else:pygame.draw.rect(screen,(200,200,200),Exitrect,0)
        pygame.draw.rect(screen,(0,0,0),Exitrect,3)
        show_text('返回主页',(0,0,0),(420,Exitrect.y+5),40)
        pygame.display.update()
    
    while part == '环境与基础':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                part = '库教程界面'
            if event.type == pygame.MOUSEMOTION:
                mp = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    hy -= 10
                if event.button == 5:
                    hy += 10
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    part = '库教程界面'
                if event.key == pygame.K_UP:
                    hy -= 20
                if event.key == pygame.K_DOWN:
                    hy += 20
        hy *= 0.85
        if abs(hy) < 1:hy = 0
        y += round(hy)
        if y < 0:
            y = 0
        if y > 1000:
            y = 1000
        screen.fill((237,237,237))
        screen.blit(bg,(0,-y))
        show_text('库教程-init-环境与基础',(0,11,255),(11,11-y),40)
        show_text('指令：[Q-退出][滚轮/上键/下键-移动]',(0,11,255),(11,81-y),20)
        show_text('Hello!欢迎来到jhx库的帮助第一课!',(0,0,0),(11,101-y),20)
        show_text('让python的库更多，写代码更方便，不是一件大好事么?',(0,0,0),(11,121-y),20)
        show_text('jhx库，由逆天团队的小轩开发。它让代码更简便，更强大。',(0,0,0),(11,141-y),20)
        show_text('有了我们的帮助，编写代码再也不是难事!',(0,0,0),(11,161-y),20)
        show_text('保留程序猿的黑发，让编程变得美丽，就是我所能做的微小之事!',(0,0,0),(11,181-y),20)
        show_text('话不多说，开启咱们的教程!',(0,0,0),(11,201-y),20)
        show_text('每个库都有自己的安装方法，设置自己的环境变量，我们先学会安装库',(0,11,255),(11,241-y),20)
        show_text('由于作者小轩没有pypi，所以不能用pip下载jhx库，抱歉了',(0,11,255),(11,261-y),20)
        show_text('不过，jhx库自带安装功能!',(11,180,61),(11,281-y),30)
        show_text('哦吼，让我们开始吧!',(0,11,255),(11,311-y),20)
        show_text('1.打开小轩的编程社区个人主页(https://code.xueersi.com/space/12907647?to=work)',(0,0,0),(11,331-y),20)
        show_text('2.找到最新的jhx库作品，点开它（跪求三连，助力每一个梦想），并且运行',(0,0,0),(11,351-y),20)
        show_text('3.库便自动安装好了',(0,0,0),(11,371-y),20)
        show_text('#4.没有xes账号怎么办？打开改编，导出左侧文件素材“jhx”放到桌面上',(0,0,0),(11,391-y),20)
        show_text('#5.再打开记事本，写入代码:',(0,0,0),(11,411-y),20)
        show_text('   from jhx import *',(0,0,0),(11,431-y),20)
        show_text('   install.download(site="Local")',(0,0,0),(11,451-y),20)
        show_text('#6.另存为.py格式文件，双击运行，于是自动安装到本地，完美!',(0,0,0),(11,471-y),20)
        screen.blit(environment_and_foundation_p1,(11,491-y))
        show_text('以上图片可作参考',(0,0,0),(11,961-y),20)
        show_text('接下来，导入库的方法:',(0,0,0),(11,991-y),20)
        show_text('import jhx',(0,0,255),(11,1011-y),20)
        show_text('导入了jhx库，现在部门可以使用它的模块',(0,0,0),(11,1031-y),20)
        show_text('如:',(0,0,0),(11,1051-y),20)
        show_text('jhx.xxx()',(0,0,255),(11,1071-y),20)
        show_text('jhx.mathadd.xxx() # 数学库',(0,0,255),(11,1091-y),20)
        show_text('第二种方法:',(0,0,0),(11,1111-y),20)
        show_text('from jhx import *',(0,0,255),(11,1131-y),20)
        show_text('xxx()',(0,0,255),(11,1151-y),20)
        show_text('mathadd.xxx() # 数学库',(0,0,255),(11,1171-y),20)
        show_text('显然，第二种方法更方便，不过如果模块较多的话，可能会混淆冲突',(255,0,0),(11,1191-y),20)
        show_text('最后一种',(0,0,0),(11,1211-y),20)
        show_text('from jhx import dsui # 只导入UI库，速度更快，混淆率更低',(0,0,255),(11,1231-y),20)
        show_text('from jhx import dictionaty as dic',(0,0,255),(11,1251-y),20)
        show_text('显然，最后一种方法也很不错',(255,0,0),(11,1271-y),20)
        show_text('环境、变量都完成了，现在可以正式开始我们的课程了!',(0,200,0),(11,1311-y),20)
        show_text('介绍一下jhx.__init__内置函数、变量',(0,0,0),(11,1331-y),20)
        show_text('import jhx',(0,0,255),(11,1351-y),20)
        show_text('print(jhx.name)   # 输出库名',(0,0,255),(11,1371-y),20)
        show_text('print(jhx.Copyright)   # 输出版权',(0,0,255),(11,1391-y),20)
        show_text('print(jhx.Version)   # 输出版本',(0,0,255),(11,1411-y),20)
        show_text('jhx.helpbook()   # 打开帮助(你都打开了，看这有用吗/doge)',(0,0,255),(11,1431-y),20)
        show_text('jhx.mathadd   # 数学库',(0,0,255),(11,1451-y),20)
        show_text('接下来列举一些库:',(0,0,0),(11,1471-y),20)
        show_text('mathadd dictionaty dsui ec filer igame install helper win_ent 中文 __init__',(0,0,255),(11,1491-y),20)
        show_text('到这里，你已经学会了基础环境，下节课再见，拜拜!',(0,0,0),(11,1511-y),20)
        pygame.display.update()
        
    
    while part == 'callback':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mp = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Helprect.collidepoint(mp):
                        pygame.quit()
                        sys.exit()
                    if Exitrect.collidepoint(mp):
                        part = '主界面'
        screen.fill((255,255,255))
        screen.blit(bg,(0,0))
        show_text('您确定要退出吗？',(255,0,111),(11,11),40)
        if Helprect.collidepoint(mp):pygame.draw.rect(screen,(255,66,50),Helprect,0)      # 懒了x3，和上文“勤奋形成鲜明对比”，不创建新矩形了
        else:pygame.draw.rect(screen,(200,200,200),Helprect,0)
        pygame.draw.rect(screen,(0,0,0),Helprect,3)
        show_text('确    定',(0,0,0),(420,205),40)
        if Exitrect.collidepoint(mp):pygame.draw.rect(screen,(0,111,255),Exitrect,0)      # helprect变为退出，exitrect变为取消了
        else:pygame.draw.rect(screen,(200,200,200),Exitrect,0)
        pygame.draw.rect(screen,(0,0,0),Exitrect,3)
        show_text('取    消',(0,0,0),(420,Exitrect.y+5),40)
        pygame.display.update()