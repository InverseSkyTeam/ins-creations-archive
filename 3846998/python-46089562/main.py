import collections
import sys
import typing

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
operators = [
    '+', '-', '*', '/', '%',
    '==', '!=', '>', '<', '>=', '<=',
    '<<', '>>', '&&', '||', '&', '|', '^',
    '!', '~',
    '(', ')', '[', ']', '{', '}', ',', '.', '=',
]
keywords = [
    'if', 'else', 'elif', 'while', 'for', 'in',
    'var', 'func', 'def', 'class', 'extends', 'module',
    'return', 'break', 'continue',
    'True', 'False', 'None',
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
RETURN, BREAK, CONTINUE = 0, 1, 2


class Error(Exception):
    ...


def tokenize(code: str) -> list[str]:
    p = 0
    res = []
    while p < len(code):
        while p < len(code) and \
                (code[p] in " \n\t" or code[p: p + 2] in ('/*', '//')):
            if code[p] in " \n\t":
                p += 1
            elif code[p: p + 2] == '//':
                while p < len(code) and code[p] != '\n':
                    p += 1
            else:
                p += 2
                while p < len(code) and code[p: p + 2] != '*/':
                    p += 1
                if p >= len(code):
                    raise Error()
                p += 2
        if p >= len(code):
            break
        elif code[p].isdigit():
            num = ""
            while p < len(code) and (code[p].isdigit() or code[p] == '.'):
                num += code[p]
                p += 1
            res.append(num)
        elif code[p].isalpha() or code[p] == '_':
            word = ""
            while p < len(code) and (code[p].isalnum() or code[p] == '_'):
                word += code[p]
                p += 1
            if word in keywords:
                res.append('*' + word)
            else:
                res.append(word)
        elif code[p] == '"':
            string = code[p]
            p += 1
            while p < len(code) and code[p] != '"':
                if code[p] == '\\':
                    p += 1
                    if p >= len(code):
                        raise Error()
                    if code[p].isdigit():
                        if p + 3 >= len(code):
                            raise Error()
                        string += chr(int(code[p: p + 3], 8))
                    elif code[p] in escape:
                        string += escape[code[p]]
                    else:
                        raise Error()
                else:
                    string += code[p]
                    p += 1
            if p >= len(code):
                raise Error()
            string += code[p]
            p += 1
        elif code[p: p + 2] in operators:
            res.append(code[p: p + 2])
            p += 2
        elif code[p] in operators:
            res.append(code[p])
            p += 1
        else:
            raise Error(code[p:])
    res.append("")
    return res


class Scope:
    def __init__(self, parent, var: dict):
        self.parent, self.var = parent, var

    def find(self, name: str):
        if name in self.var:
            return self.var[name]
        elif isinstance(self.parent, Scope):
            return self.parent.find(name)
        else:
            raise Error(name)

    def set(self, name: str, value):
        if name in self.var:
            self.var[name] = value
            return value
        elif isinstance(self.parent, Scope):
            return self.parent.set(name, value)
        else:
            raise Error(name)

    def define(self, name: str, value):
        self.var[name] = value


class Expr:
    def eval(self, scope: Scope) -> typing.Any:
        ...


class Stmt:
    def run(self, scope: Scope):
        ...


class Block(Stmt):
    def __init__(self, stmts: list[Stmt]):
        self.stmts = stmts

    def run(self, scope: Scope) -> None | tuple:
        for i in self.stmts:
            v = i.run(scope)
            if v is not None:
                return v


class Func:
    def __init__(self, para: list[str], body: Block, closure: Scope):
        self.para, self.body, self.closure = para, body, closure

    def __call__(self, *args):
        scope = Scope(self.closure, dict(zip(self.para, args)))
        v = self.body.run(scope)
        if v is None:
            return None
        elif type(v) == tuple:
            return v[1]
        else:
            raise Error()


class Object:
    def __init__(self, attrs: dict):
        self.attrs = attrs

    def __getitem__(self, name: str):
        v = self.attrs[name]
        if isinstance(v, Func):
            return Method(self, v)
        return v

    def __setitem__(self, name: str, value):
        self.attrs[name] = value


class Method:
    def __init__(self, obj: Object, func: Func):
        self.obj, self.func = obj, func

    def __call__(self, *args):
        new_scope = Scope(self.func.closure, dict(zip(self.func.para, args)))
        new_scope.define("this", self.obj)
        v = self.func.body.run(new_scope)
        if v is None:
            return None
        return v[1]


class Type:
    def __init__(self, parents: list, attrs: dict):
        self.parents: list[Type] = parents
        self.attrs = attrs

    def new(self) -> Object:
        res = {}
        for i in self.parents:
            for k, v in i.new().attrs.items():
                res[k] = v
        for k, v in self.attrs.items():
            res[k] = v
        return Object(res)

    def __getitem__(self, name: str):
        return self.new()[name]

    def __setitem__(self, name: str, value: str):
        self.attrs[name] = value

    def __call__(self, *args):
        if "__init__" in self.attrs:
            constructor: Func = self.attrs["__init__"]
            new_scope = Scope(constructor.closure, dict(zip(constructor.para, args)))
            new_scope.define("this", self.new())
            constructor.body.run(new_scope)
            return new_scope.find("this")
        else:
            return self.new()


class Module:
    def __init__(self, attrs: dict):
        self.attrs = attrs

    def __getitem__(self, name: str):
        return self.attrs[name]

    def __setitem__(self, name: str, value):
        self.attrs[name] = value


class ExprStmt(Stmt):
    def __init__(self, expr: Expr):
        self.expr = expr

    def run(self, scope: Scope):
        self.expr.eval(scope)


class IfStmt(Stmt):
    def __init__(self, cases: list[tuple[Expr, Block]], default=Block([])):
        self.cases, self.default = cases, default

    def run(self, scope: Scope):
        for cond, body in self.cases:
            if cond.eval(scope):
                return body.run(scope)
        return self.default.run(scope)


class WhileStmt(Stmt):
    def __init__(self, cond: Expr, body: Block):
        self.cond, self.body = cond, body

    def run(self, scope: Scope):
        while self.cond.eval(scope):
            v = self.body.run(scope)
            if type(v) == tuple:
                return v
            elif v == BREAK:
                break


class DefStmt(Stmt):
    def __init__(self, name: str, para: list[str], body: Block):
        self.name, self.para, self.body = name, para, body

    def run(self, scope: Scope):
        scope.define(self.name, Func(self.para, self.body, scope))


class ReturnStmt(Stmt):
    def __init__(self, expr: Expr):
        self.expr = expr

    def run(self, scope: Scope):
        return RETURN, self.expr.eval(scope)


class BreakStmt(Stmt):
    def run(self, scope: Scope):
        return BREAK


class ContinueStmt(Stmt):
    def run(self, scope: Scope):
        return CONTINUE


class ForStmt(Stmt):
    def __init__(self, varname: str, obj: Expr, body: Block):
        self.varname, self.obj, self.body = varname, obj, body

    def run(self, scope: Scope):
        obj = self.obj.eval(scope)
        if isinstance(obj, collections.Iterable):
            for i in obj:
                scope.define(self.varname, i)
                v = self.body.run(scope)
                if type(v) == tuple:
                    return v
                elif v == BREAK:
                    break
        else:
            raise Error()


class VarDeclStmt(Stmt):
    def __init__(self, pairs: list[tuple[str, Expr]]):
        self.pairs = pairs

    def run(self, scope: Scope):
        for name, value in self.pairs:
            scope.define(name, value.eval(scope))


class ClassDef(Stmt):
    def __init__(self, name: str, parents: list[Expr], body: Block):
        self.name, self.parents, self.body = name, parents, body

    def run(self, scope: Scope):
        new_scope = Scope(scope, {})
        self.body.run(new_scope)
        new_scope.define("__typename__", self.name)
        scope.define(
            self.name,
            Type([i.eval(scope) for i in self.parents], new_scope.var)
        )


class AssignStmt(Stmt):
    def __init__(self, left: Expr, right: Expr):
        self.left, self.right = left, right

    def run(self, scope: Scope):
        right = self.right.eval(scope)
        if isinstance(self.left, Index):
            v: list = self.left.obj.eval(scope)
            v[self.left.index.eval(scope)] = right
        elif isinstance(self.left, Variable):
            scope.set(self.left.name, right)
        else:
            raise Error()


class NewMod(Stmt):
    def __init__(self, name: str, body: Block):
        self.name, self.body = name, body

    def run(self, scope: Scope):
        new_scope = Scope(scope, {})
        self.body.run(new_scope)
        scope.define(self.name, new_scope.var)


class Const(Expr):
    def __init__(self, value):
        self.value = value

    def eval(self, scope: Scope):
        return self.value


class Variable(Expr):
    def __init__(self, name: str):
        self.name = name

    def eval(self, scope: Scope):
        return scope.find(self.name)


class UnaryOp(Expr):
    def __init__(self, operator: str, value: Expr):
        self.operator, self.value = operator, value

    def eval(self, scope: Scope):
        return {
            '+': lambda a: +a,
            '-': lambda a: -a,
            '!': lambda a: not a,
            '~': lambda a: ~a,
        }[self.operator](self.value.eval(scope))


class Call(Expr):
    def __init__(self, func: Expr, args: list[Expr]):
        self.func, self.args = func, args

    def eval(self, scope: Scope):
        func = self.func.eval(scope)
        if callable(func):
            return func(*[i.eval(scope) for i in self.args])
        else:
            raise Error(func)


class Index(Expr):
    def __init__(self, obj: Expr, index: Expr):
        self.obj, self.index = obj, index

    def eval(self, scope: Scope):
        obj: list = self.obj.eval(scope)
        return obj[self.index.eval(scope)]


class Lambda(Expr):
    def __init__(self, para: list[str], body: Block):
        self.para, self.body = para, body

    def eval(self, scope: Scope):
        return Func(self.para, self.body, scope)


class BinaryOp(Expr):
    def __init__(self, operator: str, left: Expr, right: Expr):
        self.operator, self.left, self.right = operator, left, right

    def eval(self, scope: Scope):
        return {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '%': lambda a, b: a % b,
            '==': lambda a, b: a == b,
            '!=': lambda a, b: a != b,
            '<': lambda a, b: a < b,
            '>': lambda a, b: a > b,
            '>=': lambda a, b: a >= b,
            '<=': lambda a, b: a <= b,
            '<<': lambda a, b: a << b,
            '>>': lambda a, b: a >> b,
            '&&': lambda a, b: a and b,
            '||': lambda a, b: a or b,
            '&': lambda a, b: a & b,
            '|': lambda a, b: a | b,
            '^': lambda a, b: a ^ b,
        }[self.operator](self.left.eval(scope), self.right.eval(scope))


class NewList(Expr):
    def __init__(self, items: list[Expr]):
        self.items = items

    def eval(self, scope: Scope) -> typing.Any:
        return [i.eval(scope) for i in self.items]


def parse(tokens: list[str]) -> Block:
    pos = 0
    token = tokens[0]

    def eat(ex=None):
        nonlocal token, pos
        if ex == token or ex is None:
            pos += 1
            token = tokens[pos]
            return tokens[pos - 1]
        raise Error(token)

    def eat_id():
        if token != "" and (token[0].isalpha() or token[0] == '_'):
            return eat()
        else:
            raise Error()

    def parse_expression() -> Expr:
        res = parse_unit()
        if token in priority:
            res = BinaryOp(eat(), res, parse_unit())
            while token in priority:
                op = eat()
                prio = priority[op]
                unit = parse_unit()
                if priority[res.operator] > prio:
                    res = BinaryOp(op, res, unit)
                else:
                    res = BinaryOp(res.operator, res.left,
                                   BinaryOp(op, res.right, unit))
        return res

    def parse_unit() -> Expr:
        if token == '':
            raise Error()
        elif token[0].isdigit():
            if '.' in token:
                res = Const(float(eat()))
            else:
                res = Const(int(eat()))
        elif token[0].isalpha() or token[0] == '_':
            res = Variable(eat())
        elif token in ('+', '-', '!', '~'):
            res = UnaryOp(eat(), parse_unit())
        elif token == '(':
            eat()
            res = parse_expression()
            eat(')')
        elif token == '*func':
            eat()
            para = []
            eat('(')
            if token != ')':
                para.append(eat_id())
                while token == ',':
                    eat()
                    para.append(eat_id())
            res = Lambda(para, parse_block())
        elif token == '[':
            eat()
            items = []
            if token != ']':
                items.append(parse_expression())
                while token == ',':
                    eat()
                    items.append(parse_expression())
            eat(']')
            res = NewList(items)
        elif token == '*True':
            eat()
            res = Const(True)
        elif token == '*False':
            eat()
            res = Const(False)
        elif token == '*None':
            eat()
            res = Const(None)
        else:
            raise Error(token)
        while token in ('(', '[', '.'):
            if token == '(':
                eat()
                args = []
                if token != ')':
                    args.append(parse_expression())
                    while token == ',':
                        eat()
                        args.append(parse_expression())
                eat(')')
                res = Call(res, args)
            elif token == '[':
                eat()
                res = Index(res, parse_expression())
                eat(']')
            elif token == '.':
                eat()
                res = Index(res, Const(eat_id()))
        return res

    def parse_statement() -> Stmt:
        if token == '*if':
            eat()
            cases = [(parse_expression(), parse_block())]
            while token == '*elif':
                eat()
                cases.append((parse_expression(), parse_block()))
            if token == '*else':
                eat()
                return IfStmt(cases, parse_block())
            else:
                return IfStmt(cases)
        elif token == '*while':
            eat()
            return WhileStmt(parse_expression(), parse_block())
        elif token == '*def':
            eat()
            name = eat_id()
            para = []
            eat('(')
            if token != ')':
                para.append(eat_id())
                while token == ',':
                    eat()
                    para.append(eat_id())
            eat(')')
            return DefStmt(name, para, parse_block())
        elif token == '*for':
            eat()
            varname = eat_id()
            eat('*in')
            obj = parse_expression()
            return ForStmt(varname, obj, parse_block())
        elif token == '*var':
            eat()
            pairs = []
            name = eat_id()
            if token == '=':
                eat()
                value = parse_expression()
            else:
                value = Const(None)
            pairs.append((name, value))
            while token == ',':
                eat()
                name = eat_id()
                if token == '=':
                    eat()
                    value = parse_expression()
                else:
                    value = Const(None)
                pairs.append((name, value))
            return VarDeclStmt(pairs)
        elif token == '*class':
            eat()
            name = eat_id()
            if token == '*extends':
                eat()
                parents = [parse_expression()]
                while token == ',':
                    eat()
                    parents.append(parse_expression())
            else:
                parents = []
            return ClassDef(name, parents, parse_block())
        elif token == '*module':
            eat()
            return NewMod(eat_id(), parse_block())
        elif token == '*return':
            eat()
            return ReturnStmt(parse_expression())
        elif token == '*break':
            eat()
            return BreakStmt()
        elif token == '*continue':
            eat()
            return ContinueStmt()
        else:
            left = parse_expression()
            if token == '=':
                eat()
                return AssignStmt(left, parse_expression())
            return ExprStmt(left)

    def parse_block() -> Block:
        res = []
        eat('{')
        while token != '}':
            res.append(parse_statement())
        eat('}')
        return Block(res)

    parser_res: list[Stmt] = []
    while token != '':
        parser_res.append(parse_statement())
    return Block(parser_res)


std_scope = Scope(None, {
    'print': lambda *args: print(*args, sep="", flush=True, end=""),
    'println': lambda *args: print(*args, sep=""),
    'ord': ord,
    'chr': chr,
    'len': len,
    'getchar': lambda: sys.stdin.read(1),
    'read_ln': input,
})
my_code = '''
'''
parse(tokenize(my_code)).run(std_scope)

'''
// 经典
var a = [1, 2, [2, 4, 5]]
println(a)
a[2][0] = 3
println(a)


// 经典
def prime(n) {
    if n < 2 {
        return False
    }
    var i = 2
    while i < n {
        if n % i == 0 {
            return False
        }
        i = i + 1
    }
    return True
}

println(prime(10))
println(prime(11))


// 经典
class T {
    def __init__(a) {
        this.a = a
    }
    
    def print() {
        println(this.a)
    }
    
    def set(a) {
        this.a = a
    }
}

var a = T(10)
a.print()
a.set(20)
a.print()


// 经典
module pi {
    var pi = 3.14
}

println(pi.pi)
'''
