from copy import copy
import sys
from time import time

def py_test():
    print("Python:")
    t = time()
    res, i = 1, 1
    while i <= 100000:
        res *= i
        i += 1
    # print(res)
    print(time() - t)

class SFException(Exception): ...
class SFSyntaxError(SFException): ...
class SFNameError(SFException): ...
class SFTypeError(SFException): ...

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
    'func', 'var',
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

def tokenize(code: str):
    res = []
    pos = 0
    length = len(code)

    while pos < length:
        while pos < length and code[pos] in ' \n\t#':
            if code[pos] == '#':
                while pos < length and code[pos] != '\n':
                    pos += 1
            else:
                pos += 1
        
        if pos >= length:
            break
        elif code[pos].isdigit():
            num = ""
            while pos < length and (code[pos].isdigit() or code[pos] == '.'):
                num += code[pos]
                pos += 1
            res.append(num)
        elif code[pos].isalpha() or code[pos] == '_':
            ident = ""
            while pos < length and (code[pos].isalnum() or code[pos] == '_'):
                ident += code[pos]
                pos += 1
            if ident in keywords:
                res.append('*' + ident)
            else:
                res.append(ident)
        elif code[pos] in '"\'':
            x = code[pos]
            s = '"'
            pos += 1
            while pos < length and code[pos] != x:
                if code[pos] == '\\':
                    pos += 1
                    if pos >= length:
                        raise SFSyntaxError("Unexpected EOF in string.")
                    elif code[pos] in escapes:
                        s += escapes[code[pos]]
                        pos += 1
                    elif code[pos] == 'x':
                        pos += 1
                        if pos + 2 >= length:
                            raise SFSyntaxError("Unexpected EOF in string.")
                        s += chr(int(code[pos: pos+2], 16))
                        pos += 2
                    elif code[pos] == 'u':
                        pos += 1
                        if pos + 4 >= length:
                            raise SFSyntaxError("Unexpected EOF in string.")
                        s += chr(int(code[pos: pos+4], 16))
                        pos += 4
                    else:
                        raise SFSyntaxError("Unknown escape sequence.")
                else:
                    s += code[pos]
                    pos += 1
            if pos >= length:
                raise SFSyntaxError("Unexpected EOF in string.")
            s += '"'
            pos += 1
            res.append(s)
        elif code[pos: pos+2] in operators:
            res.append(code[pos: pos+2])
            pos += 2
        elif code[pos] in operators:
            res.append(code[pos])
            pos += 1
        else:
            raise SFSyntaxError(f"Unexpected character '{code[pos]}'.")

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
        raise SFNameError(f"Undefined variable '{name}'.")

    def set(self, name: str, val):
        cur = self
        while isinstance(cur, Scope):
            if name in cur.var:
                cur.var[name] = val
                return
            cur = cur.parent
        raise SFNameError(f"Undefined variable '{name}'.")

    def define(self, name: str, val):
        self.var[name] = val

def compile(tokens: list):
    pos = 0
    token: str = tokens[0]

    output = []
    whilestack = []

    def eat(expect=None):
        nonlocal pos, token
        if expect is None or token == expect:
            pos += 1
            token = tokens[pos]
            return tokens[pos-1]
        raise SFSyntaxError(f"Unexpected token '{token}', expect '{expect}'.")

    def eat_id():
        if token == '':
            raise SFSyntaxError("Unexpected EOF, expect an identifier.")
        if token[0].isalpha() or token[0] == '_':
            return eat()
        raise SFSyntaxError(f"Unexpected token '{token}', expect an identifier.")

    def factor():
        if token == '':
            raise SFSyntaxError("Unexpected EOF.")
        elif token[0].isdigit():
            if '.' in token:
                output.append(('push', float(eat())))
            else:
                output.append(('push', int(eat())))
        elif token[0].isalpha() or token[0] == '_':
            output.append(('loadvar', eat()))
        elif token[0] == '"':
            output.append(('push', eat()[1: -1]))
        elif token[0] == '(':
            eat()
            expr()
            eat(')')
        elif token[0] == '[':
            cnt = 0
            eat()
            if token != ']':
                cnt += 1
                expr()
                while token == ',':
                    eat()
                    cnt += 1
                    expr()
            eat(']')
            output.append(('buildlist', cnt))
        elif token in '+-!~':
            op = eat()
            factor()
            output.append(('unaryop', op))
        elif token[0] == '{':
            attrs = []
            eat()
            while token != '}':
                attrs.append(eat_id())
                eat(':')
                expr()
                if token != '}':
                    eat(',')
            eat('}')
            output.append(('obj', attrs))
        elif token == '*func':
            eat()
            func_head = len(output)
            output.append(None)
            eat('(')
            params = []
            if token != ')':
                params.append(eat_id())
                while token == ',':
                    eat()
                    params.append(eat_id())
            eat(')')
            block()
            if output[-1][0] != 'ret':
                output.append(('push', None))
                output.append(('ret',))
            output[func_head] = 'jmp', len(output)
            output.append(('func', func_head + 1, params))
        elif token == '*True':
            eat()
            output.append(('push', True))
        elif token == '*False':
            eat()
            output.append(('push', False))
        elif token == '*None':
            eat()
            output.append(('push', None))
        else:
            raise SFSyntaxError(f"Unexpected token '{token}'.")

        while token in ('.', '(', '['):
            if token == '.':
                eat()
                output.append(('loadattr', eat_id()))
            elif token == '(':
                eat()
                arg_cnt = 0
                if token != ')':
                    arg_cnt += 1
                    expr()
                    while token == ',':
                        eat()
                        arg_cnt += 1
                        expr()
                eat(')')
                output.append(('call', arg_cnt))
            elif token == '[':
                eat()
                expr()
                eat(']')
                output.append(('index',))

    def block():
        eat('{')
        while token != '}':
            stmt()
        eat('}')

    def expr():
        st = []
        factor()
        while token in prio:
            op = eat()
            while st and st[-1] in prio and prio[st[-1]] >= prio[token]:
                output.append(('binop', st.pop()))
            st.append(op)
            factor()
        while st:
            output.append(('binop', st.pop()))

    def stmt():
        if token == ';':
            eat()
        elif token == '*var':
            eat()
            name = eat_id()
            if token == '=':
                eat()
                expr()
            else:
                output.append(('push', None))
            output.append(('defvar', name))
            while token == ',':
                eat()
                name = eat_id()
                if token == '=':
                    eat()
                    expr()
                else:
                    output.append(('push', None))
                output.append(('defvar', name))
            eat(';')
        elif token == '*if':
            eat()
            expr()
            jnz_pos = len(output)
            output.append(None)
            block()
            jmp_pos = [len(output)]
            output.append(None)
            output[jnz_pos] = 'jnz', len(output)
            while token == '*else':
                eat()
                if token == '*if':
                    eat()
                    expr()
                    jnz_pos = len(output)
                    output.append(None)
                    block()
                    jmp_pos.append(len(output))
                    output.append(None)
                    output[jnz_pos] = 'jnz', len(output)
                else:
                    block()
            for i in jmp_pos:
                output[i] = 'jmp', len(output)
        elif token == '*while':
            eat()
            whilehead = len(output)
            whilestack.append((whilehead, []))
            expr()
            toend = len(output)
            output.append(None)
            block()
            output.append(('jmp', whilehead))
            jnz_list = whilestack.pop()[1]
            output[toend] = 'jnz', len(output)
            for i in jnz_list:
                output[i] = 'jmp', len(output)
        elif token == '*func' and tokens[pos+1] != '(':
            eat()
            name = eat_id()
            func_head = len(output)
            output.append(None)
            eat('(')
            params = []
            if token != ')':
                params.append(eat_id())
                while token == ',':
                    eat()
                    params.append(eat_id())
            eat(')')
            block()
            if output[-1][0] != 'ret':
                output.append(('push', None))
                output.append(('ret',))
            output[func_head] = 'jmp', len(output)
            output.append(('func', func_head + 1, params))
            output.append(('defvar', name))
        elif token == '*return':
            eat()
            expr()
            output.append(('ret',))
            eat(';')
        elif token == '*break':
            eat()
            whilestack[-1][1].append(len(output))
            output.append(None)
            eat(';')
        elif token == '*continue':
            eat()
            output.append(('jmp', whilestack[-1][0]))
            eat(';')
        else:
            expr()
            if token == '=':
                eat()
                if output[-1][0] == 'loadvar':
                    varname = output[-1][1]
                    output.pop()
                    expr()
                    output.append(('setvar', varname))
                elif output[-1][0] == 'loadattr':
                    attrname = output[-1][1]
                    output.pop()
                    expr()
                    output.append(('setattr', attrname))
                elif output[-1][0] == 'index':
                    output.pop()
                    expr()
                    output.append(('setindex',))
                else:
                    raise SFSyntaxError("Expect an l-value.")
            else:
                output.append(('pop',))
            eat(';')

    while token != '':
        stmt()
    return output

class Func:
    def __init__(self, params: list, pos: int, closure: Scope):
        self.params, self.pos, self.closure = params, pos, closure

class Method:
    def __init__(self, base: dict, func):
        self.base, self.func = base, func

def run(code: list):
    scope = Scope(None)
    pc_stack = []
    scope_stack = []
    scope.var = {
        'print': lambda *a: print(*a, end="", flush=True, sep=''),
        'println': lambda *a: print(*a, sep=''),
        'readln': input,
        'ord': ord,
        'chr': chr,
        'readchar': lambda: sys.stdin.read(1),
        'len': len,
    }
    pc = 0
    stack = []

    while pc < len(code):
        cmd = code[pc]
        # print(pc, cmd, stack)
        if cmd[0] == 'push':
            stack.append(copy(cmd[1]))
        elif cmd[0] == 'pop':
            stack.pop()
        elif cmd[0] == 'setvar':
            scope.set(cmd[1], stack.pop())
        elif cmd[0] == 'binop':
            b = stack.pop()
            stack[-1] = {
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
            }[cmd[1]](stack[-1], b)
        elif cmd[0] == 'unaryop':
            stack[-1] = {
                '+': lambda a: +a,
                '-': lambda a: -a,
                '!': lambda a: not a,
                '~': lambda a: ~a,
            }[cmd[1]](stack[-1])
        elif cmd[0] == 'loadvar':
            stack.append(scope.find(cmd[1]))
        elif cmd[0] == 'buildlist':
            res = stack[-cmd[1]:]
            stack = stack[:-cmd[1]]
            stack.append(res)
        elif cmd[0] == 'obj':
            if len(cmd[1]):
                res = dict(zip(cmd[1], stack[-len(cmd[1]):]))
                stack = stack[:-len(cmd[1])]
            else:
                res = {}
            stack.append(res)
        elif cmd[0] == 'func':
            stack.append(Func(cmd[2], cmd[1], scope))
        elif cmd[0] == 'loadattr':
            base = stack.pop()
            attr = base[cmd[1]]
            if callable(attr) or isinstance(attr, Func):
                stack.append(Method(base, attr))
            else:
                stack.append(attr)
        elif cmd[0] == 'call':
            if cmd[1]:
                args = stack[-cmd[1]:]
                stack = stack[:-cmd[1]]
            else:
                args = []
            func = stack.pop()
            if isinstance(func, Method):
                args = [func.base] + args
                func = func.func
            if isinstance(func, Func):
                scope_stack.append(scope)
                scope = Scope(func.closure)
                scope.var = dict(zip(func.params, args))
                pc_stack.append(pc)
                pc = func.pos - 1
            elif callable(func):
                stack.append(func(*args))
            else:
                raise SFTypeError("Expect a function.")
        elif cmd[0] == 'index':
            index = stack.pop()
            base = stack.pop()
            stack.append(base[index])
        elif cmd[0] == 'defvar':
            scope.define(cmd[1], stack.pop())
        elif cmd[0] == 'setattr':
            val = stack.pop()
            base = stack.pop()
            base[cmd[1]] = val
        elif cmd[0] == 'setindex':
            val = stack.pop()
            index = stack.pop()
            base = stack.pop()
            base[index] = val
        elif cmd[0] == 'jmp':
            pc = cmd[1] - 1
        elif cmd[0] == 'jz':
            if stack.pop():
                pc = cmd[1] - 1
        elif cmd[0] == 'jnz':
            if not stack.pop():
                pc = cmd[1] - 1
        elif cmd[0] == 'ret':
            scope = scope_stack.pop()
            pc = pc_stack.pop()
        else:
            raise SFException(cmd)
        pc += 1

def test(code: str):
    tokens = tokenize(code)
    output = compile(tokens)
    print(output)
    t = time()
    run(output)
    print(time() - t)

# py_test()
print("SuperFast:")
test('''
var res = 1, i = 1;
while i <= 100000 {
    res = res * i;
    i = i + 1;
}
# println(res);
''')

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

var a = {
    a: 10,
};
println(a, " ", a.a);
a.a = 20;
println(a, " ", a.a);

println(func(a) { return a + 1; }(1));

var a = {
    a: 10,
    getA: func(self) { return self.a; },
    setA: func(self, a) { self.a = a; }
};
println(a.getA());
println(a.setA(20));
println(a.a);

var i = 0;
while i < 100000 { i = i + 1; }
println(i);
"""
