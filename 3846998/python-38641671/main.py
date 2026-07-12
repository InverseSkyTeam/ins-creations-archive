#常量定义{
ADD,SUB,MUL,DIV,MOD="ADD,SUB,MUL,DIV,MOD".split(",")
EQ,NE,GT,LT,GE,LE="EQ,NE,GT,LT,GE,LE".split(",")
LSHIFT,RSHIFT="LSHIFT,RSHIFT".split(",")
AND,OR="AND,OR".split(",")
BAND,BOR,XOR="BAND,BOR,XOR".split(",")
NOT,INV="NOT,INV".split(",")
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
    def __init__(self,para,paravalue,code):
        self.para=para
        self.paravalue=paravalue
        self.code=code
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
        return self.attr[name]
class IModule:
    def __init__(self,attr):
        self.attr=attr
    def append_attr(self,name,value):
        self.attr[name]=value
    def get_attr(self,name):
        return self.attr[name]
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
class LValue:
    def __init__(self,base,indextypes,indexs):
        self.base=base
        self.indextypes=indextypes
        self.indexs=indexs
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
            l=[While,If,For,Foreach,Switch]
            stmts=[]
            while self.tk.tp!=END:
                stmts.append(self.stmt())
                if type(stmts[-1]) not in l and self.need_semicolon==True:
                    self.eat(SEMICOLON)
                self.need_semicolon=True
            self.eat(END)
            return Block(stmts)
    def stmt(self):
        lexer=Lexer(str(self.lexer.text),self.lexer.p)
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
            cond=self.expr()
            self.eat(RPAREN)
            return While(cond,self.block())
        if self.match_id("if"):
            self.eat()
            self.eat(LPAREN)
            cond=self.expr()
            self.eat(RPAREN)
            true=self.block()
            if self.match_id("else"):
                self.eat()
                return If(cond,true,self.block())
            return If(cond,true,NoOp())
        if self.match_id("return"):
            self.eat()
            rv=self.expr()
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
            cond=self.expr()
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
            base=self.expr()
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
        else:
            tk=self.tk
            isassign=False
            while self.tk.tp!=SEMICOLON:
                self.eat()
                if self.tk.tp==ASSIGN:
                    isassign=True
            self.lexer=lexer
            self.tk=tk
            if isassign:
                base=[self.parse_lvalue()]
                while self.tk.tp==COMMA:
                    self.eat()
                    base.append(self.parse_lvalue())
                self.eat(ASSIGN)
                target=[self.expr()]
                while self.tk.tp==COMMA:
                    self.eat()
                    target.append(self.expr())
                return Assign(base,target)
            else:
                return self.expr()
    def parse_lvalue(self):
        base=self.eat(ID).v
        indextypes=[]
        indexs=[]
        while self.tk.tp in (DOT,DCOLON,LSB):
            if self.tk.tp==DOT:
                self.eat()
                indextypes.append(IndexType.OBJ_ATTR)
                indexs.append(self.eat(ID).v)
            elif self.tk.tp==DCOLON:
                self.eat()
                indextypes.append(IndexType.TYPE_ATTR)
                indexs.append(self.eat(ID).v)
            elif self.tk.tp==LSB:
                self.eat()
                indextypes.append(IndexType.ELEMENT)
                indexs.append(self.expr())
                self.eat(RSB)
        return LValue(base,indextypes,indexs)
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
                v=self.expr()
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
            e=self.expr()
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
        return IFunction(para,paravalue,self.block())
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
        return binop[node.op](l,r)
    def visit_UnaryOp(self,node):
        e=self.visit(node.e)
        return unaryop[node.op](e)
    def visit_List(self,node):
        return [self.visit(i) for i in node.l]
    def visit_Block(self,node,tp=1):
        if tp:
            self.scope=Scope(self.scope)
        for i in node.stmts:
            v=self.visit(i)
            if v!=None:
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
            if type(v)==Return:
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
            self.scope=Scope(self.scope,self.complete_args(func.para,func.paravalue,node.args))
            ret=self.visit_Block(func.code,0)
            self.scope=self.scope.parent
            if ret!=None:
                return ret.retvalue
            return None
        if type(func)==IMemberFunction:
            obj=func.obj
            this_stack.push(func.obj)
            func=func.func
            self.scope=Scope(self.scope)
            self.scope.var=self.complete_args(func.para,func.paravalue,node.args)
            ret=self.visit_Block(func.code,0)
            self.scope=self.scope.parent
            this_stack.pop()
            if ret!=None:
                return ret.retvalue
            return None
        if type(func)==IType:
            this_stack.push(IObject(func,self.get_all_attrs(func)))
            func=func.cons
            self.scope=Scope(self.scope)
            self.scope.var=self.complete_args(func.para,func.paravalue,node.args)
            self.visit_Block(func.code,0)
            self.scope=self.scope.parent
            return this_stack.pop()
        throw(InterpreterError("Can't call an object or value in this type"))
    def visit_NewType(self,node):
        parents=[self.visit(i) for i in node.parents]
        cons=node.cons
        body=node.block
        self.scope=Scope(self.scope)
        self.visit_Block(body,0)
        res=IType(parents,cons,self.scope.var)
        self.scope=self.scope.parent
        return res
    def visit_NewModule(self,node):
        body=node.body
        self.scope=Scope(self.scope)
        self.visit_Block(body,0)
        res=IModule(self.scope.var)
        self.scope=self.scope.parent
        return res
    def get_all_attrs(self,tp):
        res={}
        for p in tp.parents:
            parent=get_all_attrs(p)
            for k,v in parent:
                res[k]=v
        for k,v in tp.attr.items():
            res[k]=v
        return res
    def visit_Var(self,node):
        if node.name=="this":
            return this_stack.top()
        return self.scope.find(node.name)
    def assign(self,node):
        lvalue=node.base
        base_value=self.scope.find(lvalue.base)
        target=self.visit(node.target)
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
        base_name=lvalue.base
        if base_name=="this":
            this_stack.l[-1]=w(base_value,lvalue.indextypes,lvalue.indexs,target)
            return
        self.scope.set(base_name,w(base_value,lvalue.indextypes,lvalue.indexs,target))
    def visit_Assign(self,node):
        target=[self.visit(i) for i in node.target]
        for i in range(len(node.base)):
            self.assign(Assign(node.base[i],target[i]))
    def islvalue(self,node):
        if type(node)==Var:
            return True
        elif type(node) in (ElementOp,DOTOp,DCOLONOp):
            return islvalue(node.l)
        else:
            return False
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
            if type(v)==Return:
                self.scope=self.scope.parent
                return v
            if type(v)==Break:
                break
            self.visit(node.end)
        self.scope=self.scope.parent
    def visit_Foreach(self,node):
        base=self.visit(node.base)
        for i in base:
            j=i
            if type(j)!=list:
                j=[j]
            self.scope=Scope(self.scope,dict(zip(node.var,j)))
            v=self.visit_Block(node.body,0)
            self.scope=self.scope.parent
            if type(v)==Return:
                return v
            if type(v)==Break:
                break
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
    visit_int=visit_float=visit_str=visit_list=visit_bool=visit_NoneType=visit_IType=visit_IModule=visit_IObject=visit_NoInitValue=lambda self,a:a
    visit_Return=lambda self,node:Return(self.visit(node.retvalue))
    visit_Break=visit_Continue=lambda self,a:a
    def interprete(self):
        self.visit(self.tree)
#}
#内置函数{
Main=Scope(None,{
    "println":lambda *l:print(*l,sep=""),
    "print":lambda *l:print(*l,sep="",end=""),
    "inputln":lambda *l:input(*l),
    "ord":lambda *l:ord(*l),
    "chr":lambda *l:chr(*l),
    "len":lambda *l:len(*l),
    "substr":lambda base,begin=None,end=None,skip=None:base[begin:end:skip],
    "type":lambda l:l.tp,
    "help":lambda:print('''
integer3.1.2说明文档
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
2、变量
    用var关键字定义变量
    var name[=value]...;
    赋值
    a=value;
    a[0]=value;
    a.a=value;
    a::a=value;
    赋值语法糖
    a,b,c,d,...=v1,v2,v3,v4...；
    还可以
    a,b=b,a；
    来交换两个数
3、函数、类和模块
    函数
        lambda(<parameters>){<body>}
        定义匿名函数
        允许缺省参数
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
5、内置函数
    print/println
    inputln
    ord
    chr
    len
    substr
    type
    help
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
})
#}
Interpreter(Parser(Lexer('''
{
    var a=10,b=20;
    println(a,b);
    a,b=b,a;
    println(a,b);
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
'''