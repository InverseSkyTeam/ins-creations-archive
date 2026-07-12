import pygame,sys,random
pygame.init()

screen = pygame.display.set_mode((900,650))
pygame.display.set_caption('[小游戏-羊了个羊] 逆天团队-小轩')

# 加载图片
bgpic = pygame.transform.scale(pygame.image.load(r'./tree/images/background.png'),(900,650))
groove = pygame.image.load(r'./tree/images/groove.png')  # 370x65
titlepic = pygame.image.load(r'./tree/images/羊题.png')

class Block:
    def __init__(self,picid,x,y,surfacenum):
        self.n = picid
        self.tp = 'outside'
        self.img = pygame.transform.scale(pygame.image.load(r'./tree/images/'+str(picid)+'.png'),(50,55)).convert()
        self.rect = pygame.Rect(x,y,50,55)
        self.sur = pygame.Surface((50,55))
        self.sur.fill((0,0,0))
        self.s = surfacenum
    def draw(self):
        screen.blit(self.img,self.rect)
        screen.blit(self.sur,self.rect)

class LevelButton:
    def __init__(self,level):
        self.level = level
        self.y = random.randint(11,560)
        self.setm(1)
    def __int__(self):
        return self.level
    def setm(self,l):
        if self.level < l:
            self.img = pygame.image.load(r'./tree/images/已通过.png')
            self.rect = self.img.get_rect()
        elif self.level == l:
            self.img = pygame.image.load(r'./tree/images/未通过.png')
            self.rect = self.img.get_rect()
        else:
            self.img = pygame.image.load(r'./tree/images/锁定关.png')
            self.rect = self.img.get_rect()
        self.rect.topleft = (self.level*70,self.y)
    def draw(self):
        screen.blit(self.img,self.rect)

def is_on(t1,t2,t3,d):     # 下面是否有位置相同且没有铺垫看不见的块
    on = 0
    for i in d:
        if i[0]%2 == t1%2 and i[1] == t2 and i[2] == t3 and i[0] > t1:   # 压在下面并且位置相同
            on = i[0]
            break
    if not on:
        return False
    for i in d:
        if i[0]%2 != t1%2 and i[1] == t2 and i[2] == t3 and on > i[0]:   # 已经有铺垫
            return False
    return True

# 初始化工作
# blocks = 192
# blocksave = 11
# blockadds = 0
# surfaces = 9
# surfacew = 12
# surfaceh = 8

try:import ntpath
except:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)")
else:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)")
finally:pass

# pygame.mixer.init()
pygame.mixer.music.load(r'./tree/musics/bgm.ogg')
pygame.mixer.music.play(-1)
clicksound = pygame.mixer.Sound(r'./tree/musics/pop.wav')

part = '主页'
level = 1
lblist = [LevelButton(i) for i in range(1,11)]



while True:
    while part == '主页':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                part = '选关'
        screen.fill((0,255,0))
        screen.blit(bgpic,(0,0))
        screen.blit(titlepic,(11,11))
        show_text('逆天团队-小轩',color=(0,0,255),pos=(450,30),size=65)
        show_text('Version1.1',color=(255,0,0),pos=(400,120),size=20)
        show_text('空格开始',pos=(250,300),size=100)
        pygame.display.update()
    
    while part == '选关':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in lblist:
                        if i.rect.collidepoint(event.pos) and int(i)<=level:
                            part = int(i)
            
        screen.fill((0,255,0))
        screen.blit(bgpic,(0,0))
        for i in lblist:
            i.setm(level)
            i.draw()
            show_text(str(int(i)),pos=(i.rect.centerx-10,i.rect.centery),size=20)
        pygame.display.update()
    
    if part == 1:
        blocks = 12
        blocksave = 3
        surfaces = 3
        surfacew = 5
        surfaceh = 5
        part = '闯关'
    elif part == 2:
        blocks = 45
        blocksave = 6
        surfaces = 6
        surfacew = 10
        surfaceh = 6
        part = '闯关'
    elif part == 3:
        blocks = 60
        blocksave = 8
        surfaces = 7
        surfacew = 12
        surfaceh = 7
        part = '闯关'
    elif part == 4:
        blocks = 87
        blocksave = 10
        surfaces = 9
        surfacew = 12
        surfaceh = 8
        part = '闯关'
    elif part == 5:
        blocks = 96
        blocksave = 11
        surfaces = 9
        surfacew = 12
        surfaceh = 8
        part = '闯关'
    elif part == 6:
        blocks = 114
        blocksave = 12
        surfaces = 8
        surfacew = 12
        surfaceh = 8
        part = '闯关'
    elif part == 7:
        blocks = 123
        blocksave = 12
        surfaces = 9
        surfacew = 10
        surfaceh = 7
        part = '闯关'
    elif part == 8:
        blocks = 144
        blocksave = 12
        surfaces = 8
        surfacew = 8
        surfaceh = 8
        part = '闯关'
    elif part == 9:
        blocks = 171
        blocksave = 12
        surfaces = 11
        surfacew = 8
        surfaceh = 7
        part = '闯关'
    elif part == 10:
        blocks = 231
        blocksave = 12
        surfaces = 20
        surfacew = 8
        surfaceh = 6
        part = '闯关'
        
    if part == '闯关':     # 初始化工作
        data = []        # 三维列表降到一维列表，Block参数增多，O(n^6)降到O(n*surfaces)=O(n)
        groovedata = []
        tmp1 = 1
        tmp2 = tmp3 = 0
        tmpl = []
        tmp = random.randint(1,blocksave)
        blockadds = 0
        
        while blocks:      # 布置方块
            while (tmp1,tmp2,tmp3) in tmpl or is_on(tmp1,tmp2,tmp3,tmpl):
                tmp1 = random.randint(1,surfaces)
                tmp2 = random.randint(0,surfaceh-1)
                tmp3 = random.randint(0,surfacew-1)
            tmpl.append((tmp1,tmp2,tmp3))
            if tmp1 % 2 == 1:
                data.append(Block(tmp,(900-surfacew*50)/2+tmp3*50,60+tmp2*55,tmp1))
            else:
                data.append(Block(tmp,(900-surfacew*50)/2+15+tmp3*50,87+tmp2*55,tmp1))
            blocks -= 1
            blockadds += 1
            if blockadds == 3:
                blockadds = 0
                tmp = random.randint(1,blocksave)
        
        for block in data:
            block.sur.set_alpha(0)
            block.tp = 'outside'
            for other in data:
                if block.rect.colliderect(other.rect) and block.s > other.s:
                    block.sur.set_alpha(125)
                    block.tp = 'inside'
                    break
    
    while part == '闯关':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for block in range(len(data)):
                    if data[block].rect.collidepoint(event.pos) and data[block].tp == 'outside':
                        groovedata.append(data[block])
                        clicksound.play()
                        del data[block]
                        break
                for block in data:
                    block.sur.set_alpha(0)
                    block.tp = 'outside'
                    for other in data:
                        if block.rect.colliderect(other.rect) and block.s > other.s:
                            block.sur.set_alpha(125)
                            block.tp = 'inside'
                            break
                            
        screen.fill((0,255,0))
        screen.blit(bgpic,(0,0))
        screen.blit(groove,(265,550))
        show_text('剩余'+str(len(data))+' 羊了个羊')
        
        for i in range(surfaces,0,-1):
            for block in data:
                if block.s == i:
                    block.draw()
        grooveblocknumlist = [0 for i in range(12)]   # 算法:桶计数
        
        for block in range(len(groovedata)):
            groovedata[block].rect.topleft = (275+50*block,555)     # x=265+10+50*位置
            grooveblocknumlist[groovedata[block].n-1] += 1
            if grooveblocknumlist[groovedata[block].n-1] > 2:
                newgroovedata = []
                for i in groovedata:
                    if i.n != groovedata[block].n:
                        newgroovedata.append(i)
                groovedata = newgroovedata
                break
            groovedata[block].draw()
        
        if not len(data):     # 赢了：列表为空，所以清除掉了
            print('你把羊吃了，你赢了')
            # pygame.quit()
            # sys.exit()
            level += 1
            part = '选关'
        if len(groovedata) > 6:      # 输掉
            print('你被羊吃了，你输了')
            # pygame.quit()
            # sys.exit()
            part = '选关'
        
        pygame.display.update()