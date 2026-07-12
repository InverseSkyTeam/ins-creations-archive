from time import*
def xint(a):
    try:
        return(int(a))
    except:
        return(None)
varname="_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
operator=["+","-","*","/","%","==","!=",">","<",">=","<="]
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
            stack.append(int(eval(str(a)+i+str(b))))
            if stack[-1]==True:
                stack[-1]=1
            if stack[-1]==False:
                stack[-1]=0
    if len(stack)==1:
        return(stack[0])
    return(None)
var={}
array={}
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
if 2 _a.i.%.0.==
del i
return 0
if 2 i.1.+._a.==
del i
return 1
= i i.1.+
goto -8
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
    if name[0]=="123456789":
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
        elif getfunc(name)!=None:
            argl={}
            arg=_else[1:-1].split(",")
            for xx in range(len(arg)):
                argl[getfunc(name)[0][xx]]=arg[xx]
            ml[i]=str(funcrun(getfunc(name)[1],argl))
    return(".".join(ml))
def exp(e):
    return(hz_js(getvarinhz(e)))
def funcmake(define,code):
    global func
    define=define.split(" ")
    name=define[1][0:define[1].index("(")]
    arg=define[1][define[1].index("(")+1:-1]
    arg=arg.split(",")
    func[name]=[arg,code[1:]]
def funcrun(code,arglist):
    code="\n".join(code)
    for i in arglist:
        code=code.replace(i,arglist[i])
    code=code.split("\n")
    xxxxxx=0
    while xxxxxx<len(code):
        ml=code[xxxxxx]
        ml=check(ml.split(" "))
        xxxxxx+=1
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
        if pd(ml,[2]) and ml[0]=="putchar":
            if exp(ml[1])!=None:
                print(chr(exp(ml[1])),end="")
            elif xint(ml[1])!=None:
                print(chr(xint(ml[1])),end="")
            else:
                bc()
                continue
        if pd(ml,[2]) and ml[0]=="del":
            if getvar(ml[1])!=None:
                del var[ml[1]]
            elif getarr(ml[1])!=None:
                del array[ml[1]]
            else:
                bc()
        if pd(ml,[2]) and ml[0]=="wait":
            aaa=exp(ml[1])
            if aaa==None:
                bc()
                continue
            sleep(aaa)
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
            if getvar(ml[1])==None and "[" in ml[1] and getarr(ml[1][0:ml[1].index("[")])==None:
                print("赋值语句的第二个块必须是变量或列表元素！")
                continue
            aaa=exp(ml[2])
            if aaa==None:
                print("赋值语句的第三个块必须是可计算的后缀表达式！")
                continue
            if getvar(ml[1])!=None:
                var[ml[1]]=aaa
            elif "[" in ml[1] and getarr(ml[1][0:ml[1].index("[")])!=None:
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
            continue
        if pd(ml,[2]) and ml[0]=="list":
            if not jy(ml[1]):
                print("列表定义语句的第二个块必须是合法的变量名！")
                continue
            array[ml[1]]=[]
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
        if pd(ml,[3]) and ml[0]=="while":
            if xint(ml[1])==None:
                print("while循环的第二个块必须是整数（代表这个语句的作用范围）！")
                continue
            aaa=exp(ml[2])
            while aaa:
                if aaa==None:
                    print("while循环的第三个块必须是可计算的后缀表达式！")
                    break
                run("\n".join(code[xxxxxx:xxxxxx+xint(ml[1])]))
                aaa=exp(ml[2])
            else:
                xxxxxx+=xint(ml[1])
                continue
        if pd(ml,[5]) and ml[0]=="for":
            if xint(ml[1])==None:
                print("for循环的第二个块必须是整数（代表这个语句的作用范围）！")
                continue
            if xint(ml[2])==None:
                print("for循环的第三个块必须是整数（代表for循环的起始数）！")
                continue
            if xint(ml[3])==None:
                print("for循环的第四个块必须是整数（代表for循环的终止数）！")
                continue
            if xint(ml[4])==None:
                print("for循环的第五个块必须是整数（代表for循环的步长）！")
                continue
            for abcdef in range(xint(ml[2]),xint(ml[3]),xint(ml[4])):
                run("\n".join(code[xxxxxx:xxxxxx+xint(ml[1])]))
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
        if pd(ml,[2]) and ml[0]=="return":
            if xint(ml[1])!=None:
                return(xint(ml[1]))
            if getvar(ml[1])!=None:
                return(getvar(ml[1]))
            if ml[1] in arglist:
                return(arglist[ml[1]])
            aaa=exp(ml[0])
            if aaa!=None:
                return(aaa)
        else:
            try:
                exp(ml[0])
            except:
                pass
    return(0)
def run(code):
    code=code.split("\n")
    xxxxxx=0
    while xxxxxx<len(code):
        ml=code[xxxxxx]
        ml=check(ml.split(" "))
        xxxxxx+=1
        if pd(ml,[2]) and ml[0]=="putchar":
            if exp(ml[1])!=None:
                print(chr(exp(ml[1])),end="")
            elif xint(ml[1])!=None:
                print(chr(xint(ml[1])),end="")
            else:
                bc()
                continue
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
            continue
        if pd(ml,[2]) and ml[0]=="list":
            if not jy(ml[1]):
                print("列表定义语句的第二个块必须是合法的变量名！")
                continue
            array[ml[1]]=[]
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
        if pd(ml,[3]) and ml[0]=="while":
            if xint(ml[1])==None:
                print("while循环的第二个块必须是整数（代表这个语句的作用范围）！")
                continue
            aaa=exp(ml[2])
            while aaa:
                if aaa==None:
                    print("while循环的第三个块必须是可计算的后缀表达式！")
                    break
                run("\n".join(code[xxxxxx:xxxxxx+xint(ml[1])]))
                aaa=exp(ml[2])
            else:
                xxxxxx+=xint(ml[1])
                continue
        if pd(ml,[5]) and ml[0]=="for":
            if xint(ml[1])==None:
                print("for循环的第二个块必须是整数（代表这个语句的作用范围）！")
                continue
            if xint(ml[2])==None:
                print("for循环的第三个块必须是整数（代表for循环的起始数）！")
                continue
            if xint(ml[3])==None:
                print("for循环的第四个块必须是整数（代表for循环的终止数）！")
                continue
            if xint(ml[4])==None:
                print("for循环的第五个块必须是整数（代表for循环的步长）！")
                continue
            for abcdef in range(xint(ml[2]),xint(ml[3]),xint(ml[4])):
                run("\n".join(code[xxxxxx:xxxxxx+xint(ml[1])]))
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
        else:
            try:
                exp(ml[0])
            except:
                pass
print('''本程序是integer2的2.2.1版，可以创建库
作者很懒，不想写教程，下面是判断质数的代码，大部分内容都在里面
var a
= a input
if 2 a.2.<
put 0
goto 12
var b
= b 2
var c
= c 0
while 5 b.a.<
if 3 a.b.%.0.==
if 2 c.0.==
put 0
= c 1
= b b.1.+
if 1 c.0.==
put 1
还有一部分在这个a+b的函数里
func plus(__a,__b)
var _a
= _a __a.__b.+
return _a
done
put plus(input,input)
如果想创建库，可以点改编，代码中留了一块地，还有创建库的教程，完了要记得保存或发布
还有，如果想看教程，可以故意在一个语句出错，看它的报错信息
可以写代码了，输入end运行
''')
code=""
while 1:
    a=input()
    if a=="end":
        break
    code+="\n"+a
print("\n\033[1;33m代码运行开始\033[1;0m")
run(code)
print("\n\033[1;33m代码运行结束\033[1;0m")
'''var a
var b
= a input
= b input
put a.b.+

if 1 input
put 1
put 0

var a
= a input
while 2 a.0.>
put a
= a a.1.-
put 0

var a
= a input
if 2 a.2.<
put 0
goto 12
var b
= b 2
var c
= c 0
while 5 b.a.<
if 3 a.b.%.0.==
if 2 c.0.==
put 0
= c 1
= b b.1.+
if 1 c.0.==
put 1

list a
var b
= b input
sizeup a
put a[0].b.+

list a
var b
= b 0
sizeup a
= a[b] input
sizeup a
= b b.1.+
= a[1] input
put a[0].a[1].+

var a
= a 1
for 2 0 100 1
put a
= a a.1.+

list a
sizeup a
put a[0]

func f(a)
return a
done
put f(1)

func plus(__a,__b)
var _a
= _a __a.__b.+
return _a
done
put plus(input,input)

list a
getstr a
putstr a
putchar a[0]
'''