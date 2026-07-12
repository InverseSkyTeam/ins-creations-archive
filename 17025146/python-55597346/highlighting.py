import keyword
builtins = dir(__builtins__) # 内置函数
keywords = keyword.kwlist # 关键字

NUMBER,BUILTIN,KEYWORD,STRING = "NUMBER","BUILTIN","KEYWORD","STRING"
OTHER = "OTHER"
class Token():
    def __init__(self,tp,value):
        self.tp = tp
        self.value = value
        self.color = None
        
    def __str__(self):
        return f"({self.tp} , {self.value})"
    __repr__ = __str__
        
class Scanner():
    def __init__(self,code):
        self.code = code
        self.pos = 0
        self.char = code[0]
    def advance(self):
        self.pos += 1
        if self.pos < len(self.code):
            self.char = self.code[self.pos]
        else:
            self.char = None
    def get_token(self):
        while self.char:
            if self.char.isdigit():
                res = ""
                while self.char.isdigit() or self.char == ".":
                    res += self.char
                    self.advance()
                return Token(NUMBER,res)
            elif self.char == '"' or self.char == "'" or self.char == '"""':
                quot = self.char
                self.advance()
                res = quot
                while self.char != quot and self.char:
                    res += self.char
                    self.advance()
                self.advance()
                res += quot
                return Token(STRING,res)
            elif self.char.isalpha():
                res = ""
                while self.char.isalnum():
                    res += self.char
                    self.advance()
                if res in builtins:
                    return Token(BUILTIN,res)
                elif res in keywords:
                    return Token(KEYWORD,res)
                else:
                    return Token(OTHER,res)
            else:
                char = self.char
                self.advance()
                return Token(OTHER,char)
    def tokens(self):
        ret = []
        while self.char:
            ret.append(self.get_token())
        return ret

colortable = {
    NUMBER:"\033[96m",
    STRING:"\033[92m",
    BUILTIN:"\033[94m",
    KEYWORD:"\033[95m",
    OTHER:"\033[97m"
}
def color(tokens):
    for token in tokens:
        token.color = colortable[token.tp]

def output(tokens):
    for token in tokens:
        if token.value:
            print(token.color + token.value,end = "")

def newprint(code):
    scanner = Scanner(code)
    tokens = scanner.tokens()
    color(tokens)
    output(tokens)