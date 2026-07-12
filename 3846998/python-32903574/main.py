from time import*
var={}
array={}
const={}
def xgetpair(st,pos,pair):#匹配括号
    l=1
    r=0
    p=pos
    for i in st[pos+1:]:
        p+=1
        if i==list(pair.keys())[0]:
            l+=1
        if i==list(pair.values())[0]:
            r+=1
            if l>0:
                r-=1
                l-=1
        if l==0:
            return(p)
def cutcode(c,op,pairs,cs):#分词，不是生成语法树
    i=0
    ans=[]
    while i<len(c):
        if c[i] in op:
            if ans!=[] and ans[-1]=="":
                ans=ans[0:-1]+[c[i]]
            elif ans==[] or ans[-1][-1] not in op:
                ans.append(c[i])
            else:
                ans[-1]+=c[i]
        elif c[i] in cs:
            if ans[-1] not in cs:
                ans.append("")
        elif c[i] in pairs.keys():
            ans.append(c[i])
            ans.append(c[i+1:xgetpair(c,i,{c[i]:pairs[c[i]]})])
            ans.append(pairs[c[i]])
            i=xgetpair(c,i,{c[i]:pairs[c[i]]})
        else:
            if ans==[]:
                ans.append(c[i])
            elif ans[-1] in op or ans[-1] in pairs.values():
                ans.append(c[i])
            else:
                ans[-1]+=c[i]
        i+=1
    return(ans)
hzop=["+","-","*","/","%",">","<","==",">=","<=","&&","||"]
def hz_js(hz):#后缀表达式计算
    hz=getvarinhz(hz)
    stack=[]
    for i in hz:
        if type(i)==int:
            stack.append(i)
        if i==" ":
            continue
        if i=="+":
            try:
                v=stack[-1]+stack[-2]
                stack=stack[0:-2]+[v]
            except:
                return(None)
        if i=="-":
            try:
                v=stack[-2]-stack[-1]
                stack=stack[0:-2]+[v]
            except:
                return(None)
        if i=="*":
            try:
                v=stack[-1]*stack[-2]
                stack=stack[0:-2]+[v]
            except:
                return(None)
        if i=="/":
            try:
                v=stack[-2]/stack[-1]
                stack=stack[0:-2]+[v]
            except:
                return(None)
        if i=="%":
            try:
                v=stack[-2]%stack[-1]
                stack=stack[0:-2]+[v]
            except:
                return(None)
        if i==">":
            try:
                v=int(stack[-2]>stack[-1])
                stack=stack[0:-2]+[v]
            except:
                return(None)
        if i=="<":
            try:
                v=int(stack[-2]<stack[-1])
                stack=stack[0:-2]+[v]
            except:
                return(None)
        if i=="==":
            try:
                v=int(stack[-1]==stack[-2])
                stack=stack[0:-2]+[v]
            except:
                return(None)
        if i=="<=":
            try:
                v=int(stack[-2]<=stack[-1])
                stack=stack[0:-2]+[v]
            except:
                return(None)
        if i==">=":
            try:
                v=int(stack[-2]>=stack[-1])
                stack=stack[0:-2]+[v]
            except:
                return(None)
        if i=="&&":
            try:
                v=int(bool(stack[-1]) and bool(stack[-2]))
                stack=stack[0:-2]+[v]
            except:
                return(None)
        if i=="||":
            try:
                v=int(bool(stack[-1]) or bool(stack[-2]))
                stack=stack[0:-2]+[v]
            except:
                return(None)
    if len(stack)==1:
        return(stack[0])
    else:
        return(None)
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
def getcon(a):
    try:
        return(const[a])
    except:
        return(None)
def bc():
    print("错误！")
def getvarinhz(ml):#把后缀表达式里的变量换成数字
    ml=cutcode(ml,"+-*/%=|&><",{"[":"]","(":")"},".")
    ans=[]
    i=0
    while i<len(ml):
        try:
            ans.append(int(ml[i]))
        except:
            if ml[i] in hzop:
                ans.append(ml[i])
            elif getvar(ml[i])!=None:
                ans.append(getvar(ml[i]))
            elif getcon(ml[i])!=None:
                asn.append(getcon(ml[1]))
            elif getarr(ml[i])!=None:
                if ml[i+1]!="[" or ml[i+3]!="]":
                    i+=1
                    continue
                aaa=hz_js(ml[i+2])
                if aaa==None or aaa>=len(getarr(ml[i])):
                    i+=1
                    continue
                ans.append(getarr(ml[i])[aaa])
                i=i+3
            elif ml[i]=="input":
                try:
                    ans.append(int(input()))
                except:
                    pass
            elif ml[i]=="len":
                if ml[i+1]!="(" or ml[i+3]!=")" or getarr(ml[i+2])==None:
                    i+=1
                    continue
                ans.append(len(array[ml[i+2]]))
        i+=1        
    return(ans)
def exp(e):
    return(hz_js(e))
def cut2(code):
    code=code.replace("\n"," ").replace("    "," ").replace("    "," ")
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
def delvar(dl):
    global array,var
    for i in dl:
        if getvar(i)!=None:
            del var[i]
        if getarr(i)!=None:
            del array[i]
def run(code):
    global var,array
    code=cut2(code)
    dl=[]
    i=0
    while i<len(code):
        ml=code[i]
        if ml=="var":
            vs=code[i+1].split(",")
            for j in vs:
                v=j.split("=")
                if len(v)!=2:
                    bc()
                    delvar(dl)
                    return()
                aaa=exp(v[1])
                if jy(v[0])==0 or aaa==None:
                    bc()
                    delvar(dl)
                    return()
                var[v[0]]=aaa
                dl.append(v[0])
        if ml=="list":
            vs=code[i+1].split(",")
            for j in vs:
                if jy(j)==0:
                    bc()
                    delvar(dl)
                    return()
                array[j]=[]
                dl.append(j)
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
                    delvar(dl)
                    return()
        if ml=="let":
            ls=code[i+1].split(",")
            for j in ls:
                v=j.split("=")
                if len(v)!=2:
                    bc()
                    delvar(dl)
                    return()
                aaa=exp(v[1])
                if aaa==None:
                    bc()
                    delvar(dl)
                    return()
                nm,el=getne(v[0])
                bbb=exp(el)
                if getvar(nm)!=None and el=="":
                    var[nm]=aaa
                elif getarr(nm)!=None and bbb!=None:
                    if bbb>=len(getarr(nm)):
                        bc()
                        delvar(dl)
                        return()
                    array[nm][bbb]=aaa
                else:
                    bc()
                    delvar(dl)
                    return()
        if ml=="sizeup":
            if getarr(code[i+1])==None:
                bc()
                delvar(dl)
                return()
            array[code[i+1]].append(0)
        if ml=="sizedown":
            if getarr(code[i+1])==None:
                bc()
                delvar(dl)
                return()
            array[code[i+1]]=getarr(code[i+1])[0:-1]
        if ml=="if":
            aaa=exp(code[i+1])
            if aaa==None:
                bc()
                delvar(dl)
                return()
            try:
                if code[i+3]!="else":
                    bc()
                    delvar(dl)
                    return()
                if aaa:
                    xxa=run(code[i+2])
                    if xxa=="continue":
                        delvar(dl)
                        return("continue")
                    if xxa=="break":
                        delvar(dl)
                        return("break")
                    if xxa=="exit":
                        delvar(dl)
                        return("exit")
                else:
                    xxa=run(code[i+4])
                    if xxa=="continue":
                        delvar(dl)
                        return("continue")
                    if xxa=="break":
                        delvar(dl)
                        return("break")
            except:
                bc()
                delvar(dl)
                return()
        if ml=="repeat":
            aaa=exp(code[i+1])
            if aaa==None:
                bc()
                delvar(dl)
                return()
            try:
                for j in range(aaa):
                    xxa=run(code[i+2])
                    if xxa=="break":
                        break
                    if xxa=="exit":
                        delvar(dl)
                        return("exit")
            except:
                bc()
                delvar(dl)
                return()
        if ml=="const":
            vs=code[i+1].split(",")
            for j in vs:
                v=j.split("=")
                if len(v)!=2:
                    bc()
                    delvar(dl)
                    return()
                aaa=exp(v[1])
                if jy(v[0])==0 or aaa==None:
                    bc()
                    delvar(dl)
                    return()
                const[v[0]]=aaa
        if ml=="continue":
            delvar(dl)
            return("continue")
        if ml=="break":
            delvar(dl)
            return("break")
        if ml=="exit":
            delvar(dl)
            return("exit")
        if ml=="while":
            aaa=exp(code[i+1])
            if aaa==None:
                bc()
                delvar(dl)
                return()
            try:
                while(aaa):
                    xxa=run(code[i+2])
                    aaa=exp(code[i+1])
                    if xxa=="break":
                        break
                    if xxa=="exit":
                        delvar(dl)
                        return("exit")
            except:
                bc()
                delvar(dl)
                return()
        if ml=="wait":
            aaa=exp(code[i+1])
            if aaa==None:
                bc()
                delvar(dl)
                return()
            sleep(aaa)
        if ml=="getstr":
            if getarr(code[i+1])==None:
                bc()
                delvar(dl)
                return()
            aaa=input("输入：")
            for j in aaa:
                array[code[i+1]].append(ord(j))
        if ml=="putchar":
            aaa=exp(code[i+1])
            if aaa==None:
                bc()
                delvar(dl)
                return()
            print(chr(aaa),end="")
        if ml=="putstr":
            if getarr(code[i+1])==None:
                bc()
                delvar(dl)
                return()
            for j in getarr(code[i+1]):
                print(chr(j),end="")
        if ml=="del":
            dv=code[i+1].split(",")
            for iii in dv:
                if getvar(iii)!=None:
                    del var[iii]
                elif getarr(iii)!=None:
                    del array[iii]
                else:
                    bc()
                    delvar(dl)
                    return()
        i+=1
    delvar(dl)
print('''temp-integer——介于integer2与integer3（设想）之间的语言
1.0.6版本
灵感来源于洛谷1322 logo语言
暂时没有教程，这是求n以内所有质数的程序：
var[a=0,count=0,mx=input]
while[a.mx.<][
var[i=2,flag=0]
    if[a.2.<][]
    else[
        while[i.a.<][
            if[a.i.%.0.==.flag.0.==.&&][
                let[flag=1]
                break
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
            if[a.i.%.0.==.flag.0.==.&&][
                let[flag=1]
                break
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

const[a=10]
put[a]
end

var[a=10]
while 1[
    put 1,\n
    let[a=a.1.+]
    break
]put a
end

var[a=1]
while 1[
    put a,\n
    let[a=a.1.+]
    if a.10.==[
        break
    ]else[]
]put a
end

var a=10
put a
del a
end

if[1][
    var[a=10]
    put[a]
]else[]
end
'''