# Python >= 3.12

from __future__ import annotations
from enum import Enum, auto
import typing

from typing import (
    Any,
    Callable,
    Generator,
    NamedTuple,
    Never,
    NoReturn,
    Tuple,
    List,
)

INT, FLOAT, STR, SYMBOL, OPERATOR = "int", "float", "str", "symbol", "operator"
OPERATORS = "= + - * / % ^ < > == != <= >= , ; { } ( ) [] : . += -= *= /= ^=".split()
OPERATOR_CHR_FIRST = [i[0] for i in OPERATORS]
OPERATOR_CHR_SECOND = [i[1:] for i in OPERATORS if len(i) > 1]
KEYWORDS = "fn let const if while as return break continue use mod true false and or not move".split()

type TokType = typing.Literal[
    "int",
    "float",
    "str",
    "symbol",
    "operator",
    "keyword",
    "bool",
]
type Tok = (
    Tuple[typing.Literal["int"], int]
    | Tuple[typing.Literal["float"], float]
    | Tuple[
        typing.Literal["str"],
        str,
    ]
    | Tuple[typing.Literal["symbol"], str]
    | Tuple[typing.Literal["operator"], str]
    | Tuple[
        typing.Literal["keyword"],
        str,
    ]
    | Tuple[typing.Literal["bool"], bool]
)


def tokenize(_s: str) -> List[Tok]:
    if len(_s) == 0:
        return []
    src = _s
    cur_pos = 0
    cur_char = src[cur_pos]
    tokens: List[Tok] = []

    def int_tok(i: int) -> Tok:
        return ("int", i)

    def float_tok(f: float) -> Tok:
        return ("float", f)

    def str_tok(s: str) -> Tok:
        return ("str", s)

    def keyword_tok(s: str) -> Tok:
        if s in ["true", "false"]:
            return ("bool", True if s == "true" else False)
        return ("keyword", s)

    def symbol_tok(s: str) -> Tok:
        if not s in KEYWORDS:
            return ("symbol", s)
        else:
            return keyword_tok(s)

    def operator_tok(s: str) -> Tok:
        nonlocal err
        if not s in OPERATORS:
            err(f"Unknown operator: {s}")
        return ("operator", s)

    def is_eof() -> bool:
        return cur_pos >= len(src)

    def has_next() -> bool:
        return cur_pos + 1 < len(src)

    def peek(p: int = 1, span: int = 1):
        return src[cur_pos + p : cur_pos + p + span]

    def advance(step: int = 1):
        nonlocal cur_pos, cur_char
        cur_pos += step
        try:
            cur_char = src[cur_pos]
        except IndexError:
            cur_char = ""

    def match_next(s: str) -> bool:
        try:
            return peek(len(s)) == s
        except IndexError:
            return False

    def skip() -> None:
        while cur_char.isspace() and not is_eof():
            advance()

    def err(msg: str) -> NoReturn:
        raise Exception(f"Syntax Error: {msg}; at {cur_pos}")

    def read_number() -> str:
        s = cur_char
        while not is_eof():
            advance()
            if not cur_char.isspace() and (cur_char.isdigit() or cur_char == "."):
                s += cur_char
            else:
                break
        return s

    def eat_str() -> Tok:
        advance()
        s = ""
        while cur_char != '"' and not is_eof():
            if cur_char == "\\" and has_next():
                next = peek()
                match next:
                    case "n":
                        s += "\n"
                        advance()
                    case "r":
                        s += "\r"
                        advance()
                    case "t":
                        s += "\t"
                        advance()
                    case '"':
                        s += '"'
                        advance()
                    case _:
                        s += cur_char
            else:
                s += cur_char
            advance()
        advance()
        return str_tok(s)

    def eat_symbol() -> Tok:
        s = ""
        while (
            not cur_char.isspace()
            and not cur_char in OPERATOR_CHR_FIRST
            and not is_eof()
        ):
            s += cur_char
            advance()
        return symbol_tok(s)

    def eat_operator() -> Tok:
        _cur_char = cur_char
        if cur_char in OPERATOR_CHR_FIRST and peek() in OPERATOR_CHR_SECOND:
            _next_char = peek()
            advance(2)
            return operator_tok(_cur_char + _next_char)
        else:
            advance(1)
            return operator_tok(_cur_char)

    skip()
    while cur_pos < len(src):
        match cur_char:
            case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                number = read_number()
                if "." in number:
                    try:
                        tokens.append(float_tok(float(number)))
                    except ValueError:
                        err(f"Invalid float number: {number}")
                else:
                    try:
                        tokens.append(int_tok(int(number)))
                    except ValueError:
                        err(f"Invalid integer number: {number}")
            case "/":
                if match_next("/"):
                    while (cur_char := peek()) != "\n":
                        advance()
                    advance()
                else:
                    tokens.append(eat_operator())
            case '"':
                tokens.append(eat_str())
            case _:
                if cur_char in OPERATOR_CHR_FIRST:
                    tokens.append(eat_operator())
                else:
                    tokens.append(eat_symbol())

        skip()
    return tokens


class Literal(NamedTuple):
    value: Any
    type: Type


class ID(NamedTuple):
    name: str


type Atom = Literal | ID


class UnaryOp(Enum):
    NEG = auto()
    NOT = auto()


class BinaryOp(Enum):
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    MOD = auto()
    POW = auto()

    IADD = auto()
    ISUB = auto()
    IMUL = auto()
    IDIV = auto()
    IMOD = auto()
    IPOW = auto()

    EQ = auto()
    NE = auto()

    LT = auto()
    GT = auto()
    LE = auto()
    GE = auto()

    AND = auto()
    OR = auto()

    DOT = auto()
    INDEX = auto()


class Unary(NamedTuple):
    op: UnaryOp
    expr: Expr


class Binary(NamedTuple):
    left: Expr
    op: BinaryOp
    right: Expr


class Call(NamedTuple):
    callee: Expr
    args: List[Expr]


type Expr = Atom | Unary | Binary | Call


class Type(NamedTuple):
    name: str


class Block(NamedTuple):
    stmts: List[Stmt]


class IfStmt(NamedTuple):
    cond: Expr
    body: Stmt
    or_else: Block


class WhileStmt(NamedTuple):
    cond: Expr
    body: Stmt


class ConstantDecl(NamedTuple):
    name: str
    tp: Type
    value: Expr


class VarDecl(NamedTuple):
    name: str
    tp: Type
    value: Expr


class FnDecl(NamedTuple):
    name: str
    params: List[FnParam]
    ret: Type
    body: Block


class FnParam(NamedTuple):
    name: str
    tp: Type


class ModDecl(NamedTuple):
    name: str


class UseDecl(NamedTuple):
    name: str


class ExprStmt(NamedTuple):
    expr: Expr


type Stmt = Block | IfStmt | WhileStmt | ConstantDecl | VarDecl | FnDecl | ModDecl | UseDecl | ExprStmt

INT_TYPE = Type("int")
FLOAT_TYPE = Type("float")
STR_TYPE = Type("str")
BOOL_TYPE = Type("bool")

UNKNOWN_TYPE = Type("unknown")

PRECEDENCE_LOWEST = 10
PRECEDENCE = {
    "!": 1,
    "-": 1,
    ".": 2,
    "^": 3,
    "*": 4,
    "/": 4,
    "%": 4,
    "+": 5,
    "-": 5,
    "==": 6,
    "!=": 6,
    "<": 6,
    ">": 6,
    "<=": 6,
    ">=": 6,
    "=": 7,
    "+=": 7,
    "-=": 7,
    "*=": 7,
    "/=": 7,
    "%=": 7,
    "^=": 7,
}

type PrefixFn = Callable[[Expr], Expr]


class Parser:
    def __init__(self, tokens: list[Tok]) -> None:
        self.tokens = tokens
        self.cur_pos = -1
        self.cur_tok: Tok
        self.peek_tok: Tok | None = None

        self.next_token()
        # self.next_token()

        self.prefix_fn: dict[str, PrefixFn] = {}

        self.register_prefix_fn("+", self.parse_add)
        self.register_prefix_fn("-", self.parse_sub)
        self.register_prefix_fn("*", self.parse_mul)
        self.register_prefix_fn("/", self.parse_div)

    def err(self, msg: str) -> Never:
        raise Exception(msg)

    def eof(self) -> bool:
        return self.cur_pos + 1 >= len(self.tokens)

    def next_token(self) -> None:
        if self.cur_pos + 1 < len(self.tokens):
            self.cur_pos += 1
            self.cur_tok = self.tokens[self.cur_pos]
            self.peek_tok = (
                self.tokens[self.cur_pos + 1]
                if self.cur_pos + 1 < len(self.tokens)
                else None
            )
        # else:
        #     self.err("Unexpected end of file")

    def get_tok_type(self, token: Tok) -> str:
        if token[0] == "operator":
            return token[1]
        elif token[0] == "keyword":
            return token[1]
        else:
            return token[0]

    def register_prefix_fn(self, type: str, fn: PrefixFn) -> None:
        if type in self.prefix_fn:
            self.err(f"Prefix function for {type} already registered")
        else:
            self.prefix_fn[type] = fn

    def get_prefix_fn(self) -> PrefixFn:
        cur_tok_type = self.get_tok_type(self.cur_tok)
        return self.prefix_fn[cur_tok_type]

    def eat(self, value: str):
        if self.cur_tok_is(value):
            self.next_token()
        else:
            self.err(f"Expected {type} {value} but got {self.cur_tok}")

    def cur_tok_is(self, value: str) -> bool:
        return self.get_tok_type(self.cur_tok) == value

    def parse(self) -> Generator[Stmt, Any, None]:
        while not self.eof():
            yield self.parse_stmt()

    def parse_stmt(self) -> Stmt:
        tok_tp = self.get_tok_type(self.cur_tok)
        match tok_tp:
            case "let":
                return self.parse_let_stmt()
            case "while":
                return self.parse_while_stmt()
            case "if":
                return self.parse_if_stmt()
            case "fn":
                return self.parse_fn_decl()
            case "mod":
                return self.parse_mod_decl()
            case "use":
                return self.parse_use_decl()
            case "break":
                return self.parse_break_stmt()
            case "continue":
                return self.parse_continue_stmt()
            case _:
                return self.parse_expr_stmt()

    def parse_expr_stmt(self) -> Stmt:
        expr = self.parse_expr(PRECEDENCE_LOWEST)
        # optional semicolon
        if self.cur_tok_is(";"):
            self.next_token()
        return ExprStmt(expr)

    def parse_expr(self, precedence: int) -> Expr:
        left = self.parse_infix()
        while (
            self.cur_tok
            and PRECEDENCE.get(self.get_tok_type(self.cur_tok), PRECEDENCE_LOWEST)
            < precedence
        ):
            prefix_fn = self.get_prefix_fn()
            left = prefix_fn(left)
        return left

    def parse_atom(self) -> Atom:
        cur_tok = self.cur_tok
        match self.cur_tok[0]:
            case "bool":
                self.next_token()
                return Literal(bool(cur_tok[1]), BOOL_TYPE)
            case "int":
                self.next_token()
                return Literal(int(cur_tok[1]), INT_TYPE)
            case "float":
                self.next_token()
                return Literal(float(cur_tok[1]), FLOAT_TYPE)
            case "str":
                self.next_token()
                return Literal(cur_tok[1], STR_TYPE)
            case "symbol":
                self.next_token()
                return ID(str(cur_tok[1]))
            case _:
                self.err(f"Unexpected token: {self.cur_tok}")

    def parse_infix(self) -> Expr:
        match self.cur_tok[0]:
            case "operator":
                match self.cur_tok[1]:
                    case "(":
                        self.next_token()
                        expr = self.parse_expr(PRECEDENCE_LOWEST)
                        self.eat(")")
                        return expr
                    case "-":
                        self.next_token()
                        return Unary(UnaryOp.NEG, self.parse_expr(PRECEDENCE["-"]))
                    case _:
                        self.err(f"Unexpected operator: {self.cur_tok[1]}")
            case "keyword":
                match self.cur_tok[1]:
                    case "not":
                        self.next_token()
                        return Unary(UnaryOp.NOT, self.parse_expr(PRECEDENCE["!"]))
                    case _:
                        self.err(f"Unexpected keyword: {self.cur_tok[1]}")
            case _:
                return self.parse_atom()

    def parse_add(self, lhs: Expr) -> Expr:
        self.eat("+")
        return Binary(lhs, BinaryOp.ADD, self.parse_expr(PRECEDENCE["+"]))

    def parse_sub(self, lhs: Expr) -> Expr:
        self.eat("-")
        return Binary(lhs, BinaryOp.ADD, self.parse_expr(PRECEDENCE["-"]))

    def parse_mul(self, lhs: Expr) -> Expr:
        self.eat("*")
        return Binary(lhs, BinaryOp.MUL, self.parse_expr(PRECEDENCE["*"]))

    def parse_div(self, lhs: Expr) -> Expr:
        self.eat("/")
        return Binary(lhs, BinaryOp.DIV, self.parse_expr(PRECEDENCE["/"]))

# from parse import tokenize, Parser

print(list(Parser(tokenize("(1+2)*3")).parse()))


# a = [
#     ExprStmt(
#         expr=Binary(
#             left=Binary(
#                 left=Literal(value=1, type=Type(name="int")),
#                 op=BinaryOp.ADD,
#                 right=Literal(value=2, type=Type(name="int")),
#             ),
#             op=BinaryOp.MUL,
#             right=Literal(value=3, type=Type(name="int")),
#         )
#     )
# ]
