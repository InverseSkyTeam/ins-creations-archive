'''
temp-integer3 with type(temp-integer3+)

内置类型：
int
string
bool
float
list
dict
NoneType
'''
from os import*
from time import*
BuiltinFunctions={
    "+ int int":lambda a,b:a+b,
    "+ float float":lambda a,b:a+b,
    "+ float int":lambda a,b:a+b,
    "+ int float":lambda a,b:a+b,
    "+ int bool":lambda a,b:a+b,
    "+ bool int":lambda a,b:a+b,
    "+ bool bool":lambda a,b:a+b,
    "+ string string":lambda a,b:a+b,
    "+ list list":lambda a,b:a+b,
    
    "- int int":lambda a,b:a-b,
    "- float float":lambda a,b:a-b,
    "- int float":lambda a,b:a-b,
    "- float int":lambda a,b:a-b,
    "- int bool":lambda a,b:a-b,
    "- bool int":lambda a,b:a-b,
    "- bool bool":lambda a,b:a-b,
    "__opposite__ int":lambda a:-a,
    "__opposite__ bool":lambda a:-a,
    
    "* int int":lambda a,b:a*b,
    "* int float":lambda a,b:a*b,
    "* float int":lambda a,b:a*b,
    "* float float":lambda a,b:a*b,
    "* int string":lambda a,b:a*b,
    "* string int":lambda a,b:a*b,
    "* int list":lambda a,b:a*b,
    "* list int":lambda a,b:a*b,
    "* bool int":lambda a,b:a*b,
    "* int bool":lambda a,b:a*b,
    "* bool bool":lambda a,b:a*b,
    
    "/ int int":lambda a,b:a/b,
    "/ int float":lambda a,b:a/b,
    "/ float int":lambda a,b:a/b,
    "/ float float":lambda a,b:a/b,
    "/ int bool":lambda a,b:a/b,
    "/ bool int":lambda a,b:a/b,
    "/ bool bool":lambda a,b:a/b,
    
    "% int int":lambda a,b:a%b,
    "% bool bool":lambda a,b:a%b,
    "% int bool":lambda a,b:a%b,
    "% bool int":lambda a,b:a%b,
    "% int float":lambda a,b:a%b,
    "% float int":lambda a,b:a%b,
    "% float float":lambda a,b:a%b,
    
    "> int int":lambda a,b:a>b,
    "> bool bool":lambda a,b:a>b,
    "> int bool":lambda a,b:a>b,
    "> bool int":lambda a,b:a>b,
    "> int float":lambda a,b:a>b,
    "> float int":lambda a,b:a>b,
    "> float float":lambda a,b:a>b,
    "> list list":lambda a,b:a>b,
    "> string string":lambda a,b:a>b,
    
    "< int int":lambda a,b:a<b,
    "< bool bool":lambda a,b:a<b,
    "< int bool":lambda a,b:a<b,
    "< bool int":lambda a,b:a<b,
    "< int float":lambda a,b:a<b,
    "< float int":lambda a,b:a<b,
    "< float float":lambda a,b:a<b,
    "< list list":lambda a,b:a<b,
    "< string string":lambda a,b:a<b,
    
    "= int int":lambda a,b:a==b,
    "= int string":lambda a,b:a==b,
    "= int bool":lambda a,b:a==b,
    "= int float":lambda a,b:a==b,
    "= int list":lambda a,b:a==b,
    "= int dict":lambda a,b:a==b,
    "= int NoneType":lambda a,b:a==b,
    "= string int":lambda a,b:a==b,
    "= string string":lambda a,b:a==b,
    "= string bool":lambda a,b:a==b,
    "= string float":lambda a,b:a==b,
    "= string list":lambda a,b:a==b,
    "= string dict":lambda a,b:a==b,
    "= string NoneType":lambda a,b:a==b,
    "= bool int":lambda a,b:a==b,
    "= bool string":lambda a,b:a==b,
    "= bool bool":lambda a,b:a==b,
    "= bool float":lambda a,b:a==b,
    "= bool list":lambda a,b:a==b,
    "= bool dict":lambda a,b:a==b,
    "= bool NoneType":lambda a,b:a==b,
    "= float int":lambda a,b:a==b,
    "= float string":lambda a,b:a==b,
    "= float bool":lambda a,b:a==b,
    "= float float":lambda a,b:a==b,
    "= float list":lambda a,b:a==b,
    "= float dict":lambda a,b:a==b,
    "= float NoneType":lambda a,b:a==b,
    "= list int":lambda a,b:a==b,
    "= list string":lambda a,b:a==b,
    "= list bool":lambda a,b:a==b,
    "= list float":lambda a,b:a==b,
    "= list list":lambda a,b:a==b,
    "= list dict":lambda a,b:a==b,
    "= list NoneType":lambda a,b:a==b,
    "= dict int":lambda a,b:a==b,
    "= dict string":lambda a,b:a==b,
    "= dict bool":lambda a,b:a==b,
    "= dict float":lambda a,b:a==b,
    "= dict list":lambda a,b:a==b,
    "= dict dict":lambda a,b:a==b,
    "= dict NoneType":lambda a,b:a==b,
    "= NoneType int":lambda a,b:a==b,
    "= NoneType string":lambda a,b:a==b,
    "= NoneType bool":lambda a,b:a==b,
    "= NoneType float":lambda a,b:a==b,
    "= NoneType list":lambda a,b:a==b,
    "= NoneType dict":lambda a,b:a==b,
    "= NoneType NoneType":lambda a,b:a==b,
    
    ">= int int":lambda a,b:a>=b,
    ">= bool bool":lambda a,b:a>=b,
    ">= int bool":lambda a,b:a>=b,
    ">= bool int":lambda a,b:a>=b,
    ">= int float":lambda a,b:a>=b,
    ">= float int":lambda a,b:a>=b,
    ">= float float":lambda a,b:a>=b,
    ">= list list":lambda a,b:a>=b,
    ">= string string":lambda a,b:a>=b,
    
    "<= int int":lambda a,b:a<=b,
    "<= bool bool":lambda a,b:a<=b,
    "<= int bool":lambda a,b:a<=b,
    "<= bool int":lambda a,b:a<=b,
    "<= int float":lambda a,b:a<=b,
    "<= float int":lambda a,b:a<=b,
    "<= float float":lambda a,b:a<=b,
    "<= list list":lambda a,b:a<=b,
    "<= string string":lambda a,b:a<=b,
    
    "!= int int":lambda a,b:a!=b,
    "!= int string":lambda a,b:a!=b,
    "!= int bool":lambda a,b:a!=b,
    "!= int float":lambda a,b:a!=b,
    "!= int list":lambda a,b:a!=b,
    "!= int dict":lambda a,b:a!=b,
    "!= int NoneType":lambda a,b:a!=b,
    "!= string int":lambda a,b:a!=b,
    "!= string string":lambda a,b:a!=b,
    "!= string bool":lambda a,b:a!=b,
    "!= string float":lambda a,b:a!=b,
    "!= string list":lambda a,b:a!=b,
    "!= string dict":lambda a,b:a!=b,
    "!= string NoneType":lambda a,b:a!=b,
    "!= bool int":lambda a,b:a!=b,
    "!= bool string":lambda a,b:a!=b,
    "!= bool bool":lambda a,b:a!=b,
    "!= bool float":lambda a,b:a!=b,
    "!= bool list":lambda a,b:a!=b,
    "!= bool dict":lambda a,b:a!=b,
    "!= bool NoneType":lambda a,b:a!=b,
    "!= float int":lambda a,b:a!=b,
    "!= float string":lambda a,b:a!=b,
    "!= float bool":lambda a,b:a!=b,
    "!= float float":lambda a,b:a!=b,
    "!= float list":lambda a,b:a!=b,
    "!= float dict":lambda a,b:a!=b,
    "!= float NoneType":lambda a,b:a!=b,
    "!= list int":lambda a,b:a!=b,
    "!= list string":lambda a,b:a!=b,
    "!= list bool":lambda a,b:a!=b,
    "!= list float":lambda a,b:a!=b,
    "!= list list":lambda a,b:a!=b,
    "!= list dict":lambda a,b:a!=b,
    "!= list NoneType":lambda a,b:a!=b,
    "!= dict int":lambda a,b:a!=b,
    "!= dict string":lambda a,b:a!=b,
    "!= dict bool":lambda a,b:a!=b,
    "!= dict float":lambda a,b:a!=b,
    "!= dict list":lambda a,b:a!=b,
    "!= dict dict":lambda a,b:a!=b,
    "!= dict NoneType":lambda a,b:a!=b,
    "!= NoneType int":lambda a,b:a!=b,
    "!= NoneType string":lambda a,b:a!=b,
    "!= NoneType bool":lambda a,b:a!=b,
    "!= NoneType float":lambda a,b:a!=b,
    "!= NoneType list":lambda a,b:a!=b,
    "!= NoneType dict":lambda a,b:a!=b,
    "!= NoneType NoneType":lambda a,b:a!=b,
    
    "bool int":bool,
    "bool string":bool,
    "bool bool":bool,
    "bool float":bool,
    "bool list":bool,
    "bool dict":bool,
    "bool NoneType":bool,
    
    "char int":lambda a:chr(a),
    
    "unicode string":lambda a:ord(a),
    
    "len list":lambda a:len(a),
    "len string":lambda a:len(a),
    
    "sqrt int":lambda a:a**0.5,
    "sqrt bool":lambda a:a**0.5,
    "sqrt float":lambda a:a**0.5,
    
    "pow int int":lambda a,b:a**b,
    "pow int bool":lambda a,b:a**b,
    "pow int float":lambda a,b:a**b,
    "pow bool int":lambda a,b:a**b,
    "pow bool bool":lambda a,b:a**b,
    "pow bool float":lambda a,b:a**b,
    "pow float int":lambda a,b:a**b,
    "pow float bool":lambda a,b:a**b,
    "pow float float":lambda a,b:a**b,
    
    "slice list int int":lambda a,b,c:a[b:c],
    "slice string int int":lambda a,b,c:a[b:c],
    "slice list int NoneType":lambda a,b,c:a[b:c],
    "slice string int NoneType":lambda a,b,c:a[b:c],
    "slice list int bool":lambda a,b,c:a[b:c],
    "slice string int bool":lambda a,b,c:a[b:c],
    "slice list NoneType int":lambda a,b,c:a[b:c],
    "slice string NoneType int":lambda a,b,c:a[b:c],
    "slice list NoneType NoneType":lambda a,b,c:a[b:c],
    "slice string NoneType NoneType":lambda a,b,c:a[b:c],
    "slice list NoneType bool":lambda a,b,c:a[b:c],
    "slice string NoneType bool":lambda a,b,c:a[b:c],
    "slice list bool int":lambda a,b,c:a[b:c],
    "slice string bool int":lambda a,b,c:a[b:c],
    "slice list bool NoneType":lambda a,b,c:a[b:c],
    "slice string bool NoneType":lambda a,b,c:a[b:c],
    "slice list bool bool":lambda a,b,c:a[b:c],
    "slice string bool bool":lambda a,b,c:a[b:c],
    
    "keys dict":lambda a:list(a.keys()),
    
    "values dict":lambda a:list(a.values()),
    
    "dict list list":lambda a,b:dict(zip(a,b)),
    
    "[] list int":lambda a,b:a[b],
    "[] string int":lambda a,b:a[b],
    "[] list bool":lambda a,b:a[b],
    "[] string bool":lambda a,b:a[b],
    "[] dict int":bool,
    "[] dict string":bool,
    "[] dict bool":bool,
    "[] dict float":bool,
    "[] dict NoneType":bool,
}
class Struct:
    var=[]
    name=""
    def __init__(self,n,v):
        self.name,self.var=n,v
class ThisStruct:
    var={}
    name=""
    def __init__(self,n,v):
        self.name,self.var=n,v
    def set(self,n,v):
        self.var[n]=v
def Type(a):
    if type(a)==ThisStruct:
        return a.name
    return {int:"int",str:"string",bool:"bool",float:"float",list:"list",dict:"dict",type(None):"NoneType"}[type(a)]
def Types(a):
    return " ".join([Type(i) for i in a])
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
    structs={}
    parent=None
    def __init__(self,p):
        self.var={}
        self.func={}
        self.structs={}
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
    def finds(self,name):
        t=self
        while t!=None:
            if name in t.structs.keys():
                return t.structs[name]
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
        if i in ["if","while","func","for",'foreach']:
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
            types=c[i+2:getpair(c,i+1)]
            i=getpair(c,i+1)
            para=c[i+2:getpair(c,i+1)]
            i=getpair(c,i+1)
            code=c[i+1:getpair2(c,i)]
            i=getpair2(c,i)
            scope.func[name+" "+" ".join(types)]=[para,code]
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
        elif c[i]=="for":
            i+=1
            name=c[i]
            i+=1
            begin=preval(expr(c[i:getpair(c,i)+1],scope))
            i=getpair(c,i)+1
            end=preval(expr(c[i:getpair(c,i)+1],scope))
            i=getpair(c,i)+1
            skip=preval(expr(c[i:getpair(c,i)+1],scope))
            i=getpair(c,i)
            code=c[i:getpair2(c,i)]
            i=getpair2(c,i)
            for j in range(begin,end,skip):
                NewScope=Scope(scope)
                NewScope.var[name]=j
                ls=run(code,NewScope)
                if ls=="break":
                    break
                elif type(ls)==tuple:
                    return ls
        elif c[i]=="foreach":
            i+=1
            name=c[i]
            i+=1
            items=preval(expr(c[i:getpair(c,i)+1],scope))
            i=getpair(c,i)
            code=c[i:getpair2(c,i)]
            i=getpair2(c,i)
            for j in items:
                NewScope=Scope(scope)
                NewScope.var[name]=j
                ls=run(code,NewScope)
                if ls=="break":
                    break
                elif type(ls)==tuple:
                    return ls
        elif c[i]=="struct":
            i+=1
            name=c[i]
            i+=1
            var=c[i+1:getpair(c,i)]
            i=getpair(c,i)
            scope.structs[name]=Struct(name,var)
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
def runfunc(f,a,scope):
    para,code=f
    args=a
    NewScope=Scope(scope)
    NewScope.var=dict(zip(para,args))
    return run(code,NewScope)
def expr(c,scope):
    global BuiltinFunctions
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
        elif c[i]=="type":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=1:
                raise Exception("!")
            return Type(args[0])
        elif c[i]=="+":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            ans=args[0]
            for i in args[1:]:
                name="+"+" "+Types([ans,i])
                if name in BuiltinFunctions:
                    ans=BuiltinFunctions[name](ans,i)
                elif scope.findf(name)!=None:
                    ans=runfunc(scope.findf(name),[ans,i],scope)
                else:
                    raise Exception("!")
            return ans
        elif c[i]=="-":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)==1:
                name="__opposite__"+" "+Types([args[0]])
                if name in BuiltinFunctions:
                    return BuiltinFunctions[name](args[0])
                elif scope.findf(name)!=None:
                    return runfunc(scope.findf(name),[args[0]],scope)
                else:
                    raise Exception("!")
            ans=args[0]
            for i in args[1:]:
                name="-"+" "+Types([ans,i])
                if name in BuiltinFunctions:
                    ans=BuiltinFunctions[name](ans,i)
                elif scope.findf(name)!=None:
                    ans=runfunc(scope.findf(name),[ans,i],scope)
                else:
                    raise Exception("!")
            return ans
        elif c[i]=="*":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            ans=args[0]
            for i in args[1:]:
                name="*"+" "+Types([ans,i])
                if name in BuiltinFunctions:
                    ans=BuiltinFunctions[name](ans,i)
                elif scope.findf(name)!=None:
                    ans=runfunc(scope.findf(name),[ans,i],scope)
                else:
                    raise Exception("!")
            return ans
        elif c[i]=="/":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            ans=args[0]
            for i in args[1:]:
                name="/"+" "+Types([ans,i])
                if name in BuiltinFunctions:
                    ans=BuiltinFunctions[name](ans,i)
                elif scope.findf(name)!=None:
                    ans=runfunc(scope.findf(name),[ans,i],scope)
                else:
                    raise Exception("!")
            return ans
        elif c[i] in ["=","!=",">=","<=",">","<"]:
            args=[]
            i+=1
            args=getargs(c,i,scope)
            ans=True
            for j in range(len(args)-1):
                name=c[i-1]+" "+Types([args[j],args[j+1]])
                if name in BuiltinFunctions:
                    ans=BuiltinFunctions[name](args[j],args[j+1])
                elif scope.findf(name)!=None:
                    ans=runfunc(scope.findf(name),[args[j],args[j+1]],scope)
                else:
                    raise Exception("!")
                if ans==False:
                    return ans
            return ans
        elif c[i]=="and":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            for j in args:
                name="bool"+" "+Types([j])
                ans=0
                if name in BuiltinFunctions:
                    ans=BuiltinFunctions[name](j)
                elif scope.findf(name)!=None:
                    ans=runfunc(scope.findf(name),[j],scope)
                else:
                    raise Exception("!")
                if ans==False:
                    return False
            return True
        elif c[i]=="or":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            for j in args:
                name="bool"+" "+Types([j])
                ans=0
                if name in BuiltinFunctions:
                    ans=BuiltinFunctions[name](j)
                elif scope.findf(name)!=None:
                    ans=runfunc(scope.findf(name),[j],scope)
                else:
                    raise Exception("!")
                if ans==True:
                    return True
            return False
        elif c[i]=="not":
            args=[]
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=1:
                raise Exception("!")
            name="bool"+" "+Types(args)
            if name in BuiltinFunctions:
                return not BuiltinFunctions[name](*args)
            elif scope.findf(name)!=None:
                return not runfunc(scope.findf(name),args,scope)
            else:
                raise Exception("!")
        elif c[i]=="init":
            i+=1
            name=c[i]
            s=scope.finds(name)
            v=dict(zip(s.var,[0 for i in range(len(s.var))]))
            return ThisStruct(name,v)
        elif c[i]=="@":
            i+=1
            args=getargs(c,i,scope)
            if len(args)!=2:
                raise Exception("!")
            return args[0].var[args[1]]
        else:
            i+=1
            args=getargs(c,i,scope)
            name=c[i-1]+" "+Types(args)
            if name in BuiltinFunctions:
                return BuiltinFunctions[name](*args)
            elif scope.findf(name)!=None:
                return runfunc(scope.findf(name),args,scope)
            else:
                raise Exception("!")
print('''简介：
所谓加号，并非增强，而是语法的变动
所谓变动，其实只是变成了强类型语言
强到什么程度呢
比如：
定义了string转int的标准方法int(string)（至少可以被视为标准方法）。
然后写了一段代码output(+ 123 "123")，得到了一个错误而不是想象中的246，
原因是1、这是强类型语言，运算符和函数的参数不允许隐式转换
      2、其实这里不识别所谓标准的转换方法，只是把它们看成普通函数
解决方法：
定义+(int string)和+(string int)两个运算符，用func关键字即可
或把代码改成output(+ 123(int "123"))（前提是确实定义了int(string)函数）

这是一个简单的函数
func plus(int int)(a b)
    return(+ a b)
end
''')
code=""
print("可以写代码了，EOF结束")
while 1:
    a=input()
    if a=="EOF":
        break
    code+="\n"+a
print("\n\033[1;33m代码运行开始\033[1;0m")
MainScope=Scope(None)
run(Tokenize(code),MainScope)
print("\n\033[1;33m代码运行结束\033[1;0m")