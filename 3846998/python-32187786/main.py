var={}
array={}
def getpair(st,pos,pair):#匹配括号
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
            ans.append(c[i+1:getpair(c,i,{c[i]:pairs[c[i]]})])
            ans.append(pairs[c[i]])
            i=getpair(c,i,{c[i]:pairs[c[i]]})
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
def getvar(a):
    try:
        return(var[a])
    except:
        return(None)
def getarr(a):
    try:
        return(array[a])
    except:
        return(None)
def getvarinhz(ml):#把后缀表达式里的变量换成数字
    ml=cutcode(ml,"+-*/%=|&><",{"[":"]","(":")"}," ")
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
sym="+-*/.~`!@#$%^&*_=|\\:;<,>"
def bc():
    print("错误！")
def cutline(code,sep=";"):#主要功能是把代码按";"分成一个一个语句
    ans=[[]]
    for i in code:
        if i==sep:
            ans.append([])
        else:
            ans[-1].append(i)
    return(ans)
def jy(name):#判断变量名是否合法
    if name=="":
        return(0)
    if name[0] in "123456789":
        return(0)
    for i in name:
        if i not in "_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890":
            return(0)
    return(1)
def prestr(a):
    return(a.replace("\\\\","\\").replace("\\n","\n").replace("\\t","\t"))
def delvar(dl):#为实现变量作用域做准备
    global array,var
    for i in dl:
        if getvar(i)!=None:
            del var[i]
        if getarr(i)!=None:
            del array[i]
def run(code):#运行代码
    global var,array
    dl=[]
    c=cutcode(code.replace("\n","").replace("\t","").replace("    ",""),sym,{"[":"]","{":"}","(":")"}," ")
    c=cutline(c)
    for ml in c:
        if ml==[]:
            continue
        if ml[0]=="var":
            if ml[1]!="{" or ml[3]!="}":
                bc()
                delvar(dl)
                return()
            x=cutline(cutcode(ml[2],"=,",{"(":")"},""),",")
            for v in x:
                while "(" in v:
                    v.remove("(")
                while ")" in v:
                    v.remove(")")
                aaa=hz_js(v[2])
                if v[1]!="=" or jy(v[0])==0 or aaa==None:
                    bc()
                    delvar(dl)
                    return()
                var[v[0]]=aaa
                dl.append(v[0])
        if ml[0]=="array":
            if ml[1]!="{" or ml[3]!="}":
                bc()
                delvar(dl)
                return()
            x=cutline(cutcode(ml[2],":,",{"(":")"},""),",")
            for v in x:
                while "(" in v:
                    v.remove("(")
                while ")" in v:
                    v.remove(")")
                aaa=hz_js(v[2])
                if v[1]!=":" or jy(v[0])==0 or aaa==None:
                    bc()
                    delvar(dl)
                    return()
                array[v[0]]=[0]*aaa
                dl.append(v[0])
        if ml[0]=="put":
            if ml[1]!="(" or ml[3]!=")":
                bc()
                delvar(dl)
                return()
            x=cutline(cutcode(ml[2],"",{"(":")","[":"]"},""),",")
            for v in x:
                if v[0]=="[" and v[2]=="]":
                    print(prestr(v[1]),end="")
                    continue
                while "(" in v:
                    v.remove("(")
                while ")" in v:
                    v.remove(")")
                aaa=hz_js(v[0])
                if aaa!=None:
                    print(aaa,end="")
        if len(ml)==7 and ml[0]=="if":
            if ml[1]!="(" or ml[3]!=")" or ml[4]!="{" or ml[6]!="}":
                bc()
                delvar(dl)
                return()
            aaa=hz_js(ml[2])
            if aaa:
                bbb=run(ml[5])
                if bbb=="break":
                    delvar(dl)
                    return("break")
                if bbb=="continue":
                    delvar(dl)
                    return("continue")
        if len(ml)==11 and ml[0]=="if":
            if ml[1]!="(" or ml[3]!=")" or ml[4]!="{" or ml[6]!="}" or ml[7]!="else" or ml[8]!="{" or ml[10]!="}":
                bc()
                delvar(dl)
                return()
            aaa=hz_js(ml[2])
            if aaa:
                bbb=run(ml[5])
                if bbb=="break":
                    delvar(dl)
                    return("break")
                if bbb=="continue":
                    delvar(dl)
                    return("continue")
            else:
                bbb=run(ml[9])
                if bbb=="break":
                    delvar(dl)
                    return("break")
                if bbb=="continue":
                    delvar(dl)
                    return("continue")
        if ml[0]=="break":
            delvar(dl)
            return("break")
        if ml[0]=="continue":
            delvar(dl)
            return("continue")
        if len(ml)==7 and ml[0]=="while":
            if ml[1]!="(" or ml[3]!=")" or ml[4]!="{" or ml[6]!="}":
                bc()
                delvar(dl)
                return()
            aaa=hz_js(ml[2])
            while aaa:
                bbb=run(ml[5])
                if bbb=="break":
                    break
                aaa=hz_js(ml[2])
        if ml[0]=="getstr":
            while "(" in ml:
                ml.remove("(")
            while ")" in ml:
                ml.remove(")")
            if getarr(ml[1])==None:
                bc()
                delvar(dl)
                return()
            s=input()
            array[ml[1]]=[]
            for j in s:
                array[ml[1]].append(ord(j))
        if ml[0]=="putchar":
            while "(" in ml:
                ml.remove("(")
            while ")" in ml:
                ml.remove(")")
            aaa=hz_js(ml[1])
            print(chr(aaa),end="")
        if ml[0]=="let":
            while "(" in ml:
                ml.remove("(")
            while ")" in ml:
                ml.remove(")")
            v=cutcode(ml[1],"",{"[":"]"},"")
            aaa=hz_js(ml[2])
            if getvar(v[0])!=None:
                var[v[0]]=aaa
            elif getarr(v[0])!=None and len(v)==4:
                bbb=hz_js(v[2])
                if bbb>=len(array[v[0]]):
                    bc()
                    delvar(dl)
                    return()
                array[v[0]][bbb]=aaa
print('''temp-integer2.0.0
暂时没有教程
这是判断质数的代码
var{a=(input),i=(2),flag=(1)};
if(a 2<){
    let(flag)(0);
};
if(a 2==){
}else{
    while(i a<){
        if(a i%0==){
            let(flag)(0);
            break;
        };
        let(i)(i 1+);
    };
};
if(flag){
    put((a),[是质数]);
}else{
    put((a),[不是质数]);
};
end
可以写代码了，end结束''')
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
var{a=(1 2+)};
array{arr:(a 1-)};
put([:],(a),(arr[0]),(arr[1]));
end

if(1 1==){
    put((1));
};
end

while(1 1==){
    put((1),[\n]);
};
end

array{a:0};
getstr(a);
putchar(a[0]);
end

var{a=0};
let(a)(1);
put((a));
end

array{a:1};
let(a[0])(1);
put((a[0]));
end

if(1){
    var{
        i=(10)
    };
    put(
        (i)
    );
};
end

var{a=(input),i=(2),flag=(1)};
if(a 2<){
    let(flag)(0);
};
if(a 2==){
}else{
    while(i a<){
        if(a i%0==){
            let(flag)(0);
            break;
        };
        let(i)(i 1+);
    };
};
if(flag){
    put((a),[是质数]);
}else{
    put((a),[不是质数]);
};
end

put((1 2<=));
end

array{a:(10)};
put((len(a)));
end
'''