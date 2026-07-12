import pygame
import sys

pygame.init()
pygame.key.stop_text_input()

# 定义常量(用户可以修改设置)
SC_WIDTH = 1000
SC_HEIGHT = 700
BLOCK_SIZE = 50
DROP_SIZE = 30
MP_WIDTH = 100 * BLOCK_SIZE
MP_HEIGHT = 100 * BLOCK_SIZE
WIDTH = int(SC_WIDTH / BLOCK_SIZE)
HEIGHT = int(SC_HEIGHT / BLOCK_SIZE)

screen = pygame.display.set_mode((SC_WIDTH,SC_HEIGHT))
pygame.display.set_caption('IDU Sandbox Driver')

img = pygame.transform.scale(pygame.image.load('./images/土.png'),(BLOCK_SIZE,BLOCK_SIZE))
data = [
    *([[0,None] for i in range(100)] for line in range(10)),
    *([[2,img] for i in range(100)] for line in range(90)),
]

class Player:
    def __init__(self):
        self.x = SC_WIDTH / 2 - 20
        self.y = SC_HEIGHT / 2 - 60
        self.rect = pygame.Rect(self.x,self.y,40,120)
        self.speed = 3
    def bind(self,map_):
        self.map = map_
    
    def move(self):
        # 读取键盘移动意图
        xoffset = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
        yoffset = keystate[pygame.K_DOWN] - keystate[pygame.K_UP]
        xoffset *= self.speed
        yoffset *= self.speed
        
        # 四种情况详细研究碰撞
        bleft, btop = self.map.convert(1,self.x,self.y)
        bright, bbottom = self.map.convert(1,self.x+self.rect.w-1,self.y+self.rect.h-1)
        if xoffset < 0:    # 左右碰到方块限制
            for row in range(btop,bbottom+1):
                if self.map.data[row][bleft-1][0]:
                    xoffset = -min(-xoffset, self.x - bleft * 50)
                    break
        elif xoffset > 0:
            for row in range(btop,bbottom+1):
                if self.map.data[row][bright+1][0]:
                    xoffset = min(xoffset, bright * 50 + 50 - self.x - self.rect.w)
                    break
        self.x += xoffset    # x移动（提前移动避免出现斜对角卡方块情况）
        self.x = min(max(self.x, 0), MP_WIDTH - 41)
        
        bleft, btop = self.map.convert(1,self.x,self.y)
        bright, bbottom = self.map.convert(1,self.x+self.rect.w-1,self.y+self.rect.h-1)
        if yoffset < 0:    # 上下碰到方块限制
            for col in range(bleft,bright+1):
                if self.map.data[btop-1][col][0]:
                    yoffset = -min(-yoffset, self.y - btop * 50)
                    break
        elif yoffset > 0:
            for col in range(bleft,bright+1):
                if self.map.data[bbottom+1][col][0]:
                    yoffset = min(yoffset, bbottom * 50 + 50 - self.y - self.rect.h)
                    break
        self.y += yoffset      # y移动
        self.y = min(max(self.y, 0), MP_HEIGHT - 121)
        
        # 在地图边缘自移动
        if self.x < SC_WIDTH / 2 - 20:
            self.rect.x = int(self.x)
        elif self.x >= MP_WIDTH - SC_WIDTH / 2 - 20:
            self.rect.x = int(SC_WIDTH-MP_WIDTH+self.x+1)
        if self.y < SC_HEIGHT / 2 - 60:
            self.rect.y = int(self.y)
        elif self.y >= MP_HEIGHT - SC_HEIGHT / 2 - 60:
            self.rect.y = int(SC_HEIGHT-MP_HEIGHT+self.y+1)
    
    def draw(self):
        pygame.draw.rect(screen,(255,0,0),self.rect,3)
    
    @property
    def position(self):
        return [self.x, self.y, self.rect.x, self.rect.y]

class GameMap:
    def __init__(self,data):
        self.__keystate = {
            pygame.K_UP: 0, pygame.K_DOWN: 0, pygame.K_LEFT: 0, pygame.K_RIGHT: 0,
            pygame.K_w: 0, pygame.K_s: 0, pygame.K_a: 0, pygame.K_d: 0,
        }
        self.data = data
        self.highlightrect = pygame.Rect(0,0,50,50)
    def include(self,player):
        self.player = player
    
    def convert(self,tp,x,y,scx=None,scy=None):
        if tp == 1:     # 绝对坐标转绝对方块
            return [int(x // 50), int(y // 50)]
        if tp == 2:     # 绝对方块转绝对坐标
            return [x * 50, y * 50]
        if tp == 3:     # 绝对方块转相对坐标
            return [x * 50 - scx, y * 50 - scy]
    
    def draw(self):
        # 绘制
        px, py, psx, psy = self.player.position
        x = min(max(0, px - psx), MP_WIDTH - SC_WIDTH - 1)
        y = min(max(0, py - psy), MP_HEIGHT - SC_HEIGHT - 1)
        bleft, btop = self.convert(1, x, y)
        bright, bbottom = bleft + WIDTH, btop + HEIGHT
        while btop <= bbottom:
            while bleft <= bright:
                image = self.data[btop][bleft][1]
                if image:
                    screen.blit(image,self.convert(3, bleft, btop, x, y))
                bleft += 1
            bleft = bleft - 1 - WIDTH
            btop += 1
        
        # 高亮
        ex, ey = mousestate['pos']
        if 0 <= ex < SC_WIDTH and 0 <= ey <= SC_HEIGHT:
            highlight_col, highlight_row = self.convert(1, x+ex, y+ey)
            highbid = self.data[highlight_row][highlight_col][0]
            if highbid:
                border = 3
                if mousestate[1]:
                    self.data[highlight_row][highlight_col] = [0,None]
            else:
                border = 1
                if mousestate[3]:
                    self.data[highlight_row][highlight_col] = [2,img]
            self.highlightrect.topleft = self.convert(3, highlight_col, highlight_row, x, y)
            pygame.draw.rect(screen,(0,0,0),self.highlightrect,border,3)



player = Player()
gamemap = GameMap(data)
player.bind(gamemap)
gamemap.include(player)

clock = pygame.time.Clock()

keystate = {
    pygame.K_UP: 0,
    pygame.K_DOWN: 0,
    pygame.K_LEFT: 0,
    pygame.K_RIGHT: 0,
    pygame.K_w: 0,
    pygame.K_s: 0,
    pygame.K_a: 0,
    pygame.K_d: 0,
}
mousestate = {
    'pos': (-1,-1),
    1: 0,
    3: 0,
}



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mousestate['pos'] = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousestate[event.button] = 1
        if event.type == pygame.MOUSEBUTTONUP:
            mousestate[event.button] = 0
        if event.type == pygame.KEYDOWN:
            keystate[event.key] = 1
        if event.type == pygame.KEYUP:
            keystate[event.key] = 0
    
    screen.fill((255,255,255))
    gamemap.draw()
    player.move()
    player.draw()
    pygame.display.update()
    clock.tick(100)