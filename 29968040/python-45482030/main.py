#这个是把ccw的代码复刻成python
#源码链接（sc）：https://www.ccw.site/gandi/project/63b14077aff9870d7bbef730?remixing=true
from ccw_lib3d import *
import pygame,sys,codecs
pygame.init()
screen = pygame.display.set_mode((640,360))
pygame.display.set_caption("3d茶壶旋转")
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
    
    
tpTime=0#y轴旋转角度，在这里也代表程序的时间
tpLight=vec3(5,5,-2)#还在研究，猜测是光源的位置
tpPPoints=[None for i in range(len(tpPoints))]
tpZs=[None for i in range(len(tpQuads))]
tpPPointsProjected=[None for i in range(len(tpPoints))]
tpQuadNormals=[]
tpCenters=[]
tpPNormal=[None for i in range(len(tpQuads))]
tpPCenters=[None for i in range(len(tpQuads))]
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
xxx1=65793
def teapotRender(screen,xxx):
    global tpTime,tpPoints,tpPPoints,tpQuads,tpCenters,tpQuadNormals,tpPPointsProjected,tpZs,tpPNormal,tpLight
    #进行预处理,mat3返回一个数组，它把常用的旋转等计算预处理，在后续就不需要重复计算三角函数等
    #输入第一个是xyz缩放，第二个是旋转，第三个是平移
    tpMat=mat3({'x':1,'y':1,'z':1},vec3(xxx,tpTime,0),{"x":0,"y":0,"z":6})
    for i in range(len(tpPoints)):#把计算所有点平移、缩放、旋转后的坐标
        #print(tpPoints[i],tpMat)
        tpPPoints[i]=vec3_mulMat3(tpPoints[i],tpMat)
    for i in range(len(tpQuads)):
        tpPCenters[i]=vec3_mulMat3(tpCenters[i],tpMat)#计算每个面中心点平移、缩放、旋转后的坐标
        tpZs[i]=tpPCenters[i]['z']#存储每个面中心点的z坐标，后续需要进行排序
        tpPNormal[i]=vec3_mulMat3(tpQuadNormals[i],tpMat)#在之前gpt的说法的基础上，这个应该是计算每个法线变换后的坐标
    for i in range(len(tpPPoints)):#对每个点透视投影
        tpPPointsProjected[i]=vec2_project3d(tpPPoints[i],500)
    tpOrder=sorted(tpZs, reverse=True)#对每个面中心点z进行排序
    screen.fill((255,255,255))
    for i in range(len(tpQuads)):
        tpChoice=tpZs.index(tpOrder[i])#查找排序后这个面中心点在排序前的位置
        tpNowQuad=tpQuads[tpChoice]#获取当前面
        color=int(number_dot(tpPNormal[tpChoice],tpLight)*15)#在之前gpt的说法的基础上，应该是使用点积计算当前颜色的明暗程度
        color=max(min(color,255),0)*65537#我也不知道啥意思
        draw_points=None
        for j in range(len(tpNowQuad)):#获取当前面顶点位置
            tpProjectPoint=tpPPointsProjected[tpNowQuad[j]-1]
            if j==0:
                draw_points=[[tpProjectPoint['x']+320,180-tpProjectPoint['y']]]
            else:
                draw_points.append([tpProjectPoint['x']+320,180-tpProjectPoint['y']])
        pygame.draw.polygon(screen,calculate_rgba(color),draw_points)#绘制
        tpZs[tpChoice]='r'#标记为已查找，防止重复
    tpTime+=10
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    '''if pygame.mouse.get_pressed()[0]:
        xxx1-=1
        print(xxx1)'''
    xxx=pygame.mouse.get_pos()[1]
    teapotRender(screen,xxx//5)
    pygame.display.update()
    pygame.time.Clock().tick(30)
    #sc还是太逊了，ccw编译模式+加速模式+60fps还没pg的30fps快