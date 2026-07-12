import os,sys,time
def lex(code:str)->list:
    op=[
        '+','-','*','/','%',
        '==','!=','>','<','>=','<=',
        '<<','>>',
        '&&','||','&','|','^',
        '!','~',
        '(',')','[',']','{','}',
        ',','.',';',':','=',
    ]
    keywords=[
        "var",
        "if",
        "else",
        "while",
        "func",
        "type",
        "extends",
        "module",
        "load",
        "import",
        "for",
        "in",
        "return",
        "break",
        "continue",
    ]
    p=0
    res=[]
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
                    raise Exception("未结束的注释")
                p+=2
        if p==len(code):
            break
        if code[p].isdigit():
            s=""
            while p<len(code) and (code[p].isdigit() or code[p]=="."):
                s+=code[p]
                p+=1
            res.append(s)
        elif code[p].isalpha() or code[p]=="_":
            s=""
            while p<len(code) and (code[p].isalnum() or code[p]=="_"):
                s+=code[p]
                p+=1
            if s in keywords:
                res.append('*'+s)
            else:
                res.append(s)
        elif code[p]=='"':
            s='"'
            p+=1
            while p<len(code) and code[p]!='"':
                if code[p]=='\\':
                    p+=1
                    if p==len(code):
                        raise Exception("Unexpected EOF.")
                    if code[p].isdigit():
                        if len(code[p:p+3])!=3:
                            raise Exception("Unexpected EOF.")
                        v=chr(int(code[p:p+3],8))
                        p+=3
                        s+=v
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
                raise Exception("Unexpected EOF.")
            s+='"'
            p+=1
            res.append(s)
        elif p<len(code) and code[p:p+2] in op:
            res.append(code[p:p+2])
            p+=2
        elif code[p] in op:
            res.append(code[p])
            p+=1
    return res+[""]
def parse(tokens:list)->tuple:
    lst=[Block,IfStmt,WhileStmt,FnDef,TypeDef,ModDef,ForStmt]
    p=0
    token=tokens[0]
    def eat(ex=None)->str:
        nonlocal tokens,token,p
        if ex==None or ex==token:
            p+=1
            token=tokens[p]
            return tokens[p-1]
        raise Exception(f"Unmatched token (except '{ex}',got '{token}').")
    def eat_id()->str:
        if token[0].isalpha() or token[0]=='_':
            return eat()
        raise Exception(f"'{token}' is not an identifier.")
    def block()->tuple:
        if token!='{':
            l=[stmt()]
            if l[-1][0] not in lst:
                eat(';')
            return (Block,l)
        eat('{')
        l=[]
        while token!='}':
            l.append(stmt())
            if l[-1][0] not in lst:
                eat(';')
        eat('}')
        return (Block,l)
    def stmt()->tuple:
        if token=="*if":
            eat()
            eat('(')
            cond=expr()
            eat(')')
            t=block()
            if token=="*else":
                eat()
                return (IfStmt,cond,t,block())
            return (IfStmt,cond,t,(NoOp,))
        if token=="*while":
            eat()
            eat('(')
            cond=expr()
            eat(')')
            t=block()
            if token=="*else":
                eat()
                return (WhileStmt,cond,t,block())
            return (WhileStmt,cond,t,(NoOp,))
        if token=="*var":
            eat()
            name=[eat_id()]
            if token=='=':
                eat()
                value=[expr()]
            else:
                value=[(Const,None)]
            while token==',':
                eat()
                name.append(eat_id())
                if token=='=':
                    eat()
                    value.append(expr())
                else:
                    value.append((Const,None))
            return (VarDecl,name,value)
        if token=="*func":
            if tokens[p+2]!='(':
                pass
            else:
                eat()
                name=eat_id()
                return (FnDef,name,parse_lambda())
        if token=="*type":
            eat()
            name=eat_id()
            extend=[]
            if token=="*extends":
                eat()
                extend.append(_expr())
                while token==',':
                    eat()
                    extend.append(_expr())
            return (TypeDef,name,parse_dict(),extend)
        if token=="*load":
            eat()
            return (Load,expr())
        if token=="*import":
            eat()
            return (Import,expr())
        if token=="*module":
            eat()
            return (ModDef,eat_id(),parse_dict())
        if token=="*for":
            eat()
            eat('(')
            eat('*var')
            var=expr()
            eat('*in')
            value=expr()
            eat(')')
            return (ForStmt,var,value,block())
        if token=="*return":
            eat()
            return (ReturnStmt,expr())
        if token=="*break":
            eat()
            return (BreakStmt,)
        if token=="*continue":
            eat()
            return (ContinueStmt,)
        if token==';':
            return (NoOp,)
        v=expr()
        if token=='=':
            eat()
            return (AssignStmt,v,expr())
        return (ExprStmt,v)
    def parse_dict():
        eat('{')
        k,v=[],[]
        while token!='}':
            k.append(eat_id())
            eat(':')
            v.append(_expr())
            if token==',':
                eat()
        eat('}')
        return k,v
    def parse_lambda():
        eat('(')
        para=[]
        if token!=')':
            para.append(eat_id())
            while token==',':
                eat()
                para.append(eat_id())
        eat(')')
        return (Lambda,para,block())
    def prio(op):
        return {
            '*':10,'/':10,'%':10,
            '+':9,'-':9,
            '<<':8,'>>':8,
            '==':7,'!=':7,'<':7,'>':7,'>=':7,'<=':7,
            '&':6,'|':6,'^':6,
            '&&':5,'||':5,
        }[op]
    def expr()->tuple:
        r=_expr()
        if token==',':
            eat()
            r=[r]
            if token in (';',')','='):
                return (MakeTuple,r)
            r.append(_expr())
            while token==',':
                eat()
                r.append(_expr())
            return (MakeTuple,r)
        return r
    def _expr()->tuple:
        res=factor()
        if token in [
            '+','-','*','/','%',
            '==','!=','>','<','>=','<=',
            '<<','>>',
            "&&",'||','&','|','^',
        ]:
            res=(Binary,eat(),res,factor())
            while token in [
                '+','-','*','/','%',
                '==','!=','>','<','>=','<=',
                '<<','>>',
                "&&",'||','&','|','^',
            ]:
                op=eat()
                p=prio(op)
                fac=factor()
                if prio(res[1])>p:
                    res=(Binary,op,res,fac)
                else:
                    res=(Binary,res[1],res[2],(Binary,op,res[3],fac))
        return res
    def factor()->tuple:
        if token[0].isdigit():
            if '.' in token:
                return factor_help((Const,float(eat())))
            return factor_help((Const,int(eat())))
        if token[0]=='"':
            return factor_help((Const,eat()[1:-1]))
        if token[0].isalpha() or token[0]=='_':
            return factor_help((Id,eat()))
        if token=='(':
            eat()
            e=expr()
            eat(')')
            return factor_help(e)
        if token=='[':
            eat()
            l=[]
            if token!=']':
                l.append(_expr())
                while token==',':
                    eat()
                    l.append(_expr())
            eat(']')
            return factor_help((MakeList,l))
        if token=="*func":
            eat()
            return factor_help(parse_lambda())
        raise Exception(f"Unknown token '{token}'.")
    def factor_help(v:tuple)->tuple:
        if token=='[':
            eat()
            idx=expr()
            eat(']')
            return factor_help((Index,v,idx))
        if token=='(':
            eat()
            args=[]
            if token!=')':
                args.append(_expr())
                while token==',':
                    eat()
                    args.append(_expr())
            eat(')')
            return factor_help((Call,v,args))
        if token=='.':
            eat()
            return factor_help((Dot,v,eat_id()))
        return v
    return block()
class Scope:
    def __init__(self,p=None,v={}):
        self.parent=p
        self.var=v
    def find(self,name:str):
        if name in self.var:
            return self.var[name]
        if self.parent!=None:
            return self.parent.find(name)
        raise Exception(f"Can't find variable '{name}'")
    def set(self,name:str,value):
        if name in self.var:
            self.var[name]=value
            return
        if self.parent!=None:
            return self.parent.set(name,value)
        raise Exception(f"Can't find variable '{name}'")
    def define(self,name:str,value):
        self.var[name]=value
class Fn:
    def __init__(self,p,b,c):
        self.para,self.body,self.closure=p,b,c
class Method:
    def __init__(self,obj,fn:Fn):
        self.obj,self.fn=obj,fn
class Type:
    def __init__(self,v:dict,extend:list):
        self.attr,self.extend=v,extend
    def allattr(self)->dict:
        r={}
        for i in self.extend:
            v=i.allattr()
            for k,v in v.items():
                r[k]=v
        for k,v in self.attr.items():
            r[k]=v
        return r
class Mod:
    def __init__(self,v:dict):
        self.attr=v
class Object:
    def __init__(self,v:dict):
        self.attr=v
def match(l,r):
    if l[0] not in (MakeList,MakeTuple):
        return [(l,r)]
    else:
        l=l[1]
        res=[]
        if len(l)!=len(r):
            raise Exception("No enough value to unpack.")
        for i in range(len(l)):
            res.extend(match(l[i],r[i]))
        return res
def run_code(tree:tuple,scope:Scope=Scope()):
    def call(fn,args:list):
        if callable(fn):
            return fn(*args)
        if type(fn)==Fn:
            a=run_code(fn.body,Scope(fn.closure,dict(zip(fn.para,args))))
            if a in (None,()):
                return None
            return a[1]
        elif type(fn)==Type:
            cons=fn.allattr()["__init__"]
            obj=Object(fn.allattr())
            sc=Scope(cons.closure,dict(zip(cons.para,args)))
            sc.define("this",obj)
            a=run_code(cons.body,sc)
            return obj
        elif type(fn)==Method:
            obj,fn=fn.obj,fn.fn
            sc=Scope(fn.closure,dict(zip(fn.para,args)))
            sc.define("this",obj)
            a=run_code(fn.body,sc)
            if a in (None,()):
                return None
            return a[1]
        elif type(fn)==Object:
            obj=fn
            fn=obj.attr["__call__"]
            sc=Scope(fn.closure,dict(zip(fn.para,args)))
            sc.define("this",obj)
            a=run_code(fn.body,sc)
            if a in (None,()):
                return None
            return a[1]
        else:
            raise Exception("Can't call this object.")
    def assign(mr):
        for k,v in mr:
            l=k
            idx=[]
            while l[0]!=Id:
                if l[0]==Index:
                    idx=[(Index,run(l[2]))]+idx
                    l=l[1]
                elif l[0]==Dot:
                    idx=[(Dot,l[2])]+idx
                    l=l[1]
                else:
                    raise Exception("Wrong l-value.")
            r=v
            def w(base,idx,to):
                if idx==[]:
                    return to
                if idx[0][0]==Index:
                    if type(base)==Object:
                        call(Method(base,base.attr["__setitem__"]),[idx[0][1],w(call(Method(base,base.attr["__getitem__"]),[idx[0][1]]),idx[1:],to)])
                    else:
                        base[idx[0][1]]=w(base[idx[0][1]],idx[1:],to)
                elif idx[0][0]==Dot:
                    if type(base)==Type:
                        base.allattr()[idx[0][1]]=w(base.allattr()[idx[0][1]],idx[1:],to)
                    elif type(base)==Mod:
                        base.attr[idx[0][1]]=w(base.attr[idx[0][1]],idx[1:],to)
                    elif type(base)==Object:
                        base.attr[idx[0][1]]=w(base.attr[idx[0][1]],idx[1:],to)
                return base
            scope.set(l[1],w(scope.find(l[1]),idx,r))
    def iter_next(obj):
        return next(obj)
    def obj_iter(obj):
        if type(obj) in (list,tuple,dict):
            return iter(obj)
        raise Exception("Object is not iterable.")
    def run(tree:tuple):
        tp=tree[0]
        v=tree[1:]
        if tp==Const:
            return v[0]
        elif tp==Id:
            return scope.find(v[0])
        elif tp==Binary:
            if v=='&&':
                if run(v[1]):
                    return run(v[2])
                return False
            if v=='||':
                if not run(v[1]):
                    return run(v)
                return True
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
            }[v[0]](run(v[1]),run(v[2]))
        elif tp==Unary:
            return {
                '+':lambda a:+a,
                '-':lambda a:-a,
                '!':lambda a:not a,
                '~':lambda a:~a,
            }[v[0]](run(v[1]))
        elif tp==Lambda:
            return Fn(v[0],v[1],scope)
        elif tp==Call:
            return call(run(v[0]),[run(i) for i in v[1]])
        elif tp==Index:
            arr=run(v[0])
            if type(arr)==Object:
                arr:Object
                return call(Method(arr,arr.attr["__getitem__"]),[run(v[1])])
            return arr[run(v[1])]
        elif tp==MakeList:
            return [run(i) for i in v[0]]
        elif tp==Dot:
            l=run(v[0])
            if type(l)==Type:
                return l.allattr()[v[1]]
            elif type(l)==Object:
                r=l.attr[v[1]]
                if type(r)==Fn:
                    return Method(l,r)
                return r
            return l.attr[v[1]]
        elif tp==MakeTuple:
            return tuple(run(i) for i in v[0])
        #-------------------
        elif tp==NoOp:
            ...
        elif tp==Block:
            for i in v[0]:
                r=run(i)
                if r:
                    return r
        elif tp==ExprStmt:
            run(v[0])
        elif tp==IfStmt:
            if run(v[0]):
                return run(v[1])
            return run(v[2])
        elif tp==WhileStmt:
            while run(v[0]):
                r=run(v[1])
                if r!=() and r[0]==BreakSignal:
                    return ()
                if r!=() and r[0]==ReturnSignal:
                    return r
            return run(v[2])
        elif tp==FnDef:
            scope.define(v[0],run(v[1]))
        elif tp==TypeDef:
            kv=dict(zip(v[1][0],map(run,v[1][1])))
            name=v[0]
            kv["__name__"]=name
            scope.define(name,Type(kv,list(map(run,v[2]))))
        elif tp==ModDef:
            kv=dict(zip(v[1][0],map(run,v[1][1])))
            name=v[0]
            kv["__name__"]=name
            scope.define(name,Mod(kv))
        elif tp==VarDecl:
            for i in range(len(v[0])):
                scope.define(v[0][i],run(v[1][i]))
        elif tp==AssignStmt:
            _r=run(v[1])
            mr=match(v[0],_r)
            assign(mr)
        elif tp==ReturnStmt:
            return (ReturnSignal,run(v[0]))
        elif tp==BreakStmt:
            return (BreakSignal,)
        elif tp==ContinueStmt:
            return (ContinueSignal,)
        elif tp==Load:
            fname=run(v[0])
            file="\n".join(open(fname,'r',encoding='utf-8').readlines())
            run(parse(lex(file)))
        elif tp==Import:
            mod=run(v[0])
            for k,v in mod.attr.items():
                scope.define(k,v)
        elif tp==ForStmt:
            var,value,body=v
            it=obj_iter(run(value))
            while 1:
                try:
                    mr=match(var,iter_next(it))
                except StopIteration:
                    break
                except:
                    raise Exception("Object is not an iterator.")
                for k,b in mr:
                    scope.define(k[1],b)
                r=run(body)
                if r!=() and r[0]==BreakSignal:
                    return ()
                if r!=() and r[0]==ReturnSignal:
                    return r
        else:
            raise Exception(tree)
        return ()
    return run(tree)
BreakSignal,ContinueSignal,ReturnSignal=0,1,2
Const,Id,Binary,Unary,Lambda,Call,Index,MakeList,Dot,MakeTuple,\
NoOp,Block,ExprStmt,IfStmt,WhileStmt,FnDef,TypeDef,ModDef,VarDecl,AssignStmt,ReturnStmt,BreakStmt,ContinueStmt,Load,Import,ForStmt,\
=[i for i in range(26)]
def _fread(file,encoding):
    return "".join(open(file,"r",encoding=encoding).readlines())
def _fwrite(file,encoding,text):
    open(file,"w",encoding=encoding).write(text)
def _fadd(file,encoding,text):
    open(file,"a",encoding=encoding).write(text)
run_code(parse(lex('''
{
    type T{
        text:""
        __init__:func(text){
            this.text=text;
        }
        __call__:func(){
            println(this.text);
        }
    }
    T("Hello,world!")();
    type List{
        arr:[]
        __init__:func(arr){
            this.arr=arr;
        }
        __getitem__:func(n){
            return this.arr[n];
        }
        __setitem__:func(n,v){
            this.arr[n]=v;
        }
    }
    var lst=List([1,2,2]);
    println(lst.arr," ",lst[2]);
    lst[2]=3;
    println(lst.arr," ",lst[2]);
}
''')),Scope(None,{
    "println":lambda *args:print(*args,flush=True,sep=""),
    "print":lambda *args:print(*args,flush=True,sep="",end=""),
    "readln":input,
    "getchar":lambda:sys.stdin.read(1),
    "ord":ord,
    "chr":chr,
    "system":os.system,
    "len":len,
    "time":time.time,
    "sleep":time.sleep,
    "basic_fileio":Mod({
        "fread":_fread,
        "fwrite":_fwrite,
        "fadd":_fadd,
    }),
}))
'''
{
    func f(a,b){
        println(a," ",b);
        return a+b;
    }
    println(f(1,2));
}

{
    func prime(a){
        if(a<2) return 0;
        var i=2;
        while(i<a){
            if(a%i==0) return 0;
            i=i+1;
        }
        return 1;
    }
    println(prime(102));
}

{
    func(a){
        println(a);
    }("Hello,world!");
}

{
    module M{
        pi:3.14,
        get_pi:func(){
            return 3.14;
        }
    }
    println(M.get_pi());
}

{
    println(func(a,b){
        return a+b;
    }(1,2));
}

{
    func Counter(start){
        return func(){
            start=start+1;
            return start;
        };
    }
    var counter=Counter(0);
    var i=0;
    while(i<10){
        println(counter());
        i=i+1;
    }
}

{
    type P{
        b:0
    }
    type T extends P{
        a:10
    }
    println(T.b);
}

{
    type T{
        a:0,
        __init__:func(a){
            this.a=a;
        }
    }
    println(T(1).a);
}

{
    type T{
        a:0,
        __init__:func(a){
            this.a=a;
        },
        printThis:func(){
            println("T object: a=",this.a);
        },
        setA:func(a){
            this.a=a;
        }
    }
    var v=T(10);
    v.printThis();
    v.setA(20);
    v.printThis();
}

{
    //Speed test
    var t0=time();
    var fac=1;
    var i=1;
    while(i<=100000){
        fac=fac*i;
        i=i+1;
    }
    //println(fac);
    println(time()-t0);
}

{
    module mod{
        pi:3.14
    }
    //load "newlang/test_mod.nl";
    import mod;
    println(pi);
}

{
    var a,b,c;
    a,(b,c)=1,(2,3);
    println(a," ",b," ",c);
}

{
    for(var (i,(j,k)) in [(1,(2,3)),(4,(5,6))]) println(i," ",j," ",k);
}

{
    import basic_fileio;
    fwrite("newlang/test_fileio.txt","utf-8","Hello,world!");
    println(fread("newlang/test_fileio.txt","utf-8"));
}
'''