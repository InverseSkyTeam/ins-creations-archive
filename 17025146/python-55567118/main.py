from lex import *
from parse import *

lexer = Lexer()
@lexer.pattern("a|b")
def fn(lexer):
    return Token(lexer.buffer, None)
@lexer.eof()
def fn(lexer):
    return Token("$", None)
lexer.compile()

parser = Parser()
parser.terminals = ["a", "$"]
@parser.pattern("S -> X")
def S(args):
    return args[0]
@parser.pattern("X -> A | B")
def X(args):
    return args[0]
@parser.pattern("A -> a")
def A(args):
    return ("A", args[0])
@parser.pattern("B -> a")
def B(args):
    return ("B", args[0])
parser.compile()

lexer.read("a")
parser.read(lexer)
print(parser.parse())