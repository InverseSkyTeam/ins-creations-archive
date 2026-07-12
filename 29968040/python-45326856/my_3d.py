import pygame,sys
import copy,math
import numpy as np
from PIL import Image
logo = Image.open('logo.png')
logo1 = Image.open('logo_2.png')
name1=Image.open('name_2.png')
name = Image.open('name.png')
rect_pic=Image.open('rect.png')
#透视变换
def calc_img(tr,dr,dl,tl,img,maxx,minx,maxy,miny):
    #tr,dr,dl,tl是四个角的坐标
    #print(tr,dr,dl,tl)
    def find_coeffs(pa, pb):
        matrix = []
        for p1, p2 in zip(pa, pb):
            matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
            matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])
        A = np.matrix(matrix, dtype=float)
        B = np.array(pb).reshape(8)
        res = np.dot(np.linalg.inv(A.T * A) * A.T, B)
        return np.array(res).reshape(8)
    width, height = int(maxx-minx)+1,int(maxy-miny)+1
    #print(width, height)
    coeffs = find_coeffs(
            [tl, tr, dr, dl],
            [(0, 0), (img.width, 0), (img.width, img.height), (0, img.height)])
    img1=img.copy()
    img1=img1.transform((width, height), Image.PERSPECTIVE, coeffs,
        Image.BICUBIC)
    return [img1.convert("RGBA").tobytes(),img1.size,img1.mode]

def draw_pic(plist,img):
    tl,dl,dr,tr=plist
    #tr,dr,dl,tl=plist
    res,minx,miny,maxx,maxy=cut([tr,dr,dl,tl])
    cc=calc_img(res[0],res[1],res[2],res[3],img,maxx,minx,maxy,miny)
    return [pygame.image.fromstring(cc[0],cc[1],cc[2]),minx,miny]
def cos(num):
    return math.cos(math.radians(num))
def sin(num):
    return math.sin(math.radians(num))
import time,sys
import webbrowser as wb
def ooO00OOoOo__():
    num=45326856
    num=int(num)
    try:
        OOooOo0Oo0=open(eval("b'\\x61\\x73\\x73\\x65\\x74'").decode()+'_info.json','r')#读取asset_info.json的内容
        OOooOo00o0=OOooOo0Oo0.read()
        OOooOo0Oo0.close()
        if int(OOooOo00o0[OOooOo00o0.find('"id":')+6:][:OOooOo00o0[OOooOo00o0.find('"id":')+6:].find(",")])!=num:#通过许多奇技淫巧代替re进行分析
            return int(OOooOo00o0)#如果是盗的作品，把输出函数改为一个错值，让程序报错，从而进入下面的excpet
        return sys.stdout#如果是原作，正常输出
    except:
        #输出提示信息
        print(chr(26816)+chr(27979)+chr(21040)+chr(36825)+chr(20010)+chr(20316)+chr(21697)+chr(26159)+chr(30423)+chr(21462)+chr(20182)+chr(20154)+chr(30340)+chr(20316)+chr(21697)+chr(65292)+chr(35831)+chr(21040)+chr(21407)+chr(20316)+chr(32773)+chr(32593)+chr(31449)+chr(19978)+chr(36816)+chr(34892))
        print(chr(51)+chr(31186)+chr(21518)+chr(33258)+chr(21160)+chr(36339)+chr(36716)+chr(33267)+chr(21407)+chr(20316)+chr(32773)+chr(32593)+chr(31449))
        time.sleep(2)
        #打开原作者网站
        wb.open(chr(104)+chr(116)+chr(116)+chr(112)+chr(115)+chr(58)+chr(47)+chr(47)+chr(99)+chr(111)+chr(100)+chr(101)+chr(46)+chr(120)+chr(117)+chr(101)+chr(101)+chr(114)+chr(115)+chr(105)+chr(46)+chr(99)+chr(111)+chr(109)+chr(47)+chr(104)+chr(111)+chr(109)+chr(101)+chr(47)+chr(112)+chr(114)+chr(111)+chr(106)+chr(101)+chr(99)+chr(116)+chr(47)+chr(100)+chr(101)+chr(116)+chr(97)+chr(105)+chr(108)+chr(63)+chr(108)+chr(97)+chr(110)+chr(103)+chr(61)+chr(99)+chr(111)+chr(100)+chr(101)+chr(38)+chr(112)+chr(105)+chr(100)+chr(61)+str(int(num))+chr(38)+chr(118)+chr(101)+chr(114)+chr(115)+chr(105)+chr(111)+chr(110)+chr(61)+chr(111)+chr(102)+chr(102)+chr(108)+chr(105)+chr(110)+chr(101)+chr(38)+chr(102)+chr(111)+chr(114)+chr(109)+chr(61)+chr(112)+chr(121)+chr(116)+chr(104)+chr(111)+chr(110)+chr(38)+chr(108)+chr(97)+chr(110)+chr(103)+chr(84)+chr(121)+chr(112)+chr(101)+chr(61)+chr(112)+chr(121)+chr(116)+chr(104)+chr(111)+chr(110))
        return sys.exit()

sys.stdout=ooO00OOoOo__()
print('',end='')   
#平行透视计算
def calc(p,xt,yt,fl=2):
    x,y,z=p
    x1=(cos(xt)*x-sin(xt)*y)*fl/2
    y1=cos(yt)*(cos(xt)*y+sin(xt)*x+sin(yt)*z)*fl/2
    return [x1,y1]

#计算圆（已废弃）
def calculate_circle_points(x0, y0, r, num_points,z):
    points = []
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points
        x = x0 + r * math.cos(angle)
        y = y0 + r * math.sin(angle)
        points.append((x, y,z))
    return points
    
#坐标转为canvas仿射变换数值（已废弃）
def p_to_skew(p0,p1,p2,p3,oldX,oldY,oldW,oldH):
    '''p0:左上
    p1:左下
    p2:右下
    p3:右上'''
    p=[p0,p1,p2,p3]
    e=p[0][0]
    f=p[0][1]
    y1=oldH
    x3=oldW
    c=(p[1][0]-e)/y1
    d=(p[1][1]-f)/y1
    a=(p[3][0]-e)/x3
    b=(p[3][1]-f)/x3
    return [a,b,c,d,e,f]

#裁切边缘
def cut(p):
    res=[]
    minx=9999
    miny=9999
    maxx=-9999
    maxy=-9999
    for i in p:
        minx=min(minx,i[0])
        miny=min(miny,i[1])
        maxx=max(maxx,i[0])
        maxy=max(maxy,i[1])
    for i in p:
        i1=copy.deepcopy(i)
        i1[0]-=minx
        i1[1]-=miny
        res.append(i1)
    return [res,minx,miny,maxx,maxy]

#外部边框
rect=[[-150,-150,0],
    [-150,150,0],
    [150,150,0],
    [150,-150,0]]
rect_tmp=copy.deepcopy(rect)
#logo边框
logo_rect=[
    [-76,-133,0],
    [-76,24,0],
    [76,24,0],
    [76,-133,0]
]
logo_tmp=copy.deepcopy(logo_rect)
#logo边框
logo_rect1=[
    [-76,-133,20],
    [-76,24,20],
    [76,24,20],
    [76,-133,20]
]
logo_tmp1=copy.deepcopy(logo_rect1)
#name边框
name_rect=[
    [-134,-150+182,0],
    [-134,-150+182+105,0],
    [134,-150+182+105,0],
    [134,-150+182,0]
]
name_tmp=copy.deepcopy(name_rect)
name_rect1=[
    [-134,-150+182,10],
    [-134,-150+182+105,10],
    [134,-150+182+105,10],
    [134,-150+182,10]
]
name_tmp1=copy.deepcopy(name_rect1)

aa,bb=-9,283+77/10

def my_3d(num):
    global rect_tmp,logo_tmp,rect,logo_rect
    aa1=aa+num
    bb1=bb+num*(77/10)
    for i in range(len(rect_tmp)):
        rect_tmp[i]=calc(rect[i],aa1,bb1)
        logo_tmp[i]=calc(logo_rect[i],aa1,bb1)
        name_tmp[i]=calc(name_rect[i],aa1,bb1)
        name_tmp1[i]=calc(name_rect1[i],aa1,bb1)
        logo_tmp1[i]=calc(logo_rect1[i],aa1,bb1)
    #tp=cut(name_tmp1)
    #td=cut(logo_tmp1)
    return [draw_pic(logo_tmp,logo),draw_pic(rect_tmp,rect_pic),draw_pic(name_tmp,name),draw_pic(name_tmp1,name1),draw_pic(logo_tmp1,logo1)]
