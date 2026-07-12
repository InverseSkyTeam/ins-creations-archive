import sys,os,time
import msvcrt
from copy import deepcopy
#Rain{
EOF,ADD,SUB,MUL,DIV,MOD,EQ,NE,GT,LT,GE,LE,LSH,RSH,BAND,BOR,XOR,INV,\
COLON,COMMA,LPAREN,RPAREN,LSB,RSB,ASSIGN,QUOTE,L,R,DOT,\
AND,OR,NOT,\
IF,ELIF,ELSE,WHILE,FN,RETURN,BREAK,CONTINUE,END,LET,FOR,TO,IN,SWITCH,CASE,DEFAULT,WHERE,MODULE,IMPORT,LOAD,\
CONST,ID,\
=[i for i in range(54)]
op_dict=[('+', 1), ('-', 2), ('*', 3), ('/', 4), ('%', 5), ('==', 6), ('!=', 7), ('>=', 10), ('<=', 11), ('<<', 12), ('>>', 13), ('>', 8), ('<', 9), ('&', 14), ('|', 15), ('^', 17), ('!', 27), ('(', 20), (')', 21), (':', 18), (',', 19), ('=', 24), ('[',22), (']', 23),('\'',25),('{',26),('}',27),('.',28)]
Const,Id,Binary,Unary,Assign,While,If,Break,Continue,Return,List,Nth,Call,Fn,Let,LetFn,ForTo,ForIn,Tuple,Dict,Dot,Switch,Where,Module,Import,Load=[i for i in range(26)]
def parse(code):
    def lex():
        nonlocal code
        if code=="":
            return (EOF,)
        while code and (code[0] in ' \n\t' or code[0]=='#'):
            if code[0]=='#':
                code=code[1:]
                while code and code[0]!='\n':
                    code=code[1:]
            code=code[1:]
        if code=="":
            return (EOF,)
        if code[0].isdigit():
            s=code[0]
            code=code[1:]
            while code!="" and (code[0].isdigit() or code[0]=='.'):
                s+=code[0]
                code=code[1:]
            if '.' in s:
                return (CONST,float(s))
            return (CONST,int(s))
        if code[0].isalpha() or code[0]=='_':
            s=code[0]
            code=code[1:]
            while code!="" and (code[0].isalnum() or code[0]=='_'):
                s+=code[0]
                code=code[1:]
            if s in "and,or,not,if,else,elif,while,fn,return,break,continue,end,let,for,to,in,switch,case,default,where,module,import,load".split(","):
                return ({
                    "and":AND,
                    "or":OR,
                    "not":NOT,
                    "if":IF,
                    "elif":ELIF,
                    "else":ELSE,
                    "while":WHILE,
                    "fn":FN,
                    "return":RETURN,
                    "break":BREAK,
                    "continue":CONTINUE,
                    "end":END,
                    "let":LET,
                    "for":FOR,
                    "to":TO,
                    "in":IN,
                    "switch":SWITCH,
                    "case":CASE,
                    "default":DEFAULT,
                    "where":WHERE,
                    "module":MODULE,
                    "import":IMPORT,
                    "load":LOAD
                }[s],)
            if s=="True":
                return (CONST,True)
            if s=="False":
                return (CONST,False)
            if s=="None":
                return (CONST,None)
            return (ID,s)
        if code[0]=='"':
            code=code[1:]
            s=''
            while code and code[0]!='"':
                if code[0]=='\\':
                    code=code[1:]
                    if code[0].isdigit():
                        s+=int(code[0:3],base=8)
                        code=code[1:]
                    else:
                        s+={
                            'n':'\n',
                            't':'\t',
                            'r':'\r',
                            '\\':'\\',
                            '"':'"',
                            '\'':'\''
                        }[code[0]]
                        code=code[1:]
                else:
                    s+=code[0]
                    code=code[1:]
            code=code[1:]
            return (CONST,s)
        for k,v in op_dict:
            if code[:len(k)]==k:
                code=code[len(k):]
                return (v,)
        raise Exception(code)
    '''tks=[lex()]
    while tks[-1][0]!=EOF:
        tks.append(lex())
    tk=tks[0]
    p=0'''
    tk=lex()
    def eat(ex=None):
        nonlocal tk
        if ex==None or tk[0]==ex:
            _tk=tk
            tk=lex()
            return _tk
        raise Exception(tk,ex)
    def parse_body(*ex):
        b=[]
        while tk[0] not in ex:
            b.append(stmt())
        return b
    def stmt():
        nonlocal tk
        if tk[0]==LET:
            eat()
            name=[eat(ID)[1]]
            if tk[0]==LPAREN:
                name=name[0]
                eat()
                para=[]
                if tk[0]!=RPAREN:
                    para.append(eat(ID)[1])
                    while tk[0]==COMMA:
                        eat()
                        para.append(eat(ID)[1])
                eat(RPAREN)
                body=parse_body(END)
                eat()
                return (LetFn,name,para,body)
            value=[None]
            if tk[0]==ASSIGN:
                eat()
                value[-1]=expr()
            while tk[0]==COMMA:
                eat()
                name.append(eat(ID)[1])
                value.append(None)
                if tk[0]==ASSIGN:
                    eat()
                    value[-1]=expr()
            return (Let,name,value)
        if tk[0]==IF:
            eat()
            conds=[expr()]
            cases=[parse_body(ELIF,ELSE,END)]
            while tk[0]==ELIF:
                eat()
                conds.append(expr())
                cases.append(parse_body(ELIF,ELSE,END))
            if tk[0]==ELSE:
                eat()
                b=parse_body(END)
                eat()
                return (If,conds,cases,b)
            eat(END)
            return (If,conds,cases,[])
        if tk[0]==WHILE:
            eat()
            cond=expr()
            body=parse_body(END)
            eat()
            return (While,cond,body)
        if tk[0]==FOR:
            eat()
            eat(LET)
            name=eat(ID)[1]
            if tk[0]==IN:
                eat()
                obj=expr()
                body=parse_body(END)
                eat()
                return (ForIn,name,obj,body)
            eat(ASSIGN)
            begin=expr()
            eat(TO)
            end=expr()
            body=parse_body(END)
            eat()
            return (ForTo,name,begin,end,body)
        if tk[0]==SWITCH:
            eat()
            v=expr()
            cases=[]
            bodys=[]
            while tk[0]==CASE:
                eat()
                cases.append(expr())
                eat(COLON)
                bodys.append(parse_body(END,CASE,DEFAULT))
            if tk[0]==END:
                eat()
                return (Switch,v,cases,bodys,[])
            eat()
            eat(COLON)
            b=parse_body(END)
            eat()
            return (Switch,v,cases,bodys,b)
        if tk[0]==MODULE:
            eat()
            n=eat(ID)[1]
            b=parse_body(END)
            eat()
            return (Module,n,b)
        if tk[0]==IMPORT:
            eat()
            return (Import,expr())
        if tk[0]==LOAD:
            eat()
            return (Load,expr())
        if tk[0]==BREAK:
            eat()
            return (Break,)
        if tk[0]==CONTINUE:
            eat()
            return (Continue,)
        if tk[0]==RETURN:
            eat()
            return (Return,expr())
        else:
            e=expr()
            if tk[0]==ASSIGN:
                eat()
                v=expr()
                return (Assign,e,v)
            return e
    def expr():
        v=expr0()
        if tk[0]==WHERE:
            eat()
            eat(LPAREN)
            b=parse_body(RPAREN)
            eat()
            return (Where,v,b)
        return v
    def expr0():
        nonlocal tk
        res=expr1()
        while tk[0] in (AND,OR):
            res=(Binary,eat()[0],res,expr1())
        return res
    def expr1():
        nonlocal tk
        res=expr2()
        while tk[0] in (BAND,BOR,XOR):
            res=(Binary,eat()[0],res,expr2())
        return res
    def expr2():
        nonlocal tk
        res=expr3()
        while tk[0] in (EQ,NE,GT,LT,GE,LE):
            res=(Binary,eat()[0],res,expr3())
        return res
    def expr3():
        nonlocal tk
        res=expr4()
        while tk[0] in (LSH,RSH):
            res=(Binary,eat()[0],res,expr4())
        return res
    def expr4():
        nonlocal tk
        res=term()
        while tk[0] in (ADD,SUB):
            res=(Binary,eat()[0],res,term())
        return res
    def term():
        nonlocal tk
        res=factor()
        while tk[0] in (MUL,DIV,MOD):
            res=(Binary,eat()[0],res,factor())
        return res
    def factor():
        nonlocal tk
        if tk[0]==CONST:
            return fh((Const,eat()[1]))
        if tk[0]==ID:
            return fh((Id,eat()[1]))
        if tk[0] in (ADD,SUB,NOT,INV):
            return (Unary,eat()[0],fh(factor()))
        if tk[0]==L:
            eat()
            k,v=[],[]
            if tk[0]!=R:
                k.append(eat(ID)[1])
                eat(COLON)
                v.append(expr())
                while tk[0]==COMMA:
                    eat()
                    k.append(eat(ID)[1])
                    eat(COLON)
                    v.append(expr())
            eat(R)
            return fh((Dict,k,v))
        if tk[0]==LPAREN:
            eat()
            if tk[0]==FN:
                eat()
                eat(LPAREN)
                para=[]
                if tk[0]!=RPAREN:
                    para.append(eat(ID)[1])
                    while tk[0]==COMMA:
                        eat()
                        para.append(eat(ID)[1])
                eat(RPAREN)
                body=[]
                while tk[0]!=RPAREN:
                    body.append(stmt())
                eat(RPAREN)
                return fh((Fn,para,body))
            e=expr()
            eat(RPAREN)
            return fh(e)
        if tk[0]==LSB:
            eat()
            l=[]
            if tk[0]!=RSB:
                l.append(expr())
                while tk[0]==COMMA:
                    eat()
                    l.append(expr())
            eat(RSB)
            return fh((List,l))
        if tk[0]==QUOTE:
            eat()
            eat(LPAREN)
            l=[]
            if tk[0]!=RPAREN:
                l.append(expr())
                while tk[0]==COMMA:
                    eat()
                    l.append(expr())
            eat(RPAREN)
            return fh((Tuple,l))
        raise Exception(tk)
    def fh(v):
        nonlocal tk
        if tk[0]==LSB:
            eat()
            n=expr()
            eat(RSB)
            return fh((Nth,v,n))
        if tk[0]==LPAREN:
            eat()
            args=[]
            if tk[0]!=RPAREN:
                args=[expr()]
                while tk[0]==COMMA:
                    eat()
                    args.append(expr())
            eat(RPAREN)
            return fh((Call,v,args))
        if tk[0]==DOT:
            eat()
            return fh((Dot,v,eat(ID)[1]))
        return v
    return parse_body(EOF)
def call(fn,args):
    if callable(fn):
        return fn(*args)
    para,body,fill,closure=fn
    if len(fill)+len(args)<len(para):
        return (para,body,fill+args,closure)
    return run(body,closure+[dict(zip(para,fill+args))])[1][2][1]
def filled(fn,args):
    para,body,fill,closure=fn
    return (para,body,fill+args,closure)
def run(tree,scope):
    def find(name):
        nonlocal scope
        for i in reversed(scope):
            if name in i:
                return i[name]
        raise Exception(name)
    def set(name,value):
        nonlocal scope
        for i in reversed(scope):
            if name in i:
                i[name]=value
                return
        raise Exception(name)
    signal_default=(0,0,(0,None))
    #信号：break信号，continue信号，return信号（标示，返回值）
    if type(tree)==list:
        if tree==[]:
            return (None,signal_default)
        scope=scope+[{}]
        for i in tree:
            v=run(i,scope)
            if len(v)>1 and v[1]!=signal_default:
                scope.pop()
                return v
        scope=scope[:-1]
        return (None,signal_default)
    else:
        tp=tree[0]
        if tp==Const:
            return (tree[1],)
        if tp==Id:
            return (find(tree[1]),)
        if tp==Nth:
            return (run(tree[1],scope)[0][run(tree[2],scope)[0]],)
        if tp==Fn:
            return ((tree[1],tree[2],[],scope),)
        if tp==List:
            return ([run(i,scope)[0] for i in tree[1]],)
        if tp==Tuple:
            return (tuple([run(i,scope)[0] for i in tree[1]]),)
        if tp==Call:
            return (call(run(tree[1],scope)[0],[run(i,scope)[0] for i in tree[2]]),)
        if tp==Dict:
            return (dict(zip(tree[1],map(lambda a:run(a,scope)[0],tree[2]))),)
        if tp==Dot:
            obj,n=run(tree[1],scope)[0],tree[2]
            v=obj[n]
            if type(v)==tuple:
                return (filled(v,[obj]),)
            return (v,)
        if tp==Where:
            scope=scope+[{}]
            for i in tree[2]:
                v=run(i,scope)
                if len(v)>1 and v[1]!=signal_default:
                    raise
            r=run(tree[1],scope)[0]
            scope=scope[:-1]
            return (r,)
        if tp==Binary:
            return ({
                ADD:lambda a,b:a+b,
                SUB:lambda a,b:a-b,
                MUL:lambda a,b:a*b,
                DIV:lambda a,b:a/b,
                MOD:lambda a,b:a%b,
                EQ:lambda a,b:a==b,
                NE:lambda a,b:a!=b,
                GT:lambda a,b:a>b,
                LT:lambda a,b:a<b,
                GE:lambda a,b:a>=b,
                LE:lambda a,b:a<=b,
                LSH:lambda a,b:a<<b,
                RSH:lambda a,b:a>>b,
                AND:lambda a,b:a and b,
                OR:lambda a,b:a or b,
                BAND:lambda a,b:a&b,
                BOR:lambda a,b:a|b,
                XOR:lambda a,b:a^b,
            }[tree[1]](run(tree[2],scope)[0],run(tree[3],scope)[0]),)
        if tp==Unary:
            return ({
                ADD:lambda a:+a,
                SUB:lambda a:-a,
                NOT:lambda a:not a,
                INV:lambda a:~a,
            }[tree[1]](run(tree[2],scope)[0]),)
        if tp==Module:
            scope=scope+[{}]
            for i in tree[2]:
                v=run(i,scope)
                if len(v)>1 and v[1]!=signal_default:
                    raise
            scope[-2][tree[1]]=scope[-1]
            scope=scope[:-1]
            return (None,signal_default)
        if tp==Import:
            n=run(tree[1],scope)[0]
            for k,v in n.items():
                scope[-1][k]=v
            return (None,signal_default)
        if tp==Load:
            filename=run(tree[1],scope)[0]
            v=""
            with open(filename,"r") as f:
                v="\n".join(f.readlines())
            p=parse(v)
            for i in p:
                v=run(i,scope)
                if len(v)>1 and v[1]!=signal_default:
                    raise
            return (None,signal_default)
        if tp==Break:
            return (None,(1,0,(0,None)))
        if tp==Continue:
            return (None,(0,1,(0,None)))
        if tp==Return:
            return (None,(0,0,(1,run(tree[1],scope)[0])))
        if tp==Let:
            for k,v in map(lambda a,b:(a,b),tree[1],tree[2]):
                scope[-1][k]=run(v,scope)[0]
            return (None,)
        if tp==LetFn:
            scope[-1][tree[1]]=(tree[2],tree[3],[],scope)
            return (None,)
        if tp==If:
            for k,v in map(lambda a,b:(a,b),tree[1],tree[2]):
                if run(k,scope)[0]:
                    return run(v,scope)
            return run(tree[3],scope)
        if tp==While:
            while run(tree[1],scope)[0]:
                v=run(tree[2],scope)
                if len(v)>1 and v[1][0]:
                    break
                if len(v)>1 and v[1][2][0]:
                    return v
            return (None,signal_default)
        if tp==ForTo:
            name=tree[1]
            begin,end=run(tree[2],scope)[0],run(tree[3],scope)[0]
            for i in range(begin,end):
                v=run(tree[4],scope+[{name:i}])
                if len(v)>1 and v[1][0]:
                    break
                if len(v)>1 and v[1][2][0]:
                    return v
            return (None,signal_default)
            return (None,signal_default)
        if tp==ForIn:
            name=tree[1]
            obj=run(tree[2],scope)[0]
            for i in obj:
                v=run(tree[3],scope+[{name:i}])
                if len(v)>1 and v[1][0]:
                    break
                if len(v)>1 and v[1][2][0]:
                    return v
            return (None,signal_default)
        if tp==Switch:
            v=run(tree[1],scope)[0]
            for a,b in map(lambda a,b:(a,b),tree[2],tree[3]):
                if v==run(a,scope)[0]:
                    c=run(b,scope)
                    if len(c)>1 and c[1][0]:
                        break
                    if len(c)>1 and c[1][2][0]:
                        return c
            else:
                return run(tree[4],scope)
            return (None,signal_default)
        if tp==Assign:
            lvalue=tree[1]
            v=run(tree[2],scope)[0]
            if lvalue[0]!=Id:
                indexlist=[]
                while lvalue[0] in (Nth,Dot):
                    if lvalue[0]==Nth:
                        indexlist=[run(lvalue[2],scope)[0]]+indexlist
                    else:
                        indexlist=[lvalue[2]]+indexlist
                    lvalue=lvalue[1]
                def w(base,indexlist,v):
                    if indexlist==[]:
                        return v
                    base[indexlist[0]]=w(base[indexlist[0]],indexlist[1:],v)
                    return base
                name=lvalue[1]
                set(name,w(run(lvalue,scope)[0],indexlist,v))
                return (None,)
            else:
                set(lvalue[1],v)
                return (None,)
def printTree(tree,tab=0):
    if type(tree)==list:
        print("  "*tab+"begin")
        for i in tree:
            printTree(i,tab+1)
    elif type(tree)==tuple:
        print("  "*tab+"Const,Id,Binary,Unary,Assign,While,If,Break,Continue,Return,List,Nth,Call,Fn,Let,LetFn,ForTo,ForIn,Tuple,Dict,Dot,Switch,Where".split(",")[tree[0]])
        for i in tree[1:]:
            printTree(i,tab+1)
    else:
        print("  "*tab,tree,sep="")
fns=[{
    "print":lambda *args:print(*args,end="",sep=""),
    "println":lambda *args:print(*args,sep=""),
    "make_tuple":lambda *args:args,
    "ord":ord,
    "chr":chr,
    "inputln":input,
    "getchar":lambda:sys.stdin.read(1),
    "len":len
}]
#}
def clear():
    os.system("cls")
def gotoxy(x,y):
    print(f"\033[{x};{y}f",end="")
def getch():
    return msvcrt.getwch()
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
    size=15
    sizey=50
    ikey={}
    nkey={}
    selectx,selecty=0,0
    change=False
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
    def rainrun():
        nonlocal mode,x,y,code,begin,beginy,history,size,sizey,selectx,selecty,nu,save,tab
        clear()
        if save:
            print("\033[1;33m开始运行\033[1;0m")
            run(parse("\n".join(map("".join,code))),deepcopy(fns))
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
    def do_cmds(cmd):
        cmd=cmd.replace("<cr>","\n")\
            .replace("<esc>","\033")
        for i in cmd:
            do_cmd(i)
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
        elif ord(ch)==8 or (ch=='d' and mode=="NORMAL"):
            change=True
            lang_cfg[lang]["del"]()
        elif mode=="NORMAL":
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
                change=True
                lang_cfg[lang]["ins"](ch)
    rr=lang_cfg[lang]["render"]("\n".join(map("".join,code)))
    while 1:
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
        time.sleep(delay)
        while msvcrt.kbhit():
            ch=getch()
            if ord(ch)==3:
                break
            else:
                do_cmd(ch)
            time.sleep(delay)
        if change:
            rr=lang_cfg[lang]["render"]("\n".join(map("".join,code)))
            history.append((deepcopy(code),x,y))
        clear()
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
def rainrender(code):
    rain_kwlist="and,or,not,if,else,elif,while,fn,return,break,continue,end,let,for,to,in,switch,case,default,where,module,import,load".split(",")
    res=[]
    p=0
    while p<len(code):
        if code[p].isdigit():
            while p<len(code) and (code[p].isdigit() or code[p] in '.'):
                res.append("\033[0;33m"+code[p])
                p+=1
        elif code[p].isalpha() or code[p]=="_":
            s=""
            while p<len(code) and (code[p].isalnum() or code[p]=='_'):
                s+=code[p]
                p+=1
            if s in rain_kwlist:
                for i in s:
                    res.append("\033[1;35m"+i)
            elif s in ["self"]:
                for i in s:
                    res.append("\033[0;34m"+i)
            elif s in fns[0]:
                for i in s:
                    res.append("\033[1;34m"+i)
            else:
                for i in s:
                    res.append("\033[1;0m"+i)
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
def cpprender(code:str):
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
            if s in cpp_kw:
                for i in s:
                    res.append("\033[1;35m"+i)
            else:
                for i in s:
                    res.append("\033[1;0m"+i)
        elif code[p:p+2]=="/*":
            s=code[p:p+2]
            p+=2
            while p<len(code) and code[p:p+2]!="*/":
                s+=code[p]
                p+=1
            s+=code[p:p+2]
            p+=2
            for i in s:
                res.append("\033[0;32m"+i)
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
                res.append("\033[0;32m"+i)
        elif code[p]=='#':
            while p<len(code) and code[p]!='\n':
                res.append("\033[1;35m"+code[p])
                p+=1
        elif code[p:p+2]=='//':
            while p<len(code) and code[p]!='\n':
                res.append("\033[0;32m"+code[p])
                p+=1
        else:
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