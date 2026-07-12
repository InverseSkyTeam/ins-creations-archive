from lex import *
from parse import *

lexer = Lexer()
lexer.ignore = [" ", "\n", "\r", "\t"]

@lexer.pattern(",")
@lexer.pattern(":")
@lexer.pattern("\\{")
@lexer.pattern("\\}")
@lexer.pattern("\\[")
@lexer.pattern("\\]")
def symbol(lexer):
    return (lexer.buffer, None)

@lexer.pattern('"[^"]*"')
def string(lexer):
    return ("STRING", lexer.buffer[1:-1])

@lexer.pattern("\\-?[0-9](\\.[0-9][0-9]*)?")
def number(lexer):
    string = lexer.buffer
    return ("NUMBER", int(string) if string.isdigit() or string.replace("-", "").isdigit() else float(string))

@lexer.pattern("true")
def true(lexer):
    return ("TRUE", True)
@lexer.pattern("false")
def false(lexer):
    return ("FALSE", False)
@lexer.pattern("null")
def null(lexer):
    return ("NULL", None)

@lexer.eof()
def eof(lexer):
    return ("$", None)


parser = Parser()
parser.set_terminal(["{", "}", "[", "]", ":", ",", "$", "STRING", "NUMBER", "TRUE", "FALSE", "NULL"])

@parser.pattern("S'", ["S"])
def S_(parser, args):
    pass
@parser.pattern("S", ["Value"])
def S(parser, args):
    return args[0]

@parser.pattern("Value", ["Object"])
@parser.pattern("Value", ["Array"])
def Value_nt(parser, args):
    return args[0]
@parser.pattern("Value", ["STRING"])
def Value_s(parser, args):
    return args[0][1].replace("\\\\", "\\")
@parser.pattern("Value", ["NUMBER"])
@parser.pattern("Value", ["TRUE"])
@parser.pattern("Value", ["FALSE"])
@parser.pattern("Value", ["NULL"])
def Value_t(parser, args):
    return args[0][1]

@parser.pattern("Object", ["{", "ObjItems", "}"])
def Object(parser, args):
    obj = {}
    for key, value in args[1]:
        obj[key] = value
    return obj

@parser.pattern("ObjItems", ["ObjItems", ",", "Pair"])
def ObjItems(parser, args):
    return args[0] + [args[2]]
@parser.pattern("ObjItems", ["Pair"])
def ObjItems_t(parser, args):
    return [args[0]]

@parser.pattern("Pair", ["STRING", ":", "Value"])
def Pair(parser, args):
    return (args[0][1], args[2])

@parser.pattern("Array", ["[", "ArrayItems", "]"])
def Array(parser, args):
    return args[1]

@parser.pattern("ArrayItems", ["ArrayItems", ",", "Value"])
def ArrayItems(parser, args):
    return args[0] + [args[2]]
@parser.pattern("ArrayItems", ["Value"])
def ArrayItems_t(parser, args):
    return [args[0]]

@parser.error
def error(parser):
    print("Syntax error at", parser.token)
    exit(0)

lexer.compile()
parser.compile()

with open("./test.json", "r") as f:
    text = f.read()
lexer.read(text)
parser.read(lexer)
print(parser.parse())