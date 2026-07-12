"""
显然，Tiny Lisp作为配置语言是不行的
类型：
    int
    str
    bool
    NoneType
    list
    object(dict)
    function
"""
from typing import Any
import time
import os
import sys
keywords = [
    'if', 'else', 'while', 'def', 'var',
    'return', 'break', 'continue',
    'True', 'False', 'None', 'func',
]
escape = {
    'r': '\r',
    't': '\t',
    'a': '\a',
    'f': '\f',
    'v': '\v',
    'b': '\b',
    'n': '\n',
    '"': '"',
    '\'': '\'',
    '\\': '\\',
}
operators = [
    '+', '-', '*', '/', '%',
    '==', '!=', '>', '<', '>=', '<=',
    '<<', '>>', '&&', '||', '&', '|', '^', '!', '~',
    ',', '.', '[', ']', '(', ')', '{', '}', ':', '=',
]
priority = {
    '*': 100, '/': 100, '%': 100,
    '+': 99, '-': 99,
    '<<': 98, '>>': 98,
    '==': 97, '!=': 97,
    '>': 96, '<': 96, '>=': 96, '<=': 96,
    '&': 95, '^': 94, '|': 93,
    '&&': 92, '||': 91,
}
ASSIGN = 0
EXPR = 1
IF = 2
WHILE = 3
DEF = 4
RETURN = 5
BREAK = 6
CONTINUE = 7
POSTFIX = 8
UNIT = 9
CONST = 10
VAR = 11
NEW_LIST = 12
NEW_DICT = 13
VAR_DEF = 14
NEW_FUNC = 15

INDEX = 0
CALL = 1
GET_ATTR = 2


class Scope:
    def __init__(self, parent, variables: dict):
        self.parent, self.variables = parent, variables

    def find(self, name: str):
        if name in self.variables:
            return self.variables[name]
        elif isinstance(self.parent, Scope):
            return self.parent.find(name)
        else:
            raise Error()

    def set(self, name: str, value):
        if name in self.variables:
            self.variables[name] = value
        elif isinstance(self.parent, Scope):
            return self.parent.set(name, value)
        else:
            raise Error()

    def define(self, name: str, value):
        self.variables[name] = value


class Error(Exception):
    __str__ = __repr__ = lambda self: "Error!"


class Function:
    def __init__(self, para: list[str], body: list[tuple], closure: Scope):
        self.para, self.body, self.closure = para, body, closure

    def __call__(self, *args):
        v = run(self.body, Scope(self.closure, dict(zip(self.para, args))))
        if v is None:
            return None
        return v[1]
    

class Method:
    def __init__(self, obj: dict, func: Function):
        self.obj, self.func = obj, func

    def __call__(self, *args):
        scope = Scope(self.func.closure, dict(zip(self.func.para, args)))
        scope.define("this", self.obj)
        v = run(self.func.body, scope)
        if v is None:
            return None
        return v[1]


def tokenize(code: str) -> list[str]:
    res: list[str] = []
    p = 0
    while p < len(code):
        while p < len(code) and code[p] in ' \n\t#':
            if code[p] == '#':
                while p < len(code) and code[p] != '\n':
                    p += 1
            else:
                p += 1
        if p >= len(code):
            break
        elif code[p].isdigit():
            s = ""
            while p < len(code) and (code[p].isdigit() or code[p] == '.'):
                s += code[p]
                p += 1
            res.append(s)
        elif code[p].isalpha() or code[p] == '_':
            s = ""
            while p < len(code) and (code[p].isalnum() or code[p] == '_'):
                s += code[p]
                p += 1
            if s in keywords:
                res.append('*' + s)
            else:
                res.append(s)
        elif code[p] == '"':
            s = '"'
            p += 1
            while p < len(code) and code[p] != '"':
                if code[p] == '\\':
                    p += 1
                    if p >= len(code):
                        raise Error()
                    elif code[p].isdigit():
                        if p + 2 >= len(code):
                            raise Error()
                        s += chr(int(code[p: p+3]))
                        p += 3
                    elif code[p] in escape:
                        s += escape[code[p]]
                        p += 1
                    else:
                        raise Error()
                else:
                    s += code[p]
                    p += 1
            if p >= len(code):
                raise Error()
            s += '"'
            p += 1
            res.append(s)
        elif code[p: p+2] in operators:
            res.append(code[p: p+2])
            p += 2
        elif code[p] in operators:
            res.append(code[p])
            p += 1
        else:
            raise Error()
    res.append('')
    return res


def parse(tokens: list[str]) -> list[tuple]:
    pos: int = 0
    token = tokens[0]

    def eat(ex=None) -> str:
        nonlocal pos, token
        if ex is None or ex == token:
            pos += 1
            token = tokens[pos]
            return tokens[pos-1]
        raise Error()

    def eat_id() -> str:
        if token == '' or not (token[0].isalpha() or token[0] != '_'):
            raise Error()
        return eat()

    def parse_expression() -> tuple:
        res: list = [parse_unit()]
        stack: list[str] = []
        while token in priority or token in ('(', ')'):
            if token == ')' and '(' not in stack:
                break
            op = eat()
            if op == '(':
                stack.append('(')
            elif op == ')':
                while stack and stack[-1] != '(':
                    res.append(stack.pop())
                if not stack:
                    raise Error()
                stack.pop()
            else:
                while stack and priority[stack[-1]] >= priority[op]:
                    res.append(stack.pop())
                stack.append(op)
            res.append(parse_unit())
        while stack:
            res.append(stack.pop())
        if len(res) == 1:
            return res[0]
        return POSTFIX, res

    def parse_unit() -> tuple:
        pre: list[str] = []
        while token in ['+', '-', '!', '~']:
            pre.append(eat())
        if token == '':
            raise Error()
        elif token[0].isdigit():
            core = (CONST, int(eat()))
        elif token[0] == '"':
            core = (CONST, eat()[1: -1])
        elif token[0].isalpha() or token[0] == '_':
            core = (VAR, eat())
        elif token == '[':
            eat()
            items: list[tuple] = []
            if token != ']':
                items.append(parse_expression())
                while token == ',':
                    eat()
                    items.append(parse_expression())
            eat(']')
            core = (NEW_LIST, items)
        elif token == '{':
            eat()
            kv_pairs: list[tuple[tuple, tuple]] = []
            if token != '}':
                key = parse_expression()
                eat(':')
                value = parse_expression()
                kv_pairs.append((key, value))
                while token == ',':
                    eat(',')
                    key = parse_expression()
                    eat(':')
                    value = parse_expression()
                    kv_pairs.append((key, value))
                if token == ',':
                    eat()
            eat('}')
            core = (NEW_DICT, kv_pairs)
        elif token == '*func':
            eat()
            eat('(')
            para: list[str] = []
            if token != ')':
                para.append(eat_id())
                while token == ',':
                    eat()
                    para.append(eat_id())
            eat(')')
            return NEW_FUNC, para, parse_block()
        elif token == '*True':
            eat()
            core = (CONST, True)
        elif token == '*False':
            eat()
            core = (CONST, False)
        elif token == '*None':
            eat()
            core = (CONST, None)
        else:
            raise Error()
        extra: list[tuple] = []
        while token in ('[', '(', '.'):
            if token == '[':
                eat()
                extra.append((INDEX, parse_expression()))
                eat(']')
            elif token == '(':
                eat()
                args: list[tuple] = []
                if token != ')':
                    args.append(parse_expression())
                    while token == ',':
                        eat()
                        args.append(parse_expression())
                eat(')')
                extra.append((CALL, args))
            elif token == '.':
                eat()
                extra.append((GET_ATTR, eat_id()))
        return UNIT, pre, core, extra

    def parse_statement() -> tuple:
        if token == '*if':
            eat()
            cases = [(parse_expression(), parse_block())]
            while token == '*else':
                eat()
                if token == '*if':
                    eat()
                    cases.append((parse_expression(), parse_block()))
                else:
                    return IF, cases, parse_block()
            return IF, cases, []
        elif token == '*while':
            eat()
            return WHILE, parse_expression(), parse_block()
        elif token == '*def':
            eat()
            name = eat_id()
            eat('(')
            para: list[str] = []
            if token != ')':
                para.append(eat_id())
                while token == ',':
                    eat()
                    para.append(eat_id())
            eat(')')
            return DEF, name, para, parse_block()
        elif token == '*var':
            eat()
            name_value_pairs: list[tuple[str, tuple]] = []
            name = eat_id()
            if token == '=':
                eat()
                value = parse_expression()
            else:
                value = (CONST, None)
            name_value_pairs.append((name, value))
            while token == ',':
                eat()
                name = eat_id()
                if token == '=':
                    eat()
                    value = parse_expression()
                else:
                    value = (CONST, None)
                name_value_pairs.append((name, value))
            return VAR_DEF, name_value_pairs
        elif token == '*return':
            eat()
            return RETURN, parse_expression()
        elif token == '*break':
            eat()
            return BREAK,
        elif token == '*continue':
            eat()
            return CONTINUE,
        else:
            left = parse_expression()
            if token == '=':
                eat()
                right = parse_expression()
                return ASSIGN, left, right
            return EXPR, left

    def parse_block() -> list[tuple]:
        res: list[tuple] = []
        eat('{')
        while token != '}':
            res.append(parse_statement())
        eat()
        return res

    ast: list[tuple] = []
    while token != '':
        ast.append(parse_statement())
    return ast


def run(ast: tuple | list, scope: Scope) -> Any:
    if isinstance(ast, list):
        for stmt in ast:
            v = run(stmt, scope)
            if isinstance(v, tuple):
                return v
        return None
    else:
        match ast:
            case 0, left, right:  # ASSIGN
                if left[0] != UNIT or left[1]:
                    raise Error()
                if left[3]:
                    if left[3][-1][0] == INDEX:
                        changed_left = (left[0], left[1], left[2], left[3][:-1])
                        base = run(changed_left, scope)
                        base[run(left[3][-1][1], scope)] = run(right, scope)
                    elif left[3][-1][0] == GET_ATTR:
                        changed_left = (left[0], left[1], left[2], left[3][:-1])
                        base = run(changed_left, scope)
                        base[left[3][-1][1]] = run(right, scope)
                elif left[2][0] == VAR:
                    scope.set(left[2][1], run(right, scope))
                else:
                    raise Error()
            case 1, expr:  # EXPR
                run(expr, scope)
                return None
            case 2, cases, default:  # IF
                for cond, body in cases:
                    if run(cond, scope):
                        return run(body, scope)
                return run(default, scope)
            case 3, cond, body:  # WHILE
                while run(cond, scope):
                    v = run(body, scope)
                    if isinstance(v, tuple) and v[0] == RETURN:
                        return v
                    if isinstance(v, tuple) and v[0] == BREAK:
                        break
                return None
            case 4, name, para, body:  # DEF
                scope.define(name, Function(para, body, scope))
            case 5, expr:  # RETURN
                return RETURN, run(expr, scope)
            case 6,:  # BREAK
                return BREAK,
            case 7,:  # CONTINUE
                return CONTINUE,
            case 8, expr:  # POSTFIX
                stack = []
                for i in expr:
                    if isinstance(i, tuple):
                        stack.append(run(i, scope))
                    else:
                        b = stack.pop()
                        a = stack.pop()
                        stack.append({
                            '+': lambda x, y: x + y,
                            '-': lambda x, y: x - y,
                            '*': lambda x, y: x * y,
                            '/': lambda x, y: int(x / y),
                            '%': lambda x, y: x % y,
                            '==': lambda x, y: x == y,
                            '!=': lambda x, y: x != y,
                            '>': lambda x, y: x > y,
                            '<': lambda x, y: x < y,
                            '>=': lambda x, y: x >= y,
                            '<=': lambda x, y: x <= y,
                            '<<': lambda x, y: x << y,
                            '>>': lambda x, y: x >> y,
                            '&&': lambda x, y: x and y,
                            '||': lambda x, y: x or y,
                            '&': lambda x, y: x & y,
                            '|': lambda x, y: x | y,
                            '^': lambda x, y: x ^ y,
                        }[i](a, b))
                return stack[0]
            case 9, prev, core, extra:  # UNIT
                res: Any
                if core[0] == CONST:
                    res = core[1]
                elif core[0] == VAR:
                    res = scope.find(core[1])
                elif core[0] == NEW_LIST:
                    res = [run(i, scope) for i in core[1]]
                elif core[0] == NEW_DICT:
                    res = {}
                    for k, v in core[1]:
                        res[run(k, scope)] = run(v, scope)
                else:
                    raise Error()
                for i in extra:
                    if i[0] == INDEX:
                        res = res[run(i[1], scope)]
                    elif i[0] == CALL:
                        if callable(res):
                            res = res(*[run(x, scope) for x in i[1]])
                        else:
                            raise Error()
                    elif i[0] == GET_ATTR:
                        v = res[i[1]]
                        if isinstance(v, Function):
                            res = Method(res, v)
                        else:
                            res = v
                    else:
                        raise Error()
                for i in prev:
                    res = {
                        '+': lambda a: +a,
                        '-': lambda a: -a,
                        '!': lambda a: not a,
                        '~': lambda a: ~a,
                    }[i](res)
                return res
            case 10, value:  # CONST
                return value
            case 11, name:  # VAR
                return scope.find(name)
            case 12, items:  # NEW_LIST
                return [run(i, scope) for i in items]
            case 13, kv_pairs:  # NEW_DICT
                res = {}
                for k, v in kv_pairs:
                    res[run(k, scope)] = run(v, scope)
                return res

            case 14, variables:  # VAR_DEF
                for name, value in variables:
                    scope.define(name, run(value, scope))
            case 15, para, body:  # NEW_FUNC
                return Function(para, body, scope)


def run_code(code: str, scope: Scope):
    run(parse(tokenize(code)), scope)


scope = Scope(None, {
    'std': {
        'print': lambda *a: print(*a, end="", flush=True, sep=""),
        'println': lambda *a: print(*a, flush=True, sep=""),
        'readln': input,
        'ord': ord,
        'chr': chr,
        'len': len,
    },
})
if __name__ == "__main__":
    t = time.time()
    run_code(
        '''
    var i = 1, res = 1
    while i <= 100000 {
        res = res * i
        i = i + 1
    }
    # std.println(res)
        ''',
        scope
    )
    print(time.time() - t)

"""
var i = 0
std.println(i)
while True {
    i = i + 1
    if i == 5 {
        continue
    }
    if i == 10 {
        break
    }
    std.println(i)
}


def add(a, b) {
    std.println(a, " ", b)
    return a + b
}

std.println(add(10, 20))


var obj = {
    "a": 10,
    "printA": func() {
        std.println(this.a)
    },
    "setA": func(a) {
        this.a = a
    }
}
obj.printA()
obj.setA(20)
obj.printA()


var lst = [1, 2, [2, 4, 5]]
lst[2][0] = 3
std.println(lst)
"""


def run_file(file):
    print("\033[1;33m开始运行\033[1;0m")
    try:
        run_code(open(file, "r", encoding="utf-8").read(), scope)
    except Exception as e:
        print(e)
    print("\033[1;33m运行结束\033[1;0m")


def render(code: str, theme):
    res=[]
    p=0
    while p<len(code):
        if code[p].isdigit():
            while p<len(code) and (code[p].isdigit() or code[p] in '.'):
                res.append(theme["number"]+code[p])
                p+=1
        elif code[p].isalpha() or code[p]=="_":
            s=""
            while p<len(code) and (code[p].isalnum() or code[p]=='_'):
                s+=code[p]
                p+=1
            if s in keywords:
                for i in s:
                    res.append(theme["keyword"]+i)
            else:
                for i in s:
                    res.append(theme["identifier"]+i)
        elif code[p] in '"':
            s=code[p]
            x=s
            p+=1
            while p<len(code) and code[p]!='\n' and code[p]!=x:
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
        elif code[p]=='#':
            while p<len(code) and code[p]!='\n':
                res.append(theme["comment"]+code[p])
                p+=1
        elif code[p] in operators:
            res.append(theme["operator"]+code[p])
            p+=1
        elif code[p:p+2] in operators:
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
