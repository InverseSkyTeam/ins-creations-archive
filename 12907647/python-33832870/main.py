print('玩法：游戏有16x12个方格，点击则种植黑色方格。右侧栏中“FPS”显示游戏帧率以及流畅程度，按钮“添加国家”可以放国家种类更多。为保证编辑整洁，最多可建立7个国家。点击国家的旗帜（国家名称左边的方格），再点击左边操控区的任意位置，将会增加一个国家的国土。然后，你就能开始玩了。如果点错了，请右键点击方格。可以当游戏玩，也可以做动画，点“做下一帧”可以进入下一帧的版图制作。“导出数据”将会把作品数据导出为txt格式，下次可以供新版本游戏使用')
print('留意弹出的窗口')
from time import *
import pygame,sys,random,os

pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("国家版图变化模拟器")

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
        self.delete_image = pygame.image.load('close.png')
        self.delete_rect = pygame.Rect((self.x+60,self.y,10,10))
    def grounds_update(self,dict_):
        self.grounds = dict_[self.name]
    def draw_flag(self):
        pygame.draw.rect(screen,self.color,self.flag_rect,0)
        show_text(self.name+str(self.grounds),self.color,(self.x+15,self.y-3),16)
        screen.blit(self.delete_image,self.delete_rect)

# rectlist = [Ground(i,j,(180,180,180),1) for i in range(800) for j in range(600)]
# rectlist = [Ground(i*2,j*2,(180,180,180),2) for i in range(400) for j in range(300)]
# rectlist = [Ground(i*5,j*5,(180,180,180),5) for i in range(160) for j in range(120)]
# rectlist = [Ground(i*10,j*10,(180,180,180),10) for i in range(80) for j in range(60)]
# rectlist = [Ground(i*20,j*20,(180,180,180),20) for i in range(40) for j in range(30)]
rectlist = [Ground(i*50,j*50,(180,180,180),50) for i in range(16) for j in range(12)]
countrylist = []
add_country_button = pygame.Rect((805,56,190,30))
next_image_button = pygame.Rect((805,550,190,30))
output_button = pygame.Rect((805,430,190,30))
choose_color = (0,0,0)
choose_belong_country = 'unbelong any country'
# belong_grounds_counter = {'unbelong any country':800*600}
# belong_grounds_counter = {'unbelong any country':400*300}
# belong_grounds_counter = {'unbelong any country':160*120}
# belong_grounds_counter = {'unbelong any country':80*60}
# belong_grounds_counter = {'unbelong any country':40*30}
belong_grounds_counter = {'unbelong any country':16*12}
data = []
image_index = 1

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
                if output_button.collidepoint(event.pos):
                    with open('版图数据.txt','w') as f:
                        f.write(str(data))
                        f.close()
                    os.system('start 版图数据.txt')
                if next_image_button.collidepoint(event.pos):
                    image_index += 1
                    data.append([i.color for i in rectlist])
                if add_country_button.collidepoint(event.pos):
                    xlist = [i.name for i in countrylist]
                    if '红' not in xlist:
                        countrylist.append(Country('红',(255,0,0),0))
                        belong_grounds_counter['红'] = 0
                        break
                    if '蓝' not in xlist:
                        countrylist.append(Country('蓝',(0,0,255),1))
                        belong_grounds_counter['蓝'] = 0
                        break
                    if '绿' not in xlist:
                        countrylist.append(Country('绿',(0,255,0),2))
                        belong_grounds_counter['绿'] = 0
                        break
                    if '黄' not in xlist:
                        countrylist.append(Country('黄',(255,235,11),3))
                        belong_grounds_counter['黄'] = 0
                        break
                    if '青' not in xlist:
                        countrylist.append(Country('青',(11,255,255),4))
                        belong_grounds_counter['青'] = 0
                        break
                    if '橙' not in xlist:
                        countrylist.append(Country('橙',(255,155,11),5))
                        belong_grounds_counter['橙'] = 0
                        break
                    if '紫' not in xlist:
                        countrylist.append(Country('紫',(230,11,255),6))
                        belong_grounds_counter['紫'] = 0
                        break
                for i in countrylist:
                    if i.flag_rect.collidepoint(event.pos):
                        choose_color = i.color
                        choose_belong_country = i.name
                    if i.delete_rect.collidepoint(event.pos):
                        choose_color = (0,0,0)
                        choose_belong_country = 'unbelong any country'
                        for j in rectlist:
                            if j.belong == i.name:
                                j.belong = 'unbelong any country'
                                j.color = (0,0,0)
                        del belong_grounds_counter[i.name]
                        countrylist.remove(i)
                        break
            elif event.button == 3:
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
    pygame.draw.rect(screen,(11,255,64),output_button,0)
    show_text('导出数据',(0,0,0),(840,430),30)
    pygame.draw.rect(screen,(255,155,11),next_image_button,0)
    show_text('正在做第'+str(image_index)+'帧...',(0,0,0),(810,510),20)
    show_text('做下一帧',(0,0,0),(840,550),30)
    show_text(str(round(clock.get_fps(),1))+'/FPS',(0,0,0),(811,11),40)
    pygame.display.update()
    clock.tick()