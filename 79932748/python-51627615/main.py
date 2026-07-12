import sys
import time

stack = [[]]
scope = [{}]

binary = {
    '+': (lambda a, b: a + b),
    '-': (lambda a, b: a - b),
    '*': (lambda a, b: a * b),
    '/': (lambda a, b: a / b),
    '%': (lambda a, b: a % b),
    '//': (lambda a, b: a // b),
    '<<': (lambda a, b: a << b),
    '>>': (lambda a, b: a >> b),
    '^': (lambda a, b: a ^ b),
    '|': (lambda a, b: a | b),
    '&': (lambda a, b: a & b),
    '<': (lambda a, b: a < b),
    '>': (lambda a, b: a > b),
    '<=': (lambda a, b: a <= b),
    '>=': (lambda a, b: a >= b),
    '==': (lambda a, b: a == b),
    '!=': (lambda a, b: a != b),
}
unary = {
    '+': (lambda e: +e),
    '-': (lambda e: -e),
    '~': (lambda e: ~e),
}

class Fn:
    def __init__(self,param,pos):
        self.param = param
        self.pos = pos

ast = [
    ('Const',['x']),
    ('Fn',15),
    ('Var','x'),
    ('Const',1),
    ('Bin','=='),
    ('Cond',2),
    # x == 1
    ('Const',1),
    ('Quit',None),
    # x*f(x-1)
    ('Var','f'),
    ('Var','x'),
    ('Const',1),
    ('Bin','-'),
    ('List',1),
    ('Call',None),
    ('Var','x'),
    ('Bin','*'),
    ('Quit',None),
    
    ('Set','f'),
    ('Var','f'),
    ('Const',[1000]),
    ('Call',None),
]

begin = time.perf_counter()

p = -1
length = len(ast) - 1
while p < length:
    p += 1
    tp, *args = ast[p]
    if tp == 'Const':
        stack[-1].append(args[0])
    elif tp == 'Var':
        name = args[0]
        for _ in range(-1,-1-len(scope),-1):
            if name in scope[_]:
                value = scope[_][name]
                break
        stack[-1].append(value)
    elif tp == 'List':
        l = stack[-1][-args[0]:]
        del stack[-1][-args[0]:]
        stack[-1].append(l)
    elif tp == 'Bin':
        b = stack[-1].pop()
        a = stack[-1].pop()
        stack[-1].append(binary[args[0]](a,b))
    elif tp == 'Unary':
        e = stack[-1].pop()
        stack[-1].append(binary[args[0]](e))
    elif tp == 'Set':
        scope[-1][args[0]] = stack[-1].pop()
    elif tp == 'Cond':
        cond = stack[-1].pop()
        if not cond:
            p += args[0]
    elif tp == 'Jump':
        p = args[0] - 1   # -1是因为下次循环会自动加1
    elif tp == 'Quit':
        ret = stack[-1].pop()
        del stack[-1], scope[-1]
        p = stack[-1].pop() - 1
        stack[-1].append(ret)
    elif tp == 'Fn':
        stack[-1].append(Fn(stack[-1].pop(),p+1))
        p += args[0]
    elif tp == 'Call':
        farg = stack[-1].pop()
        fn = stack[-1].pop()
        stack[-1].append(p+1)
        stack.append([])
        scope.append(dict(zip(fn.param,farg)))
        p = fn.pos - 1
    else:
        raise Exception(f'无Flag: {tp}')

end = time.perf_counter()
print(end-begin)
# print(stack)
# print(scope)