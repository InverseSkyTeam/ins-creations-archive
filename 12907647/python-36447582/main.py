from time import *
import pygame,sys,webbrowser
try:
    from moviepy.editor import *
except:
    print('在库管理先安装moviepy库')
    sys.exit()

print('大家好，我是一个2018级别的C站原始人类')
print('你可能早就认识我，也可能与我素不相识；可能是我的朋友，也可能是我的对手；可能是个无知小白，也可能是个无敌大佬。但是，接下来的所有东西，可以请大家牺牲一点点时间看完吗？（提示：源代码的注释含彩蛋）')
print('\n键入命令"next"继续')
while input('>>') != 'next':
    print('键入"next".')
VideoFileClip('C站简总集开头.mp4').preview()

pygame.init()
w = 1280
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
part = 1

try:import ntpath
except:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)")
else:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)")
finally:pass

while True:
    while part == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if w > 600:
            w -= 5
            screen = pygame.display.set_mode((w,720))
        else:
            screen = pygame.display.set_mode((600,600))
            pygame.display.set_caption('小轩退站')
            part = 2
            y = 0
            hy = 0
        pygame.display.update()
        # 你在翻源码，知道为什么我那么喜欢1,11,111吗？见下面帧率，因为我生日在11/1
        clock.tick(111)
    
    while part == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    hy -= 10
                if event.button == 5:
                    hy += 10
            if event.type == pygame.KEYDOWN:
                if event.key == ord('n'):
                    part = 3
                    showindex = 1
        screen.fill((255,255,255))
        hy *= 0.85
        if abs(hy) < 1:hy = 0
        y += round(hy)
        if y < 0:
            y = 0
        if y > 300:
            y = 300
        show_text('大家好，我是小轩',(0,0,255),(0,0-y))
        show_text('用滚轮滚动可以移动页面',(0,0,0),(0,30-y),20)
        show_text('今天，我隆重宣布，我要退站了',(0,0,0),(0,50-y),20)
        show_text('感谢大家一直以来的鼓励与支持',(0,0,0),(0,70-y),20)
        show_text('记住，再见，只为再见，我还会来C站的',(0,0,0),(0,90-y),20)
        show_text('这个作品是我花了很多时间制作的',(0,0,0),(0,110-y),20)
        show_text('剪辑，python/sc/h5编程，cmd批处理',(0,0,0),(0,130-y),20)
        show_text('窗口的平滑缩小，也是我第一次这样做',(0,0,0),(0,150-y),20)
        show_text('我永远是大家的朋友，我有洛谷、B站',(0,0,0),(0,170-y),20)
        show_text('链接我到时候会放在评论区',(0,0,0),(0,190-y),20)
        show_text('大家有什么可以在C站以及上面的留言',(0,0,0),(0,210-y),20)
        show_text('我早晚会看的',(0,0,0),(0,230-y),20)
        show_text('我退站是因为我要进入省重点初中了',(0,0,0),(0,250-y),20)
        show_text('它的名字叫“天一实验中学”，能搜到的',(0,0,0),(0,270-y),20)
        show_text('为了理想我们应该去不懈奋斗',(0,0,0),(0,290-y),20)
        show_text('我会去住宿，一个星期回来一次',(0,0,0),(0,310-y),20)
        show_text('作业会很多，来的时间很少',(0,0,0),(0,330-y),20)
        show_text('不过我一定会来的',(0,0,0),(0,350-y),20)
        show_text('我有一种信仰，我会为了成功而用正面方法不断追求',(0,255,0),(0,370-y),20)
        show_text('我相信，仁可能会暂时输给恶，但一定会永久战胜恶',(0,255,0),(0,390-y),20)
        show_text('只要坚持不懈，惟正惟恒，我们一定会成功的！',(0,255,0),(0,410-y),20)
        show_text('相信自己，成就美好的未来！',(0,0,0),(0,430-y),20)
        show_text('让我们加油吧！',(0,0,0),(0,450-y),20)
        show_text('虽然',(255,0,0),(0,470-y),50)
        show_text('很多人不喜欢哲学',(0,0,0),(0,520-y),20)
        show_text('但是',(255,0,0),(0,540-y),60)
        show_text('哲学穿透了很多人',(0,0,0),(0,600-y),20)
        show_text('我们应该看清事物本质，得到最好的结果！',(0,0,0),(0,620-y),20)
        show_text('最后，',(11,11,255),(0,640-y),100)   # 又是11
        show_text('谢谢大家',(0,0,0),(0,740-y))
        show_text('祝我们前程似锦！',(0,0,0),(0,770-y))
        show_text('话不多说了，时间飞逝',(255,0,255),(0,800-y))
        show_text('我们进入下一个环节吧！(按n)',(255,0,255),(0,830-y))
        pygame.display.update()
    
    while part == 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    showindex += 1
                    break
        screen.fill((255,255,255))
        if showindex == 1:
            show_text('C站简史[单击继续]',(0,0,0),(0,0))
        if showindex == 2:
            show_text('2017年，编程社区成立',(0,0,0),(0,0))
            show_text('啥也没有但有3个测试作品',(0,0,0),(0,30))
            show_text('2018年，c++区火了',(0,0,0),(0,60))
            show_text('火泉就是，第一个工作室',(0,0,0),(0,90))
        if showindex == 3:
            show_text('sc熊伟时代',(0,0,0),(0,0))
            show_text('python小饼干老师当然厉害',(0,0,0),(0,30))
            show_text('c++发达，火泉全盛',(0,0,0),(0,60))
            show_text('2018年底，小轩发现社区',(0,0,0),(0,90))
        if showindex == 4:
            show_text('星空景然，抄袭大王',(0,0,0),(0,0))
            show_text('刘东亿搬运sc大作',(0,0,0),(0,30))
            show_text('金色穹顶出来，火泉谢幕',(0,0,0),(0,60))
            show_text('吴振发自己开发sc大作',(0,0,0),(0,90))
        if showindex == 5:
            show_text('2019/1社区版面是红白色',(0,0,0),(0,0))
            show_text('就一个主页，和三个按钮',(0,0,0),(0,30))
            show_text('scratch/python/c++',(0,0,0),(0,60))
            show_text('最新发布、最热发布',(0,0,0),(0,90))
        if showindex == 6:
            show_text('没有个人主页，主页就是作品管理',(0,0,0),(0,0))
            show_text('没有封面，更没有勋章',(0,0,0),(0,30))
            show_text('点赞了一段时间可以再点一次',(0,0,0),(0,60))
            show_text('不能关注没有改变直接是源码',(0,0,0),(0,90))
        if showindex == 7:
            show_text('作品介绍附在作品底部',(0,0,0),(0,0))
            show_text('黄色背景，没有硬件编程',(0,0,0),(0,30))
            show_text('python只有基础没有高阶',(0,0,0),(0,60))
            show_text('不能上传素材，没有搜索框',(0,0,0),(0,90))
        if showindex == 8:
            show_text('而且没有头像',(0,0,0),(0,0))
            show_text('上课时，h5直接刷屏',(0,0,0),(0,30))
            show_text('快速按键，不用等待时间',(0,0,0),(0,60))
            show_text('一起卡bug，评论区激烈',(0,0,0),(0,90))
            show_text('但我们，很快乐！',(0,0,0),(0,120))
        if showindex == 9:
            show_text('yzy变成python大佬',(0,0,0),(0,0))
            show_text('zzj开发survive沙盒',(0,0,0),(0,30))
            show_text('scratch改为“图形化编程”',(0,0,0),(0,60))
            show_text('最新发布、最热发布还有课堂巩固',(0,0,0),(0,90))
        if showindex == 10:
            show_text('有人会刷赞，不少人购买',(0,0,0),(0,0))
            show_text('小饼干打压他，社区恢复',(0,0,0),(0,30))
            show_text('有了改编，有了搜索框',(0,0,0),(0,60))
            show_text('2020/8，大更新来袭',(0,0,0),(0,90))
        if showindex == 11:
            show_text('猫博士，秃头管理员',(0,0,0),(0,0))
            show_text('新作品界面，黄色界面',(0,0,0),(0,30))
            show_text('有了个人主页，有消息有关注',(0,0,0),(0,60))
            show_text('有首页有收藏改编惊讶全站',(0,0,0),(0,90))
        if showindex == 12:
            show_text('改名C站，C站守卫军出现',(0,0,0),(0,0))
            show_text('大佬却开始退站，渐渐变少',(0,0,0),(0,30))
            show_text('星光工作室、火焰工作室',(0,0,0),(0,60))
            show_text('一个个都衰弱',(0,0,0),(0,90))
        if showindex == 13:
            show_text('火焰lby，其实只会水作',(0,0,0),(0,0))
            show_text('wdd更是超级水王',(0,0,0),(0,30))
            show_text('fhh没技术，pyj也水作',(0,0,0),(0,60))
            show_text('终有一天，火焰崩溃',(0,0,0),(0,90))
        if showindex == 14:
            show_text('syy水作，受到支持',(0,0,0),(0,0))
            show_text('大家打压，成功了啊',(0,0,0),(0,30))
            show_text('C站开始，出现混风',(0,0,0),(0,60))
            show_text('功能很多，但不稳定~~~',(0,0,0),(0,90))
        if showindex == 15:
            show_text('如今2018级的还有几人？',(0,0,0),(0,0))
            show_text('我未曾再找到第二人！',(0,0,0),(0,30))
            show_text('纷纷退站，然而我今天也……',(0,0,0),(0,60))
            show_text('这些道理小白不懂……',(0,0,0),(0,90))
        if showindex == 16:
            webbrowser.open('index.html')
            part = 4
            flag = 0
        pygame.display.update()
    
    while part == 4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == ord('n'):
                    flag = 1
                    break
        screen.fill((255,255,255))
        if flag == 0:
            show_text('看完网页按n继续',(0,0,0),(0,0))
        if flag == 1:
            show_text('更多更多也说不完了，我们等下一个时光穹窿吧',(0,0,0),(0,0),20)
            show_text('我难得会回来的，我还会发作品的，初中住宿没时间很正常',(0,0,0),(0,20),20)
            show_text('bye~',(0,0,0),(0,40),20)
        pygame.display.update()