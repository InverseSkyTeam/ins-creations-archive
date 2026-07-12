import sys
import tty
import termios
from copy import deepcopy
def clear():
    print("\033c",flush=1,end="")
def gotoxy(x,y):
    print(f"\033[{x};{y}f",end="")
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
def edit(render):
    clear()
    nu=True
    code=[[]]
    history=[]
    x,y=0,-1
    mode="NORMAL"
    begin=0
    beginy=0
    size=15
    sizey=50
    ikey={}
    nkey={}
    selectx,selecty=0,0
    def getall():
        res=[]
        if selectx==x and selecty==y:
            return []
        lx,ly,rx,ry=0,0,0,0
        if selectx<x or selectx==x and selecty<y:
            lx,ly,rx,ry=selectx,selecty+1,x,y+1
        else:
            lx,ly,rx,ry=x,y+1,selectx,selecty+1
        if ly==-1:
            ly+=1
        if ry==-1:
            ry+=1
        while lx!=rx or ly!=ry:
            res.append((lx,ly))
            ly+=1
            if lx==len(code):
                break
            if ly>=len(code[lx]):
                ly=0
                lx+=1
        return res
    def count_tab(line):
        i=0
        while i<len(code[line]) and code[line][i]==' ':
            i+=1
        return (i+1)//2
    def do_cmds(cmd):
        cmd=cmd.replace("<cr>","\n")\
            .replace("<esc>","\033")
        for i in cmd:
            do_cmd(i)
    def do_cmd(ch):
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu
        if ord(ch)==27:
            gotoxy(size+1,1)
            print("NORMAL")
            a=getch()
            if ord(a)==91:
                gotoxy(size+1,1)
                print(mode)
                ch=getch()
                if ch=='A':
                    if x!=0:
                        x-=1
                    else:
                        y=-1
                    if y>=len(code[x]):
                        y=len(code[x])-1
                    if y<len(code) and y!=-1 and code[x][y]=="":
                        y+=1
                elif ch=='B':
                    if x!=len(code)-1:
                        x+=1
                    else:
                        y=len(code[x])-1
                    if y>=len(code[x]):
                        y=len(code[x])-1
                    if y<len(code) and y!=-1 and code[x][y]=="":
                        y+=1
                elif ch=='D':
                    if y!=-1:
                        if code[x][y]=="":
                            y-=1
                        elif ord(code[x][y])>=128:
                            y-=2
                        else:
                            y-=1
                    else:
                        if x>0:
                            x-=1
                            y=len(code[x])-1
                elif ch=='C':
                    if y!=len(code[x])-1:
                        if code[x][y+1]=="":
                            y+=1
                        y+=1
                    else:
                        if x!=len(code)-1:
                            x+=1
                            y=-1
            else:
                mode="NORMAL"
                gotoxy(size+1,1)
                do_cmd(a)
            return
        elif ord(ch)==127 or (ch=='d' and mode=="NORMAL"):
            history.append((deepcopy(code),x,y))
            if y==-1:
                if x!=0:
                    x-=1
                    y=len(code[x])-1
                    code[x]+=code[x+1]
                    del code[x+1]
            elif code[x][y-1:y+1]==[" "," "]:
                del code[x][y-1:y+1]
                y-=2
            elif "".join(code[x][y:y+2]) in ("()","[]","{}",'""',"''"):
                del code[x][y:y+2]
                y-=1
            elif ord(code[x][y])>=128:
                del code[x][y-1:y+1]
                y-=2
            else:
                del code[x][y]
                y-=1
        if mode=="NORMAL":
            if ch in nkey:
                if callable(nkey[ch]):
                    nkey[ch]()
                else:
                    do_cmds(nkey[ch])
            elif ch=='v':
                mode="SELECT"
                selectx,selecty=x,y
            elif ch=='i':
                mode="INSERT"
            elif ch=='z':
                if history:
                    code,x,y=history.pop()
            elif ch=='k':
                if x!=0:
                    x-=1
                else:
                    y=-1
                if y>=len(code[x]):
                    y=len(code[x])-1
                if y<len(code) and y!=-1 and code[x][y]=="":
                    y+=1
            elif ch=='j':
                if x!=len(code)-1:
                    x+=1
                else:
                    y=len(code[x])-1
                if y>=len(code[x]):
                    y=len(code[x])-1
                if y<len(code) and y!=-1 and code[x][y]=="":
                    y+=1
            elif ch=='h':
                if y!=-1:
                    if code[x][y]=="":
                        y-=1
                    elif ord(code[x][y])>=128:
                        y-=2
                    else:
                        y-=1
                else:
                    if x>0:
                        x-=1
                        y=len(code[x])-1
            elif ch=='l':
                if y!=len(code[x])-1:
                    if code[x][y+1]=="":
                        y+=1
                    y+=1
                else:
                    if x!=len(code)-1:
                        x+=1
                        y=-1
            elif ch=='<':
                y=-1
            elif ch=='>':
                y=len(code[x])-1
            elif ch=='f':
                gotoxy(size+2,1)
                print('f')
                ch=getch()
                while y>=0 and x>=0:
                    if code[x][y]==ch:
                        y-=1
                        break
                    y-=1
                    if y<=-1 and x!=0:
                        x-=1
                        y=len(code[x])-1
            elif ch=='F':
                gotoxy(size+2,1)
                print('F')
                ch=getch()
                while y<len(code[x]) and x<len(code):
                    if code[x][y]==ch:
                        y-=1
                        break
                    y+=1
                    if y>=len(code[x]) and x!=len(code)-1:
                        x+=1
                        y=0
                if y>=len(code[x]):
                    y=len(code[x])-1
            elif ch=='r':
                clear()
                print("\033[1;33m开始运行\033[1;0m")
                try:
                    exec("\n".join(map("".join,code)))
                except Exception as e:
                    print(type(e).__name__+":",e)
                print("\033[1;33m运行结束\033[1;0m")
                getch()
            elif ch==':':
                gotoxy(size+2,1)
                cmd=input(':')
                cmd=cmd.split(" ")
                head=cmd[0]
                cmd=cmd[1:]
                if head=="help":
                    clear()
                    print('''帮助：
NORMAL hjkl：左下上右
NORMAL v：切换到SELECT模式
NORMAL i：切换到INSERT模式
NORMAL z：相当于Ctrl-Z
NORMAL d/INSERT BackSpace：删除当前字符
NORMAL <：到行首
NORMAL >：到行尾
NORMAL :help：获取此帮助
NORMAL :size x y：调整编辑器大小
NORMAL fx：向前寻找字符x
NORMAL Fx：向后寻找字符x
NORMAL r：运行
INSERT Esc：切换到NORMAL模式
NORMAL :nu：显示行号
NORMAL :nonu：隐藏行号
NORMAL news：显示更新内容
Arrows：上下左右（需要安装并启用XesExt）
Ctrl-C：退出编辑器
''')
                    getch()
                elif head=="size":
                    try:
                        size,sizey=int(cmd[0]),int(cmd[1])
                    except:
                        ...
                elif head=="nu":
                    nu=True
                elif head=="nonu":
                    nu=False
                elif head=="news":
                    clear()
                    print('''本次更新包括：
1、:news获取帮助
2、:nu显示行号
3、:nonu隐藏行号
4、支持上下左右（当然需要XesExt）
5、修复SELECT模式多行选择的bug
6、对内置变量的代码高亮
''')
                    getch()
        elif mode=="SELECT":
            if ord(ch)==27:
                mode="NORMAL"
            elif ch=='d' or ord(ch)==127:
                mode="INSERT"
                if x==selectx:
                    if y<selecty:
                        del code[x][y+1:selecty+1]
                    else:
                        del code[x][selecty+1:y+1]
                elif x<selectx:
                    del code[selectx][:selecty+1]
                    del code[x][y+1:]
                    for i in range(x+1,selectx):
                        del code[x+1]
                else:
                    del code[selectx][selecty+1:]
                    del code[x][:y+1]
                    for i in range(selectx+1,x):
                        del code[x+1]
                x=min(x,len(code)-1)
                y=min(y,len(code[x])-1)
            elif ch=='k':
                if x!=0:
                    x-=1
                else:
                    y=-1
                if y>=len(code[x]):
                    y=len(code[x])-1
                if y<len(code) and y!=-1 and code[x][y]=="":
                    y+=1
            elif ch=='j':
                if x!=len(code)-1:
                    x+=1
                else:
                    y=len(code[x])-1
                if y>=len(code[x]):
                    y=len(code[x])-1
                if y<len(code) and y!=-1 and code[x][y]=="":
                    y+=1
            elif ch=='h':
                if y!=-1:
                    if y<len(code) and y!=-1 and code[x][y]=="":
                        y-=1
                    elif ord(code[x][y])>=128:
                        y-=2
                    else:
                        y-=1
                else:
                    if x>0:
                        x-=1
                        y=len(code[x])-1
            elif ch=='l':
                if y!=len(code[x])-1:
                    if code[x][y+1]=="":
                        y+=1
                    y+=1
                else:
                    if x!=len(code)-1:
                        x+=1
                        y=-1
            elif ch=='<':
                y=-1
            elif ch=='>':
                y=len(code[x])-1
            elif ch=='f':
                gotoxy(size+2,1)
                print('f')
                ch=getch()
                while y>=0 and x>=0:
                    if code[x][y]==ch:
                        y-=1
                        break
                    y-=1
                    if y<=-1 and x!=0:
                        x-=1
                        y=len(code[x])-1
            elif ch=='F':
                gotoxy(size+2,1)
                print('F')
                ch=getch()
                while y<len(code[x]) and x<len(code):
                    if code[x][y]==ch:
                        y-=1
                        break
                    y+=1
                    if y>=len(code[x]) and x!=len(code)-1:
                        x+=1
                        y=0
                if y>=len(code[x]):
                    y=len(code[x])-1
        elif mode=="INSERT":
            if ch in ikey:
                if callable(ikey[ch]):
                    ikey[ch]()
                else:
                    do_cmds(ikey[ch])
            elif ord(ch)==27:
                mode="NORMAL"
            else:
                history.append((deepcopy(code),x,y))
                if ch=='\r':
                    if y!=-1 and code[x][y]==':':
                        code.insert(x+1,[" "]*(1+count_tab(x))*2+code[x][y+1:])
                        code[x]=code[x][:y+1]
                        x+=1
                        y=count_tab(x-1)*2+1
                    else:
                        code.insert(x+1,[" "]*count_tab(x)*2+code[x][y+1:])
                        code[x]=code[x][:y+1]
                        x+=1
                        y=count_tab(x-1)*2-1
                elif ch=='\t':
                    code[x].insert(y+1," ")
                    y+=1
                    code[x].insert(y+1," ")
                    y+=1
                elif ord(ch)==127:
                    ...
                elif ord(ch)>=128:
                    code[x].insert(y+1,"")
                    y+=1
                    code[x].insert(y+1,ch)
                    y+=1
                elif ch in "\"'([{":
                    code[x].insert(y+1,ch)
                    y+=1
                    code[x].insert(y+1,{
                        '"':'"',
                        '\'':'\'',
                        '(':')',
                        '[':']',
                        '{':'}',
                    }[ch])
                else:
                    code[x].insert(y+1,ch)
                    y+=1
    while 1:
        if x<begin:
            begin=x
        if x>=begin+size:
            begin=x-size+1
        if y<beginy:
            beginy=y+1
        if y>=beginy+sizey-1:
            beginy=y-sizey+2
        rr=render("\n".join(map("".join,code)))
        if len(rr)<len(code):
            rr+=[[]]
        if mode=="SELECT":
            gar=getall()
            for i in range(begin,min(begin+size,len(rr))):
                if nu:
                    print("\033[1;0m%4d | "%(i+1),flush=True,end="")
                for j in range(beginy,min(beginy+sizey,len(rr[i]))):
                    if (i,j) in gar:
                        print(rr[i][j][:-1]+"\033[1;47m"+rr[i][j][-1],end="")
                    else:
                        print(rr[i][j],end="")
                print("\033[1;0m")
            gotoxy(size+3,1)
            #print(gar,selectx,selecty)
        else:
            _i=begin
            for i in rr[begin:begin+size]:
                if nu:
                    print("\033[1;0m%4d | "%(_i+1),flush=True,end="")
                print("".join(i[beginy:beginy+sizey]))
                _i+=1
        if not nu:
            gotoxy(x+1-begin,y+2-beginy)
        else:
            gotoxy(x+1-begin,y+9-beginy)
        print("\033[1;47m \033[1;0m")
        gotoxy(size+1,1)
        print(mode)
        ch=getch()
        if ord(ch)==3:
            break
        else:
            do_cmd(ch)
        clear()
@edit
def pyrender(code):
    '''
    数字：\033[0;33m
    标识符：\033[1;0m
    关键字：\033[1;35m
    字符串|注释：\033[0;32m
    '''
    res=[]
    p=0
    while p<len(code):
        if code[p].isdigit():
            while p<len(code) and (code[p].isdigit() or code[p] in '.xbo'):
                res.append("\033[0;33m"+code[p])
                p+=1
        elif code[p].isalpha() or code[p]=="_":
            s=""
            while p<len(code) and (code[p].isalnum() or code[p]=='_'):
                s+=code[p]
                p+=1
            if s in __import__("keyword").kwlist:
                for i in s:
                    res.append("\033[1;35m"+i)
            elif s in dir(__builtins__):
                for i in s:
                    res.append("\033[1;34m"+i)
            elif s in ["self","cls"]:
                for i in s:
                    res.append("\033[0;34m"+i)
            else:
                for i in s:
                    res.append("\033[1;0m"+i)
        elif code[p:p+3] in ('"""',"'''"):
            s=code[p:p+3]
            x=s
            p+=3
            while p<len(code) and code[p:p+3]!=x:
                if code[p]=='\\':
                    s+=code[p]
                    p+=1
                    if code[p] in '\'"':
                        s+=code[p]
                        p+=1
                else:
                    s+=code[p]
                    p+=1
            s+=code[p:p+3]
            p+=3
            for i in s:
                if ord(i)>=128:
                    res.append("")
                res.append("\033[0;32m"+i)
        elif code[p] in '\'"':
            s=code[p]
            x=s
            p+=1
            while p<len(code) and code[p]!='\n' and code[p]!=x:
                if code[p]=='\\':
                    s+=code[p]
                    p+=1
                    if code[p] in '\'"\n':
                        s+=code[p]
                        p+=1
                else:
                    s+=code[p]
                    p+=1
            if p<len(code):
                s+=code[p]
                p+=1
            for i in s:
                if ord(i)>=128:
                    res.append("")
                res.append("\033[0;32m"+i)
        elif code[p]=='#':
            while p<len(code) and code[p]!='\n':
                res.append("\033[0;32m"+code[p])
                p+=1
        else:
            if ord(code[p])>=128:
                res.append("")
            res.append("\033[1;0m"+code[p])
            p+=1
    rr=[]
    tmp=[]
    for i in res:
        if "\n" in i:
            rr.append(tmp)
            tmp=[]
        else:
            tmp.append(i)
    if tmp:
        return rr+[tmp]
    return rr