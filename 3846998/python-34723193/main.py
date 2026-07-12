from time import*
INTEGER,PLUS,MINUS,MUL,DIV,LPAREN,RPAREN,EOF="INTEGER","PLUS","MINUS","MUL","DIV","LPAREN","RPAREN","EOF"
ASSIGN,SEMI,DOT,BEGIN,END,ID="ASSIGN","SEMI","DOT","BEGIN","END","ID"
COMMA,COLON,BEGINL,ENDL="COMMA","COLON","BEGINL","ENDL"
CONST="CONST"
MOD,NOT,BIT_NOT,BIT_OR,BIT_AND,XOR,LSHIFT,RSHIFT="MOD","NOT","BIT_NOT","BIT_OR","BIT_AND","XOR","LSHIFT","RSHIFT"
BEQ,SEQ="BEQ","SEQ"
BIG,SMALL="BIG","SMALL"
EQ,NEQ="EQ","NEQ"
AND,OR="AND","OR"
LIST_CONST="LIST_CONST"
ITEM_INDEX="ITEM_INDEX"
SET_ITEM_INDEX="SET_ITEM_INDEX"
QUESTION="QUESTION"
MODULE_ATTR="MODULE_ATTR"
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
    (";",Token(SEMI,";")),
    (".",Token(DOT,".")),
    ("+",Token(PLUS,"")),
    ("-",Token(MINUS,"")),
    ("*",Token(MUL,"")),
    ("/",Token(DIV,"")),
    ("(",Token(LPAREN,"")),
    (")",Token(RPAREN,"")),
    ("[",Token(BEGINL,"")),
    ("]",Token(ENDL,"")),
    ("%",Token(MOD,"")),
    ("~",Token(BIT_NOT,"")),
    ("&&",Token(AND,"")),
    ("||",Token(OR,"")),
    ("|",Token(BIT_OR,"")),
    ("&",Token(BIT_AND,"")),
    ("^",Token(XOR,"")),
    (">>",Token(RSHIFT,"")),
    ("<<",Token(LSHIFT,"")),
    ("==",Token(EQ,"")),
    ("!=",Token(NEQ,"")),
    (">=",Token(BEQ,"")),
    ("<=",Token(SEQ,"")),
    ("<",Token(SMALL,"")),
    (">",Token(BIG,"")),
    ("=",Token(ASSIGN,"=")),
    ("!",Token(NOT,"")),
    ("?",Token(QUESTION,""))
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
        return Token(ID,result)
    def match(self,s,skip=True):
        if self.peek(len(s))==s:
            if skip:
                self.pos+=len(s)
                self.currend_char=self.text[self.pos]
            return True
        return False
    def string(self):
        result=""
        while self.currend_char!=None and self.currend_char!="\"":
            result+=self.currend_char
            self.advance()
        if self.currend_char==None:
            self.error()
        self.advance()
        return Token(CONST,result)
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
                    return Token(CONST,r)
                else:
                    return Token(CONST,r)
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
def Type(a,i):
    if type(a)==Var:
        return Type(i.visit(a))
    return {int:"int",str:"string",float:"float",list:"list",type(None):"NoneType",Func:"func",dict:"dict"}[type(a)]
def Types(a,j):
    return " ".join([Type(i,j) for i in a])
class Instance:
    def __init__(self,t,v):
        self.type,self.value=t,v
class BuiltinType:
    def __init__(self,n,m):
        self.name,self.methods=n,c,m
class Func:
    def __init__(self,v,t):
        self.para,self.block=v,t
class CallFunc:
    def __init__(self,v,t):
        self.func,self.args=v,t
class Var:
    def __init__(self,v):
        self.name=v
class BinOp:
    def __init__(self,l,o,r):
        self.left,self.op,self.right=l,o,r
class UnaryOp:
    def __init__(self,o,e):
        self.op,self.expr=o,e
class ThreeEyeOp:
    def __init__(self,o,n,v):
        self.cond,self.expr1,self.expr2=o,n,v
class VarStmt:
    def __init__(self,n,v=None):
        self.name,self.value=n,v
class VarStmtList:
    def __init__(self,n):
        self.children=n
class ForeachStmt:
    def __init__(self,n,v,b):
        self.name,self.items,self.block=n,v,b
class WhileStmt:
    def __init__(self,v,b):
        self.cond,self.block=v,b
class IfStmt:
    def __init__(self,v,b):
        self.cond,self.block=v,b
class IfElseStmt:
    def __init__(self,v,b,b1):
        self.cond,self.block0,self.block1=v,b,b1
class ForStmt:
    def __init__(self,i,c,e,b):
        self.init,self.cond,self.end,self.block=i,c,e,b
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
    pass
class ContinueStmt:
    pass
class AssignStmt:
    def __init__(self,n,v):
        self.name,self.value=n,v
class TryExceptStmt:
    def __init__(self,n,v):
        self.code0,self.code1=n,v
class FuncStmt:
    def __init__(self,n,p,v):
        self.name,self.para,self.block=n,p,v
class AppendCodeStmt:
    def __init__(self,n,v):
        self.name,self.code=n,v
class BuiltinFunction:
    def __init__(self,n):
        self.func=n
class ModuleStmt:
    def __init__(self,name,b):
        self.name,self.block=name,b
class Module:
    def __init__(self,v):
        self.var=v
class ModuleAttrOp:
    def __init__(self,v,n):
        self.module,self.name=v,n
class ImportStmt:
    def __init__(self,v):
        self.name=v
class NoOp:
    pass
class Parser:
    def __init__(self,l):
        self.lexer,self.error=l,l.error
        self.currend_token=self.lexer.get_next_token()
    def eat(self,tt=None):
        if tt==None:
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
    def variable(self):
        return Var(self.eat(ID).value)
    def factor_help(self,e,l=None):
        if self.currend_token.value_type==MODULE_ATTR:
            self.eat()
            name=self.variable().name
            return self.factor_help(ModuleAttrOp(e,name))
        if self.currend_token.value_type==LPAREN:
            self.eat()
            if self.currend_token.value_type==RPAREN:
                self.eat()
                f=CallFunc(e,[])
                return self.factor_help(f)
            l=[self.expr()]
            while self.currend_token.value_type==COMMA:
                self.eat()
                l.append(self.expr())
            self.eat(RPAREN)
            return self.factor_help(CallFunc(e,l))
        if self.currend_token.value_type==BEGINL:
            self.eat()
            index=self.expr()
            self.eat(ENDL)
            return self.factor_help(BinOp(e,Token(ITEM_INDEX,""),index))
        if l==None:
            return e
        return l
    def factor(self):
        if self.token_eq(Token(ID,"None")):
            self.eat()
            return None
        if self.currend_token.value_type in (MINUS,NOT,BIT_NOT):
            return UnaryOp(self.eat().value_type,self.factor())
        if self.currend_token.value_type==COLON:
            self.eat()
            return self.factor_help(Local(self.factor()))
        if self.currend_token.value_type==BEGINL:
            self.eat()
            if self.currend_token.value_type==ENDL:
                self.eat()
                return self.factor_help(List([]))
            l=[self.expr()]
            while self.currend_token.value_type==COMMA:
                self.eat()
                l.append(self.expr())
            self.eat(ENDL)
            return self.factor_help(List(l))
        if self.currend_token.value_type==CONST:
            return self.factor_help(self.eat().value)
        if self.currend_token.value_type==LPAREN:
            self.eat()
            e=self.expr()
            self.eat(RPAREN)
            return self.factor_help(e)
        if self.currend_token.value_type==ID:
            i=self.eat()
            return self.factor_help(Var(i.value))
    def block(self):
        if self.currend_token.value_type==BEGIN:
            self.eat()
            l=[self.statement()]
            while self.currend_token.value_type in (SEMI) or type(l[-1]) in (WhileStmt,ForeachStmt,IfStmt,FuncStmt,TryExceptStmt,IfElseStmt,ForStmt,AppendCodeStmt,ModuleStmt):
                if self.currend_token.value_type in (SEMI):
                    self.eat()
                if self.currend_token.value_type==END:
                    break
                l.append(self.statement())
            self.eat(END)
            return Block(l)
        else:
            s=self.statement()
            if type(s) not in (WhileStmt,ForeachStmt,IfStmt,FuncStmt,TryExceptStmt,IfElseStmt,ForStmt,AppendCodeStmt,ModuleStmt):
                self.eat(SEMI)
            return Block([s])
    def statement(self):
        def w(self):
            n=Var(self.eat(ID).value)
            while self.currend_token.value_type==BEGINL or self.currend_token.value_type==MODULE_ATTR:
                if self.currend_token.value_type==BEGINL:
                    self.eat()
                    name=self.expr()
                    self.eat(ENDL)
                    n=BinOp(n,Token(ITEM_INDEX,""),name)
                if self.currend_token.value_type==MODULE_ATTR:
                    self.eat()
                    name=self.eat(ID).value
                    n=ModuleAttrOp(n,name)
            return n
        if self.token_eq(Token(ID,"var")):
            self.eat()
            def vd(self):
                i=self.variable()
                if self.currend_token.value_type==ASSIGN:
                    self.eat()
                    e=self.expr()
                    return VarStmt(i,e)
                return VarStmt(i)
            vdl=[vd(self)]
            while self.currend_token.value_type==COMMA:
                self.eat()
                vdl.append(vd(self))
            return VarStmtList(vdl)
        if self.token_eq(Token(ID,"foreach")):
            self.eat()
            i=self.variable()
            self.eat_token(Token(ID,"in"))
            l=self.expr()
            return ForeachStmt(i,l,self.block())
        if self.token_eq(Token(ID,"while")):
            self.eat()
            l=self.expr()
            return WhileStmt(l,self.block())
        if self.token_eq(Token(ID,"if")):
            self.eat()
            l=self.expr()
            b0=self.block()
            if not self.token_eq(Token(ID,"else")):
                return IfStmt(l,b0)
            else:
                self.eat()
                b1=self.block()
                return IfElseStmt(l,b0,b1)
        if self.token_eq(Token(ID,"break")):
            self.eat()
            return BreakStmt()
        if self.token_eq(Token(ID,"continue")):
            self.eat()
            return ContinueStmt()
        if self.token_eq(Token(ID,"for")):
            self.eat()
            i=self.statement()
            self.eat(SEMI)
            c=self.expr()
            self.eat(SEMI)
            e=self.statement()
            return ForStmt(i,c,e,self.block())
        if self.token_eq(Token(ID,"return")):
            self.eat()
            return ReturnStmt(self.expr())
        if self.token_eq(Token(ID,"try")):
            self.eat()
            c1=self.block()
            self.eat_token(Token(ID,"except"))
            c2=self.block()
            return TryExceptStmt(c1,c2)
        if self.token_eq(Token(ID,"func")):
            self.eat()
            name=w(self)
            self.eat(LPAREN)
            if self.currend_token.value_type==RPAREN:
                self.eat()    
                return FuncStmt(name,[],self.block())
            l=[self.variable().name]
            while self.currend_token.value_type==COMMA:
                self.eat()
                l.append(self.variable().name)
            self.eat(RPAREN)
            return FuncStmt(name,l,self.block())
        if self.token_eq(Token(ID,"append_code")):
            self.eat()
            name=w(self)
            return AppendCodeStmt(name,self.block())
        if self.token_eq(Token(ID,"module")):
            self.eat()
            name=w(self)
            return ModuleStmt(name,self.block())
        if self.token_eq(Token(ID,"import")):
            self.eat()
            n=self.expr()
            return ImportStmt(n)
        if self.currend_token.value_type==ID:
            n=self.expr()
            if self.currend_token.value_type==ASSIGN:
                self.eat()
                return AssignStmt(n,self.expr())
            return n
        if self.currend_token.value_type==BEGIN:
            return self.block()
        if self.currend_token.value_type==SEMI:
            return NoOp()
        return self.expr()
    def expr_help(self,lower,l):
        ans=lower()
        while self.currend_token.value_type in l:
            ans=BinOp(ans,self.eat(),lower())
        return ans
    term=lambda self:self.expr_help(self.factor,(MUL,DIV,MOD))
    expr0=lambda self:self.expr_help(self.term,(PLUS,MINUS))
    expr1=lambda self:self.expr_help(self.expr0,(LSHIFT,RSHIFT))
    expr2=lambda self:self.expr_help(self.expr1,(EQ,NEQ,BIG,SMALL,BEQ,SEQ))
    expr3=lambda self:self.expr_help(self.expr2,(BIT_OR,XOR,BIT_AND))
    expr4=lambda self:self.expr_help(self.expr3,(AND,OR))
    def expr(self):
        e=self.expr4()
        if self.currend_token.value_type!=QUESTION:
            return e
        self.eat()
        c1=self.expr4()
        self.eat(COLON)
        c2=self.expr4()
        return ThreeEyeOp(e,c1,c2)
def throw(c):
    raise Exception(c)
binary_operator_list={
    "PLUS":lambda a,b:a+b,
    "MINUS":lambda a,b:a-b,
    "MUL":lambda a,b:a*b,
    "DIV":lambda a,b:a/b,
    "MOD":lambda a,b:a%b,
    "BIT_OR":lambda a,b:a|b,
    "BIT_AND":lambda a,b:a&b,
    "XOR":lambda a,b:a^b,
    "LSHIFT":lambda a,b:a<<b,
    "RSHIFT":lambda a,b:a>>b,
    "BIG":lambda a,b:a>b,
    "SMALL":lambda a,b:a<b,
    "SEQ":lambda a,b:a<=b,
    "BEQ":lambda a,b:a>=b,
    "EQ":lambda a,b:a==b,
    "NEQ":lambda a,b:a!=b,
    "AND":lambda a,b:a and b,
    "OR":lambda a,b:a or b,
    "ITEM_INDEX":lambda a,b:a[b]
}
unary_operator_list={
    "MINUS":lambda a:-a,
    "NOT":lambda a:not a,
    "BIT_NOT":lambda a:~a
}
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
        self.struct={}
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
            if type(v)==type(lambda:0):
                v=BuiltinFunction(v)
            self.var[k]=v
class Interpreter(NodeVisitor):
    def __init__(self,t,s=Scope(None)):
        self.scope=s
        self.tree=t
    def error(self):
        raise Exception("Wrong input!")
    def visit_BinOp(self,n):
        v=binary_operator_list[n.op.value_type](self.visit(n.left),self.visit(n.right))
        if type(v)==bool:
            return int(v)
        return v
    def visit_UnaryOp(self,n):
        v=unary_operator_list[n.op.value_type](self.visit(n.expr))
    def visit_VarStmt(self,n):
        v=self.visit(n.value)
        if type(v)==Func:
            tp=v.paratypes
            name=n.name.name
            try:
                lcl=self.scope.find(name)
                self.scope.set(name,lcl.define(tp,v))
            except:
                self.scope.define(name,VarFunc(tp,v))
        else:
            self.scope.define(n.name.name,v)
    def visit_Block(self,n,w=0):
        NewScope=Scope(self.scope)
        for i in n.children:
            ls=Interpreter(i,NewScope).interprete()
            if type(ls) in [BreakStmt,ContinueStmt,ReturnStmt]:
                if w:
                    return ls,NewScope
                return ls
        return None,NewScope
    def visit_ForeachStmt(self,n):
        for i in self.visit(n.items):
            NewScope=Scope(self.scope)
            NewScope.define(n.name.name,i)
            ls=Interpreter(n.block,NewScope).interprete()
            if type(ls)==BreakStmt:
                break
            if type(ls)==ReturnStmt:
                return ls
    def visit_WhileStmt(self,n):
        while self.visit(n.cond):
            NewScope=Scope(self.scope)
            ls=Interpreter(n.block,NewScope).interprete()
            if type(ls)==BreakStmt:
                break
            if type(ls)==ReturnStmt:
                return ls
    def visit_IfStmt(self,n):
        if self.visit(n.cond):
            NewScope=Scope(self.scope)
            ls=Interpreter(n.block,NewScope).interprete()
            if type(ls) in [BreakStmt,ContinueStmt]:
                return ls
            if type(ls)==ReturnStmt:
                return ls
    def visit_IfElseStmt(self,n):
        if self.visit(n.cond):
            NewScope=Scope(self.scope)
            ls=Interpreter(n.block0,NewScope).interprete()
            if type(ls) in [BreakStmt,ContinueStmt]:
                return ls
            if type(ls)==ReturnStmt:
                return ls
        else:
            NewScope=Scope(self.scope)
            ls=Interpreter(n.block1,NewScope).interprete()
            if type(ls) in [BreakStmt,ContinueStmt]:
                return ls
            if type(ls)==ReturnStmt:
                return ls
    def visit_ForStmt(self,n):
        Big=Scope(self.scope)
        Interpreter(n.init,Big).interprete()
        while Interpreter(n.cond,Big).interprete():
            Small=Scope(Big)
            ls=Interpreter(n.block,Small).interprete()
            if type(ls)==BreakStmt:
                break
            if type(ls)==ReturnStmt:
                return ls
            Interpreter(n.end,Big).interprete()
    def visit_VarStmtList(self,n):
        for i in n.children:
            self.visit(i)
    def visit_TryExceptStmt(self,n):
        try:
            NewScope=Scope(self.scope)
            Interpreter(n.code0,NewScope).interprete()
        except Exception as e:
            NewScope=Scope(self.scope)
            NewScope.define("EXCEPTION",str(e))
            Interpreter(n.code1,NewScope).interprete()
    def visit_CallFunc(self,n):
        a=[self.visit(i) for i in n.args]
        def preval(a):
            if type(a)==ReturnStmt:
                return preval(a.value)
            return a
        f=self.visit(n.func)
        if type(n.func)==Var:
            if n.func.name=="type":
                return Types(*a,self)
        if type(f)==BuiltinFunction:
            return f.func(*a)
        p=f.para
        b=f.block
        if len(a)<len(p):
            a.extend([0]*(len(p)-len(a)))
        ARGS=a[len(p):]
        d=dict(zip(p,a))
        d["ARGS"]=ARGS
        NewScope=Scope(self.scope)
        NewScope.var=d
        itpt=Interpreter(b,NewScope)
        v,NewScope=itpt.visit_Block(b,1)
        v=preval(v)
        v=Interpreter(b,NewScope).visit(v)
        return v
    def visit_AssignStmt(self,n):
        v=self.visit(n.value)
        if (type(n.name)==BinOp and n.name.op.value_type==ITEM_INDEX) or type(n.name)==ModuleAttrOp:
            name=n.name
            indexs=[]
            while (type(name)==BinOp and name.op.value_type==ITEM_INDEX) or type(name)==ModuleAttrOp:
                if type(name)==ModuleAttrOp:
                    indexs=[name.name]+indexs
                    name=name.module
                else:
                    indexs=[self.visit(name.right)]+indexs
                    name=name.left
            if type(name)!=Var:
                self.error()
            def change(item,indexs,value):
                if indexs==[]:
                    return value
                if type(item)==Module:
                    if indexs[0] not in item.var.keys():
                        item.var[indexs[0]]=0
                    item.var[indexs[0]]=change(item.var[indexs[0]],indexs[1:],value)
                else:
                    item[indexs[0]]=change(item[indexs[0]],indexs[1:],value)
                return item
            item=self.visit(name)
            item=change(item,indexs,v)
            self.scope.set(name.name,item)
        elif type(n.name)==Var:
            self.scope.set(n.name.name,v)
        else:
            self.error()
    def visit_AppendCodeStmt(self,n):
        f=self.visit(n.name)
        if type(f)==Func:
            f.block.children.extend(n.code.children)
            self.visit(AssignStmt(n.name,Func(f.para,f.block)))
    def visit_Var(self,n):
        return self.visit(self.scope.find(n.name))
    def visit_FuncStmt(self,n):
        if type(n.name)==Var:
            self.scope.define(n.name.name,Func(n.para,n.block))
        else:
            self.visit(AssignStmt(n.name,Func(n.para,n.block)))
    def visit_ModuleStmt(self,n):
        NewScope=Scope(self.scope)
        NewItpt=Interpreter("",NewScope)
        for stmt in n.block.children:
            NewItpt.visit(stmt)
        if type(n.name)==Var:
            self.scope.define(n.name.name,Module(NewItpt.scope.var))
        else:
            self.visit(AssignStmt(n.name,NewItpt.scope.var))
    def visit_ModuleAttrOp(self,n):
        return self.visit(n.module).var[n.name]
    def visit_ImportStmt(self,n):
        self.scope.buildin(self.visit(n.name).var)
    def interprete(self):
        return self.visit(self.tree)
    visit_list=lambda self,a:a
    visit_int=visit_list
    visit_str=visit_list
    visit_float=visit_list
    visit_range=visit_list
    visit_NoneType=visit_list
    visit_ContinueStmt=visit_list
    visit_ReturnStmt=visit_list
    visit_BreakStmt=visit_list
    visit_Func=visit_list
    visit_dict=visit_list
    visit_BuiltinFunction=visit_list
    visit_Module=visit_list
    visit_NoOp=lambda self,n:None
    visit_List=lambda self,n:[self.visit(i) for i in n.value]
MainScope=Scope(None)
MainScope.buildin({
    "print":lambda *ARGS:print(*ARGS,sep="",end=""),
    "println":lambda *ARGS:print(*ARGS,sep=""),
    "len":lambda a:len(a),
    "sqrt":lambda a:a**0.5,
    "pow":lambda a,b:a**b,
    "input":lambda:input(),
    "throw":throw,
    "dict":lambda a,b:dict(zip(a,b)),
    "time":lambda:time(),
    "char":chr,
    "unicode":ord
})
print('''简介：
这是integer3-的快速版，快速主要表现在实现简单、语法简单（至少比integer3-简单）
判断质数代码了解一下：
{
    func prime(a){
        if a<2 return 0;
        for var i=2;i<=sqrt(a);i=i+1 if a%i==0 return 0;
        return 1;
    }
    print(prime(2));//输出是1
}
这个语言也可以叫“承上启下”的语言
承接integer3-的大部分语法
又为integer3打好基础
简介到此结束
更新：
新增了一个叫module的语句，可能会导致代码跑得特别慢
可以写代码了，end结束''')
t=""
while 1:
    a=input()
    if a=="end":
        break
    t+="\n"+a
print("\n\033[1;33m代码运行开始\033[1;0m")
Interpreter(Parser(Lexer(t)).block(),MainScope).interprete()
print("\n\033[1;33m代码运行结束\033[1;0m")
'''
{
    func prime(a){
        if a<2 return 0;
        for var i=2;i<=sqrt(a);i=i+1 if a%i==0 return 0;
        return 1;
    }
    print(prime(101));
}

{
    if 1 print(1);
    else print(2);
}

{
    print("Hello,world!
Hello,integer!");
}

{
    func fac(a){
        if a==0 return 1;
        return a*fac(a-1);
    }
    print(fac(10));
}

{
    func sleep(n){
        var w=time();
        while(time()-w<n);
    }
    var n=10,t=time();
    var ans=[0]*n,visit=[0]*n;
    func dfs(k){
        if k==n{
            println(ans," ",time()-t);
            sleep(0.005);
            t=time();
            return 0;
        }
        for var i=0;i<n;i=i+1 if visit[i]==0{
            ans[k]=i;
            visit[i]=1;
            dfs(k+1);
            visit[i]=0;
            ans[k]=0;
        }
    }
    dfs(0);
}

{
    func f(){};
    append_code f{
        return 1;
    }
    print(f());
}
'''