import copy,sys,time
kw=[
    'if','else','elif','end','while','fn','var','for','return','break','continue','in','to','step','where','import',
    'and','or','not','True','False','None',
]
op=[
    '+','-','*','/','%',
    '==','!=','>','<','>=','<=',
    '<<','>>','&','|','^','~',
    ',','.','(',')','[',']','{','}',':','=',
]
escape={
    'r':'\r',
    't':'\t',
    'a':"\a",
    'f':'\f',
    'v':"\v",
    'b':"\b",
    'n':"\n",
    '"':'"',
    "'":"'",
    '\\':'\\',
}
prio={
    '*':100,'/':100,'%':100,
    '+':99,'-':99,
    '<<':98,'>>':98,
    '==':97,'!=':97,
    '>':96,'<':96,'>=':96,'<=':96,
    '&':95,'^':94,'|':93,
    '*and':92,'*or':91,
}
VarDecl,If,While,ForTo,ForIn,Return,Break,Continue,FnDef,Assign,NoOp,Import,\
    Const,Var,Binary,Unary,Index,Call,NewObject,NewList,NewFn,Where,\
        =[i for i in range(22)]
class Scope:
    def __init__(self,parent,var:dict):
        self.parent,self.var=parent,var
    def find(self,name:str):
        if name in self.var:
            return self.var[name]
        elif self.parent:
            return self.parent.find(name)
        else:
            raise Exception(f"变量{name}未定义。")
    def set(self,name:str,value):
        if name in self.var:
            self.var[name]=value
        elif self.parent:
            self.parent.set(name,value)
        else:
            raise Exception(f"变量{name}未定义。")
    def define(self,name:str,value):
        self.var[name]=value
class Signal:
    def __init__(self,signal:int,value=None):
        self.signal,self.value=signal,value
    def __eq__(self,b):
        return type(b)==Signal and type(self)==Signal and b.signal==self.signal
class Function:
    def __init__(self,para,body,closure):
        self.para,self.body,self.closure=para,body,closure
    def __call__(self,*args):
        scope=Scope(self.closure,dict(zip(self.para,args)))
        v=run_code(self.body,scope)
        if v!=None:
            return v.value
        return None
class Method:
    def __init__(self,obj:dict,func:Function):
        self.obj,self.func=obj,func
    def __call__(self,*args):
        scope=Scope(self.func.closure,dict(zip(self.func.para,(self.obj,)+args)))
        v=run_code(self.func.body,scope)
        if v!=None:
            return v.value
        return None
def lex(code:str):
    p=0
    res=[]
    while p<len(code):
        while p<len(code) and code[p] in " \n\t#":
            if code[p]=='#':
                while p<len(code) and code[p]!='\n':
                    p+=1
            else:
                p+=1
        if p==len(code):
            break
        elif code[p].isdigit():
            s=""
            while p<len(code) and (code[p].isdigit() or code[p]=='.'):
                s+=code[p]
                p+=1
            res.append(s)
        elif code[p].isalpha() or code[p]=='_':
            s=""
            while p<len(code) and (code[p].isalnum() or code[p]=='_'):
                s+=code[p]
                p+=1
            if s in kw:
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
                        raise Exception("无法结束的转义字符。")
                    if code[p].isdigit():
                        if p+3>=len(code):
                            raise Exception("无法结束的转义字符。")
                        s+=chr(int(code[p:p+3],8))
                        p+=3
                    elif code[p] in escape:
                        s+=escape[code[p]]
                        p+=1
                    else:
                        raise Exception("错误的转义字符。")
                else:
                    s+=code[p]
                    p+=1
            if p==len(code):
                raise Exception("字符串未结束。")
            else:
                res.append(s+'"')
                p+=1
        elif code[p:p+2] in op:
            res.append(code[p:p+2])
            p+=2
        elif code[p] in op:
            res.append(code[p])
            p+=1
        else:
            raise Exception(f"无法识别当前字符'{code[p]}'。")
    return res+[""]
def parse(tokens):
    p=0
    token=tokens[p]
    def eat(ex=None)->str:
        nonlocal p,token
        if token==ex or ex==None:
            p+=1
            token=tokens[p]
            return tokens[p-1]
        else:
            raise Exception(f"当前单词不匹配，期望'{ex}'，得到'{token}'。")
    def block(_end):
        l=[]
        while token not in _end:
            l.append(stmt())
        return l
    def stmt()->tuple:
        if token=='*if':
            eat()
            c=[expr()]
            t=[block(['*end','*else','*elif'])]
            while token=='*elif':
                eat()
                c.append(expr())
                t.append(block(['*end','*else','*elif']))
            if token=='*end':
                eat()
                return (If,c,t,[(NoOp,)])
            else:
                eat('*else')
                f=block(['*end'])
                eat()
                return (If,c,t,f)
        elif token=='*while':
            eat()
            c=expr()
            t=block(['*end'])
            eat()
            return (While,c,t)
        elif token=='*var':
            eat()
            name=[eat_id()]
            if token=='=':
                eat()
                value=[expr()]
            else:
                value=[(Const,None)]
            while token==',':
                name.append(eat_id())
                if token=='=':
                    eat()
                    value.append(expr())
                else:
                    value.append((Const,None))
            return (VarDecl,name,value)
        elif token=='*fn':
            eat()
            name=eat_id()
            eat('(')
            para=[]
            if token!=')':
                para.append(eat_id())
                while token==',':
                    eat()
                    para.append(eat_id())
            eat(')')
            body=block(['*end'])
            eat()
            return (FnDef,name,para,body)
        elif token=='*for':
            eat()
            name=eat_id()
            if token=='*in':#ForIn
                eat()
                obj=expr()
                body=block(['*end'])
                eat()
                return (ForIn,name,obj,body)
            elif token=='=':#ForTo
                eat()
                begin=expr()
                eat('*to')
                end=expr()
                if token=='*step':
                    eat()
                    step=expr()
                else:
                    step=(Const,1)
                body=block(['*end'])
                eat()
                return (ForTo,name,begin,end,step,body)
            else:
                raise Exception("无法解析当前单词")
        elif token=='*import':
            eat()
            return (Import,expr())
        elif token=='*return':
            eat()
            return (Return,expr())
        elif token=='*break':
            eat()
            return (Break,)
        elif token=='*continue':
            eat()
            return (Continue,)
        else:
            l=expr()
            if token=='=':
                eat()
                r=expr()
                return (Assign,l,r)
            return l
    def expr()->tuple:
        res=factor()
        if token in prio:
            res=(Binary,eat(),res,factor())
            while token in prio:
                op=eat()
                if prio[op]<=prio[res[1]]:
                    res=(Binary,op,res,factor())
                else:
                    res=(Binary,res[1],res[2],(Binary,op,res[3],factor()))
        if token=='*where':
            eat()
            eat('(')
            body=block([')'])
            eat()
            return (Where,res,body)
        return res
    def factor()->tuple:
        res=None
        if token=="":
            raise Exception("代码不应该在此处结束。")
        elif token[0].isdigit():
            if '.' in token:
                res=(Const,float(eat()))
            else:
                res=(Const,int(eat()))
        elif token[0].isalpha() or token[0]=='_':
            res=(Var,eat())
        elif token[0]=='"':
            res=(Const,eat()[1:-1])
        elif token=='*True':
            eat()
            res=(Const,True)
        elif token=='*False':
            eat()
            res=(Const,False)
        elif token=='*None':
            eat()
            res=(Const,None)
        elif token=='(':
            eat()
            if token=="*fn":
                eat()
                eat('(')
                para=[]
                if token!=')':
                    para.append(eat_id())
                    while token==',':
                        eat()
                        para.append(eat_id())
                eat(')')
                body=block([')'])
                eat()
                return (NewFn,para,body)
            res=expr()
            eat(')')
        elif token=='[':
            eat()
            l=[]
            if token!=']':
                l.append(expr())
                while token==',':
                    eat()
                    l.append(expr())
            eat(']')
            res=(NewList,l)
        elif token=='{':
            eat()
            k,v=[],[]
            while token!='}':
                k.append(eat_id())
                eat(':')
                v.append(expr())
                if token==',':
                    eat()
            eat('}')
            res=(NewObject,k,v)
        else:
            raise Exception(f"无法解析当前单词'{token}'。")
        while token in ['[','(','.']:
            if token=='[':
                eat()
                res=(Index,res,expr())
                eat(']')
            elif token=='(':
                eat()
                l=[]
                if token!=')':
                    l.append(expr())
                    while token==',':
                        eat()
                        l.append(expr())
                eat(')')
                res=(Call,res,l)
            elif token=='.':
                eat()
                res=(Index,res,(Const,eat_id()))
        return res
    def eat_id()->str:
        if token[0].isalpha() or token[0]=='_':
            return eat()
        raise Exception("当前单词不是合法标识符。")
    l=[]
    while token!='':
        l.append(stmt())
    return l
def run_code(tree,scope:Scope):
    def run(tree):
        nonlocal scope
        if type(tree)==list:
            for i in tree:
                v=run(i)
                if type(v)==Signal:
                    return v
            return
        tp=tree[0]
        if tp==VarDecl:
            for i in range(len(tree[1])):
                scope.define(tree[1][i],run(tree[2][i]))
        elif tp==If:
            for i in range(len(tree[1])):
                if run(tree[1][i]):
                    return run(tree[2][i])
            return run(tree[3])
        elif tp==While:
            while run(tree[1]):
                v=run(tree[2])
                if v==Signal(Break):
                    break
                if v==Signal(Return):
                    return v
        elif tp==ForTo:
            name=tree[1]
            begin=run(tree[2])
            end=run(tree[3])
            step=run(tree[4])
            body=tree[5]
            for i in range(begin,end,step):
                scope.define(name,i)
                v=run(body)
                if v==Signal(Break):
                    break
                if v==Signal(Return):
                    return v
        elif tp==ForIn:
            name=tree[1]
            obj=run(tree[2])
            body=tree[3]
            for i in obj:
                scope.define(name,i)
                v=run(body)
                if v==Signal(Break):
                    break
                if v==Signal(Return):
                    return v
        elif tp==Return:
            return Signal(Return,run(tree[1]))
        elif tp==Break:
            return Signal(Break)
        elif tp==Continue:
            return Signal(Continue)
        elif tp==FnDef:
            scope.define(tree[1],Function(tree[2],tree[3],scope))
        elif tp==Assign:
            lvalue=tree[1]
            to=run(tree[2])
            index=[]
            while lvalue[0]==Index:
                index=[run(lvalue[2])]+index
                lvalue=lvalue[1]
            def w(base,index,to):
                if index==[]:
                    return to
                base[index[0]]=w(base[index[0]],index[1:],to)
                return base
            if lvalue[0]==Var:
                scope.set(lvalue[1],w(scope.find(lvalue[1]),index,to))
            else:
                w(run(lvalue),index,to)
        elif tp==NoOp:
            return None
        elif tp==Import:
            _v=run(tree[1])
            for k,v in _v.items():
                scope.define(k,v)
        elif tp==Const:
            return tree[1]
        elif tp==Var:
            return scope.find(tree[1])
        elif tp==Binary:
            op=tree[1]
            l=run(tree[2])
            r=run(tree[3])
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
                '*and':lambda a,b:a and b,
                '*or':lambda a,b:a or b,
                '&':lambda a,b:a&b,
                '|':lambda a,b:a|b,
                '^':lambda a,b:a^b,
            }[op](l,r)
        elif tp==Unary:
            op=tree[1]
            l=run(tree[2])
            return {
                '+':lambda a:+a,
                '-':lambda a:-a,
                '*not':lambda a:not a,
                '~':lambda a:~a,
            }[op](l)
        elif tp==Index:
            l,r=run(tree[1]),run(tree[2])
            if type(l)==dict and type(l[r])==Function:
                return Method(l,l[r])
            return l[r]
        elif tp==Call:
            return run(tree[1])(*map(run,tree[2]))
        elif tp==NewObject:
            return dict(zip(tree[1],map(run,tree[2])))
        elif tp==NewList:
            return list(map(run,tree[1]))
        elif tp==NewFn:
            return Function(tree[1],tree[2],scope)
        elif tp==Where:
            expr,body=tree[1],tree[2]
            scope=Scope(scope,{})
            run_code(body,scope)
            res=run(expr)
            scope=scope.parent
            return res
        else:
            raise Exception(f"未知的语法树类型{tp}。")
        return None
    return run(tree)
scope=Scope(None,{
    "print":lambda *args:print(*args,sep="",end="",flush=True),
    "println":lambda *args:print(*args,sep="",flush=True),
    "make_tuple":lambda *args:args,
    "ord":ord,
    "chr":chr,
    "inputln":input,
    "getchar":lambda:sys.stdin.read(1),
    "len":len,
    "time":{
        "sleep":time.sleep,
        "time":time.time,
    }
})
def _load(file:str):
    run_code(parse(lex(open(file,'r',encoding='utf-8').read())),scope)
scope.var["load"]=_load
def run_file(file:str):
    run_code(parse(lex(open(file,'r',encoding='utf-8').read())),copy.deepcopy(scope))
run_code(parse(lex('''
println("Rain1.0，新的Rain语言
更新的重点是：
1、加快运行速度，达到NewLang级别
2、语法合理化
下面进行速度测试，计算100000的阶乘
")
var t=time.time()
var num=100000
var res=res where(
    var res=1
    for i=1 to num+1
        res=res*i
    end
)
#println(res)
println("用时：",time.time()-t)
println("比NewLang快近2秒！")
''')),scope)
'''
var obj={
    a:10,
    setA:(fn(self,a)
        self.a=a)
    printSelf:(fn(self)
        println("object:a=",self.a))
}
obj.printSelf()
obj.setA(20)
obj.printSelf()

var num=100000
println(res where(
    var res=1
    for i=1 to num+1
        res=res*i
    end
))

var mod={
    pi:3.14
}
println(mod.pi)
import mod
println(pi)

load("mod.nrn")
println(mod.pi)
'''