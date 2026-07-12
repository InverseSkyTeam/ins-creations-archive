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
    '^':INV,
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
class XLexer:#众所周知，只要提供了这些接口就可以
    def __init__(self,lexer:Lexer):
        self.tk=[lexer.get()]
        self.p=0
        while self.tk[-1].tp!=EOF:
            self.tk.append(lexer.get())
    def get(self):
        self.p+=1
        return self.tk[self.p-1]
    def back(self,n=1):
        self.p-=n
#}
#类型系统{
class BasicType:
    def __init__(self,typename:str):
        self.typename=typename
class ArrayType:
    def __init__(self,base):
        self.base=base
class FunctionType:
    def __init__(self,rettype,paratype:list):
        self.rettype,self.paratype=rettype,paratype
class BuiltinFunctionType:
    def __init__(self,rettype):
        self.rettype=rettype
def type_eq(t1,t2)->bool:
    if id(t1)==id(t2):
        return True
    if type(t1)!=type(t2):
        return False
    if type(t1)==BasicType:
        return t1.typename==t2.typename
    if type(t1)==ArrayType:
        return type_eq(t1.base,t2.base)
    if type(t1)==FunctionType:
        if not type_eq(t1.rettype,t2.rettype):
            return False
        for i in range(len(t1.paratype)):
            if not type_eq(t1.paratype[i],t2.paratype[i]):
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
    if type(tp)==FunctionType:
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
    __repr__=__str__=lambda self:"["+",".join([str(i) for i in self.l])+"]"
class Function:
    def __init__(self,para,rettype,paratype,body,closure):
        self.para,self.rettype,self.paratype,self.body,self.closure=para,rettype,paratype,body,closure
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
    def __init__(self,conds,cases,default):
        self.conds,self.cases,self.default=conds,cases,default
class While:
    def __init__(self,cond,body):
        self.cond,self.body=cond,body
class Block:
    def __init__(self,children:list):
        self.children=children
class Print:
    def __init__(self,thing,sep,end,flush):
        self.thing,self.sep,self.end,self.flush=thing,sep,end,flush
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
class Lambda:
    def __init__(self,para,paratype,body,rettype):
        self.para,self.paratype,self.body,self.rettype=para,paratype,body,rettype
class NewArray:
    def __init__(self,l:list):
        self.l=l
class NullArray:
    def __init__(self,tp):
        self.tp=tp
#}
class Parser:
    def __init__(self,lexer:Lexer):
        self.lexer=XLexer(lexer)
        self.tk=self.lexer.get()
    def eat(self,tp=None):
        if tp==None or self.tk.tp==tp:
            tk=self.tk
            self.tk=self.lexer.get()
            return tk
        else:
            throw(ParserError(f"Unexpected token:expect '{tp}',got '{self.tk.tp}'"))
    def match_id(self,name:str):
        return self.tk.tp==ID and self.tk.v==name
    def eat_id(self,name:str):
        if self.tk.tp==ID and self.tk.v==name:
            self.tk=self.lexer.get()
        else:
            throw(ParserError(f"Unexpected identifier:expect '{name}',got '{self.tk.v}'"))
    def block(self):
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
            types=[None]
            if self.tk.tp==COLON:
                self.eat(COLON)
                types=[self.parse_type()]
            values=[]
            if self.tk.tp==ASSIGN:
                self.eat()
                values.append(self.expr())
            else:
                if types[-1]==None:
                    throw(ParserError())
                else:
                    values.append(new(types[-1]))
            while self.tk.tp==COMMA:
                self.eat()
                names.append(self.eat(ID).v)
                if self.tk.tp==COLON:
                    self.eat(COLON)
                    types.append(self.parse_type())
                else:
                    types.append(None)
                if self.tk.tp==ASSIGN:
                    self.eat()
                    values.append(self.expr())
                else:
                    if types[-1]==None:
                        throw(ParserError())
                    else:
                        values.append(new(types[-1]))
            return VarDecl(names,types,values)
        if self.match_id("if"):
            self.eat()
            self.eat(LPAREN)
            conds=[self.expr()]
            self.eat(RPAREN)
            blocks=[self.block()]
            have_default=1
            default=NoOp()
            while self.match_id("else"):
                self.eat()
                if not self.match_id("if"):
                    break
                self.eat(LPAREN)
                conds.append(self.expr())
                self.eat(RPAREN)
                blocks.append(self.block())
            else:
                have_default=0
            if have_default:
                default=self.block()
            return If(conds,blocks,default)
        if self.match_id("while"):
            self.eat()
            self.eat(LPAREN)
            cond=self.expr()
            self.eat(RPAREN)
            return While(cond,self.block())
        if self.match_id("func"):
            self.eat()
            if self.tk.tp==LPAREN:
                self.lexer.back()
                return self.expr()
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
            return Return(self.expr())
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
            things=[self.expr()]
            while self.tk.tp==COMMA:
                self.eat()
                things.append(self.expr())
            return Print(things,sep,end,flush)
        else:
            return self.expr()
    def _parse_type(self,v):
        if self.tk.tp==LSB:
            self.eat()
            self.eat(RSB)
            return self._parse_type(ArrayType(v))
        return v
    def parse_type(self):
        if self.match_id("function"):
            self.eat()
            self.eat(LT)
            targs=[]
            if self.tk.tp!=GT:
                targs=[self.parse_type()]
                while self.tk.tp==COMMA:
                    self.eat()
                    targs.append(self.parse_type())
            self.eat(GT)
            return self._parse_type(FunctionType(targs[0],targs[1:]))
        return self._parse_type(BasicType(self.eat(ID).v))
    def expr(self):
        res=self.expr0()
        if self.tk.tp==ASSIGN:
            self.eat()
            res=Assign(res,self.expr0())
        return res
    def expr_help(self,lower,op):
        res=lower()
        while self.tk.tp in op:
            op=self.eat().tp
            res=BinOp(op,res,lower())
        return res
    expr0=lambda self:self.expr_help(self.expr1,[AND,OR])
    expr1=lambda self:self.expr_help(self.expr2,[BAND,BOR,XOR])
    expr2=lambda self:self.expr_help(self.expr3,[EQ,NE,GT,LT,GE,LE])
    expr3=lambda self:self.expr_help(self.expr4,[LSHIFT,RSHIFT])
    expr4=lambda self:self.expr_help(self.term,[ADD,SUB])
    term=lambda self:self.expr_help(self.factor,[MUL,DIV,MOD])
    def factor(self):
        if self.match_id("nullarray"):
            self.eat()
            self.eat(COLON)
            return NullArray(self.parse_type())
        if self.tk.tp==LSB:
            self.eat()
            l=[self.expr()]
            while self.tk.tp==COMMA:
                self.eat()
                l.append(self.expr())
            self.eat(RSB)
            return NewArray(l)
        if self.match_id("func"):
            self.eat()
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
            return self.fh(Lambda(para,paratype,self.block(),rettype))
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
    def fh(self,v):
        if self.tk.tp==LSB:
            self.eat()
            r=self.expr()
            self.eat(RSB)
            return self.fh(ElementOp(v,r))
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
        return v
#下标类型{
class IndexType:
    ELEMENT=0
    OBJ_ATTR=1
    TYPE_ATTR=2
#}
#作用域{
class Scope:
    def __init__(self):
        self.stack:list=[{}]
    def define(self,name:str,value):
        self.stack[-1][name]=value
    def new(self):
        self.stack.append({})
    def delete(self):
        self.stack.pop()
    def find(self,name:str):
        for i in self.stack:
            if name in i:
                return i[name]
        throw(CheckerError(f"未定义的变量'{name}'"))
    def set(self,name:str,value):
        for i in self.stack:
            if name in i:
                i[name]=value
                return
        throw(CheckerError(f"未定义的变量'{name}'"))
    def buildin(self,var:dict):
        for k,v in var.items():
            self.stack[-1][k]=v
#}
#访问者{
class NodeVisitor:
    def visit(self,node):
        method_name="visit_"+type(node).__name__
        visitor=getattr(self,method_name,self.generic_visit)
        return visitor(node)
    def generic_visit(self,node):
        raise Exception("Can't find method\"visit_{}()\"".format(type(node).__name__))
#}
#语义分析器{
class Checker(NodeVisitor):
    def __init__(self,tree,scope:Scope=Scope()):
        self.tree=tree
        self.scope:Scope=scope
        self.rettype=BasicType("Shit")
    def visit_Block(self,node:Block):
        self.scope.new()
        for i in node.children:
            self.visit(i)
        self.scope.delete()
    def visit_BinOp(self,node:BinOp):
        l,r=self.visit(node.l),self.visit(node.r)
        op=node.op
        if op in (EQ,NE,GT,LT,GE,LE,AND,OR):
            return BasicType("bool")
        if type(l)==ArrayType or type(r)==ArrayType:
            if not type_eq(l,r):
                throw(CheckerError("运算错误"))
            return l
        if type_eq(l,r):
            return l
        if l.typename=="null_t":
            throw(CheckerError("运算错误"))
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
            if node.types[i]==None:
                node.types[i]=self.visit(node.values[i])
            elif not type_eq(node.types[i],self.visit(node.values[i])):
                throw(CheckerError("（变量定义）变量的值和类型不匹配"))
        self.scope.buildin(dict(zip(node.names,node.types)))
    def visit_Var(self,node:Var):
        return self.scope.find(node.name)
    def visit_NewArray(self,node:NewArray):
        tp=self.visit(node.l[0])
        for i in node.l[1:]:
            if not type_eq(tp,self.visit(i)):
                throw(CheckerError())
        return ArrayType(tp)
    def visit_Block(self,node:Block):
        for i in node.children:
            self.visit(i)
    def visit_While(self,node:While):
        if not type_eq(BasicType("bool"),self.visit(node.cond)):
            throw(CheckerError("while循环要求条件是布尔值"))
        self.scope.new()
        self.visit(node.body)
        self.scope.delete()
    def visit_If(self,node:If):
        for i in node.conds:
            if not type_eq(BasicType("bool"),self.visit(i)):
                throw(CheckerError("if语句要求条件是布尔值"))
        for i in node.cases:
            self.scope.new()
            self.visit(i)
            self.scope.delete()
        self.scope.new()
        self.visit(node.default)
        self.scope.delete()
    def visit_Assign(self,node:Assign):
        lvalue,target=node.lvalue,node.target
        base=self.visit(lvalue)
        target=self.visit(target)
        while type(lvalue) in (ElementOp,):
            if not type_eq(self.visit(lvalue.r),BasicType("int")):
                throw(CheckerError("索引必须是数字"))
            lvalue=lvalue.l
        if type(lvalue)!=Var:
            throw(CheckerError("（变量赋值）左边不是左值"))
        if not type_eq(base,target):
            throw(CheckerError("（变量赋值）变量的值和类型不匹配"))
        return target
    def visit_ElementOp(self,node:ElementOp):
        l,r=self.visit(node.l),self.visit(node.r)
        if not type_eq(BasicType("int"),r):
            throw(CheckerError("索引必须是数字"))
        if type(l)!=ArrayType and not type_eq(l,BasicType("string")):
            throw(CheckerError("只能对数组或字符串用下标取值"))
        if type(l)!=BasicType:
            return l.base
        return BasicType("string")
    def visit_FuncDecl(self,node:FuncDecl):
        self.scope.buildin({
            node.name:FunctionType(node.rettype,node.paratype),
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
        func:FunctionType=self.visit(node.func)
        if type(func)==FunctionType:
            if len(func.paratype)!=len(args):
                throw(CheckerError())
            for i in range(len(args)):
                if not type_eq(args[i],func.paratype[i]):
                    throw(CheckerError())
            return func.rettype
        elif type(func)==BuiltinFunctionType:
            return func.rettype
        else:
            throw(CheckerError())
    visit_NoOp=lambda self,node:None
    visit_Break=visit_Continue=lambda self,node:None
    def visit_Return(self,node:Return):
        if not type_eq(self.visit(node.retvalue),self.rettype):
            throw(CheckerError())
    def visit_Print(self,node:Print):
        for i in node.thing:
            self.visit(i)
        self.visit(node.end)
        self.visit(node.flush)
        self.visit(node.sep)
    def visit_Lambda(self,node:Lambda):
        self.scope.new()
        self.scope.buildin(dict(zip(node.para,node.paratype)))
        self_rettype=self.rettype
        self.rettype=node.rettype
        self.visit(node.body)
        self.rettype=self_rettype
        self.scope.delete()
        return FunctionType(node.rettype,node.paratype)
    def visit_NullArray(self,node:NullArray):
        return ArrayType(node.tp)
    visit_int=lambda self,node:BasicType("int")
    visit_float=lambda self,node:BasicType("float")
    visit_bool=lambda self,node:BasicType("bool")
    visit_str=lambda self,node:BasicType("string")
    visit_NoneType=lambda self,node:BasicType("null_t")
    visit_LiteralArray=lambda self,node:ArrayType(node.tp)
    visit_Function=lambda self,node:FunctionType(node.rettype,node.paratype)
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
    def visit_If(self,node:If):
        for i in range(len(node.conds)):
            if self.visit(node.conds[i]):
                return self.visit(node.cases[i])
        return self.visit(node.default)
    def visit_BinOp(self,node:BinOp):
        l,r=self.visit(node.l),self.visit(node.r)
        if type(l)==type(r)==LiteralArray:
            return LiteralArray(l.l+r.l,l.tp)
        return binop[node.op](l,r)
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
    def visit_Var(self,node:Var):
        return self.scope.find(node.name)
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
    def visit_FuncDecl(self,node:FuncDecl):
        self.scope.buildin({
            node.name:Function(node.para,node.rettype,node.paratype,node.body,copy.deepcopy(self.scope))
        })
    def visit_CallFunc(self,node:CallFunc):
        func:Function=self.visit(node.func)
        if type(func)==Function:
            args=[self.visit(i) for i in node.args]
            self_scope=self.scope
            self.scope:Scope=func.closure
            self.scope.new()
            self.scope.buildin(dict(zip(func.para,args)))
            v:Return=self.visit_Block(func.body)
            self.scope.delete()
            self.scope=self_scope
            return v.retvalue
        elif type(func)==type(lambda:1):
            args=[self.visit(i) for i in node.args]
            return func(*args)
    def visit_Lambda(self,node:Lambda):
        return Function(node.para,node.rettype,node.paratype,node.body,self.scope)
    def visit_NewArray(self,node:NewArray):
        first=self.visit(node.l[0])
        return LiteralArray([first]+[self.visit(i) for i in node.l[1:]],typeof(first))
    def visit_Print(self,node:Print):
        print(*[self.visit(i) for i in node.thing],sep=self.visit(node.sep),end=self.visit(node.end),flush=self.visit(node.flush))
    def visit_NullArray(self,node:NullArray):
        return LiteralArray([],node.tp)
    visit_Break=visit_Continue=lambda self,node:node
    visit_Return=lambda self,node:Return(self.visit(node.retvalue))
    def interpreter(self):
        return self.visit(self.tree)
#}
def _len(a):
    if type(a)==str:
        return len(a)
    return len(a.l)
check_scope=Scope()
check_scope.stack=[{
    "len":BuiltinFunctionType(BasicType("int")),
    "chr":BuiltinFunctionType(BasicType("string")),
    "ord":BuiltinFunctionType(BasicType("int")),
    "getchar":BuiltinFunctionType(BasicType("string")),
    "readln":BuiltinFunctionType(BasicType("string")),
}]
run_scope=Scope()
run_scope.stack=[{
    "len":_len,
    "chr":lambda a:chr(a),
    "ord":lambda a:ord(a),
    "getchar":lambda:sys.stdin.read(1),
    "readln":lambda:input(),
}]
code='''
{
    var mem=[0],pos=5;
    var code=readln();
    var i=0;
    while(i<10){
        mem=mem+mem;
        i=i+1;
    }
    i=0;
    while(i<len(code)){
        var c:string;
        c=code[i];
        if(c=="+"){mem[pos]=mem[pos]+1;}
        if(c=="-"){mem[pos]=mem[pos]-1;}
        if(c==">"){pos=pos+1;}
        if(c=="<"){pos=pos-1;}
        if(c=="."){print[end=""] chr(mem[pos]);}
        if(c==","){mem[pos]=ord(getchar());}
        if(c=="["){
            if(mem[pos]==0){
                var l=1,r=0;
                i=i+1;
                while(i<len(code)){
                    if(code[i]=="["){l=l+1;}
                    if(code[i]=="]"){
                        r=r+1;
                        if(l!=0){
                            r=r-1;
                            l=l-1;
                        }
                    }
                    if(l==0&&r==0){break;}
                    i=i+1;
                }
            }
        }
        if(c=="]"){
            var l:int=0,r:int=1;
            i=i-1;
            while(i>=0){
                if(code[i]=="]"){r=r+1;}
                if(code[i]=="["){
                    l=l+1;
                    if(r!=0){
                        r=r-1;
                        l=l-1;
                    }
                }
                if(l==0&&r==0){break;}
                i=i-1;
            }
            i=i-1;
        }
        i=i+1;
    }
}
'''
tree=Parser(Lexer(code)).block()
Checker(tree,check_scope).check()
Interpreter(tree,run_scope).interpreter()