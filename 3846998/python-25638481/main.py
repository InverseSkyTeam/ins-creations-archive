from time import*
names=[]
values=[]
types=[]
all=[names,values,types]
obj=["value","type"]
varname="1234567890_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
notname="1234567890"
type_str=["int","float","str","bool"]
type_all={"int":int,"float":float,"str":str,"bool":bool}
type_obj={"int":0,"float":float(0),"str":"","bool":False}
code=""
print('''语法：
    一、变量
    1、变量类型有int、float、str和bool
    2、var 变量名 变量类型=>定义变量（变量类型不能改）
    3、eval 变量名 值=>赋值
    二、输出
    out 要输出的内容=>输出，内容可以是变量
    三、输入
    in 变量 提示语=>提示语不能是变量
    四、运算
    1、普通运算格式是 命令 变量1 变量2 to 变量3（结果） 命令有add、sub、time、div、mod、inv，分别代表加减乘除模和乘方
    2、布尔运算格式相同，命令有big、small、bigequ、smaequ、equal、and、or，分别代表大于、小于、大于等于、小于等于、等于、和、或
    五、暂停
    sleep 变量=>暂停n秒
    六、简单循环
    repeat 整形变量
    内容
    ;
    =>重复执行内容n次
    七、if语句
    if 布尔变量
    内容
    ;
    =>如果a，进行下面内容
    八、while循环
    while 布尔变量
    内容
    ;
    =>如果变量为真，执行内容（跟Python、c++的while差不多，但是while后面必须跟布尔变量，而不是表达式）
    九、本次更新
    1、while循环
''')
def bc():
    print("错误！")
def check(ml):
    for i in ml:
        if i=="":
            ml.remove(i)
    return(ml)
def jy(name):
    if name[0] in notname:
        return(0)
    for i in name:
        if i not in varname:
            return(0)
    return(1)
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
def xsleep(ml):
    ml=ml.split()
    if ml[0]=="sleep":
        try:
            sleep(float(ml[1]))
        except:
            bc()
def getvar(name):
    global names,values,types,all
    if name not in names:
        return(0)
    return([values[names.index(name)],types[names.index(name)],names.index(name)])
def pd(ml,num=3):
    return(len(ml)==num)
def out(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=1)
    if ml[0]=="out":
        if pd(ml,2)==0:
            bc()
            return()
        if xtype(ml[1]):
            print(xtype(ml[1])[1],end="")
        elif getvar(ml[1]):
            print(getvar(ml[1])[0],end="")
        elif ml[1]=="enter":
            print()
        elif ml[1]=="in":
            print(input())
        else:
            bc()
def var(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=2)
    if ml[0]=="var":
        if pd(ml)==0:
            bc()
            return()
        if pd(ml):
            if jy(ml[1])==0:
                bc()
                return()
            if ml[2] not in type_str:
                bc()
                return()
            names.append(ml[1])
            values.append(type_obj[ml[2]])
            types.append(type_all[ml[2]])
def in_(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=2)
    if ml[0]=="in":
        if pd(ml)==0:
            bc()
            return()
        if getvar(ml[1])==0:
            bc()
            return()
        if xtype(ml[2])==0:
            bc()
            return()
        type_=getvar(ml[1])[1]
        pos=getvar(ml[1])[2]
        try:
            a=input(xtype(ml[2])[1])
            if a=="False" or a=="0":
                values[pos]=False
                return()
            get=type_(a)
            values[pos]=get
        except:
            bc()
def eval_(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=2)
    if ml[0]=="eval":
        if pd(ml)==0:
            bc()
            return()
        if xtype(ml[2])==0 and getvar(ml[2])==0:
            bc()
            return()
        if getvar(ml[1])==0:
            bc()
            return()
        if xtype(ml[2]):
            if xtype(ml[2])[0]!=getvar(ml[1])[1]:
                bc()
                return()
        if getvar(ml[2]):
            if getvar(ml[2])[1]!=getvar(ml[1])[1]:
                bc()
                return()
        if xtype(ml[2]) and xtype(ml[2])[0]==getvar(ml[1])[1]:
            values[getvar(ml[1])[2]]=xtype(ml[2])[1]
        if getvar(ml[2]) and getvar(ml[1])[1]==getvar(ml[2])[1]:
            values[getvar(ml[1])[2]]=getvar(ml[2])[0]
def add(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=4)
    if ml[0]=="add":
        if pd(ml,5)==0:
            bc()
            return()
        if (getvar(ml[1]) and getvar(ml[2]) and getvar(ml[4]) and ml[3]=="to")==0:
            bc()
            return()
        if (getvar(ml[1])[1] in (int,float) and getvar(ml[2])[1] in (int,float) and getvar(ml[4])[1] in (int,float))==0 or (getvar(ml[4])[1]==getvar(ml[2])[1] and getvar(ml[2])[1]==getvar(ml[1])[1])==0:
            bc()
            return()
        eval_("eval "+ml[4]+" "+str(getvar(ml[1])[0]+getvar(ml[2])[0]))
def sub(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=4)
    if ml[0]=="sub":
        if pd(ml,5)==0:
            bc()
            return()
        if (getvar(ml[1]) and getvar(ml[2]) and getvar(ml[4]) and ml[3]=="to")==0:
            bc()
            return()
        if (getvar(ml[1])[1] in (int,float) and getvar(ml[2])[1] in (int,float) and getvar(ml[4])[1] in (int,float))==0 or (getvar(ml[4])[1]==getvar(ml[2])[1] and getvar(ml[2])[1]==getvar(ml[1])[1])==0:
            bc()
            return()
        eval_("eval "+ml[4]+" "+str(getvar(ml[1])[0]-getvar(ml[2])[0]))
def time_(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=4)
    if ml[0]=="time":
        if pd(ml,5)==0:
            bc()
            return()
        if (getvar(ml[1]) and getvar(ml[2]) and getvar(ml[4]) and ml[3]=="to")==0:
            bc()
            return()
        if (getvar(ml[1])[1] in (int,float) and getvar(ml[2])[1] in (int,float) and getvar(ml[4])[1] in (int,float))==0 or (getvar(ml[4])[1]==getvar(ml[2])[1] and getvar(ml[2])[1]==getvar(ml[1])[1])==0:
            bc()
            return()
        eval_("eval "+ml[4]+" "+str(getvar(ml[1])[0]*getvar(ml[2])[0]))
def inv(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=4)
    if ml[0]=="inv":
        if pd(ml,5)==0:
            bc()
            return()
        if (getvar(ml[1]) and getvar(ml[2]) and getvar(ml[4]) and ml[3]=="to")==0:
            bc()
            return()
        if (getvar(ml[1])[1] in (int,float) and getvar(ml[2])[1] in (int,float) and getvar(ml[4])[1] in (int,float))==0 or (getvar(ml[4])[1]==getvar(ml[2])[1] and getvar(ml[2])[1]==getvar(ml[1])[1])==0:
            bc()
            return()
        eval_("eval "+ml[4]+" "+str(getvar(ml[1])[0]**getvar(ml[2])[0]))
def div(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=4)
    if ml[0]=="div":
        if pd(ml,5)==0:
            bc()
            return()
        if (getvar(ml[1]) and getvar(ml[2]) and getvar(ml[4]) and ml[3]=="to")==0:
            bc()
            return()
        if (getvar(ml[1])[1] in (int,float) and getvar(ml[2])[1] in (int,float) and getvar(ml[4])[1] in (int,float))==0 or (getvar(ml[4])[1]==getvar(ml[2])[1] and getvar(ml[2])[1]==getvar(ml[1])[1])==0:
            bc()
            return()
        eval_("eval "+ml[4]+" "+str(getvar(ml[1])[1](getvar(ml[1])[0]/getvar(ml[2])[0])))
def mod(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=4)
    if ml[0]=="mod":
        if pd(ml,5)==0:
            bc()
            return()
        if (getvar(ml[1]) and getvar(ml[2]) and getvar(ml[4]) and ml[3]=="to")==0:
            bc()
            return()
        if (getvar(ml[1])[1] in (int,) and getvar(ml[2])[1] in (int,) and getvar(ml[4])[1] in (int,float))==0 or (getvar(ml[4])[1]==getvar(ml[2])[1] and getvar(ml[2])[1]==getvar(ml[1])[1])==0:
            bc()
            return()
        eval_("eval "+ml[4]+" "+str(getvar(ml[1])[0]%getvar(ml[2])[0]))
def big(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=4)
    if ml[0]=="big":
        if pd(ml,5)==0:
            bc()
            return()
        if (getvar(ml[1]) and getvar(ml[2]) and getvar(ml[4]) and ml[3]=="to")==0:
            bc()
            return()
        if (getvar(ml[1])[1] in (int,float) and getvar(ml[2])[1] in (int,float) and getvar(ml[4])[1] in (bool,))==0:
            bc()
            return()
        eval_("eval "+ml[4]+" "+str(getvar(ml[1])[0]>getvar(ml[2])[0]))
def small(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=4)
    if ml[0]=="small":
        if pd(ml,5)==0:
            bc()
            return()
        if (getvar(ml[1]) and getvar(ml[2]) and getvar(ml[4]) and ml[3]=="to")==0:
            bc()
            return()
        if (getvar(ml[1])[1] in (int,float) and getvar(ml[2])[1] in (int,float) and getvar(ml[4])[1] in (bool,))==0:
            bc()
            return()
        eval_("eval "+ml[4]+" "+str(getvar(ml[1])[0]<getvar(ml[2])[0]))
def equal(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=4)
    if ml[0]=="equal":
        if pd(ml,5)==0:
            bc()
            return()
        if (getvar(ml[1]) and getvar(ml[2]) and getvar(ml[4]) and ml[3]=="to")==0:
            bc()
            return()
        if (getvar(ml[1])[1] in (int,float) and getvar(ml[2])[1] in (int,float) and getvar(ml[4])[1] in (bool,))==0:
            bc()
            return()
        eval_("eval "+ml[4]+" "+str(getvar(ml[1])[0]==getvar(ml[2])[0]))
def bigequ(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=4)
    if ml[0]=="bigequ":
        if pd(ml,5)==0:
            bc()
            return()
        if (getvar(ml[1]) and getvar(ml[2]) and getvar(ml[4]) and ml[3]=="to")==0:
            bc()
            return()
        if (getvar(ml[1])[1] in (int,float) and getvar(ml[2])[1] in (int,float) and getvar(ml[4])[1] in (bool,))==0:
            bc()
            return()
        eval_("eval "+ml[4]+" "+str(getvar(ml[1])[0]>=getvar(ml[2])[0]))
def smaequ(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=4)
    if ml[0]=="smaequ":
        if pd(ml,5)==0:
            bc()
            return()
        if (getvar(ml[1]) and getvar(ml[2]) and getvar(ml[4]) and ml[3]=="to")==0:
            bc()
            return()
        if (getvar(ml[1])[1] in (int,float) and getvar(ml[2])[1] in (int,float) and getvar(ml[4])[1] in (bool,))==0:
            bc()
            return()
        eval_("eval "+ml[4]+" "+str(getvar(ml[1])[0]<=getvar(ml[2])[0]))
def and_(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=4)
    if ml[0]=="and":
        if pd(ml,5)==0:
            bc()
            return()
        if (getvar(ml[1]) and getvar(ml[2]) and getvar(ml[4]) and ml[3]=="to")==0:
            bc()
            return()
        if (getvar(ml[1])[1] in (bool,) and getvar(ml[2])[1] in (bool,) and getvar(ml[4])[1] in (bool,))==0:
            bc()
            return()
        eval_("eval "+ml[4]+" "+str(getvar(ml[1])[0] and getvar(ml[2])[0]))
def or_(ml):
    global names,values,types,all
    ml=ml.split(maxsplit=4)
    if ml[0]=="or":
        if pd(ml,5)==0:
            bc()
            return()
        if (getvar(ml[1]) and getvar(ml[2]) and getvar(ml[4]) and ml[3]=="to")==0:
            bc()
            return()
        if (getvar(ml[1])[1] in (bool,) and getvar(ml[2])[1] in (bool,) and getvar(ml[4])[1] in (bool,))==0:
            bc()
            return()
        eval_("eval "+ml[4]+" "+str(getvar(ml[1])[0] or getvar(ml[2])[0]))
def repeat(ml):
    ml=ml.split("\n")
    while "" in ml:
        ml.remove("")
    ml[0]=ml[0].split()
    if ml[0][0]=="repeat":
        try:
            for j in range(getvar(ml[0][1])[0]):
                for i in ml[1:]:
                    var(i)
                    out(i)
                    in_(i)
                    eval_(i)
                    add(i)
                    sub(i)
                    time_(i)
                    inv(i)
                    div(i)
                    mod(i)
                    big(i)
                    small(i)
                    bigequ(i)
                    smaequ(i)
                    and_(i)
                    or_(i)
                    xsleep(i)
        except:
            bc()
def while_(ml):
    ml=ml.split("\n")
    while "" in ml:
        ml.remove("")
    ml[0]=ml[0].split()
    if ml[0][0]=="while":
        try:
            if getvar(ml[0][1])[1]!=bool:
                bc()
                return()
            while getvar(ml[0][1])[0]:
                for i in ml[1:]:
                    var(i)
                    out(i)
                    in_(i)
                    eval_(i)
                    add(i)
                    sub(i)
                    time_(i)
                    inv(i)
                    div(i)
                    mod(i)
                    big(i)
                    small(i)
                    bigequ(i)
                    smaequ(i)
                    and_(i)
                    or_(i)
                    xsleep(i)
        except:
            bc()
def if_(ml):
    ml=ml.split("\n")
    while "" in ml:
        ml.remove("")
    ml[0]=ml[0].split()
    if ml[0][0]=="if":
        try:
            if getvar(ml[0][1])[1]!=bool:
                bc()
                return()
            if getvar(ml[0][1])[0]:
                for i in ml[1:]:
                    var(i)
                    out(i)
                    in_(i)
                    eval_(i)
                    add(i)
                    sub(i)
                    time_(i)
                    inv(i)
                    div(i)
                    mod(i)
                    big(i)
                    small(i)
                    bigequ(i)
                    smaequ(i)
                    and_(i)
                    or_(i)
                    xsleep(i)
        except:
            bc()
while 1:
    a=input()
    if a=="end":
        break
    code=code+a+"\n"
code=code.split(';\n')
code=check(code)
print("\033[1;33m代码运行开始\033[1;0m")
for i in code:
    var(i)
    out(i)
    in_(i)
    eval_(i)
    add(i)
    sub(i)
    time_(i)
    inv(i)
    div(i)
    mod(i)
    big(i)
    small(i)
    bigequ(i)
    smaequ(i)
    and_(i)
    or_(i)
    xsleep(i)
    repeat(i)
    if_(i)
    while_(i)
print("\n\033[1;33m代码运行结束\033[1;0m")
'''
var a int;
var b int;
eval b 100;
eval a b;
out a;
end

var a int;
var b int;
var c int;
in a "";
in b "";
add a b to c;
out c;
end;

var a int;
var b int;
var c int;
in a "";
in b "";
sub a b to c;
out c;
end

var a int;
var b int;
var c int;
in a "";
in b "";
time a b to c;
out c;
end

var a int;
var b int;
var c int;
in a "";
in b "";
inv a b to c;
out c;
end

var a int;
var b int;
var c int;
in a "";
in b "";
div a b to c;
out c;
end

var a int;
var b int;
var c int;
in a "";
in b "";
mod a b to c;
out c;
end

var a float;
var b float;
var c float;
in a "";
in b "";
div a b to c;
out c;
end

var a int;
var b int;
var c bool;
in a "";
in b "";
big a b to c;
out c;
end

var a bool;
var b bool;
var c bool;
in a "";
in b "";
or a b to c;
out c;
end

out 10;
out enter;
sleep 2;
out 10;
end

var a int;
var b int;
var c int;
eval c 10;
eval b 1;
repeat c
add a b to a
out a
out enter
end

var a int;
var b int;
var c int;
eval b 1;
in c "";
repeat c
add a b to a
out a
out enter;
out "end";
end

var a bool;
eval a True;
var b int;
var c int;
eval c 1;
var d int;
eval d 100;
while a
add b c to b
small b d to a
out b
out enter;
end
'''