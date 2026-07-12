# 小轩智造
# 导库以及初始化
import pygame,sys,random
pygame.init()

screen = pygame.display.set_mode((800,900))
pygame.display.set_caption("地心游记")

player = pygame.image.load('image/player/玩家.png')
bg = pygame.image.load('image/bg/背景.png') # 冷笑话：bg，英语background 或 拼音bei'jing，都是背景的意思:)
pa = [pygame.image.load('image/pickaxe/普通镐.png'),
pygame.image.load('image/pickaxe/木镐.png')]
shop_attack = pygame.image.load('image/button/shop.png')
shop = shop_attack.convert()
shop.set_alpha(128)
new_shop = shop
s_none = pygame.image.load('image/stone/空.png')
s_basis = pygame.image.load('image/stone/基本.png')
s_grass = pygame.image.load('image/stone/草坪.png')
s_soil = pygame.image.load('image/stone/泥土.png')
s_soil_g = pygame.image.load('image/stone/高级泥土.png') # g是good产品，此处就不弄well了
so_tin = pygame.image.load('image/stone/锡矿.png')
hero = player.get_rect()
hero.bottomleft = (380,351)
hero_figure = pygame.Rect(0,0,35,49)
hero_figure.bottomleft = (385,351)
shop_rect = new_shop.get_rect()
shop_rect.bottomleft = (15,885)

class Stone(object):
    def __init__(self,img,hp,_class):
        self.img = img
        self.rect = self.img.get_rect()
        self.HP = hp
        self.cls = _class

StoneList = [[Stone(s_grass,2,'草坪') for i in range(7)]+[Stone(s_basis,1,'基本'),Stone(s_basis,1,'基本')]+[Stone(s_grass,2,'草坪') for i in range(7)]]+\
[[Stone(s_soil,3,'泥土') for i in range(16)] for i in range(8)]+\
[[Stone(s_soil_g,5,'高级泥土') for i in range(16)] for i in range(15)]+\
[[Stone(so_tin,10,'锡矿') for i in range(16)] for i in range(20)]

for i in range(len(StoneList)):
    for j in range(len(StoneList[i])):
        StoneList[i][j].rect.x = j*50
        StoneList[i][j].rect.y = i*50+350

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
                            print(money)
                            StoneList[i][j].img = s_none
                            StoneList[i][j].cls = '啥也不是嘞'
            if shop_rect.collidepoint(eventpos):
                shop_is_attack = True
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
    if move == True:Y -= 2
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
    screen.blit(new_shop,shop_rect)
    screen.blit(pickaxe,parect)
    
    #刷新
    pygame.display.update()