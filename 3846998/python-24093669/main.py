names=[]
values=[]
types=[]
all=[names,values,types]
obj=["value","type"]
varname="_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
notname="1234567890"
type_str=["int","float","str","bool"]
type_all={"int":int,"float":float,"str":str,"bool":bool}
def js():
    print('''前言：
    这个语言以模块为单位，分模块解析。模块头告诉程序模块的功能，有var、eval、in、out、add、sub、time、div、inv九种，每个模块的后面都要加done，程序末尾要加end。还有，代码最下面有示范程序。
语法：
    一、变量
        var:
        变量名 变量类型=>定义一个该类型的变量（类型不能改）
        eval:
        变量名 value 要赋的值=>给变量赋值（值必须是本类型的）
    二、输入输出
        out:
        要输出的变量或内容=>输出,不换行，如果把要输出的换成enter就能换行1次
        in:
        要输入的变量 提示语=>输入
    三、计算
        add、sub、time、div、inv分别是加减乘除和乘方，在它们下面写两个变量，程序会将计算施加于第一个变量，第二个变为0
        stradd=>两个字符串相加，施加于第一个，第二个变为""
        substr:
        变量名 起始位 结束位=>截取字符串起始位到结束位的部分（不包括结束位），起始位、结束位是数字，从0开始
''')
js()
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
def put():
    global names,values,types,all
    all=[names,values,types]
code=""
def get():
    global code
    while 1:
        a=input()
        if a=="end":
            break
        code=code+a+"\n"
    code=code.split("done\n")
get()
def bc():
    print("错误！")
def var(ml):
    global names,values,types,all
    ml=ml.split("\n")
    ml=check(ml)
    if len(ml) and ml[0]=="var:":
        for i in ml[1:]:
            ls=i.split()
            if len(ls)!=2:
                bc()
                continue
            if ls[0] in names:
                bc()
                continue
            if ls[1] not in type_str:
                bc()
                continue
            if jy(ls[0])==0:
                bc()
                continue
            names.append(ls[0])
            values.append(type_all[ls[1]](0))
            types.append(type_all[ls[1]])
def getvar(name):
    global names,values,types,all
    if name not in names:
        return(0)
    return([values[names.index(name)],types[names.index(name)],names.index(name)])
def add(ml):
    global names,values,types,all
    ml=ml.split("\n")
    ml=check(ml)
    if len(ml) and ml[0]=="add:":
        for i in ml[1:]:
            ls=i.split()
            if getvar(ls[0])==0 or getvar(ls[1])==0:
                bc()
                continue
            if len(ls)!=2:
                bc()
                continue
            ls[0]=getvar(ls[0])
            ls[1]=getvar(ls[1])
            if ls[0][1] not in (int,float) or ls[1][1] not in (int,float):
                bc()
                continue
            ls[0][0]=ls[0][0]+ls[1][0]
            ls[1][0]=0
            values[ls[0][2]]=ls[0][0]
            values[ls[1][2]]=0
            put()
def sub(ml):
    global names,values,types,all
    ml=ml.split("\n")
    ml=check(ml)
    if len(ml) and ml[0]=="sub:":
        for i in ml[1:]:
            ls=i.split()
            if getvar(ls[0])==0 or getvar(ls[1])==0:
                bc()
                continue
            if len(ls)!=2:
                bc()
                continue
            ls[0]=getvar(ls[0])
            ls[1]=getvar(ls[1])
            if ls[0][1] not in (int,float) or ls[1][1] not in (int,float):
                bc()
                continue
            ls[0][0]=ls[0][0]-ls[1][0]
            ls[1][0]=0
            values[ls[0][2]]=ls[0][0]
            values[ls[1][2]]=0
            put()
def time(ml):
    global names,values,types,all
    ml=ml.split("\n")
    ml=check(ml)
    if len(ml) and ml[0]=="time:":
        for i in ml[1:]:
            ls=i.split()
            if getvar(ls[0])==0 or getvar(ls[1])==0:
                bc()
                continue
            if len(ls)!=2:
                bc()
                continue
            ls[0]=getvar(ls[0])
            ls[1]=getvar(ls[1])
            if ls[0][1] not in (int,float) or ls[1][1] not in (int,float):
                bc()
                continue
            ls[0][0]=ls[0][0]*ls[1][0]
            ls[1][0]=0
            values[ls[0][2]]=ls[0][0]
            values[ls[1][2]]=0
            put()
def div(ml):
    global names,values,types,all
    ml=ml.split("\n")
    ml=check(ml)
    if len(ml) and ml[0]=="div:":
        for i in ml[1:]:
            ls=i.split()
            if getvar(ls[0])==0 or getvar(ls[1])==0:
                bc()
                continue
            if len(ls)!=2:
                bc()
                continue
            ls[0]=getvar(ls[0])
            ls[1]=getvar(ls[1])
            if ls[0][1] not in (int,float) or ls[1][1] not in (int,float):
                bc()
                continue
            ls[0][0]=ls[0][0]/ls[1][0]
            ls[1][0]=0
            values[ls[0][2]]=ls[0][0]
            values[ls[1][2]]=0
            put()
def inv(ml):
    global names,values,types,all
    ml=ml.split("\n")
    ml=check(ml)
    if len(ml) and ml[0]=="inv:":
        for i in ml[1:]:
            ls=i.split()
            if getvar(ls[0])==0 or getvar(ls[1])==0:
                bc()
                continue
            if len(ls)!=2:
                bc()
                continue
            ls[0]=getvar(ls[0])
            ls[1]=getvar(ls[1])
            if ls[0][1] not in (int,float) or ls[1][1] not in (int,float):
                bc()
                continue
            ls[0][0]=ls[0][0]**ls[1][0]
            ls[1][0]=0
            values[ls[0][2]]=ls[0][0]
            values[ls[1][2]]=0
            put()
def stradd(ml):
    global names,values,types,all
    ml=ml.split("\n")
    ml=check(ml)
    if len(ml) and ml[0]=="stradd:":
        for i in ml[1:]:
            ls=i.split()
            if getvar(ls[0])==0 or getvar(ls[1])==0:
                bc()
                continue
            if len(ls)!=2:
                bc()
                continue
            ls[0]=getvar(ls[0])
            ls[1]=getvar(ls[1])
            if ls[0][1] not in (str,) or ls[1][1] not in (str,):
                bc()
                continue
            ls[0][0]=ls[0][0]+ls[1][0]
            ls[1][0]=""
            values[ls[0][2]]=ls[0][0]
            values[ls[1][2]]=0
            put()
def substr(ml):
    global names,values,types,all
    ml=ml.split("\n")
    ml=check(ml)
    if len(ml) and ml[0]=="substr:":
        for i in ml[1:]:
            ls=i.split()
            if getvar(ls[0])==0:
                bc()
                continue
            if len(ls)!=3:
                bc()
                continue
            ls[0]=getvar(ls[0])
            type1=xtype(ls[1])
            type2=xtype(ls[2])
            if ls[0][1] not in (str,) or type1[0] not in (int,) or type2[0]!=int:
                bc()
                continue
            try:
                ls[0][0]=ls[0][0][type1[1]:type2[1]]
                values[ls[0][2]]=ls[0][0]
                put()
            except:
                bc()
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
            return(0,0)
def eval_(ml):
    global names,values,types,all
    ml=ml.split("\n")
    ml=check(ml)
    if len(ml) and ml[0]=="eval:":
        for i in ml[1:]:
            ls=i.split()
            if len(ls)!=3:
                bc()
                continue
            if ls[1] not in obj:
                bc()
                continue
            if getvar(ls[0])==0:
                bc()
                continue
            info=getvar(ls[0])
            if ls[1]=="value":
                if xtype(ls[2])==(0,0):
                    bc()
                    continue
                if info[1]!=xtype(ls[2])[0]:
                    bc()
                    continue
                values[info[2]]=xtype(ls[2])[1]
                put()
def out(ml):
    global names,values,types,all
    ml=ml.split("\n")
    ml=check(ml)
    if len(ml) and ml[0]=="out:":
        for i in ml[1:]:
            ls=i.split()
            if len(ls)!=1:
                bc()
                continue
            if ls[0]=="enter":
                print()
                continue
            if xtype(ls[0])!=(0,0):
                info=xtype(ls[0])
                print(info[1],end="")
            else:
                if getvar(ls[0])==0:
                    bc()
                    continue
                print(getvar(ls[0])[0],end="")
def in_(ml):
    global names,values,types,all
    ml=ml.split("\n")
    ml=check(ml)
    if len(ml) and ml[0]=="in:":
        for i in ml[1:]:
            ls=i.split()
            if len(ls)!=2:
                bc()
                continue
            if getvar(ls[0])==0:
                bc()
                continue
            if xtype(ls[1])!=(0,0):
                info=xtype(ls[1])
                ans=input(info[1])
                try:
                    values[getvar(ls[0])[2]]=getvar(ls[0])[1](ans)
                except:
                    bc()
            else:
                bc()
                try:
                    values[getvar(ls[0])[2]]=getvar(ls[0])[1](input())
                except:
                    bc()
print("\033[1;33m代码运行开始\033[1;0m")
for i in code:
    var(i)
    add(i)
    sub(i)
    time(i)
    div(i)
    inv(i)
    eval_(i)
    out(i)
    in_(i)
    stradd(i)
    substr(i)
print("\n\033[1;33m代码运行结束\033[1;0m")
'''
示范程序1（暂时不能用）：
var:
a int
b int
c str
done
eval:
a value -1
b value -1
c value ""
done
in:
a "请输入第一个数："
b "请输入第二个数："
c "请输入运算符："
done
if:
c == "+"
do:
add:
a b
done
if:
c == "-"
do:
sub:
a b
done
out:
"结果是："
a
done
end
示范程序2：
var:
a float
b float
done
in:
a "请输入第一个加数："
b "请输入第二个加数："
done
add:
a b
done
out:
"结果是："
a
done
end
示范程序3：
var:
a str
done
in:
a ""
done
out:
a
done
end
示范程序4：
var:
a int
b int
done
eval:
a value 100
b value 3
done
inv:
a b
done
out:
a
b
done
end
示范程序5：
var:
a str
done
in:
a ""
done
substr:
a 0 2
done
out:
a
done
end
'''