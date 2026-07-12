from time import*
var={}
array={}
def getpair(st,pos):
    l=1
    r=0
    p=pos
    for i in st[pos+1:]:
        p+=1
        if i=="[":
            l+=1
        if i=="]":
            r+=1
            if l>0:
                r-=1
                l-=1
        if l==0:
            return(p)
def cut1(code):
    ans=[]
    i=0
    while i<len(code):
        if code[i]=="[":
            ans.append([code[i+1:getpair(code,i)]])
            i=getpair(code,i)
        else:
            if len(ans)>0 and type(ans[-1])==str:
                ans[-1]+=code[i]
            else:
                ans.append(code[i])
        i+=1
    return(ans)
def check(a):
    while "" in a:
        a.remove("")
    return(a)
def xint(a):
    try:
        return(int(a))
    except:
        return(None)
varname="_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
operator=["+","-","*","/","%","==","!=",">","<",">=","<=","and","or"]
def hz_js(ml):
    ml=ml.split(".")
    stack=[]
    for i in ml:
        if xint(i)!=None:
            stack.append(xint(i))
        else:
            if i not in operator:
                return(None)
            if len(stack)<2:
                return(None)
            a=stack[-2]
            b=stack[-1]
            stack=stack[0:-2]
            stack.append(int(eval(str(a)+" "+i+" "+str(b))))
            if stack[-1]==True:
                stack[-1]=1
            if stack[-1]==False:
                stack[-1]=0
    if len(stack)==1:
        return(stack[0])
    return(None)
def xtype(a):
    if a=="":
        return(0)
    try:
        a=int(a)
        return(int,a)
    except:
        try:
            a=float(a)
            return(float,a)
        except:
            if a=="True":
                return(bool,True)
            if a=="False":
                return(bool,False)
            if a[0]=='"' and a[-1]=='"':
                return(str,a[1:-1])
            return(0)
def getvar(name):
    try:
        return(var[name])
    except:
        return(None)
def getarr(name):
    try:
        return(array[name])
    except:
        return(None)
def pd(code,count=[3]):
    return(len(code) in count)
def ifint(text):
    try:
        return(int(text))
    except:
        return(None)
def jy(name):
    if name=="":
        return(0)
    if name[0] in "123456789":
        return(0)
    for i in name:
        if i not in "_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890":
            return(0)
    return(1)
def bc():
    print("错误！")
def getvarinhz(ml):
    ml=check(ml.split("."))
    for i in range(len(ml)):
        name=""
        _else=""
        a0=False
        for j in ml[i]:
            if j in varname and not a0:
                name+=j
            else:
                _else+=j
                a0=True
        if getvar(name)!=None:
            ml[i]=str(getvar(name))
        elif getarr(name)!=None:
            if xint(_else[1:-1])!=None:
                ml[i]=str(getarr(name)[xint(_else[1:-1])])
            elif getvar(_else[1:-1])!=None:
                ml[i]=str(getarr(name)[getvar(_else[1:-1])])
        elif name=="input":
            try:
                ml[i]=input("输入：")
            except:
                bc()
        elif name=="len":
            if "(" in _else and ")" in _else:
                if getarr(_else[1:-1])==None:
                    bc()
                else:
                    ml[i]=str(len(getarr(_else[1:-1])))
            else:
                bc()
        '''elif getfunc(name)!=None:
            argl={}
            arg=_else[1:-1].split(",")
            for xx in range(len(arg)):
                argl[getfunc(name)[0][xx]]=arg[xx]
            ml[i]=str(funcrun(getfunc(name)[1],argl))'''
    return(".".join(ml))
def exp(e):
    return(hz_js(getvarinhz(e)))
def cut2(code):
    code=code.replace("\n","").replace("    ","").replace("    ","")
    code=cut1(code)
    ans=[]
    for i in range(len(code)):
        if type(code[i])==str:
            ans+=check(code[i].split(" "))
        else:
            ans+=[code[i][0]]
    return(ans)
def getne(n):
    if "[" not in n or "]" not in n:
        return([n,""])
    return([n[0:n.index("[")],n[n.index("[")+1:n.index("]")]])
def run(code):
    global var,array
    code=cut2(code)
    i=0
    while i<len(code):
        ml=code[i]
        if ml=="var":
            vs=code[i+1].split(",")
            for j in vs:
                v=j.split("=")
                if len(v)!=2:
                    bc()
                    return()
                aaa=exp(v[1])
                if jy(v[0])==0 or aaa==None:
                    bc()
                    return()
                var[v[0]]=aaa
        if ml=="list":
            vs=code[i+1].split(",")
            for j in vs:
                if jy(j)==0:
                    bc()
                    return()
                array[j]=[]
        if ml=="put":
            ps=code[i+1].split(",")
            for j in ps:
                aaa=exp(j)
                if aaa!=None:
                    print(aaa,end="")
                elif xtype(j)!=0:
                    print(xtype(j)[1],end="")
                elif j=="\\n":
                    print()
                elif j=="space":
                    print(" ",end="")
                elif getarr(j)!=None:
                    print(getarr(j),end="")
                else:
                    bc()
                    return()
        if ml=="let":
            ls=code[i+1].split(",")
            for j in ls:
                v=j.split("=")
                if len(v)!=2:
                    bc()
                    return()
                aaa=exp(v[1])
                if aaa==None:
                    bc()
                    return()
                nm,el=getne(v[0])
                if getvar(nm)!=None and el=="":
                    var[nm]=aaa
                elif getarr(nm)!=None and xint(el)!=None:
                    if xint(el)>=len(getarr(nm)):
                        bc()
                        return()
                    array[nm][xint(el)]=aaa
                else:
                    bc()
                    return()
        if ml=="sizeup":
            if getarr(code[i+1])==None:
                bc()
                return()
            array[code[i+1]].append(0)
        if ml=="sizedown":
            if getarr(code[i+1])==None:
                bc()
                return()
            array[code[i+1]]=getarr(code[i+1])[0:-1]
        if ml=="if":
            aaa=exp(code[i+1])
            if aaa==None:
                bc()
                return()
            try:
                if code[i+3]!="else":
                    bc()
                    return()
                if aaa:
                    run(code[i+2])
                else:
                    run(code[i+4])
            except:
                bc()
                return()
        if ml=="repeat":
            aaa=exp(code[i+1])
            if aaa==None:
                bc()
                return()
            try:
                for j in range(aaa):
                    run(code[i+2])
            except:
                bc()
                return()
        if ml=="while":
            aaa=exp(code[i+1])
            if aaa==None:
                bc()
                return()
            try:
                while(aaa):
                    run(code[i+2])
                    aaa=exp(code[i+1])
            except:
                bc()
                return()
        if ml=="wait":
            aaa=exp(code[i+1])
            if aaa==None:
                bc()
                return()
            sleep(aaa)
        if ml=="getstr":
            if getarr(code[i+1])==None:
                bc()
                return()
            aaa=input("输入：")
            for j in aaa:
                array[code[i+1]].append(ord(j))
        if ml=="putchar":
            aaa=exp(code[i+1])
            if aaa==None:
                bc()
                return()
            print(chr(aaa),end="")
        if ml=="putstr":
            if getarr(code[i+1])==None:
                bc()
                return()
            for j in getarr(code[i+1]):
                print(chr(j),end="")
        i+=1
print('''temp-integer——介于integer2与integer3（设想）之间的语言
1.0.1版本
灵感来源于洛谷1322 logo语言
暂时没有教程，这是求n以内所有质数的程序：
var[a=0,count=0,mx=input]
while[a.mx.<][
var[i=2,flag=0]
    if[a.2.<][]
    else[
        while[i.a.<][
            if[a.i.%.0.==.flag.0.==.and][
                let[flag=1]
            ]else[]
            let[i=i.1.+]
        ]if[flag.0.==][
            put[a,\\n]
            let[count=count.1.+]
        ]else[]
    ]let[a=a.1.+]
]put["数量：",count,\\n]
end
可以写代码了''')
code=""
while 1:
    a=input()
    if a=="end":
        break
    code+="\n"+a
print("\n\033[1;33m代码运行开始\033[1;0m")
run(code)
print("\n\033[1;33m代码运行结束\033[1;0m")
r'''
var[a=0,count=0,mx=input]
while[a.mx.<][
var[i=2,flag=0]
    if[a.2.<][]
    else[
        while[i.a.<][
            if[a.i.%.0.==.flag.0.==.and][
                let[flag=1]
            ]else[]
            let[i=i.1.+]
        ]if[flag.0.==][
            put[a,\n]
            let[count=count.1.+]
        ]else[]
    ]let[a=a.1.+]
]put["数量：",count,\n]
end

if 1[
    put 1
]else[
    put 0
]
end

list[a]
getstr[a]
putstr[a]
putchar[a[0]]
end

if 1[
    if 0[
        put 1
    ]else[]
]else[]
end

list[a]
var[i=0]
while[i.10.<][
    sizeup[a]
    let[i=i.1.+]
]put[len(a).len(a).+]
end
'''