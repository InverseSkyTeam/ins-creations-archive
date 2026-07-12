# import sys  
# sys.setrecursionlimit(10000)

TRUE = (lambda a: (lambda b: a))
FALSE = (lambda a: (lambda b: b))
IF = (lambda cond: (lambda expr1: (lambda expr2: cond(expr1)(expr2))))
AND = (lambda a: (lambda b: IF(a)(b)(FALSE)))
OR = (lambda a: (lambda b: IF(a)(TRUE)(b)))
NOT = (lambda a: IF(a)(FALSE)(TRUE))
ONE = (lambda g: (lambda z: g(z)))
TWO = (lambda g: (lambda z: g(g(z))))
THREE = (lambda g: (lambda z: g(g(g(z)))))
ADD = (lambda a: (lambda b: (lambda g: (lambda z: a(g)(b(g)(z))))))
MUL = (lambda a: (lambda b: (lambda g: (lambda z: a(lambda x: b(g)(x))(z)))))
SUB = (lambda a: (lambda b: b(lambda x: (lambda g: (lambda z: x(lambda u: (lambda h: h(u(g))))(lambda _: z)(lambda y: y))))(a)))
IS_ZERO = (lambda a: a(lambda _: FALSE)(TRUE))
EQ = (lambda a: (lambda b: AND(IS_ZERO(SUB(a)(b)))(IS_ZERO(SUB(b)(a)))))
LT = (lambda a: (lambda b: NOT(IS_ZERO(SUB(b)(a)))))
LE = (lambda a: (lambda b: IS_ZERO(SUB(a)(b))))
GT = (lambda a: (lambda b: NOT(IS_ZERO(SUB(a)(b)))))
GE = (lambda a: (lambda b: IS_ZERO(SUB(b)(a))))
NIL = (lambda onpair: (lambda onnil: onnil(VOID)))
PAIR = (lambda a: (lambda b: (lambda onpair: (lambda onnil: onpair(a)(b)))))
IS_NIL = (lambda pair: pair(lambda fst: (lambda rst: FALSE))(lambda x: TRUE))
IS_PAIR = (lambda pair: pair(lambda fst: (lambda rst: TRUE))(lambda x: FALSE))
FIRST = (lambda pair: pair(lambda fst: (lambda rst: fst))(VOID))
REST = (lambda pair: pair(lambda fst: (lambda rst: rst))(VOID))
Y = lambda f: (lambda x: f(lambda z: x(x)(z)))(lambda x: f(lambda z: x(x)(z)))
POWER = Y(
    lambda power: (lambda a: (lambda b: IF(EQ(b)(ONE))(lambda x: a(x))(lambda x: MUL(a)(power(a)(SUB(b)(ONE)))(x))))
)


def toint(n):
    return n(lambda x: x + 1)(0)
print(toint(
    POWER(THREE)(TWO)
))


"""
我觉得有必要为这一大堆lambda演算的源码配上每一个演算的理论推导
true(a)(b) = a
false(a)(b) = b
if(cond)(expr1)(expr2) = cond(expr1)(expr2)
推导{
  if(true)(expr1)(expr2)
    = true(expr1)(expr2)
    = expr1
  if(false)(expr1)(expr2)
    = false(expr1)(expr2)
    = expr2
}
and(a)(b) = if(a)(b)(false)
or(a)(b) = if(a)(true)(b)
not(a) = if(a)(false)(true)

one(g)(z) = g(z)
two(g)(z) = g(g(z))
n(g)(z) = g^n (z)
a+b (g)(z) = g^(a+b) (z)
a*b (g)(z) = g^(a*b) (z)
...
add(a)(b) = (lambda g: (lambda z: a(g)(b(g)(z))))
理论推导{
  a+b = (lambda g: (lambda z: g^(a+b) (z)))
  b(g)(z)
    = g^b(z)
  a(g)(b(g)(z))
    = a(g)(g^b(z))
    = g^a(g^b(z))
    = g^(a+b) (z)
  add(a)(b)
    = (lambda g: (lambda z: a(g)(b(g)(z))))
    = (lambda g: (lambda z: g^(a+b) (z)))
    = a+b
  two = (lambda g: (lambda z: g(g(z))))
  add(one)(one)
    = (lambda g: (lambda z: one(g)(one(g)(z))))
    = (lambda g: (lambda z: g(one(g)(z))))
    = (lambda g: (lambda z: g(g(z))))
    = two
}
mul(a)(b) = (lambda g: (lambda z: a(lambda x: b(g)(x))(z)))
推导{
  a*b = (lambda g: (lambda z: g^(a*b) (z)))
  b(g)(x)
    = g^b (x)
  lambda x: b(g)(x)
    = lambda x: g^b (x)
  a(lambda x: b(g)(x))(z)
    = a(lambda x: g^b (x))(z)
    = (lambda x: g^b (x))^a (z)
    = (lambda x: g^b (x))^(a-1) ((lambda x: g^b (x))(z))
    = (lambda x: g^b (x))^(a-1) (g^b (z))
    = (lambda x: g^b (x))^(a-2) ((lambda x: g^b (x))(g^b (z)))
    = (lambda x: g^b (x))^(a-2) (g^b (g^b (z)))
    = (lambda x: g^b (x))^(a-2) (g^(b*2) (z))
    = ...
    = (lambda x: g^b (x))^(a-a) (g^(b*a) (z))
    = g^(a*b) (z)
  mul(a)(b)
    = (lambda g: (lambda z: a(lambda x: b(g)(x))(z)))
    = (lambda g: (lambda z: g^(a*b) (z)))
    = a*b
  one = (lambda g: (lambda z: g(z)))
  two = (lambda g: (lambda z: g(g(z))))
  mul(one)(two)
    = (lambda g: (lambda z: one(lambda x: two(g)(x))(z)))
    = (lambda g: (lambda z: (lambda x: two(g)(x))(z)))
    = (lambda g: (lambda z: (two(g)(z))))
    = (lambda g: (lambda z: g(g(z))))
    = two
}
sub(a)(b) = b(lambda x: (lambda g: (lambda z: x(lambda u: (lambda h: h(u(g))))(lambda _: z)(lambda y: y))))(a)
推导{
  a(g)(z) = g^a (z)
  令X满足X^n (z) = (lambda h: h(g^(n-1) (z)))
  则
  a(X)(z)
    = X^a (z)
    = (lambda h: h(g^(a-1) (z)))
    = (lambda h: h((a-1) (g)(z)))
  a(X)(z)(lambda y: y)
    = (lambda h: h((a-1) (g)(z)))(lambda y: y)
    = (a-1) (g)(z)
  令pred(a)(g)(z)=(a-1) (g)(z)
  则pred(a)(g)(z) = a(X)(z)(lambda y: y)
  pred(a)
    = (lambda g: (lambda z: a(X)(z)(lambda y: y)))
  观察到当X(u) = (lambda h: h(u(g)))时
  X(lambda _: z) = (lambda h: h(z))
  X^2 (lambda _: z)
    = X(X(lambda _: z))
    = X(lambda h: h(z))
    = (lambda h: h((lambda h: h(z))(g)))
    = (lambda h: h(g(z)))
  X^n (lambda _: z) = (lambda h: h(g^(n-1) (z)))
  pred(a)
    = (lambda g: (lambda z:
      a(lambda u: (lambda h: h(u(g))))
      (lambda _: z)
      (lambda y: y)))
  sub(a)(b)
    = b(lambda x: pred(x))(a)
    = b(lambda x: (lambda g: (lambda z: 
          x(lambda u: (lambda h: h(u(g))))
          (lambda _: z)
          (lambda y: y))))(a)
}
is_zero(a) = a(lambda _: false)(true)
eq(a)(b) = and(is_zero(sub(a)(b)))(is_zero(sub(b)(a)))
lt(a)(b) = not(is_zero(sub(b)(a)))
le(a)(b) = is_zero(sub(a)(b))
gt(a)(b) = not(is_zero(sub(a)(b)))
ge(a)(b) = is_zero(sub(b)(a))
ge = (lambda a: (lambda b: is_zero(sub(a)(b))))


nil = (lambda onPair: (lambda onNil: onNil(void)))
pair(a)(b) = (lambda onPair: (lambda onNil: onPair(a)(b)))
is_nil(thenil) = thenil(lambda fst: (lambda rst: false))(lambda x: true)
推导{
  is_nil(thenil)
    = thenil(lambda fst: (lambda rst: false))(lambda x: true)
    = (lambda onPair: (lambda onNil: onNil(void)))(lambda fst: (lambda rst: false))(lambda x: true)
    = (lambda x: true)(void)
    = true
  is_nil(thepair)
    = thepair(lambda fst: (lambda rst: false))(lambda x: true)
    = (lambda onPair: (lambda onNil: onPair(a)(b)))(lambda fst: (lambda rst: false))(lambda x: true)
    = (lambda fst: (lambda rst: false))(a)(b)
    = false
}
is_pair(thepair) = thepair(lambda fst: (lambda rst: true))(lambda x: false)
first(thepair) = thepair(lambda fst: (lambda rst: fst))(void)
rest(thepair) = thepair(lambda fst: (lambda rst: rst))(void)
推导{
  first(thepair)
    = (lambda fst: (lambda rst: fst))(a)(b)
    = a
  rest(thepair)
    = (lambda fst: (lambda rst: rst))(a)(b)
    = b
}


"""