# 最高级警告：追踪机和他的子弹都有参数，part5的追踪机之做了一半!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 1级警告：part5敌机+老怪的子弹偏航！！！！！！！！！！！！！！！！！！！
# 2级警告：暂无pass！！！！！
# 3级警告：成功界面！！！
# 3级警告：失败界面、游戏结束界面、退出界面！！！
# 3级警告：格式化和新的类！！！
# 3级警告：实施强攻敌机！！！
# 4级警告：暂无pass！！
# 5级警告：暂无pass！
# 消息：赶工制作！




























































import pygame,sys,random
from time import *
from tkinter import *
from tkinter import messagebox

pygame.init()

a = '''版本1 草稿------------------------2021.3.13 始
宇宙战舰大战-草稿-V0.1：导库
宇宙战舰大战-草稿-V0.2：小框架
宇宙战舰大战-草稿-V0.3：英雄战舰类的极小部分小型框架
宇宙战舰大战-草稿-V0.4：关数变量
宇宙战舰大战-草稿-V0.5：战舰（火箭）英雄初始化
宇宙战舰大战-草稿-V0.6：战舰英雄移动
宇宙战舰大战-草稿-V0.7：战舰英雄移变身鼠标，隐藏鼠标
宇宙战舰大战-草稿-V0.8：子弹类以及他的初始化
宇宙战舰大战-草稿-V0.9：子弹类的更新，创建对象，调用，实例化；开始pygame框架

版本2 模拟------------------------2021.3.16 始
宇宙战舰大战-模拟-V0.1：发子弹完成
宇宙战舰大战-模拟-V0.2：发子弹音效
宇宙战舰大战-模拟-V0.3：发子弹优化
宇宙战舰大战-模拟-V0.4：大更：整体优化+类优化+pygame优化+时间戳
宇宙战舰大战-模拟-V0.5：发子弹声音三拍子（基于我的音乐天赋和我的全校领唱职位）
宇宙战舰大战-模拟-V0.6：普通敌机类+初始化
宇宙战舰大战-模拟-V0.7：敌机如子弹灵活显示
宇宙战舰大战-模拟-V0.8：敌机\子弹碰撞效果
宇宙战舰大战-模拟-V0.9：优化
宇宙战舰大战-模拟-V1.0：敌机\我机碰撞递减（看不见）
宇宙战舰大战-模拟-V1.1：敌机子弹类创建
宇宙战舰大战-模拟-V1.2：敌机子弹类继承
宇宙战舰大战-模拟-V1.3：再次优化
宇宙战舰大战-模拟-V1.4：敌机子弹类优化
宇宙战舰大战-模拟-V1.5：敌机子弹类完成
宇宙战舰大战-模拟-V1.6~V2.0：敌机的list、超级4层遍历、多次超级遍历

版本3 迭代------------------------2021.4.3 始
宇宙战舰大战-迭代-V0.0.1：整体优化
宇宙战舰大战-迭代-V0.0.2~V0.1.8：整体优化，类全部优化，增加遍历，变量，英雄抵抗血量、子弹对抗血
宇宙战舰大战-迭代-V0.1.8~V1.4.2：整体优化，类全部优化，处理了老怪类，老怪遍历以及相应的重做、升级、改bug
宇宙战舰大战-迭代-V1.4.3：老怪超层遍历
宇宙战舰大战-迭代-V1.4.4：老怪子弹夹子
宇宙战舰大战-迭代-V1.4.5~V1.4.7：老怪子弹发射
宇宙战舰大战-迭代-V1.4.8~V1.6.2：老怪、英雄、子弹碰撞
宇宙战舰大战-迭代-V1.6.3~V2.0.0：所有更新+优化，模板、类、框架基本落实完成，第一关完成，主页架子

版本4 测试（迭代2）---------------2021.4.5 始 
宇宙战舰大战-测试-V1：整体优化，第一关优化
宇宙战舰大战-测试-V2：整体优化，定义快速敌机类、快速敌机子弹类、血厚敌机类，调整代码美观，做好布局
宇宙战舰大战-测试-V3：定义类、第二关增加许多函数、超级遍历，第二关框架设置，快敌机出现
宇宙战舰大战-测试-V4：整体优化，第二关全完成，类多，改了18个bug!
宇宙战舰大战-测试-V5：整体优化，第二关全优化，改了13个bug，如敌机血量错误变化等
宇宙战舰大战-测试-V6：1、2关衔接、优化
宇宙战舰大战-测试-V7：开始、优化、选关init
宇宙战舰大战-测试-V8：优化，加载，还有区分首页、主页
宇宙战舰大战-测试-V9：所有全部、超级优化，英雄血量条，血量条类
宇宙战舰大战-测试-V10：终极优化
宇宙战舰大战-测试-附录夹板：优化+首页美化+作者大学习
宇宙战舰大战-测试-V1+：首页继续美化
宇宙战舰大战-测试-V2+：主页继续美化
宇宙战舰大战-测试-V3+：衔接与美化
宇宙战舰大战-测试-V4+：整体优化
宇宙战舰大战-测试-Vs1：类优化，整体美化
宇宙战舰大战-测试-Vs2：选关框架
宇宙战舰大战-测试-Vs3~s5：第三关框架，选关测试模拟，第三关变量初始化与老怪类准备
宇宙战舰大战-测试-Vs6~s14：第三关完成、优化，第三关老怪好了！！！庆贺
宇宙战舰大战-测试-Vs15~s16：第三关完成、优化，梦想的通关选关和第一二关衔接好了！！！庆贺
宇宙战舰大战-测试-Vs17~s20：第四关按钮、前几关优化，第一关漏掉的初始化，tk的messageBox优化显示
宇宙战舰大战-测试-Vs21~s30：选关按钮点亮显示，前三关优化
宇宙战舰大战-测试-bigVersion-Final_test：全部优化、衔接、完成测试版期末测试
宇宙战舰大战-测试-bigVersion-good_test：再次全部优化、衔接
小轩附录：“测试版终于结束了！”

版本5 延伸（迭代3）---------------2021.5.1 始 （劳动节新版本：猛然增加关数）
宇宙战舰大战-延伸-V1~10：整体优化，改一个超难bug:发子弹的不再是领头雁，而是每个敌机！！！
宇宙战舰大战-延伸-V11~15：整体优化，改一个普通bug，提高难度，增加趣味性！！！
宇宙战舰大战-延伸-V16~30：整体优化，改一个超级无敌本机最难bug，提高难度，增加趣味性，完成几个类，增加敌机，设立第四关！！！
宇宙战舰大战-延伸-V31~40：整体优化，完成第四关，插入第五关按钮
宇宙战舰大战-延伸-V41~43：整体优化，成功完成老怪子弹的难度碰撞检测top,bottom,left,right和屏幕上下左右碰撞，机会和运动方式
宇宙战舰大战-延伸-V43~50：整体优化，血量条美化（颜色+长度+宽度）
宇宙战舰大战-延伸-V51[附录]：整体优化，解决第三关bug，增加选关按钮（共100个）和选关提示，巩固程序，到此1400多行代码
宇宙战舰大战-延伸-V52[附录]：整体优化，第11次内测
宇宙战舰大战-延伸-V53~70：大更追踪机、第五关老怪
宇宙战舰大战-延伸-V71~80：第五关普通机构
宇宙战舰大战-延伸-V80~89：第五关完结。。。
'''
# print(a)

try:import ntpath
except:osingxing = 'kaittf'
else:osingxing = 'kaiti';del ntpath



class MineInitialSetting(object):
    def __init__(self):
        self.name = '我的初始设置cls版本'
    
    @classmethod
    def text(cls,size=30,body='你好,小轩',color=(0,0,0),textbodyable=True,pos=(0,0)):
        screen.blit(pygame.font.SysFont(osingxing,size).render(body,textbodyable,color),pos)
    @classmethod
    def show_img(cls,name='picture.png',pos=(0,0)):
        screen.blit(pygame.image.load(name),pos)
    @classmethod
    def collide_mouse(cls,img1,pos,x,y):
        img1 = pygame.image.load(img1)
        img1_rect = img1.get_rect()
        img1_rect.x = x
        img1_rect.y = y
        if img1_rect.collidepoint(pos):
            collidestate = True
        else:
            collidestate = False
        return collidestate


class HealthLine(object):
    def __init__(self,planePos,planehp,planewidth,planetype,inithp): # 最后一个英雄输入1000，栗子而已，懂吗
        self.pos = planePos
        self.hp = planehp
        self.getwidth = planewidth
        if planetype == 'Bossen':
            self.reallywidth = 300 / inithp * self.hp
        else:
            self.reallywidth = 100 / inithp * self.hp         # if HP == 1000,hp == 500,length=100
        self.blue = inithp
        self.greenblue = inithp / 5 * 4
        self.green = inithp / 5 * 3
        self.redgreen = inithp / 5 * 2
        self.red = inithp / 5
        if planetype == 'hero':
            self.rect = pygame.Rect(self.pos[0],self.pos[1]+self.getwidth+20,self.reallywidth,11)
            self.lierect = pygame.Rect(self.pos[0],self.pos[1]+self.getwidth+20,100,11)
        elif planetype == 'Bossen':
            self.rect = pygame.Rect(self.pos[0],self.pos[1]-20,self.reallywidth,18)
            self.lierect = pygame.Rect(self.pos[0],self.pos[1]-20,300,18)
        else:
            self.rect = pygame.Rect(self.pos[0],self.pos[1]-20,self.reallywidth,11)
            self.lierect = pygame.Rect(self.pos[0],self.pos[1]-20,100,11)
    def show(self):
        if self.hp <= self.red:
            self.colors = (255,0,0)
        elif self.hp <= self.redgreen:
            self.colors = (255,255,0)
        elif self.hp <= self.green:
            self.colors = (0,255,0)
        elif self.hp <= self.greenblue:
            self.colors = (0,255,255)
        else:
            self.colors = (0,0,255)
        pygame.draw.rect(screen,(150,150,150),self.lierect,0)
        pygame.draw.rect(screen,self.colors,self.rect,0)


class Hero(object):
    def __init__(self):
        self.HP = 1000
        self.img = pygame.transform.scale(pygame.image.load("PyBox\image\火箭.png"),(70,100))
        self.rect = self.img.get_rect()
        self.rect.center = (0,750)
        self.healthLine = HealthLine((self.rect.x,self.rect.y),self.HP,self.rect.width,'hero',1000)
    def move(self,HeroPOS):
        self.rect.center = HeroPOS
        self.healthLine = HealthLine((self.rect.x,self.rect.y),self.HP,self.rect.width,'hero',1000)
    def show(self,screen):
        screen.blit(self.img, self.rect)
        self.healthLine.show()

hero = Hero()


class Bullet(object):
    def __init__(self):
        self.AttackValue = 50
        self.img = pygame.image.load("PyBox\image\子弹.png")
        self.rect = self.img.get_rect()
        self.rect.center = hero.rect.center
    def move(self):
        self.rect.y -= 2
    def show(self,screen):
        screen.blit(self.img, self.rect)

class NormalEnemyBullet(Bullet):
    def __init__(self,pos):
        super().__init__()
        self.img = pygame.image.load("PyBox\image\敌子弹.png")
        self.rect.center = pos
    def move(self):
        self.rect.y += 2

class FastEnemyBullet(NormalEnemyBullet):
    def __init__(self,pos):
        super().__init__(pos)
    def move(self):
        self.rect.y += 3

class StormEnemyBullet(NormalEnemyBullet):
    def __init__(self,pos):
        super().__init__(pos)
        self.AttackValue = 100
        self.img = pygame.image.load("PyBox\image\敌子弹.png")
        self.img = pygame.transform.scale(self.img,(35,35))

class FhsEnemyBullet(StormEnemyBullet):
    def __init__(self,pos):
        super().__init__(pos)
    def move(self):
        self.rect.y += 3

class LineEnemyBullet(FhsEnemyBullet):
    def __init__(self,pos):
        super().__init__(pos)
    def move(self,h):
        self.rect.y += 2
        if self.rect.x <= h.rect.x:
            self.rect.x += 2
        else:
            self.rect.x -= 2

class LevelBossBullet1(NormalEnemyBullet):
    def __init__(self,pos):
        super().__init__(pos)
        self.AttackValue = 100
        self.img = pygame.transform.scale(pygame.image.load("PyBox\image\敌子弹.png"),(50,50))
    def move(self):
        self.rect.y += 3

class LevelBossBullet3(LevelBossBullet1):
    def __init__(self,pos):
        super().__init__(pos)
        self.AttackValue = 100
        self.img = pygame.transform.scale(pygame.image.load("PyBox\image\敌子弹.png"),(50,50))
        self.way = "don't know"
    def move(self):
        self.rect.y += 3
        if self.rect.right >= 1000:
            self.way = 'left'
        elif self.rect.left <= 0:
            self.way = 'right'
        if self.way == 'left':
            self.rect.x -= 3
        else:
            self.rect.x += 3

class LevelBossBullet5(LevelBossBullet3):
    def __init__(self,pos):
        super().__init__(pos)
        self.AttackValue = 15
        self.img = pygame.transform.scale(pygame.image.load("PyBox\image\敌子弹.png"),(10,10))
        self.way = "don't know"
        self.way2 = "down"
        self.chance = 3
    def move(self):
        if self.rect.right >= 1000:
            self.way = 'left'
        elif self.rect.left <= 0:
            self.way = 'right'
        if self.way == 'left':
            self.rect.x -= 7
        else:
            self.rect.x += 7
        if self.rect.bottom >= 800:
            self.way2 = "up"
            self.chance -= 1
        elif self.rect.top <= 0:
            self.way2 = "down"
        if self.way == 'up':
            self.rect.y -= 5
        else:
            self.rect.y += 5


class NormalEnemy(object):
    def __init__(self):
        self.HP = 50
        self.img = pygame.transform.scale(pygame.image.load("PyBox\image\敌机.jpg"),(80,55))
        self.rect = self.img.get_rect()
        self.rect.center = (random.randint(0,900),-50)
        self.bullet_list = [NormalEnemyBullet(self.rect.center)]
        self.fire_wait_time_stamp_start = time()
        self.fire_wait_time_stamp_end = 'wait for end'
    def move(self):
        self.rect.y += 1
    def show(self,screen):
        screen.blit(self.img, self.rect)
    def add_bullet(self):
        self.bullet_list.append(NormalEnemyBullet(self.rect.center))
    def fire(self,screen):
        for i in self.bullet_list:
            i.move()
            i.show(screen)


class GoodHPEnemy(NormalEnemy):
    def __init__(self):
        super().__init__()
        self.HP = 200
        self.img = pygame.transform.scale(pygame.image.load("PyBox\image\血厚敌机.jpg"),(120,80))
    def move(self):
        self.rect.y += 1
        self.healthLine = HealthLine((self.rect.x,self.rect.y),self.HP,self.rect.width,'hpen',200)
        self.healthLine.show()

class FastEnemy(NormalEnemy):
    def __init__(self):
        super().__init__()
        self.HP = 100
        self.img = pygame.transform.scale(pygame.image.load("PyBox\image\快速敌机.png"),(120,80))
        self.bullet_list = [FastEnemyBullet(self.rect.center)]
    def move(self):
        self.rect.y += 2
        self.healthLine = HealthLine((self.rect.x,self.rect.y),self.HP,self.rect.width,'fen',100)
        self.healthLine.show()
    def add_bullet(self):
        self.bullet_list.append(FastEnemyBullet(self.rect.center))

class StormEnemy(NormalEnemy):
    def __init__(self):
        super().__init__()
        self.HP = 150
        self.img = pygame.transform.scale(pygame.image.load("PyBox\image\强攻敌机.png"),(100,100))
    def move(self):
        self.rect.y += 1
        self.healthLine = HealthLine((self.rect.x,self.rect.y),self.HP,self.rect.width,'sen',150)
        self.healthLine.show()
    def add_bullet(self):
        self.bullet_list.append(StormEnemyBullet(self.rect.center))

class FhsEnemy(StormEnemy):
    def __init__(self):
        super().__init__()
        self.HP = 230
        self.img = pygame.transform.scale(pygame.image.load("PyBox\image\敌机老怪大红.png"),(120,80))
    def move(self):
        self.rect.y += 2
        self.healthLine = HealthLine((self.rect.x,self.rect.y),self.HP,self.rect.width,'fhen',230)
        self.healthLine.show()
    def add_bullet(self):
        self.bullet_list.append(FhsEnemyBullet(self.rect.center))

class LineEnemy(FhsEnemy):
    def __init__(self):
        super().__init__()
        self.HP = 180
        self.img = pygame.transform.scale(pygame.image.load("PyBox\image\追踪机.png"),(100,100))
    def move(self,h):
        if self.rect.y <= h.rect.y:
            self.rect.y += 1
        else:
            self.rect.y -= 1
        if self.rect.x <= h.rect.x:
            self.rect.x += 1
        else:
            self.rect.x -= 1
        self.healthLine = HealthLine((self.rect.x,self.rect.y),self.HP,self.rect.width,'len',180)
        self.healthLine.show()
    def add_bullet(self):
        self.bullet_list.append(LineEnemyBullet(self.rect.center))


class LevelBoss1(NormalEnemy):
    def __init__(self):
        super().__init__()
        self.HP = 1000
        self.img = pygame.transform.scale(pygame.image.load("PyBox\image\关1老怪.jpg"),(480,330))
        self.rect = self.img.get_rect()
        self.rect.center = (random.randint(0,900),-50)
        self.bullet_list = [LevelBossBullet1(self.rect.center)]
        self.way = "don't know"
    def move(self):
        if self.rect.y <= 50:
            self.rect.y += 1
        else:
            self.rect.y += random.randint(-1,1)
        if self.rect.right >= 1000:
            self.way = 'left'
        elif self.rect.left <= 0:
            self.way = 'right'
        if self.way == 'left':
            self.rect.x -= 1
        else:
            self.rect.x += 1
        self.hs()
    def hs(self):
        self.healthLine = HealthLine((self.rect.x,self.rect.y),self.HP,self.rect.width,'Bossen',1000)
        self.healthLine.show()
    def add_bullet(self):
        self.bullet_list.append(LevelBossBullet1(self.rect.center))

class LevelBoss2(LevelBoss1):
    def __init__(self):
        super().__init__()
        self.HP = 2200
        self.img = pygame.transform.scale(pygame.image.load("PyBox\image\敌机老怪大红.png"),(480,330))
        self.bullet_list = [LevelBossBullet1((self.rect.center[0]-100,self.rect.center[1])),LevelBossBullet1((self.rect.center[0]+100,self.rect.center[1]))]
    def hs(self):
        self.healthLine = HealthLine((self.rect.x,self.rect.y),self.HP,self.rect.width,'Bossen',2200)
        self.healthLine.show()
    def add_bullet(self):
        self.bullet_list.append(LevelBossBullet1((self.rect.center[0]-100,self.rect.center[1])))
        self.bullet_list.append(LevelBossBullet1((self.rect.center[0]+100,self.rect.center[1])))
    def show(self,screen):
        screen.blit(self.img, self.rect)

class LevelBoss3(LevelBoss2):
    def __init__(self):
        super().__init__()
        self.HP = 3000
        self.img = pygame.transform.scale(pygame.image.load("PyBox\image\第3老怪.png"),(420,380))
        self.bullet_list = [LevelBossBullet3((self.rect.center[0]-100,self.rect.center[1])),LevelBossBullet3((self.rect.center[0]+100,self.rect.center[1]))]
    def hs(self):
        self.healthLine = HealthLine((self.rect.x,self.rect.y),self.HP,self.rect.width,'Bossen',3000)
        self.healthLine.show()
    def add_bullet(self):
        self.bullet_list.append(LevelBossBullet3((self.rect.center[0]-100,self.rect.center[1])))
        self.bullet_list.append(LevelBossBullet3((self.rect.center[0]+100,self.rect.center[1])))

class LevelBoss4(LevelBoss3):
    def __init__(self):
        super().__init__()
        self.HP = 3500
        self.img = pygame.transform.scale(pygame.image.load("PyBox\image\老怪4.png"),(420,380))
    def move(self):
        if self.rect.y <= 60:
            self.rect.y += 2
        else:
            self.rect.y += random.randint(-1,1)
        if self.rect.right >= 1000:
            self.way = 'left'
        elif self.rect.left <= 0:
            self.way = 'right'
        if self.way == 'left':
            self.rect.x -= 2
        else:
            self.rect.x += 2
        self.hs()
    def hs(self):
        self.healthLine = HealthLine((self.rect.x,self.rect.y),self.HP,self.rect.width,'Bossen',3500)
        self.healthLine.show()

class LevelBoss5(LevelBoss4):
    def __init__(self):
        super().__init__()
        self.HP = 4200
        self.img = pygame.transform.scale(pygame.image.load("PyBox\image\快速敌机.png"),(456,386))
    def add_bullet(self):
        self.bullet_list.append(LevelBossBullet5((self.rect.center[0]-100,self.rect.center[1])))
        self.bullet_list.append(LevelBossBullet5((self.rect.center[0]+100,self.rect.center[1])))
    def hs(self):
        self.healthLine = HealthLine((self.rect.x,self.rect.y),self.HP,self.rect.width,'Bossen',4200)
        self.healthLine.show()
    


class Levelbutton():
    def __init__(self,x,y):
        self.name = '已开锁'
        self.img = pygame.image.load('PyBox\image\按钮框1.png')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

class Levelbutton2():
    def __init__(self,x,y):
        self.name = '未开锁'
        self.img = pygame.image.load('PyBox\image\按钮框2.png')
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y





part = '主页'
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("宇宙战舰大战")
sound = pygame.mixer.Sound('PyBox\music\sound\子弹发射音效.wav')
levelbuttonList = [Levelbutton(10,50)]+[Levelbutton2(70+i*60,50) for i in range(15)]+[Levelbutton2(10+i*60,110+i2*60) for i2 in range(5) for i in range(16)]+[Levelbutton2(10+i*60,110+5*60) for i in range(4)]





while True:
    while part == '首页':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mPos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MineInitialSetting.collide_mouse('PyBox\image\startgame.png',mPos,425,225) == True:
                    part = '加载'
        pygame.mouse.set_visible(True)
        PartSetScreenFillTimeStamp0 = time()
        if (int(PartSetScreenFillTimeStamp0) % 6 == 0) or (int(PartSetScreenFillTimeStamp0) % 6 == 1):
            screen.fill((68,185,211))
        if (int(PartSetScreenFillTimeStamp0) % 6 == 2) or (int(PartSetScreenFillTimeStamp0) % 6 == 3):
            screen.fill((255,223,48))
        if (int(PartSetScreenFillTimeStamp0) % 6 == 4) or (int(PartSetScreenFillTimeStamp0) % 6 == 5):
            screen.fill((14,225,37))
        MineInitialSetting.text(size=50,body='小轩版宇宙战舰大战',color=(125,2,120),pos=(275,35))
        MineInitialSetting.text(size=30,body='Version extension 89',color=(50,255,45),pos=(150,100))
        MineInitialSetting.text(size=20,body='宇宙工作室室长 小轩 亲手原创 代码1000行',color=(217,33,24),pos=(400,105))
        MineInitialSetting.text(size=25,body='飞机大战的重磅升级',color=(150,150,24),pos=(350,130))
        MineInitialSetting.text(size=30,body='点击下方按钮进入主页吧！',color=(217,33,24),pos=(300,175))
        MineInitialSetting.show_img(name='PyBox\image\startgame.png',pos=(425,225))
        pygame.time.Clock().tick(100)
        pygame.display.update()
    
    
    if part == '加载':load_times = 0
    while part == '加载':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if load_times >= 4:
            part = '主页'
        # 主要算法
        for i in range(20):
            screen.fill((255,255,255))
            if load_times == 0:
                screen.blit(pygame.font.SysFont(osingxing,30).render((' '*19),True,(100,100,100),(100,100,100)),(400,50))
                screen.blit(pygame.font.SysFont(osingxing,30).render((' '*i),True,(0,255,255),(0,255,255)),(400,50))
            if load_times == 1:
                screen.blit(pygame.font.SysFont(osingxing,30).render((' '*19),True,(0,255,255),(0,255,255)),(400,50))
                screen.blit(pygame.font.SysFont(osingxing,30).render((' '*i),True,(255,10,10),(255,10,10)),(400,50))
            if load_times == 2:
                screen.blit(pygame.font.SysFont(osingxing,30).render((' '*19),True,(255,10,10),(255,10,10)),(400,50))
                screen.blit(pygame.font.SysFont(osingxing,30).render((' '*i),True,(255,255,0),(255,255,0)),(400,50))
            if load_times == 3:
                screen.blit(pygame.font.SysFont(osingxing,30).render((' '*19),True,(255,255,0),(255,255,0)),(400,50))
                screen.blit(pygame.font.SysFont(osingxing,30).render((' '*i),True,(255,0,255),(255,0,255)),(400,50))
            if load_times == 4:
                screen.blit(pygame.font.SysFont(osingxing,30).render((' '*19),True,(255,0,255),(255,0,255)),(400,50))
                screen.blit(pygame.font.SysFont(osingxing,30).render((' '*i),True,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(random.randint(0,255),random.randint(0,255),random.randint(0,255))),(400,50))
            screen.blit(pygame.font.SysFont(osingxing,30).render(('正在玩命加载中'+'.'*(i%6)),True,(0,140,255)),(400,100))
            screen.blit(pygame.font.SysFont(osingxing,30).render(('%'+str(i*5)+' '*4+str(load_times+1)+'/5'),True,(0,100,255)),(400,150))
            screen.blit(pygame.font.SysFont(osingxing,30).render(('加载'+random.choice(["服务器","数据包","素材","代码","堆栈","库","游戏资料","上传运行","机器识别","人工智能",'抽取资料','安全防护','其他'])),True,(0,255,255)),(400,200))
            sleep(0.07)
            if i == 6:
                sleep(0.06)
            if i == 17:
                sleep(0.1)
            if i == 19:
                sleep(0.04)
            pygame.display.update()
        load_times += 1
    
    
    
    while part == '主页':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mPos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MineInitialSetting.collide_mouse('PyBox\image\startgame.png',mPos,425,225):
                    part = '选关'
        pygame.mouse.set_visible(True)
        PartSetScreenFillTimeStamp0 = time()
        if (int(PartSetScreenFillTimeStamp0) % 6 == 0) or (int(PartSetScreenFillTimeStamp0) % 6 == 1):
            screen.fill((68,185,211))
        if (int(PartSetScreenFillTimeStamp0) % 6 == 2) or (int(PartSetScreenFillTimeStamp0) % 6 == 3):
            screen.fill((255,223,48))
        if (int(PartSetScreenFillTimeStamp0) % 6 == 4) or (int(PartSetScreenFillTimeStamp0) % 6 == 5):
            screen.fill((14,225,37))
        MineInitialSetting.text(size=50,body='小轩版宇宙战舰大战',color=(125,2,120),pos=(275,35))
        MineInitialSetting.text(body='Version extension 89',color=(50,255,45),pos=(150,100))
        MineInitialSetting.text(size=20,body='宇宙工作室室长 小轩 亲手原创 代码1000行',color=(217,33,24),pos=(400,105))
        MineInitialSetting.text(size=25,body='飞机大战的无敌升级',color=(150,150,24),pos=(350,130))
        MineInitialSetting.text(body='点击下方按钮开始挑战游戏吧！！！',color=(217,33,24),pos=(280,175))
        MineInitialSetting.show_img(name='PyBox\image\startgame.png',pos=(425,225))
        pygame.time.Clock().tick(100)
        pygame.display.update()
    
    
    while part == '选关':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mPos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(levelbuttonList)):
                    if levelbuttonList[i].rect.collidepoint(mPos):
                        if levelbuttonList[i].name == '已开锁':
                            part = str(i+1)
                        else:
                            top = Tk()
                            top.withdraw()
                            messagebox.showinfo('提示','不要贪心\n先把前一关过了吧\n还没解锁。。。')
        pygame.mouse.set_visible(True)
        screen.fill((255,100,255))
        MineInitialSetting.text(body='选关',pos=(10,10))
        for i in range(len(levelbuttonList)):
            screen.blit(levelbuttonList[i].img,levelbuttonList[i].rect)
            MineInitialSetting.text(body=str(i+1),pos=(levelbuttonList[i].rect.center[0]-7*len(str(i+1)),levelbuttonList[i].rect.center[1]-15))
        pygame.time.Clock().tick(75)
        pygame.display.update()
    
    
    
    if part == '1':
        bulletList = [Bullet()]
        nEnemyList = [NormalEnemy()]
        bullet_wait_time_stamp_start = time()
        nEnemy_wait_time_stamp_start = time()
        LevelBoss1_fire_wait_time_stamp_start = time()
        part1_nEnemy = 20
    
    while part == '1':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                hero.move(event.pos)
        pygame.mouse.set_visible(False)
        bullet_wait_time_stamp_end = time()
        nEnemy_wait_time_stamp_end = time()
        LevelBoss1_fire_wait_time_stamp_end = time()
        screen.fill((0,0,0))
        hero.show(screen)
        
        for bullet in range(len(bulletList)):
            try:
                bulletList[bullet].show(screen)
                bulletList[bullet].move()
                if bulletList[bullet].rect.y <= -10:
                    bulletList.remove(bulletList[bullet])
            except:
                pass
        
        if bullet_wait_time_stamp_end - bullet_wait_time_stamp_start > 0.3:
            bullet_wait_time_stamp_start = bullet_wait_time_stamp_end
            bulletList.append(Bullet())
            sound.play()
        
        if nEnemy_wait_time_stamp_end - nEnemy_wait_time_stamp_start > 1 and part1_nEnemy > 0:
            nEnemy_wait_time_stamp_start = nEnemy_wait_time_stamp_end
            nEnemyList.append(NormalEnemy())
            part1_nEnemy -= 1
        
        for nEnemy in range(len(nEnemyList)):
            try:
                nEnemyList[nEnemy].show(screen)
                nEnemyList[nEnemy].move()
                nEnemyList[nEnemy].fire_wait_time_stamp_end = time()
                if nEnemyList[nEnemy].rect.y >= 900:
                    nEnemyList[nEnemy].rect.y = -50
                if nEnemyList[nEnemy].fire_wait_time_stamp_end - nEnemyList[nEnemy].fire_wait_time_stamp_start > 1:
                    nEnemyList[nEnemy].fire_wait_time_stamp_start = nEnemyList[nEnemy].fire_wait_time_stamp_end
                    nEnemyList[nEnemy].add_bullet()
            except:
                pass
            try:
                nEnemyList[nEnemy].fire(screen)
            except:
                pass
        
        for bullet in range(len(bulletList)):
            for nEnemy in range(len(nEnemyList)):
                try:
                    if bulletList[bullet].rect.colliderect(nEnemyList[nEnemy].rect):
                        bulletList.remove(bulletList[bullet])
                        nEnemyList.remove(nEnemyList[nEnemy])
                except:
                    pass
        
        for nEnemy in range(len(nEnemyList)):
            try:
                if hero.rect.colliderect(nEnemyList[nEnemy].rect):
                    hero.HP -= nEnemyList[nEnemy].HP
                    nEnemyList.remove(nEnemyList[nEnemy])
                for i in range(len(nEnemyList[nEnemy].bullet_list)):
                    if hero.rect.colliderect(nEnemyList[nEnemy].bullet_list[i]):
                        hero.HP -= nEnemyList[nEnemy].bullet_list[i].AttackValue
                        nEnemyList[nEnemy].bullet_list.remove(nEnemyList[nEnemy].bullet_list[i])
            except:
                pass
        
        if part1_nEnemy == 0:
            part1_nEnemy = -10
            levelBoss1 = LevelBoss1()
        
        if part1_nEnemy == -10:
            levelBoss1.move()
            levelBoss1.show(screen)
            levelBoss1.fire(screen)
            if LevelBoss1_fire_wait_time_stamp_end - LevelBoss1_fire_wait_time_stamp_start > 1:
                LevelBoss1_fire_wait_time_stamp_start = LevelBoss1_fire_wait_time_stamp_end
                levelBoss1.add_bullet()
            if hero.rect.colliderect(levelBoss1.rect):
                pygame.mouse.set_pos((pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]+150))
                hero.HP -= 50
            for i in range(len(levelBoss1.bullet_list)):
                try:
                    if hero.rect.colliderect(levelBoss1.bullet_list[i]):
                        hero.HP -= levelBoss1.bullet_list[i].AttackValue
                        levelBoss1.bullet_list.remove(levelBoss1.bullet_list[i])
                except:
                    pass
            for bullet in range(len(bulletList)):
                try:
                    if bulletList[bullet].rect.colliderect(levelBoss1.rect):
                        levelBoss1.HP -= bulletList[bullet].AttackValue
                        bulletList.remove(bulletList[bullet])
                        if levelBoss1.HP <= 0:
                            levelbuttonList[int(part)] = Levelbutton(70,50)
                            part = '选关'
                except:
                    pass
        
        if hero.HP <= 0:
            part = '主页'
        pygame.time.Clock().tick(400)
        pygame.display.update()
    
    if part == '2':
        hero.HP = 1000
        part2_nEnemy = 25
        part2_fEnemy = 15
        part2_HPEnemy = 10
        bulletList = [Bullet()]
        nEnemyList = [NormalEnemy()]
        fEnemyList = [FastEnemy()]
        HPEnemyList = [GoodHPEnemy()]
        bullet_wait_time_stamp_start = time()
        nEnemy_wait_time_stamp_start = time()
        fEnemy_wait_time_stamp_start = time()
        HPEnemy_wait_time_stamp_start = time()
        LevelBoss2_fire_wait_time_stamp_start = time()
    
    while part == '2':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                hero.move(event.pos)
        pygame.mouse.set_visible(False)
        bullet_wait_time_stamp_end = time()
        nEnemy_wait_time_stamp_end = time()
        fEnemy_wait_time_stamp_end = time()
        HPEnemy_wait_time_stamp_end = time()
        LevelBoss2_fire_wait_time_stamp_end = time()
        screen.fill((0,0,0))
        hero.show(screen)
        
        for bullet in range(len(bulletList)):
            try:
                bulletList[bullet].show(screen)
                bulletList[bullet].move()
                if bulletList[bullet].rect.y <= -10:
                    bulletList.remove(bulletList[bullet])
            except:
                pass
        
        if bullet_wait_time_stamp_end - bullet_wait_time_stamp_start > 0.3:
            bullet_wait_time_stamp_start = bullet_wait_time_stamp_end
            bulletList.append(Bullet())
            sound.play()
        
        if nEnemy_wait_time_stamp_end - nEnemy_wait_time_stamp_start > 1 and part2_nEnemy > 0:
            nEnemy_wait_time_stamp_start = nEnemy_wait_time_stamp_end
            nEnemyList.append(NormalEnemy())
            part2_nEnemy -= 1
        
        if fEnemy_wait_time_stamp_end - fEnemy_wait_time_stamp_start > 1 and part2_fEnemy > 0:
            fEnemy_wait_time_stamp_start = fEnemy_wait_time_stamp_end
            fEnemyList.append(FastEnemy())
            part2_fEnemy -= 1
        
        if HPEnemy_wait_time_stamp_end - HPEnemy_wait_time_stamp_start > 1 and part2_HPEnemy > 0:
            HPEnemy_wait_time_stamp_start = HPEnemy_wait_time_stamp_end
            HPEnemyList.append(GoodHPEnemy())
            part2_HPEnemy -= 1
        
        for nEnemy in range(len(nEnemyList)):
            try:
                nEnemyList[nEnemy].show(screen)
                nEnemyList[nEnemy].move()
                nEnemyList[nEnemy].fire_wait_time_stamp_end = time()
                if nEnemyList[nEnemy].rect.y >= 900:
                    nEnemyList[nEnemy].rect.y = -50
                if nEnemyList[nEnemy].fire_wait_time_stamp_end - nEnemyList[nEnemy].fire_wait_time_stamp_start > 1:
                    nEnemyList[nEnemy].fire_wait_time_stamp_start = nEnemyList[nEnemy].fire_wait_time_stamp_end
                    nEnemyList[nEnemy].add_bullet()
            except:
                pass
            try:
                nEnemyList[nEnemy].fire(screen)
            except:
                pass
        
        for fEnemy in range(len(fEnemyList)):
            try:
                fEnemyList[fEnemy].show(screen)
                fEnemyList[fEnemy].move()
                fEnemyList[fEnemy].fire_wait_time_stamp_end = time()
                if fEnemyList[fEnemy].rect.y >= 900:
                    fEnemyList[fEnemy].rect.y = -50
                if fEnemyList[fEnemy].fire_wait_time_stamp_end - fEnemyList[fEnemy].fire_wait_time_stamp_start > 0.8:
                    fEnemyList[fEnemy].fire_wait_time_stamp_start = fEnemyList[fEnemy].fire_wait_time_stamp_end
                    fEnemyList[fEnemy].add_bullet()
            except:
                pass
            try:
                fEnemyList[fEnemy].fire(screen)
            except:
                pass
        
        for hpEnemy in range(len(HPEnemyList)):
            try:
                HPEnemyList[hpEnemy].show(screen)
                HPEnemyList[hpEnemy].move()
                HPEnemyList[hpEnemy].fire_wait_time_stamp_end = time()
                if HPEnemyList[hpEnemy].rect.y >= 900:
                    HPEnemyList[hpEnemy].rect.y = -50
                if HPEnemyList[hpEnemy].fire_wait_time_stamp_end - HPEnemyList[hpEnemy].fire_wait_time_stamp_start > 1:
                    HPEnemyList[hpEnemy].fire_wait_time_stamp_start = HPEnemyList[hpEnemy].fire_wait_time_stamp_end
                    HPEnemyList[hpEnemy].add_bullet()
            except:
                pass
            try:
                HPEnemyList[hpEnemy].fire(screen)
            except:
                pass
        
        for bullet in range(len(bulletList)):
            for nEnemy in range(len(nEnemyList)):
                try:
                    if bulletList[bullet].rect.colliderect(nEnemyList[nEnemy].rect):
                        bulletList.remove(bulletList[bullet])
                        nEnemyList.remove(nEnemyList[nEnemy])
                except:
                    pass
            for fEnemy in range(len(fEnemyList)):
                try:
                    if bulletList[bullet].rect.colliderect(fEnemyList[fEnemy].rect):
                        bulletList.remove(bulletList[bullet])
                        fEnemyList[fEnemy].HP -= 50
                        if fEnemyList[fEnemy].HP <= 0:
                            fEnemyList.remove(fEnemyList[fEnemy])
                except:
                    pass
            for hpEnemy in range(len(HPEnemyList)):
                try:
                    if bulletList[bullet].rect.colliderect(HPEnemyList[hpEnemy].rect):
                        bulletList.remove(bulletList[bullet])
                        HPEnemyList[hpEnemy].HP -= 50
                        if HPEnemyList[hpEnemy].HP <= 0:
                            HPEnemyList.remove(HPEnemyList[hpEnemy])
                except:
                    pass
        
        for nEnemy in range(len(nEnemyList)):
            try:
                if hero.rect.colliderect(nEnemyList[nEnemy].rect):
                    hero.HP -= nEnemyList[nEnemy].HP
                    nEnemyList.remove(nEnemyList[nEnemy])
                for i in range(len(nEnemyList[nEnemy].bullet_list)):
                    if hero.rect.colliderect(nEnemyList[nEnemy].bullet_list[i]):
                        hero.HP -= nEnemyList[nEnemy].bullet_list[i].AttackValue
                        nEnemyList[nEnemy].bullet_list.remove(nEnemyList[nEnemy].bullet_list[i])
            except:
                pass
        
        for fEnemy in range(len(fEnemyList)):
            try:
                if hero.rect.colliderect(fEnemyList[fEnemy].rect):
                    hero.HP -= fEnemyList[fEnemy].HP
                    fEnemyList.remove(fEnemyList[fEnemy])
                for i in range(len(fEnemyList[fEnemy].bullet_list)):
                    if hero.rect.colliderect(fEnemyList[fEnemy].bullet_list[i]):
                        hero.HP -= fEnemyList[fEnemy].bullet_list[i].AttackValue
                        fEnemyList[fEnemy].bullet_list.remove(fEnemyList[fEnemy].bullet_list[i])
            except:
                pass
        
        for hpEnemy in range(len(HPEnemyList)):
            try:
                if hero.rect.colliderect(HPEnemyList[hpEnemy].rect):
                    hero.HP -= HPEnemyList[hpEnemy].HP
                    HPEnemyList.remove(HPEnemyList[hpEnemy])
                for i in range(len(HPEnemyList[hpEnemy].bullet_list)):
                    if hero.rect.colliderect(HPEnemyList[hpEnemy].bullet_list[i]):
                        hero.HP -= HPEnemyList[hpEnemy].bullet_list[i].AttackValue
                        HPEnemyList[hpEnemy].bullet_list.remove(HPEnemyList[hpEnemy].bullet_list[i])
            except:
                pass
        
        if part2_nEnemy == 0 and part2_fEnemy == 0 and part2_HPEnemy == 0:
            part2_nEnemy = -10
            part2_fEnemy = -10
            part2_HPEnemy = -10
            levelBoss2 = LevelBoss2()
        
        if part2_nEnemy == -10 and part2_fEnemy == -10 and part2_HPEnemy == -10:
            levelBoss2.move()
            levelBoss2.show(screen)
            levelBoss2.fire(screen)
            if LevelBoss2_fire_wait_time_stamp_end - LevelBoss2_fire_wait_time_stamp_start > 1:
                LevelBoss2_fire_wait_time_stamp_start = LevelBoss2_fire_wait_time_stamp_end
                levelBoss2.add_bullet()
            if hero.rect.colliderect(levelBoss2.rect):
                pygame.mouse.set_pos((pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]+150))
                hero.HP -= 50
            for i in range(len(levelBoss2.bullet_list)):
                try:
                    if hero.rect.colliderect(levelBoss2.bullet_list[i]):
                        hero.HP -= levelBoss2.bullet_list[i].AttackValue
                        levelBoss2.bullet_list.remove(levelBoss2.bullet_list[i])
                except:
                    pass
            for bullet in range(len(bulletList)):
                try:
                    if bulletList[bullet].rect.colliderect(levelBoss2.rect):
                        levelBoss2.HP -= bulletList[bullet].AttackValue
                        bulletList.remove(bulletList[bullet])
                        if levelBoss2.HP <= 0:
                            levelbuttonList[int(part)] = Levelbutton(130,50)
                            part = '选关'
                except:
                    pass
        
        if hero.HP <= 0:
            part = '主页'
        pygame.time.Clock().tick(400)
        pygame.display.update()
    
    if part == '3':
        hero.HP = 1000
        part3_nEnemy = 35
        part3_fEnemy = 25
        part3_HPEnemy = 20
        part3_sEnemy = 10
        bulletList = [Bullet()]
        nEnemyList = [NormalEnemy()]
        fEnemyList = [FastEnemy()]
        HPEnemyList = [GoodHPEnemy()]
        sEnemyList = [StormEnemy()]
        bullet_wait_time_stamp_start = time()
        nEnemy_wait_time_stamp_start = time()
        fEnemy_wait_time_stamp_start = time()
        HPEnemy_wait_time_stamp_start = time()
        sEnemy_wait_time_stamp_start = time()
        LevelBoss3_fire_wait_time_stamp_start = time()
    
    while part == '3':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                hero.move(event.pos)
        pygame.mouse.set_visible(False)
        bullet_wait_time_stamp_end = time()
        nEnemy_wait_time_stamp_end = time()
        fEnemy_wait_time_stamp_end = time()
        HPEnemy_wait_time_stamp_end = time()
        sEnemy_wait_time_stamp_end = time()
        LevelBoss3_fire_wait_time_stamp_end = time()
        screen.fill((0,0,0))
        hero.show(screen)
        
        for bullet in range(len(bulletList)):
            try:
                bulletList[bullet].show(screen)
                bulletList[bullet].move()
                if bulletList[bullet].rect.y <= -10:
                    bulletList.remove(bulletList[bullet])
            except:
                pass
        
        if bullet_wait_time_stamp_end - bullet_wait_time_stamp_start > 0.3:
            bullet_wait_time_stamp_start = bullet_wait_time_stamp_end
            bulletList.append(Bullet())
            sound.play()
        
        if nEnemy_wait_time_stamp_end - nEnemy_wait_time_stamp_start > 1 and part3_nEnemy > 0:
            nEnemy_wait_time_stamp_start = nEnemy_wait_time_stamp_end
            nEnemyList.append(NormalEnemy())
            part3_nEnemy -= 1
        
        if fEnemy_wait_time_stamp_end - fEnemy_wait_time_stamp_start > 1.5 and part3_fEnemy > 0:
            fEnemy_wait_time_stamp_start = fEnemy_wait_time_stamp_end
            fEnemyList.append(FastEnemy())
            part3_fEnemy -= 1
        
        if HPEnemy_wait_time_stamp_end - HPEnemy_wait_time_stamp_start > 2.2 and part3_HPEnemy > 0:
            HPEnemy_wait_time_stamp_start = HPEnemy_wait_time_stamp_end
            HPEnemyList.append(GoodHPEnemy())
            part3_HPEnemy -= 1
        
        if sEnemy_wait_time_stamp_end - sEnemy_wait_time_stamp_start > 1.2 and part3_sEnemy > 0:
            sEnemy_wait_time_stamp_start = sEnemy_wait_time_stamp_end
            sEnemyList.append(StormEnemy())
            part3_sEnemy -= 1
        
        for nEnemy in range(len(nEnemyList)):
            try:
                nEnemyList[nEnemy].show(screen)
                nEnemyList[nEnemy].move()
                nEnemyList[nEnemy].fire_wait_time_stamp_end = time()
                if nEnemyList[nEnemy].rect.y >= 900:
                    nEnemyList[nEnemy].rect.y = -50
                if nEnemyList[nEnemy].fire_wait_time_stamp_end - nEnemyList[nEnemy].fire_wait_time_stamp_start > 1:
                    nEnemyList[nEnemy].fire_wait_time_stamp_start = nEnemyList[nEnemy].fire_wait_time_stamp_end
                    nEnemyList[nEnemy].add_bullet()
            except:
                pass
            try:
                nEnemyList[nEnemy].fire(screen)
            except:
                pass
        
        for fEnemy in range(len(fEnemyList)):
            try:
                fEnemyList[fEnemy].show(screen)
                fEnemyList[fEnemy].move()
                fEnemyList[fEnemy].fire_wait_time_stamp_end = time()
                if fEnemyList[fEnemy].rect.y >= 900:
                    fEnemyList[fEnemy].rect.y = -50
                if fEnemyList[fEnemy].fire_wait_time_stamp_end - fEnemyList[fEnemy].fire_wait_time_stamp_start > 0.8:
                    fEnemyList[fEnemy].fire_wait_time_stamp_start = fEnemyList[fEnemy].fire_wait_time_stamp_end
                    fEnemyList[fEnemy].add_bullet()
            except:
                pass
            try:
                fEnemyList[fEnemy].fire(screen)
            except:
                pass
        
        for hpEnemy in range(len(HPEnemyList)):
            try:
                HPEnemyList[hpEnemy].show(screen)
                HPEnemyList[hpEnemy].move()
                HPEnemyList[hpEnemy].fire_wait_time_stamp_end = time()
                if HPEnemyList[hpEnemy].rect.y >= 900:
                    HPEnemyList[hpEnemy].rect.y = -50
                if HPEnemyList[hpEnemy].fire_wait_time_stamp_end - HPEnemyList[hpEnemy].fire_wait_time_stamp_start > 1:
                    HPEnemyList[hpEnemy].fire_wait_time_stamp_start = HPEnemyList[hpEnemy].fire_wait_time_stamp_end
                    HPEnemyList[hpEnemy].add_bullet()
            except:
                pass
            try:
                HPEnemyList[hpEnemy].fire(screen)
            except:
                pass
        
        for sEnemy in range(len(sEnemyList)):
            try:
                sEnemyList[sEnemy].show(screen)
                sEnemyList[sEnemy].move()
                sEnemyList[sEnemy].fire_wait_time_stamp_end = time()
                if sEnemyList[sEnemy].rect.y >= 900:
                    sEnemyList[sEnemy].rect.y = -50
                if sEnemyList[sEnemy].fire_wait_time_stamp_end - sEnemyList[sEnemy].fire_wait_time_stamp_start > 1:
                    sEnemyList[sEnemy].fire_wait_time_stamp_start = sEnemyList[sEnemy].fire_wait_time_stamp_end
                    sEnemyList[sEnemy].add_bullet()
            except:
                pass
            try:
                sEnemyList[sEnemy].fire(screen)
            except:
                pass
        
        for bullet in range(len(bulletList)):
            for nEnemy in range(len(nEnemyList)):
                try:
                    if bulletList[bullet].rect.colliderect(nEnemyList[nEnemy].rect):
                        bulletList.remove(bulletList[bullet])
                        nEnemyList.remove(nEnemyList[nEnemy])
                except:
                    pass
            for fEnemy in range(len(fEnemyList)):
                try:
                    if bulletList[bullet].rect.colliderect(fEnemyList[fEnemy].rect):
                        bulletList.remove(bulletList[bullet])
                        fEnemyList[fEnemy].HP -= 50
                        if fEnemyList[fEnemy].HP <= 0:
                            fEnemyList.remove(fEnemyList[fEnemy])
                except:
                    pass
            for hpEnemy in range(len(HPEnemyList)):
                try:
                    if bulletList[bullet].rect.colliderect(HPEnemyList[hpEnemy].rect):
                        bulletList.remove(bulletList[bullet])
                        HPEnemyList[hpEnemy].HP -= 50
                        if HPEnemyList[hpEnemy].HP <= 0:
                            HPEnemyList.remove(HPEnemyList[hpEnemy])
                except:
                    pass
            for sEnemy in range(len(sEnemyList)):
                try:
                    if bulletList[bullet].rect.colliderect(sEnemyList[sEnemy].rect):
                        bulletList.remove(bulletList[bullet])
                        sEnemyList[sEnemy].HP -= 50
                        if sEnemyList[sEnemy].HP <= 0:
                            sEnemyList.remove(sEnemyList[sEnemy])
                except:
                    pass
        
        for nEnemy in range(len(nEnemyList)):
            try:
                if hero.rect.colliderect(nEnemyList[nEnemy].rect):
                    hero.HP -= nEnemyList[nEnemy].HP
                    nEnemyList.remove(nEnemyList[nEnemy])
                for i in range(len(nEnemyList[nEnemy].bullet_list)):
                    if hero.rect.colliderect(nEnemyList[nEnemy].bullet_list[i]):
                        hero.HP -= nEnemyList[nEnemy].bullet_list[i].AttackValue
                        nEnemyList[nEnemy].bullet_list.remove(nEnemyList[nEnemy].bullet_list[i])
            except:
                pass
        
        for fEnemy in range(len(fEnemyList)):
            try:
                if hero.rect.colliderect(fEnemyList[fEnemy].rect):
                    hero.HP -= fEnemyList[fEnemy].HP
                    fEnemyList.remove(fEnemyList[fEnemy])
                for i in range(len(fEnemyList[fEnemy].bullet_list)):
                    if hero.rect.colliderect(fEnemyList[fEnemy].bullet_list[i]):
                        hero.HP -= fEnemyList[fEnemy].bullet_list[i].AttackValue
                        fEnemyList[fEnemy].bullet_list.remove(fEnemyList[fEnemy].bullet_list[i])
            except:
                pass
        
        for hpEnemy in range(len(HPEnemyList)):
            try:
                if hero.rect.colliderect(HPEnemyList[hpEnemy].rect):
                    hero.HP -= HPEnemyList[hpEnemy].HP
                    HPEnemyList.remove(HPEnemyList[hpEnemy])
                for i in range(len(HPEnemyList[hpEnemy].bullet_list)):
                    if hero.rect.colliderect(HPEnemyList[hpEnemy].bullet_list[i]):
                        hero.HP -= HPEnemyList[hpEnemy].bullet_list[i].AttackValue
                        HPEnemyList[hpEnemy].bullet_list.remove(HPEnemyList[hpEnemy].bullet_list[i])
            except:
                pass
        
        for sEnemy in range(len(sEnemyList)):
            try:
                if hero.rect.colliderect(sEnemyList[sEnemy].rect):
                    hero.HP -= sEnemyList[sEnemy].HP
                    sEnemyList.remove(sEnemyList[sEnemy])
                for i in range(len(sEnemyList[sEnemy].bullet_list)):
                    if hero.rect.colliderect(sEnemyList[sEnemy].bullet_list[i]):
                        hero.HP -= sEnemyList[sEnemy].bullet_list[i].AttackValue
                        sEnemyList[sEnemy].bullet_list.remove(sEnemyList[sEnemy].bullet_list[i])
            except:
                pass
        
        if part3_nEnemy == 0 and part3_fEnemy == 0 and part3_HPEnemy == 0 and part3_sEnemy == 0:
            part3_nEnemy = -10
            part3_fEnemy = -10
            part3_HPEnemy = -10
            part3_sEnemy = -10
            levelBoss3 = LevelBoss3()
        
        if part3_nEnemy == -10 and part3_fEnemy == -10 and part3_HPEnemy == -10 and part3_sEnemy == -10:
            levelBoss3.move()
            levelBoss3.show(screen)
            levelBoss3.fire(screen)
            if LevelBoss3_fire_wait_time_stamp_end - LevelBoss3_fire_wait_time_stamp_start > 1:
                LevelBoss3_fire_wait_time_stamp_start = LevelBoss3_fire_wait_time_stamp_end
                levelBoss3.add_bullet()
            if hero.rect.colliderect(levelBoss3.rect):
                pygame.mouse.set_pos((pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]+150))
                hero.HP -= 50
            for i in range(len(levelBoss3.bullet_list)):
                try:
                    if hero.rect.colliderect(levelBoss3.bullet_list[i]):
                        hero.HP -= levelBoss3.bullet_list[i].AttackValue
                        levelBoss3.bullet_list.remove(levelBoss3.bullet_list[i])
                except:
                    pass
            for bullet in range(len(bulletList)):
                try:
                    if bulletList[bullet].rect.colliderect(levelBoss3.rect):
                        levelBoss3.HP -= bulletList[bullet].AttackValue
                        bulletList.remove(bulletList[bullet])
                        if levelBoss3.HP <= 0:
                            levelbuttonList[int(part)] = Levelbutton(190,50)
                            part = '选关'
                except:
                    pass
        
        if hero.HP <= 0:
            part = '主页'
        pygame.time.Clock().tick(400)
        pygame.display.update()
    
    if part == '4':
        hero.HP = 1000
        part4_sEnemy = 10
        part4_fhsEnemy = 30
        bulletList = [Bullet()]
        sEnemyList = [StormEnemy()]
        fhsEnemyList = [FhsEnemy()]
        bullet_wait_time_stamp_start = time()
        sEnemy_wait_time_stamp_start = time()
        fhsEnemy_wait_time_stamp_start = time()
        LevelBoss4_fire_wait_time_stamp_start = time()
    
    while part == '4':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                hero.move(event.pos)
        pygame.mouse.set_visible(False)
        bullet_wait_time_stamp_end = time()
        sEnemy_wait_time_stamp_end = time()
        fhsEnemy_wait_time_stamp_end = time()
        LevelBoss4_fire_wait_time_stamp_end = time()
        screen.fill((0,0,0))
        hero.show(screen)
        
        for bullet in range(len(bulletList)):
            try:
                bulletList[bullet].show(screen)
                bulletList[bullet].move()
                if bulletList[bullet].rect.y <= -10:
                    bulletList.remove(bulletList[bullet])
            except:
                pass
        
        if bullet_wait_time_stamp_end - bullet_wait_time_stamp_start > 0.3:
            bullet_wait_time_stamp_start = bullet_wait_time_stamp_end
            bulletList.append(Bullet())
            sound.play()
        
        if sEnemy_wait_time_stamp_end - sEnemy_wait_time_stamp_start > 1 and part4_sEnemy > 0:
            sEnemy_wait_time_stamp_start = sEnemy_wait_time_stamp_end
            sEnemyList.append(StormEnemy())
            part4_sEnemy -= 1
        
        if fhsEnemy_wait_time_stamp_end - fhsEnemy_wait_time_stamp_start > 1.2 and part4_fhsEnemy > 0:
            fhsEnemy_wait_time_stamp_start = fhsEnemy_wait_time_stamp_end
            fhsEnemyList.append(FhsEnemy())
            part4_fhsEnemy -= 1
        
        for sEnemy in range(len(sEnemyList)):
            try:
                sEnemyList[sEnemy].show(screen)
                sEnemyList[sEnemy].move()
                sEnemyList[sEnemy].fire_wait_time_stamp_end = time()
                if sEnemyList[sEnemy].rect.y >= 900:
                    sEnemyList[sEnemy].rect.y = -50
                if sEnemyList[sEnemy].fire_wait_time_stamp_end - sEnemyList[sEnemy].fire_wait_time_stamp_start > 1:
                    sEnemyList[sEnemy].fire_wait_time_stamp_start = sEnemyList[sEnemy].fire_wait_time_stamp_end
                    sEnemyList[sEnemy].add_bullet()
            except:
                pass
            try:
                sEnemyList[sEnemy].fire(screen)
            except:
                pass
        
        for fhsEnemy in range(len(fhsEnemyList)):
            try:
                fhsEnemyList[fhsEnemy].show(screen)
                fhsEnemyList[fhsEnemy].move()
                fhsEnemyList[fhsEnemy].fire_wait_time_stamp_end = time()
                if fhsEnemyList[fhsEnemy].rect.y >= 900:
                    fhsEnemyList[fhsEnemy].rect.y = -50
                if fhsEnemyList[fhsEnemy].fire_wait_time_stamp_end - fhsEnemyList[fhsEnemy].fire_wait_time_stamp_start > 1:
                    fhsEnemyList[fhsEnemy].fire_wait_time_stamp_start = fhsEnemyList[fhsEnemy].fire_wait_time_stamp_end
                    fhsEnemyList[fhsEnemy].add_bullet()
            except:
                pass
            try:
                fhsEnemyList[fhsEnemy].fire(screen)
            except:
                pass
        
        for bullet in range(len(bulletList)):
            for sEnemy in range(len(sEnemyList)):
                try:
                    if bulletList[bullet].rect.colliderect(sEnemyList[sEnemy].rect):
                        bulletList.remove(bulletList[bullet])
                        sEnemyList[sEnemy].HP -= 50
                        if sEnemyList[sEnemy].HP <= 0:
                            sEnemyList.remove(sEnemyList[sEnemy])
                except:
                    pass
            for fhsEnemy in range(len(fhsEnemyList)):
                try:
                    if bulletList[bullet].rect.colliderect(fhsEnemyList[fhsEnemy].rect):
                        bulletList.remove(bulletList[bullet])
                        fhsEnemyList[fhsEnemy].HP -= 50
                        if fhsEnemyList[fhsEnemy].HP <= 0: 
                            fhsEnemyList.remove(fhsEnemyList[fhsEnemy])
                except:
                    pass
        
        for sEnemy in range(len(sEnemyList)):
            try:
                if hero.rect.colliderect(sEnemyList[sEnemy].rect):
                    hero.HP -= sEnemyList[sEnemy].HP
                    sEnemyList.remove(sEnemyList[sEnemy])
                for i in range(len(sEnemyList[sEnemy].bullet_list)):
                    if hero.rect.colliderect(sEnemyList[sEnemy].bullet_list[i]):
                        hero.HP -= sEnemyList[sEnemy].bullet_list[i].AttackValue
                        sEnemyList[sEnemy].bullet_list.remove(sEnemyList[sEnemy].bullet_list[i])
            except:
                pass
        
        for fhsEnemy in range(len(fhsEnemyList)):
            try:
                if hero.rect.colliderect(fhsEnemyList[fhsEnemy].rect):
                    hero.HP -= fhsEnemyList[fhsEnemy].HP
                    fhsEnemyList.remove(fhsEnemyList[fhsEnemy])
                for i in range(len(fhsEnemyList[fhsEnemy].bullet_list)):
                    if hero.rect.colliderect(fhsEnemyList[fhsEnemy].bullet_list[i]):
                        hero.HP -= fhsEnemyList[fhsEnemy].bullet_list[i].AttackValue
                        fhsEnemyList[fhsEnemy].bullet_list.remove(fhsEnemyList[fhsEnemy].bullet_list[i])
            except:
                pass
        
        if part4_sEnemy == 0 and part4_fhsEnemy == 0:
            part4_sEnemy = -10
            part4_fhsEnemy = -10
            levelBoss4 = LevelBoss4()
        
        if part4_sEnemy == -10 and part4_fhsEnemy == -10:
            levelBoss4.move()
            levelBoss4.show(screen)
            levelBoss4.fire(screen)
            if LevelBoss4_fire_wait_time_stamp_end - LevelBoss4_fire_wait_time_stamp_start > 1:
                LevelBoss4_fire_wait_time_stamp_start = LevelBoss4_fire_wait_time_stamp_end
                levelBoss4.add_bullet()
            if hero.rect.colliderect(levelBoss4.rect):
                pygame.mouse.set_pos((pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]+150))
                hero.HP -= 50
            for i in range(len(levelBoss4.bullet_list)):
                try:
                    if hero.rect.colliderect(levelBoss4.bullet_list[i]):
                        hero.HP -= levelBoss4.bullet_list[i].AttackValue
                        levelBoss4.bullet_list.remove(levelBoss4.bullet_list[i])
                except:
                    pass
            for bullet in range(len(bulletList)):
                try:
                    if bulletList[bullet].rect.colliderect(levelBoss4.rect):
                        levelBoss4.HP -= bulletList[bullet].AttackValue
                        bulletList.remove(bulletList[bullet])
                        if levelBoss4.HP <= 0:
                            levelbuttonList[int(part)] = Levelbutton(250,50)
                            part = '选关'
                except:
                    pass
        
        if hero.HP <= 0:
            part = '主页'
        pygame.time.Clock().tick(400)
        pygame.display.update()
    
    if part == '5':
        hero.HP = 1000
        part5_lEnemy = 25
        bulletList = [Bullet()]
        lEnemyList = [LineEnemy()]
        bullet_wait_time_stamp_start = time()
        lEnemy_wait_time_stamp_start = time()
        LevelBoss5_fire_wait_time_stamp_start = time()
    
    while part == '5':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                hero.move(event.pos)
        pygame.mouse.set_visible(False)
        bullet_wait_time_stamp_end = time()
        lineEnemy_wait_time_stamp_end = time()
        LevelBoss5_fire_wait_time_stamp_end = time()
        screen.fill((0,0,0))
        hero.show(screen)
        
        for bullet in range(len(bulletList)):
            try:
                bulletList[bullet].show(screen)
                bulletList[bullet].move()
                if bulletList[bullet].rect.y <= -10:
                    bulletList.remove(bulletList[bullet])
            except:
                pass
        
        if bullet_wait_time_stamp_end - bullet_wait_time_stamp_start > 0.3:
            bullet_wait_time_stamp_start = bullet_wait_time_stamp_end
            bulletList.append(Bullet())
            sound.play()
        
        if lineEnemy_wait_time_stamp_end - lEnemy_wait_time_stamp_start > 2 and part5_lEnemy > 0:
            lEnemy_wait_time_stamp_start = lineEnemy_wait_time_stamp_end
            lEnemyList.append(LineEnemy())
            part5_lEnemy -= 1
        
        for lEnemy in range(len(lEnemyList)):
            try:
                lEnemyList[lEnemy].show(screen)
                lEnemyList[lEnemy].move(hero)
                lEnemyList[lEnemy].fire_wait_time_stamp_end = time()
                if lEnemyList[lEnemy].fire_wait_time_stamp_end - lEnemyList[lEnemy].fire_wait_time_stamp_start > 1.2:
                    lEnemyList[lEnemy].fire_wait_time_stamp_start = lEnemyList[lEnemy].fire_wait_time_stamp_end
                    lEnemyList[lEnemy].add_bullet()
            except:
                pass
            try:
                lEnemyList[lEnemy].fire(screen)
            except:
                pass
        
        for bullet in range(len(bulletList)):
            for lEnemy in range(len(lEnemyList)):
                try:
                    if bulletList[bullet].rect.colliderect(lEnemyList[lEnemy].rect):
                        bulletList.remove(bulletList[bullet])
                        lEnemyList[lEnemy].HP -= 50
                        if lEnemyList[lEnemy].HP <= 0: 
                            lEnemyList.remove(lEnemyList[lEnemy])
                except:
                    pass
        
        for lEnemy in range(len(lEnemyList)):
            try:
                if hero.rect.colliderect(lEnemyList[lEnemy].rect):
                    hero.HP -= lEnemyList[lEnemy].HP
                    lEnemyList.remove(lEnemyList[lEnemy])
                for i in range(len(lEnemyList[lEnemy].bullet_list)):
                    if hero.rect.colliderect(lEnemyList[lEnemy].bullet_list[i]):
                        hero.HP -= lEnemyList[lEnemy].bullet_list[i].AttackValue
                        lEnemyList[lEnemy].bullet_list.remove(lEnemyList[lEnemy].bullet_list[i])
            except:
                pass
        
        if part5_lEnemy == 0:
            part5_lEnemy = -10
            levelBoss5 = LevelBoss5()
        
        if part5_lEnemy == -10:
            levelBoss5.move()
            levelBoss5.show(screen)
            levelBoss5.fire(screen)
            if LevelBoss5_fire_wait_time_stamp_end - LevelBoss5_fire_wait_time_stamp_start > 1:
                LevelBoss5_fire_wait_time_stamp_start = LevelBoss5_fire_wait_time_stamp_end
                levelBoss5.add_bullet()
            if hero.rect.colliderect(levelBoss5.rect):
                pygame.mouse.set_pos((pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]+150))
                hero.HP -= 50
            for i in range(len(levelBoss5.bullet_list)):
                try:
                    if hero.rect.colliderect(levelBoss5.bullet_list[i]):
                        hero.HP -= levelBoss5.bullet_list[i].AttackValue
                        levelBoss5.bullet_list.remove(levelBoss5.bullet_list[i])
                except:
                    pass
            for bullet in range(len(bulletList)):
                try:
                    if bulletList[bullet].rect.colliderect(levelBoss5.rect):
                        levelBoss5.HP -= bulletList[bullet].AttackValue
                        bulletList.remove(bulletList[bullet])
                        if levelBoss5.HP <= 0:
                            levelbuttonList[int(part)] = Levelbutton(310,50)
                            part = '选关'
                except:
                    pass
        
        if hero.HP <= 0:
            part = '主页'
        pygame.time.Clock().tick(400)
        pygame.display.update()
    
    try:
        exec('''
while int(part) > 4:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mPos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if MineInitialSetting.collide_mouse('PyBox\image\startgame.png',mPos,425,151):
                part = '选关'
    pygame.mouse.set_visible(True)
    PartSetScreenFillTimeStamp0 = time()
    if (int(PartSetScreenFillTimeStamp0) % 6 == 0) or (int(PartSetScreenFillTimeStamp0) % 6 == 1):
        screen.fill((68,185,211))
    if (int(PartSetScreenFillTimeStamp0) % 6 == 2) or (int(PartSetScreenFillTimeStamp0) % 6 == 3):
        screen.fill((255,223,48))
    if (int(PartSetScreenFillTimeStamp0) % 6 == 4) or (int(PartSetScreenFillTimeStamp0) % 6 == 5):
        screen.fill((14,225,37))
    MineInitialSetting.text(size=41,body='作者未更新，点击start返回',color=(125,2,120),pos=(252,35))
    MineInitialSetting.show_img(name='PyBox\image\startgame.png',pos=(425,151))
    pygame.time.Clock().tick(100)
    pygame.display.update()
        ''')
    except:
        continue
    
    