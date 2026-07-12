import sys,os,time,pyperclip
import msvcrt
from copy import deepcopy
import copy,sys,time
#Rain{
kw=[
    'if','else','elif','end','while','fn','var','for','return','break','continue','in','to','step','where','import',
    'and','or','not','True','False','None',
]
op=[
    '+','-','*','/','%',
    '==','!=','>','<','>=','<=',
    '<<','>>','&','|','^','~',
    ',','.','(',')','[',']','{','}',':','=',
]
escape={
    'r':'\r',
    't':'\t',
    'a':"\a",
    'f':'\f',
    'v':"\v",
    'b':"\b",
    'n':"\n",
    '"':'"',
    "'":"'",
    '\\':'\\',
}
prio={
    '*':100,'/':100,'%':100,
    '+':99,'-':99,
    '<<':98,'>>':98,
    '==':97,'!=':97,
    '>':96,'<':96,'>=':96,'<=':96,
    '&':95,'^':94,'|':93,
    '*and':92,'*or':91,
}
VarDecl,If,While,ForTo,ForIn,Return,Break,Continue,FnDef,Assign,NoOp,Import,\
    Const,Var,Binary,Unary,Index,Call,NewObject,NewList,NewFn,Where,\
        =[i for i in range(22)]
class Scope:
    def __init__(self,parent,var:dict):
        self.parent,self.var=parent,var
    def find(self,name:str):
        if name in self.var:
            return self.var[name]
        elif self.parent:
            return self.parent.find(name)
        else:
            raise Exception(f"变量{name}未定义。")
    def set(self,name:str,value):
        if name in self.var:
            self.var[name]=value
        elif self.parent:
            self.parent.set(name,value)
        else:
            raise Exception(f"变量{name}未定义。")
    def define(self,name:str,value):
        self.var[name]=value
class Signal:
    def __init__(self,signal:int,value=None):
        self.signal,self.value=signal,value
    def __eq__(self,b):
        return type(b)==Signal and type(self)==Signal and b.signal==self.signal
class Function:
    def __init__(self,para,body,closure):
        self.para,self.body,self.closure=para,body,closure
    def __call__(self,*args):
        scope=Scope(self.closure,dict(zip(self.para,args)))
        v=run_code(self.body,scope)
        if v!=None:
            return v.value
        return None
class Method:
    def __init__(self,obj:dict,func:Function):
        self.obj,self.func=obj,func
    def __call__(self,*args):
        scope=Scope(self.func.closure,dict(zip(self.func.para,(self.obj,)+args)))
        v=run_code(self.func.body,scope)
        if v!=None:
            return v.value
        return None
def lex(code:str):
    p=0
    res=[]
    while p<len(code):
        while p<len(code) and code[p] in " \n\t#":
            if code[p]=='#':
                while p<len(code) and code[p]!='\n':
                    p+=1
            else:
                p+=1
        if p==len(code):
            break
        elif code[p].isdigit():
            s=""
            while p<len(code) and (code[p].isdigit() or code[p]=='.'):
                s+=code[p]
                p+=1
            res.append(s)
        elif code[p].isalpha() or code[p]=='_':
            s=""
            while p<len(code) and (code[p].isalnum() or code[p]=='_'):
                s+=code[p]
                p+=1
            if s in kw:
                res.append('*'+s)
            else:
                res.append(s)
        elif code[p]=='"':
            s='"'
            p+=1
            while p<len(code) and code[p]!='"':
                if code[p]=='\\':
                    p+=1
                    if p==len(code):
                        raise Exception("无法结束的转义字符。")
                    if code[p].isdigit():
                        if p+3>=len(code):
                            raise Exception("无法结束的转义字符。")
                        s+=chr(int(code[p:p+3],8))
                        p+=3
                    elif code[p] in escape:
                        s+=escape[code[p]]
                        p+=1
                    else:
                        raise Exception("错误的转义字符。")
                else:
                    s+=code[p]
                    p+=1
            if p==len(code):
                raise Exception("字符串未结束。")
            else:
                res.append(s+'"')
                p+=1
        elif code[p] in op:
            res.append(code[p])
            p+=1
        elif code[p:p+2] in op:
            res.append(code[p:p+2])
            p+=2
        else:
            raise Exception(f"无法识别当前字符'{code[p]}'。")
    return res+[""]
def parse(tokens):
    p=0
    token=tokens[p]
    def eat(ex=None)->str:
        nonlocal p,token
        if token==ex or ex==None:
            p+=1
            token=tokens[p]
            return tokens[p-1]
        else:
            raise Exception(f"当前单词不匹配，期望'{ex}'，得到'{token}'。")
    def block(_end):
        l=[]
        while token not in _end:
            l.append(stmt())
        return l
    def stmt()->tuple:
        if token=='*if':
            eat()
            c=[expr()]
            t=[block(['*end','*else','*elif'])]
            while token=='*elif':
                eat()
                c.append(expr())
                t.append(block(['*end','*else','*elif']))
            if token=='*end':
                eat()
                return (If,c,t,[(NoOp,)])
            else:
                eat('*else')
                f=block(['*end'])
                eat()
                return (If,c,t,f)
        elif token=='*while':
            eat()
            c=expr()
            t=block(['*end'])
            eat()
            return (While,c,t)
        elif token=='*var':
            eat()
            name=[eat_id()]
            if token=='=':
                eat()
                value=[expr()]
            else:
                value=[(Const,None)]
            while token==',':
                name.append(eat_id())
                if token=='=':
                    eat()
                    value.append(expr())
                else:
                    value.append((Const,None))
            return (VarDecl,name,value)
        elif token=='*fn':
            eat()
            name=eat_id()
            eat('(')
            para=[]
            if token!=')':
                para.append(eat_id())
                while token==',':
                    eat()
                    para.append(eat_id())
            eat(')')
            body=block(['*end'])
            eat()
            return (FnDef,name,para,body)
        elif token=='*for':
            eat()
            name=eat_id()
            if token=='*in':#ForIn
                eat()
                obj=expr()
                body=block(['*end'])
                eat()
                return (ForIn,name,obj,body)
            elif token=='=':#ForTo
                eat()
                begin=expr()
                eat('*to')
                end=expr()
                if token=='*step':
                    eat()
                    step=expr()
                else:
                    step=(Const,1)
                body=block(['*end'])
                eat()
                return (ForTo,name,begin,end,step,body)
            else:
                raise Exception("无法解析当前单词")
        elif token=='*import':
            eat()
            return (Import,expr())
        elif token=='*return':
            eat()
            return (Return,expr())
        elif token=='*break':
            eat()
            return (Break,)
        elif token=='*continue':
            eat()
            return (Continue,)
        else:
            l=expr()
            if token=='=':
                eat()
                r=expr()
                return (Assign,l,r)
            return l
    def expr()->tuple:
        res=factor()
        if token in prio:
            res=(Binary,eat(),res,expr())
            while token in prio:
                op=eat()
                if prio[op]<=prio[res[1]]:
                    res=(Binary,op,res,expr())
                else:
                    res=(Binary,res[1],res[2],(Binary,res[3],expr()))
        if token=='*where':
            eat()
            eat('(')
            body=block([')'])
            eat()
            return (Where,res,body)
        return res
    def factor()->tuple:
        res=None
        if token=="":
            raise Exception("代码不应该在此处结束。")
        elif token[0].isdigit():
            if '.' in token:
                res=(Const,float(eat()))
            else:
                res=(Const,int(eat()))
        elif token[0].isalpha() or token[0]=='_':
            res=(Var,eat())
        elif token[0]=='"':
            res=(Const,eat()[1:-1])
        elif token=='*True':
            eat()
            res=(Const,True)
        elif token=='*False':
            eat()
            res=(Const,False)
        elif token=='*None':
            eat()
            res=(Const,None)
        elif token=='(':
            eat()
            if token=="*fn":
                eat()
                eat('(')
                para=[]
                if token!=')':
                    para.append(eat_id())
                    while token==',':
                        eat()
                        para.append(eat_id())
                eat(')')
                body=block([')'])
                eat()
                return (NewFn,para,body)
            res=expr()
            eat(')')
        elif token=='[':
            eat()
            l=[]
            if token!=']':
                l.append(expr())
                while token==',':
                    eat()
                    l.append(expr())
            eat(']')
            res=(NewList,l)
        elif token=='{':
            eat()
            k,v=[],[]
            while token!='}':
                k.append(eat_id())
                eat(':')
                v.append(expr())
                if token==',':
                    eat()
            eat('}')
            res=(NewObject,k,v)
        else:
            raise Exception(f"无法解析当前单词'{token}'。")
        while token in ['[','(','.']:
            if token=='[':
                eat()
                res=(Index,res,expr())
                eat(']')
            elif token=='(':
                eat()
                l=[]
                if token!=')':
                    l.append(expr())
                    while token==',':
                        eat()
                        l.append(expr())
                eat(')')
                res=(Call,res,l)
            elif token=='.':
                eat()
                res=(Index,res,(Const,eat_id()))
        return res
    def eat_id()->str:
        if token[0].isalpha() or token[0]=='_':
            return eat()
        raise Exception("当前单词不是合法标识符。")
    l=[]
    while token!='':
        l.append(stmt())
    return l
def run_code(tree,scope:Scope):
    def run(tree):
        nonlocal scope
        if type(tree)==list:
            for i in tree:
                v=run(i)
                if type(v)==Signal:
                    return v
            return
        tp=tree[0]
        if tp==VarDecl:
            for i in range(len(tree[1])):
                scope.define(tree[1][i],run(tree[2][i]))
        elif tp==If:
            for i in range(len(tree[1])):
                if run(tree[1][i]):
                    return run(tree[2][i])
            return run(tree[3])
        elif tp==While:
            while run(tree[1]):
                v=run(tree[2])
                if v==Signal(Break):
                    break
                if v==Signal(Return):
                    return v
        elif tp==ForTo:
            name=tree[1]
            begin=run(tree[2])
            end=run(tree[3])
            step=run(tree[4])
            body=tree[5]
            for i in range(begin,end,step):
                scope.define(name,i)
                v=run(body)
                if v==Signal(Break):
                    break
                if v==Signal(Return):
                    return v
        elif tp==ForIn:
            name=tree[1]
            obj=run(tree[2])
            body=tree[3]
            for i in obj:
                scope.define(name,i)
                v=run(body)
                if v==Signal(Break):
                    break
                if v==Signal(Return):
                    return v
        elif tp==Return:
            return Signal(Return,run(tree[1]))
        elif tp==Break:
            return Signal(Break)
        elif tp==Continue:
            return Signal(Continue)
        elif tp==FnDef:
            scope.define(tree[1],Function(tree[2],tree[3],scope))
        elif tp==Assign:
            lvalue=tree[1]
            to=run(tree[2])
            index=[]
            while lvalue[0]==Index:
                index=[run(lvalue[2])]+index
                lvalue=lvalue[1]
            def w(base,index,to):
                if index==[]:
                    return to
                base[index[0]]=w(base[index[0]],index[1:],to)
                return base
            if lvalue[0]==Var:
                scope.set(lvalue[1],w(scope.find(lvalue[1]),index,to))
            else:
                w(run(lvalue),index,to)
        elif tp==NoOp:
            return None
        elif tp==Import:
            _v=run(tree[1])
            for k,v in _v.items():
                scope.define(k,v)
        elif tp==Const:
            return tree[1]
        elif tp==Var:
            return scope.find(tree[1])
        elif tp==Binary:
            op=tree[1]
            l=run(tree[2])
            r=run(tree[3])
            return {
                '+':lambda a,b:a+b,
                '-':lambda a,b:a-b,
                '*':lambda a,b:a*b,
                '/':lambda a,b:a/b,
                '%':lambda a,b:a%b,
                '==':lambda a,b:a==b,
                '!=':lambda a,b:a!=b,
                '>':lambda a,b:a>b,
                '<':lambda a,b:a<b,
                '>=':lambda a,b:a>=b,
                '<=':lambda a,b:a<=b,
                '<<':lambda a,b:a<<b,
                '>>':lambda a,b:a>>b,
                '*and':lambda a,b:a and b,
                '*or':lambda a,b:a or b,
                '&':lambda a,b:a&b,
                '|':lambda a,b:a|b,
                '^':lambda a,b:a^b,
            }[op](l,r)
        elif tp==Unary:
            op=tree[1]
            l=run(tree[2])
            return {
                '+':lambda a:+a,
                '-':lambda a:-a,
                '*not':lambda a:not a,
                '~':lambda a:~a,
            }[op](l)
        elif tp==Index:
            l,r=run(tree[1]),run(tree[2])
            if type(l)==dict and type(l[r])==Function:
                return Method(l,l[r])
            return l[r]
        elif tp==Call:
            return run(tree[1])(*map(run,tree[2]))
        elif tp==NewObject:
            return dict(zip(tree[1],map(run,tree[2])))
        elif tp==NewList:
            return list(map(run,tree[1]))
        elif tp==NewFn:
            return Function(tree[1],tree[2],scope)
        elif tp==Where:
            expr,body=tree[1],tree[2]
            scope=Scope(scope,{})
            run_code(body,scope)
            res=run(expr)
            scope=scope.parent
            return res
        else:
            raise Exception(f"未知的语法树类型{tp}。")
        return None
    return run(tree)
scope=Scope(None,{
    "print":lambda *args:print(*args,sep="",end="",flush=True),
    "println":lambda *args:print(*args,sep="",flush=True),
    "make_tuple":lambda *args:args,
    "ord":ord,
    "chr":chr,
    "inputln":input,
    "getchar":lambda:sys.stdin.read(1),
    "len":len,
    "time":{
        "sleep":time.sleep,
        "time":time.time,
    }
})
def _load(file:str):
    run_code(parse(lex(open(file,'r',encoding='utf-8').read())),scope)
scope.var["load"]=_load
#}
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
    def print_info():
        gotoxy(size+1,1)
        filename:str=save
        fsize=os.get_terminal_size().columns-30
        filename=filename[:fsize]
        filename+=" "*(fsize-len(filename))
        print(f"\033[1;47;30m%6s | %s | ln: %4d col: %4d\033[1;0m"%(mode,filename,x,y))
    def pyins(ch):
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab
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
        elif ch=='\t':
            for i in range(tab):
                code[x].insert(y+1," ")
                y+=1
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
    def pydel():
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab
        if y==-1:
            if x!=0:
                x-=1
                y=len(code[x])-1
                code[x]+=code[x+1]
                del code[x+1]
        elif code[x][y-tab+1:y+1]==[" "]*tab:
            del code[x][y-tab+1:y+1]
            y-=tab
        elif "".join(code[x][y:y+2]) in ("()","[]","{}",'""',"''"):
            del code[x][y:y+2]
            y-=1
        elif y!=-1 and ord(code[x][y])>=128:
            del code[x][y-1:y+1]
            y-=2
        else:
            del code[x][y]
            y-=1
    def pyrun():
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab
        clear()
        if save:
            print("\033[1;33m开始运行\033[1;0m")
            os.system(f"powershell python '{save}'")
            print("\033[1;33m运行结束\033[1;0m")
        else:
            print("请保存后运行")
        getch()
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
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab
        if ch=='\r':
            fw=firstWord()
            if code[x] and code[x][y] in '([{':
                code.insert(x+1,[" "]*(count_tab(x)+1)*tab)
                code.insert(x+2,[" "]*(count_tab(x))*tab+code[x][y+1:])
                code[x]=code[x][:y+1]
                x+=1
                y=count_tab(x-1)*tab+tab-1
            elif y+1<len(code[x]) and code[x][y+1] in ')]}' or\
            fw in ["for","elif","else","if","while","module","switch"] or\
            "".join(code[x][:3])=="let" and code[x][-1]==")":
                code.insert(x+1,[" "]*(1+count_tab(x))*tab+code[x][y+1:])
                code[x]=code[x][:y+1]
                x+=1
                y=count_tab(x-1)*tab+tab-1
            else:
                code.insert(x+1,[" "]*count_tab(x)*tab+code[x][y+1:])
                code[x]=code[x][:y+1]
                x+=1
                y=count_tab(x-1)*tab-1
        elif ch=='\t':
            for i in range(tab):
                code[x].insert(y+1," ")
                y+=1
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
    def raindel():
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab
        if y==-1:
            if x!=0:
                x-=1
                y=len(code[x])-1 
                code[x]+=code[x+1]
                del code[x+1]
        elif code[x][y-tab+1:y+1]==[" "]*tab:
            del code[x][y-tab+1:y+1]
            y-=tab
        elif "".join(code[x][y:y+2]) in ("()","[]","{}",'""',"''"):
            del code[x][y:y+2]
            y-=1
        elif ord(code[x][y])>=128:
            del code[x][y-1:y+1]
            y-=2
        else:
            del code[x][y]
            y-=1
    def rainrun():
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab
        clear()
        if save:
            print("\033[1;33m开始运行\033[1;0m")
            run_code(parse(lex("\n".join(map("".join,code)))),deepcopy(scope))
            print("\033[1;33m运行结束\033[1;0m")
        else:
            print("请保存后运行")
        getch()
    def cppins(ch):
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab
        if ch=='\t':
            for i in range(tab):
                code[x].insert(y+1," ")
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
        elif ord(ch)>=128:
            code[x].insert(y+1,"")
            y+=1
            code[x].insert(y+1,ch)
            y+=1
        else:
            code[x].insert(y+1,ch)
            y+=1
    def cppdel():
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab
        if y==-1:
            if x!=0:
                x-=1
            y=len(code[x])-1
            code[x]+=code[x+1]
            del code[x+1]
        elif "".join(code[x][y-tab+1:y+1])==" "*tab:
            del code[x][y-tab+1:y+1]
            y-=tab
        elif "".join(code[x][y:y+2]) in ("()","[]","{}",'""',"''"):
            del code[x][y:y+2]
            y-=1
        elif ord(code[x][y])>=128:
            del code[x][y-1:y+1]
            y-=2
        else:
            del code[x][y]
            y-=1
    def cpprun():
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab
        clear()
        if save:
            os.system(f"g++ "+save+" -o "+save[:save.rfind(".")])
            print("\033[1;33m开始运行\033[1;0m")
            os.system(save[:save.rfind(".")])
            print("\033[1;33m运行结束\033[1;0m")
        else:
            print("请保存后运行")
        getch()
    lang_cfg={
        "py":{
            "ins":pyins,
            "del":pydel,
            "render":pyrender,
            "run":pyrun,
        },
        "rain":{
            "ins":rainins,
            "del":raindel,
            "render":rainrender,
            "run":rainrun,
        },
        "cpp":{
            "ins":cppins,
            "del":cppdel,
            "render":cpprender,
            "run":cpprun,
        }
    }
    def _ins(ch):
        lang_cfg[lang]["ins"](ch)
    def _del(ch):
        lang_cfg[lang]["del"](ch)
    def _run(ch):
        lang_cfg[lang]["run"](ch)
    def _render(ch):
        lang_cfg[lang]["render"](ch)
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
        return (i+1)//tab
    def NORMAL_do(ch):
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,change,delay
        if ch=='v':
            mode="SELECT"
            selectx,selecty=x,y
        elif ch=='p':
            _paste()
            change=True
        elif ch=='i':
            mode="INSERT"
        elif ch=='z':
            if history:
                code,x,y=history.pop()
                change=True
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
            lang_cfg[lang]["run"]()
        elif ch==':':
            gotoxy(size+2,1)
            cmd=input(':')
            do(cmd)
    def INSERT_do(ch):
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,change,delay
        if ord(ch)==27:
            mode="NORMAL"
        else:
            change=True
            lang_cfg[lang]["ins"](ch)
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
    def _paste():
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,change,delay
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
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,change,delay
        if ord(ch)==224:
            ch=ord(getch())
            if ch==72:
                if x!=0:
                    x-=1
                else:
                    y=-1
                if y>=len(code[x]):
                    y=len(code[x])-1
                if len(code[x]) and code[x][y]=="":
                    y+=1
            elif ch==80:
                if x!=len(code)-1:
                    x+=1
                else:
                    y=len(code[x])-1
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
            elif ch==77:
                if y!=len(code[x])-1:
                    if code[x][y+1]=="":
                        y+=1
                    y+=1
                else:
                    if x!=len(code)-1:
                        x+=1
                        y=-1
            return
        elif (ord(ch)==8 and mode!="SELECT") or (ch=='d' and mode=="NORMAL"):
            change=True
            lang_cfg[lang]["del"]()
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
            elif ch=='d' or ord(ch)==8:
                change=True
                mode="INSERT"
                if x==selectx:
                    if y<selecty:
                        del code[x][y+1:selecty+1]
                    else:
                        del code[x][selecty+1:y+1]
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
                    del code[selectx]
                    for i in range(selectx+1,x):
                        del code[x+1]
                x=min(x,len(code)-1)
                y=min(y,len(code[x])-1)
            elif ch=='c':
                v_copy()
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
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,change,delay,theme
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
    def _set(n,v):
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab,change,delay
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
    scope.var["python_editor_config"]={
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
    }
    run_code(parse(lex(open(dire+"config.rain",'r',encoding='utf-8').read())),deepcopy(scope))
    rr=lang_cfg[lang]["render"]("\n".join(map("".join,code)),theme)
    while 1:
        size=os.get_terminal_size().lines-3
        sizey=os.get_terminal_size().columns-(7 if nu else 0)
        change=False
        if x<begin:
            begin=x
        if x>=begin+size:
            begin=x-size+1
        if y<beginy:
            beginy=y+1
        if y>=beginy+sizey-1:
            beginy=y-sizey+2
        if len(rr)<len(code):
            rr+=[[]]
        if mode=="SELECT":
            gar=getall()
            for i in range(begin,min(begin+size,len(rr))):
                if nu:
                    print("\033[1;0m%4d | "%(i+1),flush=True,end="")
                for j in range(beginy,min(beginy+sizey,len(rr[i]))):
                    if (i,j) in gar:
                        if rr[i][j]:
                            print(rr[i][j][:-1]+"\033[1;47m"+rr[i][j][-1],end="\033[1;0m")
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
        #gotoxy(size+1,1)
        #print("\033[1;0m",mode)
        print_info()
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
        clear()
def pyrender(code,theme:dict):
    op=[
        '+','-','*','/','%',
        '==','!=','>','<','>=','<=',
        '<<','>>','&','|','^','~',
    ]
    res=[]
    p=0
    while p<len(code):
        if code[p].isdigit():
            while p<len(code) and (code[p].isdigit() or code[p] in '.xbo'):
                res.append(theme["number"]+code[p])
                p+=1
        elif code[p].isalpha() or code[p]=="_":
            s=""
            while p<len(code) and (code[p].isalnum() or code[p]=='_'):
                s+=code[p]
                p+=1
            if s in __import__("keyword").kwlist:
                for i in s:
                    res.append(theme["keyword"]+i)
            elif s in dir(__builtins__):
                for i in s:
                    res.append(theme["builtin"]+i)
            elif s in ["self","cls"]:
                for i in s:
                    res.append(theme["this"]+i)
            else:
                for i in s:
                    res.append(theme["identifier"]+i)
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
                res.append(theme["string"]+i)
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
                res.append(theme["string"]+i)
        elif code[p]=='#':
            while p<len(code) and code[p]!='\n':
                res.append(theme["comment"]+code[p])
                p+=1
        elif code[p] in op:
            res.append(theme["operator"]+code[p])
            p+=1
        elif code[p:p+2] in op:
            res.append(theme["operator"]+code[p])
            p+=1
            res.append(theme["operator"]+code[p])
            p+=1
        else:
            if ord(code[p])>=128:
                res.append("")
            res.append(theme["others"]+code[p])
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
def rainrender(code,theme:dict):
    op=[
        '+', '-', '*', '/', '%', '==', '!=', '>=', '<=', '<<', '>>', '>', '<', '&', '|', '^', '!',
    ]
    res=[]
    p=0
    while p<len(code):
        if code[p].isdigit():
            while p<len(code) and (code[p].isdigit() or code[p] in '.'):
                res.append(theme["number"]+code[p])
                p+=1
        elif code[p].isalpha() or code[p]=="_":
            s=""
            while p<len(code) and (code[p].isalnum() or code[p]=='_'):
                s+=code[p]
                p+=1
            if s in kw:
                for i in s:
                    res.append(theme["keyword"]+i)
            elif s in ["self"]:
                for i in s:
                    res.append(theme["this"]+i)
            elif s in scope.var:
                for i in s:
                    res.append(theme["builtin"]+i)
            else:
                for i in s:
                    res.append(theme["identifier"]+i)
        elif code[p]=='"':
            s=code[p]
            p+=1
            while p<len(code) and code[p]!='"':
                if code[p]=='\\':
                    s+=code[p]
                    p+=1
                    if p<len(code):
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
                res.append(theme["string"]+i)
        elif code[p]=='#':
            while p<len(code) and code[p]!='\n':
                res.append(theme["comment"]+code[p])
                p+=1
        elif code[p] in op:
            res.append(theme["operator"]+code[p])
            p+=1
        elif code[p:p+2] in op:
            res.append(theme["operator"]+code[p])
            p+=1
            res.append(theme["operator"]+code[p])
            p+=1
        else:
            if ord(code[p])>=128:
                res.append("")
            res.append(theme["others"]+code[p])
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
cpp_kw=[
    "asm",
    "do",
    "if",
    "return",
    "typedef",
    "auto",
    "double",
    "inline",
    "short",
    "typeid",
    "bool",
    "dynamic_cast",
    "int",
    "signed",
    "typename",
    "break",
    "else",
    "long",
    "sizeof",
    "union",
    "case",
    "enum",
    "mutable",
    "static",
    "unsigned",
    "catch",
    "explicit",
    "namespace",
    "static_cast",
    "using",
    "char",
    "export",
    "new",
    "struct",
    "virtual",
    "class",
    "extern",
    "operator",
    "switch",
    "void",
    "const",
    "false",
    "private",
    "template",
    "volatile",
    "const_cast",
    "float",
    "protected",
    "this",
    "wchar_t",
    "continue",
    "for",
    "public",
    "throw",
    "while",
    "default",
    "friend",
    "register",
    "true",
    "delete",
    "goto",
    "reinterpret_cast",
    "try",
]
def cpprender(code:str,theme:dict):
    op=[
        '+','-','*','/','%',
        '==','!=','>','<','>=','<=',
        '<<','>>','&&','||','&','|','^','~',
        '=','?',':','!',',',
    ]
    res=[]
    p=0
    while p<len(code):
        if code[p].isdigit():
            while p<len(code) and (code[p].isdigit() or code[p] in '.xbo'):
                res.append(theme["number"]+code[p])
                p+=1
        elif code[p].isalpha() or code[p]=="_":
            s=""
            while p<len(code) and (code[p].isalnum() or code[p]=='_'):
                s+=code[p]
                p+=1
            if s in cpp_kw:
                for i in s:
                    res.append(theme["keyword"]+i)
            else:
                for i in s:
                    res.append(theme["identifier"]+i)
        elif code[p:p+2]=="/*":
            s=code[p:p+2]
            p+=2
            while p<len(code) and code[p:p+2]!="*/":
                s+=code[p]
                p+=1
            s+=code[p:p+2]
            p+=2
            for i in s:
                res.append(theme["comment"]+i)
        elif code[p] in '\'"':
            s=code[p]
            x=s
            p+=1
            while p<len(code) and code[p]!='\n' and code[p]!=x:
                if code[p]=='\\':
                    s+=code[p]
                    p+=1
                    if p<len(code) and code[p] in '\'"\n':
                        s+=code[p]
                        p+=1
                else:
                    s+=code[p]
                    p+=1
            if p<len(code):
                s+=code[p]
                p+=1
            for i in s:
                res.append(theme["string"]+i)
        elif code[p]=='#':
            while p<len(code) and code[p]!='\n':
                res.append(theme["header"]+code[p])
                p+=1
        elif code[p:p+2]=='//':
            while p<len(code) and code[p]!='\n':
                res.append(theme["comment"]+code[p])
                p+=1
        elif code[p] in op:
            res.append(theme["operator"]+code[p])
            p+=1
        elif code[p:p+2] in op:
            res.append(theme["operator"]+code[p])
            p+=1
            res.append(theme["operator"]+code[p])
            p+=1
        else:
            res.append(theme["others"]+code[p])
            p+=1
    rr=[]
    tmp=[]
    for i in res:
        if "\n" in i:
            rr.append(tmp)
            tmp=[]
        else:
            tmp.append(i)
    return rr+[tmp]
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