import copy
#常量定义{
ADD,SUB,MUL,DIV,MOD="ADD,SUB,MUL,DIV,MOD".split(",")
EQ,NE,GT,LT,GE,LE="EQ,NE,GT,LT,GE,LE".split(",")
LSHIFT,RSHIFT="LSHIFT,RSHIFT".split(",")
AND,OR="AND,OR".split(",")
BAND,BOR,XOR="BAND,BOR,XOR".split(",")
NOT,INV="NOT,INV".split(",")
INC,DEC="INT,DEC".split(",")
LPAREN,RPAREN,COLON,SEMICOLON,COMMA,DOT,DCOLON="LPAREN,RPAREN,COLON,SEMICOLON,COMMA,DOT,DCOLON".split(",")
LSB,RSB,BEGIN,END="LSB,RSB,BEGIN,END".split(",")
ASSIGN="ASSIGN"
ID,CONST="ID,CONST".split(",")
EOF="EOF"
#}
#类型定义{
class NoInitValue:
    nivsym=0
class IFunction:
    def __init__(self,para,paravalue,code,closure):
        self.para=para
        self.paravalue=paravalue
        self.code=code
        self.closure=closure
class IMemberFunction:
    def __init__(self,obj,func):
        self.obj=obj
        self.func=func
class IType:
    def __init__(self,parents,cons,attr):
        self.parents=parents
        self.cons=cons
        self.attr=attr
    def append_attr(self,name,value):
        self.attr[name]=value
    def get_attr(self,name):
        return self.attr[name]
class IObject:
    def __init__(self,tp,attr):
        self.tp=tp
        self.attr=attr
    def append_attr(self,name,value):
        self.attr[name]=value
        self.tp.attr[name]=None
    def get_attr(self,name):
        ret=self.attr[name]
        if type(ret)==IFunction:
            return IMemberFunction(self,ret)
        return ret
class IModule:
    def __init__(self,attr):
        self.attr=attr
    def append_attr(self,name,value):
        self.attr[name]=value
    def get_attr(self,name):
        return self.attr[name]
class IReference:
    def __init__(self,base):
        self.base=base
#}
#this栈{
class stack:
    def __init__(self):
        self.l=[]
    def push(self,n):
        self.l.append(n)
    def pop(self):
        return self.l.pop()
    def top(self):
        return self.l[-1]
this_stack=stack()
#}
#运算符及其对应的常量{
op_dict={
    '++':INC,
    '--':DEC,
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
    '&':BAND,
    '|':BOR,
    '^':XOR,
    '!':NOT,
    '~':INV,
    '(':LPAREN,
    ')':RPAREN,
    '::':DCOLON,
    ':':COLON,
    ';':SEMICOLON,
    ',':COMMA,
    '.':DOT,
    '=':ASSIGN,
    '[':LSB,
    ']':RSB,
    '{':BEGIN,
    '}':END,
}
#}
#Token类定义{
class Token:
    def __init__(self,tp,v):
        self.tp=tp
        self.v=v
    def __str__(self):
        return f"Token({self.tp},{self.v})"
#}
#错误定义{
class LexerError:
    lesym=0
    def __init__(self,msg="None"):
        self.msg=msg
class ParserError:
    pesym=0
    def __init__(self,msg="None"):
        self.msg=msg
class InterpreterError:
    iesym=0
    def __init__(self,msg="None"):
        self.msg=msg
def throw(error):
    if type(error)==IObject:
        print(f"{error.attr['error_name']}:{error.attr['error_message']}")
        exit(-1)
    print(f"{type(error).__name__}:{error.msg}.")
    exit(-1)
#}
#词法分析器{
class Lexer:
    def __init__(self,text,p=0,line=1,row=1):
        self.text=text
        self.p=p
        self.ch=self.text[self.p]
        self.line=line
        self.row=row
    def nc(self,n=1):
        self.p+=n
        self.row+=n
        if self.p>=len(self.text):
            self.ch=""
        else:
            self.ch=self.text[self.p]
    def peek(self,n=1):
        return self.text[self.p:self.p+n]
    def char(self):
        if self.ch!='\\':
            return self.ch
        if self.peek(2)=="\\x":
            self.nc(2)
            s=self.peek(2)
            self.nc()
            return chr(int(s,base=16))
        if self.peek(2)=="\\u":
            self.nc(2)
            s=self.peek(4)
            self.nc(3)
            return chr(int(s,base=16))
        table={
            "\\":"\\",
            "n":"\n",
            "t":"\t",
            "\"":"\"",
            "\'":"\'",
            "f":"\f",
            "r":"\r",
            "a":"\a",
            "v":"\v",
            "b":"\b",
        }
        self.nc()
        return table[self.ch]
    def get(self):
        while self.ch!="" and (self.ch in " \n\t" or self.peek(2) in ("//","/*")):
            if self.ch=='\n':
                self.nc()
                self.line+=1
                self.row=1
            elif self.ch in " \t":
                self.nc()
            elif self.peek(2)=='//':
                self.nc(2)
                while self.ch!='\n':
                    self.nc()
                self.line+=1
                self.row=1
            elif self.peek(2)=='/*':
                self.nc(2)
                while self.peek(2)!='*/':
                    if self.ch=='\n':
                        self.line+=1
                        self.row=0
                    self.nc()
                self.nc(2)
        if self.ch=='':
            return Token(EOF,None)
        if self.ch.isdigit():
            i=1
            while len(self.peek(i))==i and (self.peek(i)[-1].isdigit() or self.peek(i)[-1]=='.'):
                i+=1
            i-=1
            res=self.peek(i)
            self.nc(i)
            if '.' in res:
                return Token(CONST,float(res))
            return Token(CONST,int(res))
        if self.ch.isalnum() or self.ch=='_':
            i=1
            while len(self.peek(i))==i and self.peek(i).isidentifier():
                i+=1
            i-=1
            res=self.peek(i)
            self.nc(i)
            if res=="true":
                return Token(CONST,True)
            if res=="false":
                return Token(CONST,False)
            if res=="null":
                return Token(CONST,None)
            return Token(ID,res)
        if self.ch=='"':
            self.nc()
            s=""
            i=1
            while len(self.peek(i))==i and self.ch!='"':
                if self.ch=='\n':
                    self.line+=1
                    self.row=1
                s+=self.char()
                self.nc()
            self.nc()
            return Token(CONST,s)
        for k,v in op_dict.items():
            if self.peek(len(k))==k:
                self.nc(len(k))
                return Token(v,None)
        throw(LexerError(f"Unexpected character '{self.ch}' at line {self.line} row {self.row}"))
#}
#AST定义{
class NoOp:
    pass
class BinOp:
    def __init__(self,op,l,r):
        self.op=op
        self.l=l
        self.r=r
class UnaryOp:
    def __init__(self,op,e):
        self.op=op
        self.e=e
class Var:
    def __init__(self,name):
        self.name=name
class List:
    def __init__(self,l):
        self.l=l
class While:
    def __init__(self,cond,block):
        self.cond=cond
        self.block=block
class If:
    def __init__(self,cond,true,false):
        self.cond=cond
        self.true=true
        self.false=false
class NewType:
    def __init__(self,parents,cons,block):
        self.parents=parents
        self.cons=cons
        self.block=block
class NewModule:
    def __init__(self,body):
        self.body=body
class NewObject:
    def __init__(self,attr):
        self.attr=attr
class VarDecl:
    def __init__(self,name,value):
        self.name=name
        self.value=value
class DOTOp:
    dotosym=0
    def __init__(self,l,r):
        self.l=l
        self.r=r
class DCOLONOp:
    dcolonosym=0
    def __init__(self,l,r):
        self.l=l
        self.r=r
class ElementOp:
    eosym=0
    def __init__(self,l,r):
        self.l=l
        self.r=r
class Block:
    def __init__(self,stmts):
        self.stmts=stmts
class CallFunc:
    def __init__(self,func,args):
        self.func=func
        self.args=args
class Break:
    bsym=0
class Continue:
    csym=0
class Return:
    def __init__(self,retvalue):
        self.retvalue=retvalue
class IndexType:
    ELEMENT=0
    OBJ_ATTR=1
    TYPE_ATTR=2
class Assign:
    def __init__(self,base,target):
        self.base=base
        self.target=target
class Import:
    def __init__(self,module):
        self.module=module
class For:
    def __init__(self,begin,cond,end,body):
        self.begin=begin
        self.cond=cond
        self.end=end
        self.body=body
class Foreach:
    def __init__(self,var,base,body):
        self.var=var
        self.base=base
        self.body=body
class Switch:
    def __init__(self,base,cases,bodys,default):
        self.base=base
        self.cases=cases
        self.bodys=bodys
        self.default=default
class Reference:
    def __init__(self,base):
        self.base=base
class DeReference:
    def __init__(self,base):
        self.base=base
class Tuple:
    tsym=0
    def __init__(self,l):
        self.l=l
class FunctionInit:
    def __init__(self,para,paravalue,code):
        self.para=para
        self.paravalue=paravalue
        self.code=code
class TryExcept:
    def __init__(self,tryblock,exceptblocks,defaultblock):
        self.tryblock=tryblock
        self.exceptblocks=exceptblocks
        self.defaultblock=defaultblock
class Throw:
    def __init__(self,exception):
        self.exception=exception
class IncR:
    irsym=0
    def __init__(self,lvalue):
        self.lvalue=lvalue
class DecR:
    drsym=0
    def __init__(self,lvalue):
        self.lvalue=lvalue
class IncL:
    ilsym=0
    def __init__(self,lvalue):
        self.lvalue=lvalue
class DecL:
    dlsym=0
    def __init__(self,lvalue):
        self.lvalue=lvalue
#}
#语法分析器{
class Parser:
    def __init__(self,lexer):
        self.lexer=lexer
        self.tk=self.lexer.get()
        self.need_semicolon=True
    def eat(self,expect=None):
        if expect==None:
            tk=self.tk
            self.tk=self.lexer.get()
            return tk
        elif self.tk.tp==expect:
            tk=self.tk
            self.tk=self.lexer.get()
            return tk
        else:
            throw(ParserError(f"Unexpected token at line {self.lexer.line} row {self.lexer.row}:expect '{expect}',got '{self.tk.tp}'"))
    def eat_id(self,name):
        if self.tk.tp!=ID or self.tk.v!=name:
            throw(ParserError())
        self.tk=self.lexer.get()
    def match_id(self,name):
        return self.tk.tp==ID and self.tk.v==name
    def block(self):
        if self.tk.tp!=BEGIN:
            return Block([self.stmt()])
        else:
            self.eat()
            l=[While,If,For,Foreach,Switch,TryExcept]
            stmts=[]
            while self.tk.tp!=END:
                stmts.append(self.stmt())
                if type(stmts[-1]) not in l and self.need_semicolon==True:
                    self.eat(SEMICOLON)
                self.need_semicolon=True
            self.eat(END)
            return Block(stmts)
    def stmt(self):
        if self.tk.tp==SEMICOLON:
            return NoOp()
        if self.match_id("var"):
            self.eat()
            name=[self.eat(ID).v]
            value=[]
            if self.tk.tp==ASSIGN:
                self.eat()
                value.append(self.expr())
            else:
                value.append(None)
            while self.tk.tp==COMMA:
                self.eat()
                name.append(self.eat(ID).v)
                if self.tk.tp==ASSIGN:
                    self.eat()
                    value.append(self.expr())
                else:
                    value.append(None)
            return VarDecl(name,value)
        if self.match_id("while"):
            self.eat()
            self.eat(LPAREN)
            cond=self.parse_tuple(self.expr)
            self.eat(RPAREN)
            return While(cond,self.block())
        if self.match_id("if"):
            self.eat()
            self.eat(LPAREN)
            cond=self.parse_tuple(self.expr)
            self.eat(RPAREN)
            true=self.block()
            if self.match_id("else"):
                self.eat()
                return If(cond,true,self.block())
            return If(cond,true,NoOp())
        if self.match_id("return"):
            self.eat()
            rv=self.parse_tuple(self.expr)
            return Return(rv)
        if self.match_id("break"):
            self.eat()
            return Break()
        if self.match_id("continue"):
            self.eat()
            return Continue()
        if self.match_id("func"):
            self.eat()
            name=self.eat(ID).v
            ret=self.parse_lambda()
            self.need_semicolon=False
            return VarDecl([name],[ret])
        if self.match_id("class"):
            self.eat()
            name=self.eat(ID).v
            ret=self.parse_class()
            self.need_semicolon=False
            return VarDecl([name],[ret])
        if self.match_id("module"):
            self.eat()
            name=self.eat(ID).v
            ret=NewModule(self.block())
            self.need_semicolon=False
            return VarDecl([name],[ret])
        if self.match_id("import"):
            self.eat()
            return Import(self.expr())
        if self.match_id("for"):
            self.eat()
            self.eat(LPAREN)
            begin=self.stmt()
            self.eat(SEMICOLON)
            cond=self.parse_tuple(self.expr)
            self.eat(SEMICOLON)
            end=self.stmt()
            self.eat(RPAREN)
            return For(begin,cond,end,self.block())
        if self.match_id("foreach"):
            self.eat()
            self.eat(LPAREN)
            var=[self.eat(ID).v]
            while self.tk.tp==COMMA:
                self.eat()
                var.append(self.eat(ID).v)
            self.eat(COLON)
            base=self.parse_tuple(self.expr)
            self.eat(RPAREN)
            return Foreach(var,base,self.block())
        if self.match_id("switch"):
            self.eat()
            self.eat(LPAREN)
            base=self.expr()
            self.eat(RPAREN)
            self.eat(BEGIN)
            cases=[]
            bodys=[]
            while self.match_id("case"):
                self.eat()
                cases.append(self.expr())
                bodys.append(self.block())
            default=NoOp()
            if self.match_id("default"):
                self.eat()
                default=self.block()
            self.eat(END)
            return Switch(base,cases,bodys,default)
        if self.match_id("try"):
            self.eat()
            tryblock=self.block()
            exceptblocks=[]
            while self.match_id("except"):
                self.eat()
                exceptblocks.append([self.expr(),self.block()])
            defaultblock=NoOp()
            if self.match_id("default"):
                self.eat()
                defaultblock=self.block()
            return TryExcept(tryblock,exceptblocks,defaultblock)
        if self.match_id("throw"):
            self.eat();
            return Throw(self.expr())
        else:
            e=self.parse_tuple(self.expr)
            if self.tk.tp==ASSIGN:
                self.eat()
                x=self.parse_tuple(self.expr)
                if type(e)!=Tuple:
                    e=Tuple([e])
                    x=Tuple([x])
                return Assign(e,x)
            return e
    def parse_tuple(self,low):
        if self.tk.tp in (RPAREN,):
            return Tuple([])
        base=low()
        if self.tk.tp!=COMMA:
            return base
        else:
            self.eat()
            if self.tk.tp in (END,RSB,RPAREN,ASSIGN,SEMICOLON):
                return Tuple([base])
            base=[base,low()]
            while self.tk.tp==COMMA:
                self.eat()
                base.append(low())
            return Tuple(base)
    def expr_help(self,lower,op):
        res=lower()
        while self.tk.tp in op:
            op=self.eat().tp
            res=BinOp(op,res,lower())
        return res
    expr=lambda self:self.expr_help(self.expr1,[AND,OR])
    expr1=lambda self:self.expr_help(self.expr2,[BAND,BOR,XOR])
    expr2=lambda self:self.expr_help(self.expr3,[EQ,NE,GT,LT,GE,LE])
    expr3=lambda self:self.expr_help(self.expr4,[LSHIFT,RSHIFT])
    expr4=lambda self:self.expr_help(self.term,[ADD,SUB])
    term=lambda self:self.expr_help(self.factor,[MUL,DIV,MOD])
    def factor(self):
        if self.match_id("object"):
            self.eat()
            self.eat(BEGIN)
            attr={}
            while self.tk.tp!=END:
                k=self.eat(ID).v
                self.eat(COLON)
                v=self.parse_tuple(self.expr)
                attr[k]=v
                if self.tk.tp==COMMA:
                    self.eat()
            self.eat(END)
            return self.fh(NewObject(attr))
        if self.match_id("lambda"):
            self.eat()
            return self.fh(self.parse_lambda())
        if self.match_id("anonymous_class"):
            self.eat()
            return self.fh(self.parse_class())
        if self.match_id("anonymous_module"):
            self.eat()
            return self.fh(NewModule(self.block()))
        if self.tk.tp==LPAREN:
            self.eat()
            e=self.parse_tuple(self.expr)
            self.eat(RPAREN)
            return self.fh(e)
        if self.tk.tp==CONST:
            return self.fh(self.eat().v)
        if self.tk.tp==ID:
            res=Var(self.eat().v)
            return self.fh(res)
        if self.tk.tp==LSB:
            self.eat()
            l=[]
            if self.tk.tp!=RSB:
                l=[self.expr()]
                while self.tk.tp==COMMA:
                    self.eat()
                    l.append(self.expr())
            self.eat(RSB)
            return self.fh(List(l))
        if self.tk.tp in (ADD,SUB,NOT,INV):
            op=self.eat().tp
            return UnaryOp(op,self.fh(self.factor()))
        if self.tk.tp==BAND:
            self.eat()
            return Reference(self.factor())
        if self.tk.tp==MUL:
            self.eat()
            return DeReference(self.factor())
        if self.tk.tp==INC:
            self.eat()
            return IncL(self.factor())
        if self.tk.tp==DEC:
            self.eat()
            return DecL(self.factor())
        throw(ParserError(f"Unexpected token:'{self.tk.tp}'"))
    def parse_lambda(self):
        para=[]
        paravalue=[]
        self.eat(LPAREN)
        if self.tk.tp!=RPAREN:
            para=[self.eat(ID).v]
            if self.tk.tp==ASSIGN:
                self.eat()
                paravalue.append(self.expr())
            else:
                paravalue.append(NoInitValue())
            while self.tk.tp==COMMA:
                self.eat()
                para.append(self.eat(ID).v)
                if self.tk.tp==ASSIGN:
                    self.eat()
                    paravalue.append(self.expr())
                else:
                    paravalue.append(NoInitValue())
        self.eat(RPAREN)
        return FunctionInit(para,paravalue,self.block())
    def parse_class(self):
        parents=[]
        if self.tk.tp==COLON:
            self.eat()
            parents=[self.expr()]
            while self.tk.tp==COMMA:
                self.eat()
                parents.append(self.expr())
        self.eat_id("cons")
        cons=self.parse_lambda()
        block=self.block()
        return NewType(parents,cons,block)
    def fh(self,v):
        if self.tk.tp==LPAREN:
            self.eat()
            args=[]
            if self.tk.tp!=RPAREN:
                args=[self.expr()]
                while self.tk.tp==COMMA:
                    self.eat()
                    args.append(self.expr())
            self.eat(RPAREN)
            return self.fh(CallFunc(v,args))
        if self.tk.tp==LSB:
            self.eat()
            r=self.expr()
            self.eat(RSB)
            return self.fh(ElementOp(v,r))
        if self.tk.tp==DOT:
            self.eat()
            return self.fh(DOTOp(v,self.eat(ID).v))
        if self.tk.tp==DCOLON:
            self.eat()
            return self.fh(DCOLONOp(v,self.eat(ID).v))
        if self.tk.tp==INC:
            self.eat()
            return IncR(v)
        if self.tk.tp==DEC:
            self.eat()
            return DecR(v)
        return v
#}
#作用域{
class Scope:
    def __init__(self,parent=None,var={}):
        self.parent=parent
        self.var=var
    def define(self,v,n):
        self.var[v]=n
    def find(self,name):
        if name=="this":
            return this_stack.top()
        if name in self.var:
            return self.var[name]
        if self.parent!=None:
            return self.parent.find(name)
        throw(InterpreterError(f"Undefined variable '{name}'"))
    def set(self,name,value):
        if name=="this":
            this_stack.l[-1]=value
            return
        if name in self.var:
            self.var[name]=value
            return
        if self.parent!=None:
            self.parent.set(name,value)
            return
        throw(InterpreterError(f"Undefined variable '{name}'"))
    def buildin(self,s):
        for k,v in s.items():
            self.var[k]=v
#}
#解释器{
binop={
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
    BAND:lambda a,b:a&b,
    BOR:lambda a,b:a|b,
    XOR:lambda a,b:a^b,
}
unaryop={
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
    def __init__(self,tree,scope=Scope(None)):
        class T:
            def f():
                pass
        self.basic_object=T()
        self.tree=tree
        self.scope=scope
    def visit_BinOp(self,node):
        l=self.visit(node.l)
        r=self.visit(node.r)
        if type(l)==IObject or type(r)==IObject:
            if "__"+node.op+"__" in l.attr.keys():
                return self.visit_CallFunc(CallFunc(IMemberFunction(l,l.attr["__"+node.op+"__"]),[r]))
            if "__r"+node.op+"__" in r.attr.keys():
                return self.visit_CallFunc(CallFunc(IMemberFunction(r,r.attr["__r"+node.op+"__"]),[l]))
            throw(InterpreterError(f"Can't find operator '{node.op}'"))
        return binop[node.op](l,r)
    def visit_UnaryOp(self,node):
        e=self.visit(node.e)
        return unaryop[node.op](e)
    def visit_List(self,node):
        return [self.visit(i) for i in node.l]
    def visit_Block(self,node,tp=1):
        if tp:
            self.scope=Scope(self.scope)
            self.scope.define("__scope__",self.scope)
        for i in node.stmts:
            v=self.visit(i)
            if type(v) in (Return,Break,Throw,Continue):
                if tp:
                    self.scope=self.scope.parent
                return v
        if tp:
            self.scope=self.scope.parent
    def visit_VarDecl(self,node):
        name=node.name
        value=node.value
        value=[self.visit(i) for i in value]
        self.scope.buildin(dict(zip(name,value)))
    def visit_If(self,node):
        if self.visit(node.cond):
            return self.visit(node.true)
        else:
            return self.visit(node.false)
    def visit_While(self,node):
        while self.visit(node.cond):
            v=self.visit(node.block)
            if type(v) in (Return,Throw):
                return v
            if type(v)==Break:
                break
    def visit_ElementOp(self,node):
        return self.visit(node.l)[self.visit(node.r)]
    def visit_DOTOp(self,node):
        l=self.visit(node.l)
        if type(l) in (IObject,IType,IModule) and node.r=="append_attr":
            return l.append_attr
        if type(l) in (IObject,IType,IModule) and node.r=="get_attr":
            return l.get_attr
        if type(l)!=IObject:
            if type(l)==str and node.r=="split":
                return l.split
            if type(l)==list and node.r=="append":
                return l.append
            if type(l)==Scope and node.r=="find":
                return l.find
            if type(l)==Scope and node.r=="set":
                return l.set
        res=l.attr[node.r]
        if type(res)==IFunction:
            return IMemberFunction(l,res)
        return res
    def visit_DCOLONOp(self,node):
        l=self.visit(node.l)
        return l.attr[node.r]
    def visit_CallFunc(self,node):
        func=self.visit(node.func)
        if type(func)==type(lambda:0) or type(func)==type(print) or type(func)==type(self.basic_object.f):
            args=[self.visit(i) for i in node.args]
            return func(*args)
        if type(func)==IFunction:
            self_scope=self.scope
            self.scope=Scope(func.closure,self.complete_args(func.para,func.paravalue,node.args))
            ret=self.visit_Block(func.code,0)
            self.scope=self_scope
            if ret!=None:
                return ret.retvalue
            return None
        if type(func)==IMemberFunction:
            obj=func.obj
            this_stack.push(func.obj)
            func=func.func
            self_scope=self.scope
            self.scope=Scope(func.closure)
            self.scope.var=self.complete_args(func.para,func.paravalue,node.args)
            ret=self.visit_Block(func.code,0)
            self.scope=self_scope
            this_stack.pop()
            if ret!=None:
                return ret.retvalue
            return None
        if type(func)==IType:
            tp=func
            func=func.cons
            self_scope=self.scope
            self.scope=Scope(func.closure)
            self.scope.var=self.complete_args(func.para,func.paravalue,node.args)
            this_stack.push(IObject(tp,self.get_all_attrs(tp)))
            self.visit_Block(func.code,0)
            self.scope=self_scope
            return this_stack.pop()
        throw(InterpreterError("Can't call an object or value in this type"))
    def visit_NewType(self,node):
        parents=[self.visit(i) for i in node.parents]
        cons=self.visit(node.cons)
        body=node.block
        self.scope=Scope(self.scope)
        self.scope.define("__scope__",self.scope)
        self.visit_Block(body,0)
        res=IType(parents,cons,self.scope.var)
        self.scope=self.scope.parent
        return res
    def visit_NewModule(self,node):
        body=node.body
        self.scope=Scope(self.scope)
        self.scope.define("__scope__",self.scope)
        self.visit_Block(body,0)
        res=IModule(self.scope.var)
        self.scope=self.scope.parent
        return res
    def get_all_attrs(self,tp):
        res={}
        for p in tp.parents:
            parent=self.get_all_attrs(p)
            for k,v in parent:
                res[k]=v
        for k,v in tp.attr.items():
            res[k]=v
        return res
    def visit_Var(self,node):
        if node.name=="this":
            return this_stack.top()
        return self.scope.find(node.name)
    def assign(self,lvalue,target):
        '''lvalue=self.deep_recursive(lvalue)
        _lvalue=lvalue
        target=self.visit(target)
        def w(xlvalue,target,base):
            if type(xlvalue)==Var:
                return target
            #base=self.visit(xlvalue)
            if type(xlvalue)==ElementOp:
                base[xlvalue.r]=w(xlvalue.l,target,base[xlvalue.r])
                return base
            if type(xlvalue)==DOTOp:
                base.attr[xlvalue.r]=w(xlvalue.l,target,base.attr[xlvalue.r])
                return base
            if type(xlvalue)==DCOLONOp:
                base.attr[xlvalue.r]=w(xlvalue.l,target,base.attr[xlvalue.r])
                return base
            throw(InterpreterError())
        while type(lvalue)!=Var:
            lvalue=lvalue.l
        self.scope.set(lvalue.name,w(_lvalue,target,self.visit(lvalue)))'''
        base,indexs,indextypes=self.prepare(lvalue)
        base_value=self.scope.find(base)
        target=self.visit(target)
        def w(base_value,indextypes,indexs,target):
            if len(indexs)==0:
                return target
            index=indexs[0]
            indexs=indexs[1:]
            indextype=indextypes[0]
            indextypes=indextypes[1:]
            if indextype==IndexType.ELEMENT:
                idx=self.visit(index)
                base_value[idx]=w(base_value[idx],indextypes,indexs,target)
                return base_value
            if indextype==IndexType.OBJ_ATTR:
                idx=index
                base_value.attr[idx]=w(base_value.attr[idx],indextypes,indexs,target)
                return base_value
            if indextype==IndexType.TYPE_ATTR:
                idx=index
                base_value.attr[idx]=w(base_value.attr[idx],indextypes,indexs,target)
                return base_value
        base_name=base
        self.scope.set(base_name,w(base_value,indextypes,indexs,target))
    def visit_Assign(self,node):
        target=self.visit(node.target)
        target=self.iterable_to_list(target)
        for i in range(len(node.base.l)):
            self.assign(node.base.l[i],target[i])
    def visit_Import(self,node):
        self.scope.buildin(self.visit(node.module).attr)
    def visit_NewObject(self,node):
        names=node.attr.keys()
        values=[self.visit(i) for i in node.attr.values()]
        return IObject(IType([],None,dict(zip(names,[None for i in range(len(names))]))),dict(zip(names,values)))
    def visit_For(self,node):
        self.scope=Scope(self.scope)
        self.visit(node.begin)
        while self.visit(node.cond):
            v=self.visit(node.body)
            if type(v) in (Return,Throw):
                self.scope=self.scope.parent
                return v
            if type(v)==Break:
                break
            self.visit(node.end)
        self.scope=self.scope.parent
    def visit_Foreach(self,node):
        base=self.visit(node.base)
        if type(base) in (list,str,tuple):
            for i in base:
                j=i
                if len(node.var)==1:
                    j=[j]
                self.scope=Scope(self.scope,dict(zip(node.var,self.iterable_to_list(j))))
                v=self.visit_Block(node.body,0)
                self.scope=self.scope.parent
                if type(v) in (Return,Throw):
                    return v
                if type(v)==Break:
                    break
        else:
            _iter=self.visit_CallFunc(CallFunc(base.get_attr("__iter__"),[]))
            _next=_iter.get_attr("__next__")
            i=self.visit_CallFunc(CallFunc(_next,[]))
            while type(i)!=IObject or "error_name" not in i.attr.keys() or i.attr["error_name"]!="IterationError":
                if len(node.var)==1:
                    i=[i]
                self.scope=Scope(self.scope,dict(zip(node.var,self.iterable_to_list(i))))
                v=self.visit_Block(node.body,0)
                self.scope=self.scope.parent
                if type(v) in (Return,Throw):
                    return v
                if type(v)==Break:
                    break
                i=self.visit_CallFunc(CallFunc(_next,[]))
    def visit_Switch(self,node):
        base=self.visit(node.base)
        for i in range(len(node.cases)):
            if base==self.visit(node.cases[i]):
                return self.visit(node.bodys[i])
        return self.visit(node.default)
    def visit_IFunction(self,node):
        flag=0
        for i in range(len(node.paravalue)):
            if type(node.paravalue)!=NoInitValue:
                flag=1
            if flag==1 and type(node.paravalue)==NoInitValue:
                throw(InterpreterError())
        return node
    def visit_NoOp(self,node):
        return None
    def complete_args(self,para,paravalue,args):
        res=dict(zip(para,[self.visit(i) for i in paravalue]))
        for i in range(len(args)):
            res[para[i]]=self.visit(args[i])
        return res
    def iterable_to_list(self,iterable):
        if type(iterable) in (str,list,tuple):
            return list(iterable)
        _iter=self.visit_CallFunc(CallFunc(iterable.get_attr("__iter__"),[]))
        _next=_iter.get_attr("__next__")
        i=self.visit_CallFunc(CallFunc(_next,[]))
        res=[]
        while type(i)!=IObject or "error_name" not in i.attr.keys() or i.attr["error_name"]!="IterationError":
            res.append(i)
            i=self.visit_CallFunc(CallFunc(_next,[]))
        return res
    def visit_Reference(self,node):
        return IReference(node.base)
    def visit_DeReference(self,node):
        return self.visit(self.visit(node.base).base)
    def visit_FunctionInit(self,node):
        return IFunction(node.para,node.paravalue,node.code,self.scope)
    def deep_recursive(self,node):
        lvalue=copy.deepcopy(node)
        if type(lvalue) in (Reference,IReference):
            throw(InterpreterError())
        if type(lvalue)==DeReference:
            if type(self.visit(lvalue.base)) in (IReference,Reference):
                return self.deep_recursive(self.visit(lvalue.base).base)
            throw(InterpreterError())
        if type(lvalue)==DCOLONOp:
            return DCOLONOp(self.deep_recursive(lvalue.l),lvalue.r)
        if type(lvalue)==DOTOp:
            return DOTOp(self.deep_recursive(lvalue.l),lvalue.r)
        if type(lvalue)==ElementOp:
            return ElementOp(self.deep_recursive(lvalue.l),self.visit(lvalue.r))
        if type(lvalue)==Var:
            return lvalue
        if type(lvalue)==IncL:
            _lvalue=lvalue.lvalue
            self.assign(_lvalue,self.visit(_lvalue)+1)
            return _lvalue
        if type(lvalue)==DecL:
            _lvalue=lvalue.lvalue
            self.assign(_lvalue,self.visit(_lvalue)-1)
            return _lvalue
        throw(InterpreterError())
    def visit_TryExcept(self,node):
        v=self.visit(node.tryblock)
        if type(v)==Throw:
            exception=v.exception
            for i in node.exceptblocks:
                if self.visit(i[0])==exception.attr["error_name"]:
                    return self.visit(i[1])
            if type(node.defaultblock)==NoOp:
                return v
            else:
                return self.visit(node.defaultblock)
        return v
    def visit_Throw(self,node):
        return Throw(self.visit(node.exception))
    def visit_IncR(self,node):
        old=self.visit(node.lvalue)
        self.assign(node.lvalue,old+1)
        return old
    def visit_DecR(self,node):
        old=self.visit(node.lvalue)
        self.assign(node.lvalue,old-1)
        return old
    def visit_IncL(self,node):
        _lvalue=node.lvalue
        v=self.visit(_lvalue)
        self.assign(_lvalue,v+1)
        return v+1
    def visit_DecL(self,node):
        _lvalue=node.lvalue
        v=self.visit(_lvalue)
        self.assign(_lvalue,v-1)
        return v-1
    def prepare(self,lvalue):
        lvalue=self.deep_recursive(lvalue)
        indexs,indextypes=[],[]
        while type(lvalue)!=Var:
            if type(lvalue)==ElementOp:
                indextypes=[IndexType.ELEMENT]+indextypes
                indexs=[lvalue.r]+indexs
                lvalue=lvalue.l
            if type(lvalue)==DOTOp:
                indextypes=[IndexType.OBJ_ATTR]+indextypes
                indexs=[lvalue.r]+indexs
                lvalue=lvalue.l
            if type(lvalue)==DCOLONOp:
                indextypes=[IndexType.TYPE_ATTR]+indextypes
                indexs=[lvalue.r]+indexs
                lvalue=lvalue.l
        return lvalue.name,indexs,indextypes
    visit_int=visit_float=visit_str=visit_list=visit_bool=visit_NoneType=visit_IType=visit_IModule=visit_IObject=visit_NoInitValue=visit_IMemberFunction=lambda self,a:a
    visit_Return=lambda self,node:Return(self.visit(node.retvalue))
    visit_Break=visit_Continue=lambda self,a:a
    visit_Tuple=lambda self,node:tuple(self.visit(i) for i in node.l)
    def interprete(self):
        self.scope.define("__scope__",self.scope)
        v=self.visit(self.tree)
        if type(v)==Throw:
            throw(v.exception)
#}
#内置函数{
Main=Scope(None,{
    "builtin_modules":IModule({
        "Range":NewModule(Parser(Lexer('''
{
    class _Range
    cons(begin,end,step=1){
        this.begin,this.end,this.step=begin,end,step;
    }
    {
        var begin,end,step;
        func have(value){
            return (value-this.begin)%this.step==0&&this.begin<=value&&this.end>value;
        }
        func tolist(){
            var res=[];
            for(var i=this.begin;i<this.end;i=i+this.step) res.append(i);
            return res;
        }
    }
    class RangeIter
    cons(begin,end,skip=1){
        this.begin,this.end,this.skip=begin,end,skip;
        this.now=begin;
    }
    {
        var begin,end,skip,now;
        func __iter__(){
            return this;
        }
        func __next__(){
            if(this.now>=this.end) return object{
                error_name:"IterationError"
                error_message:""
            };
            this.now=this.now+this.skip;
            return this.now-1;
        }
    }
    class Range
    cons(begin,end,skip=1){
        this.begin,this.end,this.skip=begin,end,skip;
    }
    {
        var begin,end,skip;
        func __iter__(){
            var ret=RangeIter(this.begin,this.end,this.skip);
            return ret;
        }
    }
}
''')).block()),
        "Printer":NewModule(Parser(Lexer('''
{
    func better_print(__s){
        for(var __i=0;__i<len(__s);++__i){
            if(__s[__i]=="$"){
                if(__i==len(__s)-1) throw object{
                    error_name:"PrinterError"
                    error_message:"Unexpected end of string"
                };
                if(__s[__i+1]=="$"){
                    ++++__i;
                    print("$");
                }
                else{
                    ++__i;
                    var __varname="";
                    while(__s[__i]!="$") __varname=__varname+__s[__i++];
                    print(__scope__.find(__varname));
                }
            }
            else{
                print(__s[__i]);
            }
        }
    }
}
''')).block()),
        "Random":NewModule(Parser(Lexer('''
{
    func power(base,index){
        var res = 1;
        for(var i =1;i<=index;i=i+1){
            res = res * base;
        }
        return res;
    };
    class Rand
    cons(seed){
        this.rand = seed;
        this.a,this.c,this.m = 1140671485,128201163,power(2,24);
    }
    {
        var rand,a,c,m;
        func random(){
            this.rand = (this.a * this.rand + this.c) % this.m;
            return this.rand / this.m;
        };
    };
}
''')).block()),
        "Struct":NewModule(Parser(Lexer('''
{
    // 栈
    class Stack
    cons(){
        this.members = [];
    }
    {
        var members;
        func push(value){
            this.members = this.members + [value];
        };
        func pop(){
            var value = this.members[0];
            var result = [];
            for(var i = 1;i <= len(this.members) - 1;i++){
                result = result + [this.members[i]];
            };
            this.members = result;
            return value;
        };
        func top(){
            return this.members[0];
        };
    };
    
    // 数组
    class ArrayIter
    cons(members){
        this.members = members;
        this.pos = 0;
    }
    {
        var members,pos;
        func __iter__(){
            return this;
        };
        func __next__(){
            if (this.pos < len(this.members)){
                var value = this.members[this.pos];
                this.pos = this.pos + 1;
                return value;
            }
            else{
                return object{
                    error_name:"IterationError"
                    error_message:""
                };
            };
        };
    };
    class Array
    cons(members){
        this.members = members;
        this.pos = 0;
    }
    {
        var members,pos;
        func __iter__(){
            return ArrayIter(this.members);
        };
        
        func append(value){
            this.members = this.members + [value];
        };
        func remove(value){
            var res = [];
            var mem = this.members;
            var removed = false;
            for(var i = 0;i < len(mem);i++){
                if (mem[i] != value){
                        res = res + [mem[i]];
                }else if (removed){
                    res = res + [mem[i]];
                }else{
                    removed = true;
                }
            };
            this.members = res;
        };
        func extend(value){
            var res = this.members;
            foreach(i:value){
                res = res + [i];
            };
            this.members = res;
        };
        func insert(value,position){
            var res = [];
            for(var i = 0;i<position-1;i++){
                res = res + [this.members[i]];
            };
            res = res + [value];
            for(var i = 0;i<=len(this.members)-position;i++){
                res = res + [this.members[(position +  i) - 1]];
            };
            this.members = res;
        };
        func count(value){
            var num = 0;
            foreach(i:this.members){
                if(i == value){
                    num++;
                };
            };
            return num;
        };
        func index(value){
            for(var i = 0;i<len(this.members);i++){
                if (this.members[i] == value){
                    return i;
                };
            };
            throw object{
                error_name:"ValueError"
                error_message:"value not found"
            };
        };
        func get(index){
            return this.members[index];
        };
    };
    
    // Map结构
    class Map
    cons(){
        this.keys = Array([]);
        this.values = Array([]);
    }
    {
        var keys,values;
        func set(index,to){
            this.keys.append(index);
            this.values.append(to);
        };
        func lookup(index){
            return this.values.get(this.keys.index(index));
        };
        func __iter__(){
            return this.keys;
        };
    }
}
''')).block()),
        "Freestyle":NewModule(Parser(Lexer('''
{
    
}
''')).block())
    }),
    "println":lambda *l:print(*l,sep=""),
    "print":lambda *l:print(*l,sep="",end=""),
    "inputln":lambda *l:input(*l),
    "ord":lambda *l:ord(*l),
    "chr":lambda *l:chr(*l),
    "len":lambda *l:len(*l),
    "substr":lambda base,begin=None,end=None,skip=None:base[begin:end:skip],
    "type":lambda l:l.tp,
    "help":lambda:print('''
integer3.2.0说明文档
1、类型
    内置类型：
        int
        float
        string
        bool
        null_t（直接用了python的NoneType）
        list
        type
        module
        object
        func
        tuple（新）
        reference（新）（仅仅初步实现）（Rust风格）
1.5、内置方法
    <list>.append
    <string>.split
    <object/type/module>.append_attr/get_attr
2、变量
    用var关键字定义变量
    var name[=value]...;
    赋值
    a=value;
    a[0]=value;
    a.a=value;
    a::a=value;
    赋值语法糖
    a,b,c,d,...=一个列表或元组；
    还可以
    a,b=b,a;
    来交换两个数
3、函数、类和模块
    函数
        lambda(<parameters>){<body>}
        定义匿名函数
        允许缺省参数
        已经支持闭包
    类
        anonymous_class[:<parents>]cons(<parameters>){<body>}{<members>}
        定义“匿名类型”
        name(<arguments>)
        调用name类的构造函数初始化name类的实例
        name::name
        获得属性的值
    模块
        anonymous_module{<members>}
        定义“匿名模块”
        import name
        导入“匿名模块”
        name::name
        获得属性的值
        name.name
        获得对象属性的值
    语法糖
        func name(<parameters>){<body>}
        class name[:<parents>]cons(<parameters>){<body>}{<members>}
        module name{members}
        object{name1:value1[,]name2:value2...}不定义类直接创建对象
        type(<object>)获取object的类型，一定要保证object是自定义类型的实例，哪怕是直接创建的对象也行
        通过name.append_attr(<name>,<value>)动态为类/模块/对象添加属性，name应为字符串
        通过name.get_attr(<name>)获得类/模块/对象的属性的值，name应为字符串
3.5、迭代器
    迭代器类型要有__iter__和__next__方法
    可迭代类型要有__iter__方法
    没有内置的迭代器类型
    也没有yield语句
    所以__iter__应该返回一个自定义的迭代器对象
    迭代器类型的__next__应该有终止条件
    终止应返回
    object{
        "error_name":"IterationError"
        "error_message":""
    }
4、基本结构
    <body>部分如果只有一条语句可以不加大括号，但不建议，有bug
    分支
        if(<condition>){<body>}[else{<body>}]
    switch分支
        switch(value){
            case case1{
                ...
            }
            case case2{
                ...
            }
            ...
            default{
                ...
            }
        }
        不能写break
        而且可以自动break
    while循环
        while(<condition>){<body>}
    for循环
        for(<variable declaration>;<condition>;<assign statement>){<body>}
    foreach循环
        foreach(i,j...:value){<body>}
4.5、异常处理
    try-except-default
        暂不能捕获内置错误（InterpreterError）
        try{
            ...
        }
        except <error type>{//error type应为字符串
            ...
        }
        ...
        default{
            ...
        }
    throw
        throw ...;
        ...应为一个对象
        应有error_name和error_message属性
5、内置函数
    print/println
    inputln
    ord
    chr
    len
    substr
    type
    help
6、内置模块
    用import builtin_modules::name;引入内置模块
    如果只导入一个属性
    应写var attrname=builtin_modules::modulename::attrname;
    Range模块
        这是一个用integer3.2实现的类
        它证明我的迭代器是适合使用的
        也证明integer3.2是适合使用的
        定义了_Range类
            初始化：_Range(begin,end[,step])
            tolist将_Range对象转为列表
            例如_Range(0,3).tolist()得到[0,1,2]
            have(value)判断_Range对象的范围中有没有value
            例如_Range(0,3).have(3)得到false
        定义了Range类
            内容很少，只有一个__iter__方法用于foreach遍历
            初始化同_Range类
            这是一个可迭代类型
            遍历所占内存比_Range类型小得多
        为Range类实现了RangeIter类
            它是一个迭代器类型
            不建议单独使用
差不多就这么多
最后附上我用它写的Brainfuck解释器源码
{
    var Getchar=
    anonymous_class
    cons(){
        this.line="";
    }
    {
        var line="";
        var get=lambda(){
            if(len(this.line)==0) this.line=inputln()+"\\n";
            var ch=this.line[0];
            this.line=substr(this.line,1);
            return ch;
        };
    };
    var get=Getchar();
    var code=inputln("这是一个用integer3.1.0写的Brainfuck解释器\\nBrainfuck>>>");
    var i=0;
    var mem=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
    var pos=8;
    while(i<len(code)){
        var c=code[i];
        if(c=="+") mem[pos]=mem[pos]+1;
        if(c=="-") mem[pos]=mem[pos]-1;
        if(c==">") pos=pos+1;
        if(c=="<") pos=pos-1;
        if(c==".") print(chr(mem[pos]));
        if(c==",") mem[pos]=ord(get.get());
        if(c=="["){
            if(mem[pos]==0){
                var l=1,r=0;
                i=i+1;
                while(i<len(code)){
                    if(code[i]=="[") l=l+1;
                    if(code[i]=="]"){
                        r=r+1;
                        if(l!=0){
                            r=r-1;
                            l=l-1;
                        }
                    }
                    if(l==0&&r==0) break;
                    i=i+1;
                }
            }
        }
        if(c=="]"){
            var l=0,r=1;
            i=i-1;
            while(i>=0){
                if(code[i]=="]") r=r+1;
                if(code[i]=="["){
                    l=l+1;
                    if(r!=0){
                        r=r-1;
                        l=l-1;
                    }
                }
                if(l==0&&r==0) break;
                i=i-1;
            }
            i=i-1;
        }
        i=i+1;
    }
}
'''),
    "changelog":lambda:print('''
integer3.0.0
    integer3第一个版本
    开创了很多功能
    在当时的C站python区领先
    至今在python区似乎也只有我自己的作品比它强
integer3.0.1
    相当于宣布integer3复活
    只加了getchar和以main函数作为入口
    后来全部取消
integer3.1.0
    完全的重写+重构
    焕然一新
    代码也好看多了
integer3.1.1
    object语法糖
integer3.1.2
    for和foreach
integer3.1.3
    switch
integer3.1.4
    函数的缺省参数
integer3.1.5
    append_attr和get_attr内置方法
integer3.1.6
    变量解构初步
integer3.1.7
    运算符重载
integer3.1.8
    Range类1.0版
integer3.2.0
    大更
    代码没有堆成屎
    1、迭代器、yield（重点）（已降级实现）
    2、变量的解构（重点）（已实现）
    3、函数的闭包（已实现）
    4、封装（未实现）
    5、异常处理（重点）（已初步实现）
    6、元组（已实现）
    7、引用（重点）（已实现）
    8、Range类2.0版（用迭代器重写）
integer3.2.1
    ++ --运算符（前置后置都有）
'''),
})
#}
Main.var["builtin_modules"].attr["Range"]=Interpreter(None,Main).visit(Main.var["builtin_modules"].attr["Range"])
Main.var["builtin_modules"].attr["Printer"]=Interpreter(None,Main).visit(Main.var["builtin_modules"].attr["Printer"])
Main.var["builtin_modules"].attr["Random"]=Interpreter(None,Main).visit(Main.var["builtin_modules"].attr["Random"])
Main.var["builtin_modules"].attr["Struct"]=Interpreter(None,Main).visit(Main.var["builtin_modules"].attr["Struct"])
Interpreter(Parser(Lexer('''
{
    
}
''')).block(),Main).interprete()
'''
{
    var T=
    anonymous_class
    cons(a){
        this.a=a;
    }
    {
        var a=0;
        var change=lambda(a){
            this.a=a;
        };
        var print=lambda(){
            println(this.a);
        };
    };
    var a=T(10);
    a.print();
    a.change(20);
    a.print();
}

{
    var Parent=
    anonymous_class
    cons(){
        
    }
    {
        var a=20;
    };
    
    var Child=
    anonymous_class:Parent
    cons(){
        
    }
    {
        var b=10;
    };
    Child::a=0;
    println(Child::a);
}

{
    var Getchar=
    anonymous_class
    cons(){
        this.line="";
    }
    {
        var line="";
        var get=lambda(){
            if(len(this.line)==0) this.line=inputln()+"\\n";
            var ch=this.line[0];
            this.line=substr(this.line,1);
            return ch;
        };
    };
    var get=Getchar();
    print(get.get()+get.get());
}

{
    var M=
    anonymous_module{
        var pi=3.14;
    };
    println(M::pi);
}

{
    func f(){
        return 1,2;
    }
    var a,b;
    a,b=f();
    println(a," ",b);
}

{
    var obj=object{
        a:10
    };
    var obj_ref=&obj;
    println((*obj_ref).a," ",obj.a);
    (*obj_ref).a=20;
    println((*obj_ref).a," ",obj.a);
}

{
    var a=[1,2,[3,4,6]];
    var ref=&a[2][2];
    *ref=5;
    println(a);
}

{
    var obj=object{
        a:10
        print:lambda(){
            println(this.a);
        }
    };
    var ref=&obj.a;
    obj.print();
    *ref=20;
    obj.print();
}

{
    func Counter(start){
        return lambda(){
            start=start+1;
            return start;
        };
    }
    var c=Counter(10);
    for(var i=0;i<10;i=i+1) println(c());
}

{
    var Range=builtin_modules::Range::Range;
    foreach(i:Range(0,10)) println(i);
}

{
    var a=[1,3,3];
    --a[1];
    println(a);
    for(var i=0;i++<10;0) println(i);
}
'''