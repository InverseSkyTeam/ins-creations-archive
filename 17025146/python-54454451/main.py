from parse import *

parser = Parser()

parser.set_terminal(["+", "-", "*", "/", "1", "2", "3"])
parser.set_priority({
    "+": (1, "LEFT"),
    "-": (1, "LEFT"),
    "*": (0, "LEFT"),
    "/": (0, "LEFT")
})

@parser.pattern(Product("S'", ["S"]))
def S_(stack, x):
    pass

@parser.pattern(Product("S", ["Expr"]))
def S(stack, x):
    print(stack.pop())

@parser.pattern(Product("Expr", ["Expr", "+", "Expr"]))
def Expr_add(stack, x):
    stack.append(stack.pop() + stack.pop())

@parser.pattern(Product("Expr", ["Expr", "-", "Expr"]))
def Expr_sub(stack, x):
    stack.append(stack.pop() - stack.pop())

@parser.pattern(Product("Expr", ["Expr", "*", "Expr"]))
def Expr_mul(stack, x):
    stack.append(stack.pop() * stack.pop())

@parser.pattern(Product("Expr", ["Expr", "/", "Expr"]))
def Expr_div(stack, x):
    stack.append(stack.pop() / stack.pop())

@parser.pattern(Product("Expr", ["Num"]))
def Expr_num(stack, x):
    pass

@parser.pattern(Product("Num", ["1"]))
@parser.pattern(Product("Num", ["3"]))
@parser.pattern(Product("Num", ["2"]))
def Num_1(stack, x):
    stack.append(int(x))

parser.compile()
parser.parse("1+2*3")