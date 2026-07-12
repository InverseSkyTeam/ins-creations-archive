import os
def run(save):
    os.system(f"rustc "+save)
    print("\033[1;33m开始运行\033[1;0m")
    try:
        os.system(save[:save.rfind(".")])
    except:...
    print("\033[1;33m运行结束\033[1;0m")
cpp_kw=[
    "asm",
    "do",
    "if",
    "return",
    "typedef",
    "auto",
    "double",
    "inline",
    "short",
    "typeid",
    "bool",
    "dynamic_cast",
    "int",
    "signed",
    "typename",
    "break",
    "else",
    "long",
    "sizeof",
    "union",
    "case",
    "enum",
    "mutable",
    "static",
    "unsigned",
    "catch",
    "explicit",
    "namespace",
    "static_cast",
    "using",
    "char",
    "export",
    "new",
    "struct",
    "virtual",
    "class",
    "extern",
    "operator",
    "switch",
    "void",
    "const",
    "false",
    "private",
    "template",
    "volatile",
    "const_cast",
    "float",
    "protected",
    "this",
    "wchar_t",
    "continue",
    "for",
    "public",
    "throw",
    "while",
    "default",
    "friend",
    "register",
    "true",
    "delete",
    "goto",
    "reinterpret_cast",
    "try",
]
def render(code:str,theme:dict):
    op=[
        '+','-','*','/','%',
        '==','!=','>','<','>=','<=',
        '<<','>>','&&','||','&','|','^','~',
        '=','?',':','!',',',
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
            if s in cpp_kw:
                for i in s:
                    res.append(theme["keyword"]+i)
            else:
                for i in s:
                    res.append(theme["identifier"]+i)
        elif code[p:p+2]=="/*":
            s=code[p:p+2]
            p+=2
            while p<len(code) and code[p:p+2]!="*/":
                s+=code[p]
                p+=1
            s+=code[p:p+2]
            p+=2
            for i in s:
                res.append(theme["comment"]+i)
        elif code[p] in '\'"':
            s=code[p]
            x=s
            p+=1
            while p<len(code) and code[p]!='\n' and code[p]!=x:
                if code[p]=='\\':
                    s+=code[p]
                    p+=1
                    if p<len(code) and code[p] in '\'"\n':
                        s+=code[p]
                        p+=1
                else:
                    s+=code[p]
                    p+=1
            if p<len(code):
                s+=code[p]
                p+=1
            for i in s:
                res.append(theme["string"]+i)
        elif code[p]=='#':
            while p<len(code) and code[p]!='\n':
                res.append(theme["header"]+code[p])
                p+=1
        elif code[p:p+2]=='//':
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
    return rr+[tmp]