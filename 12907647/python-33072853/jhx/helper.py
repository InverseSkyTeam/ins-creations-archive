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

CVrect = pygame.Rect(250,100,500,50)
Helprect = pygame.Rect(250,200,500,50)
Exitrect = pygame.Rect(250,300,500,50)

y = 0
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
    studyrectlist.append(pygame.Rect(300+250*(i%2),80+i*60,200,50))
# studyrectlist.append(pygame.Rect(250,10,200,50))
# studyrectlist.append(pygame.Rect(250,70,200,50))

while True:       # 这行代码显示了我的勤奋
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
                    if Exitrect.collidepoint(mp):
                        part = 'callback'
        screen.fill((255,255,255))
        screen.blit(bg,(0,0))
        show_text('INS-jhx库帮助',(0,0,255),(11,11),40)
        show_text('(C)Copyright.INS逆天团队-小轩(2021,2022)所有',(0,0,0),(275,29),20)    # 如果x=271会显得过于紧凑，y=40-11=29
        show_text('(V)Version.版本|0.4.5',(0,0,0),(740,29),20)
        
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
        show_text('退    出',(0,0,0),(420,305),40)
        
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
        show_text('版本 V0.4.5.9742-download /build.82 /beta',(0,0,255),(11,111),30)
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
            if event.type == pygame.MOUSEMOTION:
                mp = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if Exitrect.collidepoint(mp):
                        part = '主界面'
        screen.fill((255,255,255))
        screen.blit(bg,(0,0))
        show_text('库教程-选择你想学的内容',(0,11,255),(11,11),40)    # 11不是111，深蓝，为啥作者小轩那么喜欢1,11,111呢？不告诉你，偷翻源码的人！！！[doge]
        show_text('教程还在准备哟~~~',(0,11,255),(11,81),40)
        for i in studyrectlist:
            pygame.draw.rect(screen,(0,255,255),i,0)
        if Exitrect.collidepoint(mp):pygame.draw.rect(screen,(0,111,255),Exitrect,0)   # 懒了x2
        else:pygame.draw.rect(screen,(200,200,200),Exitrect,0)
        pygame.draw.rect(screen,(0,0,0),Exitrect,3)
        show_text('返回主页',(0,0,0),(420,305),40)
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
        show_text('取    消',(0,0,0),(420,305),40)
        pygame.display.update()