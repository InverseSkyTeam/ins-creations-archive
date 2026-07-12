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

    __hash__ = lambda self: hash(str(self))

    def __eq__(self, b):
        return type(b) == LispSym and b.name == self.name
        

class tl_tokenize:
    from typing import NamedTuple
    import re
    
    
    class Token(NamedTuple):
        tp: str
        value: str
        ln: int
        col: int
    
    
    def tokenize(code: str):
        keywords = [
            'if',
            'define',
            'lambda',
            'macro',
            'quote',
            'set!',
            'begin'
        ]
        syntax = {
            'COMMENT': r';[^\n]*',
            'NUM': r'\d+(\.\d*)?',
            'STRING': r'\"([^"\n\\]|(\\([rtafvbn\\\'\"]|[0-9][0-9][0-9])))*\"',
            'ID': r'[^0-9\s\'\(\),\"][^\s\(\)\";]*',
            'NEWLINE': r'\n',
            'SKIP': r'[ \t]+',
            'LPAREN': r'\(',
            'RPAREN': r'\)',
            'QUOTE': r"'",
            'NOQUOTE': r',',
            'OTHERS': r'.'
        }
        regex = '|'.join('(?P<%s>%s)' % pair for pair in syntax.items())
        ln = 0
        ln_start = 0
        for mo in re.finditer(regex, code):
            tp = mo.lastgroup
            value = mo.group()
            col = mo.start() - ln_start
            if tp == "NUM":
                yield tl_tokenize.Token(tp, value, ln, col)
            elif tp == 'ID' and value in keywords:
                yield tl_tokenize.Token('KEYWORD', value, ln, col)
            elif tp == 'ID':
                yield tl_tokenize.Token(tp, value, ln, col)
            elif tp in ('LPAREN', 'RPAREN', 'QUOTE', 'NOQUOTE'):
                yield tl_tokenize.Token(tp, value, ln, col)
            elif tp == 'STRING':
                yield tl_tokenize.Token(tp, value, ln, col)
            elif tp == 'NEWLINE':
                ln_start = mo.end()
                ln += 1
                continue
            elif tp == 'SKIP':
                continue
            # else:
            #     raise Exception((ln, col))


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
    
    def run_file(self, filename: str):
        self.run_code(open(filename, 'r', encoding='utf-8').read())

    def run(self, ast):
        if type(ast) == LispSym:
            return self.find(ast.name)
        elif type(ast) in (int, float, str):
            return ast
        elif type(ast) == NoQuote:
            raise Exception("Error!")
        elif type(ast) == Quote:
            if type(ast.items) != list:
                return ast.items
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
            if type(func) == dict:
                attr = self.run(args[0])
                return func[attr]
            if type(func) == list:
                return func[self.run(args[0])]
            args = [self.run(i) for i in args]
            return func(*args)
        else:
            raise Exception("Error!")


class Function:
    def __init__(self, para: list, body: list, closure):
        self.para, self.body, self.closure = para, body, closure

    def __call__(self, *args):
        return Scope(self.closure, dict(zip(self.para, args))).run_ast(self.body)


class Macro:
    def __init__(self, func):
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


def _dict(lst: list):
    return dict(lst)


@newBuiltinMacro
def _for(scope: Scope, varname: LispSym, begin, end, step, *body):
    body = list(body)
    varname = varname.name
    begin = scope.run(begin)
    end = scope.run(end)
    step = scope.run(step)
    r = []
    for i in range(begin, end, step):
        r.append(Scope(scope, {varname: i}).run_ast(body))
    return r


@newBuiltinMacro
def _foreach(scope: Scope, varname: LispSym, obj, *body):
    body = list(body)
    varname = varname.name
    obj = scope.run(obj)
    r = []
    for i in obj:
        r.append(Scope(scope, {varname: i}).run_ast(body))
    return r


scope = Scope(None, {
    "print": lambda *args: print(*args, sep="", end="", flush=True),
    "car": lambda arg: arg[0],
    "cdr": lambda arg: arg[1:],
    "set-car!": set_car_force,
    "set-cdr!": set_cdr_force,
    "nth": lambda a, n: a[n],
    "set-nth!": set_nth_force,
    "dict": _dict,
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
    "for": _for,
    "foreach": _foreach,
})


class highlight_with_regex:
    from typing import NamedTuple
    import re
    import sys
    import copy
    
    def gotoxy(y: int, x: int):  # y: ln, x: col
        print(f"\033[{y};{x}f", end="", flush=True)
    
    
    class Token(NamedTuple):
        tp: str
        color: str
        value: str
        ln: int
        col: int
    
    
    def flatten_list(lst):
        res = []
        for i in lst:
            res.extend(i)
        return res
    
    
    builtins = copy.deepcopy(list(scope.var.keys()))
    
    
    def tokenize(code: str):
        # sym_table = [[]]  # Test
        keywords = [
            'if',
            'define',
            'lambda',
            'macro',
            'quote',
            'set!',
            'begin'
        ]
        syntax = {
            'COMMENT': r';[^\n]*',
            'NUM': r'\d+(\.\d*)?',
            'STRING': r'\"([^"\n\\]|(\\([rtafvbn\\\'\"]|[0-9][0-9][0-9])))*\"',
            'ID': r'[^0-9\s\'\(\),\"][^\s\(\)\";]*',
            'NEWLINE': r'\n',
            'SKIP': r'[ \t]+',
            'LPAREN': r'\(',
            'RPAREN': r'\)',
            'QUOTE': r"'",
            'NOQUOTE': r',',
            'OTHERS': r'.'
        }
        paren_color = [
            "\033[1;0m",
            "\033[1;31m",
            "\033[1;94m",
            "\033[1;35m",
            "\033[1;36m"
        ]
        regex = '|'.join('(?P<%s>%s)' % pair for pair in syntax.items())
        ln = 0
        ln_start = 0
        cnt = 0
        rrr = list(re.finditer(regex, code))
        for i in range(len(rrr)):
            mo: re.Match[str] = rrr[i]
            tp = mo.lastgroup
            value = mo.group()
            col = mo.start() - ln_start
            if tp == "NUM":
                yield Token(tp, '\033[1;33m', value, ln, col)
            elif tp == 'ID' and value in keywords:
                yield Token(tp, '\033[1;35m', value, ln, col)
            elif tp == 'ID' and value in highlight_with_regex.builtins:
                yield Token(tp, '\033[1;94m', value, ln, col)
            # elif tp == 'ID' and value in flatten_list(sym_table):
            #     yield Token(tp, '\033[1;36m', value, ln, col)
            elif tp == 'ID' or tp == 'OTHERS':
                yield Token(tp, '\033[1;0m', value, ln, col)
            elif tp in ('LPAREN', 'RPAREN', 'QUOTE', 'NOQUOTE'):
                if tp == 'RPAREN':
                    cnt -= 1
                    # if sym_table:
                    #     sym_table.pop()
                yield Token(tp, paren_color[cnt%len(paren_color)], value, ln, col)
                if tp == 'LPAREN':
                    cnt += 1
                    # if i + 2 < len(rrr) and rrr[i+1].group() == "define":
                        # sym_table[-1].append(rrr[i+2].group())
                    # else:
                        # sym_table += [[]]
            elif tp == 'STRING':
                yield Token(tp, '\033[0;32m', value, ln, col)
            elif tp == 'COMMENT':
                yield Token(tp, '\033[38;5;242m', value, ln, col)
            elif tp == 'NEWLINE':
                ln_start = mo.end()
                ln += 1
                continue
            elif tp == 'SKIP':
                continue
    
    
    code = '''
    ; A program
    (define fac (lambda (a)
        (if a
            (* (fac (- a 1)) a)
            1)))
    
    (define add (lambda (a b)
        (print a " " b "\\n")
        (+ a b)))
    
    (define MACRO-GREET (macro (name)
        '(print "Hello, " ,name "!\\n")))
    '''
    '''for token in tokenize(code):
        gotoxy(token.ln, token.col + 1)
        print(token.color, token.value, end="\033[1;0m", flush=True, sep="")
        # print(token)
    print("\033[1;0m")'''
    

tl_highlighter = highlight_with_regex.tokenize
Token = highlight_with_regex.Token
import re
import sys
import termios
import tty


def gotoxy(y: int, x: int):  # y: ln, x: col
    print(f"\033[{y};{x}f", end="", flush=True)


def clear():
    print("\033c", end="", flush=True)
    
    

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def edit():
    def editor_quit():
        nonlocal need_quit
        need_quit = True

    def cursor_up():
        nonlocal ln, col
        ln = max(0, ln - 1)
        col = min(len(code[ln]), col_history)

    def cursor_down():
        nonlocal ln, col
        ln = min(ln + 1, len(code) - 1)
        col = min(len(code[ln]), col_history)

    def cursor_left():
        nonlocal col, col_history
        col_history = col = max(0, col - 1)

    def cursor_right():
        nonlocal col, col_history
        col_history = col = min(len(code[ln]), col + 1)

    def delete():
        nonlocal ln, col, col_history, need_update
        if col == 0:
            if ln:
                ln -= 1
                col = len(code[ln])
                code[ln] += code[ln+1]
                del code[ln+1]
                need_update = {i for i in range(start, start + ln_size)}
        else:
            del code[ln][col-1]
            col -= 1
            need_update.add(ln)
        col_history = col

    def insert(key):
        nonlocal ln, col, col_history, need_update
        if key == '\r':
            code.insert(ln + 1, code[ln][col:])
            code[ln] = code[ln][:col]
            ln += 1
            col = 0
            need_update = {i for i in range(start, start + ln_size)}
        else:
            code[ln].insert(col, key)
            col += 1
            need_update.add(ln)
        col_history = col

    def lparen():
        nonlocal col
        insert('(')
        insert(')')
        col -= 1

    def rparen():
        nonlocal col
        if col < len(code[ln]) and code[ln][col] == ')':
            col += 1
        else:
            insert(')')

    def quote():
        nonlocal col
        if col < len(code[ln]) and code[ln][col] == '"':
            col += 1
        else:
            insert('"')
            insert('"')
            col -= 1

    def tab():
        nonlocal col
        if all(map(lambda a: a == " ", code[ln][:col])):
            for i in range(tab_size):
                insert(' ')
        else:  # Tab补全
            this_word = ""
            while col > 0 and (code[ln][col-1] not in " \t\"\'(),"):
                this_word = code[ln][col-1] + this_word
                delete()
            words = set(get_all_word() +
                        [
                'if',
                'define',
                'lambda',
                'macro',
                'quote',
                'set!',
                'begin'
            ] + list(scope.var.keys()))
            print("\033[1;0m", end="", flush=True)
            '''gotoxy(ln_size + 1, 1)
            print(this_word, words, get_all_word(), end="", flush=True)'''
            words = sorted(list(filter(lambda a: this_word in a, words)))
            if words == []:
                for i in this_word:
                    insert(i)
            else:
                cnt = 0
                gotoxy(ln % ln_size + 1, col + 1)
                print(" " * len(this_word), end="", flush=True)
                gotoxy(ln % ln_size + 1, col + 1)
                print(words[cnt], end="", flush=True)
                while 1:
                    key = getch()
                    if key == '\t':
                        cnt += 1
                        cnt %= len(words)
                        gotoxy(ln % ln_size + 1, col + 1)
                        print(words[cnt], end="", flush=True)
                    elif key == '\x1b':
                        for i in this_word:
                            insert(i)
                        break
                    else:
                        for i in words[cnt]:
                            insert(i)
                        break

    def run_tl():
        nonlocal need_update
        clear()
        print("\033[1;0m", end="", flush=True)
        try:
            scope.run_code("\n".join(map("".join, code)))
        except Exception as e:
            print("Error: ", e)
        getch()
        clear()
        need_update = {i for i in range(start, start + ln_size)}

    def delete_ext():
        if code[ln][col-1: col+1] in (["(", ")"], ['"', '"']):
            cursor_right()
            delete()
            delete()
        elif code[ln][col-2: col] == [" ", " "]:
            delete()
            delete()
        else:
            delete()

    def get_all_word():
        text = "\n".join(map("".join, code))
        sr = re.findall(r'[^0-9\s\'\(\),\"][^\s\(\)\";]*', text)
        return sr
    
    def save():
        nonlocal save_path
        if save_path == "" and save_path == "":
            save_path = read_cmd("Path: ")
        open(save_path, "w").write("\n".join(map("".join, code)))

    def save_as():
        nonlocal save_path
        save_path = read_cmd("Path: ")
        open(save_path, "w").write("\n".join(map("".join, code)))

    def open_file(path):
        nonlocal save_path, need_update, ln, col, code
        save_path = path
        c = open(save_path, "r", encoding="utf-8").read()
        ln, col = 0, 0
        start = 0
        code = [[]]
        for i in c:
            if i == '\n':
                code.append([])
            else:
                code[-1].append(i)
        need_update = {i for i in range(start, start + ln_size)}

    def read_cmd(msg):
        gotoxy(ln_size + 1, 1)
        print("\033[1;0m", end="", flush=True)
        return input(msg)

    def get_indent():
        tokens = list(tl_tokenize.tokenize("\n".join(map("".join, code))))
        rparens = list(map(lambda x: (x.ln, x.col), filter(lambda x: x.tp == "RPAREN", tokens)))
        lparens = list(map(lambda x: (x.ln, x.col), filter(lambda x: x.tp == "LPAREN", tokens)))
        line, column = ln, col

        def next():
            nonlocal line, column
            column += 1
            if column >= len(code[line]):
                column = 0
                line += 1

        while line < len(code):
            if (line, column) in rparens:
                break
            if (line, column) in lparens:
                cnt = 0
                while line < len(code):
                    if (line, column) in lparens:
                        cnt += 1
                    if (line, column) in rparens:
                        cnt -= 1
                    if cnt == 0:
                        break
                    next()
            next()
        for i in range(len(tokens)):
            if tokens[i].col == column and tokens[i].ln == line:
                cnt = 0
                for k in range(i, -1, -1):
                    if tokens[k].tp == 'RPAREN':
                        cnt += 1
                    if tokens[k].tp == 'LPAREN':
                        cnt -= 1
                    if cnt == 0:
                        return tokens[k].col + 1
                return 0
        return 0

    def newline_and_indent():
        indent = get_indent()
        insert('\r')
        for i in range(indent):
            insert(" ")

    ln, col = 0, 0
    save_path = ""
    code: list[list[str]] = [[]]
    start = 0
    ln_size = 17 - 2
    need_update = set()
    highlighter = tl_highlighter
    need_quit = False
    tab_size = 2
    key_bindings = {
        chr(224): {
            'H': cursor_up,
            'P': cursor_down,
            'K': cursor_left,
            'M': cursor_right,
        },
        '\x7f': delete_ext,
        '\x03': editor_quit,
        '\x13': save,
        '\x0f': lambda: open_file(read_cmd("Path: ")),
        '(': lparen,
        ')': rparen,
        '"': quote,
        '\t': tab,
        '\033': {
            '[': {
                'A': cursor_up,
                'B': cursor_down,
                'D': cursor_left,
                'C': cursor_right,
            },
            'r': run_tl,
            's': save_as,
        },
        '\r': newline_and_indent,
    }
    col_history = 0
    while not need_quit:
        if ln // ln_size * ln_size != start:
            start = ln // ln_size * ln_size
            need_update = {i for i in range(start, start + ln_size)}
        for i in need_update:
            gotoxy(i % ln_size + 1, 1)
            print(" " * (50 - 1), end="", flush=True)
        for i in highlighter("\n".join(map("".join, code))):
            if i.ln in need_update:
                gotoxy(i.ln % ln_size + 1, i.col + 1)
                print(i.color + i.value, end="", flush=True)
        gotoxy(ln % ln_size + 1, col + 1)
        need_update = set()
        key = getch()
        if key in key_bindings:
            k = key_bindings[key]
            while isinstance(k, dict):
                key =getch()
                if key in k:
                    k = k[key]
                else:
                    break
            if callable(k):
                k()
        else:
            insert(key)


clear()
edit()
'''print(repr(getch()))
print(repr(getch()))
print(repr(getch()))'''
'''
        '\x1b': {
            '[': {
                'A': cursor_up,
                'B': cursor_down,
                'D': cursor_left,
                'C': cursor_right,
            },
            'r': run_tl,
        },
        chr(127): delete_ext,
        '\x03': editor_quit,
        '(': lparen,
        ')': rparen,
        '"': quote,
        '\t': tab,
'''
