'''
为了在Python区继续保持领先，我做了这次更新
这个语言可以随便转载/改编，也欢迎使用和挑错
这五行可以随便删，不用注明原作者
'''
###############AST定义{
class BinOp:
    def __init__(self,op,l,r):
        self.op,self.l,self.r=op,l,r
class UnaryOp:
    def __init__(self,op,e):
        self.op,self.e=op,e
class NoOp:
    pass
class Var:
    def __init__(self,n):
        self.n=n
class VarDecl:
    def __init__(self,ns,vs):
        self.ns,self.vs=ns,vs
class IfStmt:
    def __init__(self,cond,b1,b2=NoOp()):
        self.cond,self.b1,self.b2=cond,b1,b2
class WhileStmt:
    def __init__(self,cond,b):
        self.cond,self.b=cond,b
class ForStmt:
    def __init__(self,pre,cond,_next,b):
        self.pre,self.cond,self.next,self.b=pre,cond,_next,b
class ReturnStmt:
    def __init__(self,v):
        self.value=v
class List:
    def __init__(self,v):
        self.value=v
class Block:
    def __init__(self,v):
        self.children=v
class BreakStmt:
    sign0=0
class ContinueStmt:
    sign1=0
class AssignStmt:
    def __init__(self,n,v):
        self.name,self.value=n,v
class TryExceptStmt:
    def __init__(self,n,v):
        self.code0,self.code1=n,v
class Element:
    def __init__(self,v,idx):
        self.v,self.idx=v,idx
class GetObjectAttr:
    def __init__(self,v,n):
        self.v,self.n=v,n
class GetTypeAttr:
    def __init__(self,tp,n):
        self.tp,self.n=tp,n
class CallFunc:
    def __init__(self,f,args):
        self.f,self.args=f,args
class List:
    def __init__(self,v):
        self.value=v
###############}
###############类型定义{
class IFunction:
    def __init__(self,para,block,prev=NoOp(),next=NoOp()):
        self.para,self.block,self.prev,self.next=para,block,prev,next
class IType:
    def __init__(self,con,attr,parents):
        self.constructor,self.attr,self.parents=con,attr,parents
class IModule:
    def __init__(self,attr):
        self.attr=attr
class IObject:
    def __init__(self,tp,attr):#注：tp应为对一个IType对象的引用
        self.tp,self.attr=tp,attr
###############}
class Symbol:
    code=0
    def __init__(self):
        self.id=Symbol.code
        Symbol.code+=1
    def __eq__(self,b):
        return self.id==b.id
    def __ne__(self,b):
        return self.id!=b.id
    def __hash__(self):
        return hash(self.id)
EOF=Symbol()
ADD,SUB,MUL,DIV,MOD,EQ,NE,GT,LT,GE,LE,LSHIFT,RSHIFT,AND,OR,BITAND,BITOR,XOR,NOT,INV=[Symbol() for i in range(20)]
LSB,RSB,LPAREN,RPAREN,BEGIN,END=[Symbol() for i in range(6)]
COLON,SEMICOLON,COMMA,MODULE_ATTR,DOT,ASSIGN=[Symbol() for i in range(6)]
ID,INT,BOOL,FLOAT,STRING,NULL=[Symbol() for i in range(6)]
class Token:
    def __init__(self,vt,v):
        self.value_type,self.value=vt,v
    def __str__(self):
        return "Token({},{})".format(self.value_type,self.value)
    def __repr__(self):
        return self.__str__()
key_tokens=(
    ("::",Token(MODULE_ATTR,"::")),
    (".",Token(DOT,".")),
    (":",Token(COLON,":")),
    ("{",Token(BEGIN,"{")),
    (",",Token(COMMA,",")),
    ("}",Token(END,"}")),
    (";",Token(SEMICOLON,";")),
    (".",Token(DOT,".")),
    ("+",Token(ADD,"")),
    ("-",Token(SUB,"")),
    ("*",Token(MUL,"")),
    ("/",Token(DIV,"")),
    ("(",Token(LPAREN,"")),
    (")",Token(RPAREN,"")),
    ("[",Token(LSB,"")),
    ("]",Token(RSB,"")),
    ("%",Token(MOD,"")),
    ("~",Token(INV,"")),
    ("&&",Token(AND,"")),
    ("||",Token(OR,"")),
    ("|",Token(BITOR,"")),
    ("&",Token(BITAND,"")),
    ("^",Token(XOR,"")),
    (">>",Token(RSHIFT,"")),
    ("<<",Token(LSHIFT,"")),
    ("==",Token(EQ,"")),
    ("!=",Token(NE,"")),
    (">=",Token(GE,"")),
    ("<=",Token(LE,"")),
    (">",Token(GT,"")),
    ("<",Token(LT,"")),
    ("=",Token(ASSIGN,"")),
    ("!",Token(NOT,"")),
)
class Lexer:
    def __init__(self,t):
        self.text,self.pos,self.currend_char=t+"\n",0,t[0]
    def error(self):
        raise Exception("Wrong input!")
    def advance(self):
        self.pos+=1
        if self.pos>=len(self.text):
            self.currend_char=None
        else:
            self.currend_char=self.text[self.pos]
    def skip_whitespace(self):
        while self.currend_char!=None and self.currend_char in " \n\t":
            self.advance()
    def long_integer(self):
        result=""
        while self.currend_char!=None and self.currend_char in "0123456789.":
            result+=self.currend_char
            self.advance()
        if "." in result:
            return float(result)
        else:
            return int(result)
    def peek(self,n=1):
        pos=self.pos+n
        if pos>=len(self.text):
            return None
        else:
            return self.text[self.pos:pos]
    def skip_comment(self):
        while self.peek(2)!="*/":
            self.advance()
        self.advance()
        self.advance()
    def _id(self):
        result=""
        while self.currend_char!=None and (self.currend_char.isalnum() or self.currend_char=="_"):
            result+=self.currend_char
            self.advance()
        if result=="true":
            return Token(BOOL,True)
        if result=="false":
            return Token(BOOL,False)
        if result=="null":
            return Token(NULL,None)
        return Token(ID,result)
    def match(self,s,skip=True):
        if self.peek(len(s))==s:
            if skip:
                self.pos+=len(s)
                self.currend_char=self.text[self.pos]
            return True
        return False
    def _char(self):
        if self.currend_char!="\\":
            w=self.currend_char
            return w
        self.advance()
        if self.currend_char=="u":
            s=""
            for i in range(4):
                self.advance()
                s+=self.currend_char
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
        }[self.currend_char]
    def string(self):
        result=""
        while self.currend_char!=None and self.currend_char!="\"":
            result+=self._char()
            self.advance()
        if self.currend_char==None:
            self.error()
        self.advance()
        return Token(STRING,result)
    def get_next_token(self):
        while self.currend_char!=None:
            if self.currend_char in " \n\t":
                self.skip_whitespace()
                continue
            if self.peek(2)=="/*":
                self.advance()
                self.advance()
                self.skip_comment()
                continue
            if self.peek(2)=="//":
                self.advance()
                self.advance()
                while self.currend_char!="\n":
                    self.advance()
                continue
            if self.currend_char=="\"":
                self.advance()
                return self.string()
            ch=self.currend_char
            if ch.isalpha() or ch=="_":
                return self._id()
            if ch in "0123456789":
                r=self.long_integer()
                if type(r)==float:
                    return Token(FLOAT,r)
                else:
                    return Token(INT,r)
            for k,v in key_tokens:
                if self.match(k):
                    return v
            self.error()
        return Token(EOF,None)
    def token_list(self):
        ans=[]
        while ans==[] or ans[-1].value_type!=EOF:
            ans.append(self.get_next_token())
        return ans
class Parser:
    def __init__(self,l):
        self.lexer,self.error=l,l.error
        self.currend_token=self.lexer.get_next_token()
    def eat(self,tt=None):
        if type(tt)==type(None):
            t=self.currend_token
            self.currend_token=self.lexer.get_next_token()
            return t
        if self.currend_token.value_type!=tt:
            self.error()
        t=self.currend_token
        self.currend_token=self.lexer.get_next_token()
        return t
    def token_eq(self,t):
        return self.currend_token.value_type==t.value_type and self.currend_token.value==t.value
    def eat_token(self,t):
        if not self.token_eq(t):
            self.error()
        self.currend_token=self.lexer.get_next_token()
        return t
    def factor_help(self,v):
        if self.currend_token.value_type==DOT:
            self.eat()
            return GetObjectAttr(v,self.eat(ID).value)
        if self.currend_token.value_type==MODULE_ATTR:
            self.eat()
            return GetTypeAttr(v,self.eat(ID).value)
        if self.currend_token.value_type==LSB:
            self.eat()
            e=self.expr()
            self.eat(RSB)
            return self.factor_help(Element(v,e))
        if self.currend_token.value_type==LPAREN:
            self.eat()
            l=[]
            if self.currend_token.value_type!=RPAREN:
                l=[self.expr()]
                while self.currend_token.value_type==COMMA:
                    self.eat()
                    l.append(self.expr())
            self.eat(RPAREN)
            return self.factor_help(CallFunc(v,l))
        return v
    def stmt(self):
        if self.currend_token.value_type==SEMICOLON:
            return NoOp()
        elif self.token_eq(Token(ID,"var")):
            self.eat()
            ns=[self.eat(ID).value]
            vs=[None]
            if self.currend_token.value_type==ASSIGN:
                self.eat()
                vs[-1]=self.expr()
            while self.currend_token.value_type==COMMA:
                self.eat()
                ns.append(self.eat(ID).value)
                vs.append(None)
                if self.currend_token.value_type==ASSIGN:
                    self.eat()
                    vs[-1]=self.expr()
            return VarDecl(ns,vs)
        elif self.token_eq(Token(ID,"if")):
            self.eat()
            self.eat(LPAREN)
            cond=self.expr()
            self.eat(RPAREN)
            b=self.block()
            if self.token_eq(Token(ID,"else")):
                self.eat()
                return IfStmt(cond,b,self.block())
            return IfStmt(cond,b)
        elif self.token_eq(Token(ID,"while")):
            self.eat()
            self.eat(LPAREN)
            cond=self.expr()
            self.eat(RPAREN)
            return WhileStmt(cond,self.block())
        elif self.token_eq(Token(ID,"break")):
            self.eat()
            return BreakStmt()
        elif self.token_eq(Token(ID,"continue")):
            self.eat()
            return ContinueStmt()
        elif self.token_eq(Token(ID,"return")):
            self.eat()
            return ReturnStmt(self.expr())
        else:
            e=self.expr()
            if self.currend_token.value_type==ASSIGN:
                self.eat()
                return AssignStmt(e,self.expr())
            return e
    def block(self):
        x=[IfStmt,WhileStmt]
        if self.currend_token.value_type!=BEGIN:
            s=self.stmt()
            if type(s) not in x:
                self.eat(SEMICOLON)
            return Block([s])
        else:
            self.eat()
            l=[]
            while self.currend_token.value_type!=END:
                l.append(self.stmt())
                if type(l[-1]) not in x:
                    print(self.currend_token.value_type.id)
                    self.eat(SEMICOLON)
            self.eat(END)
            return Block(l)
    def factor(self):
        def parse_lambda(self):
            para=[]
            self.eat(LPAREN)
            if self.currend_token.value_type!=RPAREN:
                para=[self.eat(ID).value]
                while self.currend_token.value_type==COMMA:
                    self.eat()
                    para.append(self.eat(ID).value)
            self.eat(RPAREN)
            return IFunction(para,self.block())
        if self.currend_token.value_type in (INT,BOOL,NULL,STRING,FLOAT):
            return self.factor_help(self.eat().value)
        if self.currend_token.value_type==LPAREN:
            self.eat()
            e=self.expr()
            self.eat(RPAREN)
            return self.factor_help(e)
        if self.currend_token.value_type in (ADD,SUB,NOT,INV):
            t=self.eat()
            return UnaryOp(t,self.factor())
        if self.currend_token.value_type==LSB:
            self.eat()
            l=[]
            if self.currend_token.value_type!=RSB:
                l=[self.expr()]
                while self.currend_token.value_type==COMMA:
                    self.eat()
                    l.append(self.expr())
            self.eat(RSB)
            return self.factor_help(List(l))
        if self.token_eq(Token(ID,"lambda")):
            self.eat()
            return self.factor_help(parse_lambda(self))
        if self.token_eq(Token(ID,"anonymous_class")):
            self.eat()
            parents=[]
            if self.currend_token.value_type==COLON:
                self.eat()
                parents=[self.expr()]
                while self.currend_token.value_type==COMMA:
                    self.eat()
                    parents.append(self.expr())
            self.eat_token(Token(ID,"constructor"))
            constructor=parse_lambda(self)
            block=self.block()
            return self.factor_help(IType(constructor,block,parents))
        if self.currend_token.value_type==ID:
            return self.factor_help(Var(self.eat().value))
    def expr_help(self,lower,l):
        ans=lower()
        while self.currend_token.value_type in l:
            ans=BinOp(self.eat(),ans,lower())
        return ans
    term=lambda self:self.expr_help(self.factor,(MUL,DIV,MOD))
    expr0=lambda self:self.expr_help(self.term,(ADD,SUB))
    expr1=lambda self:self.expr_help(self.expr0,(LSHIFT,RSHIFT))
    expr2=lambda self:self.expr_help(self.expr1,(EQ,NE,GT,LT,GE,LE))
    expr3=lambda self:self.expr_help(self.expr2,(BITOR,XOR,BITAND))
    expr=lambda self:self.expr_help(self.expr3,(AND,OR))
class NodeVisitor:
    def visit(self,node):
        method_name="visit_"+type(node).__name__
        visitor=getattr(self,method_name,self.generic_visit)
        return visitor(node)
    def generic_visit(self,node):
        raise Exception("Can't find method\"visit_{}()\"".format(type(node).__name__))
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
        raise Exception("Wrong id!")
    def set(self,name,value):
        t=self
        while t!=None:
            if name in t.var.keys():
                t.var[name]=value
                return
            t=t.parent
        raise Exception("Wrong id!")
    def buildin(self,things):
        for k,v in things.items():
            self.var[k]=v
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
class Interpreter(NodeVisitor):
    def __init__(self,t,scope=Scope(None)):
        self.t=t
        self.scope=scope
    def visit_BinOp(self,n):
        l=[self.visit(n.l),self.visit(n.r)]
        return binop_fun_dict[n.op.value_type](*l)
    def visit_UnaryOp(self,n):
        return unaryop_fun_dict[n.op.value_type](self.visit(n.e))
    def visit_VarDecl(self,n):
        for i in range(len(n.ns)):
            self.scope.define(n.ns[i],self.visit(n.vs[i]))
    def visit_CallFunc(self,n):
        try:
            self.visit(self.visit(n.func).begin)
        except:
            pass
        f=self.visit(n.f)
        args=[self.visit(i) for i in n.args]
        if type(f)==type(lambda:0):
            return f(*args)
        if type(f)==IType:
            func=f.constructor
            self.scope=Scope(self.scope)
            self.scope.define("this",self.NewObject(f))
            self.visit(CallFunc(func,args))
            res=self.scope.find("this")
            self.scope=self.scope.parent
            return res
        para=f.para
        code=f.block
        ns=Scope(self.scope)
        ns.var=dict(zip(para,args))
        ni=Interpreter(code,ns)
        ret=ni.interprete()
        if ret==None:
            return None
        return ret.value
    def visit_Block(self,n):
        self.scope=Scope(self.scope)
        for i in n.children:
            t=self.visit(i)
            if t!=None:
                self.scope=self.scope.parent
                return t
        self.scope=self.scope.parent
    def visit_IfStmt(self,n):
        if self.visit(n.cond):
            return self.visit(n.b1)
        else:
            return self.visit(n.b2)
    def visit_WhileStmt(self,n):
        while self.visit(n.cond):
            t=self.visit(n.b)
            if type(t)==BreakStmt:
                break
            if type(t)==ReturnStmt:
                return t
    def GetAllAttrs(self,tp):
        tp=self.visit(tp)
        ret={}
        for i in tp.parents:
            v=self.GetAllAttrs(i)
            for k,v in v.items():
                ret[k]=v
        for k,v in tp.attr.items():
            ret[k]=v
        return ret
    def NewObject(self,tp):
        return IObject(tp,self.GetAllAttrs(self.visit(tp)))
    def visit_AssignStmt(self,n):
        value=self.visit(n.value)
        name=n.name
        ELEMENT,OBJATTR,TYPEATTR=0,1,2
        indexs=[]
        indextypes=[]
        while type(name)!=Var:
            t=type(name)
            if t==Element:
                indexs.append(self.visit(name.idx))
                name=name.v
                indextypes.append(ELEMENT)
            elif t==GetTypeAttr:
                indexs.append(name.n)
                name=name.tp
                indextypes.append(TYPEATTR)
            elif t==GetObjectAttr:
                indexs.append(name.n)
                name=name.v
                indextypes.append(OBJATTR)
            else:
                raise Exception("Wrong input!")
        def w(value,idx,idxtp,dest):
            if len(idx)==0:
                return dest
            tp=idxtp[0]
            i=idx[0]
            idx=idx[1:]
            idxtp=idxtp[1:]
            if tp==ELEMENT:
                value[i]=w(value[i],idx,idxtp,dest)
            elif tp==OBJATTR:
                value.attr[i]=w(value.attr[i],idx,idxtp,dest)
            elif tp==TYPEATTR:
                value.attr[i]=w(value.attr[i],idx,idxtp,dest)
            return value
        base=self.visit(name)
        base=w(base,indexs,indextypes,value)
        self.scope.set(name.n,base)
    def interprete(self,tp=0):
        if tp==1:
            self.visit(self.t)
            return self.scope
        return self.visit(self.t)
    def visit_IType(self,n):
        if type(n.attr)==dict:
            return n
        ns=Scope(self.scope)
        ni=Interpreter(n.attr,ns)
        for i in n.attr.children:
            ni.visit(i)
        n.attr=ni.scope.var
        return n
    def visit_GetObjectAttr(self,a):
        f=self.visit(a.v).attr[a.n]
        l=self.visit(a.v)
        if type(f)==IFunction:
            return IFunction(f.para,f.block,VarDecl(Var("this"),l))
        return f
    def visit_GetTypeAttr(self,a):
        return self.GetAllAttrs(self.visit(a.tp))[a.n]
    visit_BreakStmt=visit_ContinueStmt=lambda self,a:a
    visit_ReturnStmt=lambda self,a:ReturnStmt(self.visit(a.value))
    visit_Var=lambda self,a:self.scope.find(a.n)
    visit_Element=lambda self,n:self.visit(n.v)[self.visit(n.idx)]
    visit_List=lambda self,n:[self.visit(i) for i in n.value]
    visit_NoOp=lambda self,a:None
    visit_int=visit_float=visit_bool=vsiit_TextIOWrapper=visit_str=visit_NoneType=visit_IFunction=visit_IModule=lambda self,a:a
def run(code,scope):
    Interpreter(Parser(Lexer(code)).block(),scope).interprete()
def runfile(f,scope):
    s=""
    with open(f,"r") as f:
        s+=f.read()+"\n"
    run(s,scope)
main=Scope(None)
main.buildin({
    "puts":lambda l:print(l),
    "fopen":lambda *l:open(*l),
    "fclose":lambda *l:close(*l),
    "fputs":lambda f,*l:f.write(*l),
    "fgets":lambda f,*l:f.read(*l),
    "gets":lambda:input(),
    "chr":lambda *a:chr(*a),
    "ord":lambda *a:ord(*a),
    "default_to_string":lambda *a:str(*a),
})