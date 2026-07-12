"""
也罢，用一种伪高速的方法吧
说慢也不慢，在非极限情况下还是可以工作良好的
如果你改变第一行，然后移动到最后一行，这时会进行全文重新分析
连续编辑的时候每次最多分析一屏
"""

from enum import Enum, unique
from copy import deepcopy
from rain import TokenType

RAIN_OPS = "+-*/%><=!~^&@:;()[]{},."


@unique
class RainTok(Enum):
    Id = 0
    Num = 2
    Str = 3
    Op = 5
    Kw = 6
    Err = 7
    Other = 8
    Comment = 9


rain_tok2hl = {
    RainTok.Id: "identifier",
    RainTok.Num: "number",
    RainTok.Str: "string",
    RainTok.Op: "operator",
    RainTok.Kw: "keyword",
    RainTok.Err: "error",
    RainTok.Other: "others",
    RainTok.Comment: "comment",
}

RAIN_KWS = {
    "end": TokenType.END,
    "and": TokenType.AND,
    "or": TokenType.OR,
    "not": TokenType.NOT,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "while": TokenType.WHILE,
    "for": TokenType.FOR,
    "to": TokenType.TO,
    "in": TokenType.IN,
    "return": TokenType.RETURN,
    "break": TokenType.BREAK,
    "continue": TokenType.CONTINUE,
    "var": TokenType.VAR,
    "func": TokenType.FUNC,
    "True": TokenType.TRUE,
    "False": TokenType.FALSE,
    "None": TokenType.NONE,
    "step": TokenType.STEP,
    "elif": TokenType.ELIF,
    "module": TokenType.MODULE,
    "require": TokenType.REQUIRE,
}.keys()


@unique
class RainLineState(Enum):
    Unknown = 0
    Str = 2
    Null = 3
    Str1 = 5


class RainLexer:
    def __init__(self, code: list[list[list[str]]]):
        self.code = code
        self.lex_buf = []
        self.line_states = []
        self.unlexed_begin = 0

        self.lex(len(code))

    def inc_pos(self, y, x):
        if x < len(self.code[y[0]][y[1]]) - 1:
            x += 1
        elif y[1] < len(self.code[y[0]]) - 1:
            y[1] += 1
            x = 0
        elif x == len(self.code[y[0]][y[1]]) - 1:
            x += 1
        elif y[0] < len(self.code) - 1:
            y[0] += 1
            y[1] = x = 0
        return y, x

    def get_cur(self, y, x):
        if x < len(self.code[y[0]][y[1]]):
            return self.code[y[0]][y[1]][x]
        elif y[0] < len(self.code) - 1:
            return "\n"
        return None

    def get_last_state(self, line: int):
        if line == 0:
            return RainLineState.Null
        else:
            return self.line_states[line - 1]

    def process_line(self, line: int):
        def next():
            nonlocal y, x, cur
            # print(cur, end='')
            y, x = self.inc_pos(y, x)
            cur = self.get_cur(y, x)

        y, x = [line, 0], 0
        cur = self.get_cur(y, x)

        last_state = self.get_last_state(line)
        if last_state in (
            RainLineState.Str,
            RainLineState.Str1,
        ):
            if last_state == RainLineState.Str1:
                q = '"'
            else:
                q = "'"
            tp = 1
            q_cnt = 0
            while cur not in ("\n", None) and q_cnt != tp:
                if cur == "\\":
                    self.lex_buf[y[0]][y[1]][x] = RainTok.Str
                    next()
                    if cur == "\n":
                        self.line_states[line] = (
                            RainLineState.Str
                            if q == "'"
                            else RainLineState.Str1
                        )
                        return
                    self.lex_buf[y[0]][y[1]][x] = RainTok.Str
                    next()
                elif cur == q:
                    q_cnt += 1
                    self.lex_buf[y[0]][y[1]][x] = RainTok.Str
                    next()
                else:
                    self.lex_buf[y[0]][y[1]][x] = RainTok.Str
                    next()
            if cur == "\n" and q_cnt < tp:
                self.line_states[line] = (
                    RainLineState.Str if q == "'" else RainLineState.Str1
                )

        while cur not in ("\n", None):
            if cur.isalnum() or cur == "_":
                begin = deepcopy(y), x
                s = ""
                while cur and (cur.isalnum() or cur == "_"):
                    s += cur
                    next()
                if s[0].isdigit():
                    if not s.isdecimal():
                        tp = RainTok.Err
                    else:
                        tp = RainTok.Num
                elif s in RAIN_KWS:
                    tp = RainTok.Kw
                else:
                    tp = RainTok.Id
                while begin != (y, x):
                    self.lex_buf[begin[0][0]][begin[0][1]][begin[1]] = tp
                    begin = self.inc_pos(*begin)
            elif cur in RAIN_OPS:
                self.lex_buf[y[0]][y[1]][x] = RainTok.Op
                next()
            elif cur.isspace():
                self.lex_buf[y[0]][y[1]][x] = RainTok.Other
                next()
            elif cur in "'\"":
                q = cur
                tp = 1
                self.lex_buf[y[0]][y[1]][x] = RainTok.Str
                next()
                q_cnt = 0
                while cur not in ("\n", None) and q_cnt != tp:
                    if cur == "\\":
                        self.lex_buf[y[0]][y[1]][x] = RainTok.Str
                        next()
                        if cur == "\n":
                            self.line_states[line] = (
                                RainLineState.Str
                                if q == "'"
                                else RainLineState.Str1
                            )
                            return
                        self.lex_buf[y[0]][y[1]][x] = RainTok.Str
                        next()
                    elif cur == q:
                        q_cnt += 1
                        self.lex_buf[y[0]][y[1]][x] = RainTok.Str
                        next()
                    else:
                        self.lex_buf[y[0]][y[1]][x] = RainTok.Str
                        next()
                if cur == "\n" and q_cnt < tp:
                    self.line_states[line] = (
                        RainLineState.Str if q == "'" else RainLineState.Str1
                    )
            elif cur == "#":
                while cur and cur != "\n":
                    self.lex_buf[y[0]][y[1]][x] = RainTok.Comment
                    next()
            else:
                self.lex_buf[y[0]][y[1]][x] = RainTok.Err
                next()
        # print(cur)

    def lex(self, target: int):
        if target < self.unlexed_begin:
            return
        del self.lex_buf[self.unlexed_begin :]
        del self.line_states[self.unlexed_begin :]
        for line in range(self.unlexed_begin, target):
            self.lex_buf.append([])
            self.line_states.append(RainLineState.Unknown)
            for i in self.code[line]:
                self.lex_buf[-1].append([])
                for j in i:
                    self.lex_buf[-1][-1].append(None)
            self.process_line(line)
        self.unlexed_begin = target

    def change(self, y):
        if y[0] < self.unlexed_begin:
            self.unlexed_begin = y[0]

    def get(self, y, x):
        return self.lex_buf[y[0]][y[1]][x]
