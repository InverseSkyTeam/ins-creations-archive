import sys

INT = 'INT'
PLUS = '+'
MINUS = '-'
MUL = '*'
DIV = '/'
LPAREN = '('
RPAREN = ')'
EOF = 'EOF'

class Token(object):
    def __init__(self,tp,value):
        self.tp = tp
        self.value = value
    def __str__(self):
        return 'Token({tp},{value})'.format(tp=self.tp,value=self.value)
    __repr__=__str__



class Lexer(object):
    def __init__(self,code):
        self.code = code
        self.position = 0
        self.current_char = self.code[self.position]
    
    def error(self):
        raise Exception('Return an error from lexer.')
    
    def advance(self):
        self.position += 1
        if self.position >= len(self.code):
            self.current_char = None
        else:
            self.current_char = self.code[self.position]
    
    def skip_whitespace(self):
        while (self.current_char is not None) and self.current_char.isspace():
            self.advance()
    
    def long_integer(self):
        result = ''
        while (self.current_char is not None) and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)
    
    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return Token(INT, self.long_integer())
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, self.current_char)
            if self.current_char == '-':
                self.advance()
                return Token(MINUS, self.current_char)
            if self.current_char == '*':
                self.advance()
                return Token(MUL, self.current_char)
            if self.current_char == '/':
                self.advance()
                return Token(DIV, self.current_char)
            if self.current_char == '(':
                self.advance()
                return Token(LPAREN, self.current_char)
            if self.current_char == ')':
                self.advance()
                return Token(RPAREN, self.current_char)
            self.error()
        return Token(EOF, None)



class AST(object):
    pass

class UnaryOp(AST):  # 一元
    def __init__(self,op,expr):
        self.token = self.op = op
        self.expr = expr

class BinOp(AST):   # 二元
    def __init__(self,left,op,right):
        self.left = left
        self.token = self.op = op
        self.right = right

class Num(AST):    # 数字
    def __init__(self,token):
        self.token = token
        self.value = token.value

class Parser:
    def __init__(self,lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    
    def error(self):
        raise Exception('Return an error from parser.')
    
    def eat(self,token_type):
        if self.current_token.tp == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()
    
    def factor(self):
        token = self.current_token
        if token.tp in (PLUS,MINUS):
            self.eat(token.tp)
            node = UnaryOp(token,self.factor())
            return node
        if token.tp == INT:
            self.eat(INT)
            return Num(token)
        elif token.tp == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node
    
    def term(self):
        node = self.factor()
        while (self.current_token.tp in (MUL,DIV)):
            token = self.current_token
            if token.tp == MUL:
                self.eat(MUL)
            if token.tp == DIV:
                self.eat(DIV)
            node = BinOp(left=node,op=token,right=self.factor())
        return node
        
    def expr(self):
        node = self.term()
        while (self.current_token.tp in (PLUS,MINUS)):
            token = self.current_token
            if token.tp == PLUS:
                self.eat(PLUS)
            if token.tp == MINUS:
                self.eat(MINUS)
            node = BinOp(left=node,op=token,right=self.term())
        return node
    
    def parse(self):
        return self.expr()



class NodeVisitor(object):
    def visit(self,node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self,node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

class Interpreter(NodeVisitor):
    def __init__(self,parser):
        self.parser = parser
    
    def visit_BinOp(self,node):
        if node.op.tp == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.tp == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.tp == MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.tp == DIV:
            return self.visit(node.left) / self.visit(node.right)
    
    def visit_UnaryOp(self,node):
        if node.op.tp == PLUS:
            return +self.visit(node.expr)
        elif node.op.tp == MINUS:
            return -self.visit(node.expr)
    
    def visit_Num(self,node):
        return node.value
    
    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)



while True:
    try:
        text = input('>>>')
    except EOFError:
        break
    if not text:
        continue
    lexer = Lexer(text)    # [code->token]
    parser = Parser(lexer) # [token->AST]
    interpreter = Interpreter(parser) # [AST->Tree]
    result = interpreter.interpret()  # [CalcTree]
    print(text,'=',result)