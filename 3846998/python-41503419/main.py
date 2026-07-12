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
class Paren(Tree):...
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
def parse(tks):
    tk=tks[0]
    p=0
    lst=[LetFn,If,While,Block,For]
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
            return Return(expr())
        if tk=="*break":
            eat()
            return Break()
        if tk=="*continue":
            eat()
            return Continue()
        if tk==";":
            return NoOp()
        e=expr()
        if tk=='=':
            eat()
            return Assign(e,expr())
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
    def expr():#更先进的表达式语法分析
        res=factor()
        while tk in [
            '+','-','*','/','%',
            '==','!=','>','<','>=','<=',
            '<<','>>',
            "&&",'||','&','|','^',
        ]:
            op=eat()
            p=prio(op)
            fac=factor()
            if type(res)==Binary:
                if prio(res[0])>p:
                    res=Binary(op,res,fac)
                else:
                    res=Binary(res[0],res[1],Binary(op,res[2],fac))
            else:
                res=Binary(op,res,fac)
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
            e=expr()
            eat(")")
            return fh(Paren(e))
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
    if tp=="Paren":
        return run(tree[0],scope)
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
        l=tree[0]
        idx=[]
        while type(l)!=Var:
            if type(l)==Index:
                idx=[run(l[1],scope)]+idx
                l=l[0]
            else:
                raise NewLangFatalError("左值写法出错")
        r=run(tree[1],scope)
        def w(base,idx,to):
            if idx==[]:
                return to
            base[idx[0]]=w(base[idx[0]],idx[1:],to)
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
tks=lex('''
{
    var code=inputln("这是一个用NewLang写的Brainfuck解释器\\nBrainfuck>>>");
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
        if(c==",") mem[pos]=ord(getchar());
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
''')
tree=parse(tks)
run(tree,[{
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
}])
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
'''