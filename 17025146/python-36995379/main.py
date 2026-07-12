from collections import *
from enum import Enum
import sys


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

INT,ADD,SUB,MUL,DIV,MOD,LBR,RBR,POWER = "INT","ADD","SUB","MUL","DIV","MOD","LBR","RBR","POWER"
STR,BOOL,LIST = "STR","BOOL","LIST"
EQUAL,LESS,GREATER,LESSEQUAL,GREATEREQUAL,NOTEQUAL = "EQUAL","LESS","GREATER","LESSEQUAL","GREATEQUAL","NOTEQUAL"
ASSIGN,SEMI,ENDL,COLON,COMMA,ARROW,LMID,RMID = "ASSIGN","SEMI","ENDL","COLON","COMMA","ARROW","LMID","RMID"
LPARAN,RPARAN = "LPARAN","RPARAN"
LET,IF,ELSE,ELIF,AND,OR,NOT,WHILE,FUN,PRINTLN,RETURN = "LET","IF","ELSE","ELIF","AND","OR","NOT","WHILE","FUN","PRINTLN","RETURN"
FOR,INPUTLN,TOINT = "FOR","INPUTLN","TOINT"
VARIABLE,VARTYPE,END = "VARIABLE","VARTYPE","END"
RESERVE = {
    "let":Token(LET,"let"),
    "int":Token(VARTYPE,"int"),
    "float":Token(VARTYPE,"float"),
    "bool":Token(VARTYPE,"bool"),
    "str":Token(VARTYPE,"str"),
    "list":Token(VARTYPE, "list"),
    "if":Token(IF,"if"),
    "else":Token(ELSE,"else"),
    "elif":Token(ELIF,"elif"),
    "and":Token(AND,"and"),
    "or":Token(OR,"or"),
    "not":Token(NOT,"not"),
    "while":Token(WHILE,"while"),
    "fun":Token(FUN,"fun"),
    "true":Token(BOOL,"true"),
    "false":Token(BOOL,"false"),
    "println":Token(PRINTLN,"println"),
    "inputln":Token(INPUTLN,"inputln"),
    "toint":Token(TOINT,"toint"),
    "return":Token(RETURN,"return"),
    "for":Token(FOR,"for")
}
# TYPES = ["int","float","bool"]

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

    def get_string(self):
        res = ""
        while self.char is not None:
            if self.char == "\"":
                break
            res += self.char
            self.advance()
        self.advance()
        self.cross_space()
        if self.char == "[":
            self.advance()
            self.cross_space()
            index1 = self.get_int()
            indexlist = [index1]
            self.cross_space()
            while self.char == ":":
                self.advance()
                self.cross_space()
                index = self.get_int()
                indexlist.append(index)
                self.cross_space()
            if self.char == "]":
                leng = len(indexlist)
                if leng == 1:
                    res = res[indexlist[0]]
                elif leng == 2:
                    res = res[indexlist[0]:indexlist[1]]
                elif leng == 3:
                    res = res[indexlist[0]:indexlist[1]: indexlist[2]]
                self.advance()
        return self.token(STR,res)

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

    def cross_line_comment(self):
        while True:
            if self.char == "\n":
                break
            else:
                self.advance()

    def cross_block_comment(self):
        while True:
            if self.char == "*" and self.peek() == "/":
                self.advance()
                self.advance()
                break
            else:
                self.advance()

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
                if self.peek() == ">":
                    self.advance()
                    self.advance()
                    return self.token(ARROW,"->")
                else:
                    self.advance()
                    return self.token(SUB,"-")
            elif self.char == "*":
                self.advance()
                return self.token(MUL,"*")
            elif self.char == "/":
                if self.peek() == "/":
                    self.advance()
                    self.advance()
                    self.cross_line_comment()
                    continue
                elif self.peek() == "*":
                    self.advance()
                    self.advance()
                    self.cross_block_comment()
                    continue
                else:
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
                return self.token(LPARAN,"{")
            elif self.char == "}":
                self.advance()
                return self.token(RPARAN,"}")
            elif self.char == "<":
                if self.peek() == "=":
                    self.advance()
                    self.advance()
                    return self.token(LESSEQUAL,"<=")
                else:
                    self.advance()
                    return self.token(LESS,"<")
            elif self.char == ">":
                if self.peek() == "=":
                    self.advance()
                    self.advance()
                    return self.token(GREATEREQUAL,">=")
                else:
                    self.advance()
                    return self.token(GREATER,">")
            elif self.char == "!" and self.peek() == "=":
                self.advance()
                self.advance()
                return self.token(NOTEQUAL,"!=")
            elif self.char == "%":
                self.advance()
                return self.token(MOD,"!")
            elif self.char == "^":
                self.advance()
                return self.token(POWER,"^")
            elif self.char == "\"":
                self.advance()
                return self.get_string()
            elif self.char == ",":
                self.advance()
                return self.token(COMMA,",")
            elif self.char == "[":
                self.advance()
                return self.token(LMID,"[")
            elif self.char == "]":
                self.advance()
                return self.token(RMID,"]")
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

class String(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Bool(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class List(AST):
    def __init__(self,value):
        self.value = value

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

class Program(AST):
    def __init__(self,name,block):
        self.name = name
        self.block = block

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

class While(AST):
    def __init__(self,condition,then):
        self.condition = condition
        self.then = then

class Param(AST):
    def __init__(self,name,_type):
        self.name = name
        self._type = _type

class Function(AST):
    def __init__(self,name,params,block,returns):
        self.name = name
        self.params = params
        self.block = block
        self.returns = returns

class FunCall(AST):
    def __init__(self,name,params,token):
        self.name = name
        self.params = params
        self.token = token
        self.symbol = None

class Println(AST):
    def __init__(self,text):
        self.text = text

class Inputln(AST):
    def __init__(self,text):
        self.text = text

class Toint(AST):
    def __init__(self, text):
        self.text = text

class Return(AST):
    def __init__(self,value):
        self.value = value

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
        node = None
        eliflist = eliflist[::-1] # 反转列表
        for i in range(len(eliflist)):
            condition,root = eliflist[i]
            if i == 0:
                node = If(condition,root,elseroot)
            else:
                node = If(condition,root,node)
        node = If(con,ifroot,node)
        return node

    def while_statement(self):
        self.judg(WHILE)
        con = self.calc()
        self.judg(LPARAN)
        statements = self.statement_list()
        self.judg(RPARAN)
        then = Compound()
        then.children = statements
        node = While(con,then)
        return node

    def get_param(self):
        if self.token._type != VARIABLE:
            return []
        params = []
        name1 = self.variable()
        self.judg(COLON)
        tp = self.vartype()
        params.append(Param(name1,tp))
        while self.token._type == COMMA:
            self.judg(COMMA)
            name = self.variable()
            self.judg(COLON)
            tp = self.vartype()
            params.append(Param(name,tp))
        return params

    def definefunction(self):
        self.judg(FUN)
        funname = self.token.value
        self.judg(VARIABLE)
        self.judg(LBR)
        params = self.get_param()
        self.judg(RBR)
        rettype = None
        if self.token._type == ARROW:
            self.judg(ARROW)
            rettype = self.vartype()
        self.judg(LPARAN)
        block = self.statement_list()
        self.judg(RPARAN)
        com = Compound()
        com.children = block
        node = Function(funname,params,com,rettype)
        return node

    def funcall(self):
        token = self.token
        funname = self.token.value
        self.judg(VARIABLE)
        self.judg(LBR)
        params = []
        if self.token._type != RBR:
            node = self.calc()
            params.append(node)
        while self.token._type == COMMA:
            self.judg(COMMA)
            node = self.calc()
            params.append(node)
        self.judg(RBR)
        node = FunCall(funname,params,token)
        return node

    def println(self):
        self.judg(PRINTLN)
        self.judg(LBR)
        text = self.calc()
        self.judg(RBR)
        node = Println(text)
        return node

    def inputln(self):
        self.judg(INPUTLN)
        self.judg(LBR)
        text = self.calc()
        self.judg(RBR)
        node = Inputln(text)
        return node

    def toint(self):
        self.judg(TOINT)
        self.judg(LBR)
        text = self.calc()
        self.judg(RBR)
        node = Toint(text)
        return node

    def return_statement(self):
        self.judg(RETURN)
        value = self.calc()
        node = Return(value)
        return node

    def get_list(self):
        self.judg(LMID)
        res = []
        value1 = self.calc()
        res.append(value1)
        while self.token._type == COMMA:
            self.judg(COMMA)
            res.append(self.calc())
        self.judg(RMID)
        node = List(res)
        return node

    def statement(self):
        if self.token._type == LET:
            node = self.let()
        elif self.token._type == WHILE:
            node = self.while_statement()
        elif self.token._type == VARIABLE:
            if self.lexer.char == "(":
                node = self.funcall()
            else:
                node = self.change()
        elif self.token._type == IF:
            node = self.if_node()
        elif self.token._type == FUN:
            node = self.definefunction()
        elif self.token._type == PRINTLN:
            return self.println()
        elif self.token._type == RETURN:
            return self.return_statement()
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
        node = Program("main",root)
        return node

    def factor(self):
        token = self.token
        if token._type in (ADD,SUB,NOT):
            self.judg(token._type)
            node = UnaryOperate(token,self.factor())
            return node
        elif token._type == INT:
            self.judg(INT)
            return Number(token)
        elif token._type == BOOL:
            self.judg(BOOL)
            return Bool(token)
        elif token._type == LBR:
            self.judg(LBR)
            res = self.calc()
            self.judg(RBR)
            return res
        elif token._type == STR:
            self.judg(STR)
            return String(token)
        elif token._type == VARIABLE and self.lexer.char == "(":
            node = self.funcall()
            return node
        elif token._type == LMID:
            node = self.get_list()
            return node
        elif token._type == INPUTLN:
            node = self.inputln()
            return node
        elif token._type == TOINT:
            node = self.toint()
            return node
        else:
            node = self.variable()
            return node

    def xterm(self):
        node = self.factor()
        while True:
            if self.token._type in (POWER):
                operate = self.token
                if operate._type == POWER:
                    self.judg(POWER)
                node = BinOperate(node,operate,self.factor())
            else:
                break
        return node

    def term(self):
        node = self.xterm()
        while True:
            if self.token._type in (MUL,DIV,MOD):
                operate = self.token
                if operate._type == MUL:
                    self.judg(MUL)
                if operate._type == DIV:
                    self.judg(DIV)
                if operate._type == MOD:
                    self.judg(MOD)
                node = BinOperate(node,operate,self.xterm())
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
        self.level = 0

class BuiltinSymbol(Symbol):
    def __init__(self,name):
        super().__init__(name)

class VarSymbol(Symbol):
    def __init__(self,name,stype):
        super().__init__(name,stype)

class FunSymbol(Symbol):
    def __init__(self,name,params = None):
        super().__init__(name)
        if params is None:
            self.params = []
        else:
            self.params = params
        self.blockast = None

class ScopeSymbolTable():
    def __init__(self,scopename = None,scopelv = None,enclosing = None):
        self.symbol = OrderedDict()
        self.name = scopename
        self.level = scopelv
        self.enclosing = enclosing

    def init(self):
        self.define(BuiltinSymbol("int"))
        self.define(BuiltinSymbol("float"))
        self.define(BuiltinSymbol("bool"))
        self.define(BuiltinSymbol("str"))

    def define(self,symbol):
        symbol.level = self.level
        self.symbol[symbol.name] = symbol

    def query(self,name):
        symbol = self.symbol.get(name)
        if symbol is not None:
            return symbol
        if self.enclosing is not None:
            return self.enclosing.query(name)

class SemanticAnalyzer(Visitor):
    def __init__(self):
        self.table = None

    def error(self,msg):
        raise SemanticError(msg)

    def visit_Program(self,node):
        global_table = ScopeSymbolTable("main",1,self.table)
        global_table.init()
        self.table = global_table
        self.visit(node.block)

    def visit_Compound(self,node):
        for child in node.children:
            self.visit(child)

    def visit_Assign(self,node):
        varname = node.left.name
        tpname = node.vartype.name
        symbol = self.table.query(tpname)
        varsymbol = VarSymbol(varname,symbol)
        self.table.define(varsymbol)
        self.visit(node.left)
        self.visit(node.right)

    def visit_Change(self, node):
        name = node.left.name
        symbol = self.table.query(name)
        if symbol:
            self.visit(node.right)
        else:
            self.error(f"name {name} is not defined")

    def visit_Var(self,node):
        name = node.name
        symbol = self.table.query(name)
        if not symbol:
            self.error(f"name {name} is not defined")

    def visit_UnaryOprate(self, node):
        self.visit(node.expr)

    def visit_BinOperate(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit_If(self,node):
        self.visit(node.condition)
        self.visit(node.then)
        self.visit(node.elsenode)

    def visit_While(self,node):
        self.visit(node.condition)
        self.visit(node.then)

    def visit_Function(self,node):
        funsymbol = FunSymbol(node.name)
        self.table.define(funsymbol)
        funtable = ScopeSymbolTable(node.name,self.table.level + 1,self.table)
        self.table = funtable
        for param in node.params:
            ptype = self.table.query(param._type.name)
            pname = param.name.name
            symbol = VarSymbol(pname,ptype)
            self.table.define(symbol)
            funsymbol.params.append(symbol)
        self.visit(node.block)
        self.table = self.table.enclosing
        funsymbol.blockast = node.block

    def visit_FunCall(self,node):
        funname = node.name
        table = self.table.query(funname)
        greeting = table.params
        arg = node.params
        if len(greeting) == len(arg):
            for param in node.params:
                self.visit(param)
        else:
            self.error(f"function {funname} accept {len(greeting)} parameters but {len(arg)} were given")
        symbol = self.table.query(funname)
        node.symbol = symbol

    def visit_Return(self,node):
        self.visit(node.value)

    def visit_Println(self,node):
        self.visit(node.text)

    def visit_Inputln(self,node):
        self.visit(node.text)

    def visit_Toint(self,node):
        self.visit(node.text)

    def visit_List(self,node):
        for i in node.value:
            self.visit(i)

    def visit_String(self,node):
        pass

    def visit_Bool(self,node):
        pass

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
        if tp == POWER:
            return left ** right
        if tp == MOD:
            return left % right
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

    def visit_String(self,node):
        return node.value

    def visit_Bool(self,node):
        value = node.value
        if value == "true":
            return True
        else:
            return False

    def visit_VarType(self,node):
        return node.vartype.value

    def visit_Assign(self,node):
        varname = node.left.name
        vartype = self.visit(node.vartype)
        varvalue = self.visit(node.right)
        tp = f"<class '{vartype}'>"
        vtp = str(type(varvalue)).lower().replace("__main__.","")
        if vtp == tp:
            ar = self.stack.peek()
            ar[varname] = varvalue
        else:
            raise ValueError("变量的类型发生了改变")

    def visit_Change(self,node):
        varname = node.left.name
        value = self.visit(node.right)
        ar = self.stack.peek()
        ar[varname] = value

    def visit_Var(self,node):
        varname = node.name
        ar = self.stack.peek()
        value = ar.get(varname)
        if value is None:
            raise NameError("不存在的变量值")
        else:
            return value

    def visit_Program(self,node):
        program_name = node.name
        ar = ActivationRecord(program_name,"main",1)
        self.stack.push(ar)
        self.visit(node.block)
        self.stack.pop()

    def visit_Compound(self,node):
        for child in node.children:
            if type(child).__name__ == "Return":
                ret = self.visit(child)
                return ret
            self.visit(child)
        return None

    def visit_If(self,node):
        if self.visit(node.condition):
            self.visit(node.then)
        else:
            self.visit(node.elsenode)

    def visit_While(self,node):
        con = self.visit(node.condition)
        while con:
            self.visit(node.then)
            con = self.visit(node.condition)

    def visit_Function(self,node):
        pass

    def visit_FunCall(self,node):
        funname = node.name
        ar = ActivationRecord(funname,"function",node.symbol.level + 1)
        symbol = node.symbol
        formal = symbol.params
        actual = node.params
        for param_symbol,argument in zip(formal,actual):
            ar[param_symbol.name] = self.visit(argument)
        self.stack.push(ar)
        is_return = self.visit(symbol.blockast)
        self.stack.pop()
        if is_return is not None:
            return is_return
        return 0

    def visit_Return(self,node):
        ar = self.stack.peek()
        if ar.level <= 1:
            self.error("can not return from main")
        else:
            return self.visit(node.value)

    def visit_Println(self,node):
        sys.stdout.write(str(self.visit(node.text)) + "\n")

    def visit_Inputln(self,node):
        return input(self.visit(node.text))

    def visit_Toint(self,node):
        return int(self.visit(node.text))

    def visit_List(self,node):
        res = []
        for i in node.value:
            res.append(self.visit(i))
        return res

    def visit_Empty(self,node):
        pass

    def interpret(self):
        return self.visit(self.tree)
        
# 介绍
text = """
0.8版本发布！自制解释器已经全面支持函数！代码行数破千！
它已经可以完成绝大多数的算法题，比如，我们在洛谷上面随便找一道，就这道吧，“阶乘之和”，题号P1009，用这个解释器写一段代码来解决。
然后，运行于我的自制解释器上的代码成功通过了这道题，提交记录：https://www.luogu.com.cn/record/86093095
代码可以进改编或者上面的洛谷题目提交记录里面查看，个人感觉写出来还是非常清爽优雅的。
大家也可以在评论区发洛谷的题，试试能不能用我的这个自制解释器写出来。
"""
print(text)
print()
print("--------------------------------------------")
input("回车运行示例(阶乘之和):")


# 主程序
# 程序
expr = """
fun factorial(num:int){
    let i:int = 1
    let result:int = 1
    while i <= num{
        result = result * i
        i = i + 1
    }
    return result
}
fun factoradd(number:int){
    let x:int = 1
    let results:int = 0
    while x <= number{
        results = results + factorial(x)
        x = x + 1
    }
    return results
}
let num:int = toint(inputln("输入数字"))
println("结果是:")
println(factoradd(num))
"""
# 词法分析
lexer = Lexer(expr)
# 语法分析
parser = Parser(lexer)
tree = parser.program()
# 语义分析
builder = SemanticAnalyzer()
builder.visit(tree)
# 解释器
interpreter = Interpreter(tree)
interpreter.interpret()