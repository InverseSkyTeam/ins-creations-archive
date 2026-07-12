import sys
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
    def __init__(self,func,args):
        self.func,self.args=func,args
    __str__=__repr__=lambda self:"({} {})".format(str(self.func)," ".join([str(i) for i in self.args]))
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
        func=self.parse()
        args=[]
        while self.tk!=")":
            args.append(self.parse())
        self.eat()
        return Call(func,args)
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
            else:
                return self.scope.find(s)
        else:
            func=tree.func
            if type(func)==Unit and func.token in ("fn","if","begin","var"):
                if func.token=="fn":
                    para=[]
                    for i in [tree.args[0].func]+tree.args[0].args:
                        if type(i)!=Unit:
                            raise Exception("语法错误")
                        para.append(i.token)
                    body=tree.args[-1]
                    return Func(para,body,self.scope)
                if func.token=="if":
                    if self.run_tree(tree.args[0]):
                        return self.run_tree(tree.args[1])
                    return self.run_tree(tree.args[2])
                if func.token=="begin":
                    try:
                        return [self.run_tree(i) for i in tree.args][-1]
                    except:
                        return None
                if func.token=="var":
                    self.scope.var[tree.args[0].token]=self.run_tree(tree.args[1])
            else:
                func=self.run_tree(func)
                args=[self.run_tree(i) for i in tree.args]
                if type(func)==Func:
                    self_scope=self.scope
                    self.scope=Scope(func.closure)
                    self.scope.var=dict(zip(func.para,args))
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
    return sum(args)
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
main=Scope()
main.var={
    "isnull?":lambda a:int(a==None),
    "null":None,
    "print":lambda *args:print(*args,end="",sep=""),
    "println":lambda *args:print(*args,sep=""),
    "pair":_pair,
    "first":lambda a:a.first,
    "second":lambda a:a.second,
    "getchar":lambda:ord(sys.stdin.read(1)),
    "putchar":lambda a:print(chr(a),end=""),
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
}
tree=Parser(Lexer('''
(begin
    (var fac (fn(n)(if n (* (fac (- n 1)) n)1)))
    (var fib (fn(n)(
        if (= n 0) 0 
            (if (= n 1) 1 
                (+ (fib (- n 1))(fib (- n 2)))))))
    (println (fac 10))
    (println (fib 10))
    (println (first (pair 10 20)))
)
''')).parse()
Runner(tree,main).run()