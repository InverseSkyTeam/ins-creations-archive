import codecs
import 输入法 as shurufa
import pgzrun
text=''
temp=''
state='打字'
#inputs=Actor()
size=40
WIDTH = 960
HEIGHT = 420
bg=Actor('背景1.png',[WIDTH/2,HEIGHT/2])
sr=Actor('造型1.png',[100,100])
dai=[]
xs=0
xxxx=1
piy=0#指针向左偏移值
ise=0
def draw():
    global text,dai,temp,xs,temp,size,j,piy,ise,state
    if ise:
        text=text+temp
        state="打字"
        temp=''
    text1=text+temp
    j=0
    k=0
    bg.draw()
    yu=round((WIDTH-size/2)/size)
    for i in text1:       
        #print(j%yu)
        if j%yu==0 and j!=0:
            k+=size      
        screen.draw.text(text1[j],fontname='ziti.ttf',center=[(j%yu)*size+size/2, size/2+(j//yu)*size], color='black', fontsize=size) 
        j+=1
    
    if xxxx==1:
        screen.draw.text('|',fontname='ziti.ttf',center=[(j%yu)*size, size/2+(j//yu)*size], color='black', fontsize=size) 
    if state=='输入':
        sr.pos=[min((len(text)%yu)*size+190/2,WIDTH-190/2), size+k+30]
        sr.draw()
        dai=shurufa.fen(shurufa.check(temp))
        tdai=dai[xs]
        screen.draw.text('1.',fontname='ziti.ttf',center=[sr.pos[0]-70, sr.pos[1]], color='black',fontsize=30)
        screen.draw.text(tdai[0],fontname='ziti.ttf',center=[sr.pos[0]-50, sr.pos[1]], color='black',fontsize=30)
        screen.draw.text('2.',fontname='ziti.ttf',center=[sr.pos[0]-20, sr.pos[1]], color='black',fontsize=30)
        screen.draw.text(tdai[1],fontname='ziti.ttf',center=[sr.pos[0], sr.pos[1]], color='black',fontsize=30)
        screen.draw.text('3.',fontname='ziti.ttf',center=[sr.pos[0]+30, sr.pos[1]], color='black',fontsize=30)
        screen.draw.text(tdai[2],fontname='ziti.ttf',center=[sr.pos[0]+50, sr.pos[1]], color='black',fontsize=30)
        #print(shurufa.check(temp))
    
def mx():
    global xxxx
    if xxxx==0:
        xxxx=1
    else:
        xxxx=0
clock.schedule_interval(mx,0.6)
def on_key_down():
    global temp,state,text,xs,dai,xxxx,size,ise
    if keyboard.K_TAB:
        ise=int(not ise)
    if keyboard.K_BACKSPACE:
        if len(temp)==0:
            state='打字'
            text=text[:-1]
        else:
            temp=temp[:-1]
            if len(temp)==0:
                state='打字'
    if keyboard.K_Q:
        xs=0
        state='输入'
        temp+='Q'
    if keyboard.K_W:
        xs=0
        state='输入'
        temp+='W'
    if keyboard.K_E:
        xs=0
        state='输入'
        temp+='E'
    if keyboard.K_R:
        xs=0
        state='输入'
        temp+='R'
    if keyboard.K_T:
        xs=0
        state='输入'
        temp+='T'
    if keyboard.K_Y:
        xs=0
        state='输入'
        temp+='Y'
    if keyboard.K_U:
        xs=0
        state='输入'
        temp+='U'
    if keyboard.K_I:
        xs=0
        state='输入'
        temp+='I'
    if keyboard.K_O:
        xs=0
        state='输入'
        temp+='O'
    if keyboard.K_P:
        xs=0
        state='输入'
        temp+='P'
    if keyboard.K_A:
        xs=0
        state='输入'
        temp+='A'
    if keyboard.K_S:
        xs=0
        state='输入'
        temp+='S'
    if keyboard.K_D:
        xs=0
        state='输入'
        temp+='D'
    if keyboard.K_F:
        xs=0
        state='输入'
        temp+='F'
    if keyboard.K_G:
        xs=0
        state='输入'
        temp+='G'
    if keyboard.K_H:
        xs=0
        state='输入'
        temp+='H'
    if keyboard.K_J:
        xs=0
        state='输入'
        temp+='J'
    if keyboard.K_K:
        xs=0
        state='输入'
        temp+='K'
    if keyboard.K_L:
        xs=0
        state='输入'
        temp+='L'
    if keyboard.K_Z:
        xs=0
        state='输入'
        temp+='Z'
    if keyboard.K_X:
        xs=0
        state='输入'
        temp+='X'
    if keyboard.K_C:
        xs=0
        state='输入'
        temp+='C'
    if keyboard.K_V:
        xs=0
        state='输入'
        temp+='V'
    if keyboard.K_B:
        xs=0
        state='输入'
        temp+='B'
    if keyboard.K_N:
        xs=0
        state='输入'
        temp+='N'
    if keyboard.K_M:
        xs=0
        state='输入'
        temp+='M'
    if keyboard.K_1:
        if state=='输入':
            state='打字'
            temp=""
            #print(dai)
            text+=dai[xs][0]
        else:
            text+='1'
    if keyboard.K_2:
        if state=='输入':
            state='打字'
            temp=""
            text+=dai[xs][1]
        else:
            text+='2'
    if keyboard.K_3:
        if state=='输入':
            state='打字'
            temp=""
            text+=dai[xs][2]
        else:
            text+='3'
    if keyboard.K_4 and state=='打字':
        text+='4'
    if keyboard.K_5 and state=='打字':
        text+='5'
    if keyboard.K_6 and state=='打字':
        text+='6'
    if keyboard.K_7 and state=='打字':
        text+='7'
    if keyboard.K_8 and state=='打字':
        text+='8'
    if keyboard.K_9 and state=='打字':
        text+='9'
    if keyboard.K_0 and state=='打字':
        text+='0'
    if keyboard.K_RIGHT and state=='输入':
        xs+=1
        if xs>=len(dai):
            xs=len(dai)-1
    if keyboard.K_LEFT and state=='输入':
        xs-=1
        if xs<0:
            xs=0
    if keyboard.K_SPACE and state=='打字':
        text+=' '
pgzrun.go()