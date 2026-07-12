from lex import *

lexer = Lexer()
lexer.ignore = [" "]

@lexer.pattern("\\+")
@lexer.pattern("\\-")
@lexer.pattern("\\*")
@lexer.pattern("/")
@lexer.pattern("\\(")
@lexer.pattern("\\)")
def symbol(lexer):
    return (lexer.buffer, None)

@lexer.pattern("[0-9](\\.[0-9][0-9]?)?")
def number(lexer):
    return ("NUMBER", int(lexer.buffer) if lexer.buffer.isdigit() else float(lexer.buffer))

@lexer.eof()
def eof(lexer):
    return ("$", None)

@lexer.undefined
def undefined(lexer):
    print("Undefined token:", lexer.buffer)
    print("Line: " + str(lexer.line) + ", Column: " + str(lexer.column))
    exit(0)

lexer.compile()



from parse import *

parser = Parser()
terminals = [
    "NUMBER", "+", "-", "*", "/", "(", ")", "$"
]
priories = {
    "+": (1, "LEFT"),
    "-": (1, "LEFT"),
    "*": (0, "LEFT"),
    "/": (0, "LEFT")
}
parser.set_terminal(terminals)
parser.set_priority(priories)
parser.byte_code = []

@parser.pattern("S'", ["S"])
def S_(parser):
    pass

@parser.pattern("S", ["Expr"])
def S(parser):
    parser.byte_code.append(("PRINT", None))

@parser.pattern("Expr", ["Expr", "+", "Expr"])
def Expr_add(parser):
    parser.byte_code.append(("ADD", None))

@parser.pattern("Expr", ["Expr", "-", "Expr"])
def Expr_sub(parser):
    parser.byte_code.append(("SUB", None))

@parser.pattern("Expr", ["Expr", "*", "Expr"])
def Expr_mul(parser):
    parser.byte_code.append(("MUL", None))

@parser.pattern("Expr", ["Expr", "/", "Expr"])
def Expr_div(parser):
    parser.byte_code.append(("DIV", None))

@parser.pattern("Expr", ["(", "Expr", ")"])
def Expr_group(parser):
    pass

@parser.pattern("Expr", ["NUMBER"])
def Expr_num(parser):
    parser.byte_code.append(("LOAD_CONST", parser.buffer[1]))

@parser.error
def error(parser):
    print("Syntax error: " + parser.token[0])
    print("Line: " + str(parser.lexer.line) + ", Column: " + str(parser.lexer.column))
    exit(0)

parser.compile()


from qvm import *
lexer.read('(1 + 2) * 3')
parser.read(lexer)
parser.parse()
run(parser.byte_code)