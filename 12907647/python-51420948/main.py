ast = {
    'if-1': ['expr-1','expr-2','expr-3'],
    'expr-1': [('Const',int(input('输入0/1，进行对es解释器的条件判断: '))),],
    'expr-2': [('Binary','='),('Var','a'),('Const',1),],
    'expr-3': [('Binary','='),('Var','a'),('Const',2),],
}
scope = [{}]

def f_let(var,value):
    scope[-1][var] = value
    return value

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
    '=': f_let,
}
unary = {
    '+': (lambda e: +e),
    '-': (lambda e: -e),
    '~': (lambda e: ~e),
    'not': (lambda e: not e),
}

# 一般化
def generalize(value):
    # 常量
    if type(value) != tuple:
        return value
    # 变量查找
    name = value[0]
    for i in reversed(scope):
        if name in i:
            return i[name]
    return name   # 有可能使用了未命名的变量，这里不报错区分。

def expr(l):
    value_stack = []
    p = len(l)
    while p:
        p -= 1
        tp, value = l[p]
        if tp == 'Const':
            value_stack.append(value)
        elif tp == 'Var':   # 变量套个括号和普通字符串区分
            value_stack.append((value,))
        elif tp == 'Unary':
            value_stack[-1] = unary[value](generalize(value_stack[-1]))
        elif tp == 'Binary':
            left = generalize(value_stack.pop())
            right = generalize(value_stack.pop())
            value_stack.append(binary[value](left,right))
    return value_stack[-1]

def if_(l):
    condition = expr(ast[l[0]])
    if condition:
        return l[1]
    return l[2]

dic = {
    'expr': expr,
    'if': if_,
}

to = 'if-1'
while type(to) == str:
    stmt_type, stmt_id = to.split('-')
    to = dic[stmt_type](ast[to])
print(f'value: {to}')
print(f'scope: {scope}')