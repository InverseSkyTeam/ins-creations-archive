EOF,ADD,SUB,MUL,DIV,MOD,EQ,NE,GT,LT,GE,LE,LSHIFT,RSHIFT,AND,OR,BITAND,BITOR,XOR,NOT,INV,INT,FLOAT,BOOL,NONE,STRING,ID,LPAREN,RPAREN,KW_print,KW_if,KW_while,KW_func,KW_var,COMMA,ASSIGN,BEGIN,END=[i for i in range(-1,37)]
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
    '<<':LSHIFT,
    '>>':RSHIFT,
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
}
keyword_int_dict={
    "print":Token(KW_print),
    "if":Token(KW_if),
    "while":Token(KW_while),
    "var":Token(KW_var),
    "True":Token(BOOL,True),
    "False":Token(BOOL,False),
    "None":Token(NONE,None),
}
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
            return Token(FLOAT,float(s))
        return Token(INT,int(s))
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
        return Token(STRING,result)
    def get(self):
        self.skip()
        if self.ch==None:
            return Token(EOF,None)
        if self.ch.isalpha() or self.ch in "_$@?'":
            i=self.getid()
            return keyword_int_dict.get(i,Token(ID,i))
        if self.ch.isdigit():
            return self.getint()
        if self.ch=='"':
            self.eat()
            return self.string()
        for x,y in op_int_dict.items():
            if self.peek(len(x))==x:
                self.eat(len(x))
                return Token(y,None)
class BinOp:
    def __init__(self,op,l,r):
        self.op=op
        self.l=l
        self.r=r
class Assign:
    def __init__(self,l,r):
        self.l=l
        self.r=r
class UnaryOp:
    def __init__(self,op,l):
        self.op=op
        self.l=l
class Var:
    def __init__(self,i):
        self.id=i
class Stmts:
    def __init__(self,l):
        self.l=l
class PrintStmt:
    def __init__(self,i):
        self.i=i
class VarDecl:
    def __init__(self,ns,vs):
        self.ns=ns
        self.vs=vs
class WhileStmt:
    def __init__(self,cond,block):
        self.c,self.b=cond,block
class IfStmt:
    def __init__(self,cond,block):
        self.c,self.b=cond,block
class Parser:
    def __init__(self,l):
        self.l=l
        self.tk=self.l.get()
    def eat(self,tp=-1):
        t=self.tk
        if tp!=-1 and t.t!=tp:
            raise
        self.tk=self.l.get()
        return t
    def var(self):
        return Var(self.eat(ID).v)
    def factor(self):
        if self.tk.t==LPAREN:
            self.eat()
            t=self.expr()
            self.eat(RPAREN)
            return t
        if self.tk.t==ID:
            return self.var()
        if self.tk.t in (INT,FLOAT,BOOL,NONE,STRING):
            ret=self.eat()
            return ret.v
        if self.tk.t in (ADD,SUB,NOT,INV):
            return UnaryOp(self.eat().t,self.factor())
    def expr_help(self,lower,l):
        ans=lower()
        while self.tk.t in l:
            ans=BinOp(self.eat().t,ans,lower())
        return ans
    term=lambda self:self.expr_help(self.factor,(MUL,DIV,MOD))
    expr0=lambda self:self.expr_help(self.term,(ADD,SUB))
    expr1=lambda self:self.expr_help(self.expr0,(LSHIFT,RSHIFT))
    expr2=lambda self:self.expr_help(self.expr1,(EQ,NE,GT,LT,GE,LE))
    expr3=lambda self:self.expr_help(self.expr2,(BITOR,XOR,BITAND))
    expr=lambda self:self.expr_help(self.expr3,(AND,OR))
    def stmts(self):
        l=[]
        while self.tk!=None and self.tk.t!=EOF and self.tk.t!=END:
            l.append(self.stmt())
        return Stmts(l)
    def stmt(self):
        if self.tk.t==KW_while:
            self.eat()
            self.eat(LPAREN)
            c=self.expr()
            self.eat(RPAREN)
            self.eat(BEGIN)
            b=self.stmts()
            self.eat(END)
            return WhileStmt(c,b)
        if self.tk.t==KW_if:
            self.eat()
            self.eat(LPAREN)
            c=self.expr()
            self.eat(RPAREN)
            self.eat(BEGIN)
            b=self.stmts()
            self.eat(END)
            return IfStmt(c,b)
        if self.tk.t==KW_print:
            self.eat()
            return PrintStmt(self.expr())
        if self.tk.t==KW_var:
            self.eat()
            ns=[self.eat(ID).v]
            vs=[]
            if self.tk.t==ASSIGN:
                self.eat()
                vs.append(self.expr())
            else:
                vs.append(None)
            while self.tk.t==COMMA:
                self.eat()
                ns.append(self.eat(ID).v)
                if self.tk.t==ASSIGN:
                    self.eat()
                    vs.append(self.expr())
                else:
                    vs.append(None)
            return VarDecl(ns,vs)
        else:
            l=self.expr()
            if self.tk.t==ASSIGN:
                self.eat()
                r=self.expr()
                return Assign(l,r)
            else:
                return l
    parse=stmts
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
    LSHIFT:lambda a,b:a<<b,
    RSHIFT:lambda a,b:a>>b,
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
    def __init__(self,ast,scope=Scope(None)):
        self.ast=ast
        self.scope=scope
    def visit_BinOp(self,bo):
        return binop_fun_dict[bo.op](self.visit(bo.l),self.visit(bo.r))
    def visit_UnaryOp(self,bo):
        return unaryop_fun_dict[bo.op](self.visit(bo.l))
    def visit_Stmts(self,v):
        for i in v.l:
            self.visit(i)
    def visit_PrintStmt(self,v):
        print(self.visit(v.i))
    def visit_VarDecl(self,t):
        for i in range(len(t.ns)):
            self.scope.define(t.ns[i],self.visit(t.vs[i]))
    def visit_Var(self,t):
        return self.scope.find(t.id)
    def visit_WhileStmt(self,t):
        while self.visit(t.c):
            Interpreter(t.b,Scope(self.scope)).interprete()
    def visit_IfStmt(self,t):
        if self.visit(t.c):
            Interpreter(t.b,Scope(self.scope)).interprete()
    def visit_Assign(self,t):
        self.scope.set(t.l.id,self.visit(val))
    visit_int=lambda self,a:a
    visit_float=lambda self,a:a
    visit_NoneType=lambda self,a:a
    visit_bool=lambda self,a:a
    visit_list=lambda self,a:a
    visit_str=lambda self,a:a
    def interprete(self):
        return self.visit(self.ast)
Interpreter(Parser(Lexer('''
print "这是一个简单的解释器，只有334行，并且还可以压缩
它实现的语言甚至不是图灵完备的，但是它有表达式、循环、判断、输出等特性，可以完整演示解释器的实现
这个解释器五脏俱全，有词法分析器、语法分析器和解释器三部分
大家可以把它改编成一个完整的解释器，但不许转载"
''')).parse()).interprete()