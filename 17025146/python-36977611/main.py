from collections import *


# Token定义
class Token():
    def __init__(self,_type,value = None):
        self._type = _type
        self.value = value
INT,ADD,SUB,MUL,DIV,END,LBR,RBR = "INT","ADD","SUB","MUL","DIV","END","LBR","RBR"
ASSIGN,SEMI,ENDL,COLON = "ASSIGN","SEMI","\n","COLON"
VARIABLE,LET,VARTYPE = "VARIABLE","LET","VARTYPE"
RESERVE = {
    "let":Token(LET,"LET"),
    "int":Token(VARTYPE,"int")
}

# 词法分析
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
    
    def get_token(self):
        while self.char:
            if self.char == "\n":
                self.advance()
                return Token(ENDL,"\n")
            elif self.char.isspace():
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
            elif self.char.isalpha():
                return self.get_var_id()
            elif self.char == ";":
                self.advance()
                return Token(SEMI,";")
            elif self.char == "=":
                self.advance()
                return Token(ASSIGN,"=")
            elif self.char == ":":
                self.advance()
                return Token(COLON,":")
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

    def statement(self):
        if self.token._type == LET:
            node = self.let()
        elif self.token._type == VARIABLE:
            node = self.change()
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
        if token._type in (ADD,SUB):
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
        return self.program()


# 语义分析
class Visitor():
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

    def visit_Number(self,node):
        pass

    def visit_Empty(self, node):
        pass


# 解释器
class Interpreter(Visitor):
    def __init__(self,tree):
        self.tree = tree
        self.var = {}
        self.types = {}

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

    def visit_UnaryOperate(self, node):
        op = node.op._type
        if op == ADD:
            return +self.visit(node.expr)
        elif op == SUB:
            return -self.visit(node.expr)

    def visit_Number(self,node):
        return node.value

    def visit_VarType(self,node):
        return node.vartype.value

    def visit_Assign(self,node):
        varname = node.left.name
        self.var[varname] = self.visit(node.right)
        self.types[varname] = self.visit(node.vartype)

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

    def visit_Empty(self,node):
        pass

    def interpret(self):
        return self.visit(self.tree)


# 主程序
# 程序
expr = """
let a:int = 12
let b:int = (a + 3) *8 / 5
"""
# 词法分析
lexer = Lexer(expr)
# 语法分析
parser = Parser(lexer)
tree = parser.tree()
# 语义分析
builder = SemanticAnalyzer()
builder.visit(tree)
# 解释器
interpreter = Interpreter(tree)
interpreter.interpret()
# 打印最终结果
print(interpreter.var)