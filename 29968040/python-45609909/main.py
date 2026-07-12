import os
import platform
from ccw_lib3d import *
import pygame,sys,codecs,copy
from PIL import Image
import numpy as np
dtype = [('x', float), ('y', float), ('z', float)]

opsystem_info = {
    'system_name': platform.system(),
    'username': os.getlogin(),
    'path': os.getcwd(),
}

grass_s=Image.open('grass s.png')
grass_t=Image.open('grass t.png')
grass_b=Image.open('grass b.png')

f=codecs.open('tpPoints.txt','r')
tpPoints=f.read().split('\n')#点的数组
f.close()
f=codecs.open('tpQuads.txt','r')
tpQuads=f.read().split('\n')#面的数组
f.close()
#面的数组的每一项包含多个数字，每个数字是指当前顶点在点数组的位置
for i in range(len(tpPoints)):
    tpPoints[i]=eval(tpPoints[i])
for i in range(len(tpQuads)):
    tpQuads[i]=eval(tpQuads[i])
tpPoints1=[]
tpQuads1=[]


aaaa=16
for i in range(len(tpQuads)):#图片光栅化处理，大概就是把每个面的正方形分成16*16的小正方形（图片就是16*16的）
    tpNowQuad=tpQuads[i]
    res=[[{} for i in range(aaaa+1)] for i in range(aaaa+1)]
    res[ 0][ 0]=tpPoints[tpNowQuad[0]-1]
    res[-1][ 0]=tpPoints[tpNowQuad[1]-1]
    res[-1][-1]=tpPoints[tpNowQuad[2]-1]
    res[ 0][-1]=tpPoints[tpNowQuad[3]-1]
    lenn=len(tpPoints1)
    for j in range(1,len(res)-1):
        res[j][ 0]['x']=res[0][ 0]['x']+(res[-1][ 0]['x']-res[0][ 0]['x'])*(j/aaaa)
        res[j][ 0]['y']=res[0][ 0]['y']+(res[-1][ 0]['y']-res[0][ 0]['y'])*(j/aaaa)
        res[j][ 0]['z']=res[0][ 0]['z']+(res[-1][ 0]['z']-res[0][ 0]['z'])*(j/aaaa)
        res[j][-1]['x']=res[0][-1]['x']+(res[-1][-1]['x']-res[0][-1]['x'])*(j/aaaa)
        res[j][-1]['y']=res[0][-1]['y']+(res[-1][-1]['y']-res[0][-1]['y'])*(j/aaaa)
        res[j][-1]['z']=res[0][-1]['z']+(res[-1][-1]['z']-res[0][-1]['z'])*(j/aaaa)
    for j in range(len(res)):
        tpPoints1.append(res[j][0])
        for k in range(1,len(res[j])-1):
            res[j][k]['x']=res[j][0]['x']+(res[j][-1]['x']-res[j][0]['x'])*(k/aaaa)
            res[j][k]['y']=res[j][0]['y']+(res[j][-1]['y']-res[j][0]['y'])*(k/aaaa)
            res[j][k]['z']=res[j][0]['z']+(res[j][-1]['z']-res[j][0]['z'])*(k/aaaa)
            tpPoints1.append(res[j][k])
        tpPoints1.append(res[j][-1])
    for j in range(len(res)-1):
        for k in range(len(res[j])-1):
            #    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
            #  0 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
            #  1 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
            #  2 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
            #j*17+k
            
            tpQuads1.append([j*(aaaa+1)+k+1+lenn,
                            j*(aaaa+1)+k+2+lenn,
                            (j+1)*(aaaa+1)+k+2+lenn,
                            (j+1)*(aaaa+1)+k+1+lenn])
tpColors=[]
tpQuads=copy.deepcopy(tpQuads1)
tpPoints=copy.deepcopy(tpPoints1)
def add_color(img):
    for y in range(16):
        for x in range(16):
            r, g, b,a = img.getpixel((x, y))
            tpColors.append((r,g,b))
add_color(grass_t)
add_color(grass_s)
add_color(grass_s)
add_color(grass_s)
add_color(grass_s)
add_color(grass_b)
tpColors=np.array(tpColors)
tpLight=vec3(5,5,-3)#还在研究，猜测是光源的位置

tpCenters=[]
tpQuadNormals=[]

for i in range(len(tpQuads)):
    tpNowQuad=tpQuads[i]#获取当前面信息
    
    #计算当前面的法线，并将其归一化（chatGPT的回答）
    tpQuadNormals.append(
        vec_normalize(
            vec3_cross(
                vec_sub(tpPoints[tpNowQuad[0]-1],tpPoints[tpNowQuad[1]-1]),
                vec_sub(tpPoints[tpNowQuad[0]-1],tpPoints[tpNowQuad[2]-1])
            )
        )
    )
    
    #这个地方使用了每个面顶点的xyz分别求平均值的方式计算面的中心点
    tpCenterTemp=tpPoints[tpNowQuad[0]-1]
    for j in range(1,len(tpNowQuad)):
        tpCenterTemp=vec_add(tpCenterTemp,tpPoints[tpNowQuad[j]-1])
    tpCenterTemp=vec_div(tpCenterTemp,vec3_fill(len(tpNowQuad)))
    tpCenters.append(tpCenterTemp)

def calculate_rgba(color):#sc颜色转rgb
    B = color % 256
    color = color // 256
    G = color % 256
    color = color // 256
    R = color % 256
    A = color // 256
    return (R, G, B, A)

tpQuads=np.array(tpQuads)
tpPoints=np.array([(d['x'],d['y'],d['z']) for d in tpPoints],dtype=dtype)
tpCenters=np.array([(d['x'],d['y'],d['z']) for d in tpCenters],dtype=dtype)
tpQuadNormals=np.array([(d['x'],d['y'],d['z']) for d in tpQuadNormals],dtype=dtype)
def Render(screen,xxx,yyy,can_color):#绘制部分已完全使用np
    global tpPoints,tpQuads,tpCenters,tpQuadNormals,tpLight
    #进行预处理,mat3返回一个数组，它把常用的旋转等计算预处理，在后续就不需要重复计算三角函数等
    #输入第一个是xyz缩放，第二个是旋转，第三个是平移
    tpMat=mat3({'x':1,'y':1,'z':1},vec3(xxx,yyy,0),{"x":0,"y":0,"z":6})
    tpPPoints=vec3_mulMat3(tpPoints,tpMat)
    tpPCenters=vec3_mulMat3(tpCenters,tpMat)#计算每个面中心点平移、缩放、旋转后的坐标
    tpPNormal=vec3_mulMat3(tpQuadNormals,tpMat)#在之前gpt的说法的基础上，这个应该是计算每个法线变换后的坐标
    tpPPointsProjected=vec2_project3d(tpPPoints,500)#对每个点透视投影
    sortt=np.argsort(tpPCenters,order='z')[::-1]
    screen.fill((255,255,255))
    for i in sortt:
        draw_points=tpPPointsProjected[tpQuads[i]-1]
        if can_color:
            pygame.draw.polygon(screen,tpColors[i],draw_points,width=0)#绘制
        else:
            pygame.draw.polygon(screen,(127,127,127),draw_points,width=2)#绘制


pygame.init()
screen = pygame.display.set_mode((640,360))
pygame.display.set_caption("3d立方体")
if opsystem_info['system_name'] == 'Windows':
    exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)")
else:
    print('非windows系统不一定支持哦')
    exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)")
clock=pygame.time.Clock()
can_color=1
in_down=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    xxx=-pygame.mouse.get_pos()[1]
    yyy=-pygame.mouse.get_pos()[0]
    if pygame.mouse.get_pressed()[0]:
        if in_down==0:
            can_color=not can_color
            in_down=1
    else:
        in_down=0
    Render(screen,xxx,yyy,can_color)
    show_text(f'FPS: {round(clock.get_fps())}',pos=(11,11),color=(0,0,0))
    pygame.display.update()
    clock.tick(60)