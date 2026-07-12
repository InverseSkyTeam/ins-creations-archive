from typing import Union,Optional
from config import *

#Token定义{
class Token():
    def __init__(self, tp, value, line:Optional[int] = None, column:Optional[int]=None) -> None:
        self.tp = tp
        self.value = value
        self.line = line
        self.column = column

    def __str__(self)-> str:
        msg = f"Token({self.tp}, {self.value}, position={self.line}:{self.column})" if self.line and self.column else f"Token({self.tp}, {self.value})"
        return msg

    __repr__ = __str__
#}
#Scanner扫描器{
class Scanner():
    def __init__(self,code):
        self.code = code
        self.pos = 0
        self.char = self.code[self.pos]
        self.line = 1
        self.column = 1

    def advance(self,num = 1):
        for _i in range(num):
            if self.char == "\n":
                self.line += 1
                self.column = 0
            self.pos += 1
            if self.pos < len(self.code):
                self.char = self.code[self.pos]
                self.column += 1
            else:
                self.char = None

    def back(self,num = 1):
        for _i in range(num):
            self.pos -= 1
            if self.pos >= 0:
                self.char = self.code[self.pos]
            if self.char == "\n":
                self.line -= 1
                self.column = 0
                pos = self.pos
                char = self.code[pos - 1]
                while char != "\n":
                    self.column += 1
                    pos -= 1
                    char = self.code[pos]
            else:
                self.column -= 1

    def peek(self,num = 1):
        return self.code[self.pos + 1:self.pos + num + 1]

    def setpos(self,value):
        self.pos = value
        self.char = self.code[self.pos]

    def iseof(self):
        return self.pos >= len(self.code)
#}
#Tokenizer有限状态机{
class Tokenizer():
    def __init__(self, code,config):
        self.scanner = Scanner(code)
        self.config:dict = config["states"]
        self.init = config["initial"]
        self.state = self.init
        self.buffer = ""
        self.tokens = []

    def error(self):
        raise Exception("Tokenizer Error")

    def add(self,states):
        tp = states["token"]
        value = self.buffer
        line = self.scanner.line
        column = self.scanner.column
        self.tokens.append(Token(tp,value,line,column))

    def reset(self):
        self.state = self.init
        self.buffer = ""

    def get_token(self):
        while self.scanner.char:
            if self.scanner.char.isspace() and self.scanner.char != "\n" and self.state == State.INIT:
                self.scanner.advance()
            state = self.config[self.state]
            trans = state["trans"]
            if not trans:
                if state["isend"]:
                    self.add(state)
                    self.reset()
                    continue
                else:
                    self.error()
            transable = False
            for i in trans:
                checker = i["checker"]
                if isinstance(checker,str):
                    transable = checker == self.scanner.char
                elif isinstance(checker, re.Pattern):
                    transable = checker.match(self.scanner.char)
                else:
                    transable = checker(self.scanner.char)
                if transable:
                    target = i["state"]
                    break
            if transable:
                self.state = target
                self.buffer += self.scanner.char
                self.scanner.advance()
            else:
                if state["isend"]:
                    self.add(state)
                    self.reset()
                    continue
                else:
                    self.error()
        state = self.config[self.state]
        self.add(state)
        self.tokens.append(Token(TokenType.END,""))
#}

code = "1 + 1 + 2"
t = Tokenizer(code,CONFIG)
t.get_token()
print(t.tokens)