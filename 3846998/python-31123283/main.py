'''
2.2.1版之后的更新记录&教程
如果不知道2.2.1版有什么功能，请去看https://code.xueersi.com/home/project/detail?lang=code&pid=29318309&version=python&form=python&langType=python
2.3.0更了一些字符串的东西（三个命令）
2.3.1.1有了convert库
2.3.2.0 put语句更新，能输出多个值，用","分隔
2.3.3.1 prime库（prime函数）和wait命令（相当于python的sleep）
2.3.4.0接近大更的一次更新：
put语句输出多个值时用";"分隔
del 列表名 删除列表
del 列表名 下标 删除列表元素
append 列表名 值 添加一个元素
len 列表名 变量 把列表的长度赋给变量
2.3.5.0加了and和or运算符
2.4.0.0大更：
删除for循环（没用）
在循环中加入break和continue
有了全局变量和局部变量的概念，循环和函数里的是局部变量，完成后会被删了，不用手动删了
源代码行数减少不少，逻辑变复杂，以后不好更新了
速度可能慢了（我不确定）
'''
from time import*
def xint(a):
    try:
        return(int(a))
    except:
        return(None)
varname="_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
operator=["+","-","*","/","%","==","!=",">","<",">=","<=","and","or"]
func={}
module={}
#------------这里可以创建库--------------
#格式：module["库名"]='''内容'''（内容可以多行）
#例：
module["hello"]='''put "Hello,world!"'''
module["convert"]='''#module convert
func to_int(a,len)
= len len.1.-
while 2 len.0.>=
= a[len] a[len].48.-
= len len.1.-
done
func to_str(a,len)
= len len.1.-
while 2 len.0.>=
= a[len] a[len].48.+
= len len.1.-
done'''
module["prime"]='''#module prime
func prime(_a)
if 1 _a.2.<
return 0
if 1 _a.2.==
return 1
var i
= i 2
if 1 _a.i.%.0.==
return 0
if 1 i.1.+._a.==
return 1
= i i.1.+
goto -6
done
'''
#----------------------------------------
def getfunc(name):
    try:
        return(func[name])
    except:
        return(None)
def xtype(a):
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
def check(ml):
    while "" in ml:
        ml.remove("")
    return(ml)
def getmod(name):
    try:
        return(module[name])
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
    if name[0]=="123456789":
        return(0)
    for i in name:
        if i not in "_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890":
            return(0)
    return(1)
def bc():
    print("错误！")
def funcmake(define,code):
    global func
    define=define.split(" ")
    name=define[1][0:define[1].index("(")]
    arg=define[1][define[1].index("(")+1:-1]
    arg=arg.split(",")
    func[name]=[arg,"\n".join(code[1:])]
const={}
def getcon(a):
    try:
        return(const[a])
    except:
        return(None)
def run(code,rtype=0,vl={},al={}):#rtype:0:普通运行;1:函数内运行;2:循环内运行
    global func,module
    array=al
    var=vl
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
            elif getcon(name)!=None:
                ml[i]=str(getcon(name))
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
            elif getfunc(name)!=None:
                argl={}
                arg=_else[1:-1].split(",")
                for xx in range(len(arg)):
                    argl[getfunc(name)[0][xx]]=arg[xx]
                fc=getfunc(name)[1]
                for k,v in argl.items():
                    fc=fc.replace(k,v)
                ml[i]=str(run(fc,1))
        return(".".join(ml))
    def exp(e):
        return(hz_js(getvarinhz(e)))
    code=code.split("\n")
    xxxxxx=0
    dl=[]
    while xxxxxx<len(code):
        ml=code[xxxxxx]
        ml=check(ml.split(" "))
        xxxxxx+=1
        if pd(ml,[1]) and ml[0]=="break":
            if rtype!=2:
                print("循环里才能break！")
                continue
            for jjj in dl:
                if getvar(jjj)!=None:
                    del var[jjj]
                if getarr(jjj)!=None:
                    del arr[jjj]
            return("break")
        if pd(ml,[1]) and ml[0]=="continue":
            if rtype!=2:
                print("循环里才能continue！")
                continue
            for jjj in dl:
                if getvar(jjj)!=None:
                    del var[jjj]
                if getarr(jjj)!=None:
                    del arr[jjj]
            return()
        if pd(ml,[2]) and ml[0]=="putchar":
            if exp(ml[1])!=None:
                print(chr(exp(ml[1])),end="")
            elif xint(ml[1])!=None:
                print(chr(xint(ml[1])),end="")
            else:
                bc()
                continue
        if pd(ml,[3]) and ml[0]=="const":
            aaa=exp(ml[2])
            if jy(ml[1])==0:
                bc()
                continue
            if aaa==None:
                bc()
                continue
            const[ml[1]]=aaa
        if pd(ml,[2]) and ml[0]=="wait":
            aaa=exp(ml[1])
            if aaa==None:
                bc()
                continue
            sleep(aaa)
        if pd(ml,[2]) and ml[0]=="putstr":
            if getarr(ml[1])==None:
                bc()
            for ii in getarr(ml[1]):
                print(chr(ii),end="")
            continue
        if pd(ml,[2]) and ml[0]=="getstr":
            if getarr(ml[1])==None:
                bc()
            aaa=input()
            array[ml[1]]=[]
            for ii in aaa:
                array[ml[1]].append(ord(ii))
            continue
        if pd(ml,[2]) and ml[0]=="del":
            if getvar(ml[1])!=None:
                del var[ml[1]]
            elif getarr(ml[1])!=None:
                del array[ml[1]]
            else:
                bc()
        if pd(ml,[3]) and ml[1]=="append":
            if getarr[ml[1]]==None:
                bc()
                continue
            aaa=exp(ml[2])
            if aaa==None:
                bc()
                continue
            array[ml[1]].append(aaa)
        if pd(ml,[3]) and ml[1]=="del":
            if getarr[ml[1]]==None:
                bc()
                continue
            aaa=exp(ml[2])
            if aaa==None:
                bc()
                continue
            del array[ml[1]][aaa]
        if pd(ml,[3]) and ml[1]=="len":
            if getarr[ml[1]]==None:
                bc()
                continue
            if getvar(ml[2])==None:
                bc()
                continue
            var[ml[2]]=len(getarr[ml[1]])
        if pd(ml,[2]) and ml[0]=="#use":
            if getmod(ml[1])==None:
                bc()
                continue
            run(getmod(ml[1]))
        if pd(ml,[2]) and ml[0]=="func":
            if rtype==1:
                print("函数里不能定义函数！")
                continue
            if rtype==2:
                print("循环里不能定义函数！")
                continue
            fb=[]
            line=xxxxxx
            for jjj in code[xxxxxx-1:]:
                if jjj=="done":
                    break
                fb.append(jjj)
                line+=1
            funcmake(fb[0],fb)
            xxxxxx=line
        if pd(ml,[1]) and ml[0]==",":
            print(",",end="")
        if pd(ml,[2]) and ml[0]=="\\n":
            if xint(ml[1])==None:
                bc()
                continue
            print("\n"*xint(ml[1]),end="")
        if pd(ml,[2]) and ml[0]=="\\t":
            if xint(ml[1])==None:
                bc()
                continue
            print("\t"*xint(ml[1]),end="")
        if pd(ml,[2]) and ml[0]=="\\s":
            if xint(ml[1])==None:
                bc()
                continue
            print(" "*xint(ml[1]),end="")
        if pd(ml,[3]) and ml[0]=="=":
            if getvar(ml[1])==None and getarr(ml[1][0:ml[1].index("[")])==None:
                print("赋值语句的第二个块必须是变量或列表元素！")
                continue
            aaa=exp(ml[2])
            if aaa==None:
                print("赋值语句的第三个块必须是可计算的后缀表达式！")
                continue
            if getvar(ml[1])!=None:
                var[ml[1]]=aaa
            elif getarr(ml[1][0:ml[1].index("[")])!=None:
                if xint(ml[1][ml[1].index("[")+1:ml[1].index("]")])!=None:
                    array[ml[1][0:ml[1].index("[")]][xint(ml[1][ml[1].index("[")+1:ml[1].index("]")])]=aaa
                elif getvar(ml[1][ml[1].index("[")+1:ml[1].index("]")])!=None:
                    array[ml[1][0:ml[1].index("[")]][getvar(ml[1][ml[1].index("[")+1:ml[1].index("]")])]=aaa
                else:
                    print("列表元素的调用方法必须是列表名[数字或变量]！")
            continue
        if pd(ml,[2]) and ml[0]=="var":
            if not jy(ml[1]):
                print("变量定义语句的第二个块必须是合法的变量名！")
                continue
            var[ml[1]]=0
            dl.append(ml[1])
            continue
        if pd(ml,[2]) and ml[0]=="list":
            if not jy(ml[1]):
                print("列表定义语句的第二个块必须是合法的变量名！")
                continue
            array[ml[1]]=[]
            dl.append(ml[1])
            continue
        if pd(ml,[2]) and ml[0]=="put":
            for j in ml[1].split(";"):
                aaa=exp(j)
                if getvar(j)!=None:
                    print(getvar(j),end="")
                elif aaa!=None:
                    print(aaa,end="")
                elif xtype(j):
                    print(xtype(j)[1],end="")
                elif getarr(j)!=None:
                    print(getarr(j),end="")
                elif j=="enter":
                    print()
                elif j=="space":
                    print(" ",end="")
                elif j=="tab":
                    print("\t",end="")
                else:
                    print("输出语句的第二个块必须是可计算的后缀表达式、列表或其他值（布尔、浮点或字符串）！")
            continue
        if pd(ml,[3]) and ml[0]=="if":
            if xint(ml[1])==None:
                print("条件语句的第二个块必须是整数（代表这个语句的作用范围）！")
                continue
            aaa=exp(ml[2])
            if aaa==None:
                print("条件语句的第三个块必须是可计算的后缀表达式！")
                continue
            if aaa:
                continue
            else:
                xxxxxx+=xint(ml[1])
                continue
        if pd(ml,[2]) and ml[0]=="goto":
            if xint(ml[1])==None:
                print("跳转语句的第二个块必须是整数（代表要往下跳的行数）！")
                continue
            xxxxxx+=xint(ml[1])
            continue
        if pd(ml,[2]) and ml[0]=="sizeup":
            if getarr(ml[1])==None:
                print("sizeup语句的第二个块必须是列表名！")
                continue
            array[ml[1]].append(0)
            continue
        if pd(ml,[2]) and ml[0]=="sizedown":
            if getarr(ml[1])==None:
                print("sizedown语句的第二个块必须是列表名！")
                continue
            array[ml[1]]=array[ml[1]][0:-1]
            continue
        if pd(ml,[3]) and ml[0]=="while":
            if xint(ml[1])==None:
                print("while循环的第二个块必须是整数（代表这个语句的作用范围）！")
                continue
            aaa=exp(ml[2])
            while aaa:
                if aaa==None:
                    print("while循环的第三个块必须是可计算的后缀表达式！")
                    break
                bbb=run("\n".join(code[xxxxxx:xxxxxx+xint(ml[1])]),2,var,array)
                if bbb=="break":
                    break
                aaa=exp(ml[2])
            xxxxxx+=xint(ml[1])
            continue
        if pd(ml,[2]) and ml[0]=="return":
            if rtype!=1:
                print("只有函数内才能return！")
                continue
            aaa=exp(ml[1])
            for jjj in dl:
                if getvar(jjj)!=None:
                    del var[jjj]
                if getarr(jjj)!=None:
                    del arr[jjj]
            if aaa==None:
                bc()
                return(0)
            return(aaa)
        else:
            try:
                exp(ml[0])
            except:
                pass
    for i in dl:
        if getvar(i)!=None:
            del var[i]
        if getarr(i)!=None:
            del arr[i]
    if rtype==1:
        return(0)
code=""
while 1:
    a=input()
    if a=="end":
        break
    code+="\n"+a
code=code.replace("    ","")
code=code.replace("\t","")
print("\n\033[1;33m代码运行开始\033[1;0m")
run(code)
print("\n\033[1;33m代码运行结束\033[1;0m")
'''
func plus(__a,__b)
var _a
= _a __a.__b.+
return _a
done
put plus(input,input)
end

var a
while 4 1
put a;enter
if 1 a.10.==
break
= a a.1.+
end

var a
while 4 a.2.<
    = a a.1.+
    var ls
    = ls input.input.+
    put ls;enter
end
'''