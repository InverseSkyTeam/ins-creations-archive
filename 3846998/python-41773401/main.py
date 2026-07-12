import sys
import os
class NewLangFatalError(Exception):
    ...
def lex(code:str):
    p=0
    res=[]
    kw=[
        "if",
        "else",
        "while",
        "for",
        "let",
        "class",
        "module",
        "import",
        "return",
        "break",
        "continue",
        "True",
        "False",
        "None",
    ]
    op=[
        '+','-','*','/','%',
        '==','!=','>','<','>=','<=',
        '<<','>>',
        "&&",'||','&','|','^',
        '!','~',
        '(',')','[',']','{','}',
        ',','.',';','!!','=',
    ]
    while p<len(code):
        while p<len(code) and (code[p] in " \n\t" or code[p:p+2] in ("//","/*")):
            if code[p] in " \n\t":
                p+=1
            elif code[p:p+2]=="//":
                p+=2
                while p<len(code) and code[p]!="\n":
                    p+=1
            else:
                p+=2
                while p<len(code) and code[p:p+2]!="*/":
                    p+=1
                if p==len(code):
                    raise NewLangFatalError("未结束的注释")
                p+=2
        if p==len(code):
            break
        if code[p].isdigit():
            s=""
            while p<len(code) and (code[p].isdigit() or code[p]=='.'):
                s+=code[p]
                p+=1
            if s.count('.')>1:
                raise NewLangFatalError("浮点数只允许有一个小数点")
            res.append(s)
        elif code[p].isalpha() or code[p]=='_':
            s=""
            while p<len(code) and (code[p].isalnum() or code[p]=='_'):
                s+=code[p]
                p+=1
            if s in kw:
                res.append("*"+s)
            elif s=="var":#兼容integer3，不推荐使用
                res.append("*let")
            else:
                res.append(s)
        elif code[p]=='"':
            p+=1
            s=""
            while p<len(code) and code[p]!='"':
                if code[p]=='\\':
                    p+=1
                    if p==len(code):
                        raise NewLangFatalError("不完整的转义")
                    if code[p].isdigit():
                        if len(code[p:p+3])!=3:
                            raise NewLangFatalError("不完整的转义")
                        i=int(code[p:p+3],8)
                        p+=3
                        s+=chr(i)
                    else:
                        s+={
                            '"':'"',
                            "'":"'",
                            '\\':'\\',
                            'r':'\r',
                            't':'\t',
                            'a':'\a',
                            'f':'\f',
                            'v':'\v',
                            'b':'\b',
                            'n':'\n',
                        }[code[p]]
                        p+=1
                else:
                    s+=code[p]
                    p+=1
            if p==len(code):
                raise NewLangFatalError("未结束的字符串")
            p+=1
            res.append('"'+s+'"')
        else:
            if code[p:p+2] in op:
                res.append(code[p:p+2])
                p+=2
            elif code[p] in op:
                res.append(code[p])
                p+=1
            else:
                raise NewLangFatalError("无法识别的字符")
    return res+[""]
class Tree:
    def __init__(self,*args):
        self.args=args
    def __getitem__(self,n):
        return self.args[n]
    def __str__(self):
        return type(self).__name__+"("+",".join(map(str,self.args))+")"
    __repr__=__str__
class Const(Tree):...
class Var(Tree):...
class Binary(Tree):...
class Unary(Tree):...
class List(Tree):...
class NewFn(Tree):...
class NewLambda(Tree):...
class Call(Tree):...
class Index(Tree):...
class Block(Tree):...
class Let(Tree):...
class LetFn(Tree):...
class Assign(Tree):...
class If(Tree):...
class While(Tree):...
class For(Tree):...
class NoOp(Tree):...
class Return(Tree):...
class Break(Tree):...
class Continue(Tree):...
class ClassDef(Tree):...
class ModuleDef(Tree):...
class Dot(Tree):...
class Import(Tree):...
class Tuple(Tree):...
def parse(tks):
    tk=tks[0]
    p=0
    lst=[LetFn,If,While,Block,For,ClassDef,ModuleDef]
    def eat(ex=None):
        nonlocal tk,tks,p
        if ex==None or tk==ex:
            p+=1
            tk=tks[p]
            return tks[p-1]
        raise NewLangFatalError(f"不匹配的单词{tk}")
    def block():
        if tk!='{':
            l=[stmt()]
            if type(l[-1]) not in lst:
                eat(";")
            return Block(l)
        eat("{")
        l=[]
        while tk!="}":
            l.append(stmt())
            if type(l[-1]) not in lst:
                eat(";")
        eat("}")
        return Block(l)
    def stmt():
        if tk=="*if":
            eat()
            eat("(")
            cond=expr()
            eat(")")
            body=block()
            if tk=="*else":
                eat()
                return If(cond,body,block())
            else:
                return If(cond,body,NoOp())
        if tk=="*while":
            eat()
            eat("(")
            cond=expr()
            eat(")")
            body=block()
            if tk=="*else":
                eat()
                return While(cond,body,block())
            else:
                return While(cond,body,NoOp())
        if tk=="*for":
            eat()
            eat('(')
            if tk!=';':
                decl=stmt()
            else:
                decl=NoOp()
            eat(';')
            if tk!=';':
                cond=expr()
            else:
                cond=Const(True)
            eat(';')
            if tk!=')':
                incr=stmt()
            else:
                incr=NoOp()
            eat(')')
            return For(decl,cond,incr,block())
        if tk=="*let":
            eat()
            name=eat()
            if tk=='(':
                return LetFn(name,parse_fn())
            name=[name]
            value=[Const(None)]
            if tk=="=":
                eat()
                value[-1]=expr()
            while tk==",":
                eat()
                name.append(eat())
                value.append(Const(None))
                if tk=="=":
                    eat()
                    value[-1]=expr()
            return Let(name,value)
        if tk=="*return":
            eat()
            return Return(parse_tuple())
        if tk=="*break":
            eat()
            return Break()
        if tk=="*continue":
            eat()
            return Continue()
        if tk=="*class":
            eat()
            name=eat()
            parents=[]
            if tk==":":
                eat()
                parents.append(expr())
                while tk==',':
                    eat()
                    parents.append(expr())
            return ClassDef(name,parents,block())
        if tk=="*module":
            eat()
            return ModuleDef(eat(),block())
        if tk=="*import":
            eat()
            return Import(expr())
        if tk==";":
            return NoOp()
        e=parse_tuple()
        if tk=='=':
            eat()
            return Assign(e,parse_tuple())
        return e
    def prio(op):
        return {
            '*':10,'/':10,'%':10,
            '+':9,'-':9,
            '<<':8,'>>':8,
            '==':7,'!=':7,'<':7,'>':7,'>=':7,'<=':7,
            '&':6,'|':6,'^':6,
            '&&':5,'||':5,
        }[op]
    def parse_tuple():
        r=expr()
        if tk==',':
            eat()
            if tk in (';',')','='):
                return Tuple([r])
            r=[r,expr()]
            while tk==',':
                eat()
                r.append(expr())
            return Tuple(r)
        return r
    def expr():#更先进的表达式语法分析
        res=factor()
        if tk in [
            '+','-','*','/','%',
            '==','!=','>','<','>=','<=',
            '<<','>>',
            "&&",'||','&','|','^',
        ]:
            res=Binary(eat(),res,factor())
            while tk in [
                '+','-','*','/','%',
                '==','!=','>','<','>=','<=',
                '<<','>>',
                "&&",'||','&','|','^',
            ]:
                op=eat()
                p=prio(op)
                fac=factor()
                if prio(res[0])>p:
                    res=Binary(op,res,fac)
                else:
                    res=Binary(res[0],res[1],Binary(op,res[2],fac))
        return res
    def factor():
        if tk=="":
            raise NewLangFatalError("代码不应在这里结束")
        if tk=="*True":
            eat()
            return fh(Const(True))
        if tk=="*False":
            eat()
            return fh(Const(False))
        if tk=="*None":
            eat()
            return fh(Const(None))
        if tk[0].isdigit():
            if '.' in tk:
                return fh(Const(float(eat())))
            return fh(Const(int(eat())))
        if tk[0].isalpha() or tk[0]=="_":
            return fh(Var(eat()))
        if tk=="(":
            eat()
            e=parse_tuple()
            eat(")")
            return fh(e)
        if tk[0]=='"':
            return fh(Const(eat()[1:-1]))
        if tk=='[':
            eat()
            l=[]
            if tk!=']':
                l=[expr()]
                while tk==',':
                    eat()
                    l.append(expr())
            eat(']')
            return fh(List(l))
        if tk=='!!':
            eat()
            return parse_fn()
        if tk in ('+','-','!','~'):
            return Unary(eat(),factor())
        raise NewLangFatalError("无法识别的单词")
    def fh(v):
        if tk=='[':
            eat()
            idx=expr()
            eat(']')
            return fh(Index(v,idx))
        if tk=='(':
            eat()
            args=[]
            if tk!=')':
                args.append(expr())
                while tk==',':
                    eat()
                    args.append(expr())
            eat(')')
            return fh(Call(v,args))
        if tk=='.':
            eat()
            return fh(Dot(v,eat()))
        return v
    def parse_fn():
        eat('(')
        para=[]
        if tk!=')':
            para=[eat()]
            while tk==',':
                eat()
                para.append(eat())
        eat(')')
        if tk=='=':
            eat()
            return NewLambda(para,expr())
        return NewFn(para,block())
    return block()
class NewLangError(Exception):...
class Class:
    def __init__(self,name,parents,attr):
        self.name,self.parents,self.attr=name,parents,attr
    def getattr(self,name):
        return self.allattr()[name]
    def setattr(self,name,value):
        self.allattr()[name]=value
    def allattr(self):
        res={}
        for i in self.parents:
            a=i.allattr()
            for k,v in a.items():
                res[k]=v
        for k,v in self.attr.items():
            res[k]=v
        return res
    def __call__(self,*args):
        v=Object(self,self.allattr())
        Method(v,self.getattr("__init__"))(*args)
        return v
class Module:
    def __init__(self,name,attr):
        self.name,self.attr=name,attr
    def getattr(self,name):
        return self.attr[name]
    def setattr(self,name,value):
        self.attr[name]=value
class Object:
    def __init__(self,tp,attr):
        self.tp,self.attr=tp,attr
    def getattr(self,name):
        v=self.attr[name]
        if type(v) in (Fn,Lambda):
            return Method(self,v)
        return v
    def setattr(self,name,value):
        self.attr[name]=value
class Method:
    def __init__(self,obj,fn):
        self.obj,self.fn=obj,fn
    def __call__(self,*args):
        if len(args)+1!=len(self.fn.para):
            raise NewLangError("参数数量不匹配")
        scope=self.fn.closure+[dict(zip(self.fn.para,(self.obj,)+args))]
        if type(self.fn)==Fn:
            ret=run(self.fn.body,scope)
            if ret==None:
                return None
            return ret[0]
        else:
            return run(self.fn.body,scope)
class Fn:
    def __init__(self,para,body,closure):
        self.para,self.body,self.closure=para,body,closure
    def __call__(self,*args):
        if len(args)!=len(self.para):
            raise NewLangError("参数数量不匹配")
        ret=run(self.body,self.closure+[dict(zip(self.para,args))])
        if ret==None:
            return None
        return ret[0]
class Lambda:
    def __init__(self,para,body,closure):
        self.para,self.body,self.closure=para,body,closure
    def __call__(self,*args):
        if len(args)!=len(self.para):
            raise NewLangError("参数数量不匹配")
        return run(self.body,self.closure+[dict(zip(self.para,args))])
def match(l,r):
    if type(l) not in (List,Tuple):
        return [(l,r)]
    else:
        l=l[0]
        res=[]
        if len(l)!=len(r):
            raise NewLangError("解构：变量和值数量不匹配")
        for i in range(len(l)):
            res.extend(match(l[i],r[i]))
        return res
def run(tree:Tree,scope:list):
    def find(name:str):
        for i in reversed(scope):
            if name in i:
                return i[name]
        raise NewLangError("找不到变量"+name)
    def set(name:str,value):
        nonlocal scope
        for i in reversed(scope):
            if name in i:
                i[name]=value
                return
        raise NewLangError("找不到变量"+name)
    tp=type(tree).__name__
    if tp=="Const":
        return tree[0]
    if tp=="Var":
        return find(tree[0])
    if tp=="Binary":#支持短路
        op=tree[0]
        l=run(tree[1],scope)
        if op=='&&':
            if not l:
                return False
            return bool(run(tree[2],scope))
        if op=='||':
            if l:
                return True
            return bool(run(tree[2],scope))
        return {
            '+':lambda a,b:a+b,
            '-':lambda a,b:a-b,
            '*':lambda a,b:a*b,
            '/':lambda a,b:a/b,
            '%':lambda a,b:a%b,
            '==':lambda a,b:a==b,
            '!=':lambda a,b:a!=b,
            '>':lambda a,b:a>b,
            '<':lambda a,b:a<b,
            '>=':lambda a,b:a>=b,
            '<=':lambda a,b:a<=b,
            '<<':lambda a,b:a<<b,
            '>>':lambda a,b:a>>b,
            '&':lambda a,b:a&b,
            '|':lambda a,b:a|b,
            '^':lambda a,b:a^b
        }[op](l,run(tree[2],scope))
    if tp=="Unary":
        return {
            '+':lambda a:+a,
            '-':lambda a:-a,
            '!':lambda a:not a,
            '~':lambda a:~a
        }[tree[0]](run(tree[1],scope))
    if tp=="List":
        return [run(i,scope) for i in tree[0]]
    if tp=="NewFn":
        return Fn(tree[0],tree[1],scope)
    if tp=="NewLambda":
        return Lambda(tree[0],tree[1],scope)
    if tp=="Call":
        return run(tree[0],scope)(*[run(i,scope) for i in tree[1]])
    if tp=="Index":
        return run(tree[0],scope)[run(tree[1],scope)]
    if tp=="Block":
        scope+=[{}]
        for i in tree[0]:
            v=run(i,scope)
            if type(v) in (Return,Break,Continue):
                scope=scope[:-1]
                return v
        scope=scope[:-1]
        return
    if tp=="Let":
        for i in range(len(tree[0])):
            scope[-1][tree[0][i]]=run(tree[1][i],scope)
        return
    if tp=="LetFn":
        scope[-1][tree[0]]=run(tree[1],scope)
        return
    if tp=="Assign":
        _r=run(tree[1],scope)
        mr=match(tree[0],_r)
        for k,v in mr:
            l=k
            idx=[]
            while type(l)!=Var:
                if type(l)==Index:
                    idx=[run(l[1],scope)]+idx
                    l=l[0]
                elif type(l)==Dot:
                    idx=[l[1]]+idx
                    l=l[0]
                else:
                    raise NewLangFatalError("左值写法出错",type(l))
            r=v
            def w(base,idx,to):
                if idx==[]:
                    return to
                if type(base) not in (Class,Module,Object):
                    base[idx[0]]=w(base[idx[0]],idx[1:],to)
                else:
                    base.setattr(idx[0],w(base.getattr(idx[0]),idx[1:],to))
                return base
            set(l[0],w(find(l[0]),idx,r))
        return
    if tp=="If":
        if run(tree[0],scope):
            return run(tree[1],scope)
        return run(tree[2],scope)
    if tp=="While":
        while run(tree[0],scope):
            v=run(tree[1],scope)
            if type(v)==Return:
                return v
            if type(v)==Break:
                break
        else:
            return run(tree[2],scope)
        return
    if tp=="For":
        scope+=[{}]
        run(tree[0],scope)
        while run(tree[1],scope):
            v=run(tree[3],scope)
            if type(v)==Return:
                scope=scope[:-1]
                return v
            if type(v)==Break:
                break
            run(tree[2],scope)
        scope=scope[:-1]
        return
    if tp=="NoOp":
        return
    if tp=="Return":
        return Return(run(tree[0],scope))
    if tp=="Break":
        return tree
    if tp=="Continue":
        return tree
    if tp=="ClassDef":
        scope+=[{}]
        for i in tree[2][0]:
            run(i,scope)
        v=scope[-1]
        scope=scope[:-1]
        scope[-1][tree[0]]=Class(tree[0],list(map(lambda a:run(a,scope),tree[1])),v)
        if "__init__" not in scope[-1][tree[0]].attr:
            scope[-1][tree[0]].attr["__init__"]=Fn(["self"],Block([]),scope+[v])
        return
    if tp=="ModuleDef":
        scope+=[{}]
        for i in tree[1][0]:
            run(i,scope)
        v=scope[-1]
        scope=scope[:-1]
        scope[-1][tree[0]]=Module(tree[0],v)
        return
    if tp=="Dot":
        return run(tree[0],scope).getattr(tree[1])
    if tp=="Import":
        v=run(tree[0],scope).attr
        for k,v in v.items():
            scope[-1][k]=v
        return
    if tp=="Tuple":
        return tuple(run(i,scope) for i in tree[0])
def load(name):
    import copy
    s="\n".join(open(name,"r").readlines())
    tree=parse(lex(s))
    scope=copy.deepcopy(main_scope)+[{}]
    for i in tree[0]:
        run(i,scope)
    return Module("",scope[-1])
main_scope=[{
    "println":lambda *args:print(*args,sep=""),
    "print":lambda *args:print(*args,sep="",end=""),
    "inputln":input,
    "getchar":lambda:sys.stdin.read(1),
    "ord":ord,
    "chr":chr,
    "stoi":int,
    "stof":float,
    "to_string":str,
    "len":len,
    "system":os.system, 
    "load":load,
}]
tks=lex('''
{
    let a,b,c;
    a,(b,c)=1,(2,3);
    println(a," ",b," ",c);
    a,b,c=c,b,a;
    println(a," ",b," ",c);
}
''')
tree=parse(tks)
run(tree,main_scope)
'''
{
    let a=10;
    a=30;
    if(a==10) println(1);
    else if(a==20) println(2);
    else println(3);
}

{
    let a=[1,2,[2,4,5]];
    a[2][0]=3;
    println(a);
}

{
    let f(a,b){
        println(a," ",b);
        return a+b;
    }
    println(f(1,2));
}

{
    let i=1;
    while(i<10){
        println(i);
        i=i+1;
    }
    else{
        println(10);
    }
}

{
    println((!!(a,b)=a+b)(1,2));
}

{
    let i=0;
    while(1){
        if(i==10) break;
        i=i+1;
        if(i==5) continue;
        println(i);
    }
}

{
    True&&println("Hello,world!");
    False&&println("Hello,world!");
}

{
    let Counter(start)=!!(){
        start=start+1;
        return start;
    }
    let counter=Counter(0);
    let i=counter();
    while(i<10){
        println(i);
        i=counter();
    }
}

{
    for(let i=0;i<10;i=i+1) println(i);
}

{
    //经典测试用例
    class A{
        let a=0;
        let __init__(self,a){
            self.a=a;
        }
        let printA(self){
            println(self.a);
        }
        let setA(self,v){
            self.a=v;
        }
    }
    let a=A(10);
    a.printA();
    a.setA(20);
    a.printA();
}
'''