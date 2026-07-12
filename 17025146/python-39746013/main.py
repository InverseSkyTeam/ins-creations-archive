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

def toint(n):
    return n(lambda x: x + 1)(0)
print(toint( # 我说这里面写的是Lisp你有意见么?
    IF(AND(GREATER(THREE)(TWO))(LESSEQ(TWO)(TWO)))(SUB(FOUR)(THREE))(POW(TWO)(TWO))
))