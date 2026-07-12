# 布尔值
TRUE = lambda x:lambda y:x # 布尔-真值
FALSE = lambda x:lambda y:y # 布尔-假值
# 数字
ZERO = lambda f: lambda x: x # 数字-0
ONE = lambda f: lambda x: f(x) # 数字-1
TWO = lambda f: lambda x: f(f(x)) # 数字-2
THREE = lambda f: lambda x: f(f(f(x))) # 数字-3
FOUR = lambda f: lambda x: f(f(f(f(x)))) # 数字-4
# 二元组
CONS = lambda a: lambda b: (lambda s: s(a)(b)) # 二元组
CAR = lambda p: p(TRUE) # 二元组-左值
CDR = lambda p: p(FALSE) # 二元组-右值
T = lambda p: CONS(SUCC(CAR(p)))(CAR(p))
# 逻辑运算
NOT = lambda x:x(FALSE)(TRUE) # 逻辑运算-非运算
AND = lambda x:lambda y:x(y)(x) # 逻辑运算-与运算
OR = lambda x:lambda y:x(x)(y) # 逻辑运算-或运算
# 数学运算
SUCC = lambda n: lambda f: lambda x: f(n(f)(x)) # 数学运算-后继
ADD = lambda x: lambda y: y(SUCC)(x) # 数学运算-加
PRED = lambda n: CDR(n(T)(CONS(ZERO)(ZERO))) # 数学运算-前继
SUB = lambda x: lambda y: y(PRED)(x) # 数学运算-减
MUL = lambda x: lambda y: lambda f: y(x(f)) # 数学运算-乘
POW = lambda a: lambda b : b(a) # 运算-数学乘方
# 比较运算
ISZERO = lambda n: n(lambda _: FALSE)(TRUE) # 比较运算-是否为0
GREATEREQ = lambda n:lambda m:ISZERO(n(PRED)(m)) # 比较运算-大于等于
LESSEQ = lambda n:lambda m:ISZERO(m(PRED)(n)) # 比较运算-小于等于
EQ = lambda m:lambda n:NOT(AND(GREATEREQ(m)(n))(LESSEQ(n)(m))) # 比较运算-等于
GREATER = lambda m:lambda n:NOT(LESSEQ(m)(n)) # 比较运算-大于
LESS = lambda m:lambda n:NOT(GREATEREQ(m)(n)) # 比较运算-小于
NOTEQ = lambda m:lambda n:NOT(EQ(m)(n)) # 比较运算-不等于
# 控制
IF = lambda b:lambda t:lambda f:b(t)(f) # 控制-条件判断
# 递归
# 写到这里突然就有Lisp内味了
Y = lambda f: (lambda x: f(lambda z: x(x)(z)))(lambda x: f(lambda z: x(x)(z))) # Y组合子
FACT = Y(
    lambda f: lambda n: ISZERO(n)\
    (lambda x: ONE(x))\
    (lambda x: MUL(n)(f(PRED(n)))(x))
    )
# 表达式
expression = lambda x:x

def toint(n):
    return n(lambda x: x + 1)(0)


import sys  
sys.setrecursionlimit(100000)

def lex(expr):
    _id = ["if","and","or","not","true","false"]
    symbol = {"=":"eq",
              ">":"gt",
              "<":"lt",
              ">=":"ge",
              "<=":"le",
              "!=":"ne",
              "(":"lbr",
              ")":"rbr",
              "+":"add",
              "-":"sub",
              "*":"mul",
              "^":"pow"}
    ret = []
    pos = 0
    char = expr[0]
    def advance():
        nonlocal pos,char,expr
        pos += 1
        if pos < len(expr):
            char = expr[pos]
        else:
            char = None
    def peek():
        if pos+1 < len(expr):
            return expr[pos+1]
        else:
            return ""
    while char:
        if char.isspace():
            advance()
            continue
        elif char == ";":
            while char != "\n" and char is not None:
                advance()
        elif char.isalpha():
            res = ""
            while char.isalnum():
                res += char
                advance()
            if res in _id:
                ret.append((res,res))
            else:
                ret.append(("variable",res))
            del res
        elif char.isdigit():
            res = ""
            while char.isdigit():
                res += char
                advance()
            ret.append(("number",int(res)))
        elif char in symbol:
            if char + peek() in symbol:
                res = char + peek()
                advance()
            else:
                res = char
            advance() 
            ret.append((symbol[res],res))
        else:
            raise Exception("错误")
    return ret
    
def parse(tokens):
    pos = 0
    token = tokens[pos]
    lam = expression
    op = {
        "add":ADD,
        "sub":SUB,
        "mul":MUL,
        "pow":POW,
        "and":AND,
        "or":OR,
        "gt":GREATER,
        "lt":LESS,
        "ge":GREATEREQ,
        "le":LESSEQ,
        "eq":EQ,
        "ne":NOTEQ
    }
    def eat(tp=None):
        nonlocal tokens,token,pos
        if token[0] == tp or not tp:
            pos += 1
            if pos < len(tokens):
                token = tokens[pos]
            else:
                token = None
        else:
            print(tokens[pos - 1],token,tokens[pos + 1])
            raise Exception("错误")
    def expr():
        nonlocal tokens,token,pos,expr
        if token[0] == "number":
            value = token[1]
            eat("number")
            def number(f):
                def num(x):
                    for i in range(value):
                        x = f(x)
                    return x
                return num
            return number
        elif token[0] in ("true","false"):
            tp = token[0]
            eat()
            if tp == "true":
                factor = TRUE
            else:
                factor = FALSE
            return factor
        else:
            eat("lbr")
            if token[0] == "number":
                node = expr()
            elif token[0] in ("and","or","add","sub","mul","pow","gt","lt","ge","le","eq","ne"):
                tp = token[0]
                eat()
                left = expr()
                right = expr()
                node = op[tp](left)(right)
            elif token[0] == "not":
                eat()
                factor = expr()
                node = NOT(factor)
            elif token[0] in ("true","false"):
                node = expr()
            elif token[0] == "if":
                eat()
                condition = expr()
                then = expr()
                elsenode = expr()
                node = IF(condition)(then)(elsenode)
            else:
                raise Exception("错误")
            eat("rbr")
            return node
    while token:
        lam = lam(expr())
    return lam
tokens = lex("(if true (+ 1000 2000) (* 2 3));当然,Lisp-Style的注释得有")
expr = parse(tokens)
print(toint(expr))