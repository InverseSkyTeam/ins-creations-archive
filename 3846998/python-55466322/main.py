"""
上古技术的拼凑产品
灵感本身来源于2022年初temp-integer2（integer系列第四代语言）
pre_parse来自于上古资料https://www.cnblogs.com/figure9/p/3620079.html
Ref来源于2022年底integer3.3.0pre
好久不直接在xes编辑器写东西了
其实还不错的
"""

prio = {
    '*': 2, '/': 2,
    '+': 1, '-': 1,
}


class Ref:
    def __init__(self, val: list):
        self.val = val
        self.tp = 'e'
        
    def __str__(self):
        return '(' + ' '.join(map(str, self.val)) + ')'
        # return str(self.val)
        
    __repr__ = __str__


def pre_parse(tokens: list):
    prog = Ref([])
    cur = prog
    stack = []
    refs = [prog]
    
    for i in tokens:
        if i == '(':
            stack.append(cur)
            cur.val.append(Ref([]))
            cur = cur.val[-1]
            refs.append(cur)
        elif i == ')':
            cur = stack.pop()
        else:
            cur.val.append(i)
    if cur != prog:
        raise Exception("Unclosed parenthesis")
    return prog, refs
    
    
def parse_factor(expr: list, pos: int):
    res = expr[pos]
    pos += 1
    while pos < len(expr) and isinstance(expr[pos], Ref):
        expr[pos].tp = 'f'
        res = Ref([res, expr[pos]])
        pos += 1
    return res, pos
    
    
def parse_expr(expr: list, pos: int):
    fac, pos = parse_factor(expr, pos)
    res = [fac]
    stack = []
    while pos < len(expr) and expr[pos] in prio:
        op = expr[pos]
        pos += 1
        while stack and prio[op] <= prio[stack[-1]]:
            r, l = res.pop(), res.pop()
            res.append(Ref([stack.pop(), l, r]))
        stack.append(op)
        fac, pos = parse_factor(expr, pos)
        res.append(fac)
    while stack:
        r, l = res.pop(), res.pop()
        res.append(Ref([stack.pop(), l, r]))
    if len(res) != 1:
        # print(res, stack)
        raise Exception("Wrong expr")
    return res[0], pos
    

def parse(expr: Ref):
    if expr.tp == 'e':
        res, pos = parse_expr(expr.val, 0)
        if pos != len(expr.val):
            raise Exception("Syntax error")
        expr.val = res.val
    elif expr.tp == 'f':
        res = []
        if len(expr.val):
            e, pos = parse_expr(expr.val, 0)
            res.append(e)
            while pos < len(expr.val):
                if expr.val[pos] != ',':
                    raise Exception("Expect ','")
                pos += 1
                e, pos = parse_expr(expr.val, pos)
                res.append(e)
        expr.val = res
    else:
        raise Exception(expr)


tokens = "1 * f ( 2 + 3 , 4 ) + 5".split(' ')
prog, refs = pre_parse(tokens)
prog.tp = 'e'
for i in refs:
    parse(i)
print(prog)
