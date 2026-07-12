from lex import *
from parse import *

lexer = Lexer()
lexer.ignore = [" ", "\n", "\r", "\t"]

@lexer.pattern(",")
def comma(lexer):
    return Token("comma", None)
@lexer.pattern("\\[")
def lbracket(lexer):
    return Token("lbracket", None)
@lexer.pattern("\\]")
def rbracket(lexer):
    return Token("rbracket", None)

@lexer.pattern("\\-?[0-9](\\.[0-9][0-9]*)?")
def number(lexer):
    string = lexer.buffer
    return Token("number", int(string) if string.isdigit() or string.replace("-", "").isdigit() else float(string))

@lexer.eof()
def eof(lexer):
    return Token("$", None)

lexer.compile()

parser = Parser()
parser.set_terminal(["number", "comma", "lbracket", "rbracket", "$"])

@parser.pattern("S -> Array")
def S(parser, args):
    return args[0]

@parser.pattern("Array -> lbracket [Number (comma Number)*] rbracket", option = "NT")
def Array(parser, args):
    return args[0]

@parser.pattern("Number -> number")
def Number(parser, args):
    return args[0].value

parser.compile()

text = "[1, 2, 3]"
lexer.read(text)
parser.read(lexer)
print(parser.parse())