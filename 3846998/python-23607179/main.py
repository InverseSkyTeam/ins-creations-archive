var1=[]
var2=[]
o1=[]
o2=[]
def var(a):
    global var1,var2
    var1.append(a)
    var2.append(0)
    return(var1,var2)
def fz(var,obj):
    global var1,var2
    try:
        int(obj)
        type_=int
    except:
        try:
            float(obj)
            type_=float
        except:
            type_=str
    if obj=="True" or obj=="False":
        type_=bool
    '''if type_==str and xstr(a)==0:
        print("错误！1")
        return()'''
    '''elif type_==str:
        type_=xstr'''
    '''
    if type_==int:
        type_="int"
    elif type_==str:
        type_="str"
    elif type_==float:
        type_="float"
    elif type_==bool:
        type_="bool"
    '''
    obj=type_(obj)
    if var in var1:
        try:
            var2[var1.index(var)]=obj
        except:
            print("错误！")
    return(var1,var2)
def get(var):
    global var1,var2
    try:
        type_=type(var2[var1.index(var)])
        obj=type_(input())
        fz(var,obj)
    except:
        print("错误!")
    return(var1,var2)
def xstr(a):
    if a[0]=='"' and a[-1]=='"':
        a=a[1:-1]
        return(a)
    else:
        return(False)
def print_(a):
    if xstr(a)==0:
        if a=="True":
            print(True,end='')
            return()
        elif a=="False":
            print(False,end='')
            return()
        try:
            a=int(a)
            print(a,end='')
        except:
            try:
                a=float(a)
                print(a, end='')
            except:
                print("错误！")
    else:
        print(xstr(a),end='')
def printv(a):
    if a in var1:
        print(var2[var1.index(a)],end='')
    else:
        print("错误！")
def running():
    global var1,var2,o1,o2
    print("\033[1;33m代码运行开始\033[1;0m")
    for i in range(len(o1)):
        if o1[i]=='var':
            var(o2[i])
        elif o1[i]=="print":
            print_(o2[i])
        elif o1[i]=="input":
            get(o2[i])
        elif o2[i][0]=='=':
            fz(o1[i],o2[i][1:])
        elif o1[i]=="printv":
            printv(o2[i])
        elif o1[i]=="enter":
            print("\n"*int(o2[i]),end='')
        else:
            print("错误！")
    print("\033[1;33m代码运行结束")
print('''语法：
    一、关于变量：
        var 变量名：定义一个变量
        变量名 =要赋的值：赋值，也可以用来改变量的类型，如果要赋str类型的值不用加双引号，算式或有变量不行
    二、关于输出：
        print 要输出的值：输出，如果类型是str需要加双引号（单引号不行），不会换行
        printv 要输出的变量：输出一个变量，不会换行
        enter 要换的行数：换行n次
    三、关于输入：
        input 变量名：输入一个变量，输入的不是本类型会报错
    四、关于注释：
        可以用#注释，必须是本行代码的第1个字符
    五、其他：
        注意：没有运算符！
''')
while 1:
    a=input()
    if a=="end":
        break
    elif a[0]=="#":
        continue
    try:
        a,b=a.split()
        o1.append(a)
        o2.append(b)
    except:
        print("错误！")
running()
'''
示范：
var a
a =
print "请输入a："
input a
print "a的值是："
printv a
enter 1
end
'''