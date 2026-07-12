from collections import *
from enum import Enum


# Token定义
class Token():
    def __init__(self,_type,value = None,line = None,column=None):
        self._type = _type
        self.value = value
        self.line = line
        self.column = column

    def __str__(self):
        msg = f"Token({self._type}, {self.value}, position={self.line}:{self.column})"
        return msg

    __repr__ = __str__

INT,ADD,SUB,MUL,DIV,LBR,RBR = "INT","ADD","SUB","MUL","DIV","LBR","RBR"
EQUAL,LESS,GREATER,LESSEQUAL,GREATEREQUAL,NOTEQUAL = "EQUAL","LESS","GREATER","LESSEQUAL","GREATEQUAL","NOTEQUAL"
ASSIGN,SEMI,ENDL,COLON = "ASSIGN","SEMI","\n","COLON"
LPARAN,RPARAN = "LPARAN","RPARAN"
LET,IF,ELSE,ELIF,AND,OR,NOT = "LET","IF","ELSE","ELIF","AND","OR","NOT"
VARIABLE,VARTYPE,END = "VARIABLE","VARTYPE","END"
RESERVE = {
    "let":Token(LET,"let"),
    "int":Token(VARTYPE,"int"),
    "float":Token(VARTYPE,"float"),
    "if":Token(IF,"if"),
    "else":Token(ELSE,"else"),
    "elif":Token(ELIF,"elif"),
    "and":Token(AND,"and"),
    "or":Token(OR,"or"),
    "not":Token(NOT,"not")
}

# 错误定义
class Error(Exception):
    def __init__(self,message=None):
        self.message = f'{self.__class__.__name__}: {message}'

class LexerError(Error):
    pass

class ParserError(Error):
    pass

class SemanticError(Error):
    pass


# 词法分析
class Lexer():
    def __init__(self,expr):
        self.expr = expr
        self.position = 0
        self.char = self.expr[self.position]
        self.line = 1
        self.column = 1

    def error(self):
        msg = f"Lexer error on '{self.char}' line: {self.line} column: {self.column}"
        raise LexerError(msg)

    def advance(self):
        if self.char == "\n":
            self.line += 1
            self.column = 0
        self.position += 1
        if self.position >= len(self.expr):
            self.char = None
        else:
            self.char = self.expr[self.position]
            self.column += 1

    def cross_space(self):
        while True:
            if self.char != None and self.char.isspace():
                self.advance()
            else:
                break

    def get_int(self):
        res = ""
        while True:
            if self.char != None and (self.char.isdigit() or self.char == "."):
                res += self.char
                self.advance()
            else:
                break
        if "." in res:
            return float(res)
        else:
            return int(res)

    def get_var_id(self):
        res = ""
        while True:
            if self.char:
                if self.char.isalnum():
                    res += self.char
                    self.advance()
                else:
                    break
            else:
                break
        token = RESERVE.get(res,Token("VARIABLE",res))
        return token

    def token(self,_type,value = None):
        return Token(_type,value,self.line,self.column)

    def peek(self):
        return self.expr[self.position + 1]
    
    def get_token(self):
        while self.char:
            if self.char == "\n":
                self.advance()
                return self.token(ENDL,"\n")
            elif self.char.isspace():
                self.cross_space()
                continue
            elif self.char.isdigit():
                longint = self.get_int()
                return self.token(INT,longint)
            elif self.char == "+":
                self.advance()
                return self.token(ADD,"+")
            elif self.char == "-":
                self.advance()
                return self.token(SUB,"-")
            elif self.char == "*":
                self.advance()
                return self.token(MUL,"*")
            elif self.char == "/":
                self.advance()
                return self.token(DIV,"/")
            elif self.char == "(":
                self.advance()
                return self.token(LBR,"(")
            elif self.char == ")":
                self.advance()
                return self.token(RBR,")")
            elif self.char.isalpha():
                return self.get_var_id()
            elif self.char == ";":
                self.advance()
                return self.token(SEMI,";")
            elif self.char == "=":
                if self.peek() == "=":
                    self.advance()
                    self.advance()
                    return self.token(EQUAL,"==")
                else:
                    self.advance()
                    return self.token(ASSIGN,"=")
            elif self.char == ":":
                self.advance()
                return self.token(COLON,":")
            elif self.char == "{":
                self.advance()
                return self.token(LPARAN)
            elif self.char == "}":
                self.advance()
                return self.token(RPARAN)
            elif self.char == "<":
                if self.peek() == "=":
                    self.advance()
                    self.advance()
                    return self.token(LESSEQUAL)
                else:
                    self.advance()
                    return self.token(LESS)
            elif self.char == ">":
                if self.peek() == "=":
                    self.advance()
                    self.advance()
                    return self.token(GREATER)
                else:
                    self.advance()
                    return self.token(GREATEREQUAL)
            elif self.char == "!" and self.peek() == "=":
                self.advance()
                self.advance()
                return self.token(NOTEQUAL)
            else:
                self.error()
        return self.token(END)


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

class UnaryOperate(AST):
    def __init__(self,operate,expr):
        self.op = operate
        self.expr = expr

class Assign(AST):
    def __init__(self,left,operate,right,vartype):
        self.left = left
        self.operate = self.token = operate
        self.right = right
        self.vartype = vartype

class Var(AST):
    def __init__(self,token):
        self.token = token
        self.name = token.value

class Empty(AST):
    pass

class Compound(AST):
    def __init__(self):
        self.children = []

class VarType(AST):
    def __init__(self,vartype):
        self.vartype = vartype
        self.name = vartype.value

class Change(AST):
    def __init__(self,left,operate,right):
        self.left = left
        self.operate = operate
        self.right = right

class If(AST):
    def __init__(self,condition,then,elsenode = None):
        self.condition = condition
        self.then = then
        if elsenode:
            self.elsenode = elsenode
        else:
            self.elsenode = Empty()

class Parser():
    def __init__(self,lexer):
        self.lexer = lexer
        self.token = self.lexer.get_token()

    def error(self,error_code,token):
        raise ParserError(f"{error_code} -> {token}")

    def judg(self,_type):
        if self.token._type == _type:
            self.token = self.lexer.get_token()
        else:
            self.error(
                "Unexpected token",
                self.token
            )

    def variable(self):
        node = Var(self.token)
        self.judg(VARIABLE)
        return node

    def let(self):
        self.judg(LET)
        return self.assignment()

    def empty(self):
        return Empty()

    def vartype(self):
        node = VarType(self.token)
        self.judg(VARTYPE)
        return node

    def assignment(self):
        left = self.variable()
        colon = self.token
        self.judg(COLON)
        vartype = self.vartype()
        token = self.token
        self.judg(ASSIGN)
        right = self.calc()
        node = Assign(left,token,right,vartype)
        return node

    def change(self):
        left = self.variable()
        token = self.token
        self.judg(ASSIGN)
        right = self.calc()
        node = Change(left,token,right)
        return node

    def cross_endl(self):
        while True:
            if self.token._type == ENDL:
                self.token = self.lexer.get_token()
                continue
            else:
                break

    def get_branch(self,name):
        self.judg(name)
        con = self.calc()
        self.cross_endl()
        self.judg(LPARAN)
        node = self.statement_list()
        root = Compound()
        root.children = node
        self.judg(RPARAN)
        self.cross_endl()
        return con,root

    def if_node(self):
        con,ifroot = self.get_branch(IF)
        eliflist = []
        while True:
            if self.token._type == ELIF:
                elifcon,elifroot = self.get_branch(ELIF)
                eliflist.append((elifcon,elifroot))
            elif self.token._type == ELSE:
                self.judg(ELSE)
                self.judg(LPARAN)
                node = self.statement_list()
                elseroot = Compound()
                elseroot.children = node
                self.judg(RPARAN)
            else:
                break
        eliflist = eliflist[::-1] # 反转列表
        for i in range(len(eliflist)):
            condition,root = eliflist[i]
            if i == 0:
                node = If(condition,root,elseroot)
            else:
                node = If(condition,root,node)
        node = If(con,ifroot,node)
        return node

    def statement(self):
        if self.token._type == LET:
            node = self.let()
        elif self.token._type == VARIABLE:
            node = self.change()
        elif self.token._type == IF:
            node = self.if_node()
        else:
            node = self.empty()
        return node

    def statement_list(self):
        node = self.statement()
        nodelist = [node]
        while self.token._type == SEMI or self.token._type == ENDL:
            if self.token._type == SEMI:
                self.judg(SEMI)
            elif self.token._type == ENDL:
                self.judg(ENDL)
            nodelist.append(self.statement())
        return nodelist

    def program(self):
        nodelist = self.statement_list()
        root = Compound()
        root.children = nodelist
        return root

    def factor(self):
        token = self.token
        if token._type in (ADD,SUB,NOT):
            self.judg(token._type)
            node = UnaryOperate(token,self.factor())
            return node
        if token._type == INT:
            self.judg(INT)
            return Number(token)
        if token._type == LBR:
            self.judg(LBR)
            res = self.calc()
            self.judg(RBR)
            return res
        else:
            node = self.variable()
            return node

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
            if self.token._type in (ADD,SUB,EQUAL,AND,OR,LESS,GREATER,GREATEREQUAL,LESSEQUAL,NOTEQUAL):
                operate = self.token
                if operate._type == ADD:
                    self.judg(ADD)
                if operate._type == SUB:
                    self.judg(SUB)
                if operate._type == EQUAL:
                    self.judg(EQUAL)
                if operate._type == AND:
                    self.judg(AND)
                if operate._type == OR:
                    self.judg(OR)
                if operate._type == LESS:
                    self.judg(LESS)
                if operate._type == GREATER:
                    self.judg(GREATER)
                if operate._type == LESSEQUAL:
                    self.judg(LESSEQUAL)
                if operate._type == GREATEREQUAL:
                    self.judg(GREATEREQUAL)
                if operate._type == NOTEQUAL:
                    self.judg(NOTEQUAL)
                node = BinOperate(node,operate,self.term())
            else:
                break
        return node

    def tree(self):
        return self.program()


# 语义分析
class Visitor(): # 设计模式-访问者模式
    def visit(self,node):
        method = type(node).__name__
        visitor = getattr(self,"visit_" + method)
        return visitor(node)

class Symbol():
    def __init__(self,name,stype = None):
        self.name = name
        self.stype = stype

class BuiltinSymbol(Symbol):
    def __init__(self,name):
        super().__init__(name)

class VarSymbol(Symbol):
    def __init__(self,name,stype):
        super().__init__(name,stype)

class SymbolTable():
    def __init__(self):
        self.symbol = OrderedDict()
        self.init()

    def init(self):
        self.define(BuiltinSymbol("int"))
        self.define(BuiltinSymbol("float"))

    def define(self,symbol):
        self.symbol[symbol.name] = symbol

    def query(self,name):
        return self.symbol.get(name)

class SemanticAnalyzer(Visitor):
    def __init__(self):
        self.table = SymbolTable()

    def visit_Compound(self,node):
        for child in node.children:
            self.visit(child)

    def visit_Assign(self,node):
        varname = node.left.name
        tpname = node.vartype.name
        symbol = self.table.query(tpname)
        varsymbol = VarSymbol(varname,symbol)
        self.table.define(varsymbol)

    def visit_Change(self, node):
        name = node.left.name
        symbol = self.table.query(name)
        if symbol:
            self.visit(node.right)
        else:
            raise NameError("未定义的变量值")

    def visit_Var(self,node):
        name = node.name
        symbol = self.table.query(name)
        if not symbol:
            raise NameError("未定义的变量值")

    def visit_UnaryOprate(self, node):
        self.visit(node.expr)

    def visit_BinOperate(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit_If(self,node):
        self.visit(node.condition)
        self.visit(node.then)
        self.visit(node.elsenode)

    def visit_Number(self,node):
        pass

    def visit_Empty(self, node):
        pass


# 解释器
class CallStack:
    def __init__(self):
        self.stack = []

    def push(self, ar):
        self.stack.append(ar)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

class ActivationRecord:
    def __init__(self, name, type, level):
        self.name = name
        self.type = type
        self.level = level
        self.members = {}

    def __setitem__(self, key, value):
        self.members[key] = value

    def __getitem__(self, key):
        return self.members[key]

    def get(self, key):
        return self.members.get(key)

class Interpreter(Visitor):
    def __init__(self,tree):
        self.tree = tree
        self.var = {}
        self.types = {}
        self.stack = CallStack()

    def visit_BinOperate(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        tp = node.op._type
        if tp == ADD:
            return left + right
        if tp == SUB:
            return left - right
        if tp == MUL:
            return left * right
        if tp == DIV:
            res = left / right
            if res % 1 == 0:
                return int(res)
            else:
                return res
        if tp == EQUAL:
            return bool(left == right)
        if tp == LESS:
            return bool(left < right)
        if tp == GREATER:
            return bool(left > right)
        if tp == LESSEQUAL:
            return bool(left <= right)
        if tp == GREATEREQUAL:
            return bool(left >= right)
        if tp == NOTEQUAL:
            return bool(left != right)
        if tp == AND:
            return bool(left and right)
        if tp == OR:
            return bool(left or right)

    def visit_UnaryOperate(self, node):
        op = node.op._type
        if op == ADD:
            return +self.visit(node.expr)
        elif op == SUB:
            return -self.visit(node.expr)
        elif op == NOT:
            return not self.visit(node.expr)

    def visit_Number(self,node):
        return node.value

    def visit_VarType(self,node):
        return node.vartype.value

    def visit_Assign(self,node):
        varname = node.left.name
        vartype = self.visit(node.vartype)
        varvalue = self.visit(node.right)
        tp = f"<class '{vartype}'>"
        if str(type(varvalue)) == tp:
            self.var[varname] = varvalue
            self.types[varname] = vartype
        else:
            raise ValueError("变量的类型发生了改变")

    def visit_Change(self,node):
        varname = node.left.name
        value = self.visit(node.right)
        vartype = self.types[varname]
        tp = f"<class '{vartype}'>"
        if str(type(value)) == tp:
            self.var[varname] = value
        else:
            raise ValueError("变量的类型发生了改变")

    def visit_Var(self,node):
        varname = node.name
        value = self.var.get(varname)
        if value:
            return value
        else:
            raise NameError("不存在的变量值")

    def visit_Compound(self,node):
        for child in node.children:
            self.visit(child)

    def visit_If(self,node):
        if self.visit(node.condition):
            self.visit(node.then)
        else:
            self.visit(node.elsenode)

    def visit_Empty(self,node):
        pass

    def interpret(self):
        return self.visit(self.tree)


# 主程序
# 程序
expr = """
let num1:float = 1.5
let num2:int = 2
if num1 == num2{
    let result:int = 1
}
elif num1 <= num2{
    let result:int = 2
}
else{
    let result:int = 3
}
"""
# 词法分析
lexer = Lexer(expr)
# 语法分析
parser = Parser(lexer)
tree = parser.tree()
# 语义分析
builder = SemanticAnalyzer()
builder.visit(tree)
# print(builder.table.symbol["a"].stype.name)
# 解释器
interpreter = Interpreter(tree)
interpreter.interpret()
# 打印最终结果
print(interpreter.var)