from typing import NamedTuple


class IError(Exception):
    pass


class IFatalError(IError):
    def __init__(self, msg: str, ln: int, col: int):
        super().__init__(f'{msg} at line {ln}, column {col}')


class IRuntimeError(IError):
    def __init__(self, msg: str):
        super().__init__(msg)


class ISyntaxError(IFatalError):
    pass


class INameError(IRuntimeError):
    pass


class Token(NamedTuple):
    val: str
    ln: int
    col: int


OPERATORS = {
    '+', '-', '*', '/', '%',
    '==', '!=', '>', '<', '>=', '<=',
    '<<', '>>', '&&', '||', '&', '|', '^',
    '!', '~', '(', ')', '[', ']', '{', '}',
    ',', '.', ';', ':', '=',
}

KEYWORDS = {
    'if', 'else', 'while',
    'try', 'catch', 'throw',
    'var', 'func', 'class',
    'module', 'yield', 'method', 'attr',
    'return', 'break', 'continue',
    'True', 'False', 'None',
}

PRIORITY = {
    '*': 100, '/': 100, '%': 100,
    '+': 99, '-': 99,
    '<<': 98, '>>': 98,
    '==': 97, '!=': 97,
    '>': 96, '<': 96, '>=': 96, '<=': 96,
    '&': 95, '^': 94, '|': 93,
    '&&': 92, '||': 91,
}

ESCAPES = {
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

BINARYS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '%': lambda x, y: x % y,
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y,
    '<': lambda x, y: x < y,
    '>': lambda x, y: x > y,
    '>=': lambda x, y: x >= y,
    '<=': lambda x, y: x <= y,
    '&&': lambda x, y: x and y,
    '||': lambda x, y: x or y,
    '&': lambda x, y: x & y,
    '|': lambda x, y: x | y,
    '^': lambda x, y: x ^ y,
}

UNARYS = {
    '+': lambda x: +x,
    '-': lambda x: -x,
    '!': lambda x: not x,
    '~': lambda x: ~x,
}


def tokenize(code: str) -> list:
    def next_char():
        nonlocal pos, ln, col
        if pos >= len(code):
            return None
        if code[pos] == '\n':
            ln += 1
            col = 1
        else:
            col += 1
        pos += 1

    res = []
    pos = 0
    ln, col = 1, 1

    while pos < len(code):
        while pos < len(code) and (code[pos].isspace() or code[pos: pos + 2] in ('//', '/*')):
            if code[pos: pos + 2] == '//':
                while pos < len(code) and code[pos] != '\n':
                    next_char()
            elif code[pos: pos + 2] == '/*':
                next_char()
                next_char()
                while pos < len(code) and not (code[pos: pos + 2] == '*/'):
                    next_char()
                if pos < len(code):
                    next_char()
                    next_char()
                else:
                    raise ISyntaxError('unclosed comment', ln, col)
            else:
                next_char()

        if pos >= len(code):
            break
        elif code[pos].isdigit():
            val = ''
            tpos = ln, col
            while pos < len(code) and (code[pos].isdigit() or code[pos] == '.'):
                val += code[pos]
                next_char()
            if val.count('.') > 1:
                raise ISyntaxError(f'invalid number {val}', ln, col)
            res.append(Token(val, *tpos))
        elif code[pos].isalpha() or code[pos] == '_':
            val = ''
            tpos = ln, col
            while pos < len(code) and (code[pos].isalpha() or code[pos] == '_'):
                val += code[pos]
                next_char()
            if val in KEYWORDS:
                res.append(Token('*' + val, *tpos))
            else:
                res.append(Token(val, *tpos))
        elif code[pos] in '\'"':
            tpos = ln, col
            x = code[pos]
            next_char()
            val = '"'
            while pos < len(code) and code[pos] != x:
                if code[pos] == '\\':
                    next_char()
                    if pos >= len(code):
                        raise ISyntaxError('unclosed string', ln, col)
                    if code[pos] in ESCAPES:
                        val += ESCAPES[code[pos]]
                        next_char()
                    elif code[pos] == 'x':
                        next_char()
                        if pos + 2 >= len(code):
                            raise ISyntaxError('invalid hex escape sequence', ln, col)
                        try:
                            val += chr(int(code[pos: pos + 2], 16))
                        except ValueError:
                            raise ISyntaxError('invalid hex escape sequence', ln, col)
                        next_char()
                        next_char()
                    elif code[pos] == 'u':
                        next_char()
                        if pos + 4 >= len(code):
                            raise ISyntaxError('invalid unicode escape sequence', ln, col)
                        try:
                            val += chr(int(code[pos: pos + 4], 16))
                        except ValueError:
                            raise ISyntaxError('invalid unicode escape sequence', ln, col)
                        next_char()
                        next_char()
                        next_char()
                        next_char()
                    else:
                        raise ISyntaxError(f'invalid escape sequence \\{code[pos]}', ln, col)
                else:
                    val += code[pos]
                    next_char()
            if pos >= len(code):
                raise ISyntaxError('unclosed string', ln, col)
            next_char()
            res.append(Token(val, *tpos))
        elif code[pos: pos + 2] in OPERATORS:
            tpos = ln, col
            val = code[pos: pos + 2]
            next_char()
            next_char()
            res.append(Token(val, *tpos))
        elif code[pos] in OPERATORS:
            tpos = ln, col
            val = code[pos]
            next_char()
            res.append(Token(val, *tpos))
        else:
            raise ISyntaxError(f'invalid character {code[pos]}', ln, col)

    res.append(Token('', ln, col))
    return res


def parse(tokens: list):
    token = tokens[0]
    pos = 0

    def eat(expect=None):
        nonlocal token, pos
        if expect is None or token.val == expect:
            pos += 1
            token = tokens[pos]
            return tokens[pos - 1]
        raise ISyntaxError(f"unexpected token '{token.val}', expected '{expect}'", token.ln, token.col)

    def eat_id():
        nonlocal token, pos
        if not token.val or not (token.val[0].isalpha() or token.val[0] == '_'):
            raise ISyntaxError(f"unexpected token '{token.val}', expected an identifier", token.ln, token.col)
        pos += 1
        token = tokens[pos]
        return tokens[pos - 1]

    def parse_expr() -> Expr:
        res = [parse_factor()]
        stack = []
        while token.val in PRIORITY:
            op = eat().val
            while stack and PRIORITY[stack[-1]] >= PRIORITY[op]:
                r, l = res.pop(), res.pop()
                res.append(Binary(stack.pop(), l, r))
            stack.append(op)
            res.append(parse_factor())
        while stack:
            r, l = res.pop(), res.pop()
            res.append(Binary(stack.pop(), l, r))
        return res[0]

    def parse_factor() -> Expr:
        if not token.val:
            raise ISyntaxError('unexpected EOF', token.ln, token.col)
        elif token.val[0].isdigit():
            if '.' in token.val:
                res = Const(float(eat().val))
            else:
                res = Const(int(eat().val))
        elif token.val[0].isalpha() or token.val[0] == '_':
            res = VarExpr(eat().val)
        elif token.val[0] == '"':
            res = Const(eat().val[1:])
        elif token.val == '*True':
            eat()
            res = Const(True)
        elif token.val == '*False':
            eat()
            res = Const(False)
        elif token.val == '*None':
            eat()
            res = Const(None)
        elif token.val == '(':
            eat('(')
            res = parse_expr()
            eat(')')
        elif token.val == '[':
            eat()
            items = []
            while token.val != ']':
                items.append(parse_expr())
                if token.val != ']':
                    eat(',')
            res = BuildList(items)
            eat()
        elif token.val == '{':
            eat()
            kvpairs = []
            while token.val != '}':
                key = parse_expr()
                eat(':')
                val = parse_expr()
                kvpairs.append((key, val))
                if token.val != '}':
                    eat(',')
            res = BuildDict(kvpairs)
            eat()
        elif token.val in UNARYS:
            op = eat().val
            res = Unary(op, parse_factor())
        elif token.val == '*func':
            eat()
            params = []
            eat('(')
            while token.val != ')':
                params.append(eat_id().val)
                if token.val != ')':
                    eat(',')
            eat()
            body = parse_block()
            res = Lambda(params, body)
        else:
            raise ISyntaxError(f"unexpected token '{token.val}'", token.ln, token.col)

        while True:
            if token.val == '[':
                eat()
                res = Index(res, parse_expr())
                eat(']')
            elif token.val == '.':
                eat()
                res = Attr(res, eat_id().val)
            elif token.val == '(':
                eat()
                args = []
                if token.val != ')':
                    while token.val != ')':
                        args.append(parse_expr())
                        if token.val != ')':
                            eat(',')
                res = Call(res, args)
                eat(')')
            else:
                break
        return res

    def parse_stmt() -> Stmt:
        if token.val == ';':
            eat()
            return NoOp()
        elif token.val == '*if':
            eat()
            cases = []
            while True:
                cond = parse_expr()
                body = parse_block()
                cases.append((cond, body))
                if token.val != '*else':
                    return IfStmt(cases, Block([]))
                eat()
                if token.val != '*if':
                    return IfStmt(cases, parse_block())
                eat()
        elif token.val == '*while':
            eat()
            cond = parse_expr()
            body = parse_block()
            return WhileStmt(cond, body)
        elif token.val == '*break':
            eat()
            eat(';')
            return Break()
        elif token.val == '*continue':
            eat()
            eat(';')
            return Continue()
        elif token.val == '*return':
            eat()
            if token.val == ';':
                eat()
                return Return(Const(None))
            else:
                ret = parse_expr()
                eat(';')
                return Return(ret)
        elif token.val == '*var':
            eat()
            vars = []
            while token.val != ';':
                name = eat_id().val
                if token.val == '=':
                    eat()
                    val = parse_expr()
                else:
                    val = Const(None)
                vars.append((name, val))
                if token.val != ';':
                    eat(',')
            eat()
            return VarDecl(vars)
        elif token.val == '*func' and tokens[pos + 1].val != '(':
            eat()
            name = eat_id()
            params = []
            eat('(')
            while token.val != ')':
                params.append(eat_id().val)
                if token.val != ')':
                    eat(',')
            eat()
            body = parse_block()
            return FuncDecl(name.val, params, body)
        elif token.val == '*class':
            eat()
            tname = eat_id()
            parents = []
            if token.val == ':':
                eat()
                while token.val != '{':
                    parents.append(parse_expr())
                    if token.val != '{':
                        eat(',')
            eat('{')
            decls = []
            while token.val != '}':
                if token.val == ';':
                    eat(';')
                elif token.val == '*attr':
                    eat()
                    attrs = []
                    while token.val != ';':
                        name = eat_id()
                        if token.val == '=':
                            eat()
                            val = parse_expr()
                        else:
                            val = Const(None)
                        attrs.append((name.val, val))
                        if token.val != ';':
                            eat(',')
                    eat(';')
                    decls.append(AttrDecl(name.val, attrs))
                elif token.val == '*method':
                    eat()
                    name = eat_id()
                    params = []
                    eat('(')
                    while token.val != ')':
                        params.append(eat_id().val)
                        if token.val != ')':
                            eat(',')
                    eat()
                    body = parse_block()
                    decls.append(MethodDecl(name.val, params, body))
                else:
                    raise ISyntaxError(f"unexpected token '{token.val}' in class declaration", token.ln, token.col)
            eat()
            return ClassDecl(tname.val, parents, decls)
        elif token.val == '*module':
            eat()
            name = eat_id()
            body = parse_block()
            return ModuleDecl(name.val, body)
        elif token.val == '*try':
            ln, col = token.ln, token.col
            eat()
            try_block = parse_block()
            catchs: list[tuple[str, list[str], Block]] = []
            while token.val == '*catch':
                eat()
                exname = eat_id().val
                extnames = []
                while token.val != '{':
                    extnames.append(eat_id().val)
                    if token.val != '{':
                        eat(',')
                exbody = parse_block()
                catchs.append((exname, extnames, exbody))
            if not catchs:
                eat('*catch')
            checkset = set()
            for exname, extnames, exbody in catchs:
                for extname in extnames:
                    if extname in checkset:
                        raise ISyntaxError("conflicted catch-blocks", ln, col)
            return TryCatch(try_block, catchs)
        elif token.val == '*throw':
            eat()
            err = parse_expr()
            eat(';')
            return Throw(err)
        else:
            ln, col = token.ln, token.col
            left = parse_expr()
            if token.val == '=':
                eat()
                if not (isinstance(left, VarExpr) or isinstance(left, Attr) or isinstance(left, Index)):
                    raise ISyntaxError(f"unexpected l-value", ln, col)
                right = parse_expr()
                eat(';')
                return Assign(left, right)
            eat(';')
            return ExprStmt(left)

    def parse_block() -> Block:
        eat('{')
        stmts = []
        while token.val != '}':
            stmts.append(parse_stmt())
        eat('}')
        return Block(stmts)

    prog = []
    while token.val:
        prog.append(parse_stmt())
    return Block(prog)


class Scope:
    def __init__(self, parent=None):
        self.parent = parent
        self.vars = {}

    def find(self, name: str):
        if name in self.vars:
            return self.vars[name]
        elif self.parent is not None:
            return self.parent.find(name)
        else:
            raise INameError(f"name '{name}' is not defined")

    def set(self, name: str, val):
        if name in self.vars:
            self.vars[name] = val
        elif self.parent is not None:
            self.parent.set(name, val)
        else:
            raise INameError(f"name '{name}' is not defined")

    def define(self, name: str, val):
        self.vars[name] = val


class Func:
    def __init__(self, params: list, closure: Scope, pc: int):
        self.params, self.closure, self.pc = params, closure, pc


class IClass:
    def __init__(self, name: str, parents, attrs: dict):
        self.name, self.parents, self.attrs = name, parents, attrs

    def getattr(self, name: str):
        if name in self.attrs:
            return self.attrs[name]
        for parent in self.parents:
            try:
                return parent.getattr(name)
            except IRuntimeError:
                pass
        raise IRuntimeError(f'undefined attribute {name}')

    def setattr(self, name: str, val):
        self.attrs[name] = val


class IObject:
    def __init__(self, tp: IClass):
        self.tp = tp
        self.attrs = {}

    def getattr(self, name: str):
        if name in self.attrs:
            res = self.attrs[name]
        else:
            res = self.tp.getattr(name)
            self.attrs[name] = res
        if isinstance(res, Func) or isinstance(res, IMethod) or callable(res):
            return IMethod(self, res)
        return res

    def setattr(self, name: str, val):
        self.attrs[name] = val


class IMethod:
    def __init__(self, obj: IObject, func):
        self.obj, self.func = obj, func


class IModule:
    def __init__(self, name: str, attrs: dict):
        self.name, self.attrs = name, attrs

    def getattr(self, name: str):
        return self.attrs[name]

    def setattr(self, name: str, val):
        self.attrs[name] = val


class RunStatus(NamedTuple):
    jmpmap: dict
    sp: int
    scope: Scope
    csp: int


class RunEnv:
    def __init__(self, code):
        self.code = code
        self.scope = Scope()
        self.pc = 0
        self.stack = []
        self.call_stack: list[tuple[Scope, int]] = []
        self.try_stack: list[RunStatus] = []

    def run(self):
        while self.pc < len(self.code):
            # print(self.pc, self.code[self.pc])
            try:
                self.code[self.pc].do(self)
            except IRuntimeError as e:
                self.traceback(e)
            self.pc += 1

    def traceback(self, exc):
        if isinstance(exc, IObject):
            extname = exc.tp.name
        elif isinstance(exc, IClass):
            extname = 'type'
        elif isinstance(exc, IModule):
            extname = 'module'
        elif isinstance(exc, IMethod):
            extname = 'method'
        elif isinstance(exc, Func):
            extname = 'func'
        else:
            extname = type(exc).__name__
        while self.try_stack:
            jmpmap, sp, scope, csp = self.try_stack.pop()
            if extname in jmpmap or '' in jmpmap:
                if '' in jmpmap:
                    extname = ''
                self.pc = jmpmap[extname] - 1
                del self.stack[sp:]
                self.scope = scope
                del self.call_stack[csp:]
                break
        else:
            raise IFatalError(f"unresolved runtime error '{exc}'", -1, -1)
        self.stack.append(exc)


class ByteCode:
    def do(self, e: RunEnv):
        pass

    def __str__(self):
        return type(self).__name__ + str(self.__dict__)

    def __repr__(self):
        return type(self).__name__ + str(self.__dict__)


class OpPush(ByteCode):
    def __init__(self, value):
        self.value = value

    def do(self, e: RunEnv):
        e.stack.append(self.value)


class OpPop(ByteCode):
    def do(self, e: RunEnv):
        e.stack.pop()


class OpBinary(ByteCode):
    def __init__(self, op: str):
        self.op = op

    def do(self, e: RunEnv):
        right = e.stack.pop()
        left = e.stack.pop()
        e.stack.append(BINARYS[self.op](left, right))


class OpUnary(ByteCode):
    def __init__(self, op: str):
        self.op = op

    def do(self, e: RunEnv):
        val = e.stack.pop()
        e.stack.append(UNARYS[self.op](val))


class OpGroupJmp(ByteCode):
    def __init__(self, pos: int):
        self.pos = pos


class OpJmp(OpGroupJmp):
    def do(self, e: RunEnv):
        e.pc = self.pos - 1


class OpJz(OpGroupJmp):
    def do(self, e: RunEnv):
        if e.stack.pop():
            e.pc = self.pos - 1


class OpJnz(OpGroupJmp):
    def do(self, e: RunEnv):
        if not e.stack.pop():
            e.pc = self.pos - 1


class OpCall(ByteCode):
    def __init__(self, nargs: int):
        self.nargs = nargs

    def do(self, e: RunEnv):
        args = []
        for _ in range(self.nargs):
            args.append(e.stack.pop())
        func = e.stack.pop()
        # 抽象，比2022的Assign逻辑还抽象
        while True:
            if isinstance(func, IMethod):
                args.append(func.obj)
                func = func.func
            elif isinstance(func, IClass):
                args.append(IObject(func))
                try:
                    # 这就需要__init__里手写return self
                    func = func.getattr("__init__")
                except:
                    e.stack.append(args[-1])
                    return
            else:
                break
        args = list(reversed(args))
        if isinstance(func, Func):
            e.call_stack.append((e.scope, e.pc))
            e.scope = Scope(func.closure)
            e.scope.vars = dict(zip(func.params, args))
            e.pc = func.pc - 1
        elif callable(func):
            e.stack.append(func(*args))
        else:
            raise IRuntimeError(f"unexpected function for call")


class OpReturn(ByteCode):
    def do(self, e: RunEnv):
        e.scope, e.pc = e.call_stack.pop()


class OpLoadIndex(ByteCode):
    def do(self, e: RunEnv):
        index = e.stack.pop()
        base = e.stack.pop()
        e.stack.append(base[index])


class OpSetIndex(ByteCode):
    def do(self, e: RunEnv):
        val = e.stack.pop()
        index = e.stack.pop()
        base = e.stack.pop()
        base[index] = val


class OpLoadAttr(ByteCode):
    def __init__(self, name: str):
        self.name = name

    def do(self, e: RunEnv):
        base = e.stack.pop()
        if not (isinstance(base, IObject) or isinstance(base, IModule) or isinstance(base, IClass)):
            raise IRuntimeError(f'expected an object')
        e.stack.append(base.getattr(self.name))


class OpSetAttr(ByteCode):
    def __init__(self, name: str):
        self.name = name

    def do(self, e: RunEnv):
        val = e.stack.pop()
        base = e.stack.pop()
        if not (isinstance(base, IObject) or isinstance(base, IModule) or isinstance(base, IClass)):
            raise IRuntimeError(f'expected an object')
        base.setattr(self.name, val)


class OpLoadVar(ByteCode):
    def __init__(self, name: str):
        self.name = name

    def do(self, e: RunEnv):
        e.stack.append(e.scope.find(self.name))


class OpSetVar(ByteCode):
    def __init__(self, name: str):
        self.name = name

    def do(self, e: RunEnv):
        val = e.stack.pop()
        e.scope.set(self.name, val)


class OpBuildList(ByteCode):
    def __init__(self, nitems: int):
        self.nitems = nitems

    def do(self, e: RunEnv):
        if self.nitems:
            res = e.stack[-self.nitems:]
            del e.stack[-self.nitems:]
            e.stack.append(res)
        else:
            e.stack.append([])


class OpBuildDict(ByteCode):
    def __init__(self, nitems: int):
        self.nitems = nitems

    def do(self, e: RunEnv):
        if self.nitems:
            vals = e.stack[-self.nitems:]
            del e.stack[-self.nitems:]
            keys = e.stack[-self.nitems:]
            del e.stack[-self.nitems:]
            e.stack.append(dict(zip(keys, vals)))
        else:
            e.stack.append({})


class OpBuildFunc(ByteCode):
    def __init__(self, params: list, pos: int):
        self.params, self.pos = params, pos

    def do(self, e: RunEnv):
        e.stack.append(Func(self.params, e.scope, self.pos))


class OpDefClass(ByteCode):
    def __init__(self, name: str, nparents: int, attrks):
        self.name, self.nparents, self.attrks = name, nparents, attrks

    def do(self, e: RunEnv):
        if self.nparents:
            parents = e.stack[-self.nparents:]
            del e.stack[-self.nparents:]
        else:
            parents = []
        attrvs = e.stack[-len(self.attrks):]
        del e.stack[-len(self.attrks):]
        attrs = dict(zip(self.attrks, attrvs))
        e.scope.define(self.name, IClass(self.name, parents, attrs))


class OpDefVar(ByteCode):
    def __init__(self, name: str):
        self.name = name

    def do(self, e: RunEnv):
        e.scope.define(self.name, e.stack.pop())


class OpInScope(ByteCode):
    def do(self, e: RunEnv):
        e.scope = Scope(e.scope)


class OpOutScope(ByteCode):
    def do(self, e: RunEnv):
        if e.scope.parent:
            e.scope = e.scope.parent
        else:
            raise IFatalError("", -1, -1)


class OpDefModule(ByteCode):
    def __init__(self, name: str):
        self.name = name

    def do(self, e: RunEnv):
        assert e.scope.parent
        e.scope.parent.define(self.name, IModule(self.name, e.scope.vars))


class OpTryCatch(ByteCode):
    def __init__(self, jmpmap: dict):
        self.jmpmap = jmpmap

    def do(self, e: RunEnv):
        e.try_stack.append(RunStatus(self.jmpmap, len(e.stack), e.scope, len(e.call_stack)))


class OpOutTry(ByteCode):
    def do(self, e: RunEnv):
        e.try_stack.pop()


class OpThrow(ByteCode):
    def do(self, e: RunEnv):
        err = e.stack.pop()
        e.traceback(err)


class Compiler:
    def __init__(self):
        self.output: list = []
        self.while_jmpends: list = []
        self.while_begins: list[int] = []

    def add(self, *bytecodes: ByteCode):
        self.output.extend(bytecodes)

    def print_code(self):
        for i, code in enumerate(self.output):
            print(i, code)


class Expr:
    def compile(self, c: Compiler):
        pass

    def __str__(self):
        return type(self).__name__ + str(self.__dict__)

    def __repr__(self):
        return type(self).__name__ + str(self.__dict__)


class Stmt:
    def compile(self, c: Compiler):
        pass

    def __str__(self):
        return type(self).__name__ + str(self.__dict__)

    def __repr__(self):
        return type(self).__name__ + str(self.__dict__)


class NoOp(Stmt):
    pass


class ExprStmt(Stmt):
    def __init__(self, expr: Expr):
        self.expr = expr

    def compile(self, c: Compiler):
        self.expr.compile(c)
        c.add(OpPop())


class Block(Stmt):
    def __init__(self, stmts: list):
        self.stmts = stmts

    def compile(self, c: Compiler):
        for stmt in self.stmts:
            stmt.compile(c)


class IfStmt(Stmt):
    def __init__(self, cases: list, defc: Block):
        self.cases, self.defc = cases, defc

    # 虽然但是，复杂控制流编译仍然使用betterlang的逻辑
    def compile(self, c: Compiler):
        jmpends: list = []
        for cond, body in self.cases:
            cond.compile(c)
            jnz = OpJnz(0)
            c.add(jnz)
            c.add(OpInScope())
            body.compile(c)
            c.add(OpOutScope())
            jmpends.append(OpJmp(0))
            c.add(jmpends[-1])
            jnz.pos = len(c.output)
        c.add(OpInScope())
        self.defc.compile(c)
        c.add(OpOutScope())
        for i in jmpends:
            i.pos = len(c.output)


class WhileStmt(Stmt):
    def __init__(self, cond: Expr, body: Block):
        self.cond, self.body = cond, body

    def compile(self, c: Compiler):
        c.while_begins.append(len(c.output))
        self.cond.compile(c)
        c.while_jmpends.append([])
        c.while_jmpends[-1].append(OpJnz(0))
        c.add(c.while_jmpends[-1][-1])
        c.add(OpInScope())
        self.body.compile(c)
        c.add(OpOutScope())
        c.add(OpJmp(c.while_begins[-1]))
        for jmp in c.while_jmpends[-1]:
            jmp.pos = len(c.output)
        c.while_begins.pop()
        c.while_jmpends.pop()


class Break(Stmt):
    def compile(self, c: Compiler):
        c.while_jmpends[-1].append(OpJmp(0))
        c.add(c.while_jmpends[-1][-1])


class Continue(Stmt):
    def compile(self, c: Compiler):
        c.add(OpJmp(c.while_begins[-1]))


class Assign(Stmt):
    def __init__(self, left: Expr, right: Expr):
        self.left, self.right = left, right

    def compile(self, c: Compiler):
        self.left.compile(c)
        last = c.output.pop()
        self.right.compile(c)
        if isinstance(last, OpLoadVar):
            c.output.append(OpSetVar(last.name))
        elif isinstance(last, OpLoadIndex):
            c.output.append(OpSetIndex())
        elif isinstance(last, OpLoadAttr):
            c.output.append(OpSetAttr(last.name))
        else:
            raise IFatalError("", -1, -1)


class FuncDecl(Stmt):
    def __init__(self, name: str, params: list, body: Block):
        self.name, self.params, self.body = name, params, body

    def compile(self, c: Compiler):
        c.add(OpBuildFunc(self.params, len(c.output) + 3))
        c.add(OpDefVar(self.name))
        jmp = OpJmp(0)
        c.add(jmp)
        self.body.compile(c)
        c.add(OpPush(None))
        c.add(OpReturn())
        jmp.pos = len(c.output)


class Return(Stmt):
    def __init__(self, expr: Expr):
        self.expr = expr

    def compile(self, c: Compiler):
        self.expr.compile(c)
        c.add(OpReturn())


class VarDecl(Stmt):
    def __init__(self, vars: list):
        self.vars = vars

    def compile(self, c: Compiler):
        for name, val in self.vars:
            val.compile(c)
            c.add(OpDefVar(name))


class Decl:
    def compile(self, c: Compiler, attrlist: list):
        pass

    def __str__(self):
        return type(self).__name__ + str(self.__dict__)

    def __repr__(self):
        return type(self).__name__ + str(self.__dict__)


class ClassDecl(Stmt):
    def __init__(self, name: str, parents: list, decls: list):
        self.name, self.parents, self.decls = name, parents, decls

    def compile(self, c: Compiler):
        attrlist: list = []
        for decl in self.decls:
            decl.compile(c, attrlist)
        for parent in self.parents:
            parent.compile(c)
        c.add(OpDefClass(self.name, len(self.parents), attrlist))


class AttrDecl(Decl):
    def __init__(self, name: str, attrs: list):
        self.name, self.attrs = name, attrs

    def compile(self, c: Compiler, attrlist: list):
        for name, val in self.attrs:
            val.compile(c)
            attrlist.append(name)


class MethodDecl(Decl):
    def __init__(self, name: str, params: list, body: Block):
        self.name, self.params, self.body = name, params, body

    def compile(self, c: Compiler, attrlist: list):
        attrlist.append(self.name)
        c.add(OpBuildFunc(self.params, len(c.output) + 2))
        jmp = OpJmp(0)
        c.add(jmp)
        self.body.compile(c)
        c.add(OpPush(None))
        c.add(OpReturn())
        jmp.pos = len(c.output)


class ModuleDecl(Stmt):
    def __init__(self, name: str, body: Block):
        self.name, self.body = name, body

    def compile(self, c: Compiler):
        c.add(OpInScope())
        self.body.compile(c)
        c.add(OpDefModule(self.name))
        c.add(OpOutScope())


class TryCatch(Stmt):
    def __init__(self, try_block: Block, catchs: list):
        self.try_block, self.catchs = try_block, catchs

    def compile(self, c: Compiler):
        jmpmap = {}
        c.add(OpTryCatch(jmpmap))
        c.add(OpInScope())
        self.try_block.compile(c)
        c.add(OpOutScope())
        c.add(OpOutTry())
        jmpends = [OpJmp(0)]
        c.add(jmpends[-1])
        for exname, extnames, block in self.catchs:
            if not extnames:
                jmpmap[''] = len(c.output)
            for extname in extnames:
                jmpmap[extname] = len(c.output)
            c.add(OpInScope())
            c.add(OpDefVar(exname))
            block.compile(c)
            c.add(OpOutScope())
            jmpends.append(OpJmp(0))
            c.add(jmpends[-1])
        for jmp in jmpends:
            jmp.pos = len(c.output)


class Throw(Stmt):
    def __init__(self, err: Expr):
        self.err = err

    def compile(self, c: Compiler):
        self.err.compile(c)
        c.add(OpThrow())


class Const(Expr):
    def __init__(self, val):
        self.val = val

    def compile(self, c: Compiler):
        c.add(OpPush(self.val))


class VarExpr(Expr):
    def __init__(self, name: str):
        self.name = name

    def compile(self, c: Compiler):
        c.add(OpLoadVar(self.name))


class Binary(Expr):
    def __init__(self, op: str, left: Expr, right: Expr):
        self.op, self.left, self.right = op, left, right

    def compile(self, c: Compiler):
        self.left.compile(c)
        self.right.compile(c)
        c.add(OpBinary(self.op))


class Unary(Expr):
    def __init__(self, op: str, val: Expr):
        self.op, self.val = op, val

    def compile(self, c: Compiler):
        self.val.compile(c)
        c.add(OpUnary(self.op))


class BuildList(Expr):
    def __init__(self, items: list):
        self.items = items

    def compile(self, c: Compiler):
        for item in self.items:
            item.compile(c)
        c.add(OpBuildList(len(self.items)))


class Index(Expr):
    def __init__(self, base: Expr, index: Expr):
        self.base, self.index = base, index

    def compile(self, c: Compiler):
        self.base.compile(c)
        self.index.compile(c)
        c.add(OpLoadIndex())


class Lambda(Expr):
    def __init__(self, params: list, body: Block):
        self.params, self.body = params, body

    def compile(self, c: Compiler):
        c.add(OpBuildFunc(self.params, len(c.output) + 2))
        jmp = OpJmp(0)
        c.add(jmp)
        self.body.compile(c)
        c.add(OpPush(None))
        c.add(OpReturn())
        jmp.pos = len(c.output)


class BuildDict(Expr):
    def __init__(self, items: list):
        self.items = items

    def compile(self, c: Compiler):
        for k, v in self.items:
            k.compile(c)
            v.compile(c)
        c.add(OpBuildDict(len(self.items)))


class Call(Expr):
    def __init__(self, func: Expr, args: list):
        self.func, self.args = func, args

    def compile(self, c: Compiler):
        self.func.compile(c)
        for arg in self.args:
            arg.compile(c)
        c.add(OpCall(len(self.args)))


class Attr(Expr):
    def __init__(self, obj: Expr, attr: str):
        self.obj, self.attr = obj, attr

    def compile(self, c: Compiler):
        self.obj.compile(c)
        c.add(OpLoadAttr(self.attr))


code = """
try {
    func(s) { println(s); throw s; } ("Hello!");
} catch err {
    println("Err: ", err);
}
"""

tokens = tokenize(code)
ast = parse(tokens)
# print(ast)
compiler = Compiler()
ast.compile(compiler)
assert compiler.while_begins == [] and compiler.while_jmpends == []
# compiler.print_code()
runner = RunEnv(compiler.output)
runner.scope.vars = {
    "print": lambda *args: print(*args, end="", flush=True, sep=""),
    "println": lambda *args: print(*args, flush=True, sep=""),
    "readln": input,
    "ord": ord,
    "chr": chr,
    "len": len,
}
runner.run()

"""
func hello(name) {
    println("Hello, ", name, "!");
}
hello("world");
hello("integer3.3");


println(1 + 2 * 3, " ", (1 + 2) * 3);


var i = 1, res = 1;
while i <= 10 {
    res = res * i;
    i = i + 1;
}
println(res);


func fac(num) {
    if num == 1 {
        return 1;
    } else {
        return fac(num - 1) * num;
    }
}
println(fac(10));


if 1 {
    println(1);
} else if 2 {
    println(2);
} else {
    println(3);
}


var i = 0;
while True {
    i = i + 1;
    if i == 10 {
        break;
    }
    if i == 5 {
        continue;
    }
    println(i);
}


class T {
    attr a;
    method __init__(self, a) {
        self.a = a;
        return self;
    }
    method print(self) {
        println(self.a);
    }
    method set(self, a) {
        self.a = a;
    }
}
var t = T(1);
t.print();
t.set(2);
t.print();


module A {
    var pi = 3.14;
    func getPi() { return pi; }
}

println(A.pi);
println(A.getPi());


func Counter(start) {
    return func() {
        start = start + 1;
        return start;
    };
}
var c = Counter(0);
println(c()); // 1
println(c()); // 2
println(c()); // 3


try {
    func(s) { println(s); throw s; } ("Hello!");
} catch err {
    println("Err: ", err);
}
"""
