print('玩法：游戏有16x12个方格，点击则种植黑色方格。右侧栏中“FPS”显示游戏帧率以及流畅程度，按钮“添加国家”可以放国家种类更多。为保证编辑整洁，最多可建立5个国家。点击国家的旗帜（国家名称左边的方格），再点击左边操控区的任意位置，将会增加一个国家的国土。然后，你就能开始玩了。如果点错了，请右键点击方格')
import pygame,sys,random

pygame.init()
screen = pygame.display.set_mode((1000,600))

try:import ntpath
except:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)")
else:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)")
finally:pass

class Ground:
    def __init__(self,x,y,c,length,belong='unbelong any country'):
        self.rect = pygame.Rect(x,y,length,length)
        self.color = c
        self.belong = belong
    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect,0)

class Country:
    def __init__(self,name,color,site,had_grounds=0):
        self.name = name
        self.color = color
        self.site = site
        self.x = 810
        self.y = self.site * 25 + 100
        # self.size = 0
        self.grounds = had_grounds
        self.flag_rect = pygame.Rect((self.x,self.y,10,10))
    def grounds_update(self,dict_):
        self.grounds = dict_[self.name]
    def draw_flag(self):
        pygame.draw.rect(screen,self.color,self.flag_rect,0)
        show_text(self.name+str(self.grounds),self.color,(self.x+15,self.y-3),16)

# rectlist = [Ground(i,j,(0,0,0),1) for i in range(800) for j in range(600)]
# rectlist = [Ground(i*2,j*2,(0,0,0),2) for i in range(400) for j in range(300)]
# rectlist = [Ground(i*5,j*5,(0,0,0),5) for i in range(160) for j in range(120)]
# rectlist = [Ground(i*10,j*10,(0,0,0),10) for i in range(80) for j in range(60)]
# rectlist = [Ground(i*20,j*20,(0,0,0),20) for i in range(40) for j in range(30)]
rectlist = [Ground(i*50,j*50,(180,180,180),50) for i in range(16) for j in range(12)]
countrylist = []
add_country_button = pygame.Rect((805,56,190,30))
choose_color = (0,0,0)
choose_belong_country = 'unbelong any country'
belong_grounds_counter = {'unbelong any country':16*12}
data = []

mouseleftbutton_isdown = False
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseleftbutton_isdown = True
                if add_country_button.collidepoint(event.pos):
                    if len(countrylist) == 0:
                        countrylist.append(Country('红',(255,0,0),0))
                        belong_grounds_counter['红'] = 0
                        break
                    if len(countrylist) == 1:
                        countrylist.append(Country('蓝',(0,0,255),1))
                        belong_grounds_counter['蓝'] = 0
                        break
                    if len(countrylist) == 2:
                        countrylist.append(Country('绿',(0,255,0),2))
                        belong_grounds_counter['绿'] = 0
                        break
                    if len(countrylist) == 3:
                        countrylist.append(Country('黄',(200,200,11),3))
                        belong_grounds_counter['黄'] = 0
                        break
                    if len(countrylist) == 4:
                        countrylist.append(Country('青',(11,255,255),4))
                        belong_grounds_counter['青'] = 0
                        break
                for i in countrylist:
                    if i.flag_rect.collidepoint(event.pos):
                        choose_color = i.color
                        choose_belong_country = i.name
            else:
                mouseleftbutton_isdown = 'cleaning'
        if event.type == pygame.MOUSEBUTTONUP:
            mouseleftbutton_isdown = False
    screen.fill((255,255,255))
    for i in belong_grounds_counter:
        belong_grounds_counter[i] = 0
    if mouseleftbutton_isdown == 'cleaning':
        for i in rectlist:
            if i.rect.collidepoint(event.pos):
                i.color = (0,0,0)
                i.belong = 'unbelong any country'
    else:
        if mouseleftbutton_isdown == True:
            for i in rectlist:
                if i.rect.collidepoint(event.pos):
                    i.color = choose_color
                    i.belong = choose_belong_country
    for i in rectlist:
        belong_grounds_counter[i.belong] += 1
    for i in countrylist:
        i.grounds_update(belong_grounds_counter)
        i.draw_flag()
    for i in rectlist:
        i.draw()
    pygame.draw.rect(screen,(0,255,255),add_country_button,0)
    show_text('添加国家',(0,0,0),(840,56),30)
    show_text(str(round(clock.get_fps(),1))+'/FPS',(0,0,0),(811,11),40)
    pygame.display.update()
    clock.tick()