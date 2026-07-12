print('''
玩法：游戏有16x12个方格，点击则种植黑色方格。
右侧栏中“FPS”显示游戏帧率以及流畅程度，按钮“添加国家”可以放更多国家种类。
为保证编辑整洁快速，最多可建立8个国家。
点击国家的旗帜（国家名称左边的方格），再点击左边操控区的任意位置，将会增加一个国家的国土。
如果点错了，请右键点击方格。或者点击“炸掉领土”不要放开，拖到方格上，然后炸完松开
可以当游戏玩，也可以做动画，点“做下一帧”可以进入下一帧的版图制作，点“改上一帧”反之亦然，数据会被记住。
“导出数据”将会把作品数据导出为ijca专属格式文件，可以供导入播放使用
''')
print('留意弹出的窗口')
from tkinter import *
from time import *
import tkinter.filedialog
import pygame,sys,random,os
user_name = os.getlogin()

pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("国家版图变化模拟器")

try:import ntpath
except:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)")
else:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)")
finally:pass

def mkdir(path):
    import os
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False

mkdir('../../国家版图变化模拟器')

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
        self.delete_rect = pygame.Rect((self.x+100,self.y,10,10))
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
upload_ijcafile_img = pygame.image.load('上传ijca文件.png')
upload_ijcafile_rect = upload_ijcafile_img.get_rect()
upload_ijcafile_ok_rect = upload_ijcafile_img.get_rect()
upload_ijcafile_rect.topleft = (11,11)
upload_ijcafile_ok_rect.topleft = (11,81)
countrylist = []
add_country_button = pygame.Rect((805,56,190,30))
delete_ground_button = pygame.Rect((805,300,25,25))
last_image_button = pygame.Rect((805,550,190,20))
next_image_button = pygame.Rect((805,575,190,20))
output_button = pygame.Rect((805,430,190,30))
lets_make_button = pygame.Rect((250,150,500,60))
lets_view_button = pygame.Rect((250,260,500,60))
lmbcmpos = False
lvbcmpos = False
do_file_name_x = None
choose_color = (0,0,0)
choose_belong_country = 'unbelong any country'
# belong_grounds_counter = {'unbelong any country':800*600}
# belong_grounds_counter = {'unbelong any country':400*300}
# belong_grounds_counter = {'unbelong any country':160*120}
# belong_grounds_counter = {'unbelong any country':80*60}
# belong_grounds_counter = {'unbelong any country':40*30}
belong_grounds_counter = {'unbelong any country':16*12}
colors_to_countries = {(180,180,180):'unbelong any country',(0,0,0):'unbelong any country'}
data = []
image_index = 1
img_fp_index = 1
view_speed = '手动'
veiw_t = time()

part = 'mainpage'

mouseleftbutton_isdown = False
clock = pygame.time.Clock()

while True:
    while part == 'mainpage':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if lets_make_button.collidepoint(event.pos):
                    lmbcmpos = True
                else:
                    lmbcmpos = False
                if lets_view_button.collidepoint(event.pos):
                    lvbcmpos = True
                else:
                    lvbcmpos = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lets_make_button.collidepoint(event.pos):
                    data = []
                    part = 'make'
                if lets_view_button.collidepoint(event.pos):
                    part = 'view'
        screen.fill((211,211,211))
        show_text('国家',(0,0,0),(11,11),80)
        show_text('版图',(0,0,255),(171,11),80)
        show_text('变',(0,255,255),(331,11),80)
        show_text('化',(255,45,11),(411,11),80)
        show_text('模拟器',(0,255,0),(491,11),100)
        show_text('V0.4.1',(111,111,111),(800,11),60)
        pygame.draw.line(screen,(255,155,11),(0,111),(1000,111),5)
        pygame.draw.line(screen,(80,80,80),(0,116),(1000,116),4)
        pygame.draw.line(screen,(255,155,11),(0,120),(1000,120),3)
        show_text('(c)Copyright.INS-jhx逆天团队小轩 /did with python on 2022.6.11/(v)Version->0.4.1 -α',(111,111,111),(11,90),11)
        if lmbcmpos == True:
            pygame.draw.rect(screen,(111,255,255),lets_make_button,8)
            pygame.draw.rect(screen,(255,255,255),lets_make_button,0)
            show_text(' 制  作|版图动画',(0,0,255),(250,150),60)
        else:
            pygame.draw.rect(screen,(0,0,0),lets_make_button,11)
            pygame.draw.rect(screen,(180,180,180),lets_make_button,0)
            show_text(' 制  作|版图动画',(0,255,0),(250,150),60)
        if lvbcmpos == True:
            pygame.draw.rect(screen,(111,255,255),lets_view_button,8)
            pygame.draw.rect(screen,(255,255,255),lets_view_button,0)
            show_text(' 播  放|版图动画',(255,0,0),(250,260),60)
        else:
            pygame.draw.rect(screen,(0,0,0),lets_view_button,11)
            pygame.draw.rect(screen,(180,180,180),lets_view_button,0)
            show_text(' 播  放|版图动画',(0,255,0),(250,260),60)
        pygame.display.update()
    
    while part == 'make':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseleftbutton_isdown = 'click'
                if event.button == 1:
                    if output_button.collidepoint(event.pos):
                        if len(data) == image_index:
                            data[-1] = [i.color for i in rectlist]
                        elif len(data) < image_index:
                            data.append([i.color for i in rectlist])
                        # else:pass 因为如果徘徊在之前的画帧中，那么最后一帧一定被保存过且无需改动了
                        with open('../../国家版图变化模拟器/版图数据-编码'+str(random.randint(1000,9999))+'.ijca','w',encoding='utf-8') as f:
                            f.write('size->(6,"INS-jhx ijca file screen size Cx",10011001,10110101,11011011,11111001,10001000,11011001)\n')
                            f.write('data->'+str(data))
                            f.close()
                        part = 'mainpage'
                    if last_image_button.collidepoint(event.pos):
                        if image_index != 1:
                            image_index -= 1
                            if len(data) >= image_index + 1:
                                data[image_index] = [i.color for i in rectlist]
                            else:
                                data.append([i.color for i in rectlist])
                            # rectlist = [Ground(i//30*50,i%30*50,data[image_index-1][i],50) for i in range(len(data[image_index-1]))]
                            rectlist = [Ground(i//12*50,i%12*50,data[image_index-1][i],50) for i in range(len(data[image_index-1]))]
                            for i in rectlist:
                                i.belong = colors_to_countries[i.color]
                        break
                    if next_image_button.collidepoint(event.pos):
                        image_index += 1
                        if len(data) >= image_index:
                            data[image_index-2] = [i.color for i in rectlist]
                            # rectlist = [Ground(i//30*50,i%30*50,data[image_index-1][i],50) for i in range(len(data[image_index-1]))]
                            rectlist = [Ground(i//12*50,i%12*50,data[image_index-1][i],50) for i in range(len(data[image_index-1]))]
                            for i in rectlist:
                                i.belong = colors_to_countries[i.color]
                        else:
                            data.append([i.color for i in rectlist])
                        break
                    if add_country_button.collidepoint(event.pos):
                        xlist = [i.name for i in countrylist]
                        if '红' not in xlist:
                            countrylist.append(Country('红',(255,0,0),0))
                            belong_grounds_counter['红'] = 0
                            colors_to_countries[(255,0,0)] = '红'
                            break
                        if '蓝' not in xlist:
                            countrylist.append(Country('蓝',(0,0,255),1))
                            belong_grounds_counter['蓝'] = 0
                            colors_to_countries[(0,0,255)] = '蓝'
                            break
                        if '绿' not in xlist:
                            countrylist.append(Country('绿',(0,255,0),2))
                            belong_grounds_counter['绿'] = 0
                            colors_to_countries[(0,255,0)] = '绿'
                            break
                        if '黄' not in xlist:
                            countrylist.append(Country('黄',(255,235,11),3))
                            belong_grounds_counter['黄'] = 0
                            colors_to_countries[(255,235,11)] = '黄'
                            break
                        if '青' not in xlist:
                            countrylist.append(Country('青',(11,255,255),4))
                            belong_grounds_counter['青'] = 0
                            colors_to_countries[(11,255,255)] = '青'
                            break
                        if '橙' not in xlist:
                            countrylist.append(Country('橙',(255,155,11),5))
                            belong_grounds_counter['橙'] = 0
                            colors_to_countries[(255,155,11)] = '橙'
                            break
                        if '紫' not in xlist:
                            countrylist.append(Country('紫',(230,11,255),6))
                            belong_grounds_counter['紫'] = 0
                            colors_to_countries[(230,11,255)] = '紫'
                            break
                        if '冰' not in xlist:
                            countrylist.append(Country('冰',(200,255,255),7))
                            belong_grounds_counter['冰'] = 0
                            colors_to_countries[(200,255,255)] = '冰'
                            break
                    for i in countrylist:
                        if i.flag_rect.collidepoint(event.pos):
                            choose_color = i.color
                            choose_belong_country = i.name
                        if i.delete_rect.collidepoint(event.pos):
                            choose_color = (0,0,0)
                            choose_belong_country = 'unbelong any country'
                            for j in rectlist:
                                if j.belong == i.name or j.color == i.color:
                                    j.belong = 'unbelong any country'
                                    j.color = (0,0,0)
                            del belong_grounds_counter[i.name]
                            countrylist.remove(i)
                            break
                    if delete_ground_button.collidepoint(event.pos):
                        mouseleftbutton_isdown = 'cleaning'
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
        elif mouseleftbutton_isdown == 'click':
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
        pygame.draw.rect(screen,(0,0,0),delete_ground_button,0)
        show_text('炸掉领土',(0,0,0),(840,303),19)
        pygame.draw.rect(screen,(11,255,64),output_button,0)
        show_text('导出数据',(0,0,0),(840,430),30)
        pygame.draw.rect(screen,(0,100,244),last_image_button,0)
        pygame.draw.rect(screen,(255,155,11),next_image_button,0)
        show_text('正在做第'+str(image_index)+'帧...',(0,0,0),(810,520),20)
        show_text('改上一帧',(255,255,255),(860,550),20)
        show_text('做下一帧',(0,0,0),(860,575),20)
        show_text(str(round(clock.get_fps(),1))+'/FPS',(0,0,0),(811,11),40)
        pygame.display.update()
        clock.tick()
    
    while part == 'view':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if upload_ijcafile_rect.collidepoint(event.pos):
                    root = Tk()
                    filename = tkinter.filedialog.askopenfilename(initialdir='C:/Users/'+user_name+'/学而思直播/code/cache/国家版图变化模拟器',title='选择ijca文件',filetypes=[("IJCA files","*.ijca")])
                    root.destroy()
                    root.mainloop()
                    if filename != '':
                        do_file_name_x = filename.split('/')[-1]
                        with open(filename,'r',encoding='utf-8') as f:
                            fdatac = f.read().replace('->','=')
                            f.close()
                        exec(fdatac)
                        img_fp_index = 1
                if upload_ijcafile_ok_rect.collidepoint(event.pos):
                    if do_file_name_x != None:
                        part = 'loading view things'
        screen.fill((255,255,255))
        screen.blit(upload_ijcafile_img,upload_ijcafile_rect)
        if do_file_name_x == None:
            show_text('上传ijca文件',(0,0,0),(11,11),50)
            show_text('还未上传ijca文件，也并未检测到任何ijca文件',(0,0,0),(400,11),25)
        else:
            show_text('重新上传文件',(0,0,0),(11,11),50)
            # show_text('确定(OK)',(0,0,0),upload_ijcafile_ok_rect,50)
            screen.blit(upload_ijcafile_img,upload_ijcafile_ok_rect)
            show_text('确定(OK)',(0,0,0),(11,81),50)
            show_text('文件名:'+do_file_name_x,(0,0,0),(400,11),20)
        pygame.display.update()
    
    while part == 'loading view things':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    view_speed = '手动'
                    part = 'start view ijca'
        screen.fill((221,221,221))
        screen.blit(upload_ijcafile_img,upload_ijcafile_rect)
        screen.blit(upload_ijcafile_img,upload_ijcafile_ok_rect)
        show_text('加载中...',(0,0,0),(11,11),50)
        show_text('正在转化文件',(0,0,0),(11,81),50)
        show_text('正在转化您的ijca文件为国家版图......',(0,0,0),(400,11),30)
        show_text('size屏幕大小转化完毕！',(0,0,0),(11,150),30)
        show_text('data导入完毕！',(0,0,0),(11,180),30)
        show_text('data数据转化为python代码完毕！',(0,0,0),(11,210),30)
        show_text('data运行完毕，且已经存储如数组。',(0,0,0),(11,240),30)
        show_text('优化格式完毕。准备绘制方格！按下空格键开始观看！',(0,0,0),(11,270),30)
        pygame.display.update()
    
    while part == 'start view ijca':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    img_fp_index = 0
                    part = 'mainpage'
                if event.key == pygame.K_n:
                    if img_fp_index == len(data):
                        part = 'mainpage'
                    else:
                        img_fp_index += 1
                if event.key == pygame.K_LEFT:
                    if view_speed == '手动':
                        view_speed = '自动'
                    elif view_speed == '半自动':
                        view_speed = '手动'
                    else:
                        view_speed = '半自动'
                    if view_speed != '手动':veiw_t = time()
                    break
                if event.key == pygame.K_RIGHT:
                    if view_speed == '手动':
                        view_speed = '半自动'
                    elif view_speed == '半自动':
                        view_speed = '自动'
                    else:
                        view_speed = '手动'
                    if view_speed != '手动':veiw_t = time()
                    break
        screen.fill((255,255,255))
        if time() - veiw_t > 1 and view_speed == '半自动':
            if img_fp_index == len(data):
                part = 'mainpage'
            else:
                img_fp_index += 1
                veiw_t = time()
        if time() - veiw_t > 0.4 and view_speed == '自动':
            if img_fp_index == len(data):
                part = 'mainpage'
            else:
                img_fp_index += 1
                veiw_t = time()
        for i in range(len(data[img_fp_index-1])):
            pygame.draw.rect(screen,data[img_fp_index-1][i],pygame.Rect(i//12*50,i%12*50,50,50),0)
        show_text(str(round(clock.get_fps(),1))+'/FPS',(0,0,0),(811,11),40)
        show_text('按左右键',(0,0,0),(811,51),40)
        show_text('调整帧播',(0,0,0),(811,91),40)
        show_text('放速度',(0,0,0),(811,131),40)
        show_text('按N下一帧',(0,0,0),(811,171),40)
        show_text('播放速度：',(0,0,0),(811,221),40)
        show_text(view_speed,(0,0,255),(811,261),40)
        show_text('R返回主页',(255,0,0),(811,301),40)
        pygame.display.update()
        clock.tick()