import pygame,random
import numpy as np

class wer:
    def __init__(self,x,y,z):#初始化
        self.x=np.array(x)
        self.y=np.array(y)
        self.z=np.array(z)
        self.scx=0
        self.scy=0
        self.scz=0
        self.dl=[]
    def XZr(self,xa,ya):#旋转
        y=self.y
        self.y=y*np.cos(xa)-self.z*np.sin(xa)
        self.z=y*np.sin(xa)+self.z*np.cos(xa)
        x=self.x
        self.x=x*np.cos(ya)+self.z*np.sin(ya)
        self.z=self.z*np.cos(ya)-x*np.sin(ya)
    def plTO(self,px,py,pz):#根据摄像机位置进行平移
        self.x=(self.x-px)
        self.y=(self.y-py)
        self.z=(self.z-pz)
    def plXZr(self,pxa,pya):#根据摄像机角度进行转换
        self.scy=self.y*np.cos(pxa)-self.z*np.sin(pxa)
        self.z=self.y*np.sin(pxa)+self.z*np.cos(pxa)
        self.scx=self.x*np.cos(pya)+self.z*np.sin(pya)
        self.scz=self.z*np.cos(pya)-self.x*np.sin(pya)
    def WZ3D(self,w,scx,scy):#根据倍率和窗口中心位置对图像进行平移然后投影
        dx=self.scx/self.scz*w+scx
        dy=self.scy/self.scz*w+scy
        self.dl=[[dx[i],dy[i]] for i in range(len(dx))]
        return self.dl

class polygon(wer):
    def __init__(self,screen,x,y,z,rgb,w):
        wer.__init__(self,x,y,z)
        self.cor,self.w = rgb,w
        self.screen = screen
    def draw(self):#与wer几乎唯一的区别就是自带渲染方法
        pygame.draw.polygon(self.screen, self.cor, self.dl, self.w)

class cube(wer):
    def __init__(self,screen,xl,yl,zl,rgb,w):
        x = [xl,-xl,-xl,xl,xl,-xl,-xl,xl]#[xl,-xl,-xl,xl,xl,xl,xl,xl,-xl,-xl,xl,xl,xl,-xl,-xl,xl,-xl,-xl,-xl,-xl,-xl,-xl,xl,xl]
        y = [yl,yl,-yl,-yl,yl,yl,-yl,-yl]#[yl,yl,-yl,-yl,yl,-yl,-yl,yl,yl,yl,yl,yl,yl,yl,-yl,-yl,yl,-yl,-yl,yl,-yl,-yl,-yl,-yl]
        z = [zl,zl,zl,zl,-zl,-zl,-zl,-zl]#[zl,zl,zl,zl,-zl,-zl,zl,zl,zl,-zl,-zl,zl,-zl,-zl,-zl,-zl,-zl,-zl,zl,zl,zl,-zl,-zl,zl]
        wer.__init__(self,x,y,z)
        self.cor,self.w = rgb,w
        self.screen = screen
    def draw(self):#与polygon类类似，但是渲染更复杂一点（以后打算整成数组）
        for i in range(2):
            pygame.draw.polygon(self.screen, self.cor[i*3], self.dl[i*4:i*4+4], self.w)
            pygame.draw.polygon(self.screen, self.cor[i*3+1], self.dl[i*2:i*2+2]+[self.dl[i*2+5]]+[self.dl[i*2+4]], self.w)
            pygame.draw.polygon(self.screen, self.cor[i*3+2], [self.dl[4-i*2]]+[self.dl[i*6]]+[self.dl[3+i*2]]+[self.dl[(7+i*2)%8]], self.w)

#程序示例：根据鼠标位置改变视角方向的同时使物体旋转
def drawd(linlx,linly,linlz,xa,ya,pxa,pya):#根据点列表以三角形绘制图像
    zhl4=cube(screen,666,666,666,[(i,i,i) for i in range(160,256,16)],0)
    zhl4.XZr(0,0)
    zhl4.plTO(-100,300,-2000)
    # print(xa,ya)
    zhl4.plXZr(pxa,pya)
    zhl4.WZ3D(800,500,500)
    zhl4.draw()
    zhl=cube(screen,500,500,500,[(255-i,(i+255)/2,i) for i in range(160,256,16)],0)
    zhl.XZr(xa,ya)
    zhl.plTO(0,0,-5000)
    # print(xa,ya)
    zhl.plXZr(pxa,pya)
    zhl.WZ3D(1000,400,400)
    zhl.draw()
    zhl2=cube(screen,500,500,500,[(i-50,i,100) for i in range(160,256,16)],0)
    zhl2.XZr(ya,xa)
    zhl2.plTO(200,200,-8000)
    # print(xa,ya)
    zhl2.plXZr(pya,pxa)
    zhl2.WZ3D(1000,400,400)
    zhl2.draw()
    zhl3=cube(screen,500,500,500,[((i+255)/2,255-i,i) for i in range(160,256,16)],0)
    zhl3.XZr(-ya,xa)
    zhl3.plTO(-100,300,-16000)
    # print(xa,ya)
    zhl3.plXZr(pxa,pya)
    zhl3.WZ3D(200,200,200)
    zhl3.draw()

pygame.init()
screen = pygame.display.set_mode((900,800))

dlx=[500,500,-500,-500,-500,-500,500,500,500,500,500,-500,-500,-500,-500,500]
dly=[-500,500,-500,500,-500,500,-500,500,-500,500,500,500,500,-500,-500,-500]
dlz=[500,500,500,500,-500,-500,-500,-500,500,500,500,500,-500,-500,-500,500]

xu=0
yu=0
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEMOTION:
            xu = (400-event.pos[0])/100
            yu = (event.pos[1]-400)/100
    drawd(dlx,dly,dlz,yu,xu,yu/8,xu/8)
    pygame.display.update()