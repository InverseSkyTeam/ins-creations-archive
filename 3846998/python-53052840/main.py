import sys
import os
from typing import Any


class TLException(Exception):
    ...


class TLSyntaxError(TLException):
    ...


class TLTypeError(TLException):
    ...


class TLNameError(TLException):
    ...


escapes = {
    'r': '\r',
    't': '\t',
    'a': '\a',
    'f': '\f',
    'v': '\v',
    'b': '\b',
    'n': '\n',
    '\'': '\'',
    '"': '"',
    '\\': '\\',
}


def tokenize(code: str) -> list[str]:
    pos = 0
    res = []

    while pos < len(code):
        while pos < len(code) and code[pos] in ' \n\t;':
            if code[pos] == ';':
                while pos < len(code) and code[pos] != '\n':
                    pos += 1
            else:
                pos += 1
        if pos >= len(code):
            break
        elif code[pos] == '"':
            pos += 1
            s = '"'
            while pos < len(code) and code[pos] != '"':
                if code[pos] == '\\':
                    pos += 1
                    if pos >= len(code):
                        raise TLSyntaxError("Unexpected EOF.")
                    elif code[pos] in escapes:
                        s += escapes[code[pos]]
                        pos += 1
                    elif code[pos] == 'u':
                        pos += 1
                        if pos + 4 >= len(code):
                            raise TLSyntaxError("Unexpected EOF.")
                        s += chr(int(code[pos: pos+4], 16))
                        pos += 4
                    elif code[pos] == 'x':
                        pos += 1
                        if pos + 2 >= len(code):
                            raise TLSyntaxError("Unexpected EOF.")
                        s += chr(int(code[pos: pos+2], 16))
                        pos += 2
                    else:
                        raise TLSyntaxError("Unexpected escape sequence.")
                else:
                    s += code[pos]
                    pos += 1
            if pos >= len(code):
                raise TLSyntaxError("Unexpected EOF.")
            pos += 1
            s += '"'
            res.append(s)
        elif code[pos] in '()\',':
            res.append(code[pos])
            pos += 1
        elif code[pos].isdigit():
            num = ''
            while pos < len(code) and (code[pos].isdigit() or code[pos] == '.'):
                num += code[pos]
                pos += 1
            if code.count('.'):
                raise TLSyntaxError("Invalid number.")
            res.append(num)
        else:
            s = ""
            while pos < len(code) and code[pos] not in ' \n\t()\',";':
                s += code[pos]
                pos += 1
            res.append(s)
    return res + [""]


class Quote:
    def __init__(self, val):
        self.val = val

    __repr__ = __str__ = lambda self: f"'{self.val}"


class DeQuote:
    def __init__(self, val):
        self.val = val

    __repr__ = __str__ = lambda self: f",{self.val}"


class Symbol:
    def __init__(self, name: str):
        self.name = name

    __repr__ = __str__ = lambda self: f"'{self.name}"


def parse(tokens: list[str]):
    pos = 0

    def parse():
        nonlocal pos
        if tokens[pos] == '':
            raise TLSyntaxError("Unexpected EOF.")
        elif tokens[pos] == '(':
            pos += 1
            res = []
            while tokens[pos] != ')':
                res.append(parse())
            if tokens[pos] != ')':
                raise TLSyntaxError("Unexpected token: " + tokens[pos] + ".")
            pos += 1
            return res
        elif tokens[pos] == '\'':
            pos += 1
            return Quote(parse())
        elif tokens[pos] == ',':
            pos += 1
            return DeQuote(parse())
        elif tokens[pos][0] == '"':
            s = tokens[pos][1: -1]
            pos += 1
            return s
        elif tokens[pos][0].isdigit():
            num = tokens[pos]
            pos += 1
            if '.' in num:
                return float(num)
            else:
                return int(num)
        else:
            s = tokens[pos]
            pos += 1
            return Symbol(s)

    res = []
    while pos < len(tokens) and tokens[pos] != '':
        res.append(parse())
    return res


class Scope:
    def __init__(self, parent: "Scope | None", var: dict):
        self.parent, self.var = parent, var

    def find(self, name: str):
        if name in self.var:
            return self.var[name]
        elif self.parent:
            return self.parent.find(name)
        else:
            raise TLNameError(f"Undefined variable '{name}'.")

    def set(self, name: str, val):
        if name in self.var:
            self.var[name] = val
        elif self.parent:
            self.parent.set(name, val)
        else:
            raise TLNameError(f"Undefined variable '{name}'.")

    def define(self, name: str, val):
        self.var[name] = val

    def quote(self, code):
        if isinstance(code, list):
            return [self.quote(x) for x in code]
        elif isinstance(code, Symbol):
            return code
        elif isinstance(code, Quote):
            return [self.quote(x) for x in code.val]
        elif isinstance(code, DeQuote):
            return self.run(code)
        else:
            return code

    # nor - opt - rest
    def fill_args(self, params: list[tuple], args: list):
        arg_cnt = 0
        var = {}
        for i in range(len(params)):
            if params[i][0] == 'rest':
                var[params[i][1]] = args[arg_cnt:]
                break
            elif params[i][0] == 'opt':
                if arg_cnt < len(args):
                    var[params[i][1]] = args[arg_cnt]
                    arg_cnt += 1
                else:
                    var[params[i][1]] = params[i][2]
            elif params[i][0] == 'nor':
                if arg_cnt < len(args):
                    var[params[i][1]] = args[arg_cnt]
                    arg_cnt += 1
                else:
                    raise TLTypeError(f"Too few arguments.")
        return var

    def run(self, code) -> Any:
        if isinstance(code, list):
            if len(code) == 0:
                return None
            func = self.run(code[0])
            args = code[1:]
            if isinstance(func, Builtin):
                # print(func.func, args)
                return func.func(self, *args)
            if isinstance(func, Macro):
                new_scope = Scope(
                    func.closure, self.fill_args(func.params, args))
                res = None
                for i in func.body:
                    res = new_scope.run(i)
                return self.run(res)
            args = list(map(self.run, args))
            if isinstance(func, Func):
                new_scope = Scope(
                    func.closure, self.fill_args(func.params, args))
                # print(new_scope.var)
                res = None
                for i in func.body:
                    res = new_scope.run(i)
                return res
            if callable(func):
                return func(*args)
            # print(code)
            # print(func, args)
            raise TLTypeError(f"Invalid function call.")
        elif isinstance(code, Symbol):
            return self.find(code.name)
        elif isinstance(code, Quote):
            return self.quote(code.val)
        elif isinstance(code, DeQuote):
            return self.run(code.val)
        else:
            return code


class Func:
    def __init__(self, params: list[tuple], body, closure: Scope):
        self.params, self.body, self.closure = params, body, closure


class Macro:
    def __init__(self, params: list[tuple], body, closure: Scope):
        self.params, self.body, self.closure = params, body, closure


class Builtin:
    def __init__(self, func):
        self.func = func


def add_builtin(name: str):
    def fn(func):
        b = Builtin(func)
        scope.define(name, b)
        return b
    return fn


def add_func(name: str):
    def fn(func):
        scope.define(name, func)
        return func
    return fn


def add_vars(funcs: dict):
    for name, func in funcs.items():
        scope.var[name] = func


def parse_params(params):
    if not isinstance(params, list):
        raise TLTypeError("params.")
    fn_params = []
    for i in params:
        if isinstance(i, Symbol):
            fn_params.append(('nor', i.name))
            continue
        if not isinstance(i, list):
            raise TLTypeError(f"params.")
        if len(i) < 2 or not isinstance(i[1], Symbol):
            raise TLTypeError(f"params.")
        if i[0].name in ('rest', 'nor') and len(i) >= 2:
            fn_params.append((i[0].name, i[1].name))
        elif i[0].name == 'opt' and len(i) >= 3:
            fn_params.append((i[0].name, i[1].name, scope.run(i[2])))
        else:
            print(i)
            raise TLTypeError(f"params.")
    return fn_params


scope = Scope(None, {})


@add_builtin("begin")
def begin(scope: Scope, *args):
    new_scope = Scope(scope, {})
    v = None
    for i in args:
        v = new_scope.run(i)
    return v


@add_builtin("define")
def define(scope: Scope, name, *val):
    if isinstance(name, list):
        if len(name) == 0 or not isinstance(name[0], Symbol):
            raise TLTypeError(f"define.")
        n = name[0].name
        params = parse_params(name[1:])
        v = list(val)
        fv = Func(params, v, scope)
        scope.define(n, fv)
        return fv
    if not isinstance(name, Symbol) or len(val) == 0:
        raise TLTypeError(f"define.")
    v = scope.run(val[0])
    scope.define(name.name, v)
    return v


@add_builtin("lambda")
def lambda_(scope: Scope, params, *body):
    return Func(parse_params(params), list(body), scope)


@add_builtin("macro")
def macro(scope: Scope, params, *body):
    return Macro(parse_params(params), list(body), scope)


@add_builtin("if")
def if_(scope: Scope, cond, true, false):
    new_scope = Scope(scope, {})
    if scope.run(cond):
        return new_scope.run(true)
    else:
        return new_scope.run(false)


@add_builtin("set!")
def set_(scope: Scope, name, val):
    if not isinstance(name, Symbol):
        raise TLTypeError(f"set!.")
    v = scope.run(val)
    scope.set(name.name, v)
    return v


@add_builtin("and")
def and_(scope: Scope, *args):
    if len(args) == 0:
        raise TLTypeError(f"and.")
    for i in args:
        v = scope.run(i)
        if not v:
            return v
    return v


@add_builtin("or")
def or_(scope: Scope, *args):
    if len(args) == 0:
        raise TLTypeError(f"or.")
    for i in args:
        v = scope.run(i)
        if scope.run(i):
            return v
    return v


@add_builtin("while")
def while_(scope: Scope, cond, *body):
    new_scope = Scope(scope, {})
    v = None
    while scope.run(cond):
        for i in body:
            v = new_scope.run(i)
    return v


@add_func("+")
def add(*args):
    if len(args) == 0:
        raise TLTypeError(f"+.")
    v = args[0]
    for i in args[1:]:
        v += i
    return v


@add_func("-")
def sub(*args):
    if len(args) == 0:
        raise TLTypeError(f"-.")
    v = args[0]
    if len(args) == 1:
        return -v
    for i in args[1:]:
        v -= i
    return v


@add_func("*")
def mul(*args):
    if len(args) == 0:
        raise TLTypeError(f"*.")
    v = args[0]
    for i in args[1:]:
        v *= i
    return v


@add_func("/")
def div(*args):
    if len(args) == 0:
        raise TLTypeError(f"/.")
    if len(args) == 1:
        return 1 / args[0]
    v = args[0]
    for i in args[1:]:
        v /= i
    return v


@add_func("%")
def mod(*args):
    if len(args) <= 1:
        raise TLTypeError(f"%.")
    v = args[0]
    for i in args[1:]:
        v %= i
    return v


@add_builtin("=")
def eq(scope: Scope, *args):
    if len(args) == 0:
        raise TLTypeError(f"=")
    v = scope.run(args[0])
    for i in args[1:]:
        nxt = scope.run(i)
        if v != nxt:
            return False
        v = nxt
    return True


@add_builtin("!=")
def ne(scope: Scope, *args):
    if len(args) == 0:
        raise TLTypeError(f"!=")
    v = scope.run(args[0])
    for i in args[1:]:
        nxt = scope.run(i)
        if v == nxt:
            return False
        v = nxt
    return True


@add_builtin("<")
def lt(scope: Scope, *args):
    if len(args) == 0:
        raise TLTypeError(f"<")
    v = scope.run(args[0])
    for i in args[1:]:
        nxt = scope.run(i)
        if v >= nxt:
            return False
        v = nxt
    return True


@add_builtin(">")
def gt(scope: Scope, *args):
    if len(args) == 0:
        raise TLTypeError(f">")
    v = scope.run(args[0])
    for i in args[1:]:
        nxt = scope.run(i)
        if v <= nxt:
            return False
        v = nxt
    return True


@add_builtin("<=")
def le(scope: Scope, *args):
    if len(args) == 0:
        raise TLTypeError(f"<=")
    v = scope.run(args[0])
    for i in args[1:]:
        nxt = scope.run(i)
        if v > nxt:
            return False
        v = nxt
    return True


@add_builtin(">=")
def ge(scope: Scope, *args):
    if len(args) == 0:
        raise TLTypeError(f">=")
    v = scope.run(args[0])
    for i in args[1:]:
        nxt = scope.run(i)
        if v < nxt:
            return False
        v = nxt
    return True


@add_func("<<")
def lshift(*args):
    if len(args) == 0:
        raise TLTypeError(f"<<")
    v = args[0]
    for i in args[1:]:
        v <<= i
    return v


@add_func(">>")
def rshift(*args):
    if len(args) == 0:
        raise TLTypeError(f">>")
    v = args[0]
    for i in args[1:]:
        v >>= i
    return v


@add_func("&")
def band(*args):
    if len(args) == 0:
        raise TLTypeError(f"&")
    v = args[0]
    for i in args[1:]:
        v &= i
    return v


@add_func("|")
def bor(*args):
    if len(args) == 0:
        raise TLTypeError(f"|")
    v = args[0]
    for i in args[1:]:
        v |= i
    return v


@add_func("^")
def xor(*args):
    if len(args) == 0:
        raise TLTypeError(f"^")
    v = args[0]
    for i in args[1:]:
        v ^= i
    return v


@add_func("set-nth!")
def set_nth_f(base, index, val):
    base[index] = val


add_vars({
    "not": lambda x: not x,
    "~": lambda x: ~x,
    "True": True,
    "False": False,
    "None": None,
    "len": len,
    "chr": chr,
    "ord": ord,
    "nth": lambda base, index: base[index],
    "print": lambda *args: print(*args, end="", flush=True, sep=""),
    "println": lambda *args: print(*args, flush=True, sep=""),
    "inputln": input,
    "getchar": lambda: sys.stdin.read(1),
    "system": os.system,
})


code = '''

'''
tokens = tokenize(code)
ast = parse(tokens)
for i in ast:
    scope.run(i)

'''

(define hello (lambda (x) (println "Hello, " x "!")))
(define macro-hello (macro (x) '(println "Hello, " ,x "!")))
(hello "world")
(macro-hello "world")

(define (fac num)
    (if (< num 2)
        1
        (* num (fac (- num 1)))))
(println (fac 10))

(define i 0)
(while (< i 10)
    (set! i (+ i 1))
    (println i))

(define (print-vals (rest args))
    (print args)
    (define i 0)
    (while (< i (len args))
        (println (nth args i))
        (set! i (+ i 1))))

(print-vals 1 "Hello, " '(1 2 3))
'''
