import sys,os,time,pyperclip
import msvcrt
from copy import deepcopy
import copy,sys,time
import c,cpp,py,rain,txt,newlang,js
#各种文件的高亮和运行支持
def clear():
    os.system("cls")
def gotoxy(x,y):
    print(f"\033[{x};{y}f",flush=True,end="")
def getch():
    return msvcrt.getwch()
def paste():
    return pyperclip.paste()
def copy(s):
    pyperclip.copy(s)
themes={
    "default":{
        "keyword":"\033[1;35m",
        "this":"\033[0;34m",
        "builtin":"\033[1;34m",
        "string":"\033[0;32m",
        "comment":"\033[0;32m",
        "operator":"\033[1;36m",
        "header":"\033[1;35m",
        "number":"\033[0;33m",
        "identifier":"\033[1;0m",
        "others":"\033[1;0m",
    }
}
def getAllWord(code:str)->list:
    words=[]
    p=0
    while p<len(code):
        if code[p].isalnum() or code[p]=='_':
            s=""
            while p<len(code) and (code[p].isalnum() or code[p]=='_'):
                s+=code[p]
                p+=1
            words.append(s)
        else:
            p+=1
    return words
def choose_word(choices:list,ln:int,max_col:int):
    if choices==[]:
        return ""
    if len(choices)==1:
        return choices[0]
    col=max_col//15
    p=0
    while 1:
        gotoxy(ln,1)
        print("\033[1;0m"+" "*max_col)
        gotoxy(ln,1)
        for i in range(p//col*col,min(p//col*col+col,len(choices))):
            if p==i:
                print("\033[1;44m"+"%14s "%choices[i]+"\033[1;0m",end="")
            else:
                print("%14s "%choices[i],end="")
        print()
        ch=getch()
        if ch=='h':
            if p:
                p-=1
        elif ch=='l':
            if p<len(choices)-1:
                p+=1
        elif ch=='\r':
            return choices[p]
        elif ord(ch)==27:
            return ""
    return ""
def edit(lang,save):
    clear()
    tab=2
    nu=True
    code=[[]]
    def _o():
        nonlocal code
        code=[[]]
        with open(save,'r',encoding='utf-8') as f:
            for i in f.readlines():
                for j in i:
                    if j=="\n":
                        code.append([])
                    elif ord(j)<128:
                        code[-1].append(j)
                    else:
                        code[-1].append("")
                        code[-1].append(j)
    if save:
        _o()
    history=[]
    delay=0.1
    x,y=0,-1
    mode="NORMAL"
    begin=0
    beginy=0
    size=os.get_terminal_size().lines-3
    sizey=os.get_terminal_size().columns-7
    ikey={}
    nkey={}
    selectx,selecty=0,0
    change=False
    theme=themes["default"]
    ybefore=y
    scrolled=True
    need_update=[]
    def print_info():
        gotoxy(size+1,1)
        fsize=os.get_terminal_size().columns-30
        filename=" "*fsize
        print(f"\033[1;47;30m %6s  %s   ln: %4d col: %4d\033[1;0m"%(mode,filename,x,y))
    def pyins(ch):
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,scrolled
        if ch=='\r':
            if y!=-1 and code[x][y]==':':
                code.insert(x+1,[" "]*(1+count_tab(x))*tab+code[x][y+1:])
                code[x]=code[x][:y+1]
                x+=1
                y=count_tab(x-1)*tab+tab-1
            else:
                code.insert(x+1,[" "]*count_tab(x)*tab+code[x][y+1:])
                code[x]=code[x][:y+1]
                x+=1
                y=count_tab(x-1)*tab-1
            scrolled=True
        elif ch=='\t':
            for i in range(tab):
                code[x].insert(y+1," ")
                y+=1
            need_update.append(x)
        elif ord(ch)>=128:
            code[x].insert(y+1,"")
            y+=1
            code[x].insert(y+1,ch)
            y+=1
            need_update.append(x)
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
            need_update.append(x)
        else:
            code[x].insert(y+1,ch)
            y+=1
            need_update.append(x)
    def pydel():
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,scrolled
        if y==-1:
            if x!=0:
                x-=1
                y=len(code[x])-1
                code[x]+=code[x+1]
                del code[x+1]
                scrolled=True
        elif code[x][y-tab+1:y+1]==[" "]*tab:
            del code[x][y-tab+1:y+1]
            y-=tab
            need_update.append(x)
        elif "".join(code[x][y:y+2]) in ("()","[]","{}",'""',"''"):
            del code[x][y:y+2]
            y-=1
            need_update.append(x)
        elif y!=-1 and ord(code[x][y])>=128:
            del code[x][y-1:y+1]
            y-=2
            need_update.append(x)
        else:
            del code[x][y]
            y-=1
            need_update.append(x)
    def firstWord()->str:
        i=0
        while i<len(code[x]) and code[x][i]==" ":
            i+=1
        s=""
        while i<len(code[x]) and (code[x][i].isalnum() or code[x][i]=="_"):
            s+=code[x][i]
            i+=1
        return s
    def rainins(ch):
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,scrolled
        if ch=='\r':
            fw=firstWord()
            if code[x] and code[x][y] in '([{':
                code.insert(x+1,[" "]*(count_tab(x)+1)*tab)
                code.insert(x+2,[" "]*(count_tab(x))*tab+code[x][y+1:])
                code[x]=code[x][:y+1]
                x+=1
                y=count_tab(x-1)*tab+tab-1
            elif y+1<len(code[x]) and code[x][y+1] in ')]}' or\
            fw in ["for","elif","else","if","while","module","switch","fn"]:
                code.insert(x+1,[" "]*(1+count_tab(x))*tab+code[x][y+1:])
                code[x]=code[x][:y+1]
                x+=1
                y=count_tab(x-1)*tab+tab-1
            else:
                code.insert(x+1,[" "]*count_tab(x)*tab+code[x][y+1:])
                code[x]=code[x][:y+1]
                x+=1
                y=count_tab(x-1)*tab-1
            scrolled=True
        elif ch=='\t':
            for i in range(tab):
                code[x].insert(y+1," ")
                y+=1
            need_update.append(x)
        elif ord(ch)>=128:
            code[x].insert(y+1,"")
            y+=1
            code[x].insert(y+1,ch)
            y+=1
            need_update.append(x)
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
            need_update.append(x)
        else:
            code[x].insert(y+1,ch)
            y+=1
            need_update.append(x)
    def raindel():
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,scrolled
        if y==-1:
            if x!=0:
                x-=1
                y=len(code[x])-1 
                code[x]+=code[x+1]
                del code[x+1]
                scrolled=True
        elif code[x][y-tab+1:y+1]==[" "]*tab:
            del code[x][y-tab+1:y+1]
            y-=tab
            need_update.append(x)
        elif "".join(code[x][y:y+2]) in ("()","[]","{}",'""',"''"):
            del code[x][y:y+2]
            y-=1
            need_update.append(x)
        elif ord(code[x][y])>=128:
            del code[x][y-1:y+1]
            y-=2
            need_update.append(x)
        else:
            del code[x][y]
            y-=1
            need_update.append(x)
    def cppins(ch):
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,scrolled
        if ch=='\t':
            for i in range(tab):
                code[x].insert(y+1," ")
                y+=1
            need_update.append(x)
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
            need_update.append(x)
        elif ch=='\r':
            if code[x] and code[x][y]==':':
                code.insert(x+1,[" "]*(1+count_tab(x))*tab+code[x][y+1:])
                code[x]=code[x][:y+1]
                x+=1
                y=count_tab(x-1)*tab+tab-1
            elif code[x] and code[x][y] in '([{':
                if y<len(code[x])-1 and code[x][y+1] in ')]}':
                    code.insert(x+1,[" "]*(count_tab(x)+1)*tab)
                    code.insert(x+2,[" "]*(count_tab(x))*tab+code[x][y+1:])
                    code[x]=code[x][:y+1]
                    x+=1
                    y=count_tab(x-1)*tab+tab-1
                else:
                    code.insert(x+1,[" "]*(1+count_tab(x))*tab+code[x][y+1:])
                    code[x]=code[x][:y+1]
                    x+=1
                    y=count_tab(x-1)*tab+tab-1
            else:
                code.insert(x+1,[" "]*count_tab(x)*tab+code[x][y+1:])
                code[x]=code[x][:y+1]
                x+=1
                y=count_tab(x-1)*tab-1
            scrolled=True
        elif ord(ch)>=128:
            code[x].insert(y+1,"")
            y+=1
            code[x].insert(y+1,ch)
            y+=1
            need_update.append(x)
        else:
            code[x].insert(y+1,ch)
            y+=1
            need_update.append(x)
    def cppdel():
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,scrolled
        if y==-1:
            if x!=0:
                x-=1
                y=len(code[x])-1
                code[x]+=code[x+1]
                del code[x+1]
                scrolled=True
        elif "".join(code[x][y-tab+1:y+1])==" "*tab:
            del code[x][y-tab+1:y+1]
            y-=tab
            need_update.append(x)
        elif "".join(code[x][y:y+2]) in ("()","[]","{}",'""',"''"):
            del code[x][y:y+2]
            y-=1
            need_update.append(x)
        elif ord(code[x][y])>=128:
            del code[x][y-1:y+1]
            y-=2
            need_update.append(x)
        else:
            del code[x][y]
            y-=1
            need_update.append(x)
    def pure_insert(s:str):
        nonlocal x,y,scrolled
        if "\n" in s:
            scrolled=True
        else:
            need_update.append(x)
        for i in s:
            if i=='\n':
                code.insert(x+1,code[x][y+1:])
                code[x]=code[x][:y+1]
                x+=1
                y=-1
            elif ord(i)>=128:
                code[x].insert(y+1,"")
                y+=1
                code[x].insert(y+1,i)
                y+=1
            else:
                code[x].insert(y+1,i)
                y+=1
    def pure_delete(t:int=1):
        nonlocal x,y,scrolled
        need_update.append(x)
        for i in range(t):
            if y==-1:
                if x!=0:
                    x-=1
                y=len(code[x])-1
                code[x]+=code[x+1]
                del code[x+1]
                scrolled=True
            elif ord(code[x][y])>=128:
                del code[x][y-1:y+1]
                y-=2
            else:
                del code[x][y]
                y-=1
    lang_cfg={
        "py":{
            "ins":pyins,
            "del":pydel,
            "render":py.render,
            "run":py.run,
        },
        "rain":{
            "ins":rainins,
            "del":raindel,
            "render":rain.render,
            "run":rain.rrun,
        },
        "cpp":{
            "ins":cppins,
            "del":cppdel,
            "render":cpp.render,
            "run":cpp.run,
        },
        "c":{
            "ins":cppins,
            "del":cppdel,
            "render":c.render,
            "run":c.run,
        },
        "nl":{
            "ins":cppins,
            "del":cppdel,
            "render":newlang.render,
            "run":newlang.run,
        },
        "js":{
            "ins":cppins,
            "del":cppdel,
            "render":js.render,
            "run":js.run,
        },
        "txt":{
            "ins":pure_insert,
            "del":pure_delete,
            "render":txt.render,
            "run":txt.run,
        }
    }
    def _ins(ch):
        lang_cfg[lang]["ins"](ch)
    def _del(ch):
        lang_cfg[lang]["del"](ch)
    def _run():
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab
        clear()
        if save:
            lang_cfg[lang]["run"](save)
        else:
            print("请保存后运行")
        getch()
    def _render(ch):
        lang_cfg[lang]["render"](ch)
    '''def getall():
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
        return res'''
    def count_tab(line):
        i=0
        while i<len(code[line]) and code[line][i]==' ':
            i+=1
        return (i+1)//tab
    def NORMAL_do(ch):
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,change,delay,ybefore,scrolled
        if ch=='v':
            mode="SELECT"
            selectx,selecty=x,y
        elif ch=='p':
            _paste()
            change=True
            scrolled=True
        elif ch=='i':
            mode="INSERT"
        elif ch=='z':
            if history:
                code,x,y=history.pop()
                change=True
        elif ch=='k':
            if x!=0:
                x-=1
                y=ybefore
            else:
                y=-1
                ybefore=y
            if y>=len(code[x]):
                y=len(code[x])-1
            if len(code[x]) and code[x][y]=="":
                y+=1
        elif ch=='j':
            if x!=len(code)-1:
                x+=1
                y=ybefore
            else:
                y=len(code[x])-1
                ybefore=y
            if y>=len(code[x]):
                y=len(code[x])-1
            if len(code[x]) and code[x][y]=="":
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
            ybefore=y
        elif ch=='l':
            if y!=len(code[x])-1:
                if code[x][y+1]=="":
                    y+=1
                y+=1
            else:
                if x!=len(code)-1:
                    x+=1
                    y=-1
            ybefore=y
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
            _run()
            scrolled=True
        elif ch==':':
            gotoxy(size+2,1)
            cmd=input(':')
            do(cmd)
    def INSERT_do(ch):
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,change,delay,ybefore
        if ord(ch)==27:
            mode="NORMAL"
        else:
            change=True
            lang_cfg[lang]["ins"](ch)
            ybefore=y
    def v_copy():
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,change,delay
        if x==selectx:
            if y<selecty:
                copy("".join(code[x][y+1:selecty+1]))
            else:
                copy("".join(code[x][selecty+1:y+1]))
        elif x<selectx:
            s="".join(code[x][y+1:])+"\n"
            for i in range(x+1,selectx):
                s+="".join(code[i])+"\n"
            s+="".join(code[selectx][:selecty+1])
            copy(s)
        else:
            s="".join(code[selectx][selecty+1:])+"\n"
            for i in range(selectx+1,x):
                s+="".join(code[i])+"\n"
            s+="".join(code[x][:y+1])
            copy(s)
        x=min(x,len(code)-1)
        y=min(y,len(code[x])-1)
    def get_all_selected():
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,change,delay
        if x==selectx:
            if y<selecty:
                return {x:(y+1,selecty+1)}
            else:
                return {x:(selecty+1,y+1)}
        elif x<selectx:
            res={x:(y+1,len(code[x]))}
            for i in range(x+1,selectx):
                res[i]=(0,len(code[i]))
            res[selectx]=(0,selecty+1)
            return res
        else:
            res={selectx:(selecty+1,len(code[selectx]))}
            for i in range(selectx+1,x):
                res[i]=(0,len(code[i]))
            res[x]=(0,y+1)
            return res
    def _paste():
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,change,delay,ybefore
        s=paste()
        for i in s:
            if i=='\n':
                code.insert(x+1,code[x][y+1:])
                code[x]=code[x][:y+1]
                x+=1
                y=-1
            elif i=='\r':
                ...
            elif ord(i)>=128:
                code[x].insert(y+1,"")
                y+=1
                code[x].insert(y+1,i)
                y+=1
            else:
                code[x].insert(y+1,i)
                y+=1
    def do_cmd(ch):
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,change,delay,ybefore,scrolled
        if ord(ch)==224:
            ch=ord(getch())
            if ch==72:
                if x!=0:
                    x-=1
                    y=ybefore
                else:
                    y=-1
                    ybefore=y
                if y>=len(code[x]):
                    y=len(code[x])-1
                if len(code[x]) and code[x][y]=="":
                    y+=1
            elif ch==80:
                if x!=len(code)-1:
                    x+=1
                    y=ybefore
                else:
                    y=len(code[x])-1
                    ybefore=y
                if y>=len(code[x]):
                    y=len(code[x])-1
                if len(code[x]) and code[x][y]=="":
                    y+=1
            elif ch==75:
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
                ybefore=y
            elif ch==77:
                if y!=len(code[x])-1:
                    if code[x][y+1]=="":
                        y+=1
                    y+=1
                else:
                    if x!=len(code)-1:
                        x+=1
                        y=-1
                ybefore=y
            elif ch==81:
                x=min(x+size-2,len(code)-1)
                y=min(ybefore,len(code[x])-1)
                if len(code[x]) and code[x][y]=="":
                    y+=1
            elif ch==73:
                x=max(x-size+2,0)
                y=min(ybefore,len(code[x])-1)
                if len(code[x]) and code[x][y]=="":
                    y+=1
            elif ch==71:
                y=-1
                ybefore=y
            elif ch==79:
                y=len(code[x])-1
                ybefore=y
            return
        elif ord(ch)==14:#Ctrl-N，启动代码补全
            words=getAllWord("\n".join(map("".join,code)))
            word=""
            while y>=0 and (code[x][y].isalnum() or code[x][y]=='_'):
                word=code[x][y]+word
                del code[x][y]
                y-=1
            def include(_word:str):
                p=0
                for i in _word:
                    if p==len(word):
                        return True
                    if i==word[p]:
                        p+=1
                return False
            words=list(filter(include,words))
            words=list(set(words))
            choice=choose_word(words,size+1,os.get_terminal_size().columns)
            if choice=="":
                pure_insert(word)
            else:
                pure_insert(choice)
                change=True
        elif (ord(ch)==8 and mode!="SELECT") or (ch=='d' and mode=="NORMAL"):
            change=True
            lang_cfg[lang]["del"]()
            ybefore=y
        elif mode=="NORMAL":
            if ch in nkey:
                k=nkey[ch]
                while type(k)==dict:
                    time.sleep(1)
                    if msvcrt.kbhit():
                        ch=getch()
                        if ch in k:
                            k=k[ch]
                    else:
                        if "" in k:
                            k[""]()
                        break
                else:
                    k()
            else:
                NORMAL_do(ch)
        elif mode=="SELECT":
            if ord(ch)==27:
                mode="NORMAL"
                scrolled=True
            elif ch=='d' or ord(ch)==8:
                change=True
                mode="INSERT"
                if x==selectx:
                    if y<selecty:
                        del code[x][y+1:selecty+1]
                    else:
                        del code[x][selecty+1:y+1]
                        y=selecty
                elif x<selectx:
                    del code[selectx][:selecty+1]
                    del code[x][y+1:]
                    code[x]+=code[selectx]
                    del code[selectx]
                    for i in range(x+1,selectx):
                        del code[x+1]
                else:
                    del code[selectx][selecty+1:]
                    del code[x][:y+1]
                    code[selectx]+=code[x]
                    del code[x]
                    for i in range(selectx+2,x):
                        del code[selectx+1]
                    x=selectx
                    y=selecty
                x=min(x,len(code)-1)
                y=min(y,len(code[x])-1)
                scrolled=True
            elif ch=='c':
                v_copy()
            elif ch=='k':
                if x!=0:
                    x-=1
                    y=ybefore
                else:
                    y=-1
                    ybefore=y
                if y>=len(code[x]):
                    y=len(code[x])-1
                    ybefore=y
                if len(code[x]) and code[x][y]=="":
                    y+=1
            elif ch=='j':
                if x!=len(code)-1:
                    x+=1
                    y=ybefore
                else:
                    y=len(code[x])-1
                if y>=len(code[x]):
                    y=len(code[x])-1
                if len(code[x]) and code[x][y]=="":
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
                ybefore=y
            elif ch=='l':
                if y!=len(code[x])-1:
                    if code[x][y+1]=="":
                        y+=1
                    y+=1
                else:
                    if x!=len(code)-1:
                        x+=1
                        y=-1
                ybefore=y
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
                k=ikey[ch]
                chs=ch
                while type(k)==dict:
                    time.sleep(1)
                    if msvcrt.kbhit():
                        ch=getch()
                        chs+=ch
                        if ch in k:
                            k=k[ch]
                        else:
                            for i in chs:
                                INSERT_do(i)
                            break
                    else:
                        if "" in k:
                            k[""]()
                        else:
                            for i in chs:
                                INSERT_do(i)
                        break
                else:
                    k()
            else:
                INSERT_do(ch)
    def do(cmd):
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,change,delay,theme,ybefore,scrolled
        head=cmd.split(" ")[0]
        cmd=cmd[len(head)+1:]
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
NORMAL :tab num：设置缩进的宽度
NORMAL news：显示更新内容
NORMAL :delay time：设置延迟时间
Arrows：上下左右（需要安装并启用XesExt）
Ctrl-C：退出编辑器
''')
            getch()
        elif head=="size":
            try:
                cmd=cmd.split(" ")
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
        elif head=="w" or head=="write":
            if cmd:
                save=cmd
            if save!="":
                with open(save,'w',encoding='utf-8') as f:
                    f.write("\n".join(map("".join,code)))
                gotoxy(size+2,1)
                print(f"File is saved to {save}.")
            else:
                gotoxy(size+2,1)
                print(f"Expect save path.")
        elif head=="o" or head=="open":
            if cmd:
                save=cmd
            if save!="":
                _o()
                gotoxy(size+2,1)
                x=min(x,len(code)-1)
                y=min(y,len(code[x])-1)
            else:
                gotoxy(size+2,1)
                print(f"Expect save path.")
            clear()
        elif head=="tab":
            tab=int(cmd)
        elif head=="delay":
            delay=float(cmd)
        elif head=="theme":
            theme=themes.get(cmd,theme)
            scrolled=True
            change=True
    def _set(n,v):
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,change,delay,ybefore
        if n=="history":
            history=v
        if n=="delay":
            delay=v
        if n=="x":
            x=v
        if n=="y":
            y=v
        if n=="mode":
            mode=v
        if n=="begin":
            begin=v
        if n=="beginy":
            beginy=v
        if n=="size":
            size=v
        if n=="sizey":
            sizey=v
        if n=="change":
            change=v
        if n=="code":
            code=v
        if n=="nu":
            nu=v
        if n=="tab":
            tab=v
        if n=="ybefore":
            ybefore=v
    def _set_lang_cfg(lang,key,value):
        nonlocal lang_cfg
        if lang not in lang_cfg:
            lang_cfg[lang]={}
        lang_cfg[lang][key]=value
    def __map(key:str,_key:list,fn):
        if len(key)==1:
            _key[0][key]=fn
        else:
            if type(_key[0])!=dict:
                _key[0]={"":_key[0]}
            if key[0] not in _key[0]:
                _key[0][key[0]]={}
            __map(key[1:],[_key[0][key[0]]],fn)
    def imap(key,fn):
        __map(key,[ikey],fn)
    def nmap(key,fn):
        __map(key,[nkey],fn)
    def _newtheme(name,value):
        themes[name]=value
    def update_line(i,_i):
        gotoxy(_i-begin+1,1)
        print(" "*sizey)
        gotoxy(_i-begin+1,1)
        if nu:
            print("\033[1;0m%4d | "%(_i+1),flush=True,end="")
        print("".join(i[beginy:beginy+sizey]))
    rain.scope.var["python_editor_config"]={
        "do":do,
        "get":lambda s:{
            "history":history,
            "delay":delay,
            "x":x,
            "y":y,
            "mode":mode,
            "begin":begin,
            "beginy":beginy,
            "size":size,
            "sizey":sizey,
            "change":change,
            "code":code,
            "nu":nu,
            "tab":tab,
            "ybefore":ybefore,
        }[s],
        "set":_set,
        "set_lang_cfg":_set_lang_cfg,
        "get_lang_cfg":lambda:lang_cfg,
        "imap":imap,
        "nmap":nmap,
        "v_copy":v_copy,
        "paste":_paste,
        "get_paste":paste,
        "newtheme":_newtheme,
        "pure_insert":pure_insert,
        "pure_delete":pure_delete,
    }
    rain.run_code(rain.parse(rain.lex(open(dire+"config.rain",'r',encoding='utf-8').read())),rain.scope)
    rr=lang_cfg[lang]["render"]("\n".join(map("".join,code)),theme)
    while 1:
        if lang not in lang_cfg:
            lang="txt"
        size=os.get_terminal_size().lines-3
        sizey=os.get_terminal_size().columns-(7 if nu else 0)
        change=False
        if x<begin:
            begin=x
            scrolled=True
        if x>=begin+size:
            begin=x-size+1
            scrolled=True
        if y<beginy:
            beginy=y+1
            if y!=-1:
                scrolled=True
        if y>=beginy+sizey-1:
            beginy=y-sizey+2
            scrolled=True
        if len(rr)<len(code):
            rr+=[[]]
        #clear()
        gotoxy(1,1)
        if scrolled or mode=="SELECT":
            clear()
            if mode=="SELECT":
                gar=get_all_selected()
                for i in range(begin,min(begin+size,len(rr))):
                    if nu:
                        print("\033[1;0m%4d | "%(i+1),flush=True,end="")
                    for j in range(beginy,min(beginy+sizey,len(rr[i]))):
                        '''
                            selectx<=i<=x and (selectx<i<x or i==selectx and j<=selecty or i==x and j>=y) or
                            x<=i<=selectx and (x<i<selectx or i==x and j<=y or i==selectx and j>=selecty)
                        '''
                        if i in gar and gar[i][0]<=j<gar[i][1]:
                            if rr[i][j]:
                                print("\033[1;0m"+rr[i][j][:-1]+"\033[1;47m"+rr[i][j][-1],end="")
                        else:
                            '''if rr[i][j]:
                                print("\033[1;0m"+rr[i][j][:-1]+"\033[1;43m"+rr[i][j][-1],end="\033[1;0m")'''
                            print("\033[1;0m"+rr[i][j],end="\033[1;0m")
                        #time.sleep(0.1)
                    print("\033[1;0m")
                #gotoxy(size+3,1)
                #print(gar,selectx,selecty)
            else:
                _i=begin
                for i in rr[begin:begin+size]:
                    if nu:
                        print("\033[1;0m%4d | "%(_i+1),flush=True,end="")
                    print("".join(i[beginy:beginy+sizey]))
                    _i+=1
        else:
            for i in set(need_update):
                if i>=begin and i<begin+size:
                    update_line(rr[i],i)
        #gotoxy(size+1,1)
        #print("\033[1;0m",mode)
        print_info()
        #print(scrolled)
        scrolled=False
        need_update=[]
        if not nu:
            gotoxy(x+1-begin,y+2-beginy)
        else:
            gotoxy(x+1-begin,y+9-beginy)
        #print("\033[1;47m \033[1;0m")
        ch=getch()
        if ord(ch)==3:
            break
        else:
            do_cmd(ch)
        time.sleep(delay)
        while msvcrt.kbhit():
            ch=getch()
            if ord(ch)==3:
                break
            else:
                do_cmd(ch)
            time.sleep(delay)
        if change:
            rr=lang_cfg[lang]["render"]("\n".join(map("".join,code)),theme)
            history.append((deepcopy(code),x,y))
        #clear()
def choose(choices:list,start_row):
    now=0
    while 1:
        for i in range(len(choices)):
            gotoxy(i+2,start_row)
            print(choices[i])
        gotoxy(now+2,start_row)
        print("\033[1;44m"+choices[now]+"\033[1;0m",flush=True,end="")
        ch=getch()
        if ch=='\r':
            break
        elif ord(ch)==224:
            ch=ord(getch())
            if ch==72:
                now-=1
            if ch==80:
                now+=1
        elif ord(ch)==27:
            return ""
        now+=len(choices)
        now%=len(choices)
    return choices[now]
def getFileType(n:str):
    return n[n.rfind('.')+1:]
dire=__file__[:__file__.rfind("\\")+1]
try:
    open(dire+"config.rain",'r',encoding='utf-8')
except OSError:
    open(dire+"config.rain",'w',encoding='utf-8').write("#Python Editor的配置文件")
l=[
    "New",
    "Open",
    "Exit",
]
while 1:
    clear()
    a=choose(l,1)
    if a=="" or a=="Exit":
        break
    if a=="New":
        clear()
        save=input("path>")
        try:
            open(save,encoding="utf-8")
        except OSError:
            open(save,'w',encoding="utf-8").write("")
            edit(getFileType(save),save)
    if a=="Open":
        clear()
        save=input("path>")
        try:
            open(save,encoding="utf-8")
            edit(getFileType(save),save)
        except OSError:...
