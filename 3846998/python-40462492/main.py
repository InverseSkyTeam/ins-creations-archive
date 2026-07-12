from copy import deepcopy
import os,sys
class Tree:
    def __init__(self,tp,*v):
        self.tp,self.v=tp,v
    def __getitem__(self,n):
        return self.v[n]
    def __eq__(self,b):
        return self.tp==b.tp and self.v==b.v
    def __ne__(self,b):
        return self.tp!=b.tp or self.v!=b.v
    def __str__(self):
        return "{}({})".format(self.tp,",".join(map(str,self.v)))
    def __repr__(self):
        return "{}({})".format(self.tp,",".join(map(str,self.v)))
class Scope:
    def __init__(self,parent,v={}):
        self.parent=parent
        self.var=v
    def define(self,n,v):
        self.var[n]=v
    def find(self,n):
        if n in self.var:
            return self.var[n]
        if self.parent!=None:
            return self.parent.find(n)
        raise Exception(f"未定义的变量'{n}'")
    def set(self,n,v,tp=0):
        if n in self.var:
            if not tp:
                self.var[n].v=v.v
            else:
                self.var[n]=v
            return
        if self.parent!=None:
            return self.parent.set(n,v,tp)
        raise Exception(f"未定义的变量'{n}'")
class Value:
    def __init__(self,v):
        self.v=v
    __repr__=__str__=lambda self:str(self.v)
class Func:
    def __init__(self,parat,para,rtype,body,closure,args=[]):
        self.parat,self.para,self.rtype,self.body,self.closure,self.args=parat,para,rtype,body,closure,args
    def call(self,args):
        for i in range(min(len(self.para)-len(self.args),len(args))):
            if self.parat[i+len(self.args)]=="val":
                args[i]=deepcopy(args[i])
        if len(self.args+args)!=len(self.para):
            return Value(Func(self.parat,self.para,self.rtype,self.body,self.closure,self.args+args))
        scope=Scope(self.closure,dict(zip(self.para,self.args+args)))
        v=run_code(self.body[0],scope)
        if v==None:
            return Value(None)
        if self.rtype=="val":
            return deepcopy(v.v)
        return v.v
    def filled(self,args):
        return Func(self.parat,self.para,self.rtype,self.body,self.closure,self.args+args)
    __str__=__repr__=lambda self:f"(fn: para:{self.para} filled:{self.args} body:{self.body})"
class Return:
    def __init__(self,v):
        self.v=v
class Break:
    pass
class Continue:
    pass
class Type:
    def __init__(self,extend,attr):
        self.extend,self.attr=extend,attr
    def allattr(self):
        res={}
        for i in self.extend:
            r=i.v.allattr()
            for k,v in r.items():
                res[k]=v
        for k,v in self.attr.items():
            res[k]=v
        res["$type"]=Value(self)
        return res
    def getattr(self,name):
        return self.attr[name]
    def setattr(self,name,value):
        self.attr[name]=value
    __str__=__repr__=lambda self:f"(type: extend:{self.extend} attr:{self.attr})"
class Object:
    def __init__(self,attr):
        self.attr=attr
    def getattr(self,name):
        n=self.attr[name]
        if type(n.v)==Func:
            return Value(n.v.filled([Value(self)]))
        return n
    def setattr(self,name,value):
        self.attr[name]=value
    def __call__(self,*args):
        return self.getattr("$call").v.call(list(args))
    __str__=__repr__=lambda self:f"(obj:{self.attr})"
class Module:
    def __init__(self,attr):
        self.attr=attr
    def getattr(self,name):
        return self.attr[name]
    def setattr(self,name,value):
        self.attr[name]=value
    __str__=__repr__=lambda self:f"(module: attr:{self.attr})"
def lex(code:str):
    op=[
        '+','-','*','/','%',
        '==','!=','>=','<=','>','<',
        '<<','>>',
        '&&','||','&','|','^',
        '!','~',
        '=','&=',
        ',',';',':','.',
        '(',')','[',']','{','}',
    ]
    res=[]
    while code:
        while code and (code[0] in "\n \t\r" or code[:2] in ("//",'/*')):
            if code[0] in "\n \t\r":
                code=code[1:]
            elif code[:2]=="//":
                code=code[2:]
                while code and code[0]!="\n":
                    code=code[1:]
                code=code[1:]
            elif code[:2]=='/*':
                code=code[2:]
                while code and code[:2]!='*/':
                    code=code[1:]
                code=code[2:]
        if code=="":
            break
        if code[0].isdigit() or code[0]=='.':
            s=""
            while code and code[0].isdigit() or code[0]=='.':
                s+=code[0]
                code=code[1:]
            res.append(s)
        elif code[0]=='"':
            code=code[1:]
            s='"'
            while code and code[0]!='"':
                if code[0]=='\\':
                    code=code[1:]
                    if code[0].isdigit():
                        s+=int(code[0:3],base=8)
                        code=code[1:]
                    else:
                        s+={
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
                        }[code[0]]
                        code=code[1:]
                else:
                    s+=code[0]
                    code=code[1:]
            code=code[1:]
            s+='"'
            res.append(s)
        elif code[0].isalpha() or code[0] in "$_":
            s=""
            while code and (code[0].isalnum() or code[0] in "$_"):
                s+=code[0]
                code=code[1:]
            res.append(s)
        else:
            r=""
            for i in op:
                if code[:len(i)]==i and len(i)>=len(r):
                    r=i
            if r=="":
                raise Exception("词法分析错误")
            code=code[len(r):]
            res.append(r)
    return res+[""]
def parse(code):
    lst=["if","while","func","class","module","for","foreach"]
    tk=code
    if type(tk)==str:
        tk=lex(tk)
    def eat(ex=None):
        nonlocal tk
        if ex==None or tk[0]==ex:
            a=tk[0]
            tk=tk[1:]
            return a
        raise Exception(f"语法分析错误 {tk[0]},{ex}")
    def match(*ex):
        return tk[0] in ex
    def block():
        if tk[0]!='{':
            s=stmt()
            if s.tp not in lst:
                eat(';')
            return Tree("block",[s])
        s=[]
        eat("{")
        while tk[0]!="}":
            s.append(stmt())
            if s[-1].tp not in lst:
                eat(';')
        eat('}')
        return Tree("block",s)
    def stmt():
        if tk[0]=="var":
            eat()
            names=[eat()]
            values=[Tree("value",None)]
            assign_way=["val"]
            if tk[0]=='=':
                eat()
                values[-1]=expr()
            elif tk[0]=="&=":
                eat()
                values[-1]=expr()
                assign_way[-1]="ref"
            while tk[0]==',':
                eat()
                names.append(eat())
                values.append(Tree("value",None))
                assign_way.append("val")
                if tk[0]=='=':
                    eat()
                    values[-1]=expr()
                elif tk[0]=="&=":
                    eat()
                    values[-1]=expr()
                    assign_way[-1]="ref"
            return Tree("var",names,values,assign_way)
        if tk[0]=='if':
            eat()
            eat('(')
            cond=parse_tuple()
            eat(')')
            body=block()
            if tk[0]=='else':
                eat()
                return Tree("if",cond,body,block())
            return Tree("if",cond,body,Tree("noop"))
        if tk[0]=="while":
            eat()
            eat("(")
            cond=parse_tuple()
            eat(")")
            return Tree("while",cond,block())
        if tk[0]=="func":
            eat()
            name=eat()
            eat('(')
            para=[]
            parat=[]
            if tk[0]!=')':
                if tk[0]=='&':
                    eat()
                    parat.append("ref")
                else:
                    parat.append("val")
                para.append(eat())
                while tk[0]==',':
                    eat()    
                    if tk[0]=='&':
                        eat()
                        parat.append("ref")
                    else:
                        parat.append("val")
                    para.append(eat())
            eat(')')
            rtype="val"
            if tk[0]=='&':
                eat()
                rtype="ref"
            return Tree("func",name,parat,para,rtype,block())
        if tk[0] in ("break","continue"):
            return Tree(eat())
        if tk[0]=="return":
            return Tree(eat(),expr())
        if tk[0]=="class":
            eat()
            name=eat()
            extend=[]
            if tk[0]=="extends":
                eat()
                extend.append(expr())
                while tk[0]==",":
                    eat()
                    extend.append(expr())
            return Tree("class",name,extend,block())
        if tk[0]=="module":
            eat()
            name=eat()
            return Tree("module",name,block())
        if tk[0]=="import":
            eat()
            return Tree("import",expr())
        if tk[0]=="load":
            eat()
            return Tree("load",expr())
        '''if tk[0]=="for":
            eat()
            eat('(')

            eat(')')'''
        e=parse_tuple()
        if tk[0]=='=':
            eat()
            v=parse_tuple()
            if e.tp!='tuple':
                e=[e]
                v=[v]
            else:
                e=e[0]
                v=v[0]
            return Tree("assign",e,v)
        if tk[0]=='&=':
            eat()
            v=parse_tuple()
            if e.tp!='tuple':
                e=[e]
                v=[v]
            else:
                e=e[0]
                v=v[0]
            return Tree("ref assign",e,v)
        return e
    def parse_tuple():
        v=expr()
        if tk[0]==',':
            eat()
            if tk[0] in ('=',')',';','&='):
                return Tree("tuple",[v])
            v=[v,expr()]
            while tk[0]==',':
                eat()
                v.append(expr())
            return Tree("tuple",v)
        return v
    def expr():
        res=expr4()
        while match('&&','||'):
            res=Tree("binary",eat(),res,expr4())
        return res
    def expr4():
        res=expr3()
        while match('&','|','^'):
            res=Tree("binary",eat(),res,expr3())
        return res
    def expr3():
        res=expr2()
        while match('==','!=','>=','<=','>','<'):
            res=Tree("binary",eat(),res,expr2())
        return res
    def expr2():
        res=expr1()
        while match('<<','>>'):
            res=Tree("binary",eat(),res,expr1())
        return res
    def expr1():
        res=term()
        while match('+','-'):
            res=Tree("binary",eat(),res,term())
        return res
    def term():
        res=factor()
        while match('*','/','%'):
            res=Tree("binary",eat(),res,factor())
        return res
    def factor():
        if tk[0]=='.':
            eat()
            return fh(Tree("nth",Tree("id","$"),Tree("value",eat())))
        if tk[0]=='lambda':
            eat()
            eat('(')
            para=[]
            parat=[]
            if tk[0]!=')':
                if tk[0]=='&':
                    eat()
                    parat.append("ref")
                else:
                    parat.append("val")
                para.append(eat())
                while tk[0]==',':
                    eat()    
                    if tk[0]=='&':
                        eat()
                        parat.append("ref")
                    else:
                        parat.append("val")
                    para.append(eat())
            eat(')')
            rtype="val"
            if tk[0]=='&':
                eat()
                rtype="ref"
            return fh(Tree("lambda",parat,para,rtype,block()))
        if tk[0]=='[':
            eat()
            v=[]
            if tk[0]!=']':
                v.append(expr())
                while tk[0]==',':
                    eat()
                    v.append(expr())
            eat(']')
            return Tree("list",v)
        if tk[0]=="True":
            return fh(Tree("value",True))
        if tk[0]=="False":
            return fh(Tree("value",False))
        if tk[0]=="None":
            return fh(Tree("value",None))
        if tk[0][0].isdigit() or tk[0][0]=='.':
            if '.' in tk[0]:
                return fh(Tree("value",float(eat())))
            return fh(Tree("value",int(eat())))
        if tk[0][0]=='"':
            return fh(Tree("value",eat()[1:-1]))
        if tk[0]=='(':
            eat()
            e=parse_tuple()
            eat(")")
            return fh(e)
        if match('+','-','!','~'):
            return Tree("unary",eat(),factor())
        if tk[0][0].isalpha() or tk[0][0] in '$_':
            return fh(Tree("id",eat()))
        raise Exception(f"语法分析错误 {tk[0]}")
    def fh(v):
        if tk[0]=='[':
            eat()
            idx=expr()
            eat(']')
            return fh(Tree("nth",v,idx))
        if tk[0]=='.':
            eat()
            return fh(Tree("nth",v,Tree("value",eat())))
        if tk[0]=='(':
            eat()
            args=[]
            if tk[0]!=')':
                args=[expr()]
                while tk[0]==',':
                    eat()
                    args.append(expr())
            eat(')')
            return fh(Tree("call",v,args))
        return v
    l=[]
    while tk[0]!="":
        l.append(stmt())
        if l[-1].tp not in lst:
            eat(';')
    return l
def run_code(t,s=Scope(None)):
    binary_dict={
        "+":lambda a,b:a+b,
        "-":lambda a,b:a-b,
        "*":lambda a,b:a*b,
        "/":lambda a,b:a/b,
        "%":lambda a,b:a%b,
        "==":lambda a,b:a==b,
        "!=":lambda a,b:a!=b,
        ">":lambda a,b:a>b,
        "<":lambda a,b:a<b,
        "<<":lambda a,b:a<<b,
        ">>":lambda a,b:a>>b,
        "&&":lambda a,b:a and b,
        "||":lambda a,b:a or b,
        "&":lambda a,b:a&b,
        "|":lambda a,b:a|b,
        "^":lambda a,b:a^b
    }
    unary_dict={
        "+":lambda a:+a,
        "-":lambda a:-a,
        "!":lambda a:not a,
        "~":lambda a:~a
    }
    tree=t
    if type(tree)!=list:
        tree=parse(tree)
    scope=s
    def assign(a:Tree,to,tp=0):
        nonlocal scope
        idx=[]
        while a.tp=="nth":
            if a.tp=="nth":
                idx=[run(a[1])]+idx
                a=a[0]
            else:
                raise Exception("运行错误")
        b=run(a)
        #name=a[0]
        def w(a,idx,to):
            if idx==[]:
                return to
            if type(a.v)!=Object:
                a.v[idx[0].v]=w(a.v[idx[0].v],idx[1:],to)
            else:
                a.v.setattr(idx[0].v,w(a.v.getattr(idx[0].v),idx[1:],to))
            return a
        b.v=w(b,idx,to).v
        #scope.set(name,w(run(a),idx,to))
    def run(tree:Tree)->Value:
        nonlocal scope
        tp=tree.tp
        if tp=="value":
            return Value(tree[0])
        elif tp=="id":
            return scope.find(tree[0])
        elif tp=="binary":
            l,r=run(tree[1]),run(tree[2])
            if type(l.v)==Object or type(r.v)==Object:
                d={
                    '+':"add",
                    '-':'sub',
                    '*':'mul',
                    '/':'div',
                    '%':'mod',
                    '==':'eq',
                    '!=':'ne',
                    '>':'gt',
                    '<':'lt',
                    '>=':'ge',
                    '<=':'le',
                    '<<':'lshift',
                    '>>':'rshift',
                    '&&':'and',
                    '||':'or',
                    '&':'bitand',
                    '|':'bitor',
                    '^':'xor'
                }
                if type(l.v)==Object:
                    return l.v.getattr('$'+d[tree[0]]).v.call([r])
                else:
                    return r.v.getattr('$r'+d[tree[0]]).v.call([l])
            return Value(binary_dict[tree[0]](l.v,r.v))
        elif tp=="unary":
            v=run(tree[1])
            if type(v.v)==Object:
                d={
                    '+':'positive',
                    '-':'negative',
                    '!':'not',
                    '~':'invert'
                }
                return v.v.getattr('$'+d[tree[0]]).v.call([])
            return Value(unary_dict[tree[0]](v.v))
        elif tp=="call":
            fn=run(tree[0]).v
            if type(fn)==Func:
                return fn.call([run(i) for i in tree[1]])
            if callable(fn):
                if type(fn)==Object:
                    return fn(*[run(i) for i in tree[1]])
                return Value(fn(*[run(i).v for i in tree[1]]))
            if type(fn)==Type:
                obj=Value(Object(fn.allattr()))
                fn=obj.v.getattr("$init").v
                fn.call([run(i) for i in tree[1]])
                return obj
        elif tp=="nth":
            v=run(tree[0])
            if type(v)==Object:
                return v.v.getattr(run(tree[1]).v)
            return v.v.getattr(run(tree[1]).v)
        elif tp=="var":
            for i in range(len(tree[0])):
                if tree[2][i]=="ref":
                    scope.define(tree[0][i],run(tree[1][i]))
                else:
                    scope.define(tree[0][i],deepcopy(run(tree[1][i])))
        elif tp=="if":
            if run(tree[0]).v:
                return run(tree[1])
            return run(tree[2])
        elif tp=="while":
            while run(tree[0]).v:
                v=run(tree[1])
                if type(v)==Return:
                    return v
                if type(v)==Break:
                    break
        elif tp=="block":
            scope=Scope(scope)
            for i in tree[0]:
                v=run(i)
                if type(v) in (Break,Continue,Return):
                    scope=scope.parent
                    return v
            scope=scope.parent
        elif tp=="tuple":
            return Value(tuple(run(i) for i in tree[0]))
        elif tp=="list":
            return Value([run(i) for i in tree[0]])
        elif tp=="func":
            scope.define(tree[0],Value(Func(tree[1],tree[2],tree[3],tree[4],scope)))
        elif tp=="lambda":
            return Value(Func(tree[0],tree[1],tree[2],tree[3],scope))
        elif tp=="break":
            return Break()
        elif tp=="continue":
            return Continue()
        elif tp=="return":
            return Return(run(tree[0]))
        elif tp=="assign":
            for i in range(len(tree[0])):
                assign(tree[0][i],deepcopy(run(tree[1][i])))
        elif tp=="ref assign":
            for i in range(len(tree[0])):
                assign(tree[0][i],run(tree[1][i]),1)
        elif tp=="class":
            name,extend,body=tree.v
            scope=Scope(scope)
            for i in body[0]:
                run(i)
            attr=scope.var
            scope=scope.parent
            attr["$name"]=Value(name)
            scope.define(name,Value(Type([run(i) for i in extend],attr)))
        elif tp=="module":
            name,body=tree.v
            scope=Scope(scope)
            for i in body[0]:
                run(i)
            attr=scope.var
            scope=scope.parent
            attr["$name"]=Value(name)
            scope.define(name,Value(Module(attr)))
        elif tp=="import":
            v=run(tree[0]).v.attr
            for k,v in v.items():
                scope.define(k,v)
        elif tp=="load":
            name=run(tree[0]).v
            text=""
            with open(name,"r") as f:
                text="\n".join(f.readlines())
            run_code(text,scope)
        else:
            raise Exception(f"无法识别的语法树类型{tp}")
    for i in tree:
        v=run(i)
        if type(v) in (Break,Continue,Return):
            return v
run_code('''
class T{
    var a=0;
    func $init($,n){
        .a=n;
    }
    func $add($,b){
        return T(.a+b.a);
    }
    func $negative($){
        return T(-.a);
    }
}
println((T(1)+T(2)).a);
println(-T(1).a);
''',Scope(None,{
    "println":Value(lambda *args:print(*args,sep="")),
    "print":Value(lambda *args:print(*args,sep="",end="")),
    "readln":Value(input),
    "ord":Value(ord),
    "chr":Value(ord),
    "getchar":Value(lambda:sys.stdin.read(1)),
    "len":Value(len),
    "system":Value(os.system),
}))
'''
var a=0;
var b&=a;
println(a);

func ref(&a)&{
    return a;
}
var a=0;
ref(a)=10;
println(a);

func refnth(&obj,n)&{
    return obj[n];
}
var a=[1,2,2];
refnth(a,2)=3;
println(a);

class T{
    func $init($){}
    var a=0;
}
println(T()["a"]);
println(T().a);//效果一样

module M{
    var pi=3.14;
}
println(M.pi);
import M;
println(pi);
'''