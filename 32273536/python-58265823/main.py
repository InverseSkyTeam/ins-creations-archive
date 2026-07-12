from ast import Constant, arg, stmt
from collections.abc import Generator
import ctypes
from enum import Enum, unique, auto
import operator
import os
import pprint
import re
from turtle import tracer
from typing import Any, Optional
from llvmlite import ir
import llvmlite.binding as llvm


@unique
class TokenType(Enum):
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    MOD = auto()
    GT = auto()
    LT = auto()
    GE = auto()
    LE = auto()
    EQ = auto()
    NE = auto()
    ASSIGN = auto()
    DOT = auto()
    AND = auto()
    OR = auto()
    NOT = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    FUNC = auto()
    BREAK = auto()
    CONTINUE = auto()
    LET = auto()
    RETURN = auto()
    SEMI = auto()
    COMMA = auto()
    COLON = auto()
    LPAREN = auto()
    RPAREN = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    LBRACE = auto()
    RBRACE = auto()
    TRUE = auto()
    FALSE = auto()
    NULL = auto()
    IMPORT = auto()
    NUMBER = auto()
    STRING = auto()
    ID = auto()
    WS = auto()
    COMMENT = auto()


LEX_MAP = [
    (re.compile(r"[ \t\r\n\f]+"), TokenType.WS),
    (re.compile(r"\/\/[^\n]*"), TokenType.COMMENT),
    (re.compile(r"\."), TokenType.DOT),
    (re.compile(r"\+"), TokenType.ADD),
    (re.compile("-"), TokenType.SUB),
    (re.compile(r"\*"), TokenType.MUL),
    (re.compile("/"), TokenType.DIV),
    (re.compile("%"), TokenType.MOD),
    (re.compile(">"), TokenType.GT),
    (re.compile("<"), TokenType.LT),
    (re.compile(">="), TokenType.GE),
    (re.compile("<="), TokenType.LE),
    (re.compile("=="), TokenType.EQ),
    (re.compile("!="), TokenType.NE),
    (re.compile("="), TokenType.ASSIGN),
    (re.compile(";"), TokenType.SEMI),
    (re.compile(","), TokenType.COMMA),
    (re.compile(":"), TokenType.COLON),
    (re.compile(r"\("), TokenType.LPAREN),
    (re.compile(r"\)"), TokenType.RPAREN),
    (re.compile(r"\["), TokenType.LBRACKET),
    (re.compile(r"\]"), TokenType.RBRACKET),
    (re.compile(r"{"), TokenType.LBRACE),
    (re.compile(r"}"), TokenType.RBRACE),
    (re.compile(r"[0-9]+(\.[0-9]+)?"), TokenType.NUMBER),
    (re.compile(r"\"(\\\"|.)*?\""), TokenType.STRING),
    (re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*"), TokenType.ID),
]

KW_MAP = {
    "and": TokenType.AND,
    "or": TokenType.OR,
    "not": TokenType.NOT,
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
    "null": TokenType.NULL,
    "import": TokenType.IMPORT,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "while": TokenType.WHILE,
    "func": TokenType.FUNC,
    "break": TokenType.BREAK,
    "continue": TokenType.CONTINUE,
    "let": TokenType.LET,
    "return": TokenType.RETURN,
}

PREC_LOWEST = 7
PREC_ASSIGN = 6  # ASSIGN
PREC_LOGIC = 5  # EQ NE
PREC_CMP = 4  # GT LT GE TE
PREC_SUM = 3  # ADD SUB
PREC_PRODUCT = 2  # MUL DIV MOD
PREC_TOP = 1  # primary

PREC = {
    TokenType.ASSIGN: PREC_ASSIGN,
    TokenType.AND: PREC_LOGIC,
    TokenType.OR: PREC_LOGIC,
    TokenType.GT: PREC_CMP,
    TokenType.LT: PREC_CMP,
    TokenType.GE: PREC_CMP,
    TokenType.LE: PREC_CMP,
    TokenType.EQ: PREC_CMP,
    TokenType.NE: PREC_CMP,
    TokenType.ADD: PREC_SUM,
    TokenType.SUB: PREC_SUM,
    TokenType.MUL: PREC_PRODUCT,
    TokenType.DIV: PREC_PRODUCT,
    TokenType.MOD: PREC_PRODUCT,
}


def escape(s: str) -> str:
    idx = 1
    r = ""
    while idx < len(s) - 1:
        if s[idx] == "\\":
            idx += 1
            escape_chr = s[idx]
            if escape_chr == "t":
                r += "\t"
            elif escape_chr == "n":
                r += "\n"
            elif escape_chr == "\\":
                r += "\\"
            elif escape_chr == '"':
                r += '"'
            elif escape_chr == "r":
                r += "r"
            elif escape_chr == "f":
                r += "f"
            else:
                r += "\\" + escape_chr
        else:
            r += s[idx]
        idx += 1
    return r


def prec(t: TokenType) -> int:
    if t in PREC.keys():
        return PREC[t]
    raise KeyError(f"{t} is not a binary operator")


def get_kattr(o, v):
    if isinstance(o, dict) and v in o.keys():
        return o[v]
    return getattr(o, v)


def set_kattr(o, name: str, value):
    if isinstance(o, dict) and not name.startswith("__"):
        o[name] = value
    else:
        setattr(o, name, value)


DISPATCH_MAP = {
    TokenType.ADD: operator.add,
    TokenType.SUB: operator.sub,
    TokenType.MUL: operator.mul,
    TokenType.DIV: lambda l, r: l / r,
    TokenType.MOD: lambda l, r: l % r,
    TokenType.GT: operator.gt,
    TokenType.LT: operator.lt,
    TokenType.GE: operator.ge,
    TokenType.LE: operator.le,
    TokenType.EQ: operator.eq,
    TokenType.NE: operator.ne,
    TokenType.AND: operator.and_,
    TokenType.OR: operator.or_,
}

type Token = tuple[
    TokenType,
    str,
]
type TokenStream = Generator[
    Token,
    Any,
    None,
]


def dispatch_binary(op: TokenType, left: Any, right: Any) -> Any:
    fn = DISPATCH_MAP[op]
    return fn(left, right)


class SignalContinue(Exception):
    def __init__(self) -> None:
        super().__init__("SignalContinue")


class SignalBreak(Exception):
    def __init__(self) -> None:
        super().__init__("SignalBreak")


class SignalReturn(Exception):
    def __init__(self, return_value) -> None:
        super().__init__("SignalReturn")
        self.return_value = return_value


def tokenize(source: str):
    while len(source) > 0:
        matched = False
        for pat, toktp in LEX_MAP:
            if match := pat.match(source, pos=0):
                # print(match)
                # print(source)
                if match.start() == 0:
                    if toktp not in (TokenType.WS, TokenType.COMMENT):
                        yield (
                            (
                                toktp
                                if (tp := KW_MAP.get(source[: match.end()], None))
                                is None
                                else tp
                            ),
                            source[: match.end()],
                        )
                    source = source[match.end() :]
                    matched = True
                    break
        if not matched:
            raise SyntaxError("Invalid syntax")


def print_tokens(s: str):
    for tp, v in tokenize(s):
        print(f"{tp},`{v}`")


def parse(token_stream: TokenStream):
    # parser varriables
    prevtok: Optional[Token] = None
    curtok: Optional[Token] = None
    nexttok: Optional[Token] = None
    tok_iter = token_stream

    # parser utils
    def next_token() -> None:
        nonlocal prevtok, curtok, nexttok, tok_iter
        prevtok = curtok
        curtok = nexttok
        nexttok = next(tok_iter, None)

    def eat(*types: TokenType) -> tuple[Token]:
        tokens = []
        for tp in types:
            if (curtok is None) or (curtok[0] != tp):
                raise SyntaxError(
                    f"{tp} is expected, but found {curtok[0] if curtok else "EOF"}"
                )
            tokens.append(curtok)
            next_token()
        return tuple(tokens)

    def curtok_is(tp: TokenType) -> bool:
        return curtok is not None and curtok[0] == tp

    # 本来预留了lookahead的接口，结果没用上 LL(0)
    # def prevtok_is(tp: TokenType) -> bool:
    #     return prevtok is not None and prevtok[0] == tp

    # def nexttok_is(tp: TokenType) -> bool:
    #     return nexttok is not None and nexttok[0] == tp

    def expr(curprec: int = PREC_LOWEST) -> Any:
        """precedence climber"""
        nonlocal curtok
        left = primary()
        while curtok and curtok[0] in PREC.keys():
            # print(curtok)
            op = curtok
            p = prec(op[0])
            if p < curprec:
                next_token()
                right = expr(p)
                left = optimize_expr(["binary", op[0], left, right])
            else:
                break
        return left

    def optimize_expr(t: Any) -> Any:
        """constants folding optimization"""
        match t:
            case ["binary", tp, ["num", _], ["num", _]]:
                v = dispatch_binary(tp, t[2][1], t[3][1])
                return ["num", v]
            case ["binary", TokenType.AND, ["bool", l], ["bool", r]]:
                return ["bool", l and r]
            case ["binary", TokenType.OR, ["bool", l], ["bool", r]]:
                return ["bool", l or r]
            case ["binary", TokenType.ADD, ["str", lhs], ["str", rhs]]:
                return ["str", lhs + rhs]
            case ["index", ["str", s], ["num", i]]:
                if isinstance(i, int):
                    return ["str", s[int(i)]]
                return t
            case ["unary", TokenType.SUB, ["num", v]]:
                return ["num", -v]
            case ["unary", TokenType.NOT, ["num", v]]:
                return ["num", v]
            case ["unary", TokenType.NOT, ["bool", v]]:
                return ["bool", not v]
            case _:
                return t

    def primary() -> Any:
        left = _primary()
        _exit = False
        while not _exit and curtok:
            _exit = True
            if curtok_is(TokenType.LPAREN):
                args = []
                next_token()
                while not curtok_is(TokenType.RPAREN) and curtok:
                    args.append(expr())
                    if not curtok_is(TokenType.RPAREN):
                        eat(TokenType.COMMA)
                next_token()
                left = ["call", left, args]
                _exit = False
            if curtok_is(TokenType.LBRACKET):
                next_token()
                e = expr()
                eat(TokenType.RBRACKET)
                left = ["index", left, e]
                _exit = False
            if curtok_is(TokenType.DOT):
                next_token()
                n = eat(TokenType.ID)[0][1]
                left = ["binary", TokenType.DOT, left, n]
                _exit = False
        return optimize_expr(left)

    def _primary() -> Any:
        nonlocal curtok
        if curtok_is(TokenType.NUMBER):
            num = eat(TokenType.NUMBER)[0][1]
            return ["num", float(num) if "." in num else int(num)]
        if curtok_is(TokenType.STRING):
            string = eat(TokenType.STRING)[0][1]
            return ["str", escape(string)]
        if curtok_is(TokenType.ID):
            id = eat(TokenType.ID)[0][1]
            return ["id", id]
        if curtok_is(TokenType.LPAREN):
            next_token()
            e = expr()
            eat(TokenType.RPAREN)
            return e
        if curtok_is(TokenType.TRUE):
            v = eat(TokenType.TRUE)[0][1]
            return ["bool", True]
        if curtok_is(TokenType.FALSE):
            v = eat(TokenType.FALSE)[0][1]
            return ["bool", False]
        if curtok_is(TokenType.NULL):
            v = eat(TokenType.NULL)[0][1]
            return ["null", None]
        if curtok_is(TokenType.NOT):
            next_token()
            v = primary()
            return optimize_expr(["unary", TokenType.NOT, v])
        if curtok_is(TokenType.FUNC):
            next_token()
            eat(TokenType.LPAREN)
            params: list[str] = []
            if not curtok_is(TokenType.RPAREN) and curtok:
                params.append(eat(TokenType.ID)[0][1])
            while not curtok_is(TokenType.RPAREN) and curtok:
                eat(TokenType.COMMA)
                params.append(eat(TokenType.ID)[0][1])
            next_token()
            body = block()
            return ["func", params, body]
        if curtok_is(TokenType.SUB):
            next_token()
            v = primary()
            return optimize_expr(["unary", TokenType.SUB, v])
        if curtok_is(TokenType.LBRACE):
            pairs = []
            next_token()
            while not curtok_is(TokenType.RBRACE) and curtok:
                k = expr()
                eat(TokenType.COLON)
                v = expr()
                pairs.append((k, v))
                if (
                    not curtok_is(TokenType.RBRACE) or curtok_is(TokenType.COMMA)
                ) and curtok:
                    eat(TokenType.COMMA)
            next_token()
            return ["dict", pairs]
        if curtok_is(TokenType.LBRACKET):
            values = []
            next_token()
            if not curtok_is(TokenType.RBRACKET) and curtok:
                v = expr()
                values.append(v)
            while not curtok_is(TokenType.RBRACKET) and curtok:
                eat(TokenType.COMMA)
                if not curtok_is(TokenType.RBRACKET) and curtok:
                    values.append(expr())
                else:
                    break
            next_token()
            return ["list", values]
        raise SyntaxError("a primary expression was expected")

    def stmt():
        if curtok_is(TokenType.IF):
            return if_stmt()
        if curtok_is(TokenType.WHILE):
            return while_stmt()
        # if curtok_is(TokenType.FUNC):
        #     return fn_decl()
        if curtok_is(TokenType.CONTINUE):
            return continue_stmt()
        if curtok_is(TokenType.BREAK):
            return break_stmt()
        if curtok_is(TokenType.RETURN):
            return return_stmt()
        if curtok_is(TokenType.LET):
            return let_decl()
        if curtok_is(TokenType.IMPORT):
            return import_decl()
        return expr_stmt()

    def import_decl():
        eat(TokenType.IMPORT)
        path = eat(TokenType.STRING)[0][1]
        name = eat(TokenType.ID)[0][1]
        return ["import", ["str", escape(path)], ["id", name]]

    def block():
        eat(TokenType.LBRACE)
        stmts = []
        while not curtok_is(TokenType.RBRACE) and curtok:
            stmts.append(stmt())
        eat(TokenType.RBRACE)
        return ["block", stmts]

    def expr_stmt():
        if not curtok_is(TokenType.SEMI) and curtok:
            e = expr()
        else:
            e = None
        eat(TokenType.SEMI)
        return ["expr_stmt", e]

    def while_stmt():
        eat(TokenType.WHILE)
        cond = expr()
        body = block()
        return ["while", cond, body]

    def continue_stmt():
        eat(TokenType.CONTINUE, TokenType.SEMI)
        return ["continue"]

    def break_stmt():
        eat(TokenType.BREAK, TokenType.SEMI)
        return ["break"]

    def return_stmt():
        eat(TokenType.RETURN)
        if curtok_is(TokenType.SEMI):
            return ["return", None]
        v = expr()
        eat(TokenType.SEMI)
        return ["return", v]

    def let_decl():
        eat(TokenType.LET)
        name = eat(TokenType.ID)[0][1]
        eat(TokenType.ASSIGN)
        value = expr()
        eat(TokenType.SEMI)
        return ["let", name, value]

    def if_stmt():
        eat(TokenType.IF)
        cond = expr()
        then_block = stmt()
        if curtok_is(TokenType.ELSE):
            next_token()
            else_block = stmt()
            return ["if", cond, then_block, else_block]
        return ["if", cond, then_block, None]

    def program():
        stmts = []
        while curtok:
            stmts.append(stmt())
        return ["program", stmts]

    next_token()
    next_token()
    return program()


def compile_tree(tree: Any, name: str = "main") -> ir.Module:
    env: list[dict[str, ir.AllocaInstr]] = [{}]

    i32tp = ir.IntType(32)
    floattp = ir.FloatType()
    voidtp = ir.VoidType()
    booltp = ir.IntType(1)

    module = ir.Module(name)
    print_int_fn = ir.Function(module, ir.FunctionType(voidtp, (i32tp,)), "print_int")
    read_int_fn = ir.Function(module, ir.FunctionType(i32tp, ()), "read_int")
    fn_type = ir.FunctionType(i32tp, ())
    main_fn = ir.Function(module, fn_type, "main")
    entry = main_fn.append_basic_block("entry")
    builder = ir.IRBuilder(entry)

    def compile_program(tree: Any):
        match tree:
            case "program", stmts:
                for i in stmts:
                    compile_decl(i)
                builder.ret(ir.Constant(i32tp, 0))
            case _:
                raise Exception()

    def compile_decl(tree: Any) -> None:
        match tree:
            case ["expr_stmt", e]:
                compile_expr(e)
            case ["let", name, value]:
                value = compile_expr(value)
                var = builder.alloca(i32tp, name=name)
                builder.store(value, var)
                env[-1][name] = var
            case _:
                raise Exception()

    def compile_expr(tree: Any) -> ir.Value:
        match tree:
            case ["num", i]:
                if isinstance(i, int):
                    return ir.Constant(i32tp, i)
                elif isinstance(i, float):
                    return ir.Constant(floattp, i)
                else:
                    raise Exception()
            case ["bool", b]:
                if b:
                    return ir.Constant(booltp, 1)
                else:
                    return ir.Constant(booltp, 0)
            case ["id", b]:
                load = builder.load(env[-1][b], b)
                return load
            case ["binary", type, l, r]:
                left = compile_expr(l)
                right = compile_expr(r)
                match type:
                    case TokenType.ADD:
                        result = builder.add(left, right, "add_temp")
                        # print(result)
                        return result  # type:ignore
                    case TokenType.ASSIGN:
                        value = compile_expr(r)
                        result = builder.store(value, env[-1][l[1]])
                        return result
                    case _:
                        raise Exception()
            case ["call", target, args]:
                if target == ["id", "print"]:
                    a = []
                    for i in args:
                        a.append(compile_expr(i))
                    return builder.call(print_int_fn, a)
                elif target == ["id", "readint"]:
                    if args:
                        a = []
                        for i in args:
                            a.append(compile_expr(i))
                        builder.call(print_int_fn, a)
                    return builder.call(read_int_fn, ())
                else:
                    print(tree)
                    raise Exception()
            case _:
                print(tree)
                raise Exception()

    compile_program(tree)
    return module


# src = r"""
# let o = object();
# o["hello"] = "world";
# o.world = "hello";

# println(o);

# let list = array();
# list.append("hello");
# list.append("world");

# println(list);
# println(len(list));

# let json_lit = {
#     "id": 123243,
#     "name": "hello"[0],
#     "values": [
#         "v1", "v2",
#     ],
# };

# println(json_lit.values[1]);

# let print = func(s) { apply(println, [s], {"end": ""}); };
# print("hi");
# println("hello");

# let true_fn = func() { println("true_fn"); return true; };
# let false_fn = func() { println("false_fn"); return false; };
# if false_fn() and true_fn() println("unreachable");
# if true_fn() or false_fn() println("branch-or");
# """
# tokens = tokenize(src)
# pprint.pprint(list(tokens))
# tree = parse(tokenize(src))
# pprint.pprint(tree, indent=4)

src = """
let a = 0;
a = a + 1;
print(a);
let b = readint();
print(b);"""
tokens = tokenize(src)
tree = parse(tokens)
# pprint.pp(tree)

# print("generated llvm ir:")
mod = compile_tree(tree, "main")


llvm.initialize()
llvm.initialize_native_asmparser()
llvm.initialize_native_asmprinter()
llvm.initialize_native_target()

context = llvm.get_global_context()
llvmmod = llvm.parse_assembly(str(mod), context)
llvmmod.triple = "x86_64-pc-windows-msvc19.42.34435"
llvmmod.name = "main"
llvmmod.verify()

passmanager = llvm.PassManagerBuilder()
passmanager.opt_level = 2

mpm = llvm.ModulePassManager()
passmanager.populate(mpm)
mpm.run(llvmmod)

print("optimized llvm ir:\n", llvmmod)

# cfg = llvm.get_function_cfg(mod.functions[1])
# with open("cfg.dot", "w") as f:
#     f.write(cfg)

# target = llvm.Target.from_default_triple()
# target_machine = target.create_target_machine()
# # And an execution engine with an empty backing module
# backing_mod = llvm.parse_assembly("")
# engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
# engine.add_object_file(llvm.ObjectFileRef.from_path("runtime.o"))
# engine.add_module(llvmmod)
# engine.finalize_object()
# engine.run_static_constructors()

# funcptr = engine.get_function_address("main")
# cfunc_main = ctypes.CFUNCTYPE(ctypes.c_void_p)(funcptr)
# cfunc_main()

with open("out.bc", "wb+") as f:
    f.write(llvmmod.as_bitcode())
os.system("clang ./k/runtime.c -c -o runtime.o")
os.system("clang out.bc -c -o out.o")
os.system("clang out.o runtime.o -o main.exe")
