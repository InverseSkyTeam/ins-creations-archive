EOF,ADD,SUB,MUL,DIV,MOD,EQ,NE,GT,LT,GE,LE,LSHIFT,RSHIFT,AND,OR,BITAND,BITOR,XOR,NOT,INV,INT,FLOAT,BOOL,NONE,STRING,ID,LPAREN,RPAREN,KW_print,KW_if,KW_else,KW_while,KW_func,KW_var,KW_class,KW_public,KW_private,KW_protected,KW_return,COMMA,ASSIGN,BEGIN,END,BEGINL,ENDL,SEMI,COLON,DOT=[i for i in range(-1,48)]
int_string_mp=dict(zip([EOF,ADD,SUB,MUL,DIV,MOD,EQ,NE,GT,LT,GE,LE,LSHIFT,RSHIFT,AND,OR,BITAND,BITOR,XOR,NOT,INV,INT,FLOAT,BOOL,NONE,STRING,ID,LPAREN,RPAREN,KW_print,KW_if,KW_else,KW_while,KW_func,KW_var,KW_class,KW_public,KW_private,KW_protected,KW_return,COMMA,ASSIGN,BEGIN,END,BEGINL,ENDL,SEMI,COLON,DOT],"EOF,ADD,SUB,MUL,DIV,MOD,EQ,NE,GT,LT,GE,LE,LSHIFT,RSHIFT,AND,OR,BITAND,BITOR,XOR,NOT,INV,INT,FLOAT,BOOL,NONE,STRING,ID,LPAREN,RPAREN,KW_print,KW_if,KW_else,KW_while,KW_func,KW_var,KW_class,KW_public,KW_private,KW_protected,KW_return,COMMA,ASSIGN,BEGIN,END,BEGINL,ENDL,SEMI,COLON,DOT".split(",")))
class Token:
    def __init__(self,t,v=None):
        self.t=t
        self.v=v
    def __str__(self):
        return f"Token({int_string_mp[self.t]},{self.v})"
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
    '[':BEGINL,
    ']':ENDL,
    ';':SEMI,
    ':':COLON,
    '.':DOT,
}
keyword_int_dict={
    #"print":Token(KW_print),
    "if":Token(KW_if),
    "else":Token(KW_else),
    "while":Token(KW_while),
    "func":Token(KW_func),
    "var":Token(KW_var),
    "True":Token(BOOL,True),
    "False":Token(BOOL,False),
    "None":Token(NONE,None),
    "class":Token(KW_class),
    "public":Token(KW_public),
    "private":Token(KW_private),
    "protected":Token(KW_protected),
    "return":Token(KW_return),
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
    def getall(self):
        l=[]
        while 1:
            l.append(self.get())
            if l[-1].t==EOF:
                return l
class BinOp:
    def __init__(self,op,l,r):
        self.op=op
        self.l=l
        self.r=r
class Element:
    def __init__(self,l,r):
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
class MemberOp:
    def __init__(self,l,r,_=None):
        self.l=l
        self.r=r
class Var:
    def __init__(self,i):
        self.id=i
class List:
    def __init__(self,l):
        self.l=l
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
class Func:
    def __init__(self,args,block):
        self.a=args
        self.b=block
class WhileStmt:
    def __init__(self,cond,block):
        self.c,self.b=cond,block
class IfStmt:
    def __init__(self,cond,block):
        self.c,self.b=cond,block
class ReturnStmt:
    def __init__(self,i):
        self.i=i
class Class:
    def __init__(self,name,attrs,attrtype,parents=[]):
        self.name=name
        self.attrs=attrs
        self.attrtype=attrtype
        self.parents=parents
class ClassDecl:
    def __init__(self,name,l1,l2,parents=[]):
        self.name=name
        self.l1=l1
        self.l2=l2
        self.parents=parents
class Object:
    def __init__(self,name,attrs,attrtype):
        self.name=name
        self.attrs=attrs
        self.attrtype=attrtype
class CallFunc:
    def __init__(self,func,args):
        self.f=func
        self.a=args
class CallMemberFunc:
    def __init__(self,f,args):
        self.f=f
        self.args=args
class Parser:
    def __init__(self,l):
        self.l=l
        self.tk=self.l.get()
        self.TP_table=[]
    def eat(self,tp=-1):
        t=self.tk
        if tp!=-1 and t.t!=tp:
            raise Exception("Wrong input!Expected "+int_string_mp[tp]+".Got "+int_string_mp[t.t]+".")
        self.tk=self.l.get()
        return t
    def var(self):
        return Var(self.eat(ID).v)
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
        if self.tk.t==BEGINL:
            self.eat()
            e=self.expr()
            self.eat(ENDL)
            return self.fh(Element(v,e))
        if self.tk.t==DOT:
            self.eat()
            n=self.eat(ID).v
            if self.tk.t==LPAREN:
                self.eat()
                l=[]
                if self.tk.t!=RPAREN:
                    l=[self.expr()]
                    while self.tk.t==COMMA:
                        self.eat()
                        l.append(self.expr())
                self.eat(RPAREN)
                return self.fh(CallMemberFunc(MemberOp(v,n),l))
            return self.fh(MemberOp(v,n))
        return v
    def factor(self):
        if self.tk.t==KW_func:
            self.eat()
            self.eat(LPAREN)
            l=[]
            if self.tk.t!=RPAREN:
                l=[self.eat(ID).v]
                while self.tk.t==COMMA:
                    self.eat()
                    l.append(self.eat(ID).v)
            self.eat(RPAREN)
            self.eat(BEGIN)
            b=self.stmts()
            self.eat(END)
            return self.fh(Func(l,b))
        if self.tk.t==BEGINL:
            self.eat()
            if self.tk.t==ENDL:
                self.eat()
                return []
            l=[self.expr()]
            while self.tk.t==COMMA:
                self.eat()
                l.append(self.expr())
            self.eat(ENDL)
            return self.fh(List(l))
        if self.tk.t==LPAREN:
            self.eat()
            t=self.expr()
            self.eat(RPAREN)
            return self.fh(t)
        if self.tk.t==ID:
            return self.fh(self.var())
        if self.tk.t in (INT,FLOAT,BOOL,NONE,STRING):
            ret=self.eat()
            return ret.v
        if self.tk.t in (ADD,SUB,NOT,INV):
            return UnaryOp(self.eat().t,self.fh(self.factor()))
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
    def classStmts(self):
        l1=[]
        l2={}
        while self.tk.t!=EOF and self.tk.t!=END:
            tp=0
            if self.tk.t in (KW_public,KW_private,KW_protected):
                tp=self.eat().t
            else:
                tp=KW_public
            l1.append(self.stmt())
            if type(l1[-1]) not in (VarDecl,ClassDecl):
                raise Exception("Wrong input!")
            if type(l1[-1])==VarDecl:
                dic=dict(zip(l1[-1].ns,[tp for i in range(len(l1[-1].ns))]))
                for i,j in dic.items():
                    l2[i]=j
            else:
                l2[l1[-1].name]=tp
        return l1,l2
    def stmt(self):
        if self.tk.t==KW_class:
            self.eat()
            n=self.eat(ID).v
            ps=[]
            if self.tk.t==COLON:
                self.eat()
                ps=[self.var()]
                while self.tk.t==COMMA:
                    self.eat()
                    ps.append(self.var())
            self.eat(BEGIN)
            body=self.classStmts()
            self.eat(END)
            return ClassDecl(n,*body,ps)
        if self.tk.t==KW_func:
            self.eat()
            n=self.eat(ID).v
            self.eat(LPAREN)
            l=[]
            if self.tk.t!=RPAREN:
                l=[self.eat(ID).v]
                while self.tk.t==COMMA:
                    self.eat()
                    l.append(self.eat(ID).v)
            self.eat(RPAREN)
            self.eat(BEGIN)
            b=self.stmts()
            self.eat(END)
            return VarDecl([n],[Func(l,b)])
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
        '''if self.tk.t==KW_print:
            self.eat()
            return PrintStmt(self.expr())'''
        if self.tk.t==KW_return:
            self.eat()
            return ReturnStmt(self.expr())
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
builtinfunc={
    "ord":lambda a:ord(a),
    "chr":lambda a:chr(a),
    "input":input,
    "print":lambda *l:print(*l,end="",sep=""),
    "println":lambda *l:print(*l,sep=""),
    "len":len,
    "substr":lambda st,s,e:st[s:e],
    "stoi":int,
    "stod":float,
}
class Interpreter:
    def visit(self,node):
        method_name="visit_"+type(node).__name__
        visitor=getattr(self,method_name,self.generic_visit)
        return visitor(node)
    def generic_visit(self,node):
        raise Exception("Can't find method\"visit_{}()\"".format(type(node).__name__))
    def __init__(self,ast,scope=Scope(None),className=""):
        self.ast=ast
        self.scope=scope
        self.className=className
    def visit_BinOp(self,bo):
        return binop_fun_dict[bo.op](self.visit(bo.l),self.visit(bo.r))
    def visit_UnaryOp(self,bo):
        return unaryop_fun_dict[bo.op](self.visit(bo.l))
    def visit_Stmts(self,v):
        for i in v.l:
            tmp=self.visit(i)
            if type(tmp)==ReturnStmt:
                return tmp
    def visit_PrintStmt(self,v):
        print(self.visit(v.i))
    def visit_VarDecl(self,t):
        for i in range(len(t.ns)):
            self.scope.define(t.ns[i],self.visit(t.vs[i]))
    def visit_Var(self,t):
        return self.scope.find(t.id)
    def visit_WhileStmt(self,t):
        while self.visit(t.c):
            tmp=Interpreter(t.b,Scope(self.scope)).interprete()
            if type(tmp)==ReturnStmt:
                return tmp
    def visit_IfStmt(self,t):
        if self.visit(t.c):
            return Interpreter(t.b,Scope(self.scope)).interprete()
    def visit_Assign(self,t):
        val=self.visit(t.r)
        if type(t.l) in (Element,MemberOp):
            t=t.l
            l=[]
            while type(t) in (Element,MemberOp):
                if type(t)==Element:
                    l=[self.visit(t.r)]+l
                else:
                    l=[t.r]+l
                t=t.l
            if type(t)!=Var:
                raise Exception("Wrong input!")
            n=t.id
            def f(_l,l,v,idx):
                if idx==[]:
                    return v
                if type(l)==list:
                    l[idx[0]]=f(Element(_l,idx[0]),l[idx[0]],v,idx[1:])
                elif type(l)==Object:
                    if (l.attrtype[idx[0]]!=KW_public and self.className!=l.name) or (type(_l)!=Var or _l.id!="this"):
                        raise Exception("Wrong input!")
                    l.attrs[idx[0]]=f(MemberOp(_l,idx[0]),l.attrs[idx[0]],v,idx[1:])
                return l
            self.scope.set(n,f(t,self.visit(t),val,l))
            return
        if type(t.l)!=Var:
            raise Exception("Wrong input!")
        self.scope.set(t.l.id,val)
    def getAttrs(self,tp):
        mp=tp.attrs
        l=tp.attrtype
        for w in tp.parents:
            for i,j in getAttrs(w)[0].items():
                if i not in mp.keys():
                    mp[i]=j
            l.extend(getAttrs(w)[1])
        return mp,l
    def easyObject(self,tp):
        return Object(tp.name,*self.getAttrs(tp))
    def newObject(self,f,args,name):
        ni=Interpreter(f.b,Scope(self.scope),name)
        ni.scope.var=dict(zip(f.a,args))
        ni.scope.var["this"]=self.easyObject(self.scope.find(name))
        ni.interprete()
        return ni.visit(Var("this"))
    def visit_CallFunc(self,t):
        if type(t.f)==Var and t.f.id in builtinfunc.keys():
            return builtinfunc[t.f.id](*[self.visit(i) for i in t.a])
        if type(t.f)==Var and type(self.visit(t.f))==Class:
            f=self.visit(t.f)
            if f.attrtype["__init__"]!=KW_public and self.className!=t.f.id:
                raise Exception("Wrong input!")
            return self.newObject(f.attrs["__init__"],[self.visit(i) for i in t.a],t.f.id)
        ns=Scope(self.scope)
        ns.var=dict(zip(self.visit(t.f).a,[self.visit(i) for i in t.a]))
        try:
            return Interpreter(self.visit(t.f).b,ns).interprete().i
        except:
            return None
    def visit_ClassDecl(self,t):
        name=t.name
        parents=[self.visit(i) for i in t.parents]
        attrtype=t.l2
        ni=Interpreter(Stmts(t.l1),Scope(self.scope))
        ni.interprete()
        attrs=ni.scope.var
        self.scope.define(name,Class(name,attrs,attrtype,parents))
    def visit_MemberOp(self,t):
        obj=self.visit(t.l)
        if obj.attrtype[t.r]!=KW_public and self.className!=obj.name:
            raise Exception("Wrong input!")
        return obj.attrs[t.r]
    def visit_CallMemberFunc(self,t):
        f=self.visit(t.f)
        base=self.visit(t.f.l)
        a=[self.visit(i) for i in t.args]
        ni=Interpreter(f.b,Scope(self.scope),base.name)
        ni.scope.var=dict(zip(f.a,a))
        ni.scope.var["this"]=base
        tmp=ni.interprete()
        try:
            self.visit(Assign(t.f.l,ni.scope.var["this"]))
        except:
            pass
        return tmp.i
    visit_int=lambda self,a:a
    visit_float=lambda self,a:a
    visit_NoneType=lambda self,a:a
    visit_bool=lambda self,a:a
    visit_list=lambda self,a:a
    visit_Func=lambda self,a:a
    visit_List=lambda self,a:[self.visit(i) for i in a.l]
    visit_Element=lambda self,a:self.visit(a.l)[self.visit(a.r)]
    visit_str=lambda self,a:a
    visit_ReturnStmt=lambda self,a:ReturnStmt(self.visit(a.i))
    def interprete(self):
        return self.visit(self.ast)
Interpreter(Parser(Lexer('''
/*
这是用integer3.1.0预告版实现的BrainFuck
*/
/*class GetChar{
    var line=""
    func __init__(){}
    func get(){
        if(this.line==""){
            this.line=input()+chr(10)
        }
        var tmp=ord(this.line[0])
        this.line=substr(this.line,1,None)
        return tmp
    }
}
var code,x=0,mem=[],p=128,getc=GetChar(),flag=0
func getpair(text,pos){
    var l=1,r=0,_p=pos
    while(_p<len(text)){
        _p=_p+1
        println(_p)
        if(text[i]=="["){l=l+1}
        if(i=="]"){
            r=r+1
            if(l>0){
                r=r-1
                l=r-1
            }
        }
        if(l==0&&r==0){return _p}
    }
}
func BF(){
    var pc=0
    while(pc<len(code)){
        flag=0
        if(code[pc]=="!"){print(mem[p])}
        if(code[pc]=="."){print(chr(mem[p]))}
        if(code[pc]==","){mem[p]=getc.get()}
        if(code[pc]=="+"){mem[p]=mem[p]+1}
        if(code[pc]=="-"){mem[p]=mem[p]-1}
        if(code[pc]=="<"){p=p-1}
        if(code[pc]==">"){p=p+1}
        if(code[pc]=="["){
            flag=1
            println(pc+1,",",getpair(code,pc))
            while(mem[p]){BF(substr(code,pc+1,getpair(code,pc)))}
            pc=getpair(code,pc)+1
        }
        if(flag==0&&code[pc]=="]"){return 0}
        if(flag==0){pc=pc+1}
    }
}
func main(){
    var i=0
    while(i<256){
        mem=mem+[0]
        i=i+1
    }
    code=input(">>>")
    BF(code)
}
main()*/
println("本来想用这个写一个BrainFuck解释器的，结果没写成")
println("所以就写了一个判断质数")
println("请输入一个数：")
var a=stoi(input()),flag=True,i=2
if(a<2){
    flag=False
}
while(i<a&&flag){
    if(a%i==0){
        flag=False
    }
    i=i+1
}
if(flag){
    println("是质数")
}
if(!flag){
    println("不是质数")
}
''')).parse()).interprete()