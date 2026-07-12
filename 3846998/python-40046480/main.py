'''
F1-F4 up/down/left/right
F7/F8/F6
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
from time import time,sleep
class Printer:
    def __init__(self):
        self.wordcnt=0
        self.starttime=time()
    def __call__(self,*text,sep=" ",flush=True,end="\n"):
        t=sep.join([str(i) for i in text])
        for i in t:
            print(i,flush=True,end="")
            self.wordcnt+=1
            if self.wordcnt>=1000 and time()-self.starttime<=0.2:
                sleep(0.15)
                self.wordcnt=0
            elif self.wordcnt>=1000:
                self.wordcnt=0
                self.starttime=time()
        print(end,end="")
words=list(keywords)
printer=Printer()
def render(code):
    words=list(keywords)
    res="\033[1;47m\033[1;30m"
    while code!="":
        if code[0].isdigit():
            s=code[0]
            code=code[1:]
            while code!="" and (code[0].isdigit() or code[0]=='.'):
                s+=code[0]
                code=code[1:]
            res+="\033[1;34m"+s+"\033[1;0m\033[1;47m\033[1;30m"
        elif code[0].isalpha() or code[0]=="_":
            s=code[0]
            code=code[1:]
            while code!="" and (code[0].isalnum() or code[0]=='_'):
                s+=code[0]
                code=code[1:]
            if s in keywords:
                res+="\033[1;34m"+s+"\033[1;0m\033[1;47m\033[1;30m"
            else:
                if s not in words:
                    words.append(s)
                res+=s
        elif code[0]=='"':
            code=code[1:]
            s='"'
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
            if code!="":
                s+=code[0]
                code=code[1:]
            res+="\033[0;47;32m"+s+"\033[1;0m\033[1;47m\033[1;30m"
        elif len(code)>1 and code[0]==code[1]=='/':
            res+="\033[0;47;32m"
            res+=code[:2]
            code=code[2:]
            while code!="" and code[0]!='\n':
                res+=code[0]
                code=code[1:]
            res+="\033[1;0m\033[1;47m\033[1;30m"
        elif len(code)>1 and code[0]=='/' and code[1]=='*':
            res+="\033[0;47;32m"
            res+=code[:2]
            code=code[2:]
            while len(code)>1 and code[:2]!='*/':
                res+=code[0]
                code=code[1:]
            res+=code[:2]
            code=code[2:]
            res+="\033[1;0m\033[1;47m\033[1;30m"
        else:
            res+=code[0]
            code=code[1:]
    res+="\033[1;0m"
    return res
from os import system
import sys
def gotoxy(x,y):
    printer(f"\033[{x};{y}f",end="")
def getch():
    system("stty -icanon")
    system("stty -echo")
    res=sys.stdin.read(1)
    system("stty icanon")
    system("stty echo")
    return res
def IDE():
    code=[[] for i in range(15)]
    line,row=0,0
    begin,end=0,15
    def print_info(text,line=17):
        gotoxy(line,1)
        printer(" "*50)
        gotoxy(line,1)
        printer(text)
        gotoxy(1,1)
    def count_tab():
        nonlocal code,line
        n=0
        while n<len(code[line]) and code[line][n]==' ':
            n+=1
        return n//4
    def delc():
        nonlocal code,line,row
        if row==0 and line>0:
            row=len(code[line-1])
            _=code[line-1]+code[line]
            del code[line]
            code[line-1]=_
            line-=1
        elif row>0:
            row-=1
            del code[line][row]
    def addc(ch):
        nonlocal code,line,row
        if ch=='\n':
            tabcnt=count_tab()
            #print(tabcnt)
            #sleep(2)
            if len(code)!=line:
                code.insert(line+1,code[line][row:])
            else:
                code.append(code[line][row:])
            if len(code[line]) and code[line][-1]=='{':
                tabcnt+=1
            code[line+1]=[' ']*(tabcnt*4)+code[line+1]
            code[line]=code[line][:row]
            line+=1
            row=tabcnt*4
        else:
            if ch=='}' and code[line][0:4]==[' ',' ',' ',' ']:
                code[line]=code[line][4:]
            if ch=='\t':
                ch='    '
            for i in ch:
                if row<len(code[line]):
                    code[line].insert(row,i)
                else:
                    code[line].append(i)
                row+=1
    while 1:
        if row>=max(len(code[line]),1):
            row=len(code[line])
        if line>=end:
            end+=1
            begin+=1
            if line>len(code):
                code.append([])
        if line<begin:
            end-=1
            begin-=1
        print_info(f"{line} {row}",18)
        gotoxy(1,1)
        printer("\033[1;47m",end="")
        for i in range(15):
            printer(" "*50)
        printer("\033[1;0m")
        gotoxy(1,1)
        printer("\n".join(render("\n".join(["".join(i) for i in code])).split("\n")[begin:end]))
        gotoxy(line-begin+1,row+1)
        printer("\033[1;40m \033[1;0m")
        gotoxy(1,1)
        cmd=getch()
        if ord(cmd)==27:
            cmd=getch()
            if ord(cmd)==79:
                cmd=ord(getch())
                if cmd==80 and line>=0:
                    line-=1
                if cmd==81 and line<len(code):
                    line+=1
                if cmd==82 and row>=0:
                    row-=1
                if cmd==82 and row==-1 and line>=0:
                    line-=1
                    row=len(code[line])
                if cmd==83 and row<=len(code[line]):
                    row+=1
                if cmd==83 and row>len(code[line]) and line<len(code):
                    line+=1
                    row=0
            elif ord(cmd)==127:
                print_info(f"delc {line} {row}")
                delc()
        elif ord(cmd)==127:
            print_info(f"delc {line} {row}")
            delc()
        else:
            print_info(f"addc {ord(cmd)} {line} {row}")
            addc(cmd)
        #sleep(0.2)
        system("clear")
        #print_info(code,19)
IDE()