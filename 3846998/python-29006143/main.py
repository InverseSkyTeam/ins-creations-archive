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
            stack.append(eval(str(a)+i+str(b)))
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
    return(".".join(ml))
def exp(e):
    return(hz_js(getvarinhz(e)))
def run(code):
    code=code.split("\n")
    xxxxxx=0
    while xxxxxx<len(code):
        ml=code[xxxxxx]
        ml=check(ml.split(" "))
        xxxxxx+=1
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
            aaa=exp(ml[1])
            if getvar(ml[1])!=None:
                print(getvar(ml[1]))
            elif aaa!=None:
                print(aaa)
            elif xtype(ml[1]):
                print(xtype(ml[1])[1])
            elif getarr(ml[1])!=None:
                print(getarr(ml[1]))
            elif getarr(ml[1][0:ml[1].index("[")])!=None:
                if xint(ml[1][ml[1].index("[")+1:ml[1].index("]")])!=None:
                    print(getarr(ml[1][0:ml[1].index("[")])[xint(ml[1][ml[1].index("[")+1:ml[1].index("]")])])
                elif getvar(ml[1][ml[1].index("[")+1:ml[1].index("]")])!=None:
                    print(getarr(ml[1][0:ml[1].index("[")])[getvar(ml[1][ml[1].index("[")+1:ml[1].index("]")])])
                else:
                     print("列表元素的调用方法必须是列表名[数字或变量]！")
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
print('''本程序是integer2的精准报错版
作者很懒，不想写教程，况且这不是integer2完整版，下面是判断质数的代码，大部分内容都在里面
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
print("\033[1;33m代码运行结束\033[1;0m")
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
'''