from collections.abc import Generator
from enum import Enum, unique, auto
import operator
import pprint
import re
from typing import Any, Literal, Optional


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
    (re.compile(r"[ \t\r\n\f]+"), TokenType.WS),
    (re.compile(r"\/\/[^\n]*"), TokenType.COMMENT),
]

PREC_LOWEST = 5  # ASSIGN
PREC_LOGIC = 4  # EQ NE
PREC_CMP = 3  # GT LT GE TE
PREC_SUM = 2  # ADD SUB
PREC_PRODUCT = 1  # MUL DIV MOD
PREC_TOP = 0  # primary


def prec(t: TokenType) -> int:
    match t:
        case TokenType.ASSIGN:
            return PREC_LOWEST
        # case TokenType.EQ | TokenType.NE:
        #     return PREC_LOGIC
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
}

type Token = tuple[
    Literal[
        TokenType.ADD,
        TokenType.SUB,
        TokenType.MUL,
        TokenType.DIV,
        TokenType.MOD,
        TokenType.GT,
        TokenType.LT,
        TokenType.GE,
        TokenType.LE,
        TokenType.EQ,
        TokenType.NE,
        TokenType.ASSIGN,
        TokenType.IF,
        TokenType.ELSE,
        TokenType.WHILE,
        TokenType.FUNC,
        TokenType.BREAK,
        TokenType.CONTINUE,
        TokenType.LET,
        TokenType.RETURN,
        TokenType.SEMI,
        TokenType.COMMA,
        TokenType.COLON,
        TokenType.LPAREN,
        TokenType.RPAREN,
        TokenType.LBRACKET,
        TokenType.RBRACKET,
        TokenType.LBRACE,
        TokenType.RBRACE,
        TokenType.TRUE,
        TokenType.FALSE,
        TokenType.NULL,
        TokenType.PACKAGE,
        TokenType.IMPORT,
        TokenType.NUMBER,
        TokenType.STRING,
        TokenType.ID,
    ],
    str,
]
type TokenStream = Generator[
    Token,
    Any,
    None,
]


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

    def expr(curprec: int = PREC_LOWEST + 1) -> Any:
        """prec climber"""
        nonlocal curtok
        left = primary()
        while (
            not (
                curtok_is(TokenType.RBRACE)
                or curtok_is(TokenType.RBRACKET)
                or curtok_is(TokenType.RPAREN)
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
                _ = tuple(eat(TokenType.LPAREN))
                while not curtok_is(TokenType.RPAREN) and curtok:
                    args.append(expr())
                    if not curtok_is(TokenType.RPAREN):
                        _ = tuple(eat(TokenType.COMMA))
                return ["call", id, args]
            return ["id", id]
        if curtok_is(TokenType.LPAREN):
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
        raise SyntaxError("a primary expression was expected")

    next_token()
    next_token()
    return expr()


def interpret(tree: Any) -> Any:
    # interpreter varriables
    env: list[dict[str, Any]] = [{}]

    def lookup(name: str, idx: int = -1):
        nonlocal env
        try:
            cur_env = env[idx]
        except IndexError:
            raise NameError(name=name)
        else:
            if name in cur_env.keys():
                return cur_env[name]
            else:
                return lookup(name, idx - 1)
            
    def set_local(name:str,v:Any):
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

    def eval_expr(t: Any) -> Any:
        match t:
            case ["binary", op, lhs, rhs]:
                if op==TokenType.ASSIGN:
                    v = eval_expr(rhs)
                    set_local(lhs[1],v)
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

    result = eval_expr(tree)
    print(env)
    return result


src = """
result = 2 == 2 - 1 % 1 - 1 + 1
"""
tokens = tokenize(src)
pprint.pprint(list(tokens))
tree = parse(tokenize(src))
pprint.pprint(tree, indent=4)
print(interpret(parse(tokenize(src))))
