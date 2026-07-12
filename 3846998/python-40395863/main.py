import copy,sys,os,time
def lex(code:str):
    res=[]
    while code!="":
        while code!="" and code[0] in "\n\t\r ;":
            if code[0]==';':
                code=code[1:]
                while code!="" and code[0]!="\n":
                    code=code[1:]
                code=code[1:]
            else:
                code=code[1:]
        if code=="":
            break
        if code[:2]=="'(":
            res.append(code[:2])
            code=code[2:]
        elif code[0] in ",()":
            res.append(code[0])
            code=code[1:]
        elif code[0]=='"':
            code=code[1:]
            s=''
            while code and code[0]!='"':
                if code[0]=='\\':
                    code=code[1:]
                    if code[0].isdigit():
                        s+=int(code[0:3],base=8)
                        code=code[1:]
                    else:
                        s+={
                            'n':'\n',
                            't':'\t',
                            'r':'\r',
                            '\\':'\\',
                            '"':'"',
                            '\'':'\''
                        }[code[0]]
                        code=code[1:]
                else:
                    s+=code[0]
                    code=code[1:]
            code=code[1:]
            res.append('"'+s+'"')
        else:
            s=""
            while code[0] not in " \n\t\r'()":
                s+=code[0]
                code=code[1:]
            res.append(s)
    return res+[""]
class Comma:
    def __init__(self,v):
        self.v=v
    __str__=__repr__=lambda self:","+str(self.v)
def parse(tk):
    def parse():
        nonlocal tk
        if tk[0]=='(':
            tk=tk[1:]
            l=[]
            while tk[0]!=')':
                l.append(parse())
            tk=tk[1:]
            return l
        if tk[0]=="'(":
            tk=tk[1:]
            l=[]
            while tk[0]!=')':
                l.append(parse())
            tk=tk[1:]
            return tuple(l)
        if tk[0]==',':
            tk=tk[1:]
            return Comma(parse())
        r=tk[0]
        tk=tk[1:]
        return r
    l=[]
    while tk[0]!="":
        l.append(parse())
    return l
class Scope:
    def __init__(self,parent=None):
        self.parent=parent
        self.var={}
    def define(self,name,value):
        self.var[name]=value
    def find(self,name):
        if name in self.var:
            return self.var[name]
        if self.parent!=None:
            return self.parent.find(name)
        raise Exception(f"未定义的变量{name}")
    def set(self,name,value):
        if name in self.var:
            self.var[name]=value
            return
        if self.parent!=None:
            return self.parent.set(name,value)
        raise Exception(f"未定义的变量{name}")
class Func:
    def __init__(self,para,body,closure,args=[]):
        self.para,self.body,self.closure,self.args=para,body,closure,copy.deepcopy(args)
    def call(self,_scope,args):
        if len(self.args)+len(args)!=len(self.para):
            return Func(self.para,self.body,self.closure,self.args+args)
        scope=Scope(self.closure)
        scope.var=dict(zip(self.para,self.args+args))
        return run(self.body,scope)
class Macro:
    def __init__(self,para,body,closure,args=[]):
        self.para,self.body,self.closure,self.args=para,body,closure,copy.deepcopy(args)
    def call(self,_scope,args):
        if len(self.args)+len(args)!=len(self.para):
            return Macro(self.para,self.body,self.closure,self.args+args)
        scope=Scope(self.closure)
        scope.var=dict(zip(self.para,self.args+args))
        tree=run(self.body,scope)
        #print(tree)
        return run(tree,_scope)
def run(tree,scope:Scope):
    if type(tree)==str:
        if tree[0].isdigit():
            if "." in tree:
                return float(tree)
            return int(tree)
        if tree[0]==tree[-1]=='"':
            return tree[1:-1]
        return scope.find(tree)
    if type(tree)==tuple:
        res=[]
        for i in tree:
            if type(i)==Comma:
                res.append(run(i.v,scope))
            else:
                res.append(i)
        return res
    if type(tree)==list:
        fn=run(tree[0],scope)
        if callable(fn):
            return fn(scope,*tree[1:])
        if type(fn)==Func:
            return fn.call(scope,[run(i,scope) for i in tree[1:]])
        if type(fn)==Macro:
            return fn.call(scope,tree[1:])
def add(scope,*args):
    res=run(args[0],scope)
    for i in args[1:]:
        res+=run(i,scope)
    return res
def sub(scope,*args):
    if len(args)==1:
        return -run(args[0],scope)
    return run(args[0],scope)-sum([run(i,scope) for i in args[1:]])
def mul(scope,*args):
    res=run(args[0],scope)
    for i in args[1:]:
        res*=run(i,scope)
    return res
def div(scope,*args):
    return run(args[0],scope)/mul(scope,*args[1:])
def mod(scope,*args):
    return run(args[0],scope)%run(args[1],scope)
def eq(scope,*args):
    e=run(args[0],scope)
    for i in args[1:]:
        if run(i,scope)!=e:
            return 0
    return 1
def ne(scope,*args):
    e=run(args[0],scope)
    for i in args[1:]:
        if run(i,scope)==e:
            return 0
    return 1
def gt(scope,*args):
    tmp=run(args[0],scope)
    for i in args[1:]:
        i=run(i,scope)
        if i>=tmp:
            return 0
        tmp=i
    return 1
def lt(scope,*args):
    tmp=run(args[0],scope)
    for i in args[1:]:
        i=run(i,scope)
        if i<=tmp:
            return 0
        tmp=i
    return 1
def ge(scope,*args):
    tmp=run(args[0],scope)
    for i in args[1:]:
        i=run(i,scope)
        if i>tmp:
            return 0
        tmp=i
    return 1
def le(scope,*args):
    tmp=run(args[0],scope)
    for i in args[1:]:
        i=run(i,scope)
        if i<tmp:
            return 0
        tmp=i
    return 1
def set_car(scope,l,to):
    return [run(to,scope)]+run(l,scope)[1:]
def set_cdr(scope,l,to):
    return run(l,scope)[:1]+run(to,scope)
def _or(scope,*args):
    for i in args:
        if run(i,scope):
            return True
    return False
def _and(scope,*args):
    for i in args:
        if not run(i,scope):
            return False
    return True
def begin(scope,*args):
    if len(args)==0:
        return []
    scope=Scope(scope)
    return [run(i,scope) for i in args][-1]
def _if(scope,cond,t,f):
    if run(cond,scope):
        return run(t,scope)
    return run(f,scope)
def readfile(scope,name):
    name=run(name,scope)
    with open(name,"r") as f:
        return "".join(f.readlines())
def writefile(scope,name,value):
    name=run(name,scope)
    value=run(value,scope)
    with open(name,"w") as f:
        return f.write(str(value))
def addfile(scope,name,value):
    name=run(name,scope)
    value=run(value,scope)
    with open(name,"a") as f:
        return f.write(str(value))
def _module(scope,name,*decl):
    _scope=Scope(scope)
    for i in decl:
        run(i,_scope)
    scope.define(name,_scope.var)
    return _scope.var
def _import(scope,lib):
    lib=run(lib,scope)
    for k,v in lib.items():
        scope.var[k]=v
main=Scope()
main.var={
    "null":None,
    "list":lambda scope,*args:list(run(i,scope) for i in args),
    "car":lambda scope,l:run(l,scope)[0],
    "cdr":lambda scope,l:run(l,scope)[1:],
    "set-car":set_car,
    "set-cdr":set_cdr,#注意：这些都不是破坏性的
    "empty?":lambda scope,l:int(len(run(l,scope))==0),
    "null?":lambda scope,a:int(run(a,scope)==None),
    "print":lambda scope,*args:print(*[run(i,scope) for i in args],end="",sep=""),
    "println":lambda scope,*args:print(*[run(i,scope) for i in args],sep=""),
    "getchar":lambda scope:ord(sys.stdin.read(1)),
    "putchar":lambda scope,a:print(chr(a),end=""),
    "ord":lambda scope,a:ord(a),
    "chr":lambda scope,a:chr(a),
    "system":lambda scope,a:os.system(run(a,scope)),
    "sleep":lambda scope,a:time.sleep(run(a,scope)),
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
    "%":mod,
    "=":eq,
    "!=":ne,
    ">":gt,
    "<":lt,
    ">=":ge,
    "<=":le,
    "and":_and,
    "or":_or,
    "begin":begin,
    "fn":lambda scope,para,body:Func(para,body,scope),
    "macro":lambda scope,para,body:Macro(para,body,scope),
    "var":lambda scope,name,value:scope.define(name,run(value,scope)),
    "set!":lambda scope,name,value:scope.set(name,run(value,scope)),
    "if":_if,
    "floor":lambda scope,a:int(run(a,scope)),
    "read-file":readfile,
    "write-file":writefile,
    "add-file":addfile,
    "py-tostr":lambda scope,v:str(run(v,scope)),
    "module":_module,
    ".":lambda scope,a,b:run(a,scope)[b],
    "import":_import,
    "load-external":lambda scope,name:run(parse(lex(readfile(scope,name))),scope),
}
code='''
(module standard-library
    (var length(fn(lst)(if (empty? lst) 0 (+ (length (cdr lst)) 1))))
    (var nth (fn(lst n)(if (= n 0)(car lst)(nth (cdr lst)(- n 1)))))
    (var set-nth (fn(lst n v)(if(= n 0)(set-car lst v)(set-cdr lst (set-nth (cdr lst) (- n 1) v)))))
    (var not (fn(v)(= v 0)))
    (var cut-r (fn(s r)(if(= r 0) "" (+ (car s)(cut-r (cdr s) (- r 1))))))
    (var cut-l (fn(s l)(if(= l 0) s (cut-l (cdr s) (- l 1)))))
    (var greet (fn()(println "Hello,world!")))
    (var macro-greet (macro()'(println "Hello,world!")))
    (var greet-person (macro(name)'(println "Hello," ,name "!")))
    (var eval (macro(code)code))
    (var while (macro(cond body)'(if ,cond ,'(begin ,body ,'(while ,cond ,body)) null)))
    (var repeat (macro(time body)'(if ,time ,'(begin ,body ,'(repeat ,'(- ,time 1) ,body)) null)))
    (var defun (macro(name para body)'(var ,name ,'(fn ,para ,body))))
    (var defmacro (macro(name para body)'(var ,name ,'(macro ,para ,body))))
    (defun pow2 (n) (* n n))
    (defun pow (n m)(if m (if (% m 2) (* (pow2 (pow n (floor (/ m 2)))) n) (pow2 (pow n (/ m 2)))) 1))
    (defun fac (n)(if n (* (fac (- n 1)) n) 1))
    (defun fib (n)(if (< n 2) n (+ (fib (- n 1)) (fib (- n 2)))))
    (defun sum (lst)(if (empty? lst) 0 (+ (car lst) (sum (cdr lst)))))
    (defun map (fun lst)(if (empty? lst) (list) (+ (list (fun (car lst))) (map fun (cdr lst)))))
    (defun eval-tree (t) (eval '(eval ,t)))
    (defmacro when (cond body)'(if ,cond ,body null))
    (defmacro unless (cond body)'(if ,cond null ,body))
    (defmacro loop (body)'(begin ,body ,'(loop ,body)))
    (defmacro until (cond body)'(if ,cond null ,'(begin ,body ,'(until ,cond ,body))))
    (defmacro for (name begin end step body)'(if ,'(= ,begin ,end) null ,'(begin ,'(,'(fn ,'(,name) ,body) ,begin) ,'(for ,name ,'(+ ,begin ,step) ,end ,step ,body))))
    (defmacro foreach (name lst body)'(if ,'(empty? ,lst) null ,'(begin ,'(,'(fn ,'(,name) ,body) ,'(car ,lst)) ,'(foreach ,name ,'(cdr ,lst) ,body))))
    (defmacro set-car! (a b)'(set! ,a ,'(set-car ,a ,b)))
    (defmacro set-cdr! (a b)'(set! ,a ,'(set-cdr ,a ,b)))
    (defmacro set-nth! (a b c)'(set! ,a ,'(set-nth ,a ,b ,c)))
)
(import standard-library)
;(load-external "./Tiny Lisp/test-module.tlisp")
;(import test-module)
;(println pi)
'''
tree=parse(lex(code))
for i in tree:
    run(i,main)