from collections.abc import Generator
from enum import Enum, unique, auto
import operator
import pprint
import re
from typing import Any, Optional


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
    PACKAGE = auto()
    IMPORT = auto()
    NUMBER = auto()
    STRING = auto()
    ID = auto()
    WS = auto()
    COMMENT = auto()
    # EOF = auto()


LEX_MAP = [
    (re.compile(r"[ \t\r\n\f]+"), TokenType.WS),
    (re.compile(r"\/\/[^\n]*"), TokenType.COMMENT),
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
    (re.compile("and"), TokenType.AND),
    (re.compile("or"), TokenType.OR),
    (re.compile("not"), TokenType.NOT),
    (re.compile("="), TokenType.ASSIGN),
    (re.compile("if"), TokenType.IF),
    (re.compile("else"), TokenType.ELSE),
    (re.compile("while"), TokenType.WHILE),
    (re.compile("func"), TokenType.FUNC),
    (re.compile("break"), TokenType.BREAK),
    (re.compile("continue"), TokenType.CONTINUE),
    (re.compile("let"), TokenType.LET),
    (re.compile("return"), TokenType.RETURN),
    (re.compile(";"), TokenType.SEMI),
    (re.compile(","), TokenType.COMMA),
    (re.compile(":"), TokenType.COLON),
    (re.compile(r"\("), TokenType.LPAREN),
    (re.compile(r"\)"), TokenType.RPAREN),
    (re.compile(r"\["), TokenType.LBRACKET),
    (re.compile(r"\]"), TokenType.RBRACKET),
    (re.compile(r"{"), TokenType.LBRACE),
    (re.compile(r"}"), TokenType.RBRACE),
    (re.compile("true"), TokenType.TRUE),
    (re.compile("false"), TokenType.FALSE),
    (re.compile("null"), TokenType.NULL),
    (re.compile("package"), TokenType.PACKAGE),
    (re.compile("import"), TokenType.IMPORT),
    (re.compile(r"[0-9]+(\.[0-9]+)?"), TokenType.NUMBER),
    (re.compile(r"\"(\\\"|.)*?\""), TokenType.STRING),
    (re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*"), TokenType.ID),
]

PREC_LOWEST = 6
PREC_ASSIGN = 5  # ASSIGN
PREC_LOGIC = 4  # EQ NE
PREC_CMP = 3  # GT LT GE TE
PREC_SUM = 2  # ADD SUB
PREC_PRODUCT = 1  # MUL DIV MOD
PREC_TOP = 0  # primary


def prec(t: TokenType) -> int:
    match t:
        case TokenType.ASSIGN:
            return PREC_ASSIGN
        case TokenType.AND | TokenType.OR:
            return PREC_LOGIC
        case (
            TokenType.GT
            | TokenType.LT
            | TokenType.GE
            | TokenType.LE
            | TokenType.EQ
            | TokenType.NE
        ):
            return PREC_CMP
        case TokenType.ADD | TokenType.SUB:
            return PREC_SUM
        case TokenType.MUL | TokenType.DIV | TokenType.MOD:
            return PREC_PRODUCT
        case _:
            raise KeyError(f"{t} is not a binary operator")


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
                        yield (toktp, source[: match.end()])
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

    def eat(*types: TokenType) -> Generator[Token, Any, None]:
        """
        WARNING: the eat(*types) function is lazy!!!
        """
        for tp in types:
            if (curtok is None) or (curtok[0] != tp):
                raise SyntaxError(
                    f"{tp} is expected, but found {curtok[0] if curtok else "EOF"}"
                )
            yield curtok
            next_token()

    def curtok_is(tp: TokenType) -> bool:
        return curtok is not None and curtok[0] == tp

    def prevtok_is(tp: TokenType) -> bool:
        return prevtok is not None and prevtok[0] == tp

    def nexttok_is(tp: TokenType) -> bool:
        return nexttok is not None and nexttok[0] == tp

    def expr(curprec: int = PREC_LOWEST) -> Any:
        """prec climber"""
        nonlocal curtok
        left = primary()
        while (
            not (
                curtok_is(TokenType.RBRACE)
                or curtok_is(TokenType.RBRACKET)
                or curtok_is(TokenType.RPAREN)
                or curtok_is(TokenType.LBRACE)
                or curtok_is(TokenType.SEMI)
                or curtok_is(TokenType.COMMA)
            )
            and curtok
        ):
            # print(curtok)
            op = curtok
            p = prec(op[0])
            if p < curprec:
                next_token()
                right = expr(p)
                left = ["binary", op[0], left, right]
            else:
                break
        return left

    def primary() -> Any:
        nonlocal curtok
        if curtok_is(TokenType.NUMBER):
            num = tuple(eat(TokenType.NUMBER))[0][1]
            return ["num", float(num)]
        if curtok_is(TokenType.STRING):
            string = tuple(eat(TokenType.STRING))[0][1]
            return ["str", string]
        if curtok_is(TokenType.ID):
            id = tuple(eat(TokenType.ID))[0][1]
            if curtok_is(TokenType.LPAREN):
                args = []
                next_token()
                while not curtok_is(TokenType.RPAREN) and curtok:
                    args.append(expr())
                    if not curtok_is(TokenType.RPAREN):
                        _ = tuple(eat(TokenType.COMMA))
                next_token()
                return ["call", id, args]
            return ["id", id]
        if curtok_is(TokenType.LPAREN):
            next_token()
            e = expr()
            _ = tuple(eat(TokenType.RPAREN))
            return e
        if curtok_is(TokenType.TRUE):
            v = tuple(eat(TokenType.TRUE))[0][1]
            return ["bool", True]
        if curtok_is(TokenType.FALSE):
            v = tuple(eat(TokenType.FALSE))[0][1]
            return ["bool", False]
        if curtok_is(TokenType.NULL):
            v = tuple(eat(TokenType.NULL))[0][1]
            return ["null", None]
        if curtok_is(TokenType.NOT):
            next_token()
            v = primary()
            return ["unary", TokenType.NOT, v]
        if curtok_is(TokenType.FUNC):
            next_token()
            _ = tuple(eat(TokenType.LPAREN))
            params: list[str] = []
            if not curtok_is(TokenType.RPAREN) and curtok:
                params.append(tuple(eat(TokenType.ID))[0][1])
            while not curtok_is(TokenType.RPAREN) and curtok:
                _ = tuple(eat(TokenType.COMMA))
                params.append(tuple(eat(TokenType.ID))[0][1])
            next_token()
            body = block()
            return ["func", params, body]

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
        # if curtok_is(TokenType.PACKAGE):
        #     return package_decl()
        # if curtok_is(TokenType.IMPORT):
        #     return import_decl()
        return expr_stmt()

    def block():
        _ = tuple(eat(TokenType.LBRACE))
        stmts = []
        while not curtok_is(TokenType.RBRACE) and curtok:
            stmts.append(stmt())
        _ = tuple(eat(TokenType.RBRACE))
        return ["block", stmts]

    def expr_stmt():
        if not curtok_is(TokenType.SEMI) and curtok:
            e = expr()
        else:
            e = None
        _ = tuple(eat(TokenType.SEMI))
        return ["expr_stmt", e]

    def while_stmt():
        _ = tuple(eat(TokenType.WHILE))
        cond = expr()
        body = block()
        return ["while", cond, body]

    def continue_stmt():
        _ = tuple(eat(TokenType.CONTINUE, TokenType.SEMI))
        return ["continue"]

    def break_stmt():
        _ = tuple(eat(TokenType.BREAK, TokenType.SEMI))
        return ["break"]

    def return_stmt():
        _ = tuple(eat(TokenType.RETURN))
        if curtok_is(TokenType.SEMI):
            return ["return", None]
        v = expr()
        _ = tuple(eat(TokenType.SEMI))
        return ["return", v]

    def program():
        stmts = []
        while curtok:
            stmts.append(stmt())
        return ["program", stmts]

    next_token()
    next_token()
    return program()


def interpret(tree: Any) -> Any:
    # interpreter varriables
    env: list[dict[str, Any]] = []
    env.append({"println": print, "readln": input})

    def lookup(name: str, idx: int = -1):
        nonlocal env
        if len(env) + idx < 0:
            raise NameError(f"name {name} was undefined")
        if name in env[idx].keys():
            return env[idx][name]
        return lookup(name, idx - 1)

    def set_local(name: str, v: Any):
        peek_env()[name] = v

    def dispatch_binary(op: TokenType, left: Any, right: Any) -> Any:
        fn = DISPATCH_MAP[op]
        return fn(left, right)

    def push_env(e: Optional[dict[str, Any]] = None) -> None:
        env.append(e if e else {})

    def pop_env() -> dict[str, Any]:
        return env.pop()

    def peek_env() -> dict[str, Any]:
        return env[-1]

    def build_function(params: list[str], body: Any) -> Any:
        nonlocal env
        fn_env = env.copy()

        def function_wrapper(*args: Any) -> Any:
            nonlocal env
            invalid_arg = False
            try:
                param_env = dict(zip(params, args, strict=True))
            except:
                param_env = {}
                invalid_arg = True
            if invalid_arg:
                raise ValueError("Invalid number of arguments were provided")
            fn_env.append(param_env)
            fn_body = body
            # save current environment
            cur_env = env
            # replace current environment
            env = fn_env
            return_value = None
            try:
                eval_stmt(fn_body)
            except SignalReturn as ret:
                return_value = ret.return_value
            # recover environemt
            env = cur_env
            # function returned
            return return_value

        return function_wrapper

    def eval_expr(t: Any) -> Any:
        match t:
            case ["unary", op, v]:
                if op == TokenType.NOT:
                    return operator.not_(eval_expr(v))
                raise NotImplementedError()
            case ["binary", op, lhs, rhs]:
                if op == TokenType.ASSIGN:
                    v = eval_expr(rhs)
                    set_local(lhs[1], v)
                    return v
                return dispatch_binary(op, eval_expr(lhs), eval_expr(rhs))
            case ["num", float(n)]:
                return n
            case ["str", str(s)]:
                return s
            case ["id", str(id)]:
                return lookup(id)
            case ["call", name, args]:
                fn = lookup(name)
                v = []
                for arg in args:
                    v.append(eval_expr(arg))
                return fn(*v)
            case ["bool", bool(v)]:
                return v
            case ["null", _]:
                return None
            case ["func", params, body]:
                fn = build_function(params, body)
                return fn
            case _:
                raise NotImplementedError()

    def eval_stmt(t: Any) -> None:
        match t:
            case ["expr_stmt", e]:
                if e:
                    eval_expr(e)
            case ["block", stmts]:
                for s in stmts:
                    eval_stmt(s)
            case ["return", v]:
                raise SignalReturn(eval_expr(v))
            case ["while", cond, body]:
                while eval_expr(cond):
                    try:
                        eval_stmt(body)
                    except SignalContinue:
                        continue
                    except SignalBreak:
                        break
            case ["continue"]:
                raise SignalContinue()
            case ["break"]:
                raise SignalBreak()
            case _:
                raise NotImplementedError()

    def eval_program(t: Any) -> None:
        match t:
            case ["program", stmts]:
                for i in stmts:
                    eval_stmt(i)
            case _:
                raise NotImplementedError()

    result = eval_program(tree)
    # print(env)
    return result


src = r"""
counter = func () {
    cnt = 0;
    return func() {
        cnt = cnt + 1;
        return cnt;
    };
};
// hello world
c = counter();
n = c();
while n < 10 {
    println(n); 
    n = c();
}
"""
# tokens = tokenize(src)
# pprint.pprint(list(tokens))
# tree = parse(tokenize(src))
# pprint.pprint(tree, indent=4)
interpret(parse(tokenize(src)))
