from copy import deepcopy
EOF,ADD,SUB,MUL,DIV,MOD,EQ,NE,GT,LT,GE,LE,LSH,RSH,BAND,BOR,XOR,INV,\
COLON,COMMA,LPAREN,RPAREN,LSB,RSB,ASSIGN,\
AND,OR,NOT,IN,\
IF,ELIF,ELSE,WHILE,FN,RETURN,BREAK,CONTINUE,END,LET,\
CONST,ID,\
=[i for i in range(41)]
op_dict=[('+', 1), ('-', 2), ('*', 3), ('/', 4), ('%', 5), ('==', 6), ('!=', 7), ('>=', 10), ('<=', 11), ('<<', 12), ('>>', 13), ('>', 8), ('<', 9), ('&&', 25), ('||', 26), ('&', 14), ('|', 15), ('^', 17), ('!', 27), ('(', 20), (')', 21), (':', 18), (',', 19), ('=', 24), ('[',22), (']', 23)]
Const,Id,Binary,Unary,Assign,While,If,Break,Continue,Return,List,Nth,Call,Fn,Let,LetFn=[i for i in range(16)]
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
            if s in "and,or,not,in,if,else,elif,while,fn,return,break,continue,end,let".split(","):
                return ({
                    "and":AND,
                    "or":OR,
                    "not":NOT,
                    "in":IN,
                    "if":IF,
                    "elif":ELIF,
                    "else":ELSE,
                    "while":WHILE,
                    "fn":FN,
                    "return":RETURN,
                    "break":BREAK,
                    "continue":CONTINUE,
                    "end":END,
                    "let":LET
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
        return v
    return parse_body(EOF)
def call(fn,args):
    if callable(fn):
        return fn(*args)
    para,body,fill,closure=fn
    if len(fill)+len(args)<len(para):
        return (para,body,fill+args,closure)
    return run(body,closure+[dict(zip(para,fill+args))])[1][2][1]
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
        if tp==Call:
            return (call(run(tree[1],scope)[0],[run(i,scope)[0] for i in tree[2]]),)
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
                if v[1][0]:
                    break
                if v[1][2][0]:
                    return v
            return (None,signal_default)
        if tp==Assign:
            lvalue=tree[1]
            v=run(tree[2],scope)[0]
            if lvalue[0]!="var":
                indexlist=[]
                while type(lvalue)==tuple and lvalue[0]==Nth:
                    indexlist=[run(lvalue[2],scope)[0]]+indexlist
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
from time import*
fns=[{
    "print":lambda *args:print(*args,end="",sep=""),
    "println":lambda *args:print(*args,sep="")
}]
run(parse('''
let f(a,b)
    return a+b
end
println(f(1)(2))
'''),fns)