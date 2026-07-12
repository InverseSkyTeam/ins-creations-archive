"""
Butterfly归根到底是标记类型系统的编程语言
结构类型系统分支只不过是写出来给别人看的

仍然使用等价类型系统，这可能是最好实现的了，没有之一

对每个新的东西我都要为它找一个源头
如果这样的话等价类型系统的源头就是integer3.1

可以说Butterfly和Rusp是互相积累技术了
Butterfly的内置函数终于丢开可恶的描述限制了
这完全是Rusp里面builtin检查法的功劳

继承和子类弱转不准备实现，显式感觉会更明确一点，也多不了多少
（来自C和Rusp的启示）
"""

from typing import Any, NamedTuple
from enum import Enum, unique


class BException(Exception):
    ...


class BSyntaxError(BException):
    ...


class BNameError(BException):
    ...


class BTypeError(BException):
    ...


escape = {
    "r": "\r",
    "t": "\t",
    "a": "\a",
    "f": "\f",
    "v": "\v",
    "b": "\b",
    "n": "\n",
    "\\": "\\",
    "'": "'",
    '"': '"',
}

keywords = {
    'if', 'else', 'while',
    'func', 'var', 'type',
    'return', 'break', 'continue',
    'None', 'True', 'False',
    'null_list', 'new',
}

operators = {
    '+', '-', '*', '/', '%',
    '==', '!=', '>', '<', '>=', '<=',
    '<<', '>>', '&&', '||', '&', '|', '^',
    '!', '~',
    '(', ')', '[', ']', '{', '}',
    ',', '.', ';', ':', '->', '=',
}

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


class Scope:
    def __init__(self, parent: "Scope | None"):
        self.parent = parent
        self.variables = {}
        self.types = {}
        self.typegens = {}

    def find(self, name: str):
        if name in self.variables:
            return self.variables[name]
        elif self.parent:
            return self.parent.find(name)
        else:
            raise BNameError(f"Undefined variable '{name}'")

    def set(self, name: str, val):
        if name in self.variables:
            self.variables[name] = val
        elif self.parent:
            self.parent.set(name, val)
        else:
            raise BNameError(f"Undefined variable '{name}'")

    def find_type(self, name: str):
        if name in self.types:
            return self.types[name]
        elif self.parent:
            return self.parent.find_type(name)
        else:
            raise BNameError(f"Undefined typename '{name}'")
        
    def find_typegen(self, name: str):
        if name in self.typegens:
            return self.typegens[name]
        elif self.parent:
            return self.parent.find_typegen(name)
        else:
            raise BNameError(f"Undefined template '{name}'")

    def define(self, name: str, val):
        self.variables[name] = val

    def define_type(self, name: str, val):
        self.types[name] = val

    def define_typegen(self, name: str, tparams: list[str], tval):
        self.typegens[name] = tparams, tval


def parse(tokens: list[str]):
    pos = 0
    token = tokens[pos]

    def eat(expect: "str | None" = None):
        nonlocal pos, token
        if expect is None or token == expect:
            pos += 1
            token = tokens[pos]
            return tokens[pos - 1]
        raise BSyntaxError(f"Unexpected token '{token}', expected '{expect}'")

    def eat_id():
        nonlocal pos, token
        if not token or not (token[0].isalpha() or token[0] == '_'):
            raise BSyntaxError(f"Unexpected token '{
                               token}', expected an identifier")
        pos += 1
        token = tokens[pos]
        return tokens[pos - 1]

    def parse_expr():
        res = [parse_factor()]
        stack = []
        while token in priority:
            op = eat()
            while stack and priority[stack[-1]] >= priority[op]:
                r, l = res.pop(), res.pop()
                res.append(('binary', stack.pop(), l, r))
            stack.append(op)
            res.append(parse_factor())
        while stack:
            r, l = res.pop(), res.pop()
            res.append(('binary', stack.pop(), l, r))
        return res[-1]

    def parse_factor():
        if token == '':
            raise BSyntaxError("Unexpected EOF")
        elif token[0].isalpha() or token[0] == '_':
            res = 'id', eat()
        elif token[0].isdigit():
            if '.' in token:
                res = 'const', float(eat())
            else:
                res = 'const', int(eat())
        elif token[0] == '"':
            res = 'const', eat()[1:-1]
        elif token == '(':
            eat()
            res = parse_expr()
            eat(')')
        elif token == '[':
            eat()
            items = [parse_expr()]
            while token == ',':
                eat()
                items.append(parse_expr())
            if token == ',':
                eat()
            eat(']')
            res = 'list', items
        elif token == '{':
            eat()
            kvpairs = []
            while token != '}':
                name = eat_id()
                eat(':')
                val = parse_expr()
                kvpairs.append((name, val))
                if token != '}':
                    eat(',')
            eat('}')
            res = 'object', kvpairs
        elif token in ('+', '-', '!', '~'):
            res = 'unary', eat(), parse_expr()
        elif token == '*True':
            eat()
            res = 'const', True
        elif token == '*False':
            eat()
            res = 'const', False
        elif token == '*None':
            eat()
            res = 'const', None
        elif token == '*func':
            eat()
            params = []
            eat('(')
            while token != ')':
                name = eat_id()
                eat(':')
                tp = parse_type()
                params.append((name, tp))
                if token != ')':
                    eat(',')
            eat(')')
            eat('->')
            ret_tp = parse_type()
            res = 'func', params, ret_tp, parse_block()
        elif token == '*null_list':
            eat()
            eat('<')
            res = 'null_list', parse_type()
            eat('>')
        elif token == '*new':
            eat()
            tp = parse_type()
            eat('{')
            kvpairs = []
            while token != '}':
                name = eat_id()
                eat(':')
                val = parse_expr()
                kvpairs.append((name, val))
                if token != '}':
                    eat(',')
            eat('}')
            return 'new', tp, kvpairs
        else:
            raise BSyntaxError(f"Unexpected token '{token}'")

        while token in ('[', '(', '.', '?', '!!'):
            if token == '[':
                eat()
                res = 'index', res, parse_expr()
                eat(']')
            elif token == '(':
                eat()
                args = []
                while token != ')':
                    args.append(parse_expr())
                    if token != ')':
                        eat(',')
                eat(')')
                res = 'call', res, args
            elif token == '.':
                eat()
                res = 'attr', res, eat_id()

        return res

    def parse_stmt():
        if token == ';':
            eat()
            return 'noop',
        elif token == '*var':
            eat()
            variables = []
            while token != ';':
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
                    raise BSyntaxError(
                        "Expect type or value at variable declaration")
                variables.append((name, val, tp))
                if token != ';':
                    eat(',')
            eat(';')
            return 'vardecl', variables
        elif token == '*if':
            eat()
            cases = [(parse_expr(), parse_block())]
            while token == '*else':
                eat()
                if token == '*if':
                    eat()
                    cases.append((parse_expr(), parse_block()))
                else:
                    return 'if', cases, parse_block()
            return 'if', cases, ('block', [])
        elif token == '*while':
            eat()
            return 'while', parse_expr(), parse_block()
        elif token == '*func':
            eat()
            fname = eat_id()
            params = []
            eat('(')
            while token != ')':
                name = eat_id()
                eat(':')
                tp = parse_type()
                params.append((name, tp))
                if token != ')':
                    eat(',')
            eat(')')
            eat('->')
            ret_tp = parse_type()
            body = parse_block()
            return 'fndef', fname, params, ret_tp, body
        elif token == '*type':
            eat()
            tname = eat_id()
            if token == '<':
                eat()
                tparams = []
                while token != '>':
                    tparams.append(eat_id())
                    if token != '>':
                        eat(',')
                eat('>')
                eat('=')
                tval = parse_type()
                eat(';')
                return 'typegen', tname, tparams, tval
            else:
                eat('=')
                tval = parse_type()
                eat(';')
                return 'type', tname, tval
        elif token == '*return':
            eat()
            if token == ';':
                res = 'const', None
            else:
                res = parse_expr()
            eat(';')
            return 'return', res
        elif token == '*break':
            eat()
            eat(';')
            return 'break',
        elif token == '*continue':
            eat()
            eat(';')
            return 'continue',
        else:
            left = parse_expr()
            if token == '=':
                eat()
                right = parse_expr()
                eat(';')
                return 'assign', left, right
            eat(';')
            return 'exprstmt', left

    def parse_block():
        stmts = []
        eat('{')
        while token != '}':
            stmts.append(parse_stmt())
        eat('}')
        return 'block', stmts

    def parse_type():
        if not token:
            raise BSyntaxError("Unexpected EOF")
        if token[0].isalpha() or token[0] == '_':
            base = eat()
            targs = []
            if token == '<':
                eat()
                while token != '>':
                    targs.append(parse_type())
                    if token != '>':
                        eat(',')
                eat('>')
                base = 'template', base, targs
            else:
                base = 'basic', base
        elif token[0] == '{':
            eat()
            ntvpairs = []
            while token != '}':
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
                    raise BSyntaxError(
                        "Expect type or value at variable declaration")
                ntvpairs.append((name, tp, val))
                if token != '}':
                    eat(',')
            eat('}')
            base = 'complex', ntvpairs
        else:
            raise BSyntaxError(f"Unexpected token '{token}'")

        while token in ('[', '('):
            if token == '[':
                eat()
                eat(']')
                base = 'list', base
            elif token == '(':
                eat()
                param_types = []
                while token != ')':
                    param_types.append(parse_type())
                    if token != ')':
                        eat(',')
                eat(')')
                base = 'func', base, param_types
        return base
    
    res = []
    while token != '':
        res.append(parse_stmt())
    return res


def check_binary(op: str, l, r):
    if op in ('&&', '||', '==', '!='):
        return 'bool'
    if l in ('int', 'float', 'bool') and r in ('int', 'float', 'bool'):
        if op in ('>', '<', '>=', '<='):
            return 'bool'
        if 'float' in (l, r):
            return 'float'
        return 'int'
    if op == '+' and l == 'str' and r == 'str':
        return 'str'
    if op == '+' and isinstance(l, tuple) and l[0] == 'list' and\
            isinstance(r, tuple) and r[0] == 'list':
        return l
    if op == '*' and l == 'str' and r in ('int', 'bool'):
        return 'str'
    if op == '*' and l in ('int', 'bool') and r == 'str':
        return 'str'
    if op == '*' and isinstance(l, tuple) and l[0] == 'list' and r in ('int', 'bool'):
        return l
    if op == '*' and l in ('int', 'bool') and isinstance(r, tuple) and r[0] == 'list':
        return r
    raise BTypeError(f"Invalid binary operation for '{op}': {l}, {r}")


def check(prog: list, scope: Scope):

    # 又成为低内聚高耦合了（
    expected_ret = None
    context: list | None = None

    def expr(node):
        nonlocal scope, expected_ret, context
        match node:
            case 'const', val:
                return type(val).__name__
            case 'id', name:
                return scope.find(name)
            case 'unary', op, arg:
                tp = expr(arg)
                if op == '!':
                    return 'bool'
                if tp == 'bool':
                    return 'int'
                if tp in ('int', 'float'):
                    return tp
                raise BTypeError(f"Invalid unary operation for '{op}': {tp}")
            case 'binary', op, left, right:
                l, r = expr(left), expr(right)
                return check_binary(op, l, r)
            case 'list', items:
                if not items:
                    raise BTypeError(
                        "Please use null_list<T> instead of [] to create an empty list")
                tp = expr(items[0])
                for i in items[1:]:
                    if expr(i) != tp:
                        raise BTypeError("Conflicting types in list")
                return 'list', tp
            case 'index', base, index:
                base, index = expr(base), expr(index)
                if isinstance(base, tuple) and base[0] == 'list' and index in ('int', 'bool'):
                    return base[1]
                if base == 'str' and index in ('int', 'bool'):
                    return 'str'
                raise BTypeError(f"Invalid index operation: {base}, {index}")
            case 'attr', base, attr:
                base = expr(base)
                if isinstance(base, dict) and attr in base:
                    return base[attr]
                raise BTypeError(
                    f"Invalid attribute operation: {base}, {attr}")
            case 'call', fn, args:
                fn, args = expr(fn), [expr(arg) for arg in args]
                if callable(fn):
                    return fn(*args)
                if not (isinstance(fn, tuple) and fn[0] == 'func'):
                    raise BTypeError(f"Expect a function, got {fn}")
                ret_tp, *param_types = fn[1:]
                if len(args) != len(param_types):
                    raise BTypeError("Conflicting number of arguments")
                for arg, param in zip(args, param_types):
                    if arg != param:
                        raise BTypeError(f"Conflicting types in arguments: {arg}, {param}")
                return ret_tp
            case 'func', params, ret_tp, body:
                param_types = [type_eval(tp) for name, tp in params]
                ret = type_eval(ret_tp)
                ftype = 'func', ret, *param_types
                if context is None:
                    scope = Scope(scope)
                    for name, tp in zip(map(lambda x: x[0], params), param_types):
                        scope.define(name, tp)
                    expected_ret = ret
                    stmt(body)
                    expected_ret = None
                    scope = scope.parent
                else:
                    context.append((node, ftype))
                return ftype
            case 'object', kvpairs:
                res = {}
                for name, val in kvpairs:
                    res[name] = expr(val)
                return res
            case 'null_list', tp:
                return 'list', type_eval(tp)
            case 'new', tp, kvpairs:
                tp = type_eval(tp)
                for name, val in kvpairs:
                    if name not in tp:
                        raise BTypeError(f"Invalid attribute in new: {name}")
                    if expr(val) != tp[name]:
                        raise BTypeError(f"Conflicting types in new: {name}, {tp[name]}, {expr(val)}")
                return tp

    def stmt(node):
        nonlocal scope, expected_ret
        match node:
            case 'block', stmts:
                for i in stmts:
                    stmt(i)
            case 'noop':
                return
            case 'exprstmt', e:
                expr(e)
            case 'vardecl', variables:
                for name, val, tp in variables:
                    if tp is None:
                        tp = expr(val)
                    elif val is not None:
                        tp = type_eval(tp)
                        if expr(val) != tp:
                            raise BTypeError("Conflicting types in variable declaration")
                    else:
                        # raise BException(name, val, tp)
                        tp = type_eval(tp)
                    scope.define(name, tp)
            case 'if', cases, else_block:
                for cond, block in cases:
                    expr(cond)
                    scope = Scope(scope)
                    stmt(block)
                    scope = scope.parent
                scope = Scope(scope)
                stmt(else_block)
                scope = scope.parent
            case 'while', cond, block:
                expr(cond)
                scope = Scope(scope)
                stmt(block)
                scope = scope.parent
            case 'break',:
                return
            case 'continue',:
                return
            case 'return', val:
                if expected_ret is None:
                    raise BTypeError("Return statement outside function")
                val_tp = expr(val)
                if val_tp != expected_ret:
                    raise BTypeError(f"Conflicting types in return statement: {val_tp}, {expected_ret}")
            case 'fndef', fname, params, ret_tp, body:
                param_types = [type_eval(tp) for name, tp in params]
                ret = type_eval(ret_tp)
                scope.define(fname, ('func', ret, *param_types))
                scope = Scope(scope)
                for name, tp in zip(map(lambda x: x[0], params), param_types):
                    scope.define(name, tp)
                expected_ret = ret
                stmt(body)
                expected_ret = None
                scope = scope.parent
            case 'type', tname, tval:
                scope.define_type(tname, type_eval(tval))
            case 'typegen', tname, tparams, tval:
                scope.define_typegen(tname, tparams, tval)
            case 'assign', left, right:
                if left[0] not in ('id', 'attr', 'index'):
                    raise BTypeError("Invalid l-value in assignment")
                left_tp = expr(left)
                right_tp = expr(right)
                if left_tp != right_tp:
                    raise BTypeError(f"Conflicting types in assignment: {left_tp}, {right_tp}")
            
    def type_eval(node):
        nonlocal scope, expected_ret, context
        match node:
            case 'basic', name:
                if name in ('int', 'float', 'bool', 'str', 'NoneType'):
                    return name
                return scope.find_type(name)
            case 'template', name, targs:
                targs = [type_eval(targ) for targ in targs]
                tparams, tval = scope.find_typegen(name)
                if len(targs) != len(tparams):
                    raise BTypeError(f"Invalid number of type arguments: {name}, {targs}")
                scope = Scope(scope)
                scope.types = dict(zip(tparams, targs))
                res = type_eval(tval)
                scope = scope.parent
                return res
            case 'complex', ntvpairs:
                context = []
                res = {}
                for name, tp, val in ntvpairs:
                    if tp is None:
                        tp = expr(val)
                    elif val is not None:
                        tp = type_eval(tp)
                        if expr(val) != tp:
                            raise BTypeError("Conflicting types in complex type")
                    else:
                        tp = type_eval(tp)
                    res[name] = tp
                # 抽象但不得不
                # C++大概率也是这样的
                for fnode, ftype in context:
                    assert fnode[0] == 'func'
                    _, params, ret_tp, body = fnode
                    _, ret, *param_types = ftype
                    scope = Scope(scope)
                    scope.variables = dict(zip(map(lambda x: x[0], params), param_types))
                    scope.define('self', res)
                    expected_ret = ret
                    stmt(body)
                    expected_ret = None
                    scope = scope.parent
                context = None
                return res
            case 'list', tp:
                return 'list', type_eval(tp)
            case 'func', ret_tp, *param_types:
                return 'func', type_eval(ret_tp), *map(type_eval, param_types)

    for i in prog:
        stmt(i)


class Func:
    def __init__(self, params: list[str], body, closure: Scope):
        self.params, self.body, self.closure = params, body, closure


class Method:
    def __init__(self, obj, func):
        self.obj, self.func = obj, func


def run(prog: list, scope: Scope):

    def expr(node):
        nonlocal scope
        match node:
            case 'const', val:
                return val
            case 'id', name:
                return scope.find(name)
            case 'unary', op, arg:
                return {
                    '+': lambda x: +arg,
                    '-': lambda x: -arg,
                    '!': lambda x: not arg,
                    '~': lambda x: ~arg,
                }[op](expr(arg))
            case 'binary', op, left, right:
                if op == '&&':
                    if not expr(left):
                        return False
                    return bool(expr(right))
                if op == '||':
                    if expr(left):
                        return True
                    return bool(expr(right))
                return {
                    '+': lambda x, y: x + y,
                    '-': lambda x, y: x - y,
                    '*': lambda x, y: x * y,
                    '/': lambda x, y: x / y,
                    '%': lambda x, y: x % y,
                    '==': lambda x, y: x == y,
                    '!=': lambda x, y: x!= y,
                    '>': lambda x, y: x > y,
                    '<': lambda x, y: x < y,
                    '>=': lambda x, y: x >= y,
                    '<=': lambda x, y: x <= y,
                    '&': lambda x, y: x & y,
                    '|': lambda x, y: x | y,
                    '^': lambda x, y: x ^ y,
                    '<<': lambda x, y: x << y,
                    '>>': lambda x, y: x >> y,
                }[op](expr(left), expr(right))
            case 'list', items:
                return [expr(i) for i in items]
            case 'index', base, index:
                return expr(base)[expr(index)]
            case 'attr', base, attr:
                b = expr(base)
                v = b[attr]
                if isinstance(v, Func) or callable(v):
                    return Method(b, v)
                return v
            case 'call', fn, args:
                fn, args = expr(fn), [expr(arg) for arg in args]
                ismethod = False
                if isinstance(fn, Method):
                    prearg = fn.obj
                    ismethod = True
                    fn = fn.func
                if callable(fn):
                    return fn(*args)
                if isinstance(fn, Func):
                    old_scope = scope
                    scope = Scope(fn.closure)
                    scope.variables = dict(zip(fn.params, args))
                    if ismethod:
                        scope.define('self', prearg)
                    res = stmt(fn.body)
                    scope = old_scope
                    if isinstance(res, tuple):
                        return res[1]
                    return None
                raise BException(fn)
            case 'func', params, ret_tp, body:
                return Func(list(map(lambda x: x[0], params)), body, scope)
            case 'object', kvpairs:
                return {name: expr(val) for name, val in kvpairs}
            case 'null_list', tp:
                return []
            case 'new', tp, kvpairs:
                tp = type_eval(tp)
                res = {name: tp[name] for name in tp}
                for name, val in kvpairs:
                    res[name] = expr(val)
                return res

    def stmt(node):
        nonlocal scope
        match node:
            case 'block', stmts:
                for i in stmts:
                    ret = stmt(i)
                    if ret is not None:
                        return ret
            case 'noop':
                return
            case 'exprstmt', e:
                expr(e)
            case 'vardecl', variables:
                for name, val, tp in variables:
                    if val is not None:
                        val = expr(val)
                    scope.define(name, val)
            case 'if', cases, else_block:
                for cond, block in cases:
                    if expr(cond):
                        scope = Scope(scope)
                        ret = stmt(block)
                        scope = scope.parent
                        return ret
                scope = Scope(scope)
                ret = stmt(else_block)
                scope = scope.parent
                return ret
            case 'while', cond, block:
                while expr(cond):
                    scope = Scope(scope)
                    ret = stmt(block)
                    scope = scope.parent
                    if ret is not None and ret[0] == 'break':
                        break
                    if ret is not None and ret[0] == 'return':
                        return ret
            case 'break',:
                return 'break',
            case 'continue',:
                return 'continue',
            case 'return', val:
                return 'return', expr(val)
            case 'fndef', fname, params, ret_tp, body:
                scope.define(fname, Func(list(map(lambda x: x[0], params)), body, scope))
            case 'type', tname, tval:
                scope.define_type(tname, type_eval(tval))
            case 'typegen', tname, tparams, tval:
                scope.define_typegen(tname, tparams, tval)
            case 'assign', left, right:
                r = expr(right)
                if left[0] == 'id':
                    scope.set(left[1], r)
                elif left[0] == 'attr':
                    base = expr(left[1])
                    base[left[2]] = r
                elif left[0] == 'index':
                    base = expr(left[1])
                    index = expr(left[2])
                    base[index] = r
                else:
                    raise BException()
            
    def type_eval(node):
        nonlocal scope
        match node:
            case 'basic', name:
                if name in ('int', 'float', 'bool', 'str', 'NoneType'):
                    return name
                return scope.find_type(name)
            case 'template', name, targs:
                targs = [type_eval(targ) for targ in targs]
                tparams, tval = scope.find_typegen(name)
                if len(targs) != len(tparams):
                    raise BTypeError(f"Invalid number of type arguments: {name}, {targs}")
                scope = Scope(scope)
                scope.types = dict(zip(tparams, targs))
                res = type_eval(tval)
                scope = scope.parent
                return res
            case 'complex', ntvpairs:
                res = {}
                for name, tp, val in ntvpairs:
                    # tp = type_eval(tp)
                    if val:
                        res[name] = expr(val)
                    else:
                        res[name] = None
                return res
            case 'list', tp:
                return 'list', type_eval(tp)
            case 'func', ret_tp, *param_types:
                return 'func', type_eval(ret_tp), *map(type_eval, param_types)
    
    for i in prog:
        stmt(i)


check_scope = Scope(None)


def add_checker(name: str):
    """
    加入一点Rusp元素
    """
    def wrapper(func):
        check_scope.define(name, func)
    return wrapper


@add_checker('print')
def _b_print(*args):
    return 'NoneType'


@add_checker('println')
def _b_println(*args):
    return 'NoneType'


@add_checker('readln')
def _b_readln():
    return 'str'


@add_checker('ord')
def _b_ord(arg):
    assert arg == 'str'
    return 'int'


@add_checker('chr')
def _b_chr(arg):
    assert arg == 'int'
    return'str'


@add_checker('len')
def _b_len(arg):
    assert arg == 'str' or isinstance(arg, tuple) and arg[0] == 'list'
    return 'int'


run_scope = Scope(None)


def add_runner(name: str):
    def wrapper(func):
        run_scope.define(name, func)
    return wrapper


@add_runner('print')
def _b_print(*args):
    print(*args, sep='', end='', flush=True)


@add_runner('println')
def _b_println(*args):
    print(*args, sep='', flush=True)


add_runner('readln')(input)
add_checker('ord')(ord)
add_checker('chr')(chr)
add_checker('len')(len)


code = """
type Point<T> = {
    x: T,
    y: T,
    print = func () -> NoneType {
        println(self.x, " ", self.y);
    },
    getSum = func () -> T {
        return self.x + self.y;
    },
};

var p1 = new Point<int> {x: 1, y: 2};
var p2 = new Point<float> {x: 3.0, y: 4.0};
p1.print();
p2.print();
var p3 = p1.getSum();
println(p3);
var p4 = p2.getSum();
println(p4);
"""
tokens = tokenize(code)
prog = parse(tokens)
check(prog, check_scope)
# print(check_scope.variables)
# print(check_scope.types)
run(prog, run_scope)


"""
type Int = int;
type T = {
    x: Int,
    y: Int,
    getSum = func () -> Int {
        return self.x + self.y;
    },
};
var a = new T {x: 1, y: 2};
var b: T = a;
var c = a.x + b.y;
var d = a.getSum();
var e = [1, 2, 3];
var f = null_list<T>;
var g = e + e;
var h = "Hello, world!";


var a = readln();
var p = println;
p("Hello, world!");


func fac(num: int) -> int {
    if num == 0 {
        return 1;
    } else {
        return num * fac(num - 1);
    }
}

print(fac(10), "\\n");


type T = {
    a: int,
    print = func () -> NoneType {
        println(self.a);
    },
};

var a: T = new T { a: 1 };
println(a);
a.print();


var l = [[1, 2], [2, 4, 5]];
println(l);
l[1][0] = 3;
println(l);


type A = {
    a: int,
    printA = func () -> NoneType {
        println(self.a);
    },
    setA = func (a: int) -> NoneType {
        self.a = a;
    },
};

var a = new A {a: 1};
a.printA();
a.setA(2);
a.printA();


var i = 1;
var r = 1;
while i <= 10 {
    r = r * i;
    i = i + 1;
}
println(r);


var i = 0;
while True {
    i = i + 1;
    if i == 10 { break; }
    if i == 5 { continue; }
    println(i);
}


type Point<T> = {
    x: T,
    y: T,
    print = func () -> NoneType {
        println(self.x, " ", self.y);
    },
    getSum = func () -> T {
        return self.x + self.y;
    },
};

var p1 = new Point<int> {x: 1, y: 2};
var p2 = new Point<float> {x: 3.0, y: 4.0};
p1.print();
p2.print();
var p3 = p1.getSum();
println(p3);
var p4 = p2.getSum();
println(p4);
"""
