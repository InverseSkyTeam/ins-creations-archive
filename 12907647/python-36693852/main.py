from time import *
import cloudlib as clib
playerlist = eval(clib.read_from_cloud('站首云游-逆天城市-玩家名单',12907647))
user = input('输入游戏名(游戏的游玩名单上会记这个游戏名，只能输入常规符号、中英文数字，不要退格，想重输就重新运行)')
playerlook = 0

if user in playerlist:
    input('该玩家已经存在，回车直接进入游戏')
else:
    input('回车确定，玩家['+user+']将会被录入游戏名单')
    print('including...')
    playerlist.append(user)
    clib.save_to_cloud('站首云游-逆天城市-玩家名单',str(playerlist),12907647)
    print('Successful.')
    playerlook = 1

print('玩家列表:')
for i in playerlist:
    print(i)
print('我们，都是帮助扩建城市的工作者')
gamerelist = eval(clib.read_from_cloud('站首云游-逆天城市-游戏记录',12907647))

if playerlook == 1:
    sleep(0.5)
    print('欢迎新人来到此地。我是小轩，我来介绍一下这款游戏')
    print('''这是全站第一款联机游戏。这是大家不分好坏一起合作的游戏。这是一个快乐的游戏。
公元时间: 公元2430年
空间地点: 逆天恒星系|联梦星-逆天总国
          距离“标位|太阳恒星系|Earth-Fliem国”约3900秒差距
          (1秒差距约为3.26156378光年,ly)
我们要做的就是扩建逆天总国
来吧，一起肝！''')

print('游戏即将开始，请做好准备')
input('按下回车直接开始建国立业！！！')



from time import *
import pygame,sys,random
pygame.init()

screen = pygame.display.set_mode((1000,700))
pygame.display.set_icon(pygame.transform.smoothscale(pygame.image.load('INS.png'),(48,48)))
pygame.display.set_caption('逆天大国建造')

try:import ntpath
except:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)")
else:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)")
finally:pass

houselist = [pygame.image.load('image/houses/Level'+str(i)+'.png') for i in range(1,16)]
rightbox = pygame.Rect(800,0,200,700)

people = gamerelist[0]
money = gamerelist[1]

# test start
user = '逆天小轩-总统'
# test end

maxpeople = people

class Button:
    def __init__(self,text,m,x,y,p):
        self.text = text
        self.money = m
        self.rect = pygame.Rect(x,y,180,20)
        self.canbuy = 0
        self.n = 0
        self.people = p
    def draw(self,m):
        if m < self.money:
            pygame.draw.rect(screen,(166,166,166),self.rect,0)
            self.canbuy = 0
        else:
            pygame.draw.rect(screen,(238,238,238),self.rect,0)
            self.canbuy = 1
        pygame.draw.rect(screen,(1,1,1),self.rect,1)
        show_text(self.text+'/'+str(self.n),pos=self.rect,size=20)

X = 0
Y = 0

class House:
    def __init__(self,image):
        self.level = image
        self.img = houselist[image-1]
        self.rect = self.img.get_rect()
        self.rect.topleft = (random.randint(X,X+3200),random.randint(Y-400,Y+2800))
        self.P = self.rect.topleft
    def draw(self):
        screen.blit(self.img,self.rect)

buttonlist = []
buttonlist.append(Button('L1/1k币/1人',1000,810,100,1))
buttonlist.append(Button('L2/3k/3',3000,810,120,3))
buttonlist.append(Button('L3/5k/5',5000,810,140,5))
buttonlist.append(Button('L4/9k/10',9000,810,160,10))
buttonlist.append(Button('L5/1.7w/20',17000,810,180,20))
buttonlist.append(Button('L6/3m/3000',3000000,810,200,3000))
buttonlist.append(Button('L7/5m/5200',5000000,810,220,5200))
buttonlist.append(Button('L8/50m/6w',50000000,810,240,60000))
buttonlist.append(Button('L9/1.6亿/20w',160000000,810,260,200000))
buttonlist.append(Button('L10/2.5亿/30w',250000000,810,280,300000))
buttonlist.append(Button('L11/35亿/350w',3500000000,810,300,3500000))
buttonlist.append(Button('L12/100亿/8m',10000000000,810,320,8000000))
buttonlist.append(Button('L13/500亿/40m',50000000000,810,340,40000000))
buttonlist.append(Button('L14/0.3w亿/2.5亿',300000000000,810,360,250000000))
buttonlist.append(Button('L15/10w亿/50亿',10000000000000,810,380,5000000000))

drawhouselist = []

clock = pygame.time.Clock()
t = 1660990000
mapinfo = [0,0,800,700]

kl = 0
kr = 0
ku = 0
kd = 0

for i in gamerelist[2]:
    house = House(i[0])
    house.rect.x = i[1]
    house.rect.y = i[2]
    drawhouselist.append(house)
    buttonlist[i[0]-1].n += 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('关闭窗口')
            pygame.quit()
            print('关闭完成，正在保存数据...')
            l = [(i.level,i.P[0],i.P[1]) for i in drawhouselist]
            clib.save_to_cloud('站首云游-逆天城市-游戏记录','['+str(maxpeople)+','+str(money)+','+str(l)+']',12907647)
            print('保存完毕，退出游戏')
            sys.exit()
            # 退出游戏
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in buttonlist:
                if i.rect.collidepoint(event.pos):
                    if i.canbuy:
                        money -= i.money
                        i.n += 1
                        maxpeople += i.people
                        house = House(int(i.text.split('/')[0][1:]))
                        scaleinfo = mapinfo[2]/800
                        house.rect.width = round(house.rect.width/scaleinfo)
                        house.rect.height = round(house.rect.height/scaleinfo)
                        house.img = pygame.transform.scale(house.img,(house.rect.width,house.rect.height))
                        house.rect.x = round(house.rect.x/scaleinfo)
                        house.rect.y = round(house.rect.y/scaleinfo)
                        drawhouselist.append(house)
                        
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                if mapinfo[2] > 400:
                    for i in drawhouselist:
                        i.rect.width *= 2
                        i.rect.height *= 2
                        i.img = pygame.transform.scale(i.img,(i.rect.width,i.rect.height))
                        i.rect.x *= 2
                        i.rect.y *= 2
                    mapinfo[2] = int(mapinfo[2]/2)
                    mapinfo[3] = int(mapinfo[3]/2)
                break
            if event.key == ord('w'):
                if mapinfo[2] < 3200:
                    for i in drawhouselist:
                        i.rect.width = round(i.rect.width/2)
                        i.rect.height = round(i.rect.height/2)
                        i.img = pygame.transform.scale(i.img,(i.rect.width,i.rect.height))
                        i.rect.x = round(i.rect.x/2)
                        i.rect.y = round(i.rect.y/2)
                    mapinfo[2] *= 2
                    mapinfo[3] *= 2
                break
            if event.key == ord('p'):
                for i in drawhouselist:
                    if random.randint(0,1):
                        drawhouselist.remove(i)
                break
            if event.key == pygame.K_LEFT:
                kl = 1
                break
            if event.key == pygame.K_RIGHT:
                kr = 1
                break
            if event.key == pygame.K_UP:
                ku = 1
                break
            if event.key == pygame.K_DOWN:
                kd = 1
                break
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                kl = 0
                break
            if event.key == pygame.K_RIGHT:
                kr = 0
                break
            if event.key == pygame.K_UP:
                ku = 0
                break
            if event.key == pygame.K_DOWN:
                kd = 0
                break
    
    s = mapinfo[2]/800
    if kl:
        X += 5 * s
        for i in drawhouselist:
            i.rect.x += 5
    if kr:
        X -= 5 * s
        for i in drawhouselist:
            i.rect.x -= 5
    if ku:
        Y += 5 * s
        for i in drawhouselist:
            i.rect.y += 5
    if kd:
        Y -= 5 * s
        for i in drawhouselist:
            i.rect.y -= 5
    
    mapinfo[0] = int(X)
    mapinfo[1] = int(Y)
    
    screen.fill((222,255,255))
    
    for i in drawhouselist:
        i.draw()
    
    pygame.draw.rect(screen,(200,255,200),rightbox,0)
    
    if people < 10000:
        show_text('人口:'+str(people),pos=(800,0))
    elif people < 1000000:
        show_text('人口:'+str(round(people/10000,2))+'w',pos=(800,0))
    elif people < 100000000:
        show_text('人口:'+str(round(people/1000000,2))+'m',color=(0,200,160),pos=(800,0))
    elif people < 1000000000000:
        show_text('人口:'+str(round(people/100000000,2))+'亿',color=(160,200,11),pos=(800,0),size=20)
    else:
        show_text('人口:'+str(round(people/1000000000000,2))+'w亿',color=(235,179,3),pos=(800,0),size=20)
    
    if money < 10000:
        show_text('逆天币:'+str(money),pos=(800,30))
    elif money < 1000000:
        show_text('逆天币:'+str(round(money/10000,2))+'w',pos=(800,30))
    elif money < 100000000:
        show_text('逆天币:'+str(round(money/1000000,2))+'m',color=(0,200,160),pos=(800,30))
    elif money < 1000000000000:
        show_text('逆天币:'+str(round(money/100000000,2))+'亿',color=(160,200,11),pos=(800,30),size=20)
    else:
        show_text('逆天币:'+str(round(money/1000000000000,2))+'w亿',color=(235,179,3),pos=(800,30),size=20)
    
    show_text('购买房屋:',pos=(800,60))
    for i in buttonlist:
        i.draw(money)
    
    if people < 3:
        people = maxpeople
        money += 1
    elif people < 5:
        people = maxpeople
        money += 2
    elif people < 10:
        people = round(maxpeople*random.randint(90,100)/100)
        money += 3
    elif people < 10000:
        people = round(maxpeople*random.randint(85,95)/100)
        money = round(money+(people/3),1)
    elif people < 16000:
        people = round(maxpeople*random.randint(80,95)/100)
        money += 4000
    elif people < 1000000:
        people = round(maxpeople*random.randint(75,90)/100)
        money = round(money+(people/4),1)
    elif people < 100000000:
        people = round(maxpeople*random.randint(66,78)/100)
        money = round(money+(people/3.6))
    elif people < 1000000000: # 10亿
        people = round(maxpeople*random.randint(64,67)/100)
        money = round(money+(people/3.5))
    elif people < 3000000000:
        people = round(maxpeople*random.randint(71,73)/100)
        money = round(money+(people/3.4))
    elif people < 5000000000:
        people = round(maxpeople*0.718)
        money = round(money+(people/3.2))
    elif people < 7000000000:
        people = round(maxpeople*0.719)
        money = round(money+(people/3.4))
    elif people < 15000000000:
        people = round(maxpeople*0.72)
        money = round(money+(people/3.38))
    elif people < 60000000000:
        people = round(maxpeople*0.722)
        money = round(money+(people/3.37))
    else:
        people = round(maxpeople*0.731)
        money = round(money+(people/3.36))
    
    show_text('注:人数不会稳定',pos=(800,400),size=20)
    show_text('公元'+str(round((time()-t)/5)+2430)+'年',pos=(800,420),size=20)
    show_text('现实1分钟 游戏12年',color=(255,0,0),pos=(800,440),size=20)
    show_text('按q放大地图',color=(0,150,0),pos=(800,460),size=20)
    show_text('按w缩小地图',color=(0,150,0),pos=(800,480),size=20)
    show_text('地图大小:3200x2800',color=(0,150,0),pos=(800,500),size=20)
    show_text('缩放地图大小:',pos=(800,520),size=20)
    show_text(str(mapinfo[2])+'x'+str(mapinfo[3]),pos=(800,540),size=20)
    show_text('左上角坐标:'+str(-mapinfo[0])+','+str(mapinfo[1]),pos=(800,560),size=20)
    show_text('按p清理一些图像',pos=(800,580),size=20)
    show_text('(仅清除图像，不会有损失)',pos=(800,600),size=15)
    show_text('(不定时清除会内存不够)',color=(255,0,0),pos=(800,615),size=15)
    show_text('移动地图直接上下左右键',color=(255,0,0),pos=(800,630),size=15)
    show_text('退出游戏会自动存档',color=(0,0,255),pos=(800,645),size=15)
    pygame.display.update()
    clock.tick(60)