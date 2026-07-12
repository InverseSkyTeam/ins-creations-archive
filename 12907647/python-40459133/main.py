from collections import OrderedDict
from enum import Enum
import sys

# class TokenType(Enum):
#     PLUS = '+'
#     MINUS = '-'
#     MUL = '*'
#     DIV = '/'
#     LPAREN = '('
#     RPAREN = ')'
#     POINT = '.'
#     COMMA = ','
#     COLON = ':'
#     EQUAL = '='
#     LESST = '<'  # less than
#     MORET = '>'
    
#     PROGRAM = 'PROGRAM'
#     INT = 'INT'
#     STR = 'STR'
#     AND = 'AND'
#     OR = 'OR'
#     NOT = 'NOT'
#     END = 'END'
    
#     LESST_EQUAL = '<='
#     MORET_EQUAL = '>='
#     EOF = 'EOF'

INTEGER = 'INTEGER'
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
    
    def advance(self):   # 跳到下一字符
        self.position += 1
        if self.position >= len(self.code):
            self.current_char = None
        else:
            self.current_char = self.code[self.position]
    
    def skip_whitespace(self):
        while (self.current_char is not None) and self.current_char.isspace():
            self.advance()
    
    def long_integer(self):  # 获取多位数字
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
                return Token(INTEGER, self.long_integer())
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

class Interpreter(object):
    def __init__(self,lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
    
    def error(self):
        raise Exception('Return an error during running.')
    
    def eat(self,token_type):
        if (self.current_token.tp == token_type):
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()
    
    def factor(self):    # 计算整数、括号内的表达式(优先级0)
        current_token = self.current_token
        if current_token.tp == INTEGER:
            self.eat(INTEGER)
            return current_token.value
        elif current_token.tp == LPAREN:
            self.eat(LPAREN)  # 吃掉左括号
            result = self.expr()   # 计算括号内并吃掉
            self.eat(RPAREN)  # 肝掉右括号
            return result   # 返回括号表达式值
        else:
            self.error()
    
    def term(self):   # 计算乘除(优先级1)
        # 堆栈:[]
        result = self.factor()  # 堆[整数]
        
        while self.current_token.tp in (MUL,DIV):  # 堆[符号][整数]
            token = self.current_token
            if token.tp == MUL:
                self.eat(MUL)
                result *= self.factor()
            if token.tp == DIV:
                self.eat(DIV)
                result /= self.factor()
        
        return result
        
    def expr(self):   # 计算加减(优先级2)
        # 堆栈:[]
        result = self.term()  # 堆[整数]
        
        while self.current_token.tp in (PLUS,MINUS):  # 堆[符号][整数]
            token = self.current_token
            if token.tp == PLUS:
                self.eat(PLUS)
                result += self.term()
            if token.tp == MINUS:
                self.eat(MINUS)
                result -= self.term()
        
        return result


while True:
    try:
        text = input('>>>')
    except EOFError:
        break
    if not text:
        continue
    lexer = Lexer(text)   # 词法分析(code->Token)
    interpreter = Interpreter(lexer)    # 解释器(Token->run)
    result = interpreter.expr()
    print(text,'=',result)