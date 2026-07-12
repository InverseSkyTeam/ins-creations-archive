#{
from blls import*
from defs import*
from lyl_THW import*
import tkinter,sys,os,sae,math,winsound
from PIL import Image,ImageTk
import numpy as np
from copy import deepcopy
gamdp,wortp,seedp,ds,worldname,pbgm = None,None,None,1,"new_world",1

def vatovb(a,b,c):
    if a < b:
        a+= c
        if a > b:
            a = b
    elif a > b:
        a-=c
        if a < b:
            a = b
    return a
def bgm_player(pu,sd = [0,262,294,330,349,392,440,494]):
    global pbgm
    while 1:
        for i in pu:
            if pbgm:
                if i[0]<=0:pass
                else:
                    winsound.Beep(sd[i[0]],i[1])
            time.sleep(i[1]/250)
#指令函数{
def c_tp(cmd,bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl,vsa,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,printing,wwws):
    bex = int(cmd[2])//20*20
    bey = int(cmd[3])//20*20
    pl.cx = int(cmd[2])%20*40
    pl.cy = int(cmd[3])%20*40
    seet,bl,rbl,bgxl,dw,bex,bey,pl.cx,pl.cy,subl,noi7,flxl,engx,lzl = chqk(bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl.cx,pl.cy,vsa,4,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,lzl,printing,wwws)
    print("log：已将玩家传送到",cmd[2],cmd[3])
    return seet,bl,rbl,bgxl,dw,bex,bey,pl,subl,noi7,flxl,engx
def c_fill(cmd,jgqk,bex,bey,jgsj,poq,flbl,xbpo):
    bxe = int(cmd[2])//20*20
    bye = int(cmd[3])//20*20
    ebx = int(cmd[2])%20
    eby = int(cmd[3])%20
    jgqk[("fq",bxe+ebx,bye-eby,cmd[4])][19-eby+ebx*20]=[int(cmd[5])]
    seet = [jgqk[("fq",bex-1*20+i//3*20,bey-1*20+i%3*20,jgsj)] for i in range(9)]
    bl = rtbl(seet,poq,flbl,xbpo)
    print("log：已将",cmd[4],"视界的",cmd[2],cmd[3],"处方块替换为",cmd[5])
    return seet,bl
def c_gamd(cmd,pl):
    if cmd[2] in {"1","2","3"}:
        gamd=cmd[2]
        pl.fly = 0
        print("log：已将玩家游戏模式更新为",cmd[2])
    else:print("输入错误")
    return gamd,pl
def c_tosj(cmd,bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl,vsa,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,printing,wwws):
    if cmd[2] in ["0","1"]:
        jgsj = int(cmd[2])
        seet,bl,rbl,bgxl,dw,bex,bey,pl.cx,pl.cy,subl,noi7,flxl,engx,lzl = chqk(bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl.cx,pl.cy,vsa,4,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,lzl,printing,wwws)
        print("log：已将玩家传输到",cmd[2],"视界")
    else:print("输入错误")
    return seet,bl,rbl,bgxl,dw,bex,bey,pl,subl,noi7,flxl,engx,jgsj
def c_setmt(cmd):
    timeste = float(cmd[2])
    return timeste
def c_give(cmd,jgqk,bex,bey,pl,dw):
    if int(cmd[2])>0 and int(cmd[3])>0:
        dwf = saixy(jgqk,pl.cx,pl.cy,0,0,20,20,0,0,0)
        dw.append([int(cmd[2]),dwf,0,int(cmd[3])])
    return dw
def c_kill(pl):
    pl.hp=-1
def c_getdata(cmd):
    print(blokl[int(cmd[2])]())
def c_lview(lv):
    lv = 1-lv
    return lv
def c_buildst(cmd,stel,rbg,bex,bey,jgqk,seed,rbl,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl,vsa,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,printing,wwws):
    stuu = {"su":[int(cmd[3]),int(cmd[4]),stel[int(cmd[2])][2],int(cmd[5])]}
    rbg += getat5(stuu)
    seet,bl,rbl,bgxl,dw,bex,bey,pl.cx,pl.cy,subl,noi7,flxl,engx,lzl = chqk(bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl.cx,pl.cy,vsa,4,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,lzl,printing,wwws)
    return rbg,seet,bl,rbl,bgxl,dw,bex,bey,pl,subl,noi7,flxl,engx
def c_shtxt(cmd,shtl):
    sdu = [cmd[2],(int(cmd[3]),int(cmd[4])),(int(cmd[5]),int(cmd[6]),int(cmd[7])),int(cmd[8])]
    shtl.append(sdu)
    return shtl
#}
for i in range(110):
    blokl[i]()
def lerpmx(x,plist):
    for i in range(1,len(plist)):
        if x<plist[i][0]:
            return plist[i-1][1]+(plist[i][1]-plist[i-1][1])*(x-plist[i-1][0])/(plist[i][0]-plist[i-1][0])
    return -1
def fint(t):
    t=t%120
    a头=0
    a右上=lerpmx(t,[(0,20),(60,-20),(120,20)])
    a左上=lerpmx(t,[(0,-20),(60,20),(120,-20)])
    a右下=lerpmx(t,[(0,40),(60,-20),(120,40)])
    a左下=lerpmx(t,[(0,-20),(60,40),(120,-20)])
    a右大腿=lerpmx(t,[(0,-20),(60,20),(120,-20)])
    a左大腿=lerpmx(t,[(0,20),(60,-20),(120,20)])
    a右小腿=lerpmx(t,[(0,-20),(40,-20),(60,20),(120,-20)])
    a左小腿=lerpmx(t,[(0,20),(60,-20),(100,-20),(120,20)])
    return a右上,a左上,a右下,a左下,a头,a右大腿,a左大腿,a右小腿,a左小腿
def main():
    global fl,rl,kcl,vrl,vpl,iui,cgxl,fdbl,tiel,poq,flbl,flpoq,wql,libp,sqai,sdai,stel,swqx,swqf,noul,lipoq,stepoq,ds,gamdp,wortp,seedp,worldname,fgul,pbgm,wengao,labnm
    timeste = 0.016
    sys.path.append(r'./mods')
    modslist = list(os.walk(r'./mods'))[0][2]
    modslistu = []
    for i in modslist:
        if i[-3:] == ".py":
            exec("import "+i[0:-3])
            print(i+"载入中")
            try:
                modsa = eval(i[0:-3]+".initdic")
                print("插件作者："+modsa["writer"])
                modslistu.append(i[0:-3])
            except:
                print("mod："+i+" 不是mod")
    modslist = modslistu
    mods_data = {}
    for i in modslist:
        modsa = eval(i+".initdic")
        mods_data[modsa["name"]]=[]
        if "game_init" in modsa["run_at"]:
            try:
                tset = modsa["run_at"]["game_init"]
                exec(tset[1]+"="+i+".init("+tset[0]+")")
            except:
                print("mod："+i+" 不规范")
    class cbuuu():
        def __init__(self,E2,top2):
            self.txt=None
            self.E2=E2
            self.top2=top2
        def cmdj(self):
            self.txt = self.E2.get()
            self.E2.select_clear()
            self.top2.destroy()
        def ink(self):
            self.txt = self.E2.get()
            self.E2.select_clear()
    kl = {"a或←":"向左移动","d或→":"向右移动","w或↑":"向上跳跃","s或↓":"向下飞行","鼠标左键":"挖掘方块或者在背包中拖动物品","鼠标右键":"放置方块或食用食物或浏览文稿或抛投射物","f12":"打开详细信息","1~9":"从左到右第1~9格物品栏格","0、u、i、o":"第10~13格物品栏格","q键":"打开物品栏","e键":"拆包物品","空格键":"开启飞行","m键":"抛弃物品","c键":"打开指令输入框","b键":"存档","r键":"查看成就界面"}
    dul = ''
    for a in kl:
        dul+= "{"+a+"："+kl[a]+"}\n"
    bex = 0
    bey = 0
    wuy = ["1","2","3"]
    top = tkinter.Tk()
    top.title('隐匿世界-1.2.1')
    top.geometry("500x400+0+0")
    li = {'按键操作列表':dul,'详细更新介绍':sae.txd}
    class chose:
        def __init__(self,txt):self.txt=txt
        def cbuse(self):
            toop = tkinter.Tk()
            fuue=tkinter.Label(toop, text=self.txt)
            fuue.pack()
            toop.mainloop()
        def se(self,toop,listb,listb2,e1,e2):
            self.toop,self.listb,self.listbt,self.e1,self.e2 = toop,listb,listb2,e1,e2
        def cbdato(self):
            global gamdp,wortp,seedp,ds,worldname
            try:
                gamdp = wuy[self.listb.curselection()[0]]
            except:gamdp = None
            try:
                wortp = wuy[self.listbt.curselection()[0]]
            except:wortp = None
            worldname = self.e2.get()
            seedp = self.e1.get()
            self.toop.destroy()
            top.destroy()
            ds=0
    def cbda():
        toop = tkinter.Tk()
        fuue4=tkinter.Label(toop, text="世界名称：")
        E2 = tkinter.Entry(toop)
        E2.insert(0,worldname)
        fuue=tkinter.Label(toop, text="游戏模式：")
        listb  = tkinter.Listbox(toop,exportselection=0)
        liky = ["探险模式","建筑模式","测试模式"]
        for item in liky:
            listb.insert("end",item)
        fuue2=tkinter.Label(toop, text="世界类型：")
        listb2  = tkinter.Listbox(toop,exportselection=0)
        liky2 = ["随机世界","陡峭世界","平坦世界"]
        for item in liky2:
            listb2.insert("end",item)
        fuue3=tkinter.Label(toop, text="世界种子：")
        E1 = tkinter.Entry(toop)
        snn = chose("")
        snn.se(toop,listb,listb2,E1,E2)
        Kk = tkinter.Button(toop, text ="设置完成", command = snn.cbdato)
        fuue4.pack()
        E2.pack()
        fuue.pack()
        listb.pack()
        fuue2.pack()
        listb2.pack()
        fuue3.pack()
        E1.pack()
        Kk.pack()
        toop.mainloop()
    im_root = ImageTk.PhotoImage(Image.open(r'images/封面.PNG'))
    canvas_root = tkinter.Canvas(top, width=500, height=300)
    canvas_root.create_image(250, 100, image=im_root)
    canvas_root.pack()
    for item in li:
        fgf = chose(li[item])
        B = tkinter.Button(top, text = item, command = fgf.cbuse)
        B.pack()
    B = tkinter.Button(top, text = '开始游戏', command = cbda)
    B.pack()
    top.mainloop()
    if ds:return 0
    gamd,wort,seed = gamdp,wortp,seedp
    if len(seed) < 12:
        seed = str(random.randint(111111111111,999999999999))
    if gamd not in ["1","2","3"]:
        gamd = "1"
    if wort not in ["1","2","3"]:
        wort = "1"
    pygame.init()#初始化pygame
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('隐匿世界-1.2.1')
    pygame.display.set_icon(image1)  #设置图标
    class scpr:
        def __init__(self,w):
            self.txt = pygame.font.SysFont("SimHei",w)
        def pr(self,a,r,g,b,x,y):
            txt_fmt = self.txt.render(a,1,(r,g,b))
            screen.blit(txt_fmt,(x,y))
    def fsk(xlt,ylt,a):return -math.cos(a/180*math.pi)*xlt-math.sin(a/180*math.pi)*ylt,math.sin(a/180*math.pi)*xlt-math.cos(a/180*math.pi)*ylt
    class Somite:
        def __init__(self,img,rcx,rcy,tx=0,ty=0,fol=1,top=0):
            self.img = img
            self.nodes = []
            self.rcx = rcx
            self.rcy = rcy
            rxy = img.get_size()
            self.tx = -rxy[0]/2-rcx+tx
            self.ty = -rxy[1]/2-rcy+ty
            self.a = 0
            self.fol = fol
            self.ot = 0
            self.top = top
        def rot(self,a):
            self.a=a
            c = fsk(self.rcx,self.rcy,self.a)
            img = pygame.transform.rotate(self.img,self.a)
            rxy = img.get_size()
            self.tx=-rxy[0]/2+c[0]
            self.ty=-rxy[1]/2+c[1]
        def draw(self,x,y):
            img = pygame.transform.rotate(self.img,self.a)
            screen.blit(img,(x+self.tx,y+self.ty))
            for i in self.nodes:
                i[0].draw(x+i[1][0],y+i[1][1])
        def drawself(self,x,y):
            img = pygame.transform.rotate(self.img,self.a)
            screen.blit(img,(x+self.tx,y+self.ty))
        def drawfol(self,x,y):
            we = self.get_willdraw(x,y)
            we.update({self.fol:[self,(self.tx+x,self.ty+y)]})
            for i in range(max(1,min(we)),max(we)+1):
                try:
                    g = we[i][0]
                    img = pygame.transform.rotate(g.img,g.a)
                    screen.blit(img,(we[i][1][0],we[i][1][1]))
                except:pass
            try:
                g = we[-1][0]
                img = pygame.transform.rotate(g.img,g.a)
                screen.blit(img,(we[-1][1][0],we[-1][1][1]))
            except:pass
        def get_willdraw(self,x,y):
            if self.top==1:
                a={-1:[self,[x+self.tx,y+self.ty]]}
            else:
                a={self.fol:[self,[x+self.tx,y+self.ty]]}
            for i in self.nodes:
                a.update(i[0].get_willdraw(x+i[1][0],y+i[1][1]))
            return a
        def rotal(self,rcx,rcy,a):
            e = a-self.a
            self.a+=e
            c = fsk(self.rcx,self.rcy,self.a)
            rxy2 = self.img.get_size()
            rxl = [0]*4
            ryl = [0]*4
            rxl[1],ryl[1] = fsk(rxy2[0],rxy2[1],self.a)
            rxl[2],ryl[2] = fsk(rxy2[0],0,self.a)
            rxl[3],ryl[3] = fsk(0,rxy2[1],self.a)
            rxy2 = max(rxl)-min(rxl),max(ryl)-min(ryl)
            self.tx=-rxy2[0]/2+c[0]
            self.ty=-rxy2[1]/2+c[1]
            for i in self.nodes:
                i[0].rotal(rcx+i[1][0],rcy+i[1][1],i[0].a+e)
                i[1]=fsk(-i[2][0],-i[2][1],self.a)
        def appendson(self,som):
            self.nodes.append([som,(som.tx,som.ty),(som.tx,som.ty)])
        def overturn(self,fol=None):
            if not fol:fol=self.fol
            self.fol = 2*fol-self.fol
            self.ot=1-self.ot
            self.img = pygame.transform.flip(self.img, True, False)
            rxy = self.img.get_size()
            for i in self.nodes:
                i[0].overturn(fol)
                i[2] = (-i[2][0],i[2][1])
    
    class pe:
        def __init__(self,txt,t,string,w):
            self.txt,self.t,self.string,self.w = txt,t,string,w
        def pr_r(self,rgb,x,y,speed=5,ak=255):
            string = self.string[0:int(self.t//speed)]
            for i in range(0,len(string),11):
                txt_fmt = self.txt.render(string[i:min(i+11,len(string))],1,rgb)
                txt_fmt.set_alpha(ak)
                screen.blit(txt_fmt,(x,y+i//11*20))
            if self.t<len(self.string)*speed:self.t+=1
        def pr_d(self,rgb,x,y,t,speed=30):
            a = dafs(self.t,speed,t)
            string = self.string
            for i in range(0,len(string),600//self.w):
                txt_fmt = self.txt.render(string[i:min(i+600//self.w,len(string))],1,rgb)
                txt_fmt.set_alpha(a)
                screen.blit(txt_fmt,(x,y+i//(600//self.w)*self.w))
            if self.t<=t:self.t+=1
    
    class prac:
        def __init__(self,w):
            self.txt = pygame.font.SysFont("SimHei",w)
            self.w = w
        def pr_init(self,a):
            return pe(self.txt,0,a,self.w)
    som1 = Somite(imgau1t,0,0,0,0,6)
    som2 = Somite(imgau3t,0,-12.5*0.7,6*0.7,22.5*0.7,5)
    som3 = Somite(imgau2t,0,-12.5*0.7,6*0.7,22.5*0.7,8)
    som4 = Somite(imgau3t,0,-12.5*0.7,6*0.7,-20*0.7,4)
    som5 = Somite(imgau2t,0,-12.5*0.7,6*0.7,-20*0.7,9)
    som7 = Somite(imgau3t,0,-12.5*0.7,5*0.7,25*0.7,3)
    som8 = Somite(imgau2t,0,-12.5*0.7,5*0.7,25*0.7,10)
    som9 = Somite(imgau3t,0,-12.5*0.7,5*0.7,25*0.7,2)
    som10 = Somite(imgau2t,0,-12.5*0.7,5*0.7,25*0.7,11)
    som6 = Somite(imgau3t,0,12.5*0.7,6*0.7,0,7)
    som1.appendson(som5)
    som5.appendson(som10)
    som1.appendson(som4)
    som4.appendson(som9)
    som1.appendson(som6)
    som1.appendson(som2)
    som1.appendson(som3)
    som2.appendson(som7)
    som3.appendson(som8)
    #som11 = Somite(img1,0,0,30,75,8)
    #som1.appendson(som11)
    def un(bl,seet,pl,k_t,seed,vsa,mbx,be,xg,xut,yut,bgf,lzl,t,msd,jgqk,bex,bey,sx,sy,ba,tk,f12,la,rbl,gamd,uie,dw,sai,xf,t2,bgxl,fdbl,flxl,wql,sut,jdd,engx,noul,jgsj,nst,xbpo,lv,shtl,stg,subl,weather,temp,plwg,old_hp,rrr1,rrr2,rrr3,rrr4,rrr5,rrr6,printing,drct,wwws):#渲染函数，地图和实体
        mt = scpr(20)
        if la<=99.9 and stg>0:
            la+=0.1
            stg-=0.01
        if pl.hp<=99.9 and stg>0:
            pl.hp+=0.05
            stg-=0.005
        if gamd == "1":
            if la>100:
                la = 100
                cee = pl.ktu(k_t,bex,bey,jgsj,jgqk)
                for s in cee:
                    if s == 1:
                        la-=4
                        temp+=0.1
                    else:
                        la-=0.105
                        temp+=0.003
            elif la<10:pass
            else:
                cee = pl.ktu(k_t,bex,bey,jgsj,jgqk)
                for s in cee:
                    if s == 1:
                        la-=4
                        temp+=0.1
                    else:
                        la-=0.105
                        temp+=0.003
        else:
            la=100
            cee = pl.ktu(k_t,bex,bey,jgsj,jgqk)
            for s in cee:
                if s == 1:
                    la-=4
                    temp+=0.1
                else:
                    la-=0.105
                    temp+=0.003
        dda = pl.ret(bex,bey,jgsj,jgqk)
        pl.gof(bex,bey,jgsj,jgqk)
        vsa.rtu(mbx,bex,bey,jgsj,jgqk)
        vsa.ret(bex,bey,jgsj,jgqk)
        see1 = seet[0]
        u_cx=pl.cx
        u_cy=pl.cy
        wedr = []
        for xi in range(21):
            px = xi*40-(u_cx+410)%40
            for yi in range(16):
                py = yi*40-(u_cy-365)%40
                uttt=seet[int((u_cx+410+xi*40)//40//20*3+1-(u_cy-365+yi*40)//40//20)][int((u_cx+410+xi*40)//40%20*20+19-(u_cy-365+yi*40)//40%20)]
                uttt.blit(screen,px,py)
                if uttt.id==108:
                    xt,yt = px-390,py-365
                    xc = int((xt+10+pl.cx)//40)
                    yc = int((yt+15+pl.cy)//40)
                    xq = xc//20*20
                    yq = yc//20*20
                    aqqqc = ((bex+xq)+xc%20,(bey-yq)-yc%20-1)
                    if aqqqc in printing:
                        imgtq_s=pygame.transform.scale(imglist[108][0][uttt.data],(120,120))
                        screen.blit(imgtq_s,(px-80,py-80))
        for i in set(wedr):
            usin = pygame.transform.scale(i[0],(160,160))
            screen.blit(usin,(i[1],i[2]))
        if lv:
            for xi in range(-20,41):
                px = xi*2-(u_cx+410)%2+720
                for yi in range(-10,31):
                    py = yi*2-(u_cy-365)%2+540
                    bdd = ("fq",bex+int((u_cx+410+xi*40-800)//800)*20,bey-int((u_cy-365+yi*40)//800)*20,jgsj)
                    if bdd in jgqk:
                        uttt=jgqk[bdd][int((u_cx+410+xi*40)//40%20*20+19-(u_cy-365+yi*40)//40%20)]
                        if uttt.id!=0:
                            uttt.blit(screen,px,py,(2,2))#screen.blit(pygame.transform.scale(imglist[uttt.id],(2,2)),(px,py))
        for ix in range(12):
            screen.blit(img0s,(ix*32+208,568))
            try:
                screen.blit(imglist[be[ix]][1],(ix*32+214,574))
                if blokl[be[ix]]().tooltp==-1:
                    mt.pr(str(ba[ix]),0,0,0,ix*32+214,574)
                elif blokl[be[ix]]().tooltp==-3:
                    mt.pr(str(lab[ba[ix]]),0,0,0,ix*32+214,574)
                else:
                    whi = pygame.Rect(ix*32+210,568, 2, 32*ba[ix]/blokl[be[ix]]().todness)
                    pygame.draw.rect(screen, (15, 15, 255), whi, 0)
            except:
                pass
        xk = pygame.Rect(208+xg*32, 568, 32, 32)
        pygame.draw.rect(screen, (50, 50, 50), xk, 2)
        #player = pygame.Rect(390, 365, 24, 72)
        #pygame.draw.rect(screen, (64, 128, 64), player, 10)
        
        a1,a2,a3,a4,a5,a6,a7,a8,a9=fint(t)
        som1.rotal(0,0,0)
        som2.rotal(0,0,a6*drct)#大腿
        som3.rotal(0,0,a7*drct)
        som4.rotal(0,0,a1*drct)#大臂
        som5.rotal(0,0,a2*drct)
        som7.rotal(0,0,a8*drct)#小腿
        som8.rotal(0,0,a9*drct)
        som9.rotal(0,0,a3*drct)#小臂
        som10.rotal(0,0,a4*drct)
        som6.rotal(0,0,a5*drct)#头
        som1.drawfol(400,400)
        
        #screen.blit(imgpl,(390,365))
        s1s = pygame.Rect(vsa.cx-pl.cx+390, vsa.cy-pl.cy+365, 20, 30)
        pygame.draw.rect(screen, (64, 64, 128), s1s, 10)
        #screen.blit(imgs1,(x2-pl.cx+390,y2-pl.cy+365))
        xutu = int((xut+pl.cx%40+10)//40)
        yutu = int((yut+pl.cy%40-5)//40)
        if xf != 0:
            screen.blit(imglist[xf][1],(xut-10,yut-10))
        if gamd == "1":
            plh = pygame.Rect(0, 2, 16, old_hp*2.96)
            pygame.draw.rect(screen, (255, 255, 255), plh, 0)
            plh = pygame.Rect(0, 2, 16, pl.hp*2.96)
            pygame.draw.rect(screen, (200, 15, 15), plh, 0)
            old_hp+= (pl.hp-old_hp)*0.05
            plhk = pygame.Rect(0, 0, 20, 300)
            pygame.draw.rect(screen, (0, 0, 0), plhk, 5)
            pa = pygame.Rect(2, 302, 16, int(la*2.96))
            pygame.draw.rect(screen, (200, 175, 15), pa, 0)
            pak = pygame.Rect(0, 300, 20, 300)
            pygame.draw.rect(screen, (0, 0, 0), pak, 4)
            if pl.ogen !=100:
                pas = pygame.Rect(22, 2, 16, int(pl.ogen*2.96))
                pygame.draw.rect(screen, (64, 128, 255), pas, 0)
                pask = pygame.Rect(20, 0, 20, 300)
                pygame.draw.rect(screen, (0, 0, 0), pask, 4)
            if pl.ogen <= 0:
                pl.hp-=random.randint(1,4)/5
            pas = pygame.Rect(22, 302, 16, int(stg*2.96))
            pygame.draw.rect(screen, (255, 128, 16), pas, 0)
            pask = pygame.Rect(20, 300, 20, 300)
            pygame.draw.rect(screen, (0, 0, 0), pask, 4)
            if stg <= 0:
                pl.hp-=random.randint(1,4)/10
            screen.blit(temp_img,(200,536))
            tmh = pygame.Rect(205, 550, min(10,max(0,temp-30))*390/10, 4)
            pygame.draw.rect(screen, (255, 0, 0), tmh, 0)
            if not 30<temp<40 and t%30==0:
                pl.hp-=random.randint(5,10)
        bzsh = pygame.Rect(rrr3,rrr4, 40, 40)
        pygame.draw.rect(screen, (255, 255, 255), bzsh, 2)
        xc = rrr5
        yc = rrr6
        xq = xc//20*20
        yq = yc//20*20
        seeu = jgqk[("fq",bex+xq,bey-yq,jgsj)]
        if seeu[int(xc%20*20+19-yc%20)].id!=0:
            bv = seeu[int(xc%20*20+19-yc%20)].hardness
            bre = seeu[int(xc%20*20+19-yc%20)].bltype
        else:
            tk = 0
        if msd == 0:
            tk = 0
        else:
            if xc == sx and yc == sy:
                if la>=10:
                    if seeu[int(xc%20*20+19-yc%20)].id!=0:
                        if gamd == "1" :
                            if xf != 0:
                                if blokl[xf]().tooltp == bre:
                                    tk+=blokl[xf]().toolve
                                else:
                                    tk+=1
                            else:
                                tk+=1
                        else:
                            tk+=999999999999
                        la-=0.105
                        if seeu[int(xc%20*20+19-yc%20)].id!=0:
                            if bv <= tk:
                                f = seeu[int(xc%20*20+19-yc%20)]
                                if f.id==45 or f.id==82:
                                    jdd.pop((bex+xq,bey-yq,xc%20*20+19-yc%20,jgsj))
                                elif f.id==86 or f.id==92:
                                    del patl[(bex+xq,bey-yq,xc%20*20+19-yc%20,jgsj)]
                                lbd,lbn,seeu[int(xc%20*20+19-yc%20)] = f.brok(blokl[xf]())
                                bgxl,flxl,engx = cou((bex+xq)+xc%20,(bey-yq)-yc%20-1,bgxl,flxl,engx,jgsj)
                                '''
                                seeu[int(xc%20*20+19-yc%20)]=blokl[0]()
                                jgqk[("fq",bex+xq,bey-yq,jgsj)] = seeu
                                '''
                                bgxl,dw,flxl,engx=getat4(jgqk,bgxl,fdbl,poq,noul,dw,flxl,engx,bex,bey,printing)
                                dw+= [[lbd[i],saixy(jgqk,(xq+xc%20)*40+10,10-(yq-yc%20)*40,random.randint(-5,5),random.randint(1,5),20,20,0,0,0),0,lbn[i]] for i in range(len(lbd))]
                                seet = [jgqk[("fq",bex-1*20+i//3*20,bey-1*20+i%3*20,jgsj)] for i in range(9)]
                                bl = rtbl(seet,poq,flbl,xbpo)
                                if gamd=='1':
                                    if xf != 0:
                                        if blokl[xf]().tooltp != -1:
                                            ba[xg] -= 1
                                            if ba[xg] == 0:
                                                be[xg] = 0
                            else:
                                pj = pygame.Rect(rrr3+20-int(tk/bv*20),rrr4+20-int(tk/bv*20), int(tk/bv*40), int(tk/bv*40))
                                pygame.draw.rect(screen, (25, 50, 25), pj, 2)
                else:
                    tk = 0
            else:
                tk = 0
        if seet[(xq//20+1)*3+2-(yq//20+1)][xc%20*20+19-yc%20].id == 13:
            mp = scpr(30)
            txt = seet[(xq//20+1)*3+2-(yq//20+1)][xc%20*20+19-yc%20].txt
            ia = 0
            for ika in range(len(txt)//20):
                af = txt[ia:ia+20]
                mp.pr(af,255,255,255,100,300-len(txt)//20*15+ia//20*30)
                ia+=20
            af = txt[ia:-1]+txt[-1]
            mp.pr(af,255,255,255,400-len(af)*15,300-len(txt)//20*15+ia//20*30)
        if f12 == 1:
            mt.pr("坐标：x："+str(bex+pl.cx/40)+"y："+str(bey-pl.cy/40),255,255,255,0,0)
            mt.pr("区块内坐标：x："+str(pl.cx/40)+"y："+str(0-pl.cy/40),255,255,255,0,20)
            mt.pr("区块序号：x："+str(bex//20)+"y："+str(bey//20),255,255,255,0,40)
            mt.pr("方块id："+str(seeu[int(xc%20*20+19-yc%20)]),255,255,255,0,60)
            if seeu[int(xc%20*20+19-yc%20)].id!=0:
                mt.pr("方块名称："+seeu[int(xc%20*20+19-yc%20)].name,255,255,255,0,80)
            try:
                mt.pr("方块硬度："+str(bv),255,255,255,0,100)
                mt.pr("方块挖掘进度："+str(tk/bv),255,255,255,0,120)
            except:
                pass
            if t1-t2>0:
                mt.pr("运算帧率："+str(1/(t1-t2)),255,255,255,0,140)
            mt.pr("世界种子："+seed,255,255,255,0,160)
            mt.pr("玩家血量："+str(pl.hp),255,255,255,0,180)
            mt.pr("玩家体力："+str(la),255,255,255,0,200)
            mt.pr("玩家氧气："+str(pl.ogen),255,255,255,0,220)
        fre = 0
        while fre<len(sai):#实体模拟
            if -1600<=sai[fre][1].cx<2400-sai[fre][1].cw and -1600<=sai[fre][1].cy<2400-sai[fre][1].ch:
                xi = sai[fre][1].cx-pl.cx+390
                yi = sai[fre][1].cy-pl.cy+365
                if sai[fre][4]!=1:
                    sai[fre][2] = sai[fre][1].rtu(sai[fre][2],bex,bey,jgsj,jgqk)
                else:
                    if (pl.cx-sai[fre][1].cx)**2+(pl.cy-sai[fre][1].cy)**2<360000:
                        sai[fre][1].fight(bex,bey,jgsj,jgqk,pl)
                    else:
                        sai[fre][2] = sai[fre][1].rtu(sai[fre][2],bex,bey,jgsj,jgqk)
                if sai[fre][4]=="#":sai[fre][1].gof(bex,bey,jgsj,jgqk)
                sai[fre][1].ret(bex,bey,jgsj,jgqk)
                if sai[fre][4]=="#":screen.blit(sdai[sai[fre][0]][4],(xi,yi))
                else:screen.blit(sqai[sai[fre][0]][4],(xi,yi))
                if msd==1 and xi-10<=xut<=xi+sai[fre][1].cw+10 and yi-10<=yut<=yi+sai[fre][1].ch+10 and time.perf_counter()-sut>=0.7:
                    sai[fre][1].hp-=wql[xf]
                    sut=time.perf_counter()
                    for i in range(4):
                        if len(lzl)<50:
                            lzl.append([1,saixy(jgqk,sai[fre][1].cx+20,sai[fre][1].cy+20,random.randint(-20,20),random.randint(1,10),4,4,0,0,0),0,0,0,time.time(),(255,0,0)])
                    sai[fre][2]+= -5 if pl.cx>sai[fre][1].cx else 5
                    sai[fre][1].cx+= -5 if pl.cx>sai[fre][1].cx else 5
                if sai[fre][1].hp<=0:
                    xcd = sai[fre][1].cx//40
                    ycd = sai[fre][1].cy//40
                    dwf = saixy(jgqk,sai[fre][1].cx,sai[fre][1].cy,random.randint(-5,5),random.randint(1,5),20,20,0,0,0)
                    dw.append([sai[fre][3],dwf,0,random.randint(1,2)])
                    sai.pop(fre)
                    fre-=1
            elif (-4000<=sai[fre][1].cx<4800 and -4800<=sai[fre][1].cy<5400)==False:
                sai.pop(fre)
                fre-=1
            fre+=1
        fre = 0
        while fre<len(subl):#投掷物模拟
            subl[fre][3] -= 1
            if -1600<=subl[fre][1].cx<2400-subl[fre][1].cw and -1600<=subl[fre][1].cy<2400-subl[fre][1].ch:
                xi = subl[fre][1].cx-pl.cx+390
                yi = subl[fre][1].cy-pl.cy+365
                ewew = subl[fre][1].ret(bex,bey,jgsj,jgqk)
                if ewew and subl[fre][0] not in {109,110}:
                    subl[fre][1].cxv,subl[fre][1].cyv = 0,0
                    if subl[fre][0]==103:
                        seet,bl,rbl,bgxl,dw,bex,bey,pl,subl,noi7,flxl,engx,lzl = boom(5,subl[fre][1].cx,subl[fre][1].cy,bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl,vsa,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,bl,lzl,printing,wwws)
                        subl.pop(fre)
                        continue
                if subl[fre][0]==110:
                    screen.blit(imglist[110][0],(xi-10,yi-5))
                    lzl.append([8,(subl[fre][1].cx+8,subl[fre][1].cy+60),0,0,0,time.time(),(255,255,225)])
                else:
                    a = math.atan(subl[fre][1].cxv/subl[fre][1].cyv if subl[fre][1].cyv!=0 else subl[fre][1].cxv/0.00000001)/math.pi*180+90
                    if subl[fre][1].cxv<0:a=180+a
                    imgf = pygame.transform.rotate(imglist[subl[fre][0]][0],a)
                    screen.blit(imgf,(xi,yi))
                if subl[fre][0]==96:
                    for i in range(len(sai)):
                        dxi = sai[i][1].cx-pl.cx+390
                        dyi = sai[i][1].cy-pl.cy+365
                        if dxi<=xi+20<=dxi+sai[i][1].cw and dyi<=yi+20<=dyi+sai[i][1].ch:
                            if subl[fre][0] == 96:
                                sai[i][1].hp-=abs(complex(subl[fre][1].cxv,subl[fre][1].cyv))*wql[subl[fre][0]]
                                for i in range(4):
                                    if len(lzl)<50:
                                        lzl.append([1,saixy(jgqk,subl[fre][1].cx+20,subl[fre][1].cy+20,random.randint(-20,20),random.randint(1,10),4,4,0,0,0),0,0,0,time.time(),(255,0,0)])
                                subl.pop(fre)
                                fre-=1
                                break
                            elif subl[fre][0] == 103:
                                seet,bl,rbl,bgxl,dw,bex,bey,pl,subl,noi7,flxl,engx,lzl = boom(5,subl[fre][1].cx,subl[fre][1].cy,bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl,vsa,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,bl,lzl,printing,wwws)
                elif pl.cx<=subl[fre][1].cx+20<=pl.cx+pl.cw and pl.cx<=subl[fre][1].cy+20<=pl.cx+pl.ch and subl[fre][3]<3730:
                    if subl[fre][0] == 96:
                        pl.hp-=abs(complex(subl[fre][1].cxv,subl[fre][1].cyv))*wql[subl[fre][0]]
                        for i in range(4):
                            if len(lzl)<50:
                                lzl.append([1,saixy(jgqk,subl[fre][1].cx+20,subl[fre][1].cy+20,random.randint(-20,20),random.randint(1,10),4,4,0,0,0),0,0,0,time.time(),(255,0,0)])
                    elif subl[fre][0] == 103:
                        seet,bl,rbl,bgxl,dw,bex,bey,pl,subl,noi7,flxl,engx,lzl = boom(5,subl[fre][1].cx,subl[fre][1].cy,bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl,vsa,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,bl,lzl,printing,wwws)
                    else:continue
                    subl.pop(fre)
                    fre-=1
                elif (-4000<=xi<4800 and -4800<=yi<5400)==False:
                    subl.pop(fre)
                    fre-=1
                elif subl[fre][3]<0:
                    if subl[fre][0] == 109:
                        seet,bl,rbl,bgxl,dw,bex,bey,pl,subl,noi7,flxl,engx,lzl = boom(7,subl[fre][1].cx,subl[fre][1].cy,bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl,vsa,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,bl,lzl,printing,wwws)
                    elif subl[fre][0] == 110:# 烟花粒子生成
                        seet,bl,rbl,bgxl,dw,bex,bey,pl,subl,noi7,flxl,engx,lzl = boom(2,subl[fre][1].cx,subl[fre][1].cy,bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl,vsa,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,bl,lzl,printing,wwws)
                        for i in yanhua[subl[fre][2]]:
                            lzl.append([9,saixy(jgqk,subl[fre][1].cx+2,subl[fre][1].cy+4,i[0]+subl[fre][1].cxv,i[1]+subl[fre][1].cyv,8,8,0,0,0,0.7,0.7,1.3,0,0.7),0,0,0,240,i[2]])
                    subl.pop(fre)
                    fre-=1
            fre+=1
        bgr = 0
        while bgr<len(dw):#掉落物模拟
            xi = dw[bgr][1].cx-pl.cx+390
            yi = dw[bgr][1].cy-pl.cy+365
            if -1600<=dw[bgr][1].cx<2400-dw[bgr][1].cw and -1600<=dw[bgr][1].cy<2400-dw[bgr][1].ch:
                dw[bgr][1].ret(bex,bey,jgsj,jgqk)
                screen.blit(imglist[dw[bgr][0]][1],(xi,yi))
                if blokl[dw[bgr][0]]().tooltp == -1:
                    mt.pr(str(dw[bgr][3]),0,0,0,xi,yi)
                if 370<=xi<=414 and 355<=yi<=447:
                    be,ba,dn,lo = jq2(be,ba,dw[bgr][0],dw[bgr][3])
                    if lo!=0:
                        dw[bgr][3] = lo
                    elif dn == 1:
                        m_ = dw.pop(bgr)
                        bgr-=1
            rt_ = 0
            while rt_<len(dw):
                xmn = dw[rt_][1].cx-pl.cx+390
                ymn = dw[rt_][1].cy-pl.cy+365
                if rt_!=bgr%len(dw) and xi-40<xmn<xi+60 and yi-40<ymn<yi+60 and dw[rt_][0] == dw[bgr][0] and blokl[dw[bgr][0]]().tooltp==-1:
                    dw[bgr][3] = dw[bgr][3]+dw[rt_][3]
                    f2 = dw.pop(rt_)
                    rt_-=1
                    if rt_<bgr:
                        bgr-=1
                rt_+=1
            bgr+=1
        lz = 0
        while lz<len(lzl):#没错，粒子效果！
            if lzl[lz][0] in {1,9}:
                xi = lzl[lz][1].cx-pl.cx+390
                yi = lzl[lz][1].cy-pl.cy+365
            elif lzl[lz][0]==8:
                xi = lzl[lz][1][0]-pl.cx+390
                yi = lzl[lz][1][1]-pl.cy+365
            else:
                xi = lzl[lz][1]-bex*40
                yi = bey*40-lzl[lz][2]
            if lzl[lz][0] == 9:lzi = pygame.Rect(xi, yi, 8, 8)
            else:lzi = pygame.Rect(xi, yi, 4, 4)
            pygame.draw.rect(screen, lzl[lz][6], lzi, 0)
            if -800<=xi<1580 and -800<=yi<1580:
                if lzl[lz][0]==1:
                    if time.time()-lzl[lz][5]<=1:
                        lzl[lz][1].ret(bex,bey,jgsj,jgqk)
                    else:
                        lzl.pop(lz)
                        lz-=1
                elif lzl[lz][0]==2:
                    xclz = int(lzl[lz][1]//40-bex)
                    yclz = int(bey-lzl[lz][2]//40)
                    xqlz = xclz//20*20
                    yqlz = yclz//20*20
                    seeulz = jgqk[("fq",bex+xqlz,bey-yqlz,jgsj)]
                    if seeulz[int(xclz%20*20+19-yclz%20)][0] not in poq:
                        lzl.pop(lz)
                        lz-=1
                    else:
                        lzl[lz][1],lzl[lz][2] = lzl[lz][1]+lzl[lz][3],lzl[lz][2]+lzl[lz][4]
                elif lzl[lz][0]==9:
                    if lzl[lz][5]>=0:
                        lzl[lz][5]-= 1
                        lzl[lz][1].ret(bex,bey,jgsj,jgqk)
                        lzl.append([8,(lzl[lz][1].cx+2,lzl[lz][1].cy+2),0,0,0,time.time(),lzl[lz][6]])
                    else:
                        lzl.pop(lz)
                        lz-=1
                elif lzl[lz][0]==8:
                    if time.time()-lzl[lz][5]<=0.2:
                        lzl[lz][6]=(int(lzl[lz][6][0]*0.9),int(lzl[lz][6][1]*0.9),int(lzl[lz][6][2]*0.9))
                    else:
                        lzl.pop(lz)
                        lz-=1
            else:
                lzl.pop(lz)
                lz-=1
            lz+=1
        inv = 0
        while inv<len(shtl):
            try:
                shtl[inv][3]-= 1
                mt.pr(shtl[inv][0],shtl[inv][2][0],shtl[inv][2][1],shtl[inv][2][2],shtl[inv][1][0],shtl[inv][1][1])
                if shtl[inv][3]<0:
                    shtl.pop(inv)
                    inv-=1
                inv+=1
            except:
                print("erro：文字显示错误")
                shtl.pop(inv)
        mt = scpr(50)
        if plwg:
            screen.blit(wgbg_img,(100,100))
            yse = 300-len(wengao)*25
            for i in wengao:
                mt.pr(i,128,128,128,400-len(i)*25,yse)
                yse+= 50
        if weather == "sunny":
            temp = vatovb(temp,37,0.005)
        elif weather == "raining":
            temp = vatovb(temp,30,0.006)
            if t%6==0 and len(lzl)<100:
                rx = random.randint(-400,1199)
                lzl.append([2,bex*40+rx+pl.cx-390,bey*40+500-pl.cy+365,0,-10,time.time(),(0,0,128)])
        elif weather == "train":
            temp = vatovb(temp,30,0.008)
            if t%3==0 and len(lzl)<100:
                rx = random.randint(-400,1199)
                lzl.append([2,bex*40+rx+pl.cx-390,bey*40+500-pl.cy+365,0,-15,time.time(),(0,0,128)])
        elif weather == "snow":
            temp = vatovb(temp,20,0.008)
            if t%6==0 and len(lzl)<100:
                rx = random.randint(-400,1199)
                lzl.append([2,bex*40+rx+pl.cx-390,bey*40+500-pl.cy+365,0,-8,time.time(),(255,255,255)])
        temp = vatovb(temp,37,0.003)
        temp = vatovb(temp,37+bex*0.006,0.003)
        for ekf in dda:#视界折跃
            gg = seet[ekf[1]//20*3+2-ekf[0]//20][ekf[1]%20*20+19-ekf[0]%20].id
            if gg == 79 and t%128 == 0:
                jgsj = 1-jgsj
                rbg.append([air(),u_cx//40,19-u_cy//40,bex,bey,1,jgsj])
                rbg.append([air(),u_cx//40,19-u_cy//40-1,bex,bey,1,jgsj])
                rbg.append([blokl[1](),u_cx//40,19-u_cy//40-2,bex,bey,1,jgsj])
                seet,bl,rbl,bgxl,dw,bex,bey,pl.cx,pl.cy,subl,noi7,flxl,engx,lzl = chqk(bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl.cx,pl.cy,vsa,4,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,lzl,printing,wwws)
        return pl,lzl,xc,yc,seet,tk,bl,la,rbl,dw,sai,ba,be,bgxl,flxl,sut,jdd,engx,jgsj,nst,shtl,stg,subl,temp,old_hp

    def outwel(jgqk,seet,jdd,cx,cy,uie,shtl,bex,bey,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl,vsa,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,bl,noi7,timeste,lv):
        asss = []
        for oi in jdd:
            if abs(bex-oi[0])<=40 and abs(bey-oi[1])<=40:
                oue = jgqk[("fq",oi[0],oi[1],oi[3])][oi[2]]
                if oue.id==45:
                    ql,qg,qh,qha,ex,ekk,sal,sag=oue.data
                    if ekk[0]>=ekk[1] and ekk[1]!=0:
                        ekk[0]=0
                    if ql in vpl:
                        if ekk[3]>=vpl[ql][2] and ekk[2]>=vpl[ql][1] and (sal==vpl[ql][0] or sal==0):
                            if sag<255:
                                qg-=1
                                sal=vpl[ql][0]
                                sag+=1
                                if qg==0:
                                    ql=0
                                ekk[3]=0
                            elif sag==255:
                                ekk[3]=vpl[ql][2]
                        elif ekk[3]>=vpl[ql][2]*0.8 and ekk[2]<vpl[ql][1]:
                            ekk[3]=vpl[ql][2]*0.8
                        elif ekk[3]>=vpl[ql][2] and (sal!=vpl[ql][0] and sal!=0):
                            ekk[3]=vpl[ql][2]
                    else:
                        ekk[3]=0
                    if ekk[0]==0:
                        if ql in vpl and qh in vrl and (sal==vpl[ql][0] or sal==0) and vrl[qh][0]<=1200:
                            qha-=1
                            ekk[1]=vrl[qh][1]
                            ekk[2]=vrl[qh][0]
                            ekk[0]=1
                            ekk[3]+=1
                            if qha==0:
                                qh=0
                        else:
                            ekk[3]=0
                    else:
                        ekk[0]+=1
                        ekk[3]+=1
                        if uie==0:
                            px=(oi[0]-bex+oi[2]//20)*40-cx+400
                            py=(oi[1]-bey-oi[2]%20)*40-cy+1135
                            screen.blit(img15_s,(px,py))
                    jgqk[("fq",oi[0],oi[1],oi[3])][oi[2]].data=[ql,qg,qh,qha,ex,ekk,sal,sag]
                elif oue.id==82:
                    li = [oi[0]+oi[2]//20,oi[1]-20+oi[2]%20,oi[3]]
                    try:
                        y4,y1,y2,y3,y5,y6,y7,y8,me,mek,mel = getyb(jgqk,li)
                        if max([sein(y1,0),sein(y2,1),sein(y3,2),sein(y4,3)])>0:
                            shtl,seet,bl,rbl,bgxl,jgqk,dw,bex,bey,pl,subl,noi7,flxl,engx,timeste,lv = oue.data[1].pnext(shtl,bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl,vsa,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,lv,seet,bl,noi7,timeste)
                        else:
                            oue.data[1].i=0
                    except:print("警告：代码错误")
                else:
                    asss.append(oi)
        for i in asss:
            jdd.pop(i)
        return seet,shtl,bl,rbl,bgxl,dw,bex,bey,pl,subl,noi7,flxl,engx,timeste,lv

    def outpat(jgqk,patl,cx,cy):
        for oi in list(patl.keys()):
            if abs(bex-oi[0])<=40 and abs(bey-oi[1])<=40:
                oue = jgqk[("fq",oi[0],oi[1],oi[3])][oi[2]]
                if oue.id==86:
                    xw,yw = oi[2]//20,oi[2]%20+1
                    yw2 = oi[2]%20-1
                    if jgqk[("fq",oi[0],oi[1]+yw//20*20,oi[3])][xw*20+yw%20].id==0:
                        oue.data[0]+= random.randint(0,1)
                        if oue.data[0] > oue.data[1]:
                            xw,yw = oi[2]//20,oi[2]%20+1
                            yw2 = oi[2]%20-1
                            if jgqk[("fq",oi[0],oi[1]+yw2//20*20,oi[3])][xw*20+yw2%20].id!=86:
                                oue.data[0]=0
                                jgqk[("fq",oi[0],oi[1]+yw//20*20,oi[3])][xw*20+yw%20] = blokl[86]()#[oue[0],0,oue[2]]
                                patl[(oi[0],oi[1]+yw//20*20,xw*20+yw%20,oi[3])] = 86
                    else:
                        oue.data[0] = 0
                elif oue.id==92:
                    xw,yw = oi[2]//20,oi[2]%20+1
                    yw2 = oi[2]%20-1
                    if oue.data[0]<oue.data[1]:
                        oue.data[0]+= random.randint(0,1)

    class UIw():
        def __init__(self,be,ba,nul,xut,yut,hj,fr,jy,lab,labnm):
            self.be=be
            self.ba=ba
            self.nul=nul
            self.xut=xut
            self.yut=yut
            self.hj=hj
            self.fr=fr
            self.jy=jy
            self.lab=lab
            self.labnm=labnm
            self.kaa=[]
        
        def __drawww(self,ec,ac,x,y,img0s):
            screen.blit(img0s,(x-6,y-6))
            if ec!=0 and ac!=0:
                screen.blit(imglist[ec][1],(x,y))
                if blokl[ec]().tooltp==-1:
                    mt.pr(str(ac),0,0,0,x,y)
                elif blokl[ec]().tooltp==-3:
                    self.kaa.append((str(self.lab[ac]),x,y))
                else:
                    whi = pygame.Rect(x-6,y-6, 2, 32*ac/blokl[ec]().todness)
                    pygame.draw.rect(screen, (15, 15, 255), whi, 0)
        
        def it(self):
            x = self.xut
            y = self.yut
            if self.jy == 1:
                if self.hj==0 and self.fr==0:
                    if 0<=(x-208)//32<12 and (y-574)//32==0:
                        l = (x-208)//32
                        ob = sdw(self.be,self.ba,self.hj,self.fr,l)
                        self.be,self.ba,self.hj,self.fr = ob.unpu()
                    elif 0<=(x-208)//32<12 and 0<=(y-400)//32<4:
                        l = (x-208)//32*4+12+(y-400)//32
                        ob = sdw(self.be,self.ba,self.hj,self.fr,l)
                        self.be,self.ba,self.hj,self.fr = ob.unpu()
                else:
                    if 0<=(x-208)//32<12 and (y-574)//32==0:
                        l = (x-208)//32
                        ob = sdw(self.be,self.ba,self.hj,self.fr,l)
                        self.be,self.ba,self.hj,self.fr = ob.unpd()
                    elif 0<=(x-208)//32<12 and 0<=(y-400)//32<4:
                        l = (x-208)//32*4+12+(y-400)//32
                        ob = sdw(self.be,self.ba,self.hj,self.fr,l)
                        self.be,self.ba,self.hj,self.fr = ob.unpd()
            elif self.nul != []:
                x1 = self.nul[0]
                y1 = self.nul[1]
                if self.hj==0 and self.fr==0:
                    if 0<=(x1-208)//32<12 and (y1-574)//32==0:
                        l = (x1-208)//32
                        if self.be[l] != 0:
                            self.hj = self.be[l]
                            self.fr = self.ba[l]
                            self.be[l] = 0
                            self.ba[l] = 0
                    elif 0<=(x1-208)//32<12 and 0<=(y1-400)//32<4:
                        l = (x1-208)//32*4+12+(y1-400)//32
                        if self.be[l] != 0:
                            self.hj = self.be[l]
                            self.fr = self.ba[l]
                            self.be[l] = 0
                            self.ba[l] = 0
                else:
                    if 0<=(x1-208)//32<12 and (y1-574)//32==0:
                        l = (x1-208)//32
                        ob = sdw(self.be,self.ba,self.hj,self.fr,l)
                        self.be,self.ba,self.hj,self.fr = ob.pdo()
                    elif 0<=(x1-208)//32<12 and 0<=(y1-400)//32<4:
                        l = (x1-208)//32*4+12+(y1-400)//32
                        ob = sdw(self.be,self.ba,self.hj,self.fr,l)
                        self.be,self.ba,self.hj,self.fr = ob.pdo()
            mt = scpr(20)
            for ix in range(12):
                try:
                    self.__drawww(self.be[ix],self.ba[ix],ix*32+214,574,img0s)
                except:
                    pass
            for ix in range(12):
                for iy in range(4):
                    try:
                        self.__drawww(self.be[ix*4+12+iy],self.ba[ix*4+12+iy],ix*32+214,406+iy*32,imgns)
                    except:
                        pass
            if 0<=(x-208)//32<12 and (y-574)//32==0:
                l = (x-208)//32
                if self.be[l]!=0:
                    mt.pr(blokl[self.be[l]]().name,0,0,0,x,y-20)
            elif 0<=(x-208)//32<12 and 0<=(y-400)//32<4:
                l = (x-208)//32*4+12+(y-400)//32
                if self.be[l]!=0:
                    mt.pr(blokl[self.be[l]]().name,0,0,0,x,y-20)
            return self.be,self.ba,self.hj,self.fr
        
        def plan(self,hl,hg,fl,mh,mla):
            x = self.xut
            y = self.yut
            if self.jy == 1:
                if self.hj==0 and self.fr==0:
                    if 0<=(x-368)//32<2 and 0<=(y-264)//32<2:
                        l = (x-368)//32*2+(y-264)//32
                        ob = sdw(hl,hg,self.hj,self.fr,l)
                        hl,hg,self.hj,self.fr = ob.unpu()
                    elif 0==(x-384)//32 and 0==(y-328)//32:
                        ob = sdw([mh],[mla],self.hj,self.fr,0)
                        [mh],[mla],self.hj,self.fr = ob.unpu()
                else:
                    if 0<=(x-368)//32<2 and 0<=(y-264)//32<2:
                        l = (x-368)//32*2+(y-264)//32
                        ob = sdw(hl,hg,self.hj,self.fr,l)
                        hl,hg,self.hj,self.fr = ob.unpd()
                    elif 0==(x-384)//32 and 0==(y-328)//32:
                        ob = sdw([mh],[mla],self.hj,self.fr,0)
                        [mh],[mla],self.hj,self.fr = ob.unpd()
            elif self.nul != []:
                x1 = self.nul[0]
                y1 = self.nul[1]
                if self.hj==0 and self.fr==0:
                    if 0<=(x1-368)//32<2 and 0<=(y1-264)//32<2:
                        l = (x1-368)//32*2+(y1-264)//32
                        if hl[l] != 0:
                            self.hj = hl[l]
                            self.fr = hg[l]
                            hl[l] = 0
                            hg[l] = 0
                    elif 0==(x1-384)//32 and 0==(y1-328)//32:
                        if mh != 0:
                            self.hj = mh
                            self.fr = mla
                            mh = 0
                            mla = 0
                    elif 384<=x1<416 and 232<=y1<264:
                        if str(hl) in fl:
                            hl,hg,self.hj,self.fr,mh,mla,self.lab = hcxs(fl,hl,hg,self.hj,self.fr,mh,mla,self.lab,self.labnm)
                else:
                    if 0<=(x1-368)//32<2 and 0<=(y1-264)//32<2:
                        l = (x1-368)//32*2+(y1-264)//32
                        ob = sdw(hl,hg,self.hj,self.fr,l)
                        hl,hg,self.hj,self.fr = ob.pdo()
                    elif 0==(x1-384)//32 and 0==(y1-328)//32:
                        ob = sdw([mh],[mla],self.hj,self.fr,0)
                        [mh],[mla],self.hj,self.fr = ob.pdo()
                    elif 384<=x1<416 and 232<=y1<264:
                        if str(hl) in fl:
                            hl,hg,self.hj,self.fr,mh,mla,self.lab = hcxs(fl,hl,hg,self.hj,self.fr,mh,mla,self.lab,self.labnm)
            mt = scpr(20)
            for ix in range(2):
                for iy in range(2):
                    try:
                        self.__drawww(hl[ix*2+iy],hg[ix*2+iy],ix*32+374,270+iy*32,imgns)
                    except:
                        pass
            self.__drawww(mh,mla,390,334,imgns)
            screen.blit(imgns,(384,232))
            if str(hl) in fl:
                screen.blit(imglist[fl[str(hl)][0]][1],(390,238))
                mt.pr(blokl[fl[str(hl)][0]]().name,0,0,0,390,212)
                if fl[str(hl)][1][0]!=0:
                    screen.blit(imglist[fl[str(hl)][1][0]][1],(422,334))
            if 0<=(x-368)//32<2 and 0<=(y-264)//32<2:
                l = (x-368)//32*2+(y-264)//32
                if hl[l]!=0:
                    mt.pr(blokl[hl[l]]().name,0,0,0,x,y-20)
            elif 0==(x-384)//32 and 0==(y-328)//32:
                if mh!=0:
                    mt.pr(blokl[mh]().name,0,0,0,x,y-20)
            return hl,hg,mh,mla,self.hj,self.fr,self.lab
        
        def zlan(self,zl,zg,kl,rh,rha,kx,fkk):
            if fkk>=100:
                zg-=1
                if zg==0:zl=0
                if rh == 0:
                    rh=kl[kx]
                if blokl[rh]().tooltp!=-1:
                    rha=blokl[rh]().todness
                else:rha+=1
                fkk=0
            x = self.xut
            y = self.yut
            if self.jy == 1:
                if self.hj==0 and self.fr==0:
                    if 0<=(x-(400-len(kl)*16))//32<len(kl) and 0==(y-264)//32:
                        kx=(x-(400-len(kl)*16))//32
                    elif 0==(x-352)//32 and 0==(y-296)//32:
                        ob = sdw([zl],[zg],self.hj,self.fr,0)
                        [zl],[zg],self.hj,self.fr = ob.unpu()
                    elif 0==(x-384)//32 and 0==(y-328)//32:
                        ob = sdw([rh],[rha],self.hj,self.fr,0)
                        [rh],[rha],self.hj,self.fr = ob.unpu()
                else:
                    if 0<=(x-(400-len(kl)*16))//32<len(kl) and 0==(y-264)//32:
                        kx=(x-(400-len(kl)*16))//32
                    elif 0==(x-352)//32 and 0==(y-296)//32:
                        ob = sdw([zl],[zg],self.hj,self.fr,0)
                        [zl],[zg],self.hj,self.fr = ob.unpd()
                    elif 0==(x-384)//32 and 0==(y-328)//32:
                        ob = sdw([rh],[rha],self.hj,self.fr,0)
                        [rh],[rha],self.hj,self.fr = ob.unpd()
            elif self.nul != []:
                x1 = self.nul[0]
                y1 = self.nul[1]
                if self.hj==0 and self.fr==0:
                    if 0<=(x1-(400-len(kl)*16))//32<len(kl) and 0==(y1-264)//32:
                        kx=(x1-(400-len(kl)*16))//32
                    elif 0==(x1-352)//32 and 0==(y1-296)//32:
                        if zl != 0:
                            self.hj = zl
                            self.fr = zg
                            zl = 0
                            zg = 0
                    elif 0==(x1-384)//32 and 0==(y1-328)//32:
                        if rh != 0:
                            self.hj = rh
                            self.fr = rha
                            rh = 0
                            rha = 0
                else:
                    if 0<=(x1-(400-len(kl)*16))//32<len(kl) and 0==(y1-264)//32:
                        kx=(x1-(400-len(kl)*16))//32
                    elif 0==(x1-352)//32 and 0==(y1-296)//32:
                        ob = sdw([zl],[zg],self.hj,self.fr,0)
                        [zl],[zg],self.hj,self.fr = ob.pdo()
                    elif 0==(x1-384)//32 and 0==(y1-328)//32:
                        ob = sdw([rh],[rha],self.hj,self.fr,0)
                        [rh],[rha],self.hj,self.fr = ob.pdo()
            mt = scpr(20)
            self.__drawww(zl,zg,358,302,imgns)
            self.__drawww(rh,rha,390,334,imgns)
            for iks in range(len(kl)):
                if kx!=iks:
                    screen.blit(img0s,(400-len(kl)*16+iks*32,264))
                else:
                    screen.blit(imgns,(400-len(kl)*16+iks*32,264))
                screen.blit(imglist[kl[iks]][1],(406-len(kl)*16+iks*32,270))
            if 0==(x-352)//32 and 0==(y-296)//32:
                if zl!=0:
                    mt.pr(blokl[zl]().name,0,0,0,x,y-20)
            elif 0==(x-384)//32 and 0==(y-328)//32:
                if rh!=0:
                    mt.pr(blokl[rh]().name,0,0,0,x,y-20)
            elif 0<=(x-(400-len(kl)*16))//32<len(kl) and 0==(y-264)//32:
                if kl[(x-(400-len(kl)*16))//32]!=0:
                    mt.pr(blokl[kl[(x-(400-len(kl)*16))//32]]().name,0,0,0,x,y-20)
            if zl==14 and zg!=0 and ((rh==kl[kx] and blokl[kl[kx]]().tooltp==-1 and rha<255) or rh==0):
                fkk+=0.1
            elif zl==0:
                fkk=0
            whi = pygame.Rect(384,296, 32, 32*fkk/100)
            pygame.draw.rect(screen, (128, 128, 128), whi, 0)
            return zl,zg,rh,rha,self.hj,self.fr,kx,fkk
        
        def rlan(self,data,vpl,vrl):
            ql,qg,qh,qha,ex,ekk,sal,sag = data
            x = self.xut
            y = self.yut
            if self.jy == 1:
                if self.hj==0 and self.fr==0:
                    if 0==(x-352)//32 and 0==(y-296)//32:
                        ob = sdw([ql],[qg],self.hj,self.fr,0)
                        [ql],[qg],self.hj,self.fr = ob.unpu()
                    elif 0==(x-384)//32 and 0==(y-328)//32:
                        ob = sdw([qh],[qha],self.hj,self.fr,0)
                        [qh],[qha],self.hj,self.fr = ob.unpu()
                else:
                    if 0==(x-352)//32 and 0==(y-296)//32:
                        ob = sdw([ql],[qg],self.hj,self.fr,0)
                        [ql],[qg],self.hj,self.fr = ob.unpd()
                    elif 0==(x-384)//32 and 0==(y-328)//32:
                        ob = sdw([qh],[qha],self.hj,self.fr,0)
                        [qh],[qha],self.hj,self.fr = ob.unpd()
            elif self.nul != []:
                x1 = self.nul[0]
                y1 = self.nul[1]
                if self.hj==0 and self.fr==0:
                    if 0==(x1-352)//32 and 0==(y1-296)//32:
                        if ql != 0:
                            self.hj = ql
                            self.fr = qg
                            ql = 0
                            qg = 0
                    elif 0==(x1-384)//32 and 0==(y1-328)//32:
                        if qh != 0:
                            self.hj = qh
                            self.fr = qha
                            qh = 0
                            qha = 0
                    elif 0==(x1-416)//32 and 0==(y1-296)//32:
                        if sal != 0:
                            self.hj = sal
                            self.fr = sag
                            sal = 0
                            sag = 0
                else:
                    if 0==(x1-352)//32 and 0==(y1-296)//32:
                        ob = sdw([ql],[qg],self.hj,self.fr,0)
                        [ql],[qg],self.hj,self.fr = ob.pdo()
                    elif 0==(x1-384)//32 and 0==(y1-328)//32:
                        ob = sdw([qh],[qha],self.hj,self.fr,0)
                        [qh],[qha],self.hj,self.fr = ob.pdo()
                    elif 0==(x1-416)//32 and 0==(y1-296)//32:
                        ob = sdw([sal],[sag],self.hj,self.fr,0)
                        [sal],[sag],self.hj,self.fr = ob.pdo()
            mt = scpr(20)
            self.__drawww(ql,qg,358,302,imgns)
            self.__drawww(qh,qha,390,334,imgns)
            self.__drawww(sal,sag,422,302,imgns)
            if 0==(x-352)//32 and 0==(y-296)//32:
                if ql!=0:
                    mt.pr(blokl[ql]().name,0,0,0,x,y-20)
            elif 0==(x-384)//32 and 0==(y-328)//32:
                if qh!=0:
                    mt.pr(blokl[qh]().name,0,0,0,x,y-20)
            if ekk[0]!=0:
                whi = pygame.Rect(392,296+32*ekk[0]/ekk[1], 24, 32-32*ekk[0]/ekk[1])
                pygame.draw.rect(screen, (255, 64, 0), whi, 0)
                whi = pygame.Rect(384,296, 4, 32*ekk[2]/1200)
                pygame.draw.rect(screen, (255*ekk[2]/1200, 0, 0), whi, 0)
                if ql in vpl:
                    whi = pygame.Rect(384,296, 32*ekk[3]/vpl[ql][2], 4)
                    pygame.draw.rect(screen, (255, 255, 0), whi, 0)
                    whi = pygame.Rect(388,296, 4, 32*vpl[ql][1]/1200)
                    pygame.draw.rect(screen, (255*vpl[ql][1]/1200, 0, 0), whi, 0)
            return [ql,qg,qh,qha,ex,ekk,sal,sag],self.hj,self.fr
        
        def pik(self,data):#储物
            obl,oal = data
            x = self.xut
            y = self.yut
            if self.jy == 1:
                if self.hj==0 and self.fr==0:
                    if 0<=(x-304)//32<6 and 0<=(y-240)//32<4:
                        l = (x-304)//32*4+(y-240)//32
                        ob = sdw(obl,oal,self.hj,self.fr,l)
                        obl,oal,self.hj,self.fr = ob.unpu()
                else:
                    if 0<=(x-304)//32<6 and 0<=(y-240)//32<4:
                        l = (x-304)//32*4+(y-240)//32
                        ob = sdw(obl,oal,self.hj,self.fr,l)
                        obl,oal,self.hj,self.fr = ob.unpd()
            elif self.nul != []:
                x1 = self.nul[0]
                y1 = self.nul[1]
                if self.hj==0 and self.fr==0:
                    if 0<=(x1-304)//32<6 and 0<=(y1-240)//32<4:
                        l = (x1-304)//32*4+(y1-240)//32
                        if obl[l] != 0:
                            self.hj = obl[l]
                            self.fr = oal[l]
                            obl[l] = 0
                            oal[l] = 0
                else:
                    if 0<=(x1-304)//32<6 and 0<=(y1-240)//32<4:
                        l = (x1-304)//32*4+(y1-240)//32
                        ob = sdw(obl,oal,self.hj,self.fr,l)
                        obl,oal,self.hj,self.fr = ob.pdo()
            mt = scpr(20)
            for ix in range(6):
                for iy in range(4):
                    try:
                        self.__drawww(obl[ix*4+iy],oal[ix*4+iy],ix*32+310,246+iy*32,imgns)
                    except:
                        pass
            if 0<=(x-304)//32<6 and 0<=(y-240)//32<4:
                l = (x-304)//32*4+(y-240)//32
                if obl[l]!=0:
                    mt.pr(blokl[obl[l]]().name,0,0,0,x,y-20)
            return [obl,oal],self.hj,self.fr
        
        def flan(self,zl,zg,kl,rh,rha,kx,fkk):
            if zl in kl and fkk>=100:
                grt = kl[zl]
                zg-=1
                if zg==0:zl=0
                if rh == 0:
                    rh=grt[kx]
                if blokl[rh]().tooltp!=-1:
                    rha=blokl[rh]().todness
                else:rha+=1
                fkk=0
            x = self.xut
            y = self.yut
            if zl in kl:gll = len(kl[zl])
            else:gll = 0
            if self.jy == 1:
                if self.hj==0 and self.fr==0:
                    if 0<=(x-(400-gll*16))//32<gll and 0==(y-264)//32:
                        kx=(x-(400-gll*16))//32
                    elif 0==(x-352)//32 and 0==(y-296)//32:
                        ob = sdw([zl],[zg],self.hj,self.fr,0)
                        [zl],[zg],self.hj,self.fr = ob.unpu()
                    elif 0==(x-384)//32 and 0==(y-328)//32:
                        ob = sdw([rh],[rha],self.hj,self.fr,0)
                        [rh],[rha],self.hj,self.fr = ob.unpu()
                else:
                    if 0<=(x-(400-gll*16))//32<gll and 0==(y-264)//32:
                        kx=(x-(400-gll*16))//32
                    elif 0==(x-352)//32 and 0==(y-296)//32:
                        ob = sdw([zl],[zg],self.hj,self.fr,0)
                        [zl],[zg],self.hj,self.fr = ob.unpd()
                    elif 0==(x-384)//32 and 0==(y-328)//32:
                        ob = sdw([rh],[rha],self.hj,self.fr,0)
                        [rh],[rha],self.hj,self.fr = ob.unpd()
            elif self.nul != []:
                x1 = self.nul[0]
                y1 = self.nul[1]
                if self.hj==0 and self.fr==0:
                    if 0<=(x1-(400-gll*16))//32<gll and 0==(y1-264)//32:
                        kx=(x1-(400-gll*16))//32
                    elif 0==(x1-352)//32 and 0==(y1-296)//32:
                        if zl != 0:
                            self.hj = zl
                            self.fr = zg
                            zl = 0
                            zg = 0
                    elif 0==(x1-384)//32 and 0==(y1-328)//32:
                        if rh != 0:
                            self.hj = rh
                            self.fr = rha
                            rh = 0
                            rha = 0
                else:
                    if 0<=(x1-(400-gll*16))//32<gll and 0==(y1-264)//32:
                        kx=(x1-(400-gll*16))//32
                    elif 0==(x1-352)//32 and 0==(y1-296)//32:
                        ob = sdw([zl],[zg],self.hj,self.fr,0)
                        [zl],[zg],self.hj,self.fr = ob.pdo()
                    elif 0==(x1-384)//32 and 0==(y1-328)//32:
                        ob = sdw([rh],[rha],self.hj,self.fr,0)
                        [rh],[rha],self.hj,self.fr = ob.pdo()
            mt = scpr(20)
            self.__drawww(zl,zg,358,302,imgns)
            self.__drawww(rh,rha,390,334,imgns)
            if zl in kl:
                for iks in range(len(kl[zl])):
                    if kx!=iks:
                        screen.blit(img0s,(400-len(kl[zl])*16+iks*32,264))
                    else:
                        screen.blit(imgns,(400-len(kl[zl])*16+iks*32,264))
                    screen.blit(imglist[kl[zl][iks]][1],(406-len(kl[zl])*16+iks*32,270))
            if 0==(x-352)//32 and 0==(y-296)//32:
                if zl!=0:
                    mt.pr(blokl[zl]().name,0,0,0,x,y-20)
            elif 0==(x-384)//32 and 0==(y-328)//32:
                if rh!=0:
                    mt.pr(blokl[rh]().name,0,0,0,x,y-20)
            elif zl in kl and 0<=(x-(400-len(kl[zl])*16))//32<len(kl[zl]) and 0==(y-264)//32:
                if kl[zl][(x-(400-len(kl[zl])*16))//32]!=0:
                    mt.pr(blokl[kl[zl][(x-(400-len(kl[zl])*16))//32]]().name,0,0,0,x,y-20)
            if zl in kl and zg!=0 and ((rh==kl[zl][kx] and blokl[kl[zl][kx]]().tooltp==-1 and rha<255) or rh==0):
                fkk+=0.1
            elif zl==0:
                fkk=0
            whi = pygame.Rect(384,296, 32, 32*fkk/100)
            pygame.draw.rect(screen, (128, 128, 128), whi, 0)
            return zl,zg,rh,rha,self.hj,self.fr,kx,fkk
        
        def cit(self,rre,rra):
            rre,rra = rre.copy(),rra.copy()
            x = self.xut
            y = self.yut
            if self.jy == 1:
                l = (x-208+x)//32*8+(y-100)//32
                if 0<=l<len(rre) and 0<=(y-100)//32<8:
                    if blokl[rre[l]]().tooltp == -3:
                        eee = (max(lab) if lab!={} else 0)+1
                        rra[l] = eee
                        lab[eee]=labnm[hj]
                    if self.hj==0 and self.fr==0:
                        ob = sdw(rre,rra,self.hj,self.fr,l)
                        e,a,self.hj,self.fr = ob.unpu()
                    else:
                        ob = sdw(rre,rra,self.hj,self.fr,l)
                        e,a,self.hj,self.fr = ob.unpd()
                        
            elif self.nul != []:
                x1 = self.nul[0]
                y1 = self.nul[1]
                if self.hj==0 and self.fr==0:
                    l = (x1-208+x1-368)//32*8+(y1-100)//32
                    if 0<=l<len(rre) and 0<=(y1-100)//32<8:
                        if rre[l] != 0:
                            self.hj = rre[l]
                            self.fr = rra[l]
                else:
                    l = (x1-208+x1-368)//32*8+(y1-100)//32
                    if 0<=l<len(rre) and 0<=(y1-100)//32<8:
                        ob = sdw(rre,rra,self.hj,self.fr,l)
                        e,a,self.hj,self.fr = ob.pdo()
            mt = scpr(20)
            for ix in range(len(rre)//8+1):
                for iy in range(8):
                    if ix*8+iy<len(rre):
                        try:
                            self.__drawww(rre[ix*8+iy],rra[ix*8+iy],ix*32+214-x+368,106+iy*32,imgns)
                        except:
                            pass
            l = (x-208+x-368)//32*8+(y-100)//32
            if 0<=l<len(rre) and 0<=(y-100)//32<8:
                if rre[l]!=0:
                    mt.pr(blokl[rre[l]]().name,0,0,0,x,y-20)
            return self.be,self.ba,self.hj,self.fr
        
        def msoe(self):
            for i in self.kaa:
                mt.pr(str(i[0]),0,0,0,i[1],i[2])
            if self.hj != 0:
                screen.blit(imglist[self.hj][1],(self.xut-10,self.yut-10))
                if blokl[self.hj]().tooltp==-1:
                    mt.pr(str(self.fr),0,0,0,self.xut-10,self.yut-10)
                elif blokl[self.hj]().tooltp==-3:
                    pass
                else:
                    whi = pygame.Rect(self.xut-16,self.yut-16, 2, 32*self.fr/blokl[self.hj]().todness)
                    pygame.draw.rect(screen, (15, 15, 255), whi, 0)
    def UIR(x,y,wsch,d = frl(0,0,0).schl):
        _x,_y = 60,60
        mt = scpr(20)
        for i in d:
            if i in wsch:
                screen.blit(imgsh,(_x,_y))
            else:
                screen.blit(imgns,(_x+4,_y+4))
            screen.blit(imglist[d[i][1]][1],(_x+10,_y+10))
            _x+= 60
            if _x>800:_y,_x = _y+60,60
        _x,_y = 60,60
        for i in d:
            if _x<x<_x+40 and _y<y<_y+40:
                mt.pr(d[i][2],32,32,255,x-20*len(d[i][2])*_x/800,y-30)
            _x+= 60
            if _x>800:_y,_x = _y+60,60
    rre,rra = [i for i in range(len(blokl))],[0 if i==0 else 64 if blokl[i]().tooltp==-1 else blokl[i]().todness for i in range(len(blokl))]
    try:
        with open("./saves/"+worldname+".pickle","rb") as fk:
            jgqk,cx,cy,cxv,cyv,ke,seed,vsa,xg,mbx,ba,be,xut,yut,bex,bey,rbl,hp,t,gamd,hl,hg,dw,hj,fr,sai,mh,mla,bgxl,flxl,wsch,schu,zl,zg,jdd,rh,rha,engl,ogen,wort,engx,mods_data,jgsj,nst,patl,fcl,fcg,fh,fha,stg,subl,sdsww,temp,lab,tc,printing,wwws = pickle.load(fk)
        print("正在读取存档！")
        if wort == "1":
            wo=1
        elif wort == "2":
            wo=3
        elif wort == "3":
            wo=0
    except:
        bgxl = []#各变量，列表，字典初始化
        flxl = []
        engx = []
        xg = 0
        xf = 0
        cx = 10
        cy = 10
        cxv = 0
        cyv = 0
        cxv2 = 0
        cyv2 = 0
        hp = 100
        temp = 37
        xut = 0
        yut = 0
        ba = [0]*60
        be = [0]*60
        mh = 0
        mla = 0
        qw = []
        if wort == "1":
            wo=1
        elif wort == "2":
            wo=3
        elif wort == "3":
            wo=0
        rbl = []
        jgqk =  {}
        jgsj = 0
        hl = [0]*4
        hg = [0]*4
        zl = 0
        zg = 0
        fcl = 0
        fcg = 0
        t = 0
        dw = []
        hj = 0
        fr = 0
        sai = []
        wsch=[]
        schu=[]
        jdd = {}
        rh = 0
        rha = 0
        fh = 0
        fha = 0
        engl = []
        ogen = 100
        stg = 100
        nst = 0
        tc=0
        patl = {}
        subl = []
        sap = 0
        lab = {}
        fb = blokl[4]()
        printing = set()
        getat6(-8000,-100,rbl)
        for i in range(-10000,20,20):
            bex = i
            msuget,lljt = getat2(bex,bey,seed,stel,wo,swqx,swqf,stepoq,jgsj)
            if fb in msuget:
                for x_ in range(0,20):
                    for y_ in range(1,19):
                        skb1,skb2,skb3 = msuget[x_*20+y_-1:x_*20+y_+2]
                        if (skb1,skb2,skb3) == ([4],[0],[0]):
                            cx,cy = x_*40,720-y_*40
                            sap = 1
                if sap==1:
                    break
        sdsww = (bex,bey,cx,cy)
        vsa = saixy(jgqk,cx,cy,0,0,20,30,0,0,0,0.5,1,1.3,1)
        wwws=set()
    old_hp = 0
    bu = []
    bb = []
    rbg = []
    lzl = []
    seet,bl,rbl,bgxl,dw,bex,bey,cx,cy,subl,noi7,flxl,engx,lzl = chqk(bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,cx,cy,vsa,4,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,lzl,printing,wwws)
    weather_seed = int(seed[0:3])+20/abs(int(seed[0:3]))
    w = 0
    scw = 0
    mbx = 400
    ke = []
    t1 = time.perf_counter()
    t2 = time.perf_counter()
    bgf = 0
    msd = 0
    sx = 0
    sy = 0
    tk = 0
    f12 = 0
    la = 100
    uie = 0
    lv = 0
    nul = []
    fy = 0
    jy = 0
    fly = 0
    xut=0
    yut=0
    flxl=[]
    sut=time.perf_counter()
    mt = scpr(20)
    uiecl = 0
    kx = 0
    fkk = 0
    fuk = 0
    fuuk = 0
    drct = 0
    ckaa = [0,0]
    shtl = []
    sua = time.perf_counter()
    pl = saixy(jgqk,cx,cy,cxv,cyv,24,72,hp,fly,ogen,0.5,1,1.3,"pl")
    bgt = t//75000*75000
    weather_noise = noise1d(rn(weather_seed,bgt),rn(weather_seed,bgt+75000),512,750)
    rw,gw,bw = 0,0,0
    plwg = 0
    for i in modslist:
        modsa = eval(i+".initdic")
        if "game_start" in modsa["run_at"]:
            try:
                tset = modsa["run_at"]["game_start"]
                exec(tset[1]+"="+i+".start("+tset[0]+")")
            except:
                print("mode："+i+" 不规范")
    while True:#主循环体，似乎有些长，刚才好多了，现在又长了。
        if bgt != t//75000*75000:
            bgt = t//75000*75000
            weather_noise = noise1d(rn(weather_seed,bgt),rn(weather_seed,bgt+75000),512,750)
        svd = weather_noise[int((t-bgt)//100)]+noi7[int(pl.cx//40-1)]
        if svd<256:
            weather = "sunny"
            rw,gw,bw = vatovb(rw,1,0.005),vatovb(rw,1,0.005),vatovb(rw,1,0.005)
        elif svd<384:
            weather = "raining"
            rw,gw,bw = vatovb(rw,0.8,0.002),vatovb(rw,0.8,0.002),vatovb(rw,0.8,0.002)
        else:
            weather = "train"
            rw,gw,bw = vatovb(rw,0.6,0.002),vatovb(rw,0.6,0.002),vatovb(rw,0.6,0.002)
        if 29400<=t%60000<30000:
            ru="day"
            t_=t%600/600
            cr = lerp(160,16,twist(t_))
            cg = lerp(200,16,twist(t_))
            cb = lerp(255,64,twist(t_))
        elif 59400<=t%60000<60000:
            ru="night"
            t_=t%600/600
            cr = lerp(16,160,twist(t_))
            cg = lerp(16,200,twist(t_))
            cb = lerp(64,255,twist(t_))
        elif 0<=t%60000<29400:
            ru="day"
            cr = 160
            cg = 200
            cb = 255
        elif 30000<=t%60000<59400:
            ru="night"
            cr = 16
            cg = 16
            cb = 64
        screen.fill((cr*rw,cg*gw,cb*bw))
        t_=t%30000/30000
        if ru=="day":
            spx=lerp(-40,800,t_)
            spy=lerp(100,400,t_)
            screen.blit(imgsun,(spx,spy))
        else:
            spx=lerp(-280,800,t_)
            spy=lerp(400,100,t_)
            screen.blit(imgmun,(spx,spy))
        rrr1,rrr2,rrr3,rrr4,rrr5,rrr6 = indic(bex,bey,xut,yut,jgqk,jgsj,pl,poq,flbl)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                for i in modslist:
                    modsa = eval(i+".initdic")
                    if "game_end" in modsa["run_at"]:
                        try:
                            tset = modsa["run_at"]["game_end"]
                            exec(tset[1]+"="+i+".end("+tset[0]+")")
                        except:
                            print("mode："+i+" 不规范")
                with open("./saves/"+worldname+".pickle","wb") as fk:
                    pickle.dump((jgqk,pl.cx,pl.cy,cxv,cyv,ke,seed,vsa,xg,mbx,ba,be,xut,yut,bex,bey,rbl,pl.hp,t,gamd,hl,hg,dw,hj,fr,sai,mh,mla,bgxl,flxl,wsch,schu,zl,zg,jdd,rh,rha,engl,pl.ogen,wort,engx,mods_data,jgsj,nst,patl,fcl,fcg,fh,fha,stg,subl,sdsww,temp,lab,tc,printing,wwws),fk)
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:#这仨是玩家移动
                    if 1 not in ke:ke.append(1)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    drct=-1
                    if 2 not in ke:
                        som1.overturn()
                        ke.append(2)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    drct=1
                    if 3 not in ke:
                        som1.overturn()
                        ke.append(3)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if 4 not in ke:ke.append(4)
                if gamd == "2" or gamd == "3":
                    if event.key == pygame.K_f:#这4个是区块切换,用于开发者跑图
                        seet,bl,rbl,bgxl,dw,bex,bey,pl.cx,pl.cy,subl,noi7,flxl,engx,lzl = chqk(bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl.cx,pl.cy,vsa,0,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,lzl,printing,wwws)
                        pl.cx,pl.cy,vsa.cx,vsa.cy = 400,400,400,400
                    elif event.key == pygame.K_h:
                        seet,bl,rbl,bgxl,dw,bex,bey,pl.cx,pl.cy,subl,noi7,flxl,engx,lzl = chqk(bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl.cx,pl.cy,vsa,1,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,lzl,printing,wwws)
                        pl.cx,pl.cy,vsa.cx,vsa.cy = 400,400,400,400
                    elif event.key == pygame.K_g:
                        seet,bl,rbl,bgxl,dw,bex,bey,pl.cx,pl.cy,subl,noi7,flxl,engx,lzl = chqk(bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl.cx,pl.cy,vsa,2,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,lzl,printing,wwws)
                        pl.cx,pl.cy,vsa.cx,vsa.cy = 400,400,400,400
                    elif event.key == pygame.K_t:
                        seet,bl,rbl,bgxl,dw,bex,bey,pl.cx,pl.cy,subl,noi7,flxl,engx,lzl = chqk(bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl.cx,pl.cy,vsa,3,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,lzl,printing,wwws)
                        pl.cx,pl.cy,vsa.cx,vsa.cy = 400,400,400,400
                #物品栏选中格子的切换
                if event.key == pygame.K_i:xg = 10
                elif event.key == pygame.K_o:xg = 11
                elif event.key == pygame.K_3:xg = 2
                elif event.key == pygame.K_4:xg = 3
                elif event.key == pygame.K_5:xg = 4
                elif event.key == pygame.K_6:xg = 5
                elif event.key == pygame.K_7:xg = 6
                elif event.key == pygame.K_8:xg = 7
                elif event.key == pygame.K_9:xg = 8
                elif event.key == pygame.K_0:xg = 9
                elif event.key == pygame.K_1:xg = 0
                elif event.key == pygame.K_2:xg = 1
                elif event.key == pygame.K_u:bgf = 1
                elif event.key == pygame.K_F12:
                    if f12==0:f12 = 1
                    else:f12 = 0
                elif event.key == pygame.K_q:
                    if uie==0:
                        uie = 1
                        xc = rrr5#int((xut+pl.cx-390)//40)
                        yc = rrr6#int((yut+pl.cy-365)//40)
                        xq = xc//20*20
                        yq = yc//20*20
                        if seet[(xq//20+1)*3+2-(yq//20+1)][xc%20*20+19-yc%20].id == 1:
                            uiecl = 1
                        elif seet[(xq//20+1)*3+2-(yq//20+1)][xc%20*20+19-yc%20].id == 45:
                            uiecl = 2
                            ckaa = [(xq//20+1)*3+2-(yq//20+1),xc%20*20+19-yc%20]
                        elif seet[(xq//20+1)*3+2-(yq//20+1)][xc%20*20+19-yc%20].id == 77:
                            uiecl = 3
                            ckaa = [(xq//20+1)*3+2-(yq//20+1),xc%20*20+19-yc%20]
                        elif seet[(xq//20+1)*3+2-(yq//20+1)][xc%20*20+19-yc%20].id == 91:
                            uiecl = 4
                            ckaa = [(xq//20+1)*3+2-(yq//20+1),xc%20*20+19-yc%20]
                        elif seet[(xq//20+1)*3+2-(yq//20+1)][xc%20*20+19-yc%20].id==82:
                            top = tkinter.Tk()
                            E1 = tkinter.Entry(top, bd =5)
                            E1.insert(0,seet[(xq//20+1)*3+2-(yq//20+1)][xc%20*20+19-yc%20].data[0])
                            def helloCallBack():
                                t = E1.get()
                                E1.select_clear()
                                top.destroy()
                                jgqk[("fq",bex+xq,bey-yq,jgsj)][xc%20*20+19-yc%20].data=[t,codeplayer(t)]
                            B = tkinter.Button(top, text = "完成", command = helloCallBack)
                            E1.pack(side = tkinter.RIGHT)
                            B.pack()
                            top.mainloop()
                            uie=0
                    else:
                        uie,uiecl = 0,0
                        ckaa = [0,0]
                elif event.key == pygame.K_r:
                    if uie==0:
                        uie = 2
                    else:
                        uie = 0
                elif event.key == pygame.K_b:
                    pbgm = False if pbgm else True
                elif event.key == pygame.K_e:
                    jy = 1
                elif event.key == pygame.K_m and xf != 0:
                    dwf = saixy(jgqk,pl.cx-24,pl.cy-10,random.randint(-10,-5),random.randint(-2,2),20,20,0,0,0)
                    dw.append([xf,dwf,0,ba[xg]])
                    be[xg] = 0
                    ba[xg] = 0
                elif event.key == pygame.K_SPACE and gamd != "1":
                    pl.jfly()
                elif event.key == pygame.K_c and uie==0:
                    top2 = tkinter.Tk()
                    E2 = tkinter.Entry(top2, bd =5)
                    xgauu = cbuuu(E2,top2)
                    B2 = tkinter.Button(top2, text = "完成", command = xgauu.cmdj)
                    E2.pack(side = tkinter.RIGHT)
                    B2.pack()
                    top2.mainloop()
                    if xgauu.txt:
                        cmd=xgauu.txt.split(" ")
                        if cmd[0]=="c":
                            try:
                                if cmd[1]=="tp":
                                    seet,bl,rbl,bgxl,dw,bex,bey,pl,subl,noi7,flxl,engx = c_tp(cmd,bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl,vsa,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,printing,wwws)
                                elif cmd[1]=="fill":
                                    seet,bl = c_fill(cmd,jgqk,bex,bey,jgsj,poq,flbl,xbpo)
                                elif cmd[1]=="gamd":
                                    gamd,pl = c_gamd(cmd,pl)
                                elif cmd[1]=="tosj":
                                    seet,bl,rbl,bgxl,dw,bex,bey,pl,subl,noi7,flxl,engx,jgsj = c_tosj(cmd,bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl,vsa,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,printing,wwws)
                                elif cmd[1]=="setmt":
                                    timeste = c_setmt(cmd)
                                elif cmd[1]=="give":
                                    dw = c_give(cmd,jgqk,bex,bey,pl,dw)
                                elif cmd[1]=="kill":
                                    c_kill(pl)
                                elif cmd[1]=="getdata":
                                    c_getdata(cmd)
                                elif cmd[1]=="lview":
                                    lv = c_lview(lv)
                                elif cmd[1]=="buildst":
                                    rbg,seet,bl,rbl,bgxl,dw,bex,bey,pl,subl,noi7,flxl,engx = c_buildst(cmd,stel,rbg,bex,bey,jgqk,seed,rbl,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl,vsa,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,printing,wwws)
                                elif cmd[1]=="shtxt":
                                    shtl = c_shtxt(cmd,shtl)
                            except:
                                print("输入错误")
                elif event.key == pygame.K_j:
                    print("正在保存……")
                    with open("./saves/"+worldname+".pickle","wb") as fk:
                        pickle.dump((jgqk,pl.cx,pl.cy,cxv,cyv,ke,seed,vsa,xg,mbx,ba,be,xut,yut,bex,bey,rbl,pl.hp,t,gamd,hl,hg,dw,hj,fr,sai,mh,mla,bgxl,flxl,wsch,schu,zl,zg,jdd,rh,rha,engl,pl.ogen,wort,engx,mods_data,jgsj,nst,patl,fcl,fcg,fh,fha,stg,subl,sdsww,temp,lab,tc,printing,wwws),fk)
                    print("保存完成")
            elif event.type == pygame.KEYUP:#玩家运动制止程序。
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if 1 in ke:ke.remove(1)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if 2 in ke:ke.remove(2)
                    if 2 not in ke and 3 not in ke:
                        drct=0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if 3 in ke:ke.remove(3)
                    if 2 not in ke and 3 not in ke:
                        drct=0
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if 4 in ke:ke.remove(4)
                if event.key == pygame.K_u:
                    bgf = 0
            elif event.type == pygame.MOUSEMOTION:xut,yut = event.pos#鼠标方位获取，用于方块操作指示框
            elif event.type == pygame.MOUSEBUTTONDOWN:#方块挖掘程序
                if event.button == 1:
                    if uie == 1:
                        x, y = pygame.mouse.get_pos()
                        nul=[x,y]
                    else:
                        x, y = pygame.mouse.get_pos()
                        x = int((x+pl.cx-390)//40)
                        y = int((y+pl.cy-365)//40)
                        cxb = pl.cx//40
                        cyb = pl.cy//40
                        msd = 1
                elif event.button == 3 and uie == 0:#addd这个是放置
                    x = rrr5
                    y = rrr6
                    if xf == 93:xf = 92
                    bxe = x//20*20
                    bye = y//20*20
                    seep = jgqk[("fq",bex+bxe,bey-bye,jgsj)]
                    if seep[19-y%20+x%20*20].id == 97:
                        seep[19-y%20+x%20*20].data[0] = 10-seep[19-y%20+x%20*20].data[0]
                        bgxl,flxl,engx = cou(bex+x,bey-y-1,bgxl,flxl,engx,jgsj)
                    elif seep[19-y%20+x%20*20].id == 109 and time.perf_counter()-sua>0.7:
                        jgqk[("fq",bex+bxe,bey-bye,jgsj)][19-y%20+x%20*20]=blokl[0]()
                        saf = saixy(jgqk,x*40+1,y*40+1,random.randint(-10,10),-5,39,39,0,0,100,1,0.9)
                        subl.append([109,saf,random.randint(-10,10),300])
                        bgxl,flxl,engx = cou(bex+x,bey-y-1,bgxl,flxl,engx,jgsj)
                        seet = [jgqk[("fq",bex-1*20+i//3*20,bey-1*20+i%3*20,jgsj)] for i in range(9)]
                        bl = rtbl(seet,poq,flbl,xbpo)
                        sua = time.perf_counter()
                    elif seep[19-y%20+x%20*20].id == 110 and time.perf_counter()-sua>0.7:
                        saf = saixy(jgqk,x*40+10,y*40+5,0,0,7,35,0,0,100,0.5,0.5,-0.5)
                        subl.append([110,saf,seep[19-y%20+x%20*20].type,40])
                        jgqk[("fq",bex+bxe,bey-bye,jgsj)][19-y%20+x%20*20]=air()
                        bgxl,flxl,engx = cou(bex+x,bey-y-1,bgxl,flxl,engx,jgsj)
                        seet = [jgqk[("fq",bex-1*20+i//3*20,bey-1*20+i%3*20,jgsj)] for i in range(9)]
                        bl = rtbl(seet,poq,flbl,xbpo)
                        sua = time.perf_counter()
                    elif xf==86 or xf==92:
                        if (pl.cx//40 <= x <= (pl.cx+24)//40 and pl.cy//40 <= y <= (pl.cy+72)//40) == False:
                            if ((x == vsa.cx//40 or x == (vsa.cx+20)//40) and (y == vsa.cy//40 or y == (vsa.cy+30)//40)) == False:
                                if seep[19-y%20+x%20*20].id == 0 or seep[19-y%20+x%20*20].bltype==4:
                                    if jgqk[("fq",bex+bxe,bey-(y+1)//20*20,jgsj)][19-(y+1)%20+x%20*20].id not in poq:
                                        seep[19-y%20+x%20*20]=blokl[xf]()
                                        patl[(bex+bxe,bey-bye,19-y%20+x%20*20,jgsj)]=xf
                                        bgxl,flxl,engx = cou(bex+x,bey-y-1,bgxl,flxl,engx,jgsj)
                                        jgqk[("fq",bex+bxe,bey-bye,jgsj)] = seep
                                        bgxl,dw,flxl,engx=getat4(jgqk,bgxl,fdbl,poq,noul,dw,flxl,engx,bex,bey,printing)
                                        seet = [jgqk[("fq",bex-1*20+i//3*20,bey-1*20+i%3*20,jgsj)] for i in range(9)]
                                        bl = rtbl(seet,poq,flbl,xbpo)
                                        ba,be,xf = fzf(ba,be,xg,xf,gamd)
                    elif xf not in tiel:
                        if (pl.cx//40 <= x <= (pl.cx+24)//40 and pl.cy//40 <= y <= (pl.cy+72)//40) == False:#(y == pl.cy//40 or y == (pl.cy+36//40) or y == (pl.cy+72)//40)) == False:
                            if ((x == vsa.cx//40 or x == (vsa.cx+20)//40) and (y == vsa.cy//40 or y == (vsa.cy+30)//40)) == False:
                                if seep[19-y%20+x%20*20].id == 0 or seep[19-y%20+x%20*20].bltype==4:
                                    if xf == 13:
                                        top = tkinter.Tk()
                                        E1 = tkinter.Entry(top, bd =5)
                                        def helloCallBack():
                                            cdaaa = E1.get()
                                            E1.select_clear()
                                            top.destroy()
                                            seep[19-y%20+x%20*20]=blokl[13](cdaaa)
                                        B = tkinter.Button(top, text = "完成", command = helloCallBack)
                                        E1.pack(side = tkinter.RIGHT)
                                        B.pack()
                                        top.mainloop()
                                    elif xf==108:
                                        seep[19-y%20+x%20*20]=blokl[108]()#[xf,random.randint(0,1)]
                                    elif xf in iui:
                                        seep[19-y%20+x%20*20]=blokl[xf]()#[xf]+deepcopy(iui[xf])
                                        if xf==45 or xf==82:
                                            jdd[(bex+bxe,bey-bye,19-y%20+x%20*20,jgsj)]=xf
                                            if xf==82:
                                                seep[19-y%20+x%20*20].data[1]=codeplayer(seep[19-y%20+x%20*20].data[0])
                                        elif xf==86 or xf==92:
                                            patl[(bex+bxe,bey-bye,19-y%20+x%20*20,jgsj)]=xf
                                    elif xf == 110:
                                        top = tkinter.Tk()
                                        fuue=tkinter.Label(top, text="爆炸模式：")
                                        listb  = tkinter.Listbox(top,exportselection=0)
                                        liky = ["球形","炸裂","2024"]
                                        for item in liky:
                                            listb.insert("end",item)
                                        def helloCallBack2():
                                            cdaaa = listb.curselection()[0]
                                            top.destroy()
                                            seep[19-y%20+x%20*20]=blokl[110]()
                                            seep[19-y%20+x%20*20].type=int(cdaaa)
                                        B = tkinter.Button(top, text = "完成", command = helloCallBack2)
                                        fuue.pack()
                                        listb.pack()
                                        B.pack()
                                        top.mainloop()
                                    else:
                                        seep[19-y%20+x%20*20]=blokl[xf]()
                                    bgxl,flxl,engx = cou(bex+x,bey-y-1,bgxl,flxl,engx,jgsj)
                                    jgqk[("fq",bex+bxe,bey-bye,jgsj)] = seep
                                    bgxl,dw,flxl,engx=getat4(jgqk,bgxl,fdbl,poq,noul,dw,flxl,engx,bex,bey,printing)
                                    seet = [jgqk[("fq",bex-1*20+i//3*20,bey-1*20+i%3*20,jgsj)] for i in range(9)]
                                    bl = rtbl(seet,poq,flbl,xbpo)
                                    ba,be,xf = fzf(ba,be,xg,xf,gamd)
                    elif xf in {94,95}:
                        stg+= blokl[xf]().stad
                        if stg>100:stg=100
                        ba,be,xf = fzf(ba,be,xg,xf,gamd)
                    elif xf==96 and time.perf_counter()-sua>0.7:
                        xvd = xut-390
                        yvd = yut-365
                        s = abs(complex(xvd,yvd))
                        if s==0:s=1
                        xvd = xvd/s*40
                        yvd = yvd/s*40
                        saf = saixy(jgqk,pl.cx,pl.cy,xvd,yvd,10,10,0,0,100,1)
                        subl.append([xf,saf,random.randint(-10,10),3750])
                        ba,be,xf = fzf(ba,be,xg,xf,gamd)
                        sua = time.perf_counter()
                    elif xf==102:
                        plwg = 1-plwg
                    elif xf==103 and time.perf_counter()-sua>0.7:
                        xvd = xut-390
                        yvd = yut-365
                        s = abs(complex(xvd,yvd))
                        if s==0:s=1
                        xvd = xvd/s*40
                        yvd = yvd/s*40
                        saf = saixy(jgqk,pl.cx,pl.cy,xvd,yvd,20,20,0,0,100,1)
                        subl.append([xf,saf,random.randint(-10,10),300])
                        ba,be,xf = fzf(ba,be,xg,xf,gamd)
                        sua = time.perf_counter()
                    elif xf==107:
                        top = tkinter.Tk()
                        E1 = tkinter.Entry(top, bd =5)
                        E1.insert(0,lab[ba[xg]])
                        def helloCallBack():
                            t = E1.get()
                            E1.select_clear()
                            top.destroy()
                            lab[ba[xg]] = t
                        B = tkinter.Button(top, text = "完成", command = helloCallBack)
                        E1.pack(side = tkinter.RIGHT)
                        B.pack()
                        top.mainloop()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:msd = 0
        if pl.cx < 0:#玩家当前所在区块更改程序，根据玩家位置更改玩家所在区块
            seet,bl,rbl,bgxl,dw,bex,bey,pl.cx,pl.cy,subl,noi7,flxl,engx,lzl = chqk(bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl.cx,pl.cy,vsa,0,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,lzl,printing,wwws)
        if pl.cx > 800:
            seet,bl,rbl,bgxl,dw,bex,bey,pl.cx,pl.cy,subl,noi7,flxl,engx,lzl = chqk(bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl.cx,pl.cy,vsa,1,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,lzl,printing,wwws)
        if pl.cy > 800:
            seet,bl,rbl,bgxl,dw,bex,bey,pl.cx,pl.cy,subl,noi7,flxl,engx,lzl = chqk(bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl.cx,pl.cy,vsa,2,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,lzl,printing,wwws)
        if pl.cy < 0:
            seet,bl,rbl,bgxl,dw,bex,bey,pl.cx,pl.cy,subl,noi7,flxl,engx,lzl = chqk(bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl.cx,pl.cy,vsa,3,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,lzl,printing,wwws)
        if abs(vsa.cx-pl.cx) >= 600:#控制实体瞬移到玩家防止走丢卡bug
            vsa.cx,vsa.cxv = pl.cx,0
            vsa.cy,vsa.cyv = pl.cy,0
        if abs(vsa.cy-pl.cy) >= 600:
            vsa.cy,vsa.cyv = pl.cy,0
            vsa.cx,vsa.cxv = pl.cx,0
        if 0<=xg<12:xf = be[xg]#还在回忆写它干啥的
        else:xf = 0
        seet,shtl,bl,rbl,bgxl,dw,bex,bey,pl,subl,noi7,flxl,engx,timeste,lv = outwel(jgqk,seet,jdd,pl.cx,pl.cy,uie,shtl,bex,bey,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl,vsa,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,bl,noi7,timeste,lv)
        outpat(jgqk,patl,pl.cx,pl.cy)
        if uie == 1:
            UIe=UIw(be,ba,nul,xut,yut,hj,fr,jy,lab,labnm)
            be,ba,hj,fr=UIe.it()
            if uiecl==0:
                if gamd == "2" or gamd == "3":
                    be,ba,hj,fr=UIe.cit(rre,rra)
                else:
                    hl,hg,mh,mla,hj,fr,lab=UIe.plan(hl,hg,fl,mh,mla)
            elif uiecl==1:
                zl,zg,rh,rha,hj,fr,kx,fkk=UIe.zlan(zl,zg,kcl,rh,rha,kx,fkk)
            elif uiecl==2:
                seet[ckaa[0]][ckaa[1]].data,hj,fr=UIe.rlan(seet[ckaa[0]][ckaa[1]].data,vpl,vrl)
            elif uiecl==3:
                seet[ckaa[0]][ckaa[1]].data,hj,fr=UIe.pik(seet[ckaa[0]][ckaa[1]].data)
            elif uiecl==4:
                fcl,fcg,fh,fha,hj,fr,fuk,fuuk=UIe.flan(fcl,fcg,fgul,fh,fha,fuk,fuuk)
            UIe.msoe()
        elif uie == 2:
            UIR(xut,yut,wsch)
        else:
            pl,lzl,sx,sy,seet,tk,bl,la,rbl,dw,sai,ba,be,bgxl,flxl,sut,jdd,engx,jgsj,nst,shtl,stg,subl,temp,old_hp = un(bl,seet,pl,ke,seed,vsa,mbx,be,xg,xut,yut,bgf,lzl,t,msd,jgqk,bex,bey,sx,sy,ba,tk,f12,la,rbl,gamd,uie,dw,sai,xf,t2,bgxl,fdbl,flxl,wql,sut,jdd,engx,noul,jgsj,nst,xbpo,lv,shtl,stg,subl,weather,temp,plwg,old_hp,rrr1,rrr2,rrr3,rrr4,rrr5,rrr6,printing,drct,wwws)#正常运算世界
        for i in modslist:
            modsa = eval(i+".initdic")
            if "game_running" in modsa["run_at"]:
                try:
                    tset = modsa["run_at"]["game_running"]
                    exec(tset[1]+"="+i+".running("+tset[0]+")")
                except:
                    print("mode："+i+" 不规范")
                    modslist.remove(i)
                    break
        if tc <= 40:
            pl.hp = 100
        if gamd=="1":
            sdc=frl(be,pl.hp,jgsj)
            for iwe in sdc.schl:#成就系统的原理
                if iwe not in wsch:
                    if sdc.schl[iwe][0](sdc):
                        wsch.append(iwe)
                        schu.append([iwe,t,sdc.schl[iwe][1]])
            i=0
            while i<len(schu):
                scc = t-schu[i][1]
                if scc>=120:
                    del schu[i]
                else:
                    if scc<20:schy=lerp(-40,40*i,twist(scc/20))
                    elif scc>=100:schy=lerp(40*i,-40,twist(scc%20/20))
                    else:schy=40*i
                    screen.blit(imgsch,(0,schy+0))
                    screen.blit(imglist[schu[i][2]][1],(10,schy+10))
                    mt.pr(schu[i][0],255,255,255,40,schy+10)
                    i+=1
        if t%256 == 0:#实体随机运动魔鬼控制程序
            mbx = random.randint(-10,10)
            for i in range(len(sai)):
                if random.randint(0,1)==1:
                    sai[i][2] = random.randint(-10,10)
        if t%10==0:#废物生成
            for i in range(len(sqai)):
                if len(sai)<20:
                    if random.randint(1,sqai[i][1])==1:
                        if random.randint(0,1) == 1:ghx = random.randint(-1200,-400)
                        else:ghx = random.randint(1200,2000)
                        for dfk in range(bey*40-1200,bey*40+2001,40):
                            if ("fq",ghx//800*20+bex,dfk//800*20+bey,jgsj) in jgqk and jgqk[("fq",ghx//800*20+bex,dfk//800*20+bey,jgsj)][(ghx-1)%800//40*20+19-dfk%800//40].id == 4:
                                saf = saixy(jgqk,ghx,-bey*40+dfk-sqai[i][6]-1,0,0,sqai[i][5],sqai[i][6],sqai[i][2],0,100)
                                sai.append([i,saf,random.randint(-10,10),sqai[i][3],sqai[i][7]])
                                break
            for i in range(len(sdai)):
                if len(sai)<20:
                    if random.randint(1,sdai[i][1])==1:
                        if random.randint(0,1) == 1:ghx = random.randint(-1200,-400)
                        else:ghx = random.randint(1200,2000)
                        for dfk in range(bey*40-1200,bey*40+2001,40):
                            if ("fq",ghx//800*20+bex,dfk//800*20+bey,jgsj) in jgqk and jgqk[("fq",ghx//800*20+bex,dfk//800*20+bey,jgsj)][(ghx-1)%800//40*20+19-dfk%800//40].id == 11 and jgqk[("fq",ghx//800*20+bex,(dfk+40)//800*20+bey,jgsj)][(ghx-1)%800//40*20+19-(dfk+40)%800//40].id == 0:
                                saf = saixy(jgqk,ghx,-dfk-bey*40-sdai[i][6]-1,0,0,sdai[i][5],sdai[i][6],sdai[i][2],0,100,0.5,1,1.3,2)
                                sai.append([i,saf,random.randint(-10,10),sqai[i][3],"#"])
                                break
        if t%10 == 0:
            if flxl!=[]:
                jgqk,flxl,dw,bgxl,engx = fluid(jgqk,flxl,flbl,flpoq,dw,noul,bgxl,engx,bex,bey)
            if engx!=[]:
                jgqk,engx,bgxl,flxl,dw = hkgl(jgqk,jgsj,engx,bgxl,flxl,lipoq,dw,noul,bex,bey,subl)
                bgxl,dw,flxl,engx = getat4(jgqk,bgxl,fdbl,poq,noul,dw,flxl,engx,bex,bey,printing)
            seet = [jgqk[("fq",bex-1*20+i//3*20,bey-1*20+i%3*20,jgsj)] for i in range(9)]
            bl = rtbl(seet,poq,flbl,xbpo)
        t += 1#刻递增程序
        tc += 1
        t2 = time.perf_counter()
        while time.perf_counter()-t1 < timeste:pass#限帧等待
        t1 = time.perf_counter()
        pygame.display.flip()#刷新屏幕
        if pl.hp <= 0 and gamd == "1" or jgsj==1 and bey<=-500:
            print("死亡地点：维度",jgsj,"的",str(bex)+"+"+str(pl.cx),str(bey)+"+"+str(pl.cy))#孤独
            bex,bey,pl.cx,pl.cy = sdsww
            seet,bl,rbl,bgxl,dw,bex,bey,pl.cx,pl.cy,subl,noi7,flxl,engx,lzl = chqk(bex,bey,jgqk,seed,rbl,rbg,bgxl,fdbl,dw,xut,yut,poq,flbl,xbpo,wo,pl.cx,pl.cy,vsa,4,stel,swqx,swqf,stepoq,sai,noul,jgsj,subl,flxl,engx,lzl,printing,wwws)
            hp,tc,stg,temp = 100,0,100,37
        jy,nul = 0,[]
#共2050+1765+1680=5495行代码（含注释）（只有晦涩难懂的代码，才能衬托出我的____（
#} write by 林林（https://code.xueersi.com/space/2731368）