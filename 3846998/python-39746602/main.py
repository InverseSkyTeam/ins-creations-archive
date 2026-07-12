import copy,sys,os,time
class pair:
    def __init__(self,first,second):
        self.first,self.second=first,second
    __str__=__repr__=lambda self:f"({self.first},{self.second})"
class Lexer:
    def __init__(self,text):
        self.text=text
    def c(self):
        self.text=self.text[1:]
    def get(self):
        if self.text=="":
            return ""
        while self.text[0] in " \n\t":
            self.c()
            if self.text=="":
                return ""
        if self.text=="":
            return ""
        if self.text[0]=='(':
            self.c()
            return "("
        elif self.text[0]==')':
            self.c()
            return ")"
        else:
            s=""
            while self.text[0] not in " \n\t()":
                s+=self.text[0]
                self.c()
            return s
class Unit:
    def __init__(self,token):
        self.token=token
    __str__=__repr__=lambda self:self.token
class Call:
    def __init__(self,things):
        self.things=things
    __str__=__repr__=lambda self:"({})".format(" ".join([str(i) for i in self.things]))
class Parser:
    def __init__(self,lexer):
        self.lexer=lexer
        self.tk=lexer.get()
    def eat(self):
        tk=self.tk
        self.tk=self.lexer.get()
        return tk
    def parse(self):
        if self.tk==")":
            raise Exception("语法错误")
        if self.tk!="(":
            return Unit(self.eat())
        self.eat()
        args=[]
        while self.tk!=")":
            args.append(self.parse())
        self.eat()
        return Call(args)
class Scope:
    def __init__(self,parent=None):
        self.parent=parent
        self.var={}
    def find(self,name):
        if name in self.var:
            return self.var[name]
        if self.parent!=None:
            return self.parent.find(name)
        raise Exception("未定义的变量")
    def set(self,name,value):
        if name in self.var:
            self.var[name]=value
            return
        if self.parent!=None:
            return self.parent.set(name,value)
        raise Exception("未定义的变量")
class Func:
    def __init__(self,para,body,closure):
        self.para,self.body,self.closure=para,body,closure
class Runner:
    def __init__(self,tree,scope):
        self.tree=tree
        self.scope=scope
    def run_tree(self,tree):
        if type(tree)==Unit:
            s=tree.token
            if s.isdigit():
                return int(s)
            elif s[0]==s[-1]=='"':
                s=s[1:-1]
                _s=""
                i=0
                while i<len(s):
                    if s[i]=='\\':
                        i+=1
                        _s+={
                            '\\':'\\',
                            'n':'\n',
                            't':'\t',
                            'r':'\r',
                            '"':'"',
                        }[s[i]]
                    else:
                        _s+=s[i]
                    i=i+1
                return _s
            else:
                return self.scope.find(s)
        else:
            func=tree.things[0]
            if type(func)==Unit and func.token in ("fn","if","begin","var","set!"):
                if func.token=="fn":
                    para=[]
                    for i in tree.things[1].things:
                        if type(i)!=Unit:
                            raise Exception("语法错误")
                        para.append(i.token)
                    body=tree.things[-1]
                    return Func(para,body,self.scope)
                if func.token=="if":
                    if self.run_tree(tree.things[1]):
                        return self.run_tree(tree.things[2])
                    return self.run_tree(tree.things[3])
                if func.token=="begin":
                    if len(tree.things)==1:
                        return None
                    return [self.run_tree(i) for i in tree.things[1:]][-1]
                if func.token=="var":
                    self.scope.var[tree.things[1].token]=self.run_tree(tree.things[2])
                if func.token=="set!":
                    self.scope.set(tree.things[1].token,self.run_tree(tree.things[2]))
            else:
                func=self.run_tree(func)
                args=[self.run_tree(i) for i in tree.things[1:]]
                if type(func)==Func:
                    self_scope=self.scope
                    self.scope=Scope(func.closure)
                    self.scope.var=dict(zip(func.para,args))
                    if len(args)>len(func.para):
                        self.scope.var[func.para[-1]]=args[len(func.para)-1:]
                    res=self.run_tree(func.body)
                    self.scope=self_scope
                    return res
                else:
                    return func(*args)
    def run(self):
        return self.run_tree(self.tree)
def _pair(*args):
    return pair(*args)
def add(*args):
    res=args[0]
    for i in args[1:]:
        res+=i
    return res
def sub(*args):
    if len(args)==1:
        return -args[0]
    return args[0]-sum(args[1:])
def mul(*args):
    res=args[0]
    for i in args[1:]:
        res*=i
    return res
def div(*args):
    return args[0]/args[1]
def mod(*args):
    return args[0]%args[1]
def eq(*args):
    for i in args[1:]:
        if i!=args[0]:
            return 0
    return 1
def ne(*args):
    for i in args[1:]:
        if i==args[0]:
            return 1
    return 0
def gt(*args):
    tmp=args[0]
    for i in args[1:]:
        if i<=tmp:
            return 0
        tmp=i
    return 1
def lt(*args):
    tmp=args[0]
    for i in args[1:]:
        if i>=tmp:
            return 0
        tmp=i
    return 1
def ge(*args):
    tmp=args[0]
    for i in args[1:]:
        if i<tmp:
            return 0
        tmp=i
    return 1
def le(*args):
    tmp=args[0]
    for i in args[1:]:
        if i>tmp:
            return 0
        tmp=i
    return 1
def set_car(l,to):
    l=copy.deepcopy(l)
    l[0]=to
    return l
def set_cdr(l,to):
    l=copy.deepcopy(l)
    l[1:]=to
    return l
def set_first(l,to):
    l=copy.deepcopy(l)
    l.first=to
    return l
def set_second(l,to):
    l=copy.deepcopy(l)
    l.second=to
    return l
main=Scope()
main.var={
    "null":None,
    "car":lambda l:l[0],
    "cdr":lambda l:l[1:],
    "set-first":set_first,
    "set_second":set_second,
    "set-car":set_car,
    "set-cdr":set_cdr,#注意：这些都不是破坏性的
    "empty?":lambda l:int(l==[]),
    "null?":lambda a:int(a==None),
    "print":lambda *args:print(*args,end="",sep=""),
    "println":lambda *args:print(*args,sep=""),
    "getchar":lambda:ord(sys.stdin.read(1)),
    "putchar":lambda a:print(chr(a),end=""),
    "first":lambda a:a.first,
    "second":lambda a:a.second,
    "pair":_pair,
    "ord":ord,
    "chr":chr,
    "system":os.system,
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
    "and":lambda *args:int(all(args)),
    "or":lambda *args:int(any(args)),
}
tree=Parser(Lexer('''
(begin
    (var list (fn(l)l))
    (var length (fn(lst)(if (empty? lst) 0 (+(length (cdr lst))1))))
    (var nth (fn(lst n)(if (= n 0)(car lst)(nth (cdr lst)(- n 1)))))
    (var set-nth (fn(lst n v)(if(= n 0)(set-car lst v)(set-cdr lst (set-nth (cdr lst) (- n 1) v)))))
    (var not (fn(v)(= v 0)))
    (var cut-r (fn(s r)(if(= r 0) "" (+ (car s)(cut-r (cdr s) (- r 1))))))
    (var cut-l (fn(s l)(if(= l 0) s (cut-l (cdr s) (- l 1)))))
    (var greet (fn()(println "Hello,world!")))
    (greet)
    (println (cut-r "Hello,world!" 6))
    (println (cut-l "Hello,world!" 6))
)
''')).parse()
Runner(tree,main).run()