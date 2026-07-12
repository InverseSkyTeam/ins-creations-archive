ast = [
    # 预备
    ('Const',1),
    ('Set','a'),
    ('Const',1),
    ('Set','b'),
    
    # 条件
    ('Var','b'),
    ('Const',100000),
    ('Bin','<'),
    ('Cond',9),
    
    # 循环
    ('Var','b'),
    ('Const',1),
    ('Bin','+'),
    ('Set','b'),
    ('Var','a'),
    ('Var','b'),
    ('Bin','*'),
    ('Set','a'),
    ('Jump',4),
    
    # 结果
    ('Var','a'),
]
while p < length:
    p += 1
    tp, arg = ast[p]
    if tp == 'Const':
        stack.append(arg)
    elif tp == 'Var':
        stack.append(scope[-1][arg])
    elif tp == 'Bin':
        b = stack.pop()
        a = stack.pop()
        stack.append(binary[arg](a,b))
    elif tp == 'Unary':
        e = stack.pop()
        stack.append(binary[arg](e))
    elif tp == 'Set':
        scope[-1][arg] = stack.pop()
    elif tp == 'Cond':
        cond = stack.pop()
        if not cond:
            p += arg
    elif tp == 'Jump':
        p = arg - 1   # -1是因为下次循环会自动加1
    else:
        raise Exception(f'无Flag: {tp}')