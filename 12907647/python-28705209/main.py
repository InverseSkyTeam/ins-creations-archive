'''
V1.3相对V1.1增加如下体验
1.整体优化
2.优化代码
3.增加板块
4.增加镐子种类

预告：增加音效；
增加板块、镐子；
增加返回地面按钮；
跳转深度按钮；
路程；
与终点的路线绘制；
更精准的数据；
背景图片的移动；
设置；
帮助；
小地图
其他功能继续期待...

小攻略：鼠标移到小人下方，滚轮开始乡下滚动。wc!突然镐子变成了割草机
'''
# 小轩智造
# 导库以及初始化
import pygame,sys,random
pygame.init()

screen = pygame.display.set_mode((800,900))
pygame.display.set_caption("小轩-地心游记")

player = pygame.image.load('image/player/玩家.png')
bg = pygame.image.load('image/bg/背景.png') # 冷笑话：bg，英语background 或 拼音bei'jing，都是背景的意思:)
pa = [pygame.image.load('image/pickaxe/普通镐.png'),
pygame.image.load('image/pickaxe/木镐.png'),
pygame.image.load('image/pickaxe/铁镐.png'),
pygame.image.load('image/pickaxe/高级铁镐.png'),
pygame.image.load('image/pickaxe/金镐.png'),
pygame.image.load('image/pickaxe/紫镐.png'),
pygame.image.load('image/pickaxe/翡翠镐.png'),]
shop_attack = pygame.image.load('image/button/shop.png')
shop = shop_attack.convert()
shop.set_alpha(128)
new_shop = shop
shop_buy = pygame.image.load('image/button/buy.png')
shopbg = pygame.image.load('image/bg/商店背景.png')
s_none = pygame.image.load('image/stone/空.png')
s_basis = pygame.image.load('image/stone/基本.png')
s_grass = pygame.image.load('image/stone/草坪.png')
s_soil = pygame.image.load('image/stone/泥土.png')
s_soil_g = pygame.image.load('image/stone/高级泥土.png') # g是good产品，此处就不弄well了
so_tin = pygame.image.load('image/stone/锡矿.png')
so_booze = pygame.image.load('image/stone/铅矿.png')
so_lron = pygame.image.load('image/stone/铁矿.png')
so_sil = pygame.image.load('image/stone/银矿.png')
so_gold = pygame.image.load('image/stone/金矿.png')
so_gold_g = pygame.image.load('image/stone/好金矿.png')
so_purple = pygame.image.load('image/stone/紫檀矿.png')
so_ppr = pygame.image.load('image/stone/紫檀玉矿.png')
so_green = pygame.image.load('image/stone/绿宝石矿.png')
so_green_g = pygame.image.load('image/stone/翡翠矿.png')
so_white = pygame.image.load('image/stone/象牙白矿.png')
hero = player.get_rect()
hero.bottomleft = (380,351)
hero_figure = pygame.Rect(0,0,35,49)
hero_figure.bottomleft = (385,351)
shop_rect = new_shop.get_rect()
shop_rect.bottomleft = (15,885)
shop_buy_rect = shop_buy.get_rect()
shop_buy_rect.topleft = (338,693)

class Stone(object):
    def __init__(self,img,hp,_class):
        self.img = img
        self.rect = self.img.get_rect()
        self.HP = hp
        self.cls = _class

StoneList = [[Stone(s_grass,2,'草坪') for i in range(7)]+[Stone(s_basis,1,'基本'),Stone(s_basis,1,'基本')]+[Stone(s_grass,2,'草坪') for i in range(7)]]+\
[[Stone(s_soil,3,'泥土') for i in range(16)] for i in range(8)]+\
[[Stone(s_soil_g,5,'高级泥土') for i in range(16)] for i in range(15)]+\
[[Stone(so_tin,10,'锡矿') for i in range(16)] for i in range(20)]+\
[[Stone(so_booze,20,'铅矿') for i in range(16)] for i in range(30)]+\
[[Stone(so_lron,30,'铁矿') for i in range(16)] for i in range(10)]+\
[[Stone(so_sil,40,'银矿') for i in range(16)] for i in range(10)]+\
[[Stone(so_gold_g,60,'好金矿') if random.randint(1,4)==1 else Stone(so_gold,55,'金矿') for i in range(16)] for i in range(20)]+\
[[Stone(so_ppr,120,'紫檀玉矿') if random.randint(1,5)==1 else Stone(so_purple,100,'紫檀矿') for i in range(16)] for i in range(30)]+\
[[Stone(so_green_g,200,'翡翠矿') if random.randint(1,8)==1 else Stone(so_green,170,'绿宝石矿') for i in range(16)] for i in range(60)]+\
[[Stone(so_white,600,'象牙白矿') if random.randint(1,10)==1 else Stone(so_green_g,200,'翡翠矿') for i in range(16)] for i in range(80)]

for i in range(len(StoneList)):
    for j in range(len(StoneList[i])):
        StoneList[i][j].rect.x = j*50
        StoneList[i][j].rect.y = i*50+350

try:import ntpath      #文字处理系统
except:font = pygame.font.SysFont('kaittf', 30)
else:font = pygame.font.SysFont('kaiti', 30);del ntpath
def show_text(text,color=(0,0,0),pos=(0,0)):
    screen.blit(font.render((text),True,color),pos)

Y = 0
eventpos = (0,0)
pa_index = 0
pickaxe = pa[pa_index]
parect = pickaxe.get_rect()
move = False
move_up = False
hero_move = False
shop_is_attack = False
jump_pressure = 50
pa_speed = 1
money = 0

# 隐藏窗口内鼠标
pygame.mouse.set_visible(False)



# 超级主循环
while True:
    for event in pygame.event.get(): # 检测系统
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            eventpos = event.pos
            parect.center = eventpos
            if shop_rect.collidepoint(eventpos):
                new_shop = shop_attack
            else:
                new_shop = shop
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(StoneList)):
                for j in range(len(StoneList[i])):
                    if StoneList[i][j].rect.collidepoint(event.pos) and StoneList[i][j].cls != '啥也不是嘞' and StoneList[i][j].cls != '基本':
                        StoneList[i][j].HP -= pa_speed
                        if StoneList[i][j].HP <= 0:
                            if StoneList[i][j].cls == '泥土':
                                money += 1
                            if StoneList[i][j].cls == '高级泥土':
                                money += 2
                            if StoneList[i][j].cls == '锡矿':
                                money += 5
                            if StoneList[i][j].cls == '铅矿':
                                money += 7
                            if StoneList[i][j].cls == '铁矿':
                                money += 10
                            if StoneList[i][j].cls == '银矿':
                                money += 15
                            if StoneList[i][j].cls == '金矿':
                                money += 20
                            if StoneList[i][j].cls == '好金矿':
                                money += 25
                            if StoneList[i][j].cls == '紫檀矿':
                                money += 40
                            if StoneList[i][j].cls == '紫檀玉矿':
                                money += 50
                            if StoneList[i][j].cls == '绿宝石矿':
                                money += 80
                            if StoneList[i][j].cls == '翡翠矿':
                                money += 130
                            if StoneList[i][j].cls == '象牙白矿':
                                money += 500
                            StoneList[i][j].img = s_none
                            StoneList[i][j].cls = '啥也不是嘞'
            if shop_is_attack == True and shop_buy_rect.collidepoint(event.pos):
                shop_is_attack = False
                if pa_index == 0 and money >= 10:
                    money -= 10
                    pa_speed = 2
                    pa_index += 1
                    pickaxe = pa[pa_index]
                    parect = pickaxe.get_rect()
                elif pa_index == 1 and money >= 60:
                    money -= 60
                    pa_speed = 5
                    pa_index += 1
                    pickaxe = pa[pa_index]
                    parect = pickaxe.get_rect()
                elif pa_index == 2 and money >= 150:
                    money -= 150
                    pa_speed = 10
                    pa_index += 1
                    pickaxe = pa[pa_index]
                    parect = pickaxe.get_rect()
                elif pa_index == 3 and money >= 320:
                    money -= 320
                    pa_speed = 20
                    pa_index += 1
                    pickaxe = pa[pa_index]
                    parect = pickaxe.get_rect()
                elif pa_index == 4 and money >= 750:
                    money -= 750
                    pa_speed = 50
                    pa_index += 1
                    pickaxe = pa[pa_index]
                    parect = pickaxe.get_rect()
                elif pa_index == 5 and money >= 7000:
                    money -= 7000
                    pa_speed = 150
                    pa_index += 1
                    pickaxe = pa[pa_index]
                    parect = pickaxe.get_rect()
            if shop_rect.collidepoint(eventpos):
                shop_is_attack = True
            else:
                shop_is_attack = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero_move = 'left'
            if event.key == pygame.K_RIGHT:
                hero_move = 'right'
            if event.key == pygame.K_SPACE:
                hero_move = 'jump'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                hero_move = False
    
    # 屏幕铺垫
    screen.fill((255,255,255))
    screen.blit(bg,(0,0))
    move = False
    
    # 判断是否可以下落
    for i in range(len(StoneList)):
        for j in range(len(StoneList[i])):
            screen.blit(StoneList[i][j].img,StoneList[i][j].rect)
            try:
                if hero_figure.colliderect(StoneList[i][j].rect) and StoneList[i][j].cls == '啥也不是嘞' and (not hero_figure.colliderect(StoneList[i][j-1].rect) or StoneList[i][j-1].cls == '啥也不是嘞') and (not hero_figure.colliderect(StoneList[i][j+1].rect) or StoneList[i][j+1].cls == '啥也不是嘞') and j>0:
                    try:
                        if (not hero_figure.colliderect(StoneList[i+1][j].rect)) or StoneList[i+1][j].cls == '啥也不是嘞':
                            move = True
                    except:
                        if (not hero_figure.colliderect(StoneList[0][j].rect)) or StoneList[0][j].cls == '啥也不是嘞':
                            move = True
            except:
                pass
            StoneList[i][j].rect.y = i*50+350+Y
    
    # 屏幕移动
    if move_up == True:
        move = False
        Y += 3
        jump_pressure -= 3
        if jump_pressure <= 0:
            if Y <= -97:
                jump_pressure = 120
            if Y <= -47 and Y > -97:
                jump_pressure = 80
            if Y > -47:
                jump_pressure = 50
            move_up = False
    if move == True:
        if Y >= -2000:
            Y -= 2
        else:
            Y -= 4
    if move == False:
        if hero_move == 'left':
            if hero.left >= 0:
                hero.x -= 3
                hero_figure.x -= 3
        if hero_move == 'right':
            if hero.right <= 800:
                hero.x += 3
                hero_figure.x += 3
        if hero_move == 'jump':
            if Y < -50:
                move_up = True
        
    screen.blit(player,hero)
    if shop_is_attack == False: # 商城代码
        screen.blit(new_shop,shop_rect)
    else:
        screen.blit(shopbg,(150,150))
        try:
            screen.blit(pa[pa_index+1],(380,440))
        except:
            pass
        if pa_index == 0:
            show_text('10￥',color=(0,0,0),pos=(295,625))
        if pa_index == 1:
            show_text('60￥',color=(0,0,0),pos=(295,625))
        if pa_index == 2:
            show_text('150￥',color=(0,0,0),pos=(295,625))
        if pa_index == 3:
            show_text('320￥',color=(0,0,0),pos=(295,625))
        if pa_index == 4:
            show_text('750￥',color=(0,0,0),pos=(295,625))
        if pa_index == 5:
            show_text('7k￥',color=(0,0,0),pos=(295,625))
        screen.blit(shop_buy,shop_buy_rect)
    if money < 1000:
        show_text('￥:'+str(money),color=(0,0,0),pos=(11,11))
    else:
        show_text('￥:'+str(round(money/1000,2))+'k',color=(0,0,0),pos=(11,11))
    show_text(str(Y//20)+'m',color=(0,0,0),pos=(709,11))
    
    # 镐子鼠标，必须置顶
    screen.blit(pickaxe,parect)
    
    # 刷新
    pygame.display.update()