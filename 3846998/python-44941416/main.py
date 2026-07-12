from copy import deepcopy
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


class LispSym:
    def __init__(self, name: str):
        self.name = name

    __str__ = __repr__ = lambda self: f"'{self.name}"


class BuiltinMacro:
    def __init__(self, func):
        self.func = func


def newBuiltinMacro(func):
    return BuiltinMacro(func)


class Scope:
    def __init__(self, parent, var: dict):
        self.parent, self.var = parent, var

    def find(self, name: str):
        if name in self.var:
            return self.var[name]
        if isinstance(self.parent, Scope):
            return self.parent.find(name)
        raise Exception(name)

    def set(self, name: str, value):
        if name in self.var:
            self.var[name] = value
            return self.var[name]
        elif isinstance(self.parent, Scope):
            return self.parent.set(name, value)
        raise Exception(name)

    def define(self, name: str, value):
        self.var[name] = value

    def run_code(self, code: str):
        ast = []
        tokens = tokenize(code)
        while tokens[0] != "":
            ast.append(parse(tokens))
        for i in ast:
            self.run(i)

    def run_ast(self, ast: list):
        r = None
        for i in ast:
            r = self.run(i)
        return r

    def run(self, ast):
        if type(ast) == LispSym:
            return self.find(ast.name)
        elif type(ast) in (int, float, str):
            return ast
        elif type(ast) == NoQuote:
            raise Exception("Error!")
        elif type(ast) == Quote:
            res = []
            for i in ast.items:
                if type(i) == NoQuote:
                    res.append(self.run(i.ast))
                else:
                    res.append(i)
            return res
        elif type(ast) == list:
            func, *args = ast
            if type(func) == LispSym:
                func = func.name
                if func == "if":
                    if self.run(args[0]):
                        return Scope(self, {}).run(args[1])
                    return Scope(self, {}).run(args[2])
                elif func == "define":
                    self.define(args[0].name, self.run(args[1]))
                    return
                elif func == "lambda":
                    if len(args) == 1:
                        return lambda *a: None
                    return Function(list(map(lambda a: a.name, args[0])), args[1:], scope)
                elif func == "macro":
                    if len(args) == 1:
                        raise Exception("Error")
                    return Macro(Function(list(map(lambda a: a.name, args[0])), args[1:], scope))
                elif func == "quote":
                    return args[0]
                elif func == "set!":
                    self.set(args[0].name, self.run(args[1]))
                    return
                elif func == "begin":
                    if args == []:
                        return None
                    new_scope = Scope(self, {})
                    return [new_scope.run(i) for i in args][-1]
                func = LispSym(func)
            func = self.run(func)
            if type(func) == BuiltinMacro:
                return func.func(scope, *args)
            if type(func) == Macro:
                a = func.expand(*args)
                return self.run(a)
            args = [self.run(i) for i in args]
            return func(*args)
        else:
            raise Exception("Error!")


class Function:
    def __init__(self, para: list, body: list, closure: Scope):
        self.para, self.body, self.closure = para, body, closure

    def __call__(self, *args):
        return Scope(self.closure, dict(zip(self.para, args))).run_ast(self.body)


class Macro:
    def __init__(self, func: Function):
        self.expand = func
    

class Quote:
    def __init__(self, items):
        self.items = items

    __str__ = __repr__ = lambda self: "'" + str(self.items)
    

class NoQuote:
    def __init__(self, ast: list):
        self.ast = ast

    __str__ = __repr__ = lambda self: "," + str(self.ast)


def tokenize(lisp_code: str):
    res = []
    p = 0
    length = len(lisp_code)
    while p < length:
        while p < length and lisp_code[p] in " \n\t;":
            if lisp_code[p] == ';':
                while p < length and lisp_code[p] != '\n':
                    p += 1
            else:
                p += 1
        if p == length:
            break
        elif lisp_code[p] in '()\',':
            res.append(lisp_code[p])
            p += 1
        elif lisp_code[p] == '"':
            s = '"'
            p += 1
            while p < length and lisp_code[p] != '"' and lisp_code[p] != '\n':
                if lisp_code[p] == '\\':
                    p += 1
                    if p == length:
                        raise Exception("Error!")
                    elif lisp_code[p] in escape:
                        s += escape[lisp_code[p]]
                        p += 1
                    elif lisp_code[p].isdigit():
                        if p + 3 > length:
                            raise Exception("Error!")
                        s += chr(int(lisp_code[p: p+3], 8))
                        p += 3
                    else:
                        raise Exception("Error!")
                else:
                    s += lisp_code[p]
                    p += 1
            if p == length or lisp_code[p] != '"':
                raise Exception("Error!")
            p += 1
            s += '"'
            res.append(s)
        else:
            s = ""
            while lisp_code[p] not in " \n\t()":
                s += lisp_code[p]
                p += 1
            res.append(s)
    return res + [""]


def parse(tokens: list):
    if tokens[0] == "":
        raise Exception("Error!")
    elif tokens[0] == '(':
        tokens.pop(0)
        r = []
        while tokens[0] != ')':
            r.append(parse(tokens))
        tokens.pop(0)
        return r
    elif tokens[0][0].isdigit():
        if '.' in tokens[0]:
            return float(tokens.pop(0))
        else:
            return int(tokens.pop(0))
    elif tokens[0][0] == '"':
        return tokens.pop(0)[1: -1]
    elif tokens[0] == "'":
        tokens.pop(0)
        return Quote(parse(tokens))
    elif tokens[0] == ',':
        tokens.pop(0)
        return NoQuote(parse(tokens))
    else:
        return LispSym(tokens.pop(0))


def add(pre, *a):
    res = pre
    for i in a:
        res += i
    return res


def sub(pre, *a):
    if len(a) == 0:
        return -pre
    res = pre
    for i in a:
        res -= i
    return res


def mul(pre, *a):
    res = pre
    for i in a:
        res *= i
    return res


def div(pre, *a):
    res = pre
    for i in a:
        res /= i
    return res

def mod(pre, *a):
    res = pre
    for i in a:
        res %= i
    return res


def eq(pre, *a):
    for i in a:
        if not (pre == i):
            return False
    return True


def ne(pre, *a):
    for i in a:
        if not (pre != i):
            return False
    return True


def gt(pre, *a):
    for i in a:
        if not (pre > i):
            return False
    return True


def lt(pre, *a):
    for i in a:
        if not (pre < i):
            return False
    return True


def ge(pre, *a):
    for i in a:
        if not (pre >= i):
            return False
    return True


def le(pre, *a):
    for i in a:
        if not (pre <= i):
            return False
    return True


def lsh(pre, *a):
    res = pre
    for i in a:
        res <<= i
    return res


def rsh(pre, *a):
    res = pre
    for i in a:
        res >>= i
    return res


@newBuiltinMacro
def _and(scope: Scope, *args):
    for i in args:
        if not scope.run(i):
            return False
    return True


@newBuiltinMacro
def _or(scope: Scope, *args):
    for i in args:
        if scope.run(i):
            return True
    return False


def set_car_force(lst: list, v):
    lst[0] = v


def set_cdr_force(lst: list, cdr: list):
    lst[1:] = cdr


def set_nth_force(lst: list, n: int, v):
    lst[n] = v


@newBuiltinMacro
def _while(scope: Scope, cond, *body):
    body = list(body)
    r = None
    while scope.run(cond):
        r = Scope(scope, {}).run_ast(body)
    return r


scope = Scope(None, {
    "print": lambda *args: print(*args, sep="", end="", flush=True),
    "car": lambda arg: arg[0],
    "cdr": lambda arg: arg[1:],
    "set-car!": set_car_force,
    "set-cdr!": set_cdr_force,
    "nth": lambda a, n: a[n],
    "set-nth!": set_nth_force,
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "%": mod,
    "=": eq,
    "!=": ne,
    ">": gt,
    "<": lt,
    ">=": ge,
    "<=": le,
    "<<": lsh,
    ">>": rsh,
    "and": _and,
    "or": _or,
    "not": lambda a: not a,
    "expand": lambda macro, *args: macro.expand(*args),
    "while": _while,
})
scope.run_code('''
(define fac (lambda (a)
    (if a
        (* (fac (- a 1)) a)
        1)))

(define add (lambda (a b)
    (print a " " b "\\n")
    (+ a b)))

(define MACRO-GREET (macro (name)
    '(print "Hello, " ,name "!\\n")))

(print (fac 10) "\\n")
(print (add 1 2) "\\n")
(print '(1 2 ,(+ 1 2)) "\\n")
(print (expand MACRO-GREET "world") "\\n")
(MACRO-GREET "world")

(define lst '(1 2 2))
(set-nth! lst 2 3)
(print lst "\\n")

(define i 0)
(while (< i 10)
    (print i "\\n")
    (set! i (+ i 1)))
''')
