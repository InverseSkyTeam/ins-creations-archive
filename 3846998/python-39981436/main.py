'''
F1/F2/F3/F4 up/down/left/right
Backspace/Alt-Backspace back
F11 run（暂不支持）
F5 quit
'''
keywords=[
    "var",
    "if",
    "else",
    "while",
    "for",
    "foreach",
    "switch",
    "case",
    "default",
    "try",
    "except",
    "throw",
    "break",
    "continue",
    "return",
    "func",
    "class",
    "module",
    "object",
    "lambda",
    "anonymous_class",
    "anonymous_module",
    "cons",
    "import",
]
def render(code):
    print("\033[1;47m",end="")
    print("\033[1;30m",end="")
    while code!="":
        if code[0].isdigit():
            s=code[0]
            code=code[1:]
            while code!="" and (code[0].isdigit() or code[0]=='.'):
                s+=code[0]
                code=code[1:]
            print("\033[1;34m"+s+"\033[1;0m\033[1;47m\033[1;30m",end="")
        elif code[0].isalpha() or code[0]=="_":
            s=code[0]
            code=code[1:]
            while code!="" and (code[0].isalnum() or code[0]=='_'):
                s+=code[0]
                code=code[1:]
            if s in keywords:
                print("\033[1;34m"+s+"\033[1;0m\033[1;47m\033[1;30m",end="")
            else:
                print(s,end="")
        elif code[0]=='"':
            code=code[1:]
            s=""
            while code!="" and code[0]!='"':
                if code[0]=='\\':
                    code=code[1:]
                    if code!="" and code[0]=='"':
                        code=code[1:]
                        s+='\\"'
                        continue
                    else:
                        s+='\\'
                s+=code[0]
                code=code[1:]
            code=code[1:]
            print("\033[0;47;32m\""+s+"\"\033[1;0m\033[1;47m\033[1;30m",end="")
        else:
            print(code[0],end="")
            code=code[1:]
    print("\033[1;0m")
from os import system
import sys
from time import sleep
def gotoxy(x,y):
    print(f"\033[{x};{y}f",end="")
def getch():
    system("stty -icanon")
    system("stty -echo")
    res=sys.stdin.read(1)
    system("stty icanon")
    system("stty echo");
    return res
def IDE():
    code=""
    p=[1,0]
    while 1:
        print("\033[1;47m",end="")
        for i in range(15):
            print(" "*50)
        gotoxy(1,1)
        render(code)
        gotoxy(p[0],p[1]+1)
        print("\033[1;40m \033[1;0m")
        gotoxy(1,1)
        sleep(0.1)
        cmd=getch()
        system("clear")
        gotoxy(20,1)
        print(ord(cmd))
        gotoxy(1,1)
        if ord(cmd)==27:
            cmd=getch()
            if ord(cmd)==79:
                cmd=ord(getch())
                if cmd==80:
                    p[0]=max(0,p[0]-1)
                if cmd==81:
                    p[0]=p[0]+1
                if cmd==82:
                    p[1]=max(0,p[1]-1)
                if cmd==83:
                    p[1]=p[1]+1
            elif ord(cmd)==127:
                if code=="":
                    continue
                flat,line=0,1
                while line!=p[0]:
                    if code[flat]=='\n':
                        line+=1
                    flat+=1
                lcode=list(code)
                ch=lcode[flat+p[1]-1]
                del lcode[flat+p[1]-1]
                code="".join(lcode)
                if ch=='\n':
                    p[0]-=1
                    __flat,_flat,_line=0,0,1
                    while _line!=p[0]:
                        if code[__flat]=='\n':
                            _line+=1
                        __flat+=1
                    while __flat+_flat<len(code) and code[__flat+_flat]!='\n':
                        _flat+=1
                    p[1]=_flat
                else:
                    p[1]-=1
        elif ord(cmd)==127:
            if code=="":
                continue
            flat,line=0,1
            while line!=p[0]:
                if code[flat]=='\n':
                    line+=1
                flat+=1
            lcode=list(code)
            ch=lcode[flat+p[1]-1]
            del lcode[flat+p[1]-1]
            code="".join(lcode)
            if ch=='\n':
                p[0]-=1
                __flat,_flat,_line=0,0,1
                while _line!=p[0]:
                    if code[__flat]=='\n':
                        _line+=1
                    __flat+=1
                while __flat+_flat<len(code) and code[__flat+_flat]!='\n':
                    _flat+=1
                p[1]=_flat
            else:
                p[1]-=1
        elif ord(cmd)==126:
            break
        else:
            ch=cmd
            if ch=='(':
                ch='()'
            if ch=='[':
                ch='[]'
            if ch=='{':
                ch='{}'
            if ch=='\t':
                ch='    '
            flat,line=0,1
            while line!=p[0] and flat<len(code):
                if code[flat]=='\n':
                    line+=1
                flat+=1
            code=code[:flat+p[1]]+ch+code[flat+p[1]:]
            if cmd=='\n':
                p[1]=0
                p[0]+=1
            elif cmd=='\t':
                p[1]+=4
            else:
                p[1]+=1
IDE()