import os
def run(save):
    print("\033[1;33m开始运行\033[1;0m")
    try:
        os.system("node "+save)
    except:...
    print("\033[1;33m运行结束\033[1;0m")
js_kw=[
    "break",
    "delete",
    "function",
    "return",
    "typeof",
    "case",
    "do",
    "if",
    "switch",
    "var",
    "catch",
    "else",
    "in",
    "this",
    "void",
    "continue",
    "false",
    "instanceof",
    "throw",
    "while",
    "debugger",
    "finally",
    "new",
    "true",
    "with",
    "default",
    "for",
    "null",
    "try",
    "abstract",
    "double",
    "goto",
    "native",
    "static",
    "boolean",
    "enum",
    "implements",
    "package",
    "super",
    "byte",
    "export",
    "import",
    "private",
    "synchronized",
    "char",
    "extends",
    "int",
    "protected",
    "throws",
    "class",
    "final",
    "interface",
    "public",
    "transient",
    "const",
    "float",
    "long",
    "short",
    "volatile",
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
            if s in js_kw:
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
        elif code[p] in '`':
            s=code[p]
            p+=1
            while p<len(code) and code[p]!='`':
                if code[p]=='\\':
                    s+=code[p]
                    p+=1
                    if p<len(code):
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