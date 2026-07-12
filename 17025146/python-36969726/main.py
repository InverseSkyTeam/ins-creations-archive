# Token定义
INT,ADD,SUB,MUL,DIV,END,LBR,RBR = "INT","ADD","SUB","MUL","DIV","END","LBR","RBR"

# 词法分析

class Token():
    def __init__(self,_type,value = None):
        self._type = _type
        self.value = value

class Lexer():
    def __init__(self,expr):
        self.expr = expr
        self.position = 0
        self.char = self.expr[self.position]

    def error(self):
        raise SyntaxError("表达式错误")

    def advance(self):
        self.position += 1
        if self.position >= len(self.expr):
            self.char = None
        else:
            self.char = self.expr[self.position]

    def cross_space(self):
        while True:
            if self.char != None and self.char.isspace():
                self.advance()
            else:
                break

    def get_int(self):
        res = ""
        while True:
            if self.char != None and self.char.isdigit():
                res += self.char
                self.advance()
            else:
                break
        return int(res)
    
    def get_token(self):
        while self.char:
            if self.char.isspace():
                self.cross_space()
                continue
            elif self.char.isdigit():
                longint = self.get_int()
                return Token(INT,longint)
            elif self.char == "+":
                self.advance()
                return Token(ADD,"+")
            elif self.char == "-":
                self.advance()
                return Token(SUB,"-")
            elif self.char == "*":
                self.advance()
                return Token(MUL,"*")
            elif self.char == "/":
                self.advance()
                return Token(DIV,"/")
            elif self.char == "(":
                self.advance()
                return Token(LBR,"(")
            elif self.char == ")":
                self.advance()
                return Token(RBR,")")
            else:
                self.error()
        return Token(END)


# 语法分析
class AST():
    pass

class Number(AST):
    def __init__(self,token):
        self.token = token
        self.value = token.value

class BinOperate(AST):
    def __init__(self,left,operate,right):
        self.left = left
        self.right = right
        self.op = self.token = operate

class Parser():
    def __init__(self,lexer):
        self.lexer = lexer
        self.token = self.lexer.get_token()

    def error(self):
        raise SyntaxError("表达式错误")

    def judg(self,_type):
        if self.token._type == _type:
            self.token = self.lexer.get_token()
        else:
            self.error()

    def factor(self):
        token = self.token
        if token._type == INT:
            self.judg(INT)
            return Number(token)
        if token._type == LBR:
            self.judg(LBR)
            res = self.calc()
            self.judg(RBR)
            return res

    def term(self):
        node = self.factor()
        while True:
            if self.token._type in (MUL,DIV):
                operate = self.token
                if operate._type == MUL:
                    self.judg(MUL)
                if operate._type == DIV:
                    self.judg(DIV)
                node = BinOperate(node,operate,self.factor())
            else:
                break
        return node

    def calc(self):
        node = self.term()
        while True:
            if self.token._type in (ADD,SUB):
                operate = self.token
                if operate._type == ADD:
                    self.judg(ADD)
                if operate._type == SUB:
                    self.judg(SUB)
                node = BinOperate(node,operate,self.term())
            else:
                break
        return node

    def tree(self):
        return self.calc()


# 解释器
class Interpreter():
    def __init__(self,parser):
        self.parser = parser

    def visit(self,node):
        method = type(node).__name__
        visitor = getattr(self,"visit_" + method)
        return visitor(node)

    def visit_BinOperate(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if node.op._type == ADD:
            return left + right
        if node.op._type == SUB:
            return left - right
        if node.op._type == MUL:
            return left * right
        if node.op._type == DIV:
            return left // right
        # else:
        #     return node.op

    def visit_Number(self,node):
        return node.value

    def interpret(self):
        tree = self.parser.tree()
        return self.visit(tree)

while True:
    expr = input("输入表达式:")
    lexer = Lexer(expr)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    print(interpreter.interpret())