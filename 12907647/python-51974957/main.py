import pygame
import sys

pygame.init()
pygame.key.stop_text_input()

SC_WIDTH = 1000
SC_HEIGHT = 700
BLOCK_SIZE = 50
MP_WIDTH = 100 * BLOCK_SIZE
MP_HEIGHT = 10006 * BLOCK_SIZE
WIDTH = int(SC_WIDTH / BLOCK_SIZE)
HEIGHT = int(SC_HEIGHT / BLOCK_SIZE)

print(f'''[INFO]
窗口大小: {SC_WIDTH}x{SC_HEIGHT}={SC_WIDTH*SC_HEIGHT}px
地图大小: {MP_WIDTH}x{MP_HEIGHT}={MP_WIDTH*MP_HEIGHT}px
地图方块: 100x10006=1000600个
单个方块: 50x50=2500px
wsad/up down left right移动
(fps/xpos/ypos在窗口标题显示)
Version dev-1''')

screen = pygame.display.set_mode((SC_WIDTH,SC_HEIGHT))
pygame.display.set_caption('IDU Sandbox Driver')

images = {
    0: None,
    2: pygame.transform.scale(pygame.image.load('./images/土.png'),(BLOCK_SIZE,BLOCK_SIZE)),
    1: pygame.transform.scale(pygame.image.load('./images/草地.png'),(BLOCK_SIZE,BLOCK_SIZE)),
}
data = [*([0 for i in range(100)] for line in range(5)),
        [1 for i in range(100)],
        *([2 for i in range(100)] for line in range(10000)),]

class GameMap:
    def __init__(self,data):
        self.__state = 'unclick'
        self.__keystate = {
            pygame.K_UP: 0,
            pygame.K_DOWN: 0,
            pygame.K_LEFT: 0,
            pygame.K_RIGHT: 0,
            pygame.K_w: 0,
            pygame.K_s: 0,
            pygame.K_a: 0,
            pygame.K_d: 0,
        }
        self.data = data
        self.offset_x = 0
        self.offset_y = 0
        self.choose_pos = None
        self.choose_bid = None
        self.choose_rect = pygame.Rect(0,0,BLOCK_SIZE,BLOCK_SIZE)
        self.player_rect = pygame.Rect(0,0,40,120)
        self.player_rect.center = (SC_WIDTH/2,SC_HEIGHT/2)
    def state(self,s):
        self.__state = s
    def keyin(self,k,s):
        self.__keystate[k] = s
    def get_id(self,pos):
        col = (self.offset_x + pos[0]) // BLOCK_SIZE
        row = (self.offset_y + pos[1]) // BLOCK_SIZE
        return (row,col)
    def get_pos(self,row,col):
        if (row >= len(self.data)) or (col >= len(self.data[row])) or (not self.data[row][col]):
            return None
        x = col * BLOCK_SIZE - self.offset_x
        y = row * BLOCK_SIZE - self.offset_y
        return (x,y)
    def choose(self,epos):
        self.choose_bid = self.get_id(epos)
        self.choose_pos = self.get_pos(*self.choose_bid)
        if self.choose_pos:
            self.choose_rect.topleft = self.choose_pos
    def move(self):
        # 测定player四个角所在的位置
        p_lt_site = self.get_id(self.player_rect.topleft)
        p_lb_site = self.get_id(self.player_rect.bottomleft)
        p_rt_site = self.get_id(self.player_rect.topright)
        p_rb_site = self.get_id(self.player_rect.bottomright)
        # 键盘移动
        ks = self.__keystate
        x_movement = 0
        y_movement = 0
        x_movement -= ks[pygame.K_LEFT] + ks[pygame.K_a]
        x_movement += ks[pygame.K_RIGHT] + ks[pygame.K_d]
        y_movement -= ks[pygame.K_DOWN] + ks[pygame.K_s]
        y_movement += ks[pygame.K_UP] + ks[pygame.K_w]
        self.offset_x += x_movement
        self.offset_y -= y_movement
        if self.offset_x >= MP_WIDTH - SC_WIDTH:
            self.offset_x = MP_WIDTH - SC_WIDTH - 1
        elif self.offset_x < 0:
            self.offset_x = 0
        if self.offset_y >= MP_HEIGHT - SC_HEIGHT:
            self.offset_y = MP_HEIGHT - SC_HEIGHT - 1
        elif self.offset_y < 0:
            self.offset_y = 0
        # 光标选择
        self.choose(evt_pos)
    def show(self):
        left = self.offset_x // BLOCK_SIZE
        top = self.offset_y // BLOCK_SIZE
        left_pos = self.offset_x % BLOCK_SIZE
        top_pos = self.offset_y % BLOCK_SIZE
        for row in range(top, top + HEIGHT + 1):
            for col in range(left, left + WIDTH + 1):
                img = images[self.data[row][col]]
                if img:
                    x = (col - left) * BLOCK_SIZE - left_pos
                    y = (row - top) * BLOCK_SIZE - top_pos
                    screen.blit(img,(x,y))
        pygame.draw.rect(screen,(255,0,0),self.player_rect,3)
        if self.choose_pos:
            pygame.draw.rect(screen,(0,0,0),self.choose_rect,3)
        if self.__state == 'click':
            row, col = self.choose_bid
            if (row < len(self.data)) and (col < len(self.data[row])) and self.data[row][col]:
                self.data[row][col] = 0

gamemap = GameMap(data)

clock = pygame.time.Clock()
evt_pos = (-1,-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            evt_pos = event.pos
            gamemap.choose(evt_pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            gamemap.state('click')
        if event.type == pygame.MOUSEBUTTONUP:
            gamemap.state('unclick')
        if event.type == pygame.KEYDOWN:
            gamemap.keyin(event.key,1)
        if event.type == pygame.KEYUP:
            gamemap.keyin(event.key,0)
    
    screen.fill((255,255,255))
    gamemap.move()
    gamemap.show()
    pygame.display.update()
    clock.tick()
    pygame.display.set_caption(f'IDU Sandbox Driver (FPS: {round(clock.get_fps())} x:{gamemap.offset_x} y:{gamemap.offset_y})')