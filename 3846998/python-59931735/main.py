import keyword
import time

onedark_theme = {
    "bg": (0x282C34, 0x000000),
    "text": (0x282C34, 0xABB2BF),
    "id": (0x282C34, 0xABB2BF),
    "sel": (0x3E4452, 0x000000),
    "cursor": (0x528BFF, 0x528BFF),
    "linum": (0x282C34, 0x495162),
    "num": (0x282C34, 0xD19A66),
    "kw": (0x282C34, 0xC678DD),
    "str": (0x282C34, 0x98C379),
    "const": (0x282C34, 0xD19A66),
    "comment": (0x282C34, 0x5C6370),
    "op": (0x282C34, 0xABB2BF),
    "func": (0x282C34, 0x61AFEF),
    "class": (0x282C34, 0xE5C07B),
    "module": (0x282C34, 0xE5C07B),
    "field": (0x282C34, 0xE06C75),
    "param": (0x282C34, 0xD19A66),
    "error": (0xFF0000, 0xABB2BF),
}

default_theme = onedark_theme

pyTokDict = [
    "id",
    "num",
    "const",
    "kw",
    "str",
    "comment",
    "op",
    "text",
    "class",
    "func",
    "module",
    "field",
    "param",
]

pyKwSet = set(keyword.kwlist)
pySoftKwSet = {"_", "match", "case"}
pySelfSet = {"self", "cls"}
pyConstSet = {"True", "False", "None"}

pyOpSet = set("~!%^&*()-+=[{}]|/;:,.<>")

pyFuncSet = {
    "abs",
    "all",
    "any",
    "ascii",
    "bin",
    "breakpoint",
    "callable",
    "chr",
    "compile",
    "copyright",
    "credits",
    "delattr",
    "dir",
    "divmod",
    "eval",
    "exec",
    "exit",
    "format",
    "getattr",
    "globals",
    "hasattr",
    "hash",
    "help",
    "hex",
    "id",
    "input",
    "isinstance",
    "issubclass",
    "iter",
    "len",
    "license",
    "locals",
    "max",
    "min",
    "next",
    "oct",
    "open",
    "ord",
    "pow",
    "print",
    "quit",
    "repr",
    "round",
    "setattr",
    "sum",
    "vars",
}


pyClassSet = {
    "str",
    "int",
    "float",
    "complex",
    "bool",
    "list",
    "tuple",
    "dict",
    "set",
    "frozenset",
    "bytes",
    "bytearray",
    "memoryview",
    "object",
    "type",
    "enumerate",
    "range",
    "zip",
    "map",
    "filter",
    "reversed",
    "slice",
    "staticmethod",
    "classmethod",
    "property",
    "super",

    "Exception",
    "BaseException",
    "SystemExit",
    "KeyboardInterrupt",
    "GeneratorExit",
    "StopIteration",
    "StopAsyncIteration",
    "ArithmeticError",
    "FloatingPointError",
    "OverflowError",
    "ZeroDivisionError",
    "AssertionError",
    "AttributeError",
    "BufferError",
    "EOFError",
    "ImportError",
    "ModuleNotFoundError",
    "LookupError",
    "IndexError",
    "KeyError",
    "MemoryError",
    "NameError",
    "UnboundLocalError",
    "OSError",
    "BlockingIOError",
    "ChildProcessError",
    "ConnectionError",
    "BrokenPipeError",
    "ConnectionAbortedError",
    "ConnectionRefusedError",
    "ConnectionResetError",
    "FileExistsError",
    "FileNotFoundError",
    "InterruptedError",
    "IsADirectoryError",
    "NotADirectoryError",
    "PermissionError",
    "ProcessLookupError",
    "TimeoutError",
    "ReferenceError",
    "RuntimeError",
    "NotImplementedError",
    "RecursionError",
    "SyntaxError",
    "IndentationError",
    "TabError",
    "SystemError",
    "TypeError",
    "ValueError",
    "UnicodeError",
    "UnicodeDecodeError",
    "UnicodeEncodeError",
    "UnicodeTranslateError",
    "Warning",
    "UserWarning",
    "DeprecationWarning",
    "PendingDeprecationWarning",
    "SyntaxWarning",
    "RuntimeWarning",
    "FutureWarning",
    "ImportWarning",
    "UnicodeWarning",
    "BytesWarning",
    "ResourceWarning",
}


def colorcvt(fg):
    if isinstance(fg, int):
        return fg // (256 * 256), fg % (256 * 256) // 256, fg % 256
    return fg


def cvt_truecolor(fg: tuple, bg: tuple):
    if bg == (0, 0, 0):
        return f"\033[38;2;{fg[0]};{fg[1]};{fg[2]}m"
    else:
        return f"\033[38;2;{fg[0]};{fg[1]};{fg[2]}m\033[48;2;{bg[0]};{bg[1]};{bg[2]}m"


def ispynum(s: str):
    if s[:2] == '00':
        return False
    if s[:2] in {'0b', '0o', '0x'}:
        return all(map(lambda x: x.isdecimal() or x == '.' or ord('A') <= ord(x) <= ord('F') or ord('a') <= ord(x) <= ord('f'), s[2:]))
    return all(map(lambda x: x.isdigit() or x == '.', s))


def render(code: str):
    def find_after(c='('):
        p = pos
        while p < len(code) and (code[p].isspace() or code[p] == '\\'):
            if code[p] == '\n' and not sum(braclv):
                return False
            if code[p] == '\\':
                if p + 1 < len(code) and code[p + 1] == '\n':
                    p += 1
            p += 1
        return code[p] == c

    pos = 0
    buf: list[tuple[str, str]] = []
    braclv = [0, 0, 0]
    after_th = None
    after_dot = False
    after_class = False
    after_def = False
    after_import = False

    while pos < len(code):
        cur_token = ""
        if code[pos].isspace():
            while pos < len(code) and code[pos].isspace():
                cur_token += code[pos]
                if code[pos] == '\n' and not sum(braclv):
                    after_th = None
                    after_class = False
                    after_def = False
                    after_import = False
                pos += 1
            buf.append(("text", cur_token))
            after_dot = False
        elif code[pos].isdigit():
            while pos < len(code) and (code[pos].isalnum() or code[pos] == "."):
                cur_token += code[pos]
                pos += 1
            if ispynum(cur_token):
                buf.append(("num", cur_token))
            else:
                buf.append(("error", cur_token))
            after_dot = False
        elif code[pos].isalpha() or code[pos] == "_":
            while pos < len(code) and (code[pos].isalnum() or code[pos] == "_"):
                cur_token += code[pos]
                pos += 1
            if cur_token in pyConstSet:
                tp = "const"
            elif cur_token in pyKwSet:
                tp = "kw"
                if cur_token == "class" and braclv == [0, 0, 0]:
                    after_class = True
                elif cur_token == "def" and braclv == [0, 0, 0]:
                    after_def = True
                elif cur_token == "from" and braclv == [0, 0, 0]:
                    after_import = True
                elif cur_token == "import" and braclv == [0, 0, 0]:
                    after_import = not after_import
            elif find_after('=') and braclv[0] > 0:
                tp = "param"
            elif after_import:
                tp = "module"
            elif after_th or after_class:
                tp = "class"
            elif after_def and (find_after('=') or find_after(')')
                                or find_after(',') or find_after(':')):
                tp = "param"
            elif after_def:
                tp = "func"
            elif after_dot:
                if find_after():
                    if ord('A') <= ord(cur_token[0]) <= ord('Z') and '_' not in cur_token:
                        tp = "class"
                    else:
                        tp = "func"
                else:
                    tp = "field"
            elif cur_token in pyClassSet:
                tp = "class"
            elif cur_token in pyFuncSet:
                tp = "func"
            elif find_after():
                if ord('A') <= ord(cur_token[0]) <= ord('Z') and '_' not in cur_token:
                    tp = "class"
                else:
                    tp = "func"
            elif cur_token in pySelfSet:
                tp = "param"
            elif cur_token in pySoftKwSet:
                tp = "kw"
            else:
                tp = "id"
            buf.append((tp, cur_token))
            after_dot = False
        elif code[pos] in "\"'":
            qc = code[pos]
            pos += 1
            cur_token += qc
            if pos < len(code) and code[pos] == qc:
                cur_token += qc
                pos += 1
                if pos < len(code) and code[pos] == qc:
                    cur_token += qc
                    pos += 1
                else:
                    buf.append(("str", cur_token))
                    continue
            qc = cur_token
            while pos < len(code) and code[pos: pos + len(qc)] != qc:
                if code[pos] == "\\":
                    cur_token += code[pos]
                    pos += 1
                if pos < len(code):
                    cur_token += code[pos]
                    pos += 1
            if pos < len(code):
                cur_token += code[pos: pos + len(qc)]
                pos += len(qc)
            buf.append(("str", cur_token))
            after_dot = False
        elif code[pos] in pyOpSet:
            while pos < len(code) and code[pos] in pyOpSet:
                if code[pos] == '(':
                    braclv[0] += 1
                elif code[pos] == ')' and braclv[0] > 0:
                    braclv[0] -= 1
                elif code[pos] == '[':
                    braclv[1] += 1
                elif code[pos] == ']' and braclv[1] > 0:
                    braclv[1] -= 1
                elif code[pos] == '{':
                    braclv[2] += 1
                elif code[pos] == '}' and braclv[2] > 0:
                    braclv[2] -= 1
                cur_token += code[pos]
                pos += 1
            buf.append(("op", cur_token))
            if cur_token.endswith("->") and braclv == [0, 0, 0]:
                after_th = "->"
            elif cur_token.endswith(":") and braclv in ([0, 0, 0], [1, 0, 0]):
                after_th = ":"
            elif cur_token.endswith(":") and braclv in [0, 0, 0]:
                after_class = after_def = False
            elif cur_token.endswith(",") and after_th == ":" and braclv == [1, 0, 0]:
                after_th = None
            elif cur_token.endswith("=") and after_th == ":" and braclv in ([0, 0, 0], [1, 0, 0]):
                after_th = None
            elif cur_token.endswith(":") and after_th == "->" and braclv == [0, 0, 0]:
                after_th = None
            if cur_token.endswith(".") or cur_token.endswith("...."):
                after_dot = True
            else:
                after_dot = False
        elif code[pos] == "#":
            while pos < len(code) and code[pos] != "\n":
                cur_token += code[pos]
                pos += 1
            buf.append(("comment", cur_token))
            after_dot = False
        elif code[pos] == '\\':
            if pos + 1 < len(code) and code[pos + 1] == '\n':
                pos += 2
                buf.append(('text', '\\\n'))
            else:
                buf.append(('error', '\\'))
                pos += 1
            after_dot = False
        else:
            cur_token += code[pos]
            pos += 1
            buf.append(("error", cur_token))

    return buf


def highlight(code: str, theme=default_theme):
    buf = render(code)
    for tp, token in buf:
        print(cvt_truecolor(colorcvt(theme[tp][1]), colorcvt(theme[tp][0])), end="", flush=False)
        print(token, end="", flush=True)
        time.sleep(0.005)
    print("\033[0m", end="", flush=True)


highlight(open(__file__, encoding="utf-8").read())
