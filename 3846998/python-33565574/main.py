from os import*
from time import*
class Struct:
    value=[]
    def __init__(self,a):
        self.value=list(a)
    def __str__(self):
        return "struct:{}".format(",".join("{}".format(k) for k in self.value))
class ThisStruct:
    value={}
    def __init__(self,a,b):
        self.value=dict(zip(a,b))
    def set(self,name,v):
        if name not in self.value.keys():
            raise Exception("!")
        self.value[name]=v
def throw(a=""):
    raise Exception("Error:"+a)
def Tokenize(s):
    pos=0
    ls=""
    ans=[]
    s+=" "
    while pos<len(s):
        if s[pos]=="\"":
            if ls!="":
                ans.append(ls)
                ls=""
            ls+="\""
            pos+=1
            while pos<len(s):
                ls+=s[pos]
                if s[pos]=="\"":
                    break
                pos+=1
            else:
                throw("wrong input!")
            ans.append(ls)
            ls=""
        elif s[pos] in " \n\t\r":
            if ls!="":
                ans.append(ls)
                ls=""
        elif s[pos] in "()":
            if ls!="":
                ans.append(ls)
                ls=""
            ans.append(s[pos])
        else:
            ls+=s[pos]
        pos+=1
    return ans
module={}
module["screen-drawing"]=Tokenize('''
var screen(list)
func init()
    var i 0
    while(< i 20)
        var j 0
        var x(list)
        while(< j 20)
            let x(+ x(list 0))
            let j(+ j 1)
        end
        let screen(+ screen(list x))
        let i(+ 1 i)
    end
end
func show()
    var i 0
    while(< i 20)
        var j 0
        while(< j 20)
            output([]([] screen i)j)
            let j(+ j 1)
        end
        output newline
        let i(+ 1 i)
    end
end
func write(x y c)
    modify screen(list x y)c
end
''')
module["time"]=Tokenize('''
func time()
    return time
end
func sleep(t)
    var l(time)
    while 1
        if(>=(-(time)l)t)
            break
        end
    end
end
''')
def allnum(a):
    for i in a:
        if i not in "0123456789":
            return 0
    return 1
def if_float(a):
    try:
        float(a)
        return 1
    except:
        return 0
class Scope:
    var={}
    func={}
    parent=None
    def __init__(self,p):
        self.var={}
        self.func={}
        self.parent=p
    def find(self,name):
        t=self
        while t!=None:
            if name in t.var.keys():
                return t.var[name]
            t=t.parent
    def findf(self,name):
        t=self
        while t!=None:
            if name in t.func.keys():
                return t.func[name]
            t=t.parent
def getpair(st,pos):
    if st[pos]!="(":
        return pos
    l=1
    r=0
    p=pos
    for i in st[pos+1:]:
        p+=1
        if i=="(":
            l+=1
        if i==")":
            r+=1
            if l>0:
                r-=1
                l-=1
        if l==0:
            return(p)
def getpair2(st,pos):
    l=1
    r=0
    p=pos
    for i in st[pos+1:]:
        p+=1
        if i in ["if","while","func"]:
            l+=1
        if i=="end":
            r+=1
            if l>0:
                r-=1
                l-=1
        if l==0:
            return(p)
def preval(a):
    if type(a)==tuple and a[0]=="return":
        return preval(a[1])
    return a
def run(c,scope):
    i=0
    while i<len(c):
        if c[i]=="output":
            i+=1
            print(preval(expr(c[i:getpair(c,i)+1],scope)),end="")
            i=getpair(c,i)
        elif c[i]=="var":
            i+=1
            v=preval(expr(c[i+1:getpair(c,i+1)+1],scope))
            scope.var[c[i]]=v
            i=getpair(c,i+1)
        elif c[i]=="if":
            i+=1
            cond=c[i:getpair(c,i)+1]
            i=getpair(c,i)
            code=c[i:getpair2(c,i)]
            i=getpair2(c,i)
            if preval(expr(cond,scope)):
                ls=run(code,Scope(scope))
                if ls=="break":
                    return "break"
                elif ls=="continue":
                    return "continue"
                elif type(ls)==tuple:
                    return ls
        elif c[i]=="while":
            i+=1
            cond=c[i:getpair(c,i)+1]
            i=getpair(c,i)
            code=c[i:getpair2(c,i)]
            i=getpair2(c,i)
            while preval(expr(cond,scope)):
                ls=run(code,Scope(scope))
                if ls=="break":
                    break
                elif type(ls)==tuple:
                    return ls
        elif c[i]=="let":
            i+=1
            name=c[i]
            value=preval(expr(c[i+1:getpair(c,i+1)+1],scope))
            i=getpair(c,i+1)
            if scope.find(name)==None:
                raise Exception("!")
            t=scope
            while t!=None:
                if name in t.var.keys():
                    t.var[name]=value
                    break
                t=t.parent
        elif c[i]=="read":
            i+=1
            name=c[i]
            if scope.find(name)==None:
                raise Exception("!")
            value=type(scope.find(c[i]))(input())
            t=scope
            while t!=None:
                if name in t.var.keys():
                    t.var[name]=value
                    break
                t=t.parent
            else:
                raise Exception("!")
        elif c[i]=="break":
            return "break"
        elif c[i]=="continue":
            return "continue"
        elif c[i]=="func":
            i+=1
            name=c[i]
            i+=1
            para=c[i+1:getpair(c,i)]
            i=getpair(c,i)
            code=c[i+1:getpair2(c,i)]
            i=getpair2(c,i)
            scope.func[name]=[para,code]
        elif c[i]=="return":
            i+=1
            return ("return",expr(c[i:getpair(c,i)+1],scope))
        elif c[i]=="modify":
            i+=1
            name=c[i]
            if scope.find(name)==None:
                raise Exception("!")
            i+=1
            l=expr(c[i:getpair(c,i)+1],scope)
            i=getpair(c,i)+1
            val=expr(c[i:getpair(c,i)+1],scope)
            i=getpair(c,i)
            t=scope
            while t!=None:
                if name in t.var.keys():
                    exec("t.var[name]"+"".join("["+repr(i)+"]" for i in l)+"="+str(val))
                    break
                t=t.parent
            else:
                raise Exception("!")
        elif c[i]=="clear":
            system("clear")
        elif c[i]=="import":
            i+=1
            run(module[c[i]],scope)
        elif c[i]=="(":
            expr(c[i:getpair(c,i)+1],scope)
        elif c[i]=="set":
            i+=1
            name=c[i]
            i+=1
            w=preval(expr(c[i:getpair(c,i)+1],scope))
            i=getpair(c,i)
            value=preval(expr(c[i+1:getpair(c,i+1)+1],scope))
            i=getpair(c,i+1)
            if scope.find(name)==None:
                raise Exception("!")
            t=scope
            while t!=None:
                if name in t.var.keys():
                    t.var[name].set(w,value)
                    break
                t=t.parent
        elif c[i]=="del":
            i+=1
            name=c[i]
            if scope.find(name)==None:
                raise Exception("!")
            t=scope
            while t!=None:
                if name in t.var.keys():
                    del t.var[name]
                    break
                t=t.parent
        i+=1
def getargs(c,i,scope):
    args=[]
    while i<len(c)-1:
        args.append(preval(expr(c[i:getpair(c,i)+1],scope)))
        i=getpair(c,i)+1
    return args
def xsum(a):
    ans=a[0]
    for i in a[1:]:
        ans+=i
    return ans
def expr(c,scope):
    if c[0]!="(":
        if allnum(c[0]):
            return int(c[0])
        elif if_float(c[0]):
            return float(c[0])
        elif scope.find(c[0])!=None:
            return scope.find(c[0])
        elif c[0][0]=="\"" and c[0][-1]=="\"":
            return c[0][1:-1]
        elif c[0][0]=="$":
            return c[0][1:]
        elif c[0]=="True":
            return True
        elif c[0]=="False":
            return False
        elif c[0]=="None":
            return None
        elif c[0]=="time":
            return time()
    else:
        i=1
        if c[i]=="list":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            return args
        elif c[i]=="char":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=1:
                raise Exception("!")
            return chr(args[0])
        elif c[i]=="sqrt":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=1:
                raise Exception("!")
            return args[0]**0.5
        elif c[i]=="unicode":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=1:
                raise Exception("!")
            return ord(args[0])
        elif c[i]=="init":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=1:
                raise Exception("!")
            s=args[0]
            if type(s)!=Struct:
                raise Exception("!")
            return ThisStruct(s.value,[0 for i in range(len(s.value))])
        elif c[i]=="len":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=1:
                raise Exception("!")
            return len(args[0])
        elif c[i]=="type":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=1:
                raise Exception("!")
            return {int:"int",str:"string",bool:"bool",float:"float",list:"list",dict:"dict",type(None):"NoneType",ThisStruct:"struct"}[type(args[0])]
        elif c[i]=="pow":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=2:
                raise Exception("!")
            return args[0]**args[1]
        elif c[i]=="slice":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=3:
                raise Exception("!")
            return args[0][args[1]:args[2]]
        elif c[i]=="keys":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=1:
                raise Exception("!")
            return list(args[0].keys())
        elif c[i]=="values":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=1:
                raise Exception("!")
            return list(args[0].values())
        elif c[i]=="get":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=2:
                raise Exception("!")
            return args[0].value[args[1]]
        elif c[i]=="struct":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            return Struct(args)
        elif c[i]=="dict":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=2:
                raise Exception("!")
            return dict(zip(args[0],args[1]))
        elif c[i]=="[]":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=2:
                raise Exception("!")
            return args[0][args[1]]
        elif c[i]=="+":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            return xsum(args)
        elif c[i]=="-":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)==1:
                return -args[0]
            return args[0]-xsum(args[1:])
        elif c[i]=="*":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            ans=1
            for j in args:
                ans*=j
            return ans
        elif c[i]=="/":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            ans=args[0]
            for j in args[1:]:
                ans/=j
            return ans
        elif c[i]=="%":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=2:
                raise Exception("!")
            return args[0]%args[1]
        elif c[i]=="=":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            ans=True
            for j in range(len(args)-1):
                ans=args[j]==args[j+1]
                if ans==False:
                    return ans
            return ans
        elif c[i]=="!=":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            ans=True
            for j in range(len(args)-1):
                ans=args[j]!=args[j+1]
                if ans==False:
                    return ans
            return ans
        elif c[i]==">":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            ans=True
            for j in range(len(args)-1):
                ans=args[j]>args[j+1]
                if ans==False:
                    return ans
            return ans
        elif c[i]=="<":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            ans=True
            for j in range(len(args)-1):
                ans=args[j]<args[j+1]
                if ans==False:
                    return ans
            return ans
        elif c[i]==">=":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            ans=True
            for j in range(len(args)-1):
                ans=args[j]>=args[j+1]
                if ans==False:
                    return ans
            return ans
        elif c[i]=="<=":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            ans=True
            for j in range(len(args)-1):
                ans=args[j]<=args[j+1]
                if ans==False:
                    return ans
            return ans
        elif c[i]=="and":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            ans=args[0]
            for j in range(1,len(args)):
                if ans==False:
                    return ans
                ans=ans and args[j]
            return ans
        elif c[i]=="or":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            for j in args:
                if j:
                    return True
            return False
        elif c[i]=="not":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=1:
                raise Exception("!")
            return not args[0]
        elif scope.findf(c[i])!=None:
            f=scope.findf(c[i])
            para=f[0]
            code=f[1]
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=len(para):
                raise Exception("!")
            fscope=Scope(scope)
            for k,v in dict(zip(para,args)).items():
                fscope.var[k]=v
            return run(code,fscope)
print('''temp-integer3.0.0
暂时没有教程
这是判断质数的函数的代码
func prime(a)
    if(< a 2)
        return False
    end
    var i 2
    while(< i a)
        if(=(% a i)0)
            return False
        end
        let i(+ i 1)
    end
    return True
end
这是调用
output(prime 2)''')
o=input("1、写代码 2、查看库源码 请选择：")
if o=="1":
    code=""
    print("可以写代码了，EOF结束")
    while 1:
        a=input()
        if a=="EOF":
            break
        code+="\n"+a
    print("\n\033[1;33m代码运行开始\033[1;0m")
    MainScope=Scope(None)
    run(Tokenize('''var newline(char 10)var back(char 8)var tab(char 9)var space(char 32)'''),MainScope)
    run(Tokenize(code),MainScope)
    print("\n\033[1;33m代码运行结束\033[1;0m")
elif o=="2":
    print('''screen-drawing库：尽管实际不能画图，但是我还是起了这个名字
代码：
var screen(list)
func init()
    var i 0
    while(< i 20)
        var j 0
        var x(list)
        while(< j 20)
            let x(+ x(list 0))
            let j(+ j 1)
        end
        let screen(+ screen(list x))
        let i(+ 1 i)
    end
end
func show()
    var i 0
    while(< i 20)
        var j 0
        while(< j 20)
            output([]([] screen i)j)
            let j(+ j 1)
        end
        output newline
        let i(+ 1 i)
    end
end
func write(x y c)
    modify screen(list x y)c
end

time库
代码：
func time()
    return time
end
func sleep(t)
    var l(time)
    while 1
        if(>=(-(time)l)t)
            break
        end
    end
end
''')
'''
var a 0
read a
var i 2
var flag True
if(< a 2)
    let flag False
end
while(< i a)
    if(=(% a i)0)
        let flag False
        break
    end
    let i(+ i 1)
end
output flag

func a(para)
    return(+ para 1)
end
output(a 1)

func prime(a)
    if(< a 2)
        return False
    end
    var i 2
    while(< i a)
        if(=(% a i)0)
            return False
        end
        let i(+ i 1)
    end
    return True
end
output(prime 2)

func add(a b)
    return(+ a b)
end
output(add 1 2)

func put(a)
    output a
end
(put 10)

output(char 65)

func bool(a)
    if a
        return True
    end
    return False
end
output(bool 1)

func reverse(a)
    var ans ""
    var i 0
    while(< i(len a))
        let ans(+([] a i)ans)
        let i(+ 1 i)
    end
    return ans
end
output(reverse "123")

var l(list 1 2)
modify l(list 0)3
output l

var newline(char 10)
var back(char 8)
var tab(char 9)
var space(char 32)
output newline

clear

output time

output(dict(list "a")(list 1))

func fac(a)
    if(= a 0)
        return 1
    end
    return(* a(fac(- a 1)))
end
output(fac 10)

output(struct $a $b $c)

output(get(init(struct $a $b $c))$a)

var a(struct $a $b $c)
var A(init a)
set A $c 1
output(get A $c)

var a 0
del a
output a
'''