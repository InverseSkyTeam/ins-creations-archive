from copy import copy, deepcopy
from time import time
import sys


class Error(Exception):
    ...


escapes = {
    'r': '\r',
    't': '\t',
    'a': '\a',
    'f': '\f',
    'v': '\v',
    'b': '\b',
    'n': '\n',
    '\\': '\\',
    '"': '"',
    '\'': '\'',
}

keywords = {
    'if', 'else', 'while',
    'return', 'break', 'continue',
    'func', 'var', 'object',
    'True', 'False', 'None',
}

operators = [
    '+', '-', '*', '/', '%',
    '==', '!=', '>', '<', '>=', '<=',
    '<<', '>>', '&&', '||', '&', '|', '^', '!', '~',
    ',', '.', '[', ']', '(', ')', '{', '}', ':', '=', '->', ';',
]
prio = {
    '*': 100, '/': 100, '%': 100,
    '+': 99, '-': 99,
    '<<': 98, '>>': 98,
    '==': 97, '!=': 97,
    '>': 96, '<': 96, '>=': 96, '<=': 96,
    '&': 95, '^': 94, '|': 93,
    '&&': 92, '||': 91,
}


def lex(code: str):
    res = []
    pos = 0
    while pos < len(code):
        while pos < len(code) and code[pos] in ' \n\t#':
            if code[pos] == '#':
                while pos < len(code) and code[pos] != '\n':
                    pos += 1
            else:
                pos += 1
        if pos >= len(code):
            break
        elif code[pos] == '"':
            s = '"'
            pos += 1
            while pos < len(code) and code[pos] != '"':
                if code[pos] == '\\':
                    pos += 1
                    if pos >= len(code):
                        raise Error("Unexpected EOF.")
                    elif code[pos] in escapes:
                        s += escapes[code[pos]]
                        pos += 1
                    elif code[pos] == 'x':
                        pos += 1
                        if pos + 2 >= len(code):
                            raise Error("Unexpected EOF.")
                        s += chr(int(code[pos: pos + 2], 16))
                        pos += 2
                    elif code[pos] == 'u':
                        pos += 1
                        if pos + 4 >= len(code):
                            raise Error("Unexpected EOF.")
                        s += chr(int(code[pos: pos + 4], 16))
                        pos += 4
                    else:
                        raise Error("Unexpected escape sequence.")
                else:
                    s += code[pos]
                    pos += 1
            if pos >= len(code):
                raise Error()
            pos += 1
            s += '"'
            res.append(s)
        elif code[pos].isalpha() or code[pos] == '_':
            ident = ""
            while pos < len(code) and (code[pos].isalnum() or code[pos] == '_'):
                ident += code[pos]
                pos += 1
            if ident in keywords:
                res.append('*' + ident)
            else:
                res.append(ident)
        elif code[pos].isdigit():
            num = ""
            while pos < len(code) and (code[pos].isdigit() or code[pos] == '.'):
                num += code[pos]
                pos += 1
            res.append(num)
        elif code[pos: pos + 2] in operators:
            res.append(code[pos: pos + 2])
            pos += 2
        elif code[pos] in operators:
            res.append(code[pos])
            pos += 1
        else:
            raise Error(code[pos])
    return res + ['']


class Scope:
    def __init__(self, parent):
        self.parent = parent
        self.var = {}

    def find(self, name: str):
        cur = self
        while isinstance(cur, Scope):
            if name in cur.var:
                return cur.var[name]
            cur = cur.parent

    def set(self, name: str, val):
        cur = self
        while isinstance(cur, Scope):
            if name in cur.var:
                cur.var[name] = val
                return
            cur = cur.parent

    def define(self, name: str, val):
        self.var[name] = val


class Func:
    def __init__(self, params: list, code: list, closure: Scope, jmptags: dict):
        self.code = code
        self.params = params
        self.closure = closure
        self.jmptags = jmptags


class Method:
    def __init__(self, obj: dict, func):
        self.obj, self.func = obj, func


def build_jmptags(code: list):
    tags = {}
    for i in range(len(code)):
        if code[i][0] == 'label':
            tags[code[i][1]] = i
    return tags


def compile(tokens: list):
    pos = 0
    token: str = tokens[0]
    code = []
    if_cnt = 0
    while_cnt = 0
    scope_cnt = 0
    while_st = []

    def eat(expect=None):
        nonlocal pos, token
        if expect is None or token == expect:
            pos += 1
            token = tokens[pos]
            return tokens[pos - 1]
        raise Error(f"Unexpected token '{token}', expect '{expect}'.")

    def eat_id():
        if token == '':
            raise Error("Unexpected EOF.")
        elif token[0].isalpha() or token[0] == '_':
            return eat()
        else:
            raise Error(f"Expected an identifier, got '{token}'.")

    def factor():
        nonlocal code, scope_cnt
        if token == '':
            raise Error("Unexpected EOF.")
        elif token[0].isalpha() or token[0] == '_':
            code.append(('load-var', eat()))
        elif token[0].isdigit():
            if '.' in token:
                code.append(('load-const', float(eat())))
            else:
                code.append(('load-const', int(eat())))
        elif token[0] == '"':
            code.append(('load-const', eat()[1: -1]))
        elif token[0] == '(':
            eat()
            expr()
            eat(')')
        elif token == '*True':
            eat()
            code.append(('load-const', True))
        elif token == '*False':
            eat()
            code.append(('load-const', False))
        elif token == '*None':
            eat()
            code.append(('load-const', None))
        elif token in '+-!~':
            op = eat()
            factor()
            code.append(('op-unary', op))
        elif token == '[':
            eat()
            item_cnt = 0
            if token != ']':
                expr()
                item_cnt += 1
                while token == ',':
                    eat()
                    expr()
                    item_cnt += 1
            eat(']')
            code.append(('build-list', item_cnt))
        elif token == '*object':
            eat()
            eat('{')
            keys = []
            while token != '}':
                keys.append(eat_id())
                eat(':')
                expr()
                if token != '}':
                    eat(',')
            eat('}')
            code.append(('build-obj', keys))
        elif token == '*func':
            eat()
            eat('(')
            params = []
            if token != ')':
                params.append(eat_id())
                while token == ',':
                    eat()
                    params.append(eat_id())
            eat(')')
            old_code = code
            code = []
            old_scope_cnt = scope_cnt
            scope_cnt = 0
            block()
            scope_cnt = old_scope_cnt
            if code[-1][0] != 'ret':
                code.append(('load-const', None))
                code.append(('ret',))
            old_code.append(('build-func', params, code, build_jmptags(code)))
            code = old_code
        else:
            raise Error(token)
        while token in ('(', '[', '.'):
            if token == '(':
                eat()
                arg_cnt = 0
                if token != ')':
                    expr()
                    arg_cnt += 1
                    while token == ',':
                        eat()
                        expr()
                        arg_cnt += 1
                eat(')')
                code.append(('call', arg_cnt))
            elif token == '[':
                eat()
                expr()
                eat(']')
                code.append(('op-index',))
            elif token == '.':
                eat()
                code.append(('load-attr', eat_id()))

    def expr():
        stack = []
        factor()
        while token in prio:
            while stack and stack[-1] in prio and prio[stack[-1]] >= prio[token]:
                code.append(('op-binary', stack.pop()))
            stack.append(token)
            eat()
            factor()
        while stack:
            code.append(('op-binary', stack.pop()))

    def block():
        eat('{')
        while token != '}':
            stmt()
        eat('}')

    def stmt():
        nonlocal code, if_cnt, scope_cnt, while_cnt
        if token == ';':
            eat()
        elif token == '*var':
            eat()
            name = eat_id()
            if token == '=':
                eat()
                expr()
            else:
                code.append(('load-const', None))
            code.append(('def-var', name))
            while token == ',':
                eat()
                name = eat_id()
                if token == '=':
                    eat()
                    expr()
                else:
                    code.append(('load-const', None))
                code.append(('def-var', name))
            eat(';')
        elif token == '*func' and tokens[pos + 1] != '(':
            eat()
            name = eat_id()
            eat('(')
            params = []
            if token != ')':
                params.append(eat_id())
                while token == ',':
                    eat()
                    params.append(eat_id())
            eat(')')
            old_code = code
            code = []
            old_scope_cnt = scope_cnt
            scope_cnt = 0
            block()
            scope_cnt = old_scope_cnt
            if code[-1][0] != 'ret':
                code.append(('load-const', None))
                code.append(('ret',))
            old_code.append(('def-func', name, params, code, build_jmptags(code)))
            code = old_code
        elif token == '*if':
            scope_cnt += 1
            cur_if = if_cnt
            eat()
            expr()
            code.append(('jnz', f'ifelse{if_cnt}'))
            # 改为函数作用域
            # code.append(('scope-enter',))
            block()
            # code.append(('scope-quit',))
            code.append(('jmp', f'ifend{cur_if}'))
            code.append(('label', f'ifelse{if_cnt}'))
            if_cnt += 1
            while token == '*else':
                eat()
                if token == '*if':
                    eat()
                    expr()
                    code.append(('jnz', f'ifelse{if_cnt}'))
                    # code.append(('scope-enter',))
                    block()
                    # code.append(('scope-quit',))
                    code.append(('jmp', f'ifend{cur_if}'))
                    code.append(('label', f'ifelse{if_cnt}'))
                    if_cnt += 1
                else:
                    block()
            code.append(('label', f'ifend{cur_if}'))
            scope_cnt -= 1
        elif token == '*while':
            eat()
            cur_while = while_cnt
            while_cnt += 1
            scope_cnt += 1
            while_st.append((cur_while, scope_cnt))
            code.append(('label', f'whilehead{cur_while}'))
            expr()
            code.append(('jnz', f'whileend{cur_while}'))
            # code.append(('scope-enter',))
            block()
            # code.append(('scope-quit',))
            code.append(('jmp', f'whilehead{cur_while}'))
            code.append(('label', f'whileend{cur_while}'))
            while_st.pop()
            scope_cnt -= 1
        elif token == '*return':
            eat()
            expr()
            # 整个当前作用域都直接销毁了，所以不用什么scope-quit
            code.append(('ret',))
            eat(';')
        elif token == '*break':
            eat()
            code.append(('jmp', f'whileend{while_st[-1][0]}'))
            eat(';')
        elif token == '*continue':
            eat()
            code.append(('jmp', f'whilehead{while_st[-1][0]}'))
            eat(';')
        else:
            expr()
            if token == '=':
                # 赋值的实现有点像c4
                eat()
                if code[-1][0] == 'op-index':
                    code.pop()
                    expr()
                    code.append(('set-index',))
                elif code[-1][0] == 'load-attr':
                    tmp = code.pop()
                    tmp = ('set-attr', tmp[1])
                    expr()
                    code.append(tmp)
                elif code[-1][0] == 'load-var':
                    tmp = code.pop()
                    tmp = ('set-var', tmp[1])
                    expr()
                    code.append(tmp)
                else:
                    raise Error(f"Expected an l-value.")
            else:
                code.append(('pop',))
            eat(';')

    while token != '':
        stmt()
    return code

# 码风一如既往地不怎么样啊、、、为什么不用match-case，要用一大堆if
def run(code: list):
    scope_stack = []
    scope = Scope(None)
    scope.var = {
        'print': lambda *a: print(*a, end="", flush=True, sep=''),
        'println': lambda *a: print(*a, sep=''),
        'readln': input,
        'ord': ord,
        'chr': chr,
        'readchar': lambda: sys.stdin.read(1),
        'len': len,
    }
    old_codes = []
    jmptags = build_jmptags(code)
    st = []
    pc = 0
    while pc < len(code):
        cur = code[pc]
        # print(cur, st)
        if cur[0] == 'load-const':
            st.append(deepcopy(cur[1]))
        elif cur[0] == 'load-var':
            st.append(scope.find(cur[1]))
        elif cur[0] == 'op-unary':
            st.append({
                '+': lambda a: +a,
                '-': lambda a: -a,
                '!': lambda a: not a,
                '~': lambda a: ~a,
            }[cur[1]](st.pop()))
        elif cur[0] == 'op-binary':
            b = st.pop()
            a = st.pop()
            st.append({
                '+': lambda a, b: a + b,
                '-': lambda a, b: a - b,
                '*': lambda a, b: a * b,
                '/': lambda a, b: a / b,
                '%': lambda a, b: a % b,
                '==': lambda a, b: a == b,
                '!=': lambda a, b: a != b,
                '>': lambda a, b: a > b,
                '<': lambda a, b: a < b,
                '>=': lambda a, b: a >= b,
                '<=': lambda a, b: a <= b,
                '>>': lambda a, b: a >> b,
                '<<': lambda a, b: a << b,
                '&': lambda a, b: a & b,
                '|': lambda a, b: a | b,
                '^': lambda a, b: a ^ b,
                '&&': lambda a, b: a and b,
                '||': lambda a, b: a or b,
            }[cur[1]](a, b))
        elif cur[0] == 'label':
            pass
        elif cur[0] == 'jmp':
            pc = jmptags[cur[1]]
        elif cur[0] == 'jz':
            if st.pop():
                pc = jmptags[cur[1]]
        elif cur[0] == 'jnz':
            if not st.pop():
                pc = jmptags[cur[1]]
        elif cur[0] == 'scope-enter':
            scope = Scope(scope)
        elif cur[0] == 'scope-quit':
            if len(cur) == 2:
                r = cur[1]
            else:
                r = 1
            for _ in range(r):
                if isinstance(scope.parent, Scope):
                    scope = scope.parent
                else:
                    raise Error()
        elif cur[0] == 'build-list':
            lst = st[-cur[1]:]
            st = st[:-cur[1]]
            st.append(lst)
        elif cur[0] == 'build-obj':
            cnt = len(cur[1])
            v = st[-cnt:]
            st = st[:-cnt]
            st.append(dict(zip(cur[1], v)))
        elif cur[0] == 'build-func':
            st.append(Func(cur[1], cur[2], scope, cur[3]))
        elif cur[0] == 'op-index':
            b = st.pop()
            a = st.pop()
            st.append(a[b])
        elif cur[0] == 'load-attr':
            attr = st[-1][cur[1]]
            if isinstance(attr, Func) or callable(attr):
                attr = Method(st[-1], attr)
            st[-1] = attr
        elif cur[0] == 'call':
            args = copy(st[-cur[1]:])
            func = st[-cur[1] - 1]
            st = st[:-cur[1] - 1]
            # print(func, args, st)
            if isinstance(func, Method):
                args = [func.obj] + args
                func = func.func
            if isinstance(func, Func):
                if pc + 1 < len(code) and code[pc + 1][0] == 'ret':
                    scope_stack.pop()
                scope_stack.append(scope)
                scope = Scope(func.closure)
                scope.var = dict(zip(func.params, args))
                old_codes.append((code, pc, jmptags))
                code = func.code
                jmptags = func.jmptags
                pc = 0
                continue
            elif callable(func):
                st.append(func(*args))
            else:
                raise Error(func, args, st)
            # print(st)
        elif cur[0] == 'ret':
            scope = scope_stack.pop()
            code, pc, jmptags = old_codes.pop()
        elif cur[0] == 'def-var':
            scope.define(cur[1], st.pop())
        elif cur[0] == 'set-index':
            v = st.pop()
            b = st.pop()
            a = st.pop()
            a[b] = v
        elif cur[0] == 'set-attr':
            v = st.pop()
            a = st.pop()
            a[cur[1]] = v
        elif cur[0] == 'set-var':
            scope.set(cur[1], st.pop())
        elif cur[0] == 'pop':
            st.pop()
        elif cur[0] == 'def-func':
            scope.define(cur[1], Func(cur[2], cur[3], scope, cur[4]))
        else:
            raise Error(f"Unsupported bytecode '{cur}'.")
        pc += 1


code = '''
var res = 1, i = 1;
while i <= 100000 {
    res = res * i;
    i = i + 1;
}
# println(res);
'''
tokens = lex(code)
# print(tokens)
code = compile(tokens)
print(*code, sep='\n')
t = time()
run(code)
print(time() - t)

t = time()
res, i = 1, 1
while i <= 100000:
    res = res * i
    i = i + 1
# print(res)
print(time() - t)

"""
func fac(num) {
    # println("fac ", num);
    if (num == 0) { return 1; }
    else { return num * fac(num - 1); }
}
fac(100);

var l = [1, 2, [2, 4, 5]];
println(l);
l[2][0] = 3;
println(l);

var res = 1, i = 1;
while i <= 10 {
    res = res * i;
    i = i + 1;
}
# println(res);

func Counter(start) {
    func next() {
        start = start + 1;
        return start;
    }
    return next;
}
var counter = Counter(0);
var i = counter();
while i <= 10 {
    println(i);
    i = counter();
}

var i = 0;
while True {
    i = i + 1;
    if (i == 5) { continue; }
    if (i == 10) { break; }
    println(i);
}

var a = object {
    a: 10,
};
println(a, " ", a.a);
a.a = 20;
println(a, " ", a.a);

println(func(a) { return a + 1; }(1));

var a = object {
    a: 10,
    getA: func(self) { return self.a; },
    setA: func(self, a) { self.a = a; }
};
println(a.getA());
println(a.setA(20));
println(a.a);
"""
