INTEGER,PLUS,MINUS,MUL,DIV,LPAREN,RPAREN,EOF="INTEGER","PLUS","MINUS","MUL","DIV","LPAREN","RPAREN","EOF"
ASSIGN,SEMI,DOT,BEGIN,END,ID="ASSIGN","SEMI","DOT","BEGIN","END","ID"
COMMA,COLON,BEGINL,ENDL="COMMA","COLON","BEGINL","ENDL"
INTEGER_CONST,FLOAT_CONST,STRING_CONST,NONE_CONST="INTEGER_CONST","FLOAT_CONST","STRING_CONST","NONE_CONST"
MOD,NOT,BIT_NOT,BIT_OR,BIT_AND,XOR,LSHIFT,RSHIFT="MOD","NOT","BIT_NOT","BIT_OR","BIT_AND","XOR","LSHIFT","RSHIFT"
BEQ,SEQ="BEQ","SEQ"
BIG,SMALL="BIG","SMALL"
EQ,NEQ="EQ","NEQ"
AND,OR="AND","OR"
LIST_CONST="LIST_CONST"
ITEM_INDEX="ITEM_INDEX"
SET_ITEM_INDEX="SET_ITEM_INDEX"
QUESTION="QUESTION"
class Token:
    def __init__(self,vt,v):
        self.value_type,self.value=vt,v
    def __str__(self):
        return "Token({},{})".format(self.value_type,self.value)
    def __repr__(self):
        return self.__str__()
key_tokens=(
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
        return Token(STRING_CONST,result)
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
                    return Token(FLOAT_CONST,r)
                else:
                    return Token(INTEGER_CONST,r)
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
class ConstValue:
    def __init__(self,v,t):
        self.value,self.type=v,t
'''class ItemIndex:
    def __init__(self,v,t):
        self.item,self.index=v,t'''
class Func:
    def __init__(self,tp,v,t):
        self.paratypes,self.para,self.block=tp,v,t
def Type(a,i):
    if type(a) in (Var,ConstValue):
        return Type(i.visit(a),i)
    if type(a)==ThisStruct:
        return a.name
    return {int:"int",str:"string",float:"float",list:"list",type(None):"NoneType",VarFunc:"func",Func:"func",dict:"dict"}[type(a)]
def Types(a,j):
    return " ".join([Type(i,j) for i in a])
class VarFunc:
    def __init__(self,tp,f):
        self.funcs={tp:f}
    def define(self,tp,f):
        self.funcs[tp]=f
        return self
class CallFunc:
    def __init__(self,v,t):
        self.func,self.args=v,t
class Var:
    def __init__(self,v):
        self.name=v
class Local:
    def __init__(self,v):
        self.value=v
class BinOp:
    def __init__(self,l,o,r):
        self.left,self.op,self.right=l,o,r
class UnaryOp:
    def __init__(self,o,e):
        self.op,self.expr=o,e
class ThreeEyeOp:
    def __init__(self,o,n,v):
        self.cond,self.expr1,self.expr2=o,n,v
class DotOp:
    def __init__(self,l,r):
        self.left,self.right=l,r
'''class PrintStmt:
    def __init__(self,v):
        self.item=v'''
class VarStmt:
    def __init__(self,n,v=ConstValue(None,NONE_CONST)):
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
class Dict:
    def __init__(self,k,v):
        self.keys,self.values=k,v
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
class StructStmt:
    def __init__(self,n,v):
        self.name,self.var=n,v
class InitOp:
    def __init__(self,n):
        self.name=n
class Method:
    def __init__(self,n,v):
        self.instance,self.func=n,v
class NoOp:
    pass
CONST_TYPES=(STRING_CONST,INTEGER_CONST,FLOAT_CONST,NONE_CONST,LIST_CONST)
TYPE_DICT={int:INTEGER_CONST,float:FLOAT_CONST,str:STRING_CONST,type(None):NONE_CONST,list:LIST_CONST,Func:""}
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
        return Var(self.eat(ID))
    def statement(self):
        #print变成函数了
        '''if self.currend_token.value_type==ID and self.currend_token.value=="print":
            self.eat()
            e=self.expr()
            return PrintStmt(e)'''
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
        if self.token_eq(Token(ID,"struct")):
            self.eat()
            n=self.eat(ID)
            self.eat(BEGIN)
            v=[]
            while self.currend_token.value_type!=END:
                v.append(self.eat(ID).value)
            self.eat(END)
            return StructStmt(n,v)
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
    def block(self):
        if self.currend_token.value_type==BEGIN:
            self.eat()
            l=[self.statement()]
            while self.currend_token.value_type in (SEMI) or type(l[-1]) in (WhileStmt,ForeachStmt,IfStmt,IfElseStmt,TryExceptStmt,ForStmt):
                if self.currend_token.value_type in (SEMI):
                    self.eat()
                if self.currend_token.value_type==END:
                    break
                l.append(self.statement())
            self.eat(END)
            return Block(l)
        else:
            s=self.statement()
            if type(s) not in (WhileStmt,ForeachStmt,IfStmt,IfElseStmt,TryExceptStmt,ForStmt):
                self.eat(SEMI)
            return Block([s])
    def factor_help(self,e,l=None):
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
        if self.currend_token.value_type==DOT:
            self.eat()
            index=self.variable().name.value
            return self.factor_help(DotOp(e,index))
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
        if self.currend_token.value_type==BEGIN:
            self.eat()
            if self.currend_token.value_type==END:
                self.eat()
                return Dict([],[])
            k=[self.expr()]
            self.eat(COLON)
            v=[self.expr()]
            while self.currend_token.value_type==COMMA:
                self.eat()
                k.append(self.expr())
                self.eat(COLON)
                v.append(self.expr())
            self.eat(END)
            return Dict(k,v)
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
        if self.currend_token.value_type in CONST_TYPES:
            return self.factor_help(ConstValue(self.eat().value,""))
        if self.currend_token.value_type==LPAREN:
            self.eat()
            e=self.expr()
            self.eat(RPAREN)
            return self.factor_help(e)
        if self.token_eq(Token(ID,"func")):
            self.eat()
            self.eat(LPAREN)
            if self.currend_token.value_type==RPAREN:
                self.eat()
                f=Func("",[],self.block())
                return self.factor_help(f)
            t=[self.eat(ID)]
            l=[self.eat(ID)]
            while self.currend_token.value_type==COMMA:
                self.eat()
                t.append(self.eat(ID))
                l.append(self.eat(ID))
            self.eat(RPAREN)
            return self.factor_help(Func(" ".join(i.value for i in t),l,self.block()))
        if self.token_eq(Token(ID,"init")):
            self.eat()
            return InitOp(self.eat(ID))
        if self.currend_token.value_type==ID:
            i=self.eat()
            return self.factor_help(Var(i.value))
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
class NodeVisitor:
    def visit(self,node):
        method_name="visit_"+type(node).__name__
        visitor=getattr(self,method_name,self.generic_visit)
        return visitor(node)
    def generic_visit(self,node):
        raise Exception("Can't find method\"visit_{}()\"".format(type(node).__name__))
freebuiltinfunctions={
    "print":lambda *a:print(*a,end="",sep=""),
    "input":input
}
def set_item_index(i,n,v):
    i[n]=v
    return i
builtinfunctions={
    "sqrt int":lambda a:a**0.5,
    "sqrt float":lambda a:a**0.5,
    "char int":chr,
    "range int":range,
    "range int int":range,
    "range int int int":range,
    "unicode string":ord,
    "pow int int":lambda a,b:a**b,
    "pow float int":lambda a,b:a**b,
    "pow int float":lambda a,b:a**b,
    "pow float int":lambda a,b:a**b,
    "int string":int,
    "int float":int,
    "len string":len,
    "len list":len,
    
    "__AND__ int int":lambda a,b:a and b,
    
    "__OR__ int int":lambda a,b:a or b,
    
    "__BIT_OR__ int int":lambda a,b:a|b,
    "__BIT_OR__ int float":lambda a,b:a|b,
    "__BIT_OR__ float int":lambda a,b:a|b,
    "__BIT_OR__ float float":lambda a,b:a|b,
    
    "__BIT_AND__ int int":lambda a,b:a&b,
    "__BIT_AND__ int float":lambda a,b:a&b,
    "__BIT_AND__ float int":lambda a,b:a&b,
    "__BIT_AND__ float float":lambda a,b:a&b,
    
    "__BIT_XOR__ int int":lambda a,b:a^b,
    "__BIT_XOR__ int float":lambda a,b:a^b,
    "__BIT_XOR__ float int":lambda a,b:a^b,
    "__BIT_XOR__ float float":lambda a,b:a^b,
    
    "__PLUS__ int int":lambda a,b:a+b,
    "__PLUS__ float float":lambda a,b:a+b,
    "__PLUS__ float int":lambda a,b:a+b,
    "__PLUS__ int float":lambda a,b:a+b,
    "__PLUS__ string string":lambda a,b:a+b,
    "__PLUS__ list list":lambda a,b:a+b,
    
    "__MINUS__ int int":lambda a,b:a-b,
    "__MINUS__ float float":lambda a,b:a-b,
    "__MINUS__ int float":lambda a,b:a-b,
    "__MINUS__ float int":lambda a,b:a-b,
    
    "__MUL__ int int":lambda a,b:a*b,
    "__MUL__ int float":lambda a,b:a*b,
    "__MUL__ float int":lambda a,b:a*b,
    "__MUL__ float float":lambda a,b:a*b,
    "__MUL__ int string":lambda a,b:a*b,
    "__MUL__ string int":lambda a,b:a*b,
    "__MUL__ int list":lambda a,b:a*b,
    "__MUL__ list int":lambda a,b:a*b,
    
    "__DIV__ int int":lambda a,b:a/b,
    "__DIV__ int float":lambda a,b:a/b,
    "__DIV__ float int":lambda a,b:a/b,
    "__DIV__ float float":lambda a,b:a/b,
    
    "__MOD__ int int":lambda a,b:a%b,
    "__MOD__ int float":lambda a,b:a%b,
    "__MOD__ float int":lambda a,b:a%b,
    "__MOD__ float float":lambda a,b:a%b,
    
    "__BIG__ int int":lambda a,b:a>b,
    "__BIG__ int float":lambda a,b:a>b,
    "__BIG__ float int":lambda a,b:a>b,
    "__BIG__ float float":lambda a,b:a>b,
    "__BIG__ list list":lambda a,b:a>b,
    "__BIG__ string string":lambda a,b:a>b,
    
    "__SMALL__ int int":lambda a,b:a<b,
    "__SMALL__ int float":lambda a,b:a<b,
    "__SMALL__ float int":lambda a,b:a<b,
    "__SMALL__ float float":lambda a,b:a<b,
    "__SMALL__ list list":lambda a,b:a<b,
    "__SMALL__ string string":lambda a,b:a<b,
    
    "__EQ__ int int":lambda a,b:a==b,
    "__EQ__ int string":lambda a,b:a==b,
    "__EQ__ int float":lambda a,b:a==b,
    "__EQ__ int list":lambda a,b:a==b,
    "__EQ__ int dict":lambda a,b:a==b,
    "__EQ__ int NoneType":lambda a,b:a==b,
    "__EQ__ string int":lambda a,b:a==b,
    "__EQ__ string string":lambda a,b:a==b,
    "__EQ__ string float":lambda a,b:a==b,
    "__EQ__ string list":lambda a,b:a==b,
    "__EQ__ string dict":lambda a,b:a==b,
    "__EQ__ string NoneType":lambda a,b:a==b,
    "__EQ__ float int":lambda a,b:a==b,
    "__EQ__ float string":lambda a,b:a==b,
    "__EQ__ float float":lambda a,b:a==b,
    "__EQ__ float list":lambda a,b:a==b,
    "__EQ__ float dict":lambda a,b:a==b,
    "__EQ__ float NoneType":lambda a,b:a==b,
    "__EQ__ list int":lambda a,b:a==b,
    "__EQ__ list string":lambda a,b:a==b,
    "__EQ__ list float":lambda a,b:a==b,
    "__EQ__ list list":lambda a,b:a==b,
    "__EQ__ list dict":lambda a,b:a==b,
    "__EQ__ list NoneType":lambda a,b:a==b,
    "__EQ__ dict int":lambda a,b:a==b,
    "__EQ__ dict string":lambda a,b:a==b,
    "__EQ__ dict float":lambda a,b:a==b,
    "__EQ__ dict list":lambda a,b:a==b,
    "__EQ__ dict dict":lambda a,b:a==b,
    "__EQ__ dict NoneType":lambda a,b:a==b,
    "__EQ__ NoneType int":lambda a,b:a==b,
    "__EQ__ NoneType string":lambda a,b:a==b,
    "__EQ__ NoneType float":lambda a,b:a==b,
    "__EQ__ NoneType list":lambda a,b:a==b,
    "__EQ__ NoneType dict":lambda a,b:a==b,
    "__EQ__ NoneType NoneType":lambda a,b:a==b,
    
    "__BEQ__ int int":lambda a,b:a>=b,
    "__BEQ__ int float":lambda a,b:a>=b,
    "__BEQ__ float int":lambda a,b:a>=b,
    "__BEQ__ float float":lambda a,b:a>=b,
    "__BEQ__ list list":lambda a,b:a>=b,
    "__BEQ__ string string":lambda a,b:a>=b,
    
    "__SEQ__ int int":lambda a,b:a<=b,
    "__SEQ__ int float":lambda a,b:a<=b,
    "__SEQ__ float int":lambda a,b:a<=b,
    "__SEQ__ float float":lambda a,b:a<=b,
    "__SEQ__ list list":lambda a,b:a<=b,
    "__SEQ__ string string":lambda a,b:a<=b,
    
    "__NEQ__ int int":lambda a,b:a!=b,
    "__NEQ__ int string":lambda a,b:a!=b,
    "__NEQ__ int float":lambda a,b:a!=b,
    "__NEQ__ int list":lambda a,b:a!=b,
    "__NEQ__ int dict":lambda a,b:a!=b,
    "__NEQ__ int NoneType":lambda a,b:a!=b,
    "__NEQ__ string int":lambda a,b:a!=b,
    "__NEQ__ string string":lambda a,b:a!=b,
    "__NEQ__ string float":lambda a,b:a!=b,
    "__NEQ__ string list":lambda a,b:a!=b,
    "__NEQ__ string dict":lambda a,b:a!=b,
    "__NEQ__ string NoneType":lambda a,b:a!=b,
    "__NEQ__ float int":lambda a,b:a!=b,
    "__NEQ__ float string":lambda a,b:a!=b,
    "__NEQ__ float float":lambda a,b:a!=b,
    "__NEQ__ float list":lambda a,b:a!=b,
    "__NEQ__ float dict":lambda a,b:a!=b,
    "__NEQ__ float NoneType":lambda a,b:a!=b,
    "__NEQ__ list int":lambda a,b:a!=b,
    "__NEQ__ list string":lambda a,b:a!=b,
    "__NEQ__ list float":lambda a,b:a!=b,
    "__NEQ__ list list":lambda a,b:a!=b,
    "__NEQ__ list dict":lambda a,b:a!=b,
    "__NEQ__ list NoneType":lambda a,b:a!=b,
    "__NEQ__ dict int":lambda a,b:a!=b,
    "__NEQ__ dict string":lambda a,b:a!=b,
    "__NEQ__ dict float":lambda a,b:a!=b,
    "__NEQ__ dict list":lambda a,b:a!=b,
    "__NEQ__ dict dict":lambda a,b:a!=b,
    "__NEQ__ dict NoneType":lambda a,b:a!=b,
    "__NEQ__ NoneType int":lambda a,b:a!=b,
    "__NEQ__ NoneType string":lambda a,b:a!=b,
    "__NEQ__ NoneType float":lambda a,b:a!=b,
    "__NEQ__ NoneType list":lambda a,b:a!=b,
    "__NEQ__ NoneType dict":lambda a,b:a!=b,
    "__NEQ__ NoneType NoneType":lambda a,b:a!=b,
    
    "__MINUS__ int":lambda a:-a,
    "__MINUS__ float":lambda a:-a,
    
    "__NOT__ int":lambda a:not a,
    "__NOT__ float":lambda a:not a,
    
    "__BIT_NOT__ int":lambda a:~a,
    "__BIT_NOT__ float":lambda a:~a,
    
    "__ITEM_INDEX__ string int":lambda a,b:a[b],
    "__ITEM_INDEX__ list int":lambda a,b:a[b],
    "__ITEM_INDEX__ dict int":lambda a,b:a[b],
    "__ITEM_INDEX__ dict float":lambda a,b:a[b],
    "__ITEM_INDEX__ dict string":lambda a,b:a[b],
    
    "__SET_ITEM_INDEX__ string int":set_item_index,
    "__SET_ITEM_INDEX__ list int":set_item_index,
    "__SET_ITEM_INDEX__ dict int":set_item_index,
    "__SET_ITEM_INDEX__ dict float":set_item_index,
    "__SET_ITEM_INDEX__ dict string":set_item_index,
}
'''operators={
    "+":"__PLUS__",
    "-":"__MINUS__",
    "*":"__MUL__",
    "/":"__DIV__",
    "%":"__MOD__",
    "|":"__BIT_OR__",
    "&":"__BIT_AND__",
    "^":"__XOR__",
    "<<":"__LSHIFT__",
    ">>":"__RSHIFT__",
    ">":"__BIG__",
    "<":"__SMALL__",
    "<=":"__SEQ__",
    ">=":"__BEQ__",
    "==":"__EQ__",
    "!=":"__NEQ__",
    "&&":"__AND__",
    "||":"__OR__"
}'''
'''binary_operator_list={
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
    "OR":lambda a,b:a or b
}'''
class Struct:
    def __init__(self,n,v):
        self.name,self.var=n,v
class ThisStruct:
    def __init__(self,n,v):
        self.name,self.var=n,v
    def set(self,n,v):
        self.var[n]=v
class Scope:
    def __init__(self,p):
        self.var={}
        self.struct={}
        self.parent=p
    def define(self,n,v):
        self.var[n]=v
    def defines(self,n,v):
        self.struct[n]=v
    def find(self,name):
        t=self
        while t!=None:
            if name in t.var.keys():
                return t.var[name]
            t=t.parent
        raise Exception("Wrong id!")
    def finds(self,name):
        t=self
        while t!=None:
            if name in t.struct.keys():
                return t.struct[name]
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
class Interpreter(NodeVisitor):
    def __init__(self,t,s=Scope(None)):
        self.scope=s
        self.tree=t
    def error(self):
        raise Exception("Wrong input!")
    def visit_BinOp(self,n):
        l,r=self.visit(n.left),self.visit(n.right)
        name="__"+n.op.value_type+"__ "+Types([l,r],self)
        if "__"+n.op.value_type+"__" in freebuiltinfunctions.keys():
            v=freebuiltinfunctions["__"+n.op.value_type+"__"](l,r)
            if type(v)==bool:
                return int(v)
            return v
        if name in builtinfunctions.keys():
            v=builtinfunctions[name](l,r)
            if type(v)==bool:
                return int(v)
            return v
        a=[l,r]
        def preval(a):
            if type(a)==ReturnStmt:
                return preval(a.value)
            return a
        tp=Types(a,self)
        func=self.scope.find("__"+n.op.value_type+"__").funcs[tp]
        p=[i.value for i in self.visit(func).para]
        b=self.visit(func).block
        NewScope=Scope(self.scope)
        NewScope.var=dict(zip(p,a))
        itpt=Interpreter(b,NewScope)
        v,NewScope=itpt.visit_Block(b,1)
        v=preval(v)
        v=Interpreter(b,NewScope).visit(v)
        return v
    def visit_Var(self,n):
        if type(n.name)==str:
            return self.visit(self.scope.find(n.name))
        return self.visit(self.scope.find(n.name.value))
    def visit_PrintStmt(self,n):
        print(self.visit(n.item),end="")
    def visit_VarStmt(self,n):
        v=self.visit(n.value)
        if type(v)==Func:
            tp=v.paratypes
            name=n.name.name.value
            try:
                lcl=self.scope.find(name)
                self.scope.set(name,lcl.define(tp,v))
            except:
                self.scope.define(name,VarFunc(tp,v))
        else:
            self.scope.define(n.name.name.value,v)
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
            NewScope.define(n.name.name.value,ConstValue(i,TYPE_DICT[type(i)]))
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
    def visit_CallFunc(self,n):
        a=[self.visit(i) for i in n.args]
        def preval(a):
            if type(a)==ReturnStmt:
                return preval(a.value)
            return a
        if type(n.func)==Var:
            name=n.func.name
            if name=="type":
                return Type(*a,self)
            if name in freebuiltinfunctions.keys():
                return freebuiltinfunctions[name](*a)
            if name+" "+Types(a,self) in builtinfunctions.keys():
                return builtinfunctions[name+" "+Types(a,self)](*a)
        if type(n.func)==Var:
            tp=Types(a,self)
            func=self.scope.find(n.func.name).funcs[tp]
            p=[i.value for i in self.visit(func).para]
            b=self.visit(func).block
            if len(a)!=len(p):
                self.error()
            NewScope=Scope(self.scope)
            NewScope.var=dict(zip(p,a))
            itpt=Interpreter(b,NewScope)
            v,NewScope=itpt.visit_Block(b,1)
            v=preval(v)
            v=Interpreter(b,NewScope).visit(v)
            return v
        if type(self.visit(n.func))==VarFunc:
            tp=Types(a,self)
            func=self.visit(n.func).funcs[tp]
            p=[i.value for i in self.visit(func).para]
            b=self.visit(func).block
            if len(a)!=len(p):
                self.error()
            NewScope=Scope(self.scope)
            NewScope.var=dict(zip(p,a))
            itpt=Interpreter(b,NewScope)
            v,NewScope=itpt.visit_Block(b,1)
            v=preval(v)
            v=Interpreter(b,NewScope).visit(v)
            return v
        if type(self.visit(n.func))==Method:
            tp=Type(self.visit(n.func).instance,self)+" "+Types(a,self)
            func=self.visit(n.func).func.funcs[tp]
            p=[i.value for i in self.visit(func).para]
            b=self.visit(func).block
            if len(a)!=len(p)-1:
                self.error()
            NewScope=Scope(self.scope)
            NewScope.var=dict(zip(p[1:],a))
            NewScope.define(p[0],self.visit(n.func).instance)
            itpt=Interpreter(b,NewScope)
            v,NewScope=itpt.visit_Block(b,1)
            v=preval(v)
            v=Interpreter(b,NewScope).visit(v)
            return v
        p=[i.value for i in self.visit(n.func).para]
        b=self.visit(n.func).block
        a=[ConstValue(v,TYPE_DICT[type(v)]) for v in a]
        if len(a)!=len(p):
            self.error()
        NewScope=Scope(self.scope)
        NewScope.var=dict(zip(p,a))
        itpt=Interpreter(b,NewScope)
        v,NewScope=itpt.visit_Block(b,1)
        v=preval(v)
        v=Interpreter(b,NewScope).visit(v)
        return v
    def AssignStmt_help(self,item,index,value):
        l,r=self.visit(item),self.visit(index)
        v=self.visit(value)
        name="__SET_ITEM_INDEX__ "+Types([l,r,v],self)
        if "__SET_ITEM_INDEX__" in freebuiltinfunctions.keys():
            return freebuiltinfunctions["__SET_ITEM_INDEX__"](l,r,v)
        if name in builtinfunctions.keys():
            return builtinfunctions[name](l,r,v)
        a=[l,r,v]
        tp=Types(a,self)
        func=self.scope.find("__SET_ITEM_INDEX__").funcs[tp]
        p=[i.value for i in self.visit(func).para]
        b=self.visit(func).block
        NewScope=Scope(self.scope)
        NewScope.var=dict(zip(p,a))
        itpt=Interpreter(b,NewScope)
        v,NewScope=itpt.visit_Block(b,1)
        v=preval(v)
        v=Interpreter(b,NewScope).visit(v)
        return v
    def visit_AssignStmt(self,n):
        v=self.visit(n.value)
        if (type(n.name)==BinOp and n.name.op.value_type==ITEM_INDEX) or type(n.name)==DotOp:
            name=n.name
            indexs=[]
            while (type(name)==BinOp and name.op.value_type==ITEM_INDEX) or type(name)==DotOp:
                if type(name)==BinOp:
                    indexs.append(self.visit(name.right))
                else:
                    indexs.append(name.right)
                name=name.left
            if type(name)!=Var:
                self.error()
            def change(item,indexs,value):
                if indexs==[]:
                    return value
                if type(item)==ThisStruct:
                    item.var[indexs[0]]=change(item.var[indexs[0]],indexs[1:],value)
                else:
                    item[indexs[0]]=change(item[indexs[0]],indexs[1:],value)
                return item
            item=self.visit(name)
            item=change(item,indexs,v)
            self.scope.set(name.name,item)
        elif type(n.name)==Var:
            self.scope.set(n.name.name,ConstValue(v,TYPE_DICT[type(v)]))
        else:
            self.error()
    def visit_UnaryOp(self,n):
        r=self.visit(n.expr)
        name="__"+n.op+"__ "+Types([r],self)
        if "__"+n.op+"__" in freebuiltinfunctions.keys():
            return freebuiltinfunctions["__"+n.op+"__"](r)
        if name in builtinfunctions.keys():
            return builtinfunctions[name](r)
        a=[r]
        def preval(a):
            if type(a)==ReturnStmt:
                return preval(a.value)
            return a
        tp=Types(a,self)
        func=self.scope.find("__"+n.op+"__").funcs[tp]
        p=[i.value for i in self.visit(func).para]
        b=self.visit(func).block
        NewScope=Scope(self.scope)
        NewScope.var=dict(zip(p,a))
        itpt=Interpreter(b,NewScope)
        v,NewScope=itpt.visit_Block(b,1)
        v=preval(v)
        v=Interpreter(b,NewScope).visit(v)
        return v
        return {MINUS:lambda a:-a,NOT:lambda a:not a,BIT_NOT:lambda a:~a}[n.op](self.visit(n.expr))
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
    def visit_InitOp(self,n):
        name=n.name.value
        sv=self.scope.finds(name)
        return ThisStruct(name,dict(zip(sv.var,[None]*len(sv.var))))
    def visit_DotOp(self,n):
        v=self.visit(n.left).var[n.right]
        if type(v)==VarFunc:
            return Method(self.visit(n.left),v)
        return v
    def visit_ThreeEyeOp(self,n):
        if self.visit(n.cond):
            return self.visit(n.expr1)
        return self.visit(n.expr2)
    visit_ConstValue=lambda self,n:self.visit(n.value)
    visit_List=lambda self,n:[self.visit(i) for i in n.value]
    visit_Dict=lambda self,n:dict(zip([self.visit(i) for i in n.keys],[self.visit(i) for i in n.values]))
    visit_ItemIndex=lambda self,n:self.visit(n.item)[self.visit(n.index)]
    visit_NoOp=lambda self,n:None
    visit_list=lambda self,a:a
    visit_int=visit_list
    visit_str=visit_list
    visit_float=visit_list
    visit_NoneType=visit_list
    visit_range=visit_list
    visit_dict=visit_list
    visit_VarFunc=visit_list
    visit_ContinueStmt=visit_list
    visit_ReturnStmt=visit_list
    visit_BreakStmt=visit_list
    visit_Func=visit_list
    visit_ThisStruct=visit_list
    visit_Local=lambda self,n:n.value
    visit_StructStmt=lambda self,n:self.scope.defines(n.name.value,Struct(n.name,n.var))
    def interprete(self):
        ans=self.visit(self.tree)
        return ans
t=""
print('''     integer3-    3-.0.1版本
更新内容：三目运算''')
print("可以写代码了，end结束")
while 1:
    a=input()
    if a=="end":
        break
    t+="\n"+a
print("\n\033[1;33m代码运行开始\033[1;0m")
Interpreter(Parser(Lexer(t)).block()).interprete()
print("\n\033[1;33m代码运行结束\033[1;0m")
'''
integer3-
C站Python区图灵完备自创编程语言

1、图灵完备？
应该差不多
2、语法比较正常？
除了结构体和函数都挺正常
3、动态类型？静态类型？
动态类型
4、强类型？弱类型？
强类型
5、比较好用？
比较好用
6、有标准库？
暂时没有
7、有缺陷？
有
'''
'''
{
    var prime=func(int a){
        if a<2 return 0;
        for var i=2;i<=sqrt(a);i=i+1 if a%i==0 return 0;
        return 1;
    };
    print(prime(2));
}

{
    //struct演示
    struct A{
        a
        b
    };
    var a=init A;
    a.a=10;
    a.b=20;
    print(a.a+a.b);//30
}

{
    //list演示
    var list1=[1,2,2];
    list1[2]=3;
    print(list1);//[1,2,3]
}
'''