class BException(Exception):
    ...


class BSyntaxError(BException):
    ...


class BTypeError(BException):
    ...


class BNameError(BException):
    ...


keywords = {
    'if', 'else', 'while',
    'func', 'var', 'type',
    'return', 'break', 'continue',
    'None', 'True', 'False',
}
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
    ',', '.', '[', ']', '(', ')', '{', '}', ':', '=', '->', ';',
    '?', '!!',
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


def tokenize(code: str):
    res = []
    pos = 0

    while pos < len(code):
        # Skip whitespace/comment
        while pos < len(code) and (code[pos] in ' \n\t' or
                                   code[pos: pos + 2] in ('//', '/*')):
            if code[pos: pos + 2] == '//':
                while pos < len(code) and code[pos] != '\n':
                    pos += 1
            elif code[pos: pos + 2] == '/*':
                pos += 2
                while pos < len(code) and code[pos: pos + 2] != '*/':
                    pos += 1
                if pos >= len(code):
                    raise BSyntaxError("Unexpected EOF.")
            else:
                pos += 1
        # EOF
        if pos >= len(code):
            break
        # Number
        elif code[pos].isdigit():
            num = code[pos]
            pos += 1
            while pos < len(code) and (code[pos].isdigit() or
                                       code[pos] == '.'):
                num += code[pos]
                pos += 1
            if num.count('.') > 1:
                raise BSyntaxError(f"Too many dots in '{num}'.")
            res.append(num)
        # String
        elif code[pos] == '"':
            pos += 1
            s = '"'
            while pos < len(code) and code[pos] != '"':
                if code[pos] == '\\':
                    pos += 1
                    if pos >= len(code):
                        raise BSyntaxError("Unexpected EOF.")
                    elif code[pos] in escape:
                        s += escape[code[pos]]
                        pos += 1
                    elif code[pos] == 'x':
                        pos += 1
                        if pos + 2 >= len(code):
                            raise BSyntaxError("Unexpected EOF.")
                        s += chr(int(code[pos: pos + 2], 16))
                        pos += 2
                    elif code[pos] == 'u':
                        pos += 1
                        if pos + 4 >= len(code):
                            raise BSyntaxError("Unexpected EOF.")
                        s += chr(int(code[pos: pos + 4], 16))
                        pos += 4
                    else:
                        raise BSyntaxError("Unknown escape sequence.")
                else:
                    s += code[pos]
                    pos += 1
            if pos >= len(code):
                raise BSyntaxError("Unexpected EOF.")
            pos += 1
            s += '"'
            res.append(s)
        # Identifier/Keyword
        elif code[pos].isalpha() or code[pos] == '_':
            ident = code[pos]
            pos += 1
            while pos < len(code) and (code[pos].isalnum() or
                                       code[pos] == '_'):
                ident += code[pos]
                pos += 1
            if ident in keywords:
                res.append('*' + ident)
            else:
                res.append(ident)
        # Operator
        elif code[pos: pos + 2] in operators:
            res.append(code[pos: pos + 2])
            pos += 2
        elif code[pos] in operators:
            res.append(code[pos])
            pos += 1
        # Unknown
        else:
            raise BSyntaxError(f"Unexpected character '{code[pos]}'.")

    return res + ['']


class Func:
    def __init__(self, params: list, closure: "Scope", body: "Block"):
        self.params, self.closure, self.body = params, closure, body

    def __str__(self):
        return "Func(" + ", ".join(self.params) + ")"

    def __repr__(self):
        return "Func(" + ", ".join(self.params) + ")"


class Type:
    id_cnt = 0

    def __str__(self):
        ...

    def __repr__(self):
        ...

    def is_convertable(self, other: "Type"):
        ...

    def default_new(self):
        ...


class BasicType(Type):
    name_set = {}
    defaults = {
        'int': 0,
        'float': 0.0,
        'str': '',
        'bool': False,
        'NoneType': None,
    }

    # 有一种把基本数据类型和Object兼容的方式：
    # 把基本数据类型的各种方法硬编码进去
    # 这也是不得已而为之

    def __init__(self, name: str):
        self.name = name
        if name not in BasicType.name_set:
            self.id = BasicType.name_set[name] = Type.id_cnt
            Type.id_cnt += 1
        else:
            self.id = BasicType.name_set[name]

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def is_convertable(self, other: Type):
        if isinstance(other, OptType):
            if self.name == "NoneType":
                return True
            return self.is_convertable(other.base)
        if not isinstance(other, BasicType):
            return False
        return self.id == other.id

    def default_new(self):
        if self.name in BasicType.defaults:
            return BasicType.defaults[self.name]


class ObjectType(Type):
    def __init__(self, nt_pairs: dict):
        self.nt_pairs = nt_pairs
        self.id = Type.id_cnt
        self.cvt_set = {}
        Type.id_cnt += 1

    def __str__(self):
        return str(self.nt_pairs)

    def __repr__(self):
        return str(self.nt_pairs)

    def is_convertable(self, other: Type):
        if isinstance(other, OptType):
            return self.is_convertable(other.base)
        if not isinstance(other, ObjectType):
            return False
        if other.id == self.id:
            return True
        if other.id in self.cvt_set:
            return self.cvt_set[other.id]
        self.cvt_set[other.id] = True
        for i in other.nt_pairs:
            if i not in self.nt_pairs or\
                    not self.nt_pairs[i].\
                    is_convertable(other.nt_pairs[i]):
                self.cvt_set[other.id] = False
        return self.cvt_set[other.id]

    def default_new(self):
        res = {}
        for name, tp in self.nt_pairs.items():
            res[name] = tp.default_new()
        return res


class OptType(Type):
    def __init__(self, base: Type):
        self.base = base
        self.id = Type.id_cnt
        Type.id_cnt += 1

    def __str__(self):
        return f"{self.base}?"

    def __repr__(self):
        return f"{self.base}?"

    def is_convertable(self, other: Type):
        if isinstance(other, OptType):
            if self.base.is_convertable(other.base):
                return True
        return False

    def default_new(self):
        return None


class FuncType(Type):
    def __init__(self, params: list, ret: Type):
        self.params, self.ret = params, ret
        self.id = Type.id_cnt
        Type.id_cnt += 1
        self.cvt_set = {}

    def __str__(self):
        return f"{self.ret}(" + ", ".join(map(str, self.params)) + ")"

    def __repr__(self):
        return f"{self.ret}(" + ", ".join(map(str, self.params)) + ")"

    def is_convertable(self, other: Type):
        if isinstance(other, OptType):
            return self.is_convertable(other.base)
        if not isinstance(other, FuncType):
            return False
        if other.id == self.id:
            return True
        if other.id in self.cvt_set:
            return self.cvt_set[other.id]
        if len(self.params) != len(other.params):
            return False
        self.cvt_set[other.id] = True
        for i in range(len(self.params)):
            if not self.params[i].is_convertable(other.params[i]):
                return False
        return self.ret.is_convertable(other.ret)

    def default_new(self):
        return Func(self.params, Scope(None), Block([]))


class Scope:
    def __init__(self, parent: "Scope | None"):
        self.parent = parent
        self.vars = {}
        self.types = {}

    def find(self, name: str):
        if name in self.vars:
            return self.vars[name]
        elif self.parent:
            return self.parent.find(name)
        else:
            raise BNameError(f"Undefined variable '{name}'")

    def find_type(self, name: str) -> Type:
        if name in self.types:
            return self.types[name]
        elif self.parent:
            return self.parent.find_type(name)
        else:
            raise BNameError(f"Undefined typename '{name}'")

    def set(self, name: str, val):
        if name in self.vars:
            self.vars[name] = val
        elif self.parent:
            self.parent.set(name, val)
        else:
            raise BNameError(f"Undefined variable '{name}'")

    def define(self, name: str, val):
        self.vars[name] = val

    def define_type(self, name: str, val: Type):
        self.types[name] = val


class RunSignal:
    Return, Break, Continue = 0, 1, 2

    def __init__(self, signal: int, ret_val=None):
        self.signal, self.ret_val = signal, ret_val


class Stmt:
    def check(self, scope: Scope):
        ...

    def run(self, scope: Scope):
        ...


class Expr:
    def check(self, scope: Scope) -> Type:
        ...

    def eval(self, scope: Scope):
        ...


class TypeExpr:
    def get(self, scope: Scope) -> Type:
        ...


class NameTypeExpr(TypeExpr):
    def __init__(self, name: str):
        self.name = name

    def get(self, scope: Scope) -> Type:
        return scope.find_type(self.name)


class ObjectTypeExpr(TypeExpr):
    def __init__(self, nt_pairs: list):
        self.nt_pairs = nt_pairs

    def get(self, scope: Scope) -> Type:
        res = {}
        for name, tp in self.nt_pairs:
            res[name] = tp.get(scope)
        return ObjectType(res)


class OptTypeExpr(TypeExpr):
    def __init__(self, base: TypeExpr):
        self.base = base

    def get(self, scope: Scope) -> Type:
        return OptType(self.base.get(scope))


class FuncTypeExpr(TypeExpr):
    def __init__(self, params: list, ret: TypeExpr):
        self.params, self.ret = params, ret

    def get(self, scope: Scope) -> Type:
        return FuncType(list(map(lambda a: a.get(scope), self.params)),
                        self.ret.get(scope))


class ExprStmt(Stmt):
    def __init__(self, expr: Expr):
        self.expr = expr

    def check(self, scope: Scope):
        self.expr.check(scope)

    def run(self, scope: Scope):
        self.expr.eval(scope)


class NoOp(Stmt):
    ...


class Block(Stmt):
    def __init__(self, stmts: list):
        self.stmts = stmts

    def check(self, scope: Scope):
        res = None
        for stmt in self.stmts:
            cur = stmt.check(scope)
            if cur is not None:
                if res is not None:
                    if not cur.is_convertable(res):
                        raise BTypeError("Incompatible types")
                else:
                    res = cur
        return res

    def run(self, scope: Scope):
        for stmt in self.stmts:
            ret = stmt.run(scope)
            if ret is not None:
                return ret


class TypeDef(Stmt):
    def __init__(self, name: str, val: TypeExpr):
        self.name, self.val = name, val

    def check(self, scope: Scope):
        if isinstance(self.val, NameTypeExpr):
            scope.define_type(self.name, self.val.get(scope))
        elif isinstance(self.val, OptTypeExpr):
            scope.define_type(self.name, OptType(None))
            res = self.val.get(scope)
            scope.types[self.name].__dict__ = res.__dict__
        elif isinstance(self.val, ObjectTypeExpr):
            scope.define_type(self.name, ObjectType(None))
            res = self.val.get(scope)
            scope.types[self.name].__dict__ = res.__dict__
        elif isinstance(self.val, FuncTypeExpr):
            scope.define_type(self.name, FuncType([], None))
            res = self.val.get(scope)
            scope.types[self.name].__dict__ = res.__dict__

    def run(self, scope: Scope):
        if isinstance(self.val, NameTypeExpr):
            scope.define_type(self.name, self.val.get(scope))
        elif isinstance(self.val, OptTypeExpr):
            scope.define_type(self.name, OptType(None))
            res = self.val.get(scope)
            scope.types[self.name].__dict__ = res.__dict__
        elif isinstance(self.val, ObjectTypeExpr):
            scope.define_type(self.name, ObjectType(None))
            res = self.val.get(scope)
            scope.types[self.name].__dict__ = res.__dict__
        elif isinstance(self.val, FuncTypeExpr):
            scope.define_type(self.name, FuncType([], None))
            res = self.val.get(scope)
            scope.types[self.name].__dict__ = res.__dict__


class VarDecl(Stmt):
    def __init__(self, vars: list):
        self.vars = vars

    def check(self, scope: Scope):
        for name, tp, val in self.vars:
            if tp is not None:
                tp = tp.get(scope)
            if val is not None:
                val_tp = val.check(scope)
            else:
                val_tp = None
            if tp is None:
                tp = val_tp
            elif val_tp and not val_tp.is_convertable(tp):
                print(tp, val_tp)
                raise BTypeError("Incompatible types at vardecl")
            scope.define(name, tp)

    def run(self, scope: Scope):
        for name, tp, val in self.vars:
            if val is None:
                scope.define(name, tp.get(scope).default_new())
            else:
                scope.define(name, val.eval(scope))


class If(Stmt):
    def __init__(self, cases: list, default: Block):
        self.cases, self.default = cases, default

    def check(self, scope: Scope):
        res = None
        for cond, body in self.cases:
            cond.check(scope)
            cur = body.check(Scope(scope))
            if cur is not None:
                if res is not None:
                    if not cur.is_convertable(res):
                        raise BTypeError("Incompatible types")
                else:
                    res = cur
        cur = self.default.check(Scope(scope))
        if cur is not None:
            if res is not None:
                if not cur.is_convertable(res):
                    raise BTypeError("Incompatible types")
            else:
                res = cur
        return res

    def run(self, scope: Scope):
        for cond, body in self.cases:
            if cond.eval(scope):
                return body.run(scope)
        return self.default.run(scope)


class While(Stmt):
    def __init__(self, cond: Expr, body: Block):
        self.cond, self.body = cond, body

    def check(self, scope: Scope):
        self.cond.check(scope)
        return self.body.check(Scope(scope))

    def run(self, scope: Scope):
        new_scope = Scope(scope)
        while self.cond.eval(scope):
            ret = self.body.run(new_scope)
            if isinstance(ret, RunSignal):
                if ret.signal == RunSignal.Break:
                    break
                if ret.signal == RunSignal.Return:
                    return ret


class Break(Stmt):
    def run(self, scope: Scope):
        return RunSignal(RunSignal.Break)


class Continue(Stmt):
    def run(self, scope: Scope):
        return RunSignal(RunSignal.Continue)


class Return(Stmt):
    def __init__(self, val: Expr):
        self.val = val

    def check(self, scope: Scope):
        return self.val.check(scope)

    def run(self, scope: Scope):
        return RunSignal(RunSignal.Return, self.val.eval(scope))


class FuncDef(Stmt):
    def __init__(self, name: str, params: list,
                 ret: TypeExpr, body: Block):
        self.name = name
        self.params, self.ret, self.body = params, ret, body

    def check(self, scope: Scope):
        params = list(map(lambda a: a[1].get(scope), self.params))
        ret = self.ret.get(scope)
        fntype = FuncType(params, ret)
        scope.define(self.name, fntype)
        new_scope = Scope(scope)
        new_scope.vars = dict(zip(map(lambda a: a[0], self.params),
                                  params))
        ret = self.body.check(new_scope)
        if not ret.is_convertable(ret):
            raise BTypeError("Mismatched function return type")
        return fntype

    def run(self, scope: Scope):
        scope.define(self.name,
                     Func(list(map(lambda a: a[0], self.params)),
                          scope, self.body))


class Assign(Stmt):
    def __init__(self, left: Expr, right: Expr):
        self.left, self.right = left, right

    def check(self, scope: Scope):
        if not isinstance(self.left, VarExpr) and\
                not isinstance(self.left, DotOp):
            raise BTypeError("Expect an l-value")
        left, right = self.left.check(scope), self.right.check(scope)
        if not right.is_convertable(left):
            raise BTypeError("Incompatible types at Assign")

    def run(self, scope: Scope):
        right = self.right.eval(scope)
        if isinstance(self.left, VarExpr):
            scope.set(self.left.name, right)
        elif isinstance(self.left, DotOp):
            base = self.left.base.eval(scope)
            attr = self.left.attr
            base[attr] = right


class ValueExpr(Expr):
    def __init__(self, val):
        self.val = val

    def check(self, scope: Scope):
        return BasicType(type(self.val).__name__)

    def eval(self, scope: Scope):
        return self.val


class VarExpr(Expr):
    def __init__(self, name: str):
        self.name = name

    def check(self, scope: Scope):
        return scope.find(self.name)

    def eval(self, scope: Scope):
        return scope.find(self.name)


class Unary(Expr):
    ops = {
        '+': lambda a: +a,
        '-': lambda a: -a,
        '!': lambda a: not a,
        '~': lambda a: ~a,
    }

    def __init__(self, op: str, val: Expr):
        self.op, self.val = op, val

    def check(self, scope: Scope):
        val_tp = self.val.check(scope)
        if self.op == '!':
            return BasicType('bool')
        if isinstance(val_tp, BasicType):
            if val_tp.name in ('int', 'bool'):
                return BasicType('int')
            if val_tp.name == 'float':
                return val_tp
        raise BTypeError("Unsupported unary operation")

    def eval(self, scope: Scope):
        return Unary.ops[self.op](self.val.eval(scope))


class Binary(Expr):
    ops = {
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
    }

    def __init__(self, op: str, left: Expr, right: Expr):
        self.op, self.left, self.right = op, left, right

    def check(self, scope: Scope):
        op = self.op
        left, right = self.left.check(scope), self.right.check(scope)
        if op in ('==', '!=', '&&', '||'):
            return BasicType('bool')
        if isinstance(left, BasicType) and isinstance(right, BasicType):
            if left.name in ('int', 'float', 'bool') and\
                    right.name in ('int', 'float', 'bool'):
                if op in ('>', '<', '>=', '<='):
                    return BasicType('bool')
                if left.name == 'float' or right.name == 'float':
                    return BasicType('float')
                return BasicType('int')
            if op in ('>', '<', '>=', '<=') and\
                    left.name == right.name == 'str':
                return BasicType('bool')
            if op == '+' and left.name == right.name == 'str':
                return left
            if op == '*' and left.name in ('int', 'bool') and\
                    right.name == 'str':
                return 'str'
            if op == '*' and right.name in ('int', 'bool') and\
                    left.name == 'str':
                return 'str'
        raise BTypeError("Unsupported binary operation")

    def eval(self, scope: Scope):
        return Binary.ops[self.op](self.left.eval(scope),
                                   self.right.eval(scope))


class DotOp(Expr):
    def __init__(self, base: Expr, attr: str):
        self.base, self.attr = base, attr

    def check(self, scope: Scope):
        base, attr = self.base.check(scope), self.attr
        if isinstance(base, ObjectType):
            if attr not in base.nt_pairs:
                raise BTypeError("Wrong attrname at DotOp")
            return base.nt_pairs[attr]
        raise BTypeError("Wrong object as DotOp.base")

    def eval(self, scope: Scope):
        return self.base.eval(scope)[self.attr]


class ObjectExpr(Expr):
    def __init__(self, val: list):
        self.val = val

    def check(self, scope: Scope):
        res = {}
        for k, v in self.val:
            res[k] = v.check(scope)
        return ObjectType(res)

    def eval(self, scope: Scope):
        res = {}
        for k, v in self.val:
            res[k] = v.eval(scope)
        return res


class ForceOp(Expr):
    def __init__(self, base: Expr):
        self.base = base

    def check(self, scope: Scope):
        base = self.base.check(scope)
        if not isinstance(base, OptType):
            raise BTypeError("Expect an OptType at ForceOp")
        return base.base

    def eval(self, scope: Scope):
        return self.base.eval(scope)


class FuncExpr(Expr):
    def __init__(self, params: list, ret: TypeExpr, body: Block):
        self.params, self.ret, self.body = params, ret, body

    def check(self, scope: Scope):
        params = list(map(lambda a: a[1].get(scope), self.params))
        ret = self.ret.get(scope)
        fntype = FuncType(params, ret)
        new_scope = Scope(scope)
        new_scope.vars = dict(zip(map(lambda a: a[0], self.params),
                                  params))
        ret = self.body.check(new_scope)
        if not ret.is_convertable(ret):
            raise BTypeError("Mismatched function return type")
        return fntype

    def eval(self, scope: Scope):
        return Func(list(map(lambda a: a[0], self.params)),
                    scope, self.body)


class Call(Expr):
    def __init__(self, func: Expr, args: list):
        self.func, self.args = func, args

    def check(self, scope: Scope):
        func = self.func.check(scope)
        args = list(map(lambda a: a.check(scope), self.args))
        if not isinstance(func, FuncType):
            raise BTypeError("Expect a function at Call")
        if len(args) != len(func.params):
            raise BTypeError("Mismatched function args")
        for i in range(len(args)):
            if not args[i].is_convertable(func.params[i]):
                raise BTypeError("Mismatched function args")
        return func.ret

    def eval(self, scope: Scope):
        func = self.func.eval(scope)
        args = list(map(lambda a: a.eval(scope), self.args))
        new_scope = Scope(func.closure)
        new_scope.vars = dict(zip(func.params, args))
        ret = func.body.run(new_scope)
        if ret is None:
            return None
        return ret.ret_val


def parse(tokens: list):
    token = tokens[0]
    pos = 0

    def eat(expect=None):
        nonlocal token, pos
        if expect is None or token == expect:
            pos += 1
            token = tokens[pos]
            return tokens[pos-1]
        raise BSyntaxError(f"Unexpected token '{token}', expected '{expect}'")

    def eat_id():
        if token and (token[0].isalpha() or token[0] == '_'):
            return eat()
        raise BSyntaxError(f"Unexpected token '{token}'\
, expected an identifier")

    def parse_factor():
        if token == '':
            raise BSyntaxError("Unexpected EOF.")
        elif token[0].isdigit():
            if '.' in token:
                res = ValueExpr(float(eat()))
            else:
                res = ValueExpr(int(eat()))
        elif token[0].isalpha() or token[0] == '_':
            res = VarExpr(eat())
        elif token == '(':
            eat()
            res = parse_expr()
            eat(')')
        elif token in ('+', '-', '!', '~'):
            op = eat()
            return Unary(op, parse_factor())
        elif token == '*True':
            eat()
            res = ValueExpr(True)
        elif token == '*False':
            eat()
            res = ValueExpr(False)
        elif token == '*None':
            eat()
            res = ValueExpr(None)
        elif token == '{':
            eat()
            res = []
            while token != '}':
                name = eat_id()
                eat(':')
                val = parse_expr()
                res.append((name, val))
                if token != '}':
                    eat(',')
            eat('}')
            res = ObjectExpr(res)
        elif token == '*func':
            eat()
            eat('(')
            params = []
            if token != ')':
                name = eat_id()
                eat(':')
                tp = parse_type()
                params.append((name, tp))
                while token == ',':
                    eat(',')
                    name = eat_id()
                    eat(':')
                    tp = parse_type()
                    params.append((name, tp))
            eat(')')
            eat('->')
            ret = parse_type()
            body = parse_block()
            res = FuncExpr(params, ret, body)
        else:
            raise BSyntaxError(f"Unexpected token '{token}'")

        while token in ('.', '!!', '('):
            if token == '.':
                eat()
                res = DotOp(res, eat_id())
            elif token == '!!':
                eat()
                res = ForceOp(res)
            elif token == '(':
                eat()
                args = []
                if token != ')':
                    args.append(parse_expr())
                    while token == ',':
                        eat(';')
                        args.append(parse_expr())
                eat(')')
                res = Call(res, args)

        return res

    def parse_expr():
        res = [parse_factor()]
        stack = []
        while token in priority:
            op = eat()
            while stack and priority[stack[-1]] >= priority[op]:
                r, l = res.pop(), res.pop()
                res.append(Binary(stack.pop(), l, r))
            stack.append(op)
            res.append(parse_factor())
        while stack:
            r, l = res.pop(), res.pop()
            res.append(Binary(stack.pop(), l, r))
        return res[-1]

    def parse_stmt():
        if token == ';':
            eat()
            return NoOp()
        elif token == '*type':
            eat()
            name = eat_id()
            eat('=')
            return TypeDef(name, parse_type())
        elif token == '*var':
            eat()
            vars = []
            name = eat_id()
            if token == ':':
                eat()
                tp = parse_type()
            else:
                tp = None
            if token == '=':
                eat()
                val = parse_expr()
            else:
                val = None
            if tp is None and val is None:
                raise BSyntaxError("Expect value or type at VarDecl")
            vars.append((name, tp, val))
            while token == ',':
                eat()
                name = eat_id()
                if token == ':':
                    eat()
                    tp = parse_type()
                else:
                    tp = None
                if token == '=':
                    eat()
                    val = parse_expr()
                else:
                    val = None
                if tp is None and val is None:
                    raise BSyntaxError("Expect value or type at VarDecl")
                vars.append((name, tp, val))
            return VarDecl(vars)
        elif token == '*func' and token[pos + 1] != '(':
            eat()
            fnname = eat_id()
            eat('(')
            params = []
            if token != ')':
                name = eat_id()
                eat(':')
                tp = parse_type()
                params.append((name, tp))
                while token == ',':
                    eat(',')
                    name = eat_id()
                    eat(':')
                    tp = parse_type()
                    params.append((name, tp))
            eat(')')
            eat('->')
            ret = parse_type()
            body = parse_block()
            return FuncDef(fnname, params, ret, body)
        elif token == '*if':
            eat()
            cases = [(parse_expr(), parse_block())]
            while token == '*else':
                eat()
                if token == '*if':
                    eat()
                    cases.append((parse_expr(), parse_block()))
                else:
                    default = parse_block()
                    return If(cases, default)
            return If(cases, Block([]))
        elif token == '*while':
            eat()
            return While(parse_expr(), parse_block())
        elif token == '*return':
            eat()
            val = parse_expr()
            return Return(val)
        elif token == '*break':
            eat()
            return Break()
        elif token == '*continue':
            eat()
            return Continue()
        else:
            left = parse_expr()
            if token == '=':
                eat()
                right = parse_expr()
                eat(';')
                return Assign(left, right)
            eat(';')
            return ExprStmt(left)

    def parse_type():
        if token == '{':
            eat()
            res = []
            while token != '}':
                name = eat_id()
                eat(':')
                tp = parse_type()
                res.append((name, tp))
                if token != '}':
                    eat(',')
            eat('}')
            res = ObjectTypeExpr(res)
        else:
            res = NameTypeExpr(eat_id())

        while token == '(':
            eat()
            params = []
            if token != ')':
                params.append(parse_type())
                while token == ',':
                    eat(',')
                    params.append(parse_type())
            eat(')')
            res = FuncTypeExpr(params, res)

        if token == '?':
            eat()
            res = OptTypeExpr(res)
        return res

    def parse_block():
        eat('{')
        res = []
        while token != '}':
            res.append(parse_stmt())
        eat('}')
        return Block(res)

    res = []
    while token != '':
        res.append(parse_stmt())
    return Block(res)


def std_scope():
    scope = Scope(None)
    scope.types = {
        "int": BasicType("int"),
        "float": BasicType("float"),
        "str": BasicType("str"),
        "bool": BasicType("bool"),
        "NoneType": BasicType("NoneType")
    }
    return scope


code = '''
'''
scope = std_scope()
check_scope = std_scope()
tokens = tokenize(code)
ast = parse(tokens)
ast.check(check_scope)
print(check_scope.vars, check_scope.types)
ast.run(scope)
print(scope.vars, scope.types)

"""
type A = {
    a: int,
}

var a: A;
while a.a < 10 {
    a.a = a.a + 1;
}

type Int = int
var a: Int = 1;
a;

type A = { val: int, next: { some: A, none: NoneType } }
type B = { val: int, val2: str, next: { some: A, none: NoneType } }

var b: B; // default_new爆炸（
var a: A = b;

type A = { val: int, next: A? }
type B = { val: int, val2: str, next: B? }

var b: B;
var a: A = b;

var a: int? = 1;
var b: int? = None;

type Fn = int(int)

var fn: Fn = func(a: int) -> int { return a + 1; }
var ret = fn(10);

func fn(a: int) -> int { return a + 1; }
var ret = fn(10);

func fac(a: int) -> int {
    if a == 0 { return 1; }
    else      { return fac(a - 1) * a; }
}

var ret = fac(10);

func Counter(start: int) -> int() {
    return func() -> int {
        start = start + 1;
        return start;
    }
}

var counter = Counter(1);
var a = counter();
var b = counter();
"""
