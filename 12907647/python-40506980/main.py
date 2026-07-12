import pygame
import sys
import data
pygame.init()

screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('python跑酷')

try:import ntpath
except:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)")
else:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)")
finally:pass

ld = []
lines = data.col
level = 1   # 分两个变量，程序会更快
levelindex = level - 1

class Block:
    def __init__(self,kind,x,y):
        self.kind = data.kinddict[kind][0]
        self.color = data.kinddict[kind][1]
        self.size = 40
        self.rect = pygame.Rect(x*self.size,y*self.size,self.size,self.size)
    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect,0)

class Player:
    def __init__(self):
        self.rect = pygame.Rect(0,0,30,30)
        self.xm = 0
        self.ym = 0
        self.life = 2023666
        self.addtoX = 0
        self.addtoY = 0
        self.addtoaddtoY = 0
    def collide(self,other):
        if self.rect.colliderect(other.rect):
            if other.rect.top < self.rect.top < other.rect.bottom < self.rect.bottom:
                return 'under'
            elif self.rect.top < other.rect.top < self.rect.bottom < other.rect.bottom:
                return 'on'
            elif self.rect.left < other.rect.left < self.rect.right < other.rect.right:
                return 'left'
            elif other.rect.left < self.rect.left < other.rect.right < self.rect.right:
                return 'right'
            else:
                return 'in'
        return False
    def addtoXY(self):
        if player.xm == 1:
            self.addtoX += 1.2
        elif player.xm == -1:
            self.addtoX -= 1.2
        if player.ym == 1:
            self.addtoY = 0
        elif player.ym == -1:
            self.addtoY -= 10
    def minustoXY(self):
        self.addtoX *= 0.9
        self.addtoaddtoY *= 0.98
        self.addtoY *= self.addtoaddtoY
        if abs(self.addtoX) < 0.1:
            self.addtoX = 0
        if abs(self.addtoY) < 0.1:
            self.addtoY = 0
        if self.addtoaddtoY < 0.2:
            self.addtoaddtoY = 0
    def move(self):
        self.rect.x += round(self.addtoX)
        self.rect.y += round(self.addtoY)
    def setrange(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1000:
            self.rect.right = 1000
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.x = 0
            self.rect.y = 0
            self.life -= 20
    def draw(self):
        pygame.draw.rect(screen,(255,238,111),self.rect,0)

for i in data.leveldata:
    tmpld = []
    for j in range(len(i)):
        if i[j]:
            tmpld.append(Block(i[j],j%lines,j//lines))
    ld.append(tmpld)

player = Player()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.xm = 1
            if event.key == pygame.K_LEFT:
                player.xm = -1
            # if event.key == pygame.K_DOWN:
            #     player.ym = 1
            if event.key == pygame.K_UP:
                if not player.addtoY:
                    player.addtoaddtoY = 0.8
                    player.ym = -1
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT,pygame.K_RIGHT):
                player.xm = 0
            if event.key in (pygame.K_UP,pygame.K_DOWN):
                player.ym = 0
    screen.fill((238,255,255))
    player.draw()
    player.addtoXY()
    player.minustoXY()
    player.move()
    player.setrange()
    player.rect.y += 10   # 自然下落
    for i in ld[levelindex]:
        i.draw()
        isc = player.collide(i)
        if i.kind == 'normal':
            while isc:
                isc = player.collide(i)
                if isc == 'under':
                    player.rect.y += 10
                elif isc == 'left':
                    player.addtoX -= 2   # 左侧就向左上弹开，并获得连跳机会
                    player.addtoY = 0
                    player.addtoaddtoY += 0.013
                elif isc == 'right':
                    player.addtoX += 2   # 右侧就向右上弹开，并获得连跳机会
                    player.addtoY = 0
                    player.addtoaddtoY += 0.013
                player.rect.y -= 1   # 进入地就上升
        elif i.kind == 'die':
            if isc:
                player.rect.x = 0
                player.rect.y = 0
                player.life -= 10
                break
        elif i.kind == 'jump':
            if isc:
                player.ym = -1
                player.addtoaddtoY = 0.9
        else:     # win
            if isc:
                levelindex += 1
                level += 1
                if levelindex == len(ld):
                    print('恭喜你过关了,剩余血量为',player.life)
                    pygame.quit()
                    sys.exit()
                player.rect.x = 0
                player.rect.y = 0
    show_text('level:'+str(level),pos=(3,3))
    show_text('life:'+str(player.life),pos=(3,33))
    if level == 1:
        show_text('这是C站第一个成熟的python仿照scratch跑酷',pos=(3,63))
        show_text('左上角是你的等级和生命',pos=(3,93))
        show_text('游戏目前有4中砖块：普通、红色、绿色、蓝色',pos=(3,123))
        show_text('分别代表地、岩浆（会shi掉）、跳板（顾名思义）、传送门（通关）',pos=(3,153),color=(255,238,111))
        show_text('碰到岩浆，血量扣10；摔到最下端，血量扣20.关卡数据在data.py里面',pos=(3,183),color=(255,238,111))
        show_text('由于pygame没有颜色检测，所以不能踩字，但是可以爬墙',pos=(3,213),color=(255,238,111))
        show_text('制作不难(yi)，但是调整加速度花了我好久。我y轴还做了加速度的加速度',pos=(3,243),color=(255,238,111))
        show_text('本来是给袁梓轩看的模板。。。喜欢的一键三连！',pos=(3,273),color=(255,238,111))
    if player.life <= 0:
        print('恭喜你逝世了')
        pygame.quit()
        sys.exit()
    pygame.display.update()
    clock.tick(70)  # 限制帧率