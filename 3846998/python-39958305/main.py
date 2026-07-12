import sys
EOF,ADD,SUB,MUL,DIV,MOD,EQ,NE,GT,LT,GE,LE,LSH,RSH,BAND,BOR,XOR,INV,\
COLON,COMMA,LPAREN,RPAREN,LSB,RSB,ASSIGN,\
AND,OR,NOT,IN,\
IF,WHILE,DEF,RETURN,BREAK,CONTINUE,\
CONST,ID,\
TAB\
=[i for i in range(38)]
op_dict={
    '+':ADD,
    '-':SUB,
    '*':MUL,
    '/':DIV,
    '%':MOD,
    '==':EQ,
    '!=':NE,
    '>=':GE,
    '<=':LE,
    '<<':LSH,
    '>>':RSH,
    '>':GT,
    '<':LT,
    '&&':AND,
    '||':OR,
    '&':BAND,
    '|':BOR,
    '^':XOR,
    '!':NOT,
    '^':INV,
    '(':LPAREN,
    ')':RPAREN,
    ':':COLON,
    ',':COMMA,
    '=':ASSIGN,
    '[':LSB,
    ']':RSB,
}
def to_str(tk):
    return "EOF,ADD,SUB,MUL,DIV,MOD,EQ,NE,GT,LT,GE,LE,LSH,RSH,BAND,BOR,XOR,INV,\
COLON,COMMA,LPAREN,RPAREN,LSB,RSB,ASSIGN,\
AND,OR,NOT,IN,\
IF,WHILE,DEF,RETURN,BREAK,CONTINUE,\
CONST,ID,\
TAB".split(",")[tk]
def print_token(tk):
    print("(",to_str(tk[0]),",",repr(tk[1]),")",sep="")
def run(code:str):
    def lex():
        nonlocal code
        if code=="":
            return (EOF,None)
        while code[0]==' ':
            code=code[1:]
        if code=="":
            return (EOF,None)
        if code[0]=='\n':
            while code!="" and code[0]=='\n':
                code=code[1:]
            if code[0:4]=="    ":
                cnt=0
                while code[0:4]=="    ":
                    code=code[4:]
                    cnt+=1
                return (TAB,cnt)
            else:
                return (TAB,0)
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
            if s in "and,or,not,in,if,while,def,return,break,continue".split(","):
                return ({
                    "and":AND,
                    "or":OR,
                    "not":NOT,
                    "in":IN,
                    "if":IF,
                    "while":WHILE,
                    "def":DEF,
                    "return":RETURN,
                    "break":BREAK,
                    "continue":CONTINUE
                }[s],None)
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
        for k,v in op_dict.items():
            if code[:len(k)]==k:
                code=code[len(k):]
                return (v,None)
        raise
    tk=lex()
    def eat(expect=None):
        nonlocal tk
        if expect==None or tk[0]==expect:
            _tk=tk
            tk=lex()
            return _tk
        raise
    def eat_tab(num=0):
        nonlocal tk
        if tk[0]==TAB and tk[1]==num:
            tk=lex()
        else:
            raise
    def parse():
        nonlocal tk
        l=[]
        while tk[0]!=EOF:
            l.append(stmt())
            eat_tab()
        return ("program",l)
    def block(tab=0):
        eat(COLON)
        l=[]
        while tk==(TAB,tab+1):
            eat()
            l.append(stmt(tab+1))
        return l
    def stmt(tab=0):
        nonlocal tk
        if tk[0]==TAB:
            return ("noop",)
        if tk[0]==DEF:
            eat()
            name=eat(ID)[1]
            para=[]
            eat(LPAREN)
            if tk[0]!=RPAREN:
                para=[eat(ID)[1]]
                while tk[0]==COMMA:
                    eat()
                    para.append(eat(ID)[1])
            eat(RPAREN)
            return ("def",name,para,block(tab))
        if tk[0]==IF:
            eat()
            return ("if",expr(),block(tab))
        if tk[0]==WHILE:
            eat()
            return ("while",expr(),block(tab))
        if tk[0]==BREAK:
            eat()
            return ("break",)
        if tk[0]==CONTINUE:
            eat()
            return ("continue",)
        if tk[0]==RETURN:
            eat()
            return ("return",expr())
        else:
            e=expr()
            if tk[0]==ASSIGN:
                eat()
                return ("assign",e,expr())
            return e
    def expr():
        nonlocal tk
        res=expr1()
        while tk[0] in (AND,OR):
            res=("binary",eat()[0],res,expr1())
        return res
    def expr1():
        nonlocal tk
        res=expr2()
        while tk[0] in (BAND,BOR,XOR):
            res=("binary",eat()[0],res,expr2())
        return res
    def expr2():
        nonlocal tk
        res=expr3()
        while tk[0] in (EQ,NE,GT,LT,GE,LE):
            res=("binary",eat()[0],res,expr3())
        return res
    def expr3():
        nonlocal tk
        res=expr4()
        while tk[0] in (LSH,RSH):
            res=("binary",eat()[0],res,expr4())
        return res
    def expr4():
        nonlocal tk
        res=term()
        while tk[0] in (ADD,SUB):
            res=("binary",eat()[0],res,term())
        return res
    def term():
        nonlocal tk
        res=factor()
        while tk[0] in (MUL,DIV,MOD):
            res=("binary",eat()[0],res,factor())
        return res
    def factor():
        nonlocal tk
        if tk[0]==CONST:
            return fh(eat()[1])
        if tk[0]==ID:
            return fh(("var",eat()[1]))
        if tk[0] in (ADD,SUB,NOT,INV):
            return ("unary",eat()[0],fh(factor()))
        if tk[0]==LSB:
            eat()
            l=[]
            if tk[0]!=RSB:
                l.append(expr())
                while tk[0]==COMMA:
                    eat()
                    l.append(expr())
            eat(RSB)
            return fh(("mklist",l))
        print_token(tk)
        raise
    def fh(v):
        nonlocal tk
        if tk[0]==LSB:
            eat()
            n=expr()
            eat(RSB)
            return fh(("nth",v,n))
        if tk[0]==LPAREN:
            eat()
            args=[]
            if tk[0]!=RPAREN:
                args=[expr()]
                while tk[0]==COMMA:
                    eat()
                    args.append(expr())
            eat(RPAREN)
            return fh(("call",v,args))
        return v
    scope=[{
        "print":lambda *args:print(*args,sep="",end=""),
        "println":lambda *args:print(*args,sep=""),
        "input":lambda *args:input(*args),
        "getchar":lambda:sys.stdin.read(1),
        "chr":lambda a:chr(a),
        "ord":lambda a:ord(a),
        "len":lambda a:len(a),
    }]
    def inscope():
        nonlocal scope
        scope.append({})
    def outscope():
        nonlocal scope
        scope.pop()
    def findv(name):
        nonlocal scope
        for i in scope:
            if name in i:
                return i[name]
        raise
    def setv(name,value):
        nonlocal scope
        for i in scope:
            if name in i:
                i[name]=value
                return
        scope[-1][name]=value
    def runcode(tree):
        nonlocal scope
        if type(tree)!=tuple:
            return tree
        if len(tree)==0:
            return tree
        cmd=tree[0]
        if cmd=="program":
            for i in tree[1]:
                runcode(i)
        if cmd=="def":
            scope[-1][tree[1]]=(tree[2],tree[3],scope)
        elif cmd=="if":
            if runcode(tree[1]):
                for i in tree[2]:
                    if i[0] in ("return","break","continue"):
                        if i[0]=="return":
                            return ("return",runcode(i[1]))
                        return i
                    v=runcode(i)
                    if type(v)==tuple and v[0] in ("return","break","continue"):
                        return v
            return None
        elif cmd=="while":
            while runcode(tree[1]):
                inscope()
                for i in tree[2]:
                    if i[0]=="break":
                        outscope()
                        return
                    if i[0]=="continue":
                        break
                    if i[0]=="return":
                        outscope()
                        return ("return",runcode(i[1]))
                    v=runcode(i)
                    if type(v)==tuple and v[0]=="break":
                        outscope()
                        return
                    if type(v)==tuple and v[0]=="return":
                        outscope()
                        return v
                    if type(v)==tuple and v[0]=="continue":
                        break
                outscope()
            return None
        elif cmd=="var":
            return findv(tree[1])
        elif cmd=="mklist":
            return [runcode(i) for i in tree[1]]
        elif cmd=="nth":
            return runcode(tree[1])[runcode(tree[2])]
        elif cmd=="binary":
            return {
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
            }[tree[1]](runcode(tree[2]),runcode(tree[3]))
        elif cmd=="unary":
            return {
                ADD:lambda a:+a,
                SUB:lambda a:-a,
                NOT:lambda a:not a,
                INV:lambda a:~a,
            }[tree[1]](runcode(tree[2]))
        elif cmd=="call":
            func=runcode(tree[1])
            if type(func)==type(lambda:1):
                return func(*[runcode(i) for i in tree[2]])
            else:
                _scope=scope
                scope=func[2]
                inscope()
                scope[-1]=dict(zip(func[0],[runcode(i) for i in tree[2]]))
                res=None
                for i in func[1]:
                    if type(i)==tuple and i[0]=="return":
                        res=runcode(i[1])
                        break
                    v=runcode(i)
                    if type(v)==tuple and v[0]=="return":
                        res=v[1]
                        break
                scope=_scope
                return res
        elif cmd=="assign":
            lvalue=tree[1]
            v=runcode(tree[2])
            if lvalue[0]!="var":
                indexlist=[]
                while type(lvalue)==tuple and lvalue[0]=="nth":
                    indexlist=[runcode(lvalue[2])]+indexlist
                    lvalue=lvalue[1]
                def w(base,indexlist,v):
                    if indexlist==[]:
                        return v
                    base[indexlist[0]]=w(base[indexlist[0]],indexlist[1:],v)
                    return base
                name=lvalue[1]
                setv(name,w(runcode(lvalue),indexlist,v))
                return
            else:
                setv(lvalue[1],v)
                return
        else:
            return tree
    runcode(parse())
run('''
print("
这是用My Python实现的Brainfuck解释器
")
code=input("Brainfuck>")
mem=[0]*256
i=0
p=128
while i<len(code):
    ch=code[i]
    if ch=="+":
        mem[p]=mem[p]+1
    if ch=="-":
        mem[p]=mem[p]+1
    if ch=="<":
        p=p-1
    if ch==">":
        p=p+1
    if ch==",":
        mem[p]=ord(getchar())
    if ch==".":
        print(chr(mem[p]))
    if ch=="[":
        if not mem[p]:
            l=0
            r=0
            while i<len(code):
                if code[i]=="[":
                    l=l+1
                if code[i]=="]":
                    r=r+1
                    if l>0:
                        r=r-1
                        l=l-1
                if l==0 and r==0:
                    break
                i=i+1
            i=i+1
    if ch=="]":
        l=0
        r=0
        while i>=0:
            if code[i]=="]":
                r=r+1
            if code[i]=="[":
                l=l+1
                if r>0:
                    r=r-1
                    l=l-1
            if l==0 and r==0:
                break
            i=i-1
        i=i-1
    i=i+1
''')
'''
a=0
while a<10:
    if a==5:
        a=a+1
        continue
    if a==8:
        break
    println(a)
    a=a+1

a=[1,[2,3,4,5,7]]
println(a)
a[1][4]=6
println(a)

def f(s,time):
    i=0
    while 1:
        println(s)
        i=i+1
        if i==time:
            return time
    return None
println(f("Hello!",5))

def Counter(start):
    def inc():
        start=start+1
        return start
    return inc
counter=Counter(10)
i=0
while i<10:
    println(counter())
    i=i+1
'''