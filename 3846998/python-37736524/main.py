class Symbol:
    _id=0
    def __init__(self):
        self.id=Symbol._id
        Symbol._id+=1
    def __eq__(self,a):
        if type(a)==list:
            return self.id==a[0].id
        if a==None:
            return False
        if type(a)==int:
            return self.id==a
        return self.id==a.id
    def __ne__(self,a):
        if type(a)==list:
            return self.id!=a[0].id
        if type(a)==int:
            return self.id!=a
        return self.id!=a.id
    def __hash__(self):
        return hash(self.id)
EOF,ADD,SUB,MUL,DIV,MOD,EQ,NE,GT,LT,GE,LE,SHL,SHR,AND,OR,BITAND,BITOR,XOR,NOT,INV,LPAREN,RPAREN,LSB,RSB,BEGIN,END,LRSB,COMMA,ASSIGN,SEMI,ID=[Symbol() for i in range(-1,31)]
TP_int,TP_bool,TP_float,TP_null_t,TP_string=[Symbol() for i in range(5)]
V_int,V_bool,V_float,V_null_t,V_string=[Symbol() for i in range(5)]
KW_if,KW_else,KW_while,KW_for,KW_func=[Symbol() for i in range(5)]
class Token:
    def __init__(self,t,v=None):
        self.t=t
        self.v=v
op_int_dict={
    '+':ADD,
    '-':SUB,
    '*':MUL,
    '/':DIV,
    '%':MOD,
    '==':EQ,
    '!=':NE,
    '>=':GE,
    '<=':LE,
    '<<':SHL,
    '>>':SHR,
    '>':GT,
    '<':LT,
    '&&':AND,
    '||':OR,
    '&':BITAND,
    '|':BITOR,
    '^':XOR,
    '!':NOT,
    '~':INV,
    '(':LPAREN,
    ')':RPAREN,
    ',':COMMA,
    '=':ASSIGN,
    '{':BEGIN,
    '}':END,
    '[]':LRSB,
    '[':LSB,
    ']':RSB,
    ';':SEMI,
}
keyword_int_dict={
    "int":Token(TP_int),
    "bool":Token(TP_bool),
    "float":Token(TP_float),
    "null_t":Token(TP_null_t),
    "string":Token(TP_string),
    "null":Token(V_null_t,None),
    "true":Token(V_bool,True),
    "false":Token(V_bool,False),
    "if":Token(KW_if),
    "else":Token(KW_else),
    "while":Token(KW_while),
    "for":Token(KW_for),
    "func":Token(KW_func),
}
def initvalueof(tp):
    if type(tp)==list and len(tp)==1:
        tp=tp[0]
    if type(tp)==list:
        return [initvalueof(tp[1:]) for i in range(tp[0])]
    if tp==TP_int:
        return 0
    if tp==TP_bool:
        return False
    if tp==TP_float:
        return 0.0
    if tp==TP_null_t:
        return None
    if tp==TP_string:
        return ""
    raise
def typeof(v):
    if type(v)==tuple:
        return v[:-1]
    if type(v)==list:
        return [len(v)]+typeof(v[0])
    if type(v)==int:
        return [TP_int]
    if type(v)==bool:
        return [TP_bool]
    if type(v)==float:
        return [TP_float]
    if type(v)==str:
        return [TP_string]
    if v==None:
        return [TP_null_t]
def typename(tp):
    if type(tp)==list:
        return typename(tp[-1])+" "+" ".join(["None"]*len(tp[:-1]))
    if tp==TP_int:
        return "int"
    if tp==TP_bool:
        return "bool"
    if tp==TP_float:
        return "float"
    if tp==TP_null_t:
        return "null_t"
    if tp==TP_string:
        return "string"
class Value:
    def __init__(self,tp,v):
        self.tp=tp
        self.v=v
class Lexer:
    def __init__(self,t):
        self.t=t
        self.p=0
        self.ch=t[0]
    def peek(self,n=1):
        return self.t[self.p:self.p+n]
    def eat(self,n=1):
        self.p+=n
        if self.p>=len(self.t):
            self.ch=None
        else:
            self.ch=self.t[self.p]
    def getint(self):
        s=""
        while self.ch!=None and (self.ch.isdigit() or self.ch=='.'):
            s+=self.ch
            self.eat()
        if '.' in s:
            return Token(V_float,float(s))
        return Token(V_int,int(s))
    def getid(self):
        s=""
        while self.ch.isalnum() or self.ch in "_$@?'":
            s+=self.ch
            self.eat()
        return s
    def skip(self):
        while self.ch!=None and (self.ch in " \t\n" or self.peek(2)=="/*"):
            if self.ch=='':
                return
            while self.ch!=None and self.ch in " \t\n":
                self.eat()
                while self.peek(2)=="/*":
                    while self.peek(2)!="*/":
                        self.eat()
                    self.eat(2)
    def _char(self):
        if self.ch!="\\":
            w=self.ch
            return w
        self.eat()
        if self.ch=="u":
            s=""
            for i in range(4):
                self.advance()
                s+=self.ch
            i=s[0]*16*16*16+s[1]*16*16+s[2]*16+s[3]
            return chr(i)
        return {
            "t":"\t",
            "b":"\b",
            "n":"\n",
            "r":"\r",
            "\'":"\'",
            "\"":"\"",
            "\\":"\\"
        }[self.ch]
    def string(self):
        result=""
        while self.ch!=None and self.ch!="\"":
            result+=self._char()
            self.eat()
        if self.ch==None:
            self.error()
        self.eat()
        return Token(V_string,result)
    def get(self):
        self.skip()
        if self.ch==None:
            return Token(EOF,None)
        if self.ch.isalpha() or self.ch in "_$@?":
            i=self.getid()
            return keyword_int_dict.get(i,Token(ID,i))
        if self.ch.isdigit():
            return self.getint()
        if self.ch=='"':
            self.eat()
            return self.string()
        if self.ch=='\'':
            self.eat()
            c=self._char()
            self.eat()
            self.eat()
            return Token(V_int,ord(c))
        for x,y in op_int_dict.items():
            if self.peek(len(x))==x:
                self.eat(len(x))
                return Token(y,None)
class AST:
    def __init__(self,*l):
        self.l=l
    def __getitem__(self,i):
        return self.l[i]
class BinOp(AST):
    sign0=None
class UnaryOp(AST):
    sign1=None
class Block(AST):
    sign2=None
class VarDecl(AST):
    sign3=None
class Var(AST):
    sign4=None
class LiteralString(AST):
    sign5=None
class NoOp(AST):
    sign6=None
class CallFunc(AST):
    sign7=None
class Element(AST):
    sign8=None
class Assign(AST):
    sign9=None
class If(AST):
    sign10=None
class IfElse(AST):
    sign11=None
class While(AST):
    sign12=None
class For(AST):
    sign13=None
class FuncDecl(AST):
    sign14=None
class Parser:
    #Base
    def __init__(self,l):
        self.l=l
        self.tk=self.l.get()
    def eat(self,tp=-1):
        t=self.tk
        if t==None or (tp!=-1 and t.t!=tp):
            t=Token(EOF)
            raise Exception("Wrong input!Expected "+str(tp.id)+".Got "+str(t.t.id)+".")
        self.tk=self.l.get()
        return t
    #Statements
    def block(self):
        if self.tk.t==BEGIN:
            self.eat()
            l=[]
            while self.tk.t!=END:
                l.append(self.stmt())
            self.eat()
            return Block(l)
        return Block([self.stmt()])
    def stmt(self,f=1):
        if self.tk.t in (TP_int,TP_bool,TP_float,TP_null_t,TP_string):
            return self.vardecl(f)
        elif self.tk.t==BEGIN:
            return self.block()
        elif self.tk.t==SEMI:
            self.eat()
            return NoOp()
        elif self.tk.t==KW_if:
            self.eat();
            self.eat(LPAREN)
            e=self.expr()
            self.eat(RPAREN)
            b=self.block()
            if self.tk.t==KW_else:
                self.eat()    
                return IfElse(e,b,self.block())
            return If(e,b)
        elif self.tk.t==KW_while:
            self.eat();
            self.eat(LPAREN)
            e=self.expr()
            self.eat(RPAREN)
            b=self.block()
            return While(e,b)
        elif self.tk.t==KW_for:
            self.eat()
            self.eat(LPAREN)
            l=[self.stmt(0)]
            self.eat(SEMI)
            l+=[self.expr()]
            self.eat(SEMI)
            l+=[self.stmt(0)]
            self.eat(RPAREN)
            return For(*l,self.block())
        elif self.tk.t==KW_func:
            return self.funcdecl()
        else:
            v=self.expr()
            if self.tk.t==ASSIGN:
                self.eat()
                e=self.expr()
                if f:
                    self.eat(SEMI)
                return Assign(v,e)
            if f:
                self.eat(SEMI)
            return v
    def vardecl(self,f=1):
        tp=self.eat().t
        def w(self,tp,f):
            n=self.eat(ID).v
            level=[]
            while self.tk!=None and self.tk.t==LSB:
                self.eat()
                level.append(self.expr())
                self.eat(RSB)
            v=None
            if self.tk.t==ASSIGN:
                self.eat()
                v=self.expr()
            return [n,level+[tp],v]
        l=[w(self,tp,f)]
        while self.tk.t==COMMA:
            self.eat()
            l.append(w(self,tp,f))
        if f:
            self.eat(SEMI)
        return VarDecl(l)
    def funcdecl(self):
        self.eat()
        name=self.eat(ID).v
        para=[]
        paratp=[]
        self.eat(LPAREN)
        if self.tk.t!=RPAREN:
            paratp=[self.gettype()]
            para=[self.eat(ID).v]
            while self.tk.t==COMMA:
                self.eat()
                paratp.append(self.gettype())
                para.append(self.eat(ID).v)
        self.eat(RPAREN)
        self.eat(SUB)
        self.eat(GT)
        tp=self.gettype()
        return FuncDecl(name,tp,paratp,para,self.block())
    def gettype(self):
        base=[self.eat().t]
        while self.tk.t==LRSB:
            self.eat()
            base=[None]+base
        return base
    #Expression
    def expr_help(self,lower,l):
        ans=lower()
        while self.tk.t in l:
            ans=BinOp(self.eat().t,ans,lower())
        return ans
    term=lambda self:self.expr_help(self.factor,(MUL,DIV,MOD))
    expr0=lambda self:self.expr_help(self.term,(ADD,SUB))
    expr1=lambda self:self.expr_help(self.expr0,(SHL,SHR))
    expr2=lambda self:self.expr_help(self.expr1,(EQ,NE,GT,LT,GE,LE))
    expr3=lambda self:self.expr_help(self.expr2,(BITOR,XOR,BITAND))
    expr=lambda self:self.expr_help(self.expr3,(AND,OR))
    def factor(self):
        if self.tk.t==LPAREN:
            self.eat()
            v=self.expr()
            self.eat(RPAREN)
            return self.fh(v)
        if self.tk.t==ID:
            return self.fh(Var(self.eat().v))
        if self.tk.t in (V_int,V_bool,V_float,V_null_t):
            return self.fh(self.eat().v)
        if self.tk.t==V_string:
            return self.fh(self.eat().v)
        if self.tk.t in (ADD,SUB,NOT,INV):
            return UnaryOp(self.eat(),self.fh(self.factor()))
        raise Exception("Wrong input!")
    def fh(self,v):
        if self.tk.t==LPAREN:
            self.eat()
            l=[]
            if self.tk.t!=RPAREN:
                l=[self.expr()]
                while self.tk.t==COMMA:
                    self.eat()
                    l.append(self.expr())
            self.eat(RPAREN)
            return self.fh(CallFunc(v,l))
        if self.tk.t==LSB:
            self.eat()
            l=[self.expr()]
            self.eat(RSB)
            while self.tk.t==LSB:
                self.eat()
                l.append(self.expr())
                self.eat(RSB)
            return self.fh(Element(v,l))
        return v
class Scope:
    def __init__(self,p):
        self.var={}
        self.parent=p
    def define(self,n,v):
        self.var[n]=v
    def find(self,name):
        t=self
        while t!=None:
            if name in t.var.keys():
                return t.var[name]
            t=t.parent
        raise Exception("Undefined varible '"+str(name)+"'!")
    def set(self,name,value):
        t=self
        while t!=None:
            if name in t.var.keys():
                t.var[name]=value
                return
            t=t.parent
        raise Exception("Undefined varible '"+str(name)+"'!")
binop_fun_dict={
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
    SHL:lambda a,b:a<<b,
    SHR:lambda a,b:a>>b,
    AND:lambda a,b:a and b,
    OR:lambda a,b:a or b,
    BITAND:lambda a,b:a&b,
    BITOR:lambda a,b:a|b,
    XOR:lambda a,b:a^b,
}
unaryop_fun_dict={
    ADD:lambda a:+a,
    SUB:lambda a:-a,
    NOT:lambda a:not a,
    INV:lambda a:~a,
}
class Interpreter:
    def visit(self,node):
        method_name="visit_"+type(node).__name__
        visitor=getattr(self,method_name,self.generic_visit)
        return visitor(node)
    def generic_visit(self,node):
        raise Exception("Can't find method\"visit_{}()\"".format(type(node).__name__))
    def __init__(self,t,s=Scope(None)):
        self.t=t
        self.scope=s
    def visit_BinOp(self,t):
        return binop_fun_dict[t[0]](self.visit(t[1]),self.visit(t[2]))
    def visit_UnaryOp(self,t):
        return unaryop_fun_dict[t[0]](self.visit(t[1]))
    def visit_Block(self,t):
        for i in t.l[0]:
            self.visit(i)
    def visit_CallFunc(self,t):
        if type(t[0])==Var and t[0][0] in ("print","println","inputln","len","ord","chr"):
            a=[self.visit(i) for i in t[1]]
            name=t[0][0]
            if name=="print":
                return print(*a,sep="",end="")
            if name=="println":
                return print(*a,sep="")
            if name=="inputln":
                return input(*a)
            if name=="len":
                return len(*a)
            if name=="ord":
                return ord(*a)
            if name=="chr":
                return chr(*a)
        if type(t[0])!=Var:
            raise
        args=[self.visit(i) for i in t[1]]
        argtp=[typeof(i) for i in args]
        name=t[0][0]+" "+" ".join([typename(i) for i in argtp])
        func=self.scope.find(name).v
        para=func[2]
        block=func[3]
        i=Interpreter(block,Scope(self.scope))
        i.scope.var=dict(zip(para,[Value(typeof(j),j) for j in args]))
        return i.interprete()
    def visit_VarDecl(self,_t):
        for t in _t.l[0]:
            tp=t[1]
            name=t[0]
            if len(tp)==1:
                tp=tp[0]
            else:
                tp[:-1]=[self.visit(i) for i in tp[:-1]]
            if t[2]!=None:
                v=self.visit(t[2])
                if typeof(v)!=tp:
                    raise Exception("Wrong input!")
                self.scope.define(name,Value(tp,v))
            else:
                self.scope.define(name,Value(tp,initvalueof(tp)))
    def visit_Element(self,t):
        v=self.visit(t[0])
        l=[self.visit(i) for i in t[1]]
        while l!=[]:
            v=v[l[0]]
            l=l[1:]
        return v
    def visit_Assign(self,t):
        name=t[0][0]
        if type(name)==str:
            v=self.visit(t[1])
            if typeof(v)!=typeof(self.scope.find(name).v):
                raise Exception("Wrong input!")
            self.scope.set(name,Value(self.scope.find(name).tp,v))
            return
        vn=self.visit(name)
        name=name[0]
        base=[self.visit(i) for i in t[0][1]]
        v=self.visit(t[1])
        tp=typeof(vn)
        def w(base,l,v):
            if l==[]:
                return v
            base[l[0]]=w(base[l[0]],l[1:],v)
            return base
        vn=w(vn,base,v)
        if typeof(vn)!=tp:
            raise Exception("Wrong input!")
        self.scope.set(name,Value(self.scope.find(name).tp,vn))
    def visit_If(self,t):
        if self.visit(t[0]):
            Interpreter(t[1],Scope(self.scope)).interprete()
    def visit_IfElse(self,t):
        if self.visit(t[0]):
            Interpreter(t[1],Scope(self.scope)).interprete()
        else:
            Interpreter(t[2],Scope(self.scope)).interprete()
    def visit_While(self,t):
        while self.visit(t[0]):
            Interpreter(t[1],Scope(self.scope)).interprete()
    def visit_For(self,t):
        i1=Interpreter(t[0],Scope(self.scope))
        i1.interprete()
        while i1.visit(t[1]):
            Interpreter(t[3],Scope(i1.scope)).interprete()
            i1.visit(t[2])
    def visit_FuncDecl(self,t):
        name,rettp,paratp,para,block=t
        functp=(rettp,paratp)
        func=(rettp,paratp,para,block)
        funcname=name+" "+" ".join([typename(i) for i in paratp])
        self.scope.define(funcname,Value(functp,func))
    visit_int=lambda self,a:a
    visit_float=lambda self,a:a
    visit_bool=lambda self,a:a
    visit_NoneType=lambda self,a:a
    visit_list=lambda self,a:a
    visit_str=lambda self,a:a
    visit_Var=lambda self,t:self.scope.find(t[0]).v
    interprete=lambda self:self.visit(self.t)
Interpreter(Parser(Lexer('''
{
    func f(int a)->null_t{
        println(a);
    }
    func f(string a)->null_t{
        println(a);
    }
    f(10);
    f("hhh");
}
''')).stmt()).interprete()