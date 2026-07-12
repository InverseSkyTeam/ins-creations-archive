from xeslib import *  # 播放音乐的库，之后会接触到
import pygame,random
import time as ttime
from os import *

# 全局变量定义
WIDTH = 800
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('打地鼠')
clock = pygame.time.Clock()

bg_img = pygame.image.load('bg.jpg')
system('clear')
bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT))
hole_img = None
hole_rect = mole_rect = None
time_img = pygame.image.load('时间.png')
system('clear')
score_img = pygame.image.load('分数.png')
system('clear')
over = pygame.image.load('over.jpg')
system('clear')
hit_img = pygame.image.load('打.png')
system('clear')
hit_sound = playbgMusic("打.mp3")   # 加载音乐
system('clear')
fire = playbgMusic("bomb.wav")
system('clear')

g_map = None

map_w_num = map_h_num = hole_w = hole_h = dis = 0
w_blank = 40
h_blank = 20
mole_h = 327
mole_w = 276
image_dic = {}
font = pygame.font.SysFont(None,30)
hammer = None
mole_dict = {}
hit_row = 0
hit_col = 0
g_time = 0
default_game_time_state = 0

start_time = ttime.time()
g_score = 0
hole_num = 0

count1 = 0

count2 = 1

g_level = 0
hole_tag = ''
music_state = 1


'''锤子类'''
class Hammer():
    def __init__(self, image1,image2,position):
        self.image1 = image1
        self.image2 = image2
        self.rect = self.image1.get_rect()
        self.rect.left, self.rect.top = position
        # 用于显示锤击时的特效
        self.hammer_count = 0
        self.hammer_last_time = 4
        self.is_hammering = False
    '''设置位置'''
    def setPosition(self, pos):
        self.rect.center = pos
    '''设置hammering'''
    def setHammering(self):
        self.is_hammering = True
    '''显示在屏幕上'''
    def draw(self, screen):
        if self.is_hammering:
            self.image = self.image2
            self.hammer_count += 1
            if self.hammer_count > self.hammer_last_time:
                self.is_hammering = False
                self.hammer_count = 0
        else:
            self.image = self.image1
        screen.blit(self.image, self.rect)

'''地鼠'''
class Mole():
    def __init__(self, image, i,j,hit_img):
        self.image = image
        self.hit_img = hit_img
        self.hit_rect = self.hit_img.get_rect()
        self.rect = self.image.get_rect()
        self.row = i
        self.col = j
        self.rect.center = (w_blank//2+j*hole_w+hole_w//2,dis + h_blank//2+i*hole_h)
        self.rect.bottom = dis + h_blank // 2 + i * hole_h + hole_h // 2
        self.hit_rect.center = (w_blank//2+j*hole_w+hole_w//2,self.rect.top)
        self.is_hammer = False
        self.is_show = False
        self._count = 0    # 用来控制地鼠被打情况的显示

    '''设置被击中'''
    def setBeHammered(self):
        self.is_hammer = True

    def set_show(self):
        self.is_show = True

    def set_hide(self):
        self.is_show = False

    def isHammered(self):
        return self.is_hammer

    '''显示在屏幕上'''
    def draw(self, screen):
        if self.is_show:
            screen.blit(self.image, self.rect)
            if self.is_hammer:# and self._count<5:
                screen.blit(self.hit_img,self.hit_rect)
                hit_sound.play(1)
                ###########################################击打音乐
                # self.set_hide()
                # self.is_hammer = False
                # self._count += 1
                # if self._count == 5:
                #     self._count = 0
    '''重置'''
    def reset(self):
        self.is_hammer = False
        self._count = 0
        # self.is_show = False

def set_bgpic(pic = 'bg.jpg'):
    global bg_img
    bg_img = pygame.image.load(pic)
    bg_img = pygame.transform.scale(bg_img,(WIDTH,HEIGHT)) 
    
def _show_map():
    for i in range(map_h_num):
        for j in range(map_w_num):
            hole_rect.center = (w_blank//2+j*hole_w+hole_w//2,dis + h_blank//2 + i*hole_h+ hole_h//2)
            screen.blit(hole_img,hole_rect)
            if hole_tag != g_map[i][j]:
                if (i,j) in mole_dict:
                    mole_dict[(i,j)].set_show()
                else:
                    mole = Mole(image_dic[g_map[i][j]],i,j,hit_img)
                    mole.set_show()
                    mole_dict[(i,j)] = mole
            else:
                if (i,j) in mole_dict:
                    del mole_dict[(i,j)]
    # print(mole_dict)

def _init():
    global hammer,time_img,score_img,h_image1,h_image2
    h_image1 = pygame.image.load('锤子.png')
    h_image2 = pygame.image.load('锤子2.png')
    # 锤子图片大小
    W = h_image1.get_rect().width
    H = h_image1.get_rect().height
    w = 160
    h = w * H / W
    h_image1 = pygame.transform.scale(h_image1,(w,h))
    h_image2 = pygame.transform.scale(h_image2,(w,h))
    hammer = Hammer(h_image1,h_image2,(-100,-100))
    # 分数和时间图片大小
    w = 180
    h = w//3
    time_img = pygame.transform.scale(time_img,(w,h))
    score_img = pygame.transform.scale(score_img,(w,h))

def big():
    global hammer,count1,h_image1,h_image2,count2
    
    
    count2  = count2 + 1
    W = h_image1.get_rect().width
    H = h_image1.get_rect().height
    # w1 = 80
    # h1 = w1 * H / W
    # h_image11 = pygame.transform.scale(h_image1,(w1,h1))
    # h_image21 = pygame.transform.scale(h_image2,(w1,h1))
    
    w2 = 100 * count2
    h2 = w2 * H / W
    h_image12 = pygame.transform.scale(h_image1,(w2,h2))
    h_image22 = pygame.transform.scale(h_image2,(w2,h2))
    hammer = Hammer(h_image12,h_image22,pygame.mouse.get_pos())
    hammer.draw(screen)
    
    # pic = [
    #     h_image11,h_image21,h_image12,h_image22,
    #     ]
    # print(count1)
    # if count1 == 0:
        
    #     # w = 80
    #     # h = w * H / W 
    #     # h_image1 = pygame.transform.scale(h_image1,(w,h))
    #     # h_image2 = pygame.transform.scale(h_image2,(w,h))
    #     hammer = Hammer(pic[0],pic[1],(pic[0].get_rect().left,pic[0].get_rect().top))
    #     count1 = 1
    #     print(count1)
    #     # hammer.is_hammer = True
    #     hammer.draw(screen)
    # else:
    #     # W = h_image1.get_rect().width
    #     # H = h_image1.get_rect().height
        
    #     hammer = Hammer(pic[2],pic[3],(pic[2].get_rect().left,pic[2].get_rect().top))
    #     count1 = 0
    #     print(count1)
    #     # hammer.is_hammer = True
    #     hammer.draw(screen)
    # # count1 = count1 + 1

'''
检查列表中是否图片文件名
'''
def _init_map(map):
    global hole_tag,g_map
    if hole_tag == '':
        hole_tag = 'h'
    
    if '.' in map[0][0]:
        add_hole(hole_tag,map[0][0])
        row = len(map)
        col = len(map[0])
        g_map = [[hole_tag for i in range(col) ] for i in range(row)]
        return True
    else:
        return False
    
def small():
    global hammer,count1,h_image1,h_image2,count2
    
    
    count2  = count2 + 1
    W = h_image1.get_rect().width
    H = h_image1.get_rect().height
    # w1 = 80
    # h1 = w1 * H / W
    # h_image11 = pygame.transform.scale(h_image1,(w1,h1))
    # h_image21 = pygame.transform.scale(h_image2,(w1,h1))
    
    w2 = 300 / count2
    h2 = w2 * H / W
    h_image12 = pygame.transform.scale(h_image1,(w2,h2))
    h_image22 = pygame.transform.scale(h_image2,(w2,h2))
    hammer = Hammer(h_image12,h_image22,pygame.mouse.get_pos())
    hammer.draw(screen)

def add_hole(image,tag = 'h'):
    global hole_tag
    hole_tag = tag
    image_dic[tag] = pygame.image.load(image)
    
def add_pic(image,tag = '年兽'):
    image_dic[tag] = pygame.image.load(image)
    # print(image_dic)
start_time = 0
def set_map(map):
    _init()
    global g_map, hole_img, mole_w, mole_h, map_w_num, map_h_num, hole_w, hole_h,dis,hole_rect,mole_rect,hit_img,hole_num,start_time
    start_time = ttime.time()
    
    dis = int(HEIGHT * (300/1440))
    map_h = HEIGHT - dis - h_blank
    if not _init_map(map):
        g_map = map
    # 计算地鼠洞的大小
    map_w_num = len(g_map[0])
    map_h_num = len(g_map)
    hole_num = map_h_num * map_w_num
    hole_h = map_h/map_h_num
    hole_w = (WIDTH-w_blank)/map_w_num
    rate_h = hole_h/229
    rate_w = hole_w/369
    if rate_h < rate_w:
        h = int(229* rate_h)
        w = int(369*rate_h)
    else:
        h = int(229*rate_w)
        w = int(369 * rate_w)
    hole_img = pygame.transform.scale(image_dic[hole_tag],(w,h))
    hole_rect = hole_img.get_rect()
    rate_mole = mole_w/mole_h
    # 计算地鼠的大小
    mole_h = int(h*1.5)
    mole_w = int(rate_mole * mole_h)
    hit_img_w = max(281,mole_w)
    hit_img_h = int(hit_img_w/281*159)
    hit_img = pygame.transform.scale(hit_img,(hit_img_w,hit_img_h))

    for k in image_dic:
        if k!=hole_tag:
            image_dic[k] = pygame.transform.scale(image_dic[k],(mole_w,mole_h))

    screen.blit(bg_img,(0,0))
    # screen.blit(score_img,(20,20))
    # screen.blit(time_img,(600,20))
    _show_map()
    pygame.display.update()

def mouse(level = 1,num = 2):
    global hit_row,hit_col,hole_num,g_level
    if level > 10:
        level = 10
    if level < 1:
        level = 1
    
    cnt = 60-(level-1)*6
    g_level+=1
    if g_level>cnt:
        g_level = 0
    
        # 地鼠数量不能超过洞的数量
        if num>=hole_num:
            num = hole_num-1
    
        # 全部重置为洞
        for i in range(map_h_num):
            for j in range(map_w_num):
                if g_map[i][j]!=hole_tag:
                    g_map[i][j] = hole_tag
        # 随机生成地鼠
        m_list = list(image_dic.keys())
        # print(m_list)
        m_list.remove(hole_tag)
        for i in range(num):
            x = random.randint(0,map_h_num-1)
            y = random.randint(0,map_w_num-1)
            num = len(m_list)
            n = random.randint(0,num-1)
            g_map[x][y] = m_list[n]
            # print(m_list[n])
    
        # 返回的row和col标记的未知不能有地鼠
        for i in range(map_h_num):
            for j in range(map_w_num):
                if g_map[i][j] == hole_tag:
                    hit_row = i
                    hit_col = j
                    break

song = True
def music(name):
    global song
    song = playbgMusic(name)   # 加载音乐
    song.play() # 播放音乐

end = playbgMusic('over.mp3')
system('clear')

boom_list = []
for i in range(23):
    boom_list.append(pygame.image.load(str(i) + '.png'))
    system('clear')
for i in range(23):
    boom_list[i] = pygame.transform.scale(boom_list[i], (800,800))

def boom():
    global boom_list
    song.stop()
    fire.play(2)
    for i in boom_list:
        screen.fill((0, 0, 0))
        screen.blit(i,(0,-120))
        pygame.time.wait(40)
        pygame.display.update()
    # song.continue(2)
    song.play()

remaining_time = 0
countdown = 60
coin = 0
def play():
    global hit_row,hit_col,g_time,music_state,countdown,coin,song,remaining_time,start_time
    if music_state == 1:
        music_state = 0
        music("bgm.mp3")
    g_map[hit_row][hit_col] = hole_tag
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEMOTION:
            hammer.setPosition(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                hammer.setHammering()
                for m in mole_dict.values():
                    if m.rect.colliderect(hammer.rect):
                        m.setBeHammered()
                        hit_row = m.row
                        hit_col = m.col
                        break
    
    
    screen.blit(bg_img,(0,0))
    # 显示时间和分数
    screen.blit(score_img,(20,20))
    screen.blit(time_img,(600,20))
    g_time = int(ttime.time() - start_time)
    
    remaining_time = countdown - g_time
    t_txt = font.render(str(remaining_time),True,(0,0,0))
    screen.blit(t_txt,(685,32))
    score_txt = font.render(str(g_score), True, (0, 0, 0))
    screen.blit(score_txt, (105, 35))
    # 显示地图
    _show_map()
    # 显示地鼠
    for v in mole_dict.values():
        v.draw(screen)
        if v.isHammered():
            for i in range(6):
                v.draw(screen)
    hammer.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
    default_game_time(59) # 默认游戏时长30秒

def hit_index1():
    return hit_row

def hit_index2():
    return  hit_col

def hit():
    return g_map[hit_row][hit_col]

def show_beast(score):
    global g_score
    # g_map[hit_row][hit_col] = "h"
    g_score = score


# 默认游戏时长
def default_game_time(t):
    global default_game_time_state,g_score,song
    if default_game_time_state == 0 and g_time > t:
        song.stop()
        ttime.sleep(1)
        screen.blit(over,(0,0))
        end.play(3)
        score_txt = font.render(str(g_score), True, (0, 0, 0))
        screen.blit(score_txt,(420, 303))
        pygame.display.update()
        ttime.sleep(5)
        pygame.quit()
        

def game_time(t):
    global default_game_time_state
    default_game_time_state = 1
    if g_time>t:
        screen.blit(over,(WIDTH/2-150,HEIGHT/2-135))
        pygame.display.update()
        
        pygame.quit()