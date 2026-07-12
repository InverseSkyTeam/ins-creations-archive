'''
def const fac a =
    if (a == 0) 1
    else fac (a - 1) * a;

def main argv = {
    defvar num = input 'int';
    output ['answer = ', fac num];
    defvar a = input 'int', b = input 'int';
    output ['a + b = ', a + b];
};
'''
import time
escape = {
    'r': '\r',
    't': '\t',
    'a': "\a",
    'f': '\f',
    'v': "\v",
    'b': "\b",
    'n': "\n",
    '"': '"',
    "'": "'",
    '\\': '\\',
}
keywords = (
    'def', 'defvar', 'do', 'const', 'if', 'else',
    'True', 'False', 'None',
)
prio = {
    '*': 100, '/': 100, '%': 100,
    '+': 99, '-': 99,
    '<<': 98, '>>': 98,
    '==': 97, '!=': 97,
    '>': 96, '<': 96, '>=': 96, '<=': 96,
    '&': 95, '^': 94, '|': 93,
    '&&': 92, '||': 91,
}
operators = [
    '+', '-', '*', '/', '%',
    '==', '!=', '<=', '>=', '<', '>',
    '>>', '<<',
    '&&', '||', '&', '|', '^',
    '!', '~',
    '(', ')', '[', ']', '{', '}',
    ';', ':', ',', '=',
]


class pf_istream:
    def __init__(self):
        self.buffer = ""

    def fill_buffer(self):
        if self.buffer == "":
            self.buffer = input() + "\n"

    def readstr(self):
        while self.buffer != "" and self.buffer[0] in " \n\t":
            self.buffer = self.buffer[1:]
        self.fill_buffer()
        s = ""
        while self.buffer != "" and self.buffer[0] not in " \n\t":
            s += self.buffer[0]
            self.buffer = self.buffer[1:]
        if s == "":
            return self.readstr()
        return s
    
    def readint(self):
        return int(self.readstr())
    
    def read_float(self):
        return float(self.readstr())
    
    def readline(self):
        self.fill_buffer()
        ret = self.buffer[: -1]
        self.buffer = ""
        return ret
    
    def readchar(self):
        self.fill_buffer()
        ret = self.buffer[0]
        self.buffer = self.buffer[1:]
        return ret


pfin = pf_istream()


class Function:
    def __init__(self, expr, argument, memory, is_const, closure):
        self.expr, self.argument, self.memory, self.is_const, self.closure = expr, argument, memory, is_const, closure


class Scope:
    def __init__(self, parent, var, function={}):
        self.parent, self.var, self.function = parent, var, function

    def find(self, name):
        if name in self.var:
            return self.var[name]
        if self.parent is not None:
            return self.parent.find(name)
        raise Exception()

    def findfunction(self, name):
        if name in self.function:
            return self.function[name]
        if self.parent is not None:
            return self.parent.findfunction(name)
        raise Exception()

    def define(self, name, value):
        self.var[name] = value

    def deffunction(self, name, value):
        self.function[name] = value


class ExprStmt:
    def __init__(self, expr):
        self.expr = expr

    def run(self, scope):
        self.expr.run(scope)


class NoOp:
    ...


class Def:
    def __init__(self, name, argument, expr, is_const):
        self.name, self.argument, self.expr, self.is_const = name, argument, expr, is_const

    def run(self, scope):
        scope.deffunction(self.name, Function(self.expr, self.argument, {}, self.is_const, scope))


class DefVar:
    def __init__(self, names, values):
        self.names, self.values = names, values

    def run(self, scope):
        for i in range(len(self.names)):
            scope.define(self.names[i], self.values[i].run(scope))


class Const:
    def __init__(self, value):
        self.value = value

    def run(self, scope):
        return self.value


class Var:
    def __init__(self, name):
        self.name = name

    def run(self, scope):
        return scope.find(self.name)


class Binary:
    def __init__(self, op, left, right):
        self.op, self.left, self.right = op, left, right

    def run(self, scope):
        return {
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
            '<<': lambda a, b: a << b,
            '>>': lambda a, b: a >> b,
            '&&': lambda a, b: a and b,
            '||': lambda a, b: a or b,
            '&': lambda a, b: a & b,
            '|': lambda a, b: a | b,
            '^': lambda a, b: a ^ b,
        }[self.op](self.left.run(scope), self.right.run(scope))


class Unary:
    def __init__(self, op, value):
        self.op, self.value = op, value

    def run(self, scope):
        return {
            '+': lambda a: +a,
            '-': lambda a: -a,
            '!': lambda a: not a,
            '~': lambda a: ~a,
        }[self.op](self.value.run(scope))


class Call:
    def __init__(self, function, argument):
        self.function, self.argument = function, argument

    def run(self, scope):
        function = scope.findfunction(self.function)
        argument = self.argument.run(scope)
        if callable(function):
            return function(argument)
        if function.is_const:
            try:
                return function.memory[argument]
            except:
                ...
        res = function.expr.run(
            Scope(function.closure, {function.argument: argument}))
        if function.is_const:
            try:
                function.memory[argument] = res
            except TypeError:
                ...
        return res


class Index:
    def __init__(self, left, right):
        self.left, self.right = left, right

    def run(self, scope):
        return self.left.run(scope)[self.right.run(scope)]


class NewList:
    def __init__(self, items):
        self.items = items

    def run(self, scope):
        return [i.run(scope) for i in self.items]


class DoExpr:
    def __init__(self, stmts, ret):
        self.stmts, self.ret = stmts, ret

    def run(self, scope):
        new_scope = Scope(scope, {})
        for i in self.stmts:
            i.run(new_scope)
        return self.ret.run(new_scope)
    

class IfElseExpr:
    def __init__(self, cond, true, false):
        self.cond, self.true, self.false = cond, true, false

    def run(self, scope):
        if self.cond.run(scope):
            ret = self.true.run(scope)
        else:
            ret = self.false.run(scope)
        return ret


def tokenize(code):
    p = 0
    res = []
    while p < len(code):
        while p < len(code) and code[p] in " \n\t#":
            if code[p] == '#':
                while p < len(code) and code[p] != '\n':
                    p += 1
            else:
                p += 1
        if p == len(code):
            break
        elif code[p].isdigit():
            s = ""
            while p < len(code) and (code[p].isdigit() or code[p] == '.'):
                s += code[p]
                p += 1
            res.append(s)
        elif code[p].isalpha():
            s = ""
            while p < len(code) and (code[p].isalnum() or code[p] == '_'):
                s += code[p]
                p += 1
            if s in keywords:
                res.append("*" + s)
            else:
                res.append(s)
        elif code[p] == '"' or code[p] == "'":
            x = code[p]
            s = '"'
            p += 1
            while p < len(code) and code[p] != x:
                if code[p] == '\\':
                    p += 1
                    if p == len(code):
                        raise Exception()
                    if code[p].isdigit():
                        if p + 3 >= len(code):
                            raise Exception()
                        s += chr(int(code[p: p+3], 8))
                        p += 3
                    elif code[p] in escape:
                        s += escape[code[p]]
                        p += 1
                    else:
                        raise Exception()
                else:
                    s += code[p]
                    p += 1
            if p == len(code):
                raise Exception()
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
            raise Exception(code[p:])
    return res + [""]


def parse(tokens, _functions):
    _pos = 0
    token = tokens[_pos]
    functions = [_functions]

    def eat(expect=None):
        nonlocal _pos, token
        if token == expect or expect is None:
            _pos += 1
            token = tokens[_pos]
            return tokens[_pos-1]
        raise Exception(tokens[_pos:])

    def do_block():
        nonlocal _pos, token
        eat('{')
        functions.append([])
        stmts = []
        ret = Const(None)
        while token != '}':
            pos = _pos
            stmts.append(stmt())
            if token == '}':
                _pos = pos
                token = tokens[_pos]
                ret = expr()
                break
            else:
                eat(';')
        eat('}')
        functions.pop()
        return DoExpr(stmts, ret)

    def stmt():
        if token == ';':
            return NoOp()
        elif token == '*def':
            eat()
            if token == '*const':
                eat()
                is_const = True
            else:
                is_const = False
            name = eat_id()
            functions[-1].append(name)
            argument = eat_id()
            eat('=')
            e = expr()
            return Def(name, argument, e, is_const)
        elif token == '*defvar':
            eat()
            names = [eat_id()]
            eat('=')
            values = [expr()]
            while token == ',':
                eat()
                names.append(eat_id())
                eat('=')
                values.append(expr())
            return DefVar(names, values)
        return ExprStmt(expr())

    def expr():
        if token == '*if':
            eat()
            cond = factor()
            true = expr()
            eat('*else')
            false = expr()
            return IfElseExpr(cond, true, false)
        res = factor()
        if token in prio:
            res = Binary(eat(), res, factor())
            while token in prio:
                op = eat()
                if prio[op] <= prio[res.op]:
                    res = Binary(op, res, factor())
                else:
                    res = Binary(res.op, res.left, Binary(
                        op, res.right, factor()))
        return res

    def factor():
        if token == "":
            raise Exception()
        elif token[0].isdigit():
            if '.' in token:
                res = Const(float(eat()))
            else:
                res = Const(int(eat()))
        elif token[0].isalpha() or token[0] == '_':
            for i in reversed(functions):
                if token in i:
                    function = eat()
                    argument = factor()
                    res = Call(function, argument)
                    break
            else:
                res = Var(eat())
        elif token[0] == '"':
            res = Const(eat()[1:-1])
        elif token == '*True':
            eat()
            res = Const(True)
        elif token == '*False':
            eat()
            res = Const(False)
        elif token == '*None':
            eat()
            res = Const(None)
        elif token == '(':
            eat()
            res = expr()
            eat(')')
        elif token == '[':
            eat()
            items = []
            if token != ']':
                items.append(expr())
                while token == ',':
                    eat()
                    items.append(expr())
            eat(']')
            res = NewList(items)
        elif token == '{':
            res = do_block()
        elif token in ('+', '-', '!', '~'):
            op = eat()
            res = Unary(op, factor())
        else:
            raise Exception(token, tokens[_pos:])
        while token in ('['):
            if token == '[':
                eat()
                res = Index(res, expr())
                eat(']')
        return res

    def eat_id() -> str:
        if token == "":
            raise Exception()
        if token[0].isalpha() or token[0] == '_':
            return eat()
        raise Exception(token)

    stmts = []
    while token != "":
        stmts.append(stmt())
        eat(';')
    return stmts


def run_code(code, _scope, argv):
    scope = Scope(_scope, {})
    ast = parse(tokenize(code), list(_scope.function.keys()))
    for i in ast:
        i.run(scope)
    return Call("main", Const(argv)).run(scope)


def _output(args):
    print(*args, sep="", flush=True, end="")


def _input(tp):
    if tp == "int":
        return pfin.readint()
    elif tp == "float":
        return pfin.read_float()
    elif tp == "str":
        return pfin.readstr()
    elif tp == "line":
        return pfin.readline()
    elif tp == "char":
        return pfin.readchar()
    raise Exception(tp)


v = run_code('''
def const fac a =
    if (a == 0) 1
    else fac (a - 1) * a;

def main argv = {
    defvar num = input 'int';
    output ['answer = ', fac num, '\\n'];
    defvar a = input 'int', b = input 'int';
    output ['a + b = ', a + b, '\\n'];
};
''', Scope(None, {}, {
    "output": _output,
    "get_time": lambda a:time.time(),
    "input": _input,
}), [])
print("main函数返回值：", v)
'''
#记忆化递归真神！
#好消息：PF开记忆化只需要多打5个字母和2个空格（
#注意：有输入输出的函数千万不要开记忆化
#否则会出大问题
#下次更新内容：输入
def const fac n =
    if (n == 0) 1
    else fac (n - 1) * n;

def fib n = 
    if (n == 0) 0
    else if (n == 1) 1
    else fib (n - 2) + fib (n - 1);

def add1 num = {
    output ["num = ", num, "\\n"];
    num + 1
};

def const fast_fib n = 
    if (n == 0) 0
    else if (n == 1) 1
    else fast_fib (n - 2) + fast_fib (n - 1);

def main argv = {
    #你可能想不到，output是函数
    output ["PureFunctional0.0，一个函数式语言\\n下面进行速度测试，用递归的方法（反正也没有循环）来计算25的阶乘\\n比较记忆化和不记忆化的速度\\n"];
    defvar num = 25;
    defvar time1 = get_time None;
    output [fib num, "\\n"];
    output ["不记忆化：", get_time None - time1, "秒\\n"];
    defvar time2 = get_time None;
    output [fast_fib num, "\\n"];
    output ["记忆化：", get_time None - time2, "秒\\n"];
    #output [add1 10];
    #output [-1];
    0
};


#测试输入
def main argv = {
    defvar
        intv = input 'int',
        floatv = input 'float',
        strv = input 'str',
        linev = input 'line',
        charv = input 'char';
    output [
        intv, "\\n",
        floatv, "\\n",
        strv, "\\n",
        linev, "\\n",
        charv, "\\n"
    ];
    0
};


#A + B Problem
def main argv = {
    output ['请输入a和b：'];
    defvar a = input 'int', b = input 'int';
    output ['a + b = ', a + b, '\\n'];
    0
};
'''
