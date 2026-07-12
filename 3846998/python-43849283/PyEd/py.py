import os
def render(code,theme:dict):
    op=[
        '+','-','*','/','%',
        '==','!=','>','<','>=','<=',
        '<<','>>','&','|','^','~',
    ]
    res=[]
    p=0
    while p<len(code):
        if code[p].isdigit():
            while p<len(code) and (code[p].isdigit() or code[p] in '.xbo'):
                res.append(theme["number"]+code[p])
                p+=1
        elif code[p].isalpha() or code[p]=="_":
            s=""
            while p<len(code) and (code[p].isalnum() or code[p]=='_'):
                s+=code[p]
                p+=1
            if s in __import__("keyword").kwlist:
                for i in s:
                    res.append(theme["keyword"]+i)
            elif s in dir(__builtins__):
                for i in s:
                    res.append(theme["builtin"]+i)
            elif s in ["self","cls"]:
                for i in s:
                    res.append(theme["this"]+i)
            else:
                for i in s:
                    res.append(theme["identifier"]+i)
        elif code[p:p+3] in ('"""',"'''"):
            s=code[p:p+3]
            x=s
            p+=3
            while p<len(code) and code[p:p+3]!=x:
                if code[p]=='\\':
                    s+=code[p]
                    p+=1
                    if code[p] in '\'"':
                        s+=code[p]
                        p+=1
                else:
                    s+=code[p]
                    p+=1
            s+=code[p:p+3]
            p+=3
            for i in s:
                if ord(i)>=128:
                    res.append("")
                res.append(theme["string"]+i)
        elif code[p] in '\'"':
            s=code[p]
            x=s
            p+=1
            while p<len(code) and code[p]!='\n' and code[p]!=x:
                if code[p]=='\\':
                    s+=code[p]
                    p+=1
                    if code[p] in '\'"\n':
                        s+=code[p]
                        p+=1
                else:
                    s+=code[p]
                    p+=1
            if p<len(code):
                s+=code[p]
                p+=1
            for i in s:
                if ord(i)>=128:
                    res.append("")
                res.append(theme["string"]+i)
        elif code[p]=='#':
            while p<len(code) and code[p]!='\n':
                res.append(theme["comment"]+code[p])
                p+=1
        elif code[p] in op:
            res.append(theme["operator"]+code[p])
            p+=1
        elif code[p:p+2] in op:
            res.append(theme["operator"]+code[p])
            p+=1
            res.append(theme["operator"]+code[p])
            p+=1
        else:
            if ord(code[p])>=128:
                res.append("")
            res.append(theme["others"]+code[p])
            p+=1
    rr=[]
    tmp=[]
    for i in res:
        if "\n" in i:
            rr.append(tmp)
            tmp=[]
        else:
            tmp.append(i)
    if tmp:
        return rr+[tmp]
    return rr
def run(save):
    print("\033[1;33m开始运行\033[1;0m")
    try:
        os.system(f"powershell python '{save}'")
    except:...
    print("\033[1;33m运行结束\033[1;0m")