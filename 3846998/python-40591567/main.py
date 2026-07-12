from copy import deepcopy
import sys
EOF,ADD,SUB,MUL,DIV,MOD,EQ,NE,GT,LT,GE,LE,LSH,RSH,BAND,BOR,XOR,INV,\
COLON,COMMA,LPAREN,RPAREN,LSB,RSB,ASSIGN,QUOTE,L,R,DOT,\
AND,OR,NOT,\
IF,ELIF,ELSE,WHILE,FN,RETURN,BREAK,CONTINUE,END,LET,FOR,TO,IN,SWITCH,CASE,DEFAULT,\
CONST,ID,\
=[i for i in range(50)]
op_dict=[('+', 1), ('-', 2), ('*', 3), ('/', 4), ('%', 5), ('==', 6), ('!=', 7), ('>=', 10), ('<=', 11), ('<<', 12), ('>>', 13), ('>', 8), ('<', 9), ('&', 14), ('|', 15), ('^', 17), ('!', 27), ('(', 20), (')', 21), (':', 18), (',', 19), ('=', 24), ('[',22), (']', 23),('\'',25),('{',26),('}',27),('.',28)]
Const,Id,Binary,Unary,Assign,While,If,Break,Continue,Return,List,Nth,Call,Fn,Let,LetFn,ForTo,ForIn,Tuple,Dict,Dot,Switch=[i for i in range(22)]
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
            if s in "and,or,not,if,else,elif,while,fn,return,break,continue,end,let,for,to,in,switch,case,default".split(","):
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
                    "default":DEFAULT
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
        print("  "*tab+"Const,Id,Binary,Unary,Assign,While,If,Break,Continue,Return,List,Nth,Call,Fn,Let,LetFn,ForTo,ForIn,Tuple,Dict,Dot,Switch".split(",")[tree[0]])
        for i in tree[1:]:
            printTree(i,tab+1)
    else:
        print("  "*tab,tree,sep="")
from time import*
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
run(parse('''
let code=inputln(),
    mem=[0],
    i=0,
    pos=512
for let i=0 to 10
    mem=mem+mem
end
while i<len(code)
    let ch=code[i]
    if ch=="+" mem[pos]=mem[pos]+1
    elif ch=="-" mem[pos]=mem[pos]-1
    elif ch=="<" pos=pos-1
    elif ch==">" pos=pos+1
    elif ch=="," mem[pos]=ord(getchar())
    elif ch=="." print(chr(mem[pos]))
    elif ch=="["
        if not mem[pos]
            let l=0,r=0
            while i<len(code)
                if code[i]=="[" l=l+1
                elif code[i]=="]"
                    if l l=l-1
                    else r=r+1
                    end
                end
                if l==0 and r==0
                    break
                end
                i=i+1
            end
        end
    elif ch=="]"
        let l=0,r=0
        while i>=0
            if code[i]=="]" l=l+1
            elif code[i]=="["
                if l l=l-1
                else r=r+1
                end
            end
            if l==0 and r==0
                break
            end
            i=i-1
        end
        i=i-1
    end
    i=i+1
end
'''),fns)