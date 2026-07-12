# 小轩制作，感谢胡锦辉的建议。
from moviepy.editor import *
import pygame,sys,random
import game_life_data as ld
import game_hdata as hd
pygame.init()

pygame.display.set_icon(pygame.image.load('file/icon/地球图标.png'))

screen = pygame.display.set_mode((1400,900))
pygame.display.set_caption("小轩-创造星球NSE版")

planet_window_rect = pygame.Rect(60,100,700,500)
config_window_rect = pygame.Rect(900,100,420,700)

try:import ntpath      #文字处理系统
except:font = pygame.font.SysFont('kaittf', 30);font2 = pygame.font.SysFont('kaittf', 20)
else:font = pygame.font.SysFont('kaiti', 30);font2 = pygame.font.SysFont('kaiti', 20);del ntpath
def show_text(text,color=(0,0,0),pos=(0,0)):
    screen.blit(font.render((text),True,color),pos)
def show_text2(text,color=(0,0,0),pos=(0,0)):
    screen.blit(font2.render((text),True,color),pos)

def draw_window(r,c1,c2,size=4):
    pygame.draw.rect(screen,c1,r,0)
    pygame.draw.rect(screen,c2,r,size)

class PageButton(object):
    def __init__(self,all,text):
        self.rect = pygame.Rect(all)
        self.color = (220,220,220)
        self.text = text
    def draw(self):
        draw_window(self.rect,self.color,(0,0,0),size=2)
        show_text2(text=self.text,pos=self.rect.topleft)
    def hit(self,pos):
        if self.rect.collidepoint(pos):
            self.color = (170,170,170)
            return 'hit'
        else:
            self.color = (220,220,220)
            return 'none'

class Button(PageButton):
    def __init__(self,all,text):
        super().__init__(all,text)
        self.color = (0,225,225)
    def draw(self):
        draw_window(self.rect,self.color,(0,0,0),size=3)
        show_text(text=self.text,pos=self.rect.topleft)
    def hit(self,pos,func=False,the_func=None):
        if self.rect.collidepoint(pos):
            if func:
                the_func()
            else:
                return 'hit'

class Planet(object):
    def __init__(self,planet_name,r):
        self.name = planet_name
        self.color = (255,0,0)
        self.w = random.randint(400,410)
        self.h = self.w - 10
        self.rect = pygame.Rect(0,0,self.w,self.h)
        self.rect.center = r.center
        self.YEARS = -4720000000
    def draw(self):
        pygame.draw.ellipse(screen,self.color,self.rect,0)

Earth_land_picture_list = [
    pygame.image.load('file/大陆板块/前寒武纪.png'),
    pygame.image.load('file/大陆板块/寒武纪.png'),
    pygame.image.load('file/大陆板块/二叠纪.png'),
    pygame.image.load('file/大陆板块/侏罗纪.png'),
    pygame.image.load('file/大陆板块/现.png')
    ]

pagebutton = PageButton((60,80,80,20),'我的行星')
pagebutton2 = PageButton((140,80,40,20),'卫星')
pagebutton3 = PageButton((180,80,120,20),'查看生物状况')
pagebutton4 = PageButton((300,80,80,20),'历史资料')
water_ok_button = Button((910,450,180,40),'完成水的控制')
start_life_button = Button((900,160,420,45),'生命的开始（培养单细胞生物）')
histroy_button = Button((910,190,270,40),'下一个重要历史事件')
return_button = Button((1329,849,60,40),'返回')

page = 1
part = '主页面'
BIGevent = '选择行星'
next_text_choice = ''
planet_OK = False
pagebutton_path = False
pagebutton_path2 = False
planet_img = False
period = '元古宙'
water = 0
histroy_number = 0
all_ld = {
    '元古宙':ld.l1,
    '前寒武纪':ld.l2,
    '寒武纪':ld.l3,
    '奥陶纪':ld.l4,
    '志留纪':ld.l5,
    '泥盆纪':ld.l6,
    '石炭纪':ld.l7,
    '二叠纪':ld.l8,
    '三叠纪':ld.l9,
    '侏罗纪':ld.l10,
    '白垩纪':ld.l11,
    '古近纪':ld.l12,
    '新近纪':ld.l13,
    '第四纪':ld.l14,
}

planet = Planet('地球',planet_window_rect)
planet_x = Planet('月球',planet_window_rect);planet_x.color=(255,255,150)

while True:
    while part == '主页面':
        for event in pygame.event.get(): # 检测系统事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if pagebutton.hit(event.pos) == 'hit':
                        page = 1
                    if pagebutton_path:
                        if pagebutton2.hit(event.pos) == 'hit':
                            page = 2
                        if pagebutton3.hit(event.pos) == 'hit':
                            if pagebutton3.text == '查看生物状况':
                                part = '生物页面'
                            else:
                                clip = VideoFileClip('file/电影/地球动态.mp4')
                                clip = clip.resize(newsize=(480,480))
                                clip.preview()
                                screen = pygame.display.set_mode((1400,900))
                    if pagebutton_path2:
                        if pagebutton4.hit(event.pos) == 'hit':
                            part = '历史资料页面'
                    if water_ok_button.hit(event.pos) == 'hit' and BIGevent == '固态行星':
                        if water <= 50:
                            BIGevent = '水源过少！！'
                            next_text_choice = '这里不再适合生物生存'
                        elif water <= 60:
                            BIGevent = '水源较少！！'
                            next_text_choice = '勉强制造了一个“干巴巴”'
                        elif water <= 80:
                            BIGevent = '水源确定！！'
                            next_text_choice = '干得不错！'
                            water = 71
                            planet.color = (0,113,202)
                        elif water <= 85:
                            BIGevent = '水源较多！！'
                            next_text_choice = '陨石降临，把你的水量降低了'
                            water = 75
                            planet.color = (0,113,202)
                        else:
                            BIGevent = '水源过多！！'
                            next_text_choice = '这里不适合生物生存下去'
                    if start_life_button.hit(event.pos) == 'hit' and BIGevent == '培养生物':
                        BIGevent = '生物时代'
                        pagebutton_path = True
                    if histroy_button.hit(event.pos) == 'hit' and BIGevent == '人类':
                        histroy_number += 1
                        i2 = -1
                        for i in hd.histroy_dict:
                            i2 += 1
                            if i2 == histroy_number:
                                planet.YEARS = i
                                break
                        if histroy_number == len(hd.histroy_dict):
                            BIGevent = '未来'
                            pagebutton_path2 = False
                            planet.YEARS = 2023
            
            if event.type == pygame.KEYDOWN:
                if BIGevent == '选择行星':
                    if event.key == ord('a'):
                        BIGevent = '固态行星'
                        planet_OK = True
                        planet.YEARS = -4600000000
                        next_text_choice = random.choice(['你的固态行星非常稳定','行星成功创建','固态行星形成非常好','你的行星很不错！','你的创造真令人羡慕！'])
                    if event.key == ord('b'):
                        if random.randint(0,2):
                            BIGevent = '气态行星'
                            next_text_choice = random.choice(['你的气态行星极不稳定','行星被别的星球撞击了','气态行星很无聊','气态行星太大了','你的创造被别人颠覆了'])
                        else:
                            BIGevent = 'good气态行星'
                            next_text_choice = random.choice(['行星极稳定了下来','行星大而美'])
                if BIGevent == '固态行星':
                    if event.key == ord('w'):
                        water += random.randint(1,2)
                    if event.key == ord('q'):
                        water -= 1
        screen.fill((160,200,255))
        if page == 1:
            show_text(text='我的行星：'+planet.name,pos=(11,11))
        if page == 2:
            show_text(text=planet.name+'的卫星：'+planet_x.name,pos=(11,11))
        draw_window(planet_window_rect,(220,220,220),(10,155,200))
        draw_window(config_window_rect,(255,255,255),(150,150,150))
        pagebutton.draw()
        if pagebutton_path:
            pagebutton2.draw()
            pagebutton3.draw()
        if pagebutton_path2:
            pagebutton4.draw()
        if planet_OK:
            if page == 1:
                if not planet_img:
                    planet.draw()
                else:
                    screen.blit(Earth_land_picture_list[4],planet.rect.topleft)
            elif page == 2:
                planet_x.draw()
        if BIGevent == '选择行星':
            show_text(text='你好，这里是人类的',pos=(900,100))
            show_text(text='[小轩王牌控制台]',pos=(900,130))
            show_text(text='这里能创造关于行星的一切',pos=(900,160))
            show_text(text='别担心，在这里“智”造很简捷',pos=(900,190))
            show_text(text='我会一直在这里帮助你的',pos=(900,220))
            show_text(text='请你按键选择',pos=(900,250))
            show_text(text='a.固态行星(good)',pos=(900,280))
            show_text(text='b.气态行星',pos=(900,310))
        
        if BIGevent == '气态行星':
            show_text(text=next_text_choice,pos=(900,100))
            show_text(text='创造失败！',color=(255,0,0),pos=(900,130))
        
        if BIGevent == 'good气态行星':
            show_text(text=next_text_choice,pos=(900,100))
            show_text(text='由于气压太大',pos=(900,130))
            show_text(text='星球上的钻石很多',pos=(900,160))
            show_text(text='你因此而富得流油',pos=(900,190))
            show_text(text='创造失败！',color=(255,0,0),pos=(900,220))
            show_text(text='达成成就：富得流油',color=(0,255,0),pos=(900,250))
        
        if BIGevent == '固态行星':
            show_text(text='石头撞击合成了固态行星',pos=(900,100))
            show_text(text=next_text_choice,pos=(900,130))
            show_text(text='创造成功！',color=(0,255,0),pos=(900,160))
            show_text(text='接下来你可以调整一下星球的',pos=(900,190))
            show_text(text='初始属性',pos=(900,220))
            show_text(text='--------------------------',pos=(900,250))
            show_text(text='按w增加水源，按q减少',pos=(900,280))
            show_text(text='水源可能自动增加/减少',pos=(900,310))
            show_text(text='因带水或不带水陨石撞击',pos=(900,340))
            show_text(text='以及其他特殊原因、冷却',pos=(900,370))
            show_text(text='水源越接近71，环境越好',pos=(900,400))
            show_text(text='水:'+str(round(water)),pos=(60,610))
            water_ok_button.draw()
            water += random.randint(-1,1) / 5
            if water < 0:
                water = 0
            if water <= 40:
                planet.color = (255-water*5,water*3,0)
            if water <= 60 and water >= 40:
                planet.color = (0,water*4+15,30+water*2)
            if water <= 80 and water >= 60:
                planet.color = (0,255-water*2,60+water*2)
            if water >= 80:
                planet.color = (0,60,255)
        
        if '水源' in BIGevent and '！！' in BIGevent:
            show_text(text=BIGevent,color=(0,255,255),pos=(900,100))
            show_text(text=next_text_choice,pos=(900,130))
            show_text(text='现在水源共有'+str(round(water))+'个',pos=(900,160))
            if water == 71 or water == 75 or planet.YEARS > -4600000000 and planet.YEARS <= -3780000000:
                show_text(text='你的星球需要时间冷却',pos=(900,190))
                planet.YEARS += random.randint(15000,230000)
                if planet.YEARS <= -4550000000 and planet.YEARS >= -4551000000:
                    water = random.randint(54,64)
                    planet.color = (0,230,200)
                    next_text_choice = '水分大蒸发'
                if planet.YEARS <= -4480000000 and planet.YEARS >= -4481000000:
                    water = random.randint(48,61)
                    planet.color = (80,230,240)
                    next_text_choice = '陨石撞击'
                if planet.YEARS <= -4300000000 and planet.YEARS >= -4301000000:
                    water = random.randint(84,106)
                    planet.color = (0,150,255)
                    next_text_choice = '超大暴雨'
                if planet.YEARS <= -4250000000 and planet.YEARS >= -4251000000:
                    water = random.randint(64,72)
                    planet.color = (150,120,40)
                    next_text_choice = '超级火山喷发'
                if planet.YEARS <= -4190000000 and planet.YEARS >= -4191000000:
                    water = random.randint(84,106)
                    planet.color = (255,255,238)
                    next_text_choice = '大冰期 平均' + str(random.randint(-180,-80)) + '℃'
                if planet.YEARS <= -3900000000 and planet.YEARS >= -3901000000:
                    water = 73
                    planet.color = (40,255,220)
                    next_text_choice = '生前大灾难过去了'
                if planet.YEARS <= -3820000000 and planet.YEARS >= -3821000000:
                    water = 71
                    planet.color = (50,200,255)
                    next_text_choice = '一切都过去了……'
            if planet.YEARS > -3780000000:
                planet.YEARS = -3760000000
                BIGevent = '培养生物'
        
        if BIGevent == '培养生物':
            show_text(text='你现在需要培养生物',pos=(900,100))
            show_text(text='请先按下下方按钮',pos=(900,130))
            start_life_button.draw()
        
        if BIGevent == '生物时代':
            show_text(text=period,color=(0,255,255),pos=(900,100))
            show_text(text='单击左边窗口上方的按钮',pos=(900,130))
            show_text(text='就能查看生物了^_^',pos=(900,160))
            if page == 1:
                if period == '元古宙':
                    planet.YEARS += 1000000
                    if planet.YEARS == -1500000000:
                        period = '前寒武纪'
                        planet.w = 410
                        planet.h = 400
                        planet.rect = pygame.Rect(0,0,planet.w,planet.h)
                        planet.rect.center = planet_window_rect.center
                if period == '前寒武纪':
                    screen.blit(Earth_land_picture_list[0],planet.rect.topleft)
                    planet.YEARS += 500000
                    if planet.YEARS == -541000000:
                        period = '寒武纪'
                if period == '寒武纪':
                    screen.blit(Earth_land_picture_list[1],planet.rect.topleft)
                    planet.YEARS += 50000
                    if planet.YEARS == -478000000:
                        period = '奥陶纪'
                if period == '奥陶纪':
                    screen.blit(Earth_land_picture_list[0],planet.rect.topleft)
                    planet.YEARS += 25000
                    if planet.YEARS == -438000000:
                        period = '志留纪'
                if period == '志留纪':
                    screen.blit(Earth_land_picture_list[0],planet.rect.topleft)
                    planet.YEARS += 50000
                    if planet.YEARS == -400000000:
                        period = '泥盆纪'
                if period == '泥盆纪':
                    screen.blit(Earth_land_picture_list[0],planet.rect.topleft)
                    planet.YEARS += 25000
                    if planet.YEARS == -350000000:
                        period = '石炭纪'
                if period == '石炭纪':
                    screen.blit(Earth_land_picture_list[1],planet.rect.topleft)
                    planet.YEARS += 25000
                    if planet.YEARS == -300000000:
                        period = '二叠纪'
                if period == '二叠纪':
                    screen.blit(Earth_land_picture_list[2],(planet.rect.x+70,planet.rect.y+50))
                    planet.YEARS += 20000
                    if planet.YEARS == -250000000:
                        period = '三叠纪'
                if period == '三叠纪':
                    screen.blit(Earth_land_picture_list[2],(planet.rect.x+70,planet.rect.y+50))
                    planet.YEARS += 20000
                    if planet.YEARS == -200000000:
                        period = '侏罗纪'
                if period == '侏罗纪':
                    screen.blit(Earth_land_picture_list[3],(planet.rect.x+60,planet.rect.y+60))
                    planet.YEARS += 20000
                    if planet.YEARS == -140000000:
                        period = '白垩纪'
                if period == '白垩纪':
                    screen.blit(Earth_land_picture_list[3],(planet.rect.x+60,planet.rect.y+60))
                    planet.YEARS += 20000
                    if planet.YEARS == -65000000:
                        period = '古近纪'
                        planet_img = True
                if period == '古近纪':
                    planet.YEARS += 10000
                    if planet.YEARS == -23000000:
                        period = '新近纪'
                if period == '新近纪':
                    planet.YEARS += 10000
                    if planet.YEARS == -2600000:
                        period = '第四纪'
                if period == '第四纪':
                    planet.YEARS += 500
                    if planet.YEARS == -2300000:
                        planet.YEARS = -2300000
                        BIGevent = '人类'
                        pagebutton3 = PageButton((180,80,120,20),'动态地球一展')
                        pagebutton_path2 = True
        
        if BIGevent == '人类':
            show_text(text='现在你可以查看地球现状',pos=(900,100))
            show_text(text='人属已经开始发展',pos=(900,130))
            show_text(text='历史资料可以告诉你一切',pos=(900,160))
            histroy_button.draw()
        
        if BIGevent == '未来':
            show_text(text='现在是2023年',pos=(900,100))
        
        show_text(text='时间：'+str(planet.YEARS)+'年',pos=(900,810))
        pygame.display.update()
    
    while part == '生物页面':
        for event in pygame.event.get(): # 检测系统事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if return_button.hit(event.pos) == 'hit':
                        part = '主页面'
        screen.fill((160,200,255))
        return_button.draw()
        show_text(text=planet.name+'上的主要生物',color=(0,255,255),pos=(11,11))
        show_text(text=period,color=(255,0,0),pos=(11,41))
        for text_id in range(len(all_ld[period])):
            show_text(text=all_ld[period][text_id],pos=(11,71+text_id*30))
        show_text(text='|请点击窗口右下',pos=(1089,41))
        show_text(text='角的返回键返回|',pos=(1089,71))
        pygame.display.update()
    
    while part == '历史资料页面':
        for event in pygame.event.get(): # 检测系统事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if return_button.hit(event.pos) == 'hit':
                        part = '主页面'
        screen.fill((160,200,255))
        return_button.draw()
        show_text(text=planet.name+'上的主要事件',color=(0,255,255),pos=(11,11))
        i2 = -1
        for i in hd.histroy_dict:
            i2 += 1
            if i2 == histroy_number:
                for ii in range(len(hd.histroy_dict[i])):
                    show_text(text=hd.histroy_dict[i][ii],pos=(11,41+ii*30))
        show_text(text='|请点击窗口右下',pos=(1089,41))
        show_text(text='角的返回键返回|',pos=(1089,71))
        pygame.display.update()