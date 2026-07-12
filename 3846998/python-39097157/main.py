import copy,sys,os
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
GETCHAR,READLN,LEN,CHR,ORD="GETCHAR,READLN,LEN,CHR,ORD".split(",")
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
    def __init__(self,tp:str,v):
        self.tp=tp
        self.v=v
    def __str__(self):
        return f"Token({self.tp},{self.v})"
#}
#错误定义{
class LexerError:
    lesym=0
    def __init__(self,msg:str="None"):
        self.msg=msg
class ParserError:
    pesym=0
    def __init__(self,msg:str="None"):
        self.msg=msg
class InterpreterError:
    iesym=0
    def __init__(self,msg:str="None"):
        self.msg=msg
class CheckerError:
    cesym=0
    def __init__(self,msg:str="None"):
        self.msg=msg
def throw(error):
    '''if type(error)==IObject:
        print(f"{error.attr['error_name']}:{error.attr['error_message']}")
        exit(-1)'''
    print(f"{type(error).__name__}:{error.msg}.")
    exit(-1)
#}
#词法分析器{
class Lexer:
    def __init__(self,text:str,p:int=0,line:int=1,row:int=1):
        self.text=text
        self.p=p
        self.ch=self.text[self.p]
        self.line=line
        self.row=row
    def nc(self,n:int=1):
        self.p+=n
        self.row+=n
        if self.p>=len(self.text):
            self.ch=""
        else:
            self.ch=self.text[self.p]
    def peek(self,n:int=1)->str:
        return self.text[self.p:self.p+n]
    def char(self)->str:
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
    def get(self)->Token:
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
            if res in ("getchar","readln","len","ord","chr"):
                if self.ch!='!':
                    throw(LexerError())
                self.nc()
                return Token(res.upper(),None)
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
#类型系统{
class BasicType:
    def __init__(self,typename:str):
        self.typename=typename
class ArrayType:
    def __init__(self,base):
        self.base=base
class TemplateType:
    def __init__(self,tname:str,targs:list):
        self.tname,self.targs=tname,targs
def type_eq(t1,t2)->bool:
    if id(t1)==id(t2):
        return True
    if type(t1)!=type(t2):
        return False
    if type(t1)==BasicType:
        return t1.typename==t2.typename
    if type(t1)==ArrayType:
        return type_eq(t1.base,t2.base)
    if type(t1)==TemplateType:
        if t1.tname!=t2.tname or len(t1.targs)!=len(t2.targs):
            return False
        for i in range(len(t1.targs)):
            if not type_eq(t1.targs[i],t2.targs[i]):
                return False
        return True
    raise
def typeof(obj):
    if type(obj)==LiteralArray:
        return ArrayType(obj.tp)
    else:
        if type(obj)==int:
            return BasicType("int")
        if type(obj)==bool:
            return BasicType("bool")
        if type(obj)==float:
            return BasicType("float")
        if type(obj)==str:
            return BasicType("string")
        if type(obj)==type(None):
            return BasicType("null_t")
        throw(CheckerError())
def new(tp):
    if type(tp)==ArrayType:
        return LiteralArray([],tp.base)
    if type(tp)==TemplateType and tp.tname=="function":
        return None
    return {
        "int":0,
        "float":0.0,
        "string":"",
        "null_t":None,
        "bool":False,
    }[tp.typename]
class LiteralArray:
    def __init__(self,l,tp):
        self.l=l
        self.tp=tp
    __repr__=__str__=lambda self:"{"+",".join([str(i) for i in self.l])+"}"
class Function:
    def __init__(self,para,paratype,body,closure):
        self.para,self.paratype,self.body,self.closure=para,paratype,body,closure
#}
#AST定义{
class NoOp:
    pass
class Var:
    def __init__(self,name:str):
        self.name=name
class BinOp:
    def __init__(self,op:str,l,r):
        self.op,self.l,self.r=op,l,r
class UnaryOp:
    def __init__(self,op:str,v):
        self.op,self.v=op,v
class VarDecl:
    def __init__(self,names:list,types:list,values:list):
        self.names,self.types,self.values=names,types,values
class If:
    def __init__(self,cond,true,false):
        self.cond,self.true,self.false=cond,true,false
class While:
    def __init__(self,cond,body):
        self.cond,self.body=cond,body
class Block:
    def __init__(self,children:list):
        self.children=children
class Print:
    def __init__(self,things,sep,end,flush):
        self.things,self.sep,self.end,self.flush=things,sep,end,flush
class Assign:
    def __init__(self,lvalue,target):
        self.lvalue,self.target=lvalue,target
class ElementOp:
    eosym=0
    def __init__(self,l,r):
        self.l,self.r=l,r
class NewList:
    def __init__(self,tp,value):
        self.tp,self.value=tp,value
class MacroGetchar:
    mgsym=0
class MacroReadln:
    mrsym=0
class MacroLen:
    mlsym=0
    def __init__(self,arg):
        self.arg=arg
class MacroChr:
    mcsym=0
    def __init__(self,arg):
        self.arg=arg
class MacroOrd:
    mosym=0
    def __init__(self,arg):
        self.arg=arg
class FuncDecl:
    def __init__(self,name,para,paratype,body,rettype):
        self.name,self.para,self.paratype,self.body,self.rettype=name,para,paratype,body,rettype
class CallFunc:
    def __init__(self,func,args):
        self.func,self.args=func,args
class Break:
    bsym=0
class Continue:
    csym=0
class Return:
    def __init__(self,retvalue):
        self.retvalue=retvalue
#}
#语法分析器{
class Parser:
    def __init__(self,lexer:Lexer):
        self.lexer=lexer
        self.tk=self.lexer.get()
    def eat(self,tp=None):
        if tp==None or self.tk.tp==tp:
            tk=self.tk
            self.tk=self.lexer.get()
            return tk
        else:
            throw(ParserError(f"Unexpected token at line {self.lexer.line} row {self.lexer.row}:expect '{tp}',got '{self.tk.tp}'"))
    def match_id(self,name:str):
        return self.tk.tp==ID and self.tk.v==name
    def eat_id(self,name:str):
        if self.tk.tp==ID and self.tk.v==name:
            self.tk=self.lexer.get()
        else:
            throw(InterpreterError())
    def block(self):
        if self.tk.tp!=BEGIN:
            res=Block([self.stmt()])
            if self.tk.tp==SEMICOLON:
                self.eat()
            return res
        else:
            self.eat(BEGIN)
            stmts=[]
            while self.tk.tp!=END:
                stmts.append(self.stmt())
                if type(stmts[-1]) not in (If,While,FuncDecl):
                    self.eat(SEMICOLON)
            self.eat(END)
            return Block(stmts)
    def stmt(self):
        if self.tk.tp==SEMICOLON:
            return NoOp()
        if self.match_id("var"):
            self.eat()
            names=[self.eat(ID).v]
            self.eat(COLON)
            types=[self.parse_type()]
            values=[]
            if self.tk.tp==ASSIGN:
                self.eat()
                values.append(self.expr())
            else:
                values.append(new(types[-1]))
            while self.tk.tp==COMMA:
                self.eat()
                names.append(self.eat(ID).v)
                self.eat(COLON)
                types.append(self.parse_type())
                if self.tk.tp==ASSIGN:
                    self.eat()
                    values.append(self.expr())
                else:
                    values.append(new(types[-1]))
            return VarDecl(names,types,values)
        if self.match_id("print"):
            self.eat()
            sep,end,flush=" ","\n",False
            if self.tk.tp==LSB:
                self.eat()
                if self.tk.tp!=RSB:
                    name=self.eat(ID).v
                    self.eat(ASSIGN)
                    value=self.expr()
                    if name=="sep":
                        sep=value
                    if name=="end":
                        end=value
                    if name=="flush":
                        flush=value
                    while self.tk.tp==COMMA:
                        self.eat()
                        name=self.eat(ID).v
                        self.eat(ASSIGN)
                        value=self.expr()
                        if name=="sep":
                            sep=value
                        if name=="end":
                            end=value
                        if name=="flush":
                            flush=value
                self.eat(RSB)
            things=[self.xexpr()]
            while self.tk.tp==COMMA:
                self.eat()
                things.append(self.xexpr())
            return Print(things,sep,end,flush)
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
        if self.match_id("while"):
            self.eat()
            self.eat(LPAREN)
            cond=self.expr()
            self.eat(RPAREN)
            return While(cond,self.block())
        if self.match_id("func"):
            self.eat()
            name=self.eat().v
            para=[]
            paratype=[]
            self.eat(LPAREN)
            if self.tk.tp!=RPAREN:
                para=[self.eat(ID).v]
                self.eat(COLON)
                paratype=[self.parse_type()]
                while self.tk.tp==COMMA:
                    self.eat()
                    para.append(self.eat(ID).v)
                    self.eat(COLON)
                    paratype.append(self.parse_type())
            self.eat(RPAREN)
            self.eat(COLON)
            rettype=self.parse_type()
            return FuncDecl(name,para,paratype,self.block(),rettype)
        if self.match_id("break"):
            self.eat()
            return Break()
        if self.match_id("continue"):
            self.eat()
            return Continue()
        if self.match_id("return"):
            self.eat()
            return Return(self.xexpr())
        else:
            return self.xexpr()
    def _parse_type(self,base):
        if self.tk.tp==LSB:
            self.eat()
            self.eat(RSB)
            return self._parse_type(ArrayType(base))
        if self.tk.tp==LT:
            self.eat()
            targs=[]
            if self.tk.tp!=GT:
                targs=[self.parse_type()]
                while self.tk.tp==COMMA:
                    self.eat()
                    targs.append(self.parse_type())
            self.eat(GT)
            return TemplateType(base.typename,targs)
        return base
    def parse_type(self):
        return self._parse_type(BasicType(self.eat(ID).v))
    def xexpr(self):
        res=self.expr()
        if self.tk.tp==ASSIGN:
            self.eat()
            res=Assign(res,self.xexpr())
        return res
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
        if self.match_id("array"):
            self.eat()
            self.eat(COLON)
            tp=self.parse_type()
            self.eat(BEGIN)
            l=[]
            if self.tk.tp!=END:
                l=[self.xexpr()]
                while self.tk.tp==COMMA:
                    self.eat()
                    l.append(self.xexpr())
            self.eat(END)
            return self.fh(NewList(tp,l))
        if self.tk.tp==CONST:
            return self.fh(self.eat().v)
        if self.tk.tp==ID:
            return self.fh(Var(self.eat(ID).v))
        if self.tk.tp==LPAREN:
            self.eat()
            e=self.xexpr()
            self.eat(RPAREN)
            return self.fh(e)
        if self.tk.tp in (ADD,SUB,NOT,INV):
            return UnaryOp(self.eat().tp,self.fh(self.factor()))
        if self.tk.tp in (GETCHAR,READLN):
            tp=self.eat().tp
            self.eat(LPAREN)
            self.eat(RPAREN)
            return {
                GETCHAR:MacroGetchar,
                READLN:MacroReadln,
            }[tp]()
        if self.tk.tp in (LEN,CHR,ORD):
            tp=self.eat().tp
            self.eat(LPAREN)
            arg=self.expr()
            self.eat(RPAREN)
            return {
                LEN:MacroLen,
                CHR:MacroChr,
                ORD:MacroOrd,
            }[tp](arg)
    def fh(self,v):
        if self.tk.tp==LSB:
            self.eat()
            r=self.xexpr()
            self.eat(RSB)
            return self.fh(ElementOp(v,r))
        if self.tk.tp==LPAREN:
            self.eat()
            args=[]
            if self.tk.tp!=RPAREN:
                args=[self.xexpr()]
                while self.tk.tp==COMMA:
                    self.eat()
                    args.append(self.xexpr())
            self.eat(RPAREN)
            return self.fh(CallFunc(v,args))
        return v
#}
#类型作用域{
class TypeScope:
    def __init__(self,var:dict={}):
        self.stack=[var]
    def new(self,var:dict={}):
        self.stack.append(var)
    def delete(self):
        self.stack.pop()
    def find(self,name:str):
        for i in reversed(self.stack):
            if name in i:
                return i[name]
        throw(CheckerError("Undefined identifier"))
    def buildin(self,var:dict):
        for k,v in var.items():
            self.stack[-1][k]=v
#}
#下标类型{
class IndexType:
    ELEMENT=0
    OBJ_ATTR=1
    TYPE_ATTR=2
#}
#值作用域{
class Scope:
    def __init__(self,var:dict={}):
        self.stack=[var]
    def new(self,var:dict={}):
        self.stack.append(var)
    def delete(self):
        self.stack.pop()
    def find(self,name:str):
        for i in reversed(self.stack):
            if name in i:
                return i[name]
        throw(CheckerError("Undefined identifier"))
    def set(self,name:str,value):
        for i in reversed(self.stack):
            if name in i:
                i[name]=value
                return
        throw(CheckerError("Undefined identifier"))
    def buildin(self,var:dict):
        for k,v in var.items():
            self.stack[-1][k]=v
#}
#语义分析器{
class Checker:
    def visit(self,node):
        method_name="visit_"+type(node).__name__
        visitor=getattr(self,method_name,self.generic_visit)
        return visitor(node)
    def generic_visit(self,node):
        raise Exception("Can't find method\"visit_{}()\"".format(type(node).__name__))
    def __init__(self,tree,scope:TypeScope=TypeScope()):
        self.tree=tree
        self.scope=scope
        self.rettype=BasicType("Shit")
    visit_int=lambda self,node:BasicType("int")
    visit_float=lambda self,node:BasicType("float")
    visit_bool=lambda self,node:BasicType("bool")
    visit_str=lambda self,node:BasicType("string")
    visit_NoneType=lambda self,node:BasicType("null_t")
    visit_LiteralArray=lambda self,node:ArrayType(node.tp)
    visit_Function=lambda self,node:TemplateType("function",[node.rettype]+node.paratype)
    def visit_BinOp(self,node:BinOp):
        l,r=self.visit(node.l),self.visit(node.r)
        op=node.op
        if op in (EQ,NE,GT,LT,GE,LE,AND,OR):
            return BasicType("bool")
        if type(l)==ArrayType or type(r)==ArrayType:
            if not type_eq(l,r):
                throw(CheckerError())
            return l
        if type_eq(l,r):
            return l
        if l.typename=="null_t":
            throw(CheckerError())
        if op==MUL and "string" in (l.typename,r.typename):
            return BasicType("string")
        if not type_eq(l,r) and l.typename!="float" and r.typename!="float":
            return BasicType("int")
        return BasicType("float")
    def visit_UnaryOp(self,node:UnaryOp):
        v=self.visit(node.v)
        op=node.op
        if op==NOT:
            return BasicType("bool")
        return v
    def visit_VarDecl(self,node:VarDecl):
        for i in range(len(node.types)):
            if not type_eq(node.types[i],self.visit(node.values[i])):
                throw(CheckerError())
        self.scope.buildin(dict(zip(node.names,node.types)))
    def visit_Var(self,node:Var):
        return self.scope.find(node.name)
    def visit_Block(self,node:Block):
        for i in node.children:
            self.visit(i)
    def visit_Print(self,node:Print):
        for i in node.things:
            self.visit(i)
        self.visit(node.end)
        self.visit(node.flush)
        self.visit(node.sep)
    def visit_If(self,node:If):
        if not type_eq(BasicType("bool"),self.visit(node.cond)):
            throw(CheckerError())
        self.scope.new()
        self.visit(node.true)
        self.scope.delete()
        self.scope.new()
        self.visit(node.false)
        self.scope.delete()
    def visit_While(self,node:While):
        if not type_eq(BasicType("bool"),self.visit(node.cond)):
            throw(CheckerError())
        self.scope.new()
        self.visit(node.body)
        self.scope.delete()
    def visit_Assign(self,node:Assign):
        lvalue,target=node.lvalue,node.target
        base=self.visit(lvalue)
        target=self.visit(target)
        while type(lvalue) in (ElementOp,):
            if not type_eq(self.visit(lvalue.r),BasicType("int")):
                throw(CheckerError())
            lvalue=lvalue.l
        if type(lvalue)!=Var:
            throw(CheckerError())
        if not type_eq(base,target):
            throw(CheckerError())
        return target
    def visit_ElementOp(self,node:ElementOp):
        l,r=self.visit(node.l),self.visit(node.r)
        if not type_eq(BasicType("int"),r):
            throw(CheckerError())
        if type(l)!=ArrayType and (type(l)==BasicType and l.typename!="string"):
            throw(CheckerError())
        if type(l)==BasicType:
            return l
        return l.base
    def visit_NewList(self,node:ElementOp):
        tp=node.tp
        for i in node.value:
            if not type_eq(self.visit(i),tp):
                throw(CheckerError())
        return ArrayType(tp)
    visit_MacroReadln=visit_MacroGetchar=lambda self,node:BasicType("string")
    def visit_MacroLen(self,node:MacroLen):
        arg=self.visit(node.arg)
        if (type(arg)==BasicType and arg.typename=="string") or type(arg)==ArrayType:
            return BasicType("int")
        throw(CheckerError())
    def visit_MacroChr(self,node:MacroChr):
        arg=self.visit(node.arg)
        if type(arg)!=BasicType or arg.typename!="int":
            throw(CheckerError())
        return BasicType("string")
    def visit_MacroOrd(self,node:MacroOrd):
        arg=self.visit(node.arg)
        if type(arg)!=BasicType or arg.typename!="string":
            throw(CheckerError())
        return BasicType("int")
    def visit_FuncDecl(self,node:FuncDecl):
        self.scope.buildin({
            node.name:TemplateType("function",[node.rettype]+node.paratype),
        })
        self.scope.new()
        self.scope.buildin(dict(zip(node.para,node.paratype)))
        self_rettype=self.rettype
        self.rettype=node.rettype
        self.visit(node.body)
        self.rettype=self_rettype
        self.scope.delete()
    def visit_CallFunc(self,node:CallFunc):
        args=[self.visit(i) for i in node.args]
        func=self.visit(node.func)
        if type(func)!=TemplateType or func.tname!="function" or len(func.targs)-1!=len(args):
            throw(CheckerError())
        for i in range(len(args)):
            if not type_eq(args[i],func.targs[i+1]):
                throw(CheckerError())
        return func.targs[0]
    visit_NoOp=lambda self,node:None
    visit_Break=visit_Continue=lambda self,node:None
    def visit_Return(self,node:Return):
        if not type_eq(self.visit(node.retvalue),self.rettype):
            throw(CheckerError())
    def check(self):
        self.visit(self.tree)
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
    def __init__(self,tree,scope:Scope=Scope()):
        self.tree=tree
        self.scope=scope
    def visit_BinOp(self,node:BinOp):
        return binop[node.op](self.visit(node.l),self.visit(node.r))
    def visit_UnaryOp(self,node:UnaryOp):
        return unaryop[node.op](self.visit(node.v))
    visit_int=visit_str=visit_bool=visit_float=visit_NoneType=visit_LiteralArray=visit_Function=lambda self,node:node
    def visit_VarDecl(self,node:VarDecl):
        self.scope.buildin(dict(zip(node.names,[self.visit(i) for i in node.values])))
    def visit_Block(self,node:Block):
        for i in node.children:
            v=self.visit(i)
            if type(v) in (Break,Continue,Return):
                return v
    def visit_Print(self,node:Print):
        print(*[self.visit(i) for i in node.things],sep=self.visit(node.sep),end=self.visit(node.end),flush=self.visit(node.flush))
    def visit_Var(self,node:Var):
        return self.scope.find(node.name)
    def visit_If(self,node:If):
        if self.visit(node.cond):
            self.scope.new()
            res=self.visit(node.true)
            self.scope.delete()
            return res
        self.scope.new()
        res=self.visit(node.false)
        self.scope.delete()
        return res
    def visit_While(self,node:While):
        while self.visit(node.cond):
            self.scope.new()
            v=self.visit(node.body)
            self.scope.delete()
            if type(v)==Break:
                break
            if type(v)==Return:
                return v
    visit_NoOp=lambda self,node:None
    def assign(self,lvalue,target):
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
                base_value.l[idx]=w(base_value.l[idx],indextypes,indexs,target)
                return base_value
        base_name=base
        self.scope.set(base_name,w(base_value,indextypes,indexs,target))
    def visit_Assign(self,node:Assign):
        lvalue,target=node.lvalue,self.visit(node.target)
        self.assign(lvalue,target)
        return target
    def visit_ElementOp(self,node:ElementOp):
        l,r=self.visit(node.l),self.visit(node.r)
        if type(l)==str:
            return l[r]
        return l.l[r]
    def visit_NewList(self,node:NewList):
        return LiteralArray([self.visit(i) for i in node.value],node.tp)
    def prepare(self,lvalue):
        lvalue=lvalue
        indexs,indextypes=[],[]
        while type(lvalue)!=Var:
            if type(lvalue)==ElementOp:
                indextypes=[IndexType.ELEMENT]+indextypes
                indexs=[self.visit(lvalue.r)]+indexs
                lvalue=lvalue.l
        return lvalue.name,indexs,indextypes
    visit_MacroGetchar=lambda self,node:sys.stdin.read(1)
    visit_MacroReadln=lambda self,node:input()
    def visit_MacroLen(self,node:MacroLen):
        arg=self.visit(node.arg)
        if type(arg)==LiteralArray:
            return len(arg.l)
        return len(arg)
    def visit_FuncDecl(self,node:FuncDecl):
        self.scope.buildin({
            node.name:Function(node.para,node.paratype,node.body,self.scope)
        })
    def visit_CallFunc(self,node:CallFunc):
        func=self.visit(node.func)
        args=[self.visit(i) for i in node.args]
        self_scope=self.scope
        self.scope=func.closure
        self.scope.new()
        self.scope.buildin(dict(zip(func.para,args)))
        v=self.visit_Block(func.body)
        self.scope.delete()
        self.scope=self_scope
        return v.retvalue
    visit_MacroChr=lambda self,node:chr(self.visit(node.arg))
    visit_MacroOrd=lambda self,node:ord(self.visit(node.arg))
    visit_Break=visit_Continue=lambda self,node:node
    visit_Return=lambda self,node:Return(self.visit(node.retvalue))
    def interpreter(self):
        return self.visit(self.tree)
#}
code='''
{
    var mem:int[]=array:int{0,0,0,0,0,0,0,0,0,0},pos:int=5;
    var code:string=readln!();
    var i:int=0;
    while(i<len!(code)){
        var c:string;
        c=code[i];
        if(c=="+") mem[pos]=mem[pos]+1;
        if(c=="-") mem[pos]=mem[pos]-1;
        if(c==">") pos=pos+1;
        if(c=="<") pos=pos-1;
        if(c==".") print[end=""] chr!(mem[pos]);
        if(c==",") mem[pos]=ord!(getchar!());
        if(c=="["){
            if(mem[pos]==0){
                var l:int=1,r:int=0;
                i=i+1;
                while(i<len!(code)){
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
            var l:int=0,r:int=1;
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
'''
tree=Parser(Lexer(code)).block()
Checker(tree).check()
Interpreter(tree).interpreter()
'''
{
    var a:int;
    a=0;
    while(a<10){
        if(a%2==0){
            print a;
        }
        a=a+1;
    }
}

{
    var arr:int[];
    arr=array:int{10,20,20};
    arr[2]=30;
    print arr;
}

{
    var l:int[][];
    l=array:int[]{array:int{1,1}};
    print l;
    l[0][1]=2;
    print l;
}

{
    print[end=""] len!("123456");
}

{
    var a:int;
    while(true){
        if(a==10) break;
        a=a+1;
        if(a==5) continue;
        print a;
    }
    print "break";
}

{
    func f(v:string):int{
        print v;
        return len!(v);
    }
    print f("Hello!");
}

{
    func f():function<int,int>{
        func ret(a:int):int{
            return a+1;
        }
        return ret;
    }
    var ret:function<int,int>;
    ret=f();
    print ret(10);
}

{
    func Counter(start:int):function<int>{
        func inc():int{
            start=start+1;
            return start;
        }
        return inc;
    }
    var counter:function<int>;
    counter=Counter(1);
    var i:int;
    while(i<10){
        print counter();
        i=i+1;
    }
}

{
    var a:int=10,b:int=20;
    print a+b;
}
'''