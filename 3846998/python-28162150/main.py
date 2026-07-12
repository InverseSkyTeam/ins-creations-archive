var={}
array={}
code=""
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
while 1:
    a=input()
    if a=="end":
        break
    code+="\n"+a
code=code.split("\n")
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
print("\033[1;33m代码运行开始\033[1;0m")
l=len(code)
i=0
while i<l:
    if code[i]=="exit":
        break
    ml=check(code[i].split())
    i+=1
    if pd(ml,[0,1])==1:
        continue
    if pd(ml) and ml[0]=="var":
        if jy(ml[1])==0:
            bc()
            continue
        if ifint(ml[2])==None and getvar(ml[2])==None:
            bc()
            continue
        if ifint(ml[2])!=None:
            var[ml[1]]=ifint(ml[2])
            continue
        if getvar(ml[2])!=None:
            var[ml[1]]=getvar(ml[2])
            continue
    if pd(ml,[2]) and ml[0]=="var":
        if jy(ml[1])==0:
            bc()
            continue
        var[ml[1]]=0
        continue
    if pd(ml) and ml[0]=="list":
        if jy(ml[1])==0:
            bc()
            continue
        if ifint(ml[2])==None and getvar(ml[2])==None:
            bc()
            continue
        if ifint(ml[2])!=None:
            array[ml[1]]=[0]*ifint(ml[2])
            continue
        if getvar(ml[2])!=None:
            array[ml[1]]=[0]*getvar(ml[2])
            continue
    if pd(ml,[2]) and ml[0]=="sizeup":
        if getarr(ml[1])==None:
            bc()
            continue
        array[ml[1]].append(0)
    if pd(ml,[2]) and ml[0]=="sizedown":
        if getarr(ml[1])==None:
            bc()
            continue
        array[ml[1]]=array[ml[1]][0:-1]
    if pd(ml,[2]) and ml[0]=="print":
        if xtype(ml[1]):
            print(xtype(ml[1])[1])
            continue
        elif getvar(ml[1])!=None:
            print(getvar(ml[1]))
            continue
        elif getarr(ml[1])!=None:
            print(getarr(ml[1]))
            continue
        else:
            bc()
            continue
    if pd(ml,[3]) and ml[0]=="print":
        if getarr(ml[1])==None:
            bc()
            continue
        elif getvar(ml[2])!=None:
            print(getarr(ml[1])[getvar(ml[2])])
            continue
        elif ifint(ml[2])!=None:
            print(getarr(ml[1])[ifint(ml[2])])
            continue
        else:
            bc()
            continue
    if pd(ml,[2]) and ml[0]=="input":
        if getvar(ml[1])==None:
            bc()
            continue
        try:
            var[ml[1]]=int(input("输入："))
        except:
            bc()
            continue
    if pd(ml,[3]) and ml[0]=="=":
        if getvar(ml[1])!=None and getvar(ml[2])!=None:
            var[ml[1]]=getvar(ml[2])
        elif getvar(ml[1])!=None and ifint(ml[2])!=None:
            var[ml[1]]=ifint(ml[2])
        else:
            bc()
            continue
    if pd(ml,[4]) and ml[1]=="=":
        if getvar(ml[0])!=None and getarr(ml[2])!=None and getvar(ml[3])!=None:
            var[ml[0]]=getarr(ml[2])[getvar(ml[3])]
        elif getvar(ml[0])!=None and getarr(ml[2])!=None and ifint(ml[3])!=None:
            var[ml[0]]=getarr(ml[2])[ifint(ml[3])]
        else:
            bc()
            continue
    if pd(ml,[4]) and ml[2]=="=":
        if getarr(ml[0])!=None and getvar(ml[1])!=None and getvar(ml[3])!=None:
            array[ml[0]][getvar(ml[1])]=getvar(ml[3])
        elif getarr(ml[0])!=None and ifint(ml[2])!=None and getvar(ml[3])!=None:
            array[ml[0]][ifint(ml[2])]=getvar(ml[3])
        else:
            bc()
            continue
    if pd(ml,[3]) and ml[0]=="+":
        if getvar(ml[1])==None:
            bc()
            continue
        if getvar(ml[2])!=None:
            var[ml[1]]+=getvar(ml[2])
        elif ifint(ml[2]):
            var[ml[1]]+=ifint(ml[2])
        else:
            bc()
            continue
    if pd(ml,[3]) and ml[0]=="-":
        if getvar(ml[1])==None:
            bc()
            continue
        if getvar(ml[2])!=None:
            var[ml[1]]-=getvar(ml[2])
        elif ifint(ml[2]):
            var[ml[1]]-=ifint(ml[2])
        else:
            bc()
            continue
    if pd(ml,[3]) and ml[0]=="*":
        if getvar(ml[1])==None:
            bc()
            continue
        if getvar(ml[2])!=None:
            var[ml[1]]*=getvar(ml[2])
        elif ifint(ml[2]):
            var[ml[1]]*=ifint(ml[2])
        else:
            bc()
            continue
    if pd(ml,[3]) and ml[0]=="/":
        if getvar(ml[1])==None:
            bc()
            continue
        if getvar(ml[2])!=None:
            var[ml[1]]/=getvar(ml[2])
            var[ml[1]]=int(var[ml[1]])
        elif ifint(ml[2]):
            var[ml[1]]/=ifint(ml[2])
            var[ml[1]]=int(var[ml[1]])
        else:
            bc()
            continue
    if pd(ml,[3]) and ml[0]=="%":
        if getvar(ml[1])==None:
            bc()
            continue
        if getvar(ml[2])!=None:
            var[ml[1]]%=getvar(ml[2])
        elif ifint(ml[2]):
            var[ml[1]]%=ifint(ml[2])
        else:
            bc()
            continue
    if pd(ml,[2]) and ml[0]=="goto":
        if jy(ml[1])==0:
            bc()
            continue
        for j in range(l):
            if code[j]==ml[1]+":":
                i=j
                continue
    if pd(ml,[2]) and ml[0]=="del":
        if ml[1]=="all":
            var={}
            array={}
            continue
        if getvar(ml[1])==0:
            bc()
            continue
        del var[ml[1]]
        continue
    if pd(ml,[5]) and ml[0]=="if":
        if jy(ml[4])==0 or ml[2] not in ["==",">","<",">=","<="]:
            bc()
            continue
        ifend=0
        for j in range(l):
            if code[j]==ml[4]+".end":
                ifend=j
        if ifend==0:
            bc()
            continue
        if ml[2]=="==":
            if getvar(ml[1])==None:
                bc()
                continue
            if getvar(ml[3])!=None:
                if var[ml[1]]==getvar(ml[3]):
                    continue
                else:
                    i=ifend+1
                    continue
            elif ifint(ml[3])!=None:
                if var[ml[1]]==ifint(ml[3]):
                    continue
                else:
                    i=ifend+1
                    continue
            else:
                bc()
                continue
        if ml[2]==">":
            if getvar(ml[1])==None:
                bc()
                continue
            if getvar(ml[3])!=None:
                if var[ml[1]]>getvar(ml[3]):
                    continue
                else:
                    i=ifend+1
                    continue
            if ifint(ml[3])!=None:
                if var[ml[1]]>ifint(ml[3]):
                    continue
                else:
                    i=ifend+1
                    continue
            bc()
            continue
        if ml[2]=="<":
            if getvar(ml[1])==None:
                bc()
                continue
            if getvar(ml[3])!=None:
                if var[ml[1]]<getvar(ml[3]):
                    continue
                else:
                    i=ifend+1
                    continue
            elif ifint(ml[3]):
                if var[ml[1]]<ifint(ml[3]):
                    continue
                else:
                    i=ifend+1
                    continue
            else:
                bc()
                continue
        if ml[2]=="<=":
            if getvar(ml[1])==None:
                bc()
                continue
            if getvar(ml[3])!=None:
                if var[ml[1]]<=getvar(ml[3]):
                    continue
                else:
                    i=ifend+1
                    continue
            elif ifint(ml[3]):
                if var[ml[1]]<=ifint(ml[3]):
                    continue
                else:
                    i=ifend+1
                    continue
            else:
                bc()
                continue
        if ml[2]==">=":
            if getvar(ml[1])==None:
                bc()
                continue
            if getvar(ml[3])!=None:
                if var[ml[1]]>=getvar(ml[3]):
                    continue
                else:
                    i=ifend+1
                    continue
            elif ifint(ml[3]):
                if var[ml[1]]>=ifint(ml[3]):
                    continue
                else:
                    i=ifend+1
                    continue
            else:
                bc()
                continue
print("\033[1;33m代码运行结束\033[1;0m")
'''
var a
print a
end

var a 100
print a
end

var a
input a
print a
end

var a
= a 100
print a
end

var a
var b
input a
input b
* a b
print a
/ b 3
print b
end

var a
var b
input a
input b
* a b
print a
end

var a
var b
input b
= a b
print a
end

a:
print 100
goto a
end

a:
var a
var b
input a
input b
* a b
print a
goto a
end

a:
print 100
b:
print 100000000000000000000000
goto b
goto a
end

var a 100
print a
del a
print a
end

var a 1
if a == 1 abc
print 1
if a == 2 bca
print 2
bca.end
if a == 1 cab
print 3
cab.end
abc.end
print 4
end

var count
input count
a:
print count
- count 1
if count > 0 loop
goto a
loop.end
end

var count1
var count2
input count1
loop:
+ count2 1
print count2
if count1 > count2 do
goto loop
do.end
end

var a
exit
print a
end

var count1
var count2 2
var count1_
input count1
if count1 <= 1 do0
print "不是质数"
exit
do0.end
if count1 == 2 do_
print "是质数"
exit
do_.end
loop:
= count1_ count1
% count1_ count2
if count1_ == 0 do1
print "不是质数"
exit
do1.end
+ count2 1
if count1 > count2 do2
goto loop
do2.end
print "是质数"
end

list a 2
var b 100
b = a 1
print b
print a 0
end

var a_ 100
var b 0
list a 2
a b = a_
print a 0
end

var a 0
var ls
list l1 5
l:
input ls
l1 a = ls
+ a 1
if a < 5 do
goto l
do.end
print l1
l2:
- a 1
print l1 a
if a > 0 do1
goto l2
do1.end
end

list a 0
var a
input a
var i
loop:
sizeup a
var ls
input ls
a i = ls
print a i
+ i 1
del ls
if i < a xif
goto loop
xif.end
end
'''