from enum import Enum
from collections import OrderedDict
import sys
import time


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


# 符号Token
class SymbolToken(Enum):
    # 数学运算
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    MOD = "%"
    POWER = "^"
    # 布尔运算
    EQUAL = "=="
    LESS = "<"
    GREATER = ">"
    LESSEQUAL = "<="
    GREATEREQUAL = ">="
    NOTEQUAL = "!="
    # 语法符号
    ASSIGN = "="
    SEMI = ";"
    ENDL = "\n"
    COLON = ":"
    COMMA = ","
    DOT = "."
    ARROW = "->"
    LBR = "("
    RBR = ")"
    LMID = "["
    RMID = "]"
    LPARAN = "{"
    RPARAN = "}"


# 类型Token
class TokenType(Enum):
    # 内置类型
    INT = "INT" # 整数类型
    FLOAT = "FLOAT" # 浮点数类型
    STR = "STR" # 字符串类型
    BOOL = "BOOL" # 布尔类型
    LIST = "LIST" # 列表类型
    NULL = "NULL" # 空类型
    FUNCTION = "FUNCITON" # 函数类型
    AUTO = "AUTO" # 自动推导
    # 关键字
    # 变量
    LET = "LET" # 声明变量
    # 常量
    CONST = "CONST" # 声明常量
    # 分支
    IF = "IF" # 条件判断-if
    ELIF = "ELIF" # 条件判断-elif
    ELSE = "ELSE" # 条件判断-else
    SWITCH = "SWITCH" # 变量判断-switch
    CASE = "CASE" # 变量判断-case
    # 循环
    WHILE = "WHILE" # 条件循环
    FOR = "FOR" # 遍历对象
    IN ="IN" # for语句组成部分
    BREAK = "BREAK" # 结构控制-break
    CONTINUE = "CONTINUE" # 结构控制-continue
    # 函数
    FUN = "FUN" # 函数定义
    RETURN = "RETURN" # 函数返回
    # 导入模块
    IMPORT = "IMPORT"
    AS = "AS"
    # 布尔运算
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    # 内置函数
    PRINTLN = "PRINTLN"
    INPUTLN = "INPUTLN"
    TOINT = "TOINT"
    RANGE = "RANGE"
    LENGTH = "LENGTH"
    ORD = "ORD"
    CHR = "CHR"
    PRINT = "PRINT"
    # 其它
    VARIABLE = "VARIABLE" # 变量
    VARTYPE = "VARTYPE" # 变量类型
    END = "END" # 代码结束


# 保留字
class ReserveWord(Enum):
    # 关键字
    letR = Token(TokenType.LET,"let") # 变量定义
    constR = Token(TokenType.CONST, "const") # 常量定义
    ifR = Token(TokenType.IF,"if") # 条件判断-如果
    elifR = Token(TokenType.ELIF,"elif") # 条件判断-否则如果
    elseR = Token(TokenType.ELSE,"else") # 条件判断-否则
    switchR = Token(TokenType.SWITCH,"switch") # 变量判断-switch
    caseR = Token(TokenType.CASE,"case") # 变量判断-case
    whileR = Token(TokenType.WHILE,"while") # 条件循环
    forR = Token(TokenType.FOR,"for") # 遍历数组
    inR = Token(TokenType.IN,"in") # for语句必需结构
    importR = Token(TokenType.IMPORT,"import") # 导入模块语句
    asR = Token(TokenType.AS,"as") # 导入别名语句
    # 结构体
    funR = Token(TokenType.FUN,"fun") # 函数定义
    # 结构控制
    returnR = Token(TokenType.RETURN,"return") # 函数返回
    breakR = Token(TokenType.BREAK,"break") # 退出循环
    continueR = Token(TokenType.CONTINUE,"continue") # 跳过此次循环
    # 表达式运算
    andR = Token(TokenType.AND,"and") # 与运算
    orR = Token(TokenType.OR,"or") # 或运算
    notR = Token(TokenType.NOT,"not") # 非运算
    # 内置类型
    intR = Token(TokenType.VARTYPE,"int") # 整数类型
    realR = Token(TokenType.VARTYPE,"real") # 浮点数类型
    strR = Token(TokenType.VARTYPE,"str") # 字符串类型
    boolR = Token(TokenType.VARTYPE,"bool") # 布尔类型
    arrayR = Token(TokenType.VARTYPE,"array") # 数组类型
    nulltypeR = Token(TokenType.VARTYPE,"nulltype") # 空类型
    functionR = Token(TokenType.VARTYPE,"function")
    autoR = Token(TokenType.VARTYPE, "auto") # 自动推导
    # 内置常量
    trueR = Token(TokenType.BOOL,"true") # bool-真值
    talseR = Token(TokenType.BOOL,"false") # bool-假值
    nullR = Token(TokenType.NULL,"null") # NoneType-空值
    # 内置函数
    printlnR = Token(TokenType.PRINTLN,"println") # 打印一行字符
    printR = Token(TokenType.PRINT,"print") # 打印一段字符
    inputlnR = Token(TokenType.INPUTLN,"inputln") # 输入一行字符
    tointR = Token(TokenType.TOINT,"toint") # 转换为int类型
    rangeR = Token(TokenType.RANGE,"range") # 生成列表
    lengthR = Token(TokenType.LENGTH,"length") # 获取长度
    ordR = Token(TokenType.ORD,"ord") # 字符转换为ASCII
    chrR = Token(TokenType.CHR,"chr") # ASCII转换为字符


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

class InterpreterError(Error):
    pass


# 生成保留字字典
def build_reserve(reserveclass):
    res = {}
    reserve = list(reserveclass)
    for word in reserve:
        res[word.name[:-1]] = word.value
    return res

RESERVE  = build_reserve(ReserveWord)


class Lexer():
    def __init__(self,expr):
        self.expr = expr
        self.position = 0
        self.char = self.expr[self.position]
        self.line = 1
        self.column = 1

    # 报错函数
    def error(self):
        msg = f"Lexer error on '{self.char}' line: {self.line} column: {self.column}"
        raise LexerError(msg)

    # 更新当前位置
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

    # 跳过所有空格(不包括回车)
    def cross_space(self):
        while True:
            if self.char != None and self.char.isspace() and self.char != "\n":
                self.advance()
            else:
                break
    
    # 获取数字
    def get_int(self):
        res = ""
        while True:
            if self.char != None and (self.char.isdigit() or self.char == "."):
                res += self.char
                self.advance()
            else:
                break
        if "." in res:
            return self.token(TokenType.FLOAT,float(res))
        else:
            return self.token(TokenType.INT,int(res))

    # 获取字符串
    def get_string(self,quot = "\""):
        res = ""
        while self.char is not None:
            if self.char == quot:
                break
            res += self.char
            self.advance()
        self.advance()
        return self.token(TokenType.STR,res)

    # 获取变量或保留字
    def get_var_id(self):
        res = ""
        while True:
            if self.char:
                if self.char.isalnum() or self.char == "_":
                    res += self.char
                    self.advance()
                else:
                    break
            else:
                break
        token = RESERVE.get(res,Token(TokenType.VARIABLE,res))
        return token

    # 跳过行注释
    def cross_line_comment(self):
        while True:
            if self.char == "\n":
                break
            else:
                self.advance()

    # 跳过块注释
    def cross_block_comment(self):
        while True:
            if self.char == "*" and self.peek() == "/":
                self.advance()
                self.advance()
                break
            else:
                self.advance()

    # 获取Token
    def token(self,_type,value = None):
        return Token(_type,value,self.line,self.column)

    # 获取下一个字符
    def peek(self):
        return self.expr[self.position + 1]
    
    # 获取一个Token
    def get_token(self):
        while self.char:
            # 跳过空格
            if self.char.isspace() and self.char != "\n":
                self.cross_space()
                continue
            # 获取数字
            elif self.char.isdigit():
                return self.get_int()
            # 块注释
            elif self.char == "/" and self.peek() == "*":
                self.advance()
                self.advance()
                self.cross_block_comment()
                continue
            # 行注释
            elif self.char == "/" and self.peek() == "/":
                self.advance()
                self.advance()
                self.cross_line_comment()
                continue
            # 字符串-双引号
            elif self.char == "\"":
                self.advance()
                return self.get_string()
            # 字符串-单引号
            elif self.char == "'":
                self.advance()
                return self.get_string("'")
            # 变量或保留字
            elif self.char.isalnum() or self.char == "_":
                return self.get_var_id()
            # 拿到符号
            try:
                token_type = SymbolToken(self.char + self.peek())
                self.advance()
                self.advance()
                return self.token(token_type,token_type.value)
            except:
                try:
                    token_type = SymbolToken(self.char)
                    self.advance()
                    return self.token(token_type,token_type.value)
                except ValueError:
                    self.error()
        # 标注代码结束
        return self.token(TokenType.END)


# 所有节点类的父类:AST树
class AST():
    pass

# 常量
# 整数常量
class IntConst(AST):
    def __init__(self,token):
        self.token = token
        self.value = token.value
# 浮点数常量
class FloatConst(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
# 字符串常量
class StringConst(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
# 布尔值常量
class BoolConst(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
# 空值常量
class NullConst(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
# 列表常量
class ListConst(AST):
    def __init__(self,value):
        self.value = value

# 项
# 变量项
class VarTerm(AST):
    def __init__(self,token):
        self.token = token
        self.name = token.value
# 类型项
class VartypeTerm(AST):
    def __init__(self,vartype):
        self.vartype = vartype
        self.name = vartype.value
# 参数项
class ParamTerm(AST):
    def __init__(self,name,_type,default = None):
        self.name = name
        self._type = _type
        self.default = default
# 方法项
class MethodTerm(AST):
    def __init__(self,name,params,token):
        self.name = name
        self.params = params
        self.token = token

# 运算符
# 二元运算符
class BinOperate(AST):
    def __init__(self,left,operate,right):
        self.left = left
        self.right = right
        self.op = self.token = operate
# 一元运算符
class UnaryOperate(AST):
    def __init__(self,operate,expr):
        self.op = operate
        self.expr = expr
# 点运算符
class DotOperate(AST):
    def __init__(self,left,right):
        self.left = left
        self.right = right
# 索引运算符
class IndexOperate(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right
# 函数调用运算符
class FuncallOperate(AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

# 语句
# 空语句
class EmptyStatement(AST):
    pass
# 变量声明语句
class AssignStatement(AST):
    def __init__(self,left,operate,right,vartype):
        self.left = left
        self.operate = self.token = operate
        self.right = right
        self.vartype = vartype
# 修改变量值
class ChangeStatement(AST):
    def __init__(self,left,operate,right):
        self.left = left
        self.operate = operate
        self.right = right
# 定义常量
class ConstStatement(AST):
    def __init__(self, left, operate, right,constype):
        self.left = left
        self.operate = operate
        self.right = right
        self.constype = constype
# elif语句
class ElifStatement(AST):
    def __init__(self,con,root):
        self.con = con
        self.root = root
# if条件判断语句
class IfStatement(AST):
    def __init__(self,condition,then,elifnode = None,elsenode = None):
        self.condition = condition
        self.then = then
        self.elifnode = elifnode if elifnode is not None else []
        self.elsenode = elsenode if elsenode is not None else EmptyStatement()
# while条件循环语句
class WhileStatement(AST):
    def __init__(self,condition,then):
        self.condition = condition
        self.then = then
# for循环与遍历语句
class ForStatement(AST):
    def __init__(self,var,iterobj,block):
        self.var = var
        self.iterobj = iterobj
        self.block = block
# 结构控制-break语句
class BreakStatement(AST):
    pass
# 结构控制-continue语句
class ContinueStatement(AST):
    pass
# 函数声明语句
class FunctionStatement(AST):
    def __init__(self,name,params,block,returns,default):
        self.name = name
        self.params = params
        self.block = block
        self.returns = returns
        self.default = default
# 返回函数语句
class ReturnStatement(AST):
    def __init__(self,value):
        self.value = value
# 导入模块语句
class ImportStatement(AST):
    def __init__(self,modulename) -> None:
        self.name = modulename

# 语句块
# 复合语句块
class CompoundBlock(AST):
    def __init__(self):
        self.children = []
# 程序块
class ProgramBlock(AST):
    def __init__(self,name,block):
        self.name = name
        self.block = block

# 内置函数
# 单行输出函数
class PrintlnFunction(AST):
    def __init__(self,text):
        self.text = text
# 单段输出函数
class PrintFunction(AST):
    def __init__(self,text):
        self.text = text
# 单行输入函数
class InputlnFunction(AST):
    def __init__(self,text):
        self.text = text
# 转换为整数函数
class TointFunction(AST):
    def __init__(self, text):
        self.text = text
# 生成列表函数
class RangeFunction(AST):
    def __init__(self,end,start = None,every = None):
        self.end = end
        self.start = start if start is not None else IntConst(Token(TokenType.INT,0))
        self.every = every if every is not None else IntConst(Token(TokenType.INT,1))
# 字符转ASCII函数
class OrdFunction(AST):
    def __init__(self,char):
        self.char = char
# ASCII转字符函数
class ChrFunction(AST):
    def __init__(self,num):
        self.num = num
# 获取可遍历对象长度函数
class LengthFunction(AST):
    def __init__(self,value):
        self.value = value


class Parser():
    def __init__(self,lexer):
        self.lexer = lexer
        self.token = self.lexer.get_token()
        self.constdict = {
            TokenType.INT:IntConst,
            TokenType.FLOAT: FloatConst,
            TokenType.STR:StringConst,
            TokenType.BOOL:BoolConst,
            TokenType.NULL:NullConst
        }
        self.functionlist = [
            TokenType.PRINTLN,
            TokenType.PRINT,
            TokenType.INPUTLN,
            TokenType.ORD,
            TokenType.CHR,
            TokenType.LENGTH,
            TokenType.TOINT,
            TokenType.RANGE
        ]
        self.statements = [
            TokenType.IF,
            TokenType.WHILE,
            TokenType.FOR,
            TokenType.FUN,
            TokenType.BREAK,
            TokenType.CONTINUE,
            TokenType.RETURN,
            TokenType.LET,
            TokenType.CONST,
            TokenType.IMPORT
        ]

    # 报错函数
    def error(self,error_code,token):
        raise ParserError(f"{error_code} -> {token}")

    # 验证Token类型
    def judg(self,_type = None):
        if _type is not None:
            if self.token._type == _type:
                self.token = self.lexer.get_token()
            else:
                print(_type)
                print(self.token._type)
                self.error(
                    "Unexpected token",
                    self.token
                )
        else:
            self.token = self.lexer.get_token()

    # 引用变量
    # 获取变量类型
    def vartype(self):
        node = VartypeTerm(self.token)
        self.judg(TokenType.VARTYPE)
        return node
    # 变量调用
    def variable(self):
        token = self.token
        self.judg(TokenType.VARIABLE)
        return VarTerm(token)
    # 修改变量值
    def change(self):
        left = self.variable()
        token = self.token
        self.judg(SymbolToken.ASSIGN)
        right = self.expr()
        node = ChangeStatement(left,token,right)
        return node

    # 获取常量值
    # 获取列表
    def get_list(self):
        self.judg(SymbolToken.LMID)
        res = []
        value1 = self.expr()
        res.append(value1)
        while self.token._type == SymbolToken.COMMA:
            self.judg(SymbolToken.COMMA)
            res.append(self.expr())
        self.judg(SymbolToken.RMID)
        node = ListConst(res)
        return node

    # 语句
    # 变量声明语句
    def let_statement(self):
        self.judg(TokenType.LET)
        left = self.variable()
        if self.token._type == SymbolToken.COLON:
            self.judg()
            vartype = self.vartype()
        else:
            vartype = VartypeTerm(Token(TokenType.AUTO,"auto"))
        token = self.token
        self.judg(SymbolToken.ASSIGN)
        right = self.expr()
        node = AssignStatement(left,token,right,vartype)
        return node
    # const常量声明语句
    def const_statement(self):
        self.judg(TokenType.CONST)
        left = self.variable()
        if self.token._type == SymbolToken.COLON:
            self.judg()
            constype = self.vartype()
        else:
            constype = VartypeTerm(Token(TokenType.AUTO,"auto"))
        token = self.token
        self.judg(SymbolToken.ASSIGN)
        right = self.expr()
        node = ConstStatement(left,token,right,constype)
        return node
    # if条件判断语句
    def if_statement(self):
        def get_branch(name,is_expr = True):
            self.judg(name)
            con = self.expr() if is_expr else None
            while True:
                if self.token._type == SymbolToken.ENDL:
                    self.token = self.lexer.get_token()
                    continue
                else:
                    break
            self.judg(SymbolToken.LPARAN)
            node = self.statement_list()
            root = CompoundBlock()
            root.children = node
            self.judg(SymbolToken.RPARAN)
            return con,root
        con,root = get_branch(TokenType.IF)
        elifnode = []
        elseroot = None
        while True:
            if self.token._type == TokenType.ELIF:
                elifcon,elifroot = get_branch(TokenType.ELIF)
                elifnode.append(ElifStatement(elifcon,elifroot))
            elif self.token._type == TokenType.ELSE:
                elsecon,elseroot = get_branch(TokenType.ELSE)
                break
            else:
                break
        return IfStatement(con,root,elifnode,elseroot)
    # while条件循环语句
    def while_statement(self):
        self.judg(TokenType.WHILE)
        con = self.expr()
        self.judg(SymbolToken.LPARAN)
        statements = self.statement_list()
        self.judg(SymbolToken.RPARAN)
        then = CompoundBlock()
        then.children = statements
        node = WhileStatement(con,then)
        return node
    # for循环与遍历语句
    def for_statement(self):
        self.judg(TokenType.FOR)
        var = self.variable()
        self.judg(TokenType.IN)
        iterobj = self.expr()
        self.judg(SymbolToken.LPARAN)
        statements = self.statement_list()
        self.judg(SymbolToken.RPARAN)
        blocks = CompoundBlock()
        blocks.children = statements
        node = ForStatement(var,iterobj,blocks)
        return node
    # 定义函数语句
    def fun_statement(self):
        self.judg(TokenType.FUN)
        funname = self.token.value
        self.judg(TokenType.VARIABLE)
        self.judg(SymbolToken.LBR)
        params = []
        num = 0
        if self.token._type == TokenType.VARIABLE:
            name1 = self.variable()
            self.judg(SymbolToken.COLON)
            tp = self.vartype()
            params.append(ParamTerm(name1,tp))
            while self.token._type == SymbolToken.COMMA:
                self.judg(SymbolToken.COMMA)
                name = self.variable()
                self.judg(SymbolToken.COLON)
                tp = self.vartype()
                if self.token._type == SymbolToken.ASSIGN:
                    self.judg(SymbolToken.ASSIGN)
                    num += 1
                    default = self.expr()
                    params.append(ParamTerm(name,tp,default))
                else:
                    if num:
                        self.error("错误")
                    else:
                        params.append(ParamTerm(name, tp))
        self.judg(SymbolToken.RBR)
        rettype = None
        if self.token._type == SymbolToken.ARROW:
            self.judg(SymbolToken.ARROW)
            rettype = self.vartype()
        self.judg(SymbolToken.LPARAN)
        block = self.statement_list()
        self.judg(SymbolToken.RPARAN)
        com = CompoundBlock()
        com.children = block
        node = FunctionStatement(funname,params,com,rettype,num)
        return node
    # 函数返回
    def return_statement(self):
        self.judg(TokenType.RETURN)
        value = self.expr()
        node = ReturnStatement(value)
        return node
    # 跳出循环
    def break_statement(self):
        self.judg(TokenType.BREAK)
        return BreakStatement()
    # 跳过本次循环
    def continue_statement(self):
        self.judg(TokenType.CONTINUE)
        return ContinueStatement()
    # 导入模块
    def import_statement(self):
        self.judg(TokenType.IMPORT)
        modname = self.variable()
        return ImportStatement(modname)

    # 内置函数
    # 单行输出语句
    def println_function(self):
        self.judg(TokenType.PRINTLN)
        self.judg(SymbolToken.LBR)
        text = self.expr()
        self.judg(SymbolToken.RBR)
        node = PrintlnFunction(text)
        return node
    # 单段输出语句
    def print_function(self):
        self.judg(TokenType.PRINT)
        self.judg(SymbolToken.LBR)
        text = self.expr()
        self.judg(SymbolToken.RBR)
        node = PrintFunction(text)
        return node
    # 获取可遍历对象长度
    def length_function(self):
        self.judg(TokenType.LENGTH)
        self.judg(SymbolToken.LBR)
        text = self.expr()
        self.judg(SymbolToken.RBR)
        node = LengthFunction(text)
        return node
    # 单行输入
    def inputln_funciton(self):
        self.judg(TokenType.INPUTLN)
        self.judg(SymbolToken.LBR)
        text = self.expr()
        self.judg(SymbolToken.RBR)
        node = InputlnFunction(text)
        return node
    # 转换为整数类型
    def toint_function(self):
        self.judg(TokenType.TOINT)
        self.judg(SymbolToken.LBR)
        text = self.expr()
        self.judg(SymbolToken.RBR)
        node = TointFunction(text)
        return node
    # 字符转ASCII
    def ord_function(self):
        self.judg(TokenType.ORD)
        self.judg(SymbolToken.LBR)
        text = self.expr()
        self.judg(SymbolToken.RBR)
        node = OrdFunction(text)
        return node
    # ASCII转字符
    def chr_function(self):
        self.judg(TokenType.CHR)
        self.judg(SymbolToken.LBR)
        text = self.expr()
        self.judg(SymbolToken.RBR)
        node = ChrFunction(text)
        return node
    # 生成列表
    def range_function(self):
        self.judg(TokenType.RANGE)
        self.judg(SymbolToken.LBR)
        param1 = self.expr()
        params = [param1]
        while self.token._type == SymbolToken.COMMA:
            self.judg(SymbolToken.COMMA)
            param = self.expr()
            params.append(param)
        self.judg(SymbolToken.RBR)
        leng = len(params)
        if leng == 1:
            node = RangeFunction(params[0])
        elif leng == 2:
            node = RangeFunction(params[1],params[0])
        elif leng == 3:
            node = RangeFunction(params[1], params[0],params[2])
        return node

    # 语句与程序
    # 获取单条语句
    def statement(self,is_change = 1):
        # print(self.token._type)
        if self.token._type in self.statements:
            node = getattr(self,self.token.value + "_statement")()
        elif self.token._type in self.functionlist:
            node = getattr(self,self.token.value + "_function")()
        elif self.token._type == TokenType.VARIABLE and is_change:
            while True:
                if self.lexer.char == " ":
                    self.lexer.advance()
                else:
                    break
            if self.lexer.char == "=":
                node = self.change()
            else:
                node = self.statement(0)
        elif self.token._type in (SymbolToken.ENDL,SymbolToken.LPARAN,SymbolToken.RPARAN,TokenType.END):
            node = EmptyStatement()
        else:
            node = self.expr()
        return node
    # 获取语句列表
    def statement_list(self):
        node = self.statement()
        nodelist = [node]
        while self.token._type == SymbolToken.SEMI or self.token._type == SymbolToken.ENDL:
            if self.token._type == SymbolToken.SEMI:
                self.judg(SymbolToken.SEMI)
            elif self.token._type == SymbolToken.ENDL:
                self.judg(SymbolToken.ENDL)
            nodelist.append(self.statement())
        return nodelist
    # 程序
    def program(self):
        nodelist = self.statement_list()
        root = CompoundBlock()
        root.children = nodelist
        node = ProgramBlock("main",root)
        return node
    # 空语句
    def empty(self):
        return EmptyStatement()
    
    # 表达式计算
    # 获取一个值
    def factor(self):
        token = self.token
        if token._type in (SymbolToken.ADD,SymbolToken.SUB,TokenType.NOT):
            self.judg()
            node = UnaryOperate(token,self.factor())
            return node
        elif token._type in self.constdict:
            self.judg()
            return self.constdict[token._type](token)
        elif token._type == SymbolToken.LBR:
            self.judg(SymbolToken.LBR)
            res = self.expr()
            self.judg(SymbolToken.RBR)
            return res
        elif token._type == SymbolToken.LMID:
            node = self.get_list()
            return node
        elif token._type in self.functionlist:
            return getattr(self,token.value + "_function")()
        else:
            node = self.variable()
            return node
    # 调用方法
    def method(self):
        node = self.factor()
        while True:
            if self.token._type in (SymbolToken.DOT,SymbolToken.LMID,SymbolToken.LBR):
                operate = self.token
                if operate._type == SymbolToken.DOT:
                    self.judg()
                    token = self.token
                    funname = self.token.value
                    self.judg(TokenType.VARIABLE)
                    self.judg(SymbolToken.LBR)
                    params = []
                    if self.token._type != SymbolToken.RBR:
                        right = self.expr()
                        params.append(right)
                    while self.token._type == SymbolToken.COMMA:
                        self.judg(SymbolToken.COMMA)
                        right = self.expr()
                        params.append(right)
                    self.judg(SymbolToken.RBR)
                    right = MethodTerm(funname,params,token)
                    node = DotOperate(node,right)
                elif operate._type == SymbolToken.LMID:
                    self.judg()
                    indexlist = []
                    index1 = self.expr()
                    indexlist.append(index1)
                    while self.token._type == SymbolToken.COLON:
                        self.judg(SymbolToken.COLON)
                        index = self.expr()
                        indexlist.append(index)
                    self.judg(SymbolToken.RMID)
                    node = IndexOperate(node,indexlist)
                elif operate._type == SymbolToken.LBR:
                    self.judg(SymbolToken.LBR)
                    params = []
                    if self.token._type != SymbolToken.RBR:
                        param = self.expr()
                        params.append(param)
                        while self.token._type == SymbolToken.COMMA:
                            self.judg(SymbolToken.COMMA)
                            param = self.expr()
                            params.append(param)
                    self.judg(SymbolToken.RBR)
                    node = FuncallOperate(node,params)
                else:
                    break
            else:
                break
        return node
    # 计算乘方
    def xterm(self):
        node = self.method()
        while True:
            if self.token._type == SymbolToken.POWER:
                operate = self.token
                self.judg()
                node = BinOperate(node,operate,self.method())
            else:
                break
        return node
    # 计算次一级运算符
    def term(self):
        node = self.xterm()
        while True:
            if self.token._type in (SymbolToken.MUL,SymbolToken.DIV,SymbolToken.MOD):
                operate = self.token
                self.judg()
                node = BinOperate(node,operate,self.xterm())
            else:
                break
        return node
    # 计算顶级二元运算符
    def addsub(self):
        node = self.term()
        while True:
            if self.token._type in (SymbolToken.ADD,SymbolToken.SUB):
                operate = self.token
                self.judg()
                node = BinOperate(node,operate,self.term())
            else:
                break
        return node
    def compare(self):
        node = self.addsub()
        while True:
            if self.token._type in (SymbolToken.EQUAL,SymbolToken.LESS,SymbolToken.GREATER,
            SymbolToken.LESSEQUAL,SymbolToken.GREATEREQUAL,SymbolToken.NOTEQUAL):
                operate = self.token
                self.judg()
                node = BinOperate(node,operate,self.addsub())
            else:
                break
        return node
    def expr(self):
        node = self.compare()
        while True:
            if self.token._type in (TokenType.AND,TokenType.OR):
                operate = self.token
                self.judg()
                node = BinOperate(node,operate,self.compare())
            else:
                break
        return node

class Symbol():
    def __init__(self,name,stype = None):
        self.name = name
        self.stype = stype
        self.level = 0

class BuiltinTypeSymbol(Symbol):
    def __init__(self,name):
        super().__init__(name)
        self.table = {
            "str":{
                "split":([("char","str")],"array"),
                "isdigit":([],"bool"),
                "isalpha":([],"bool"),
                "isalnum":([],"bool"),
                "startswith":([("char","str")],"bool"),
                "endswith":([("char","str")],"bool")
            },
            "array":{
                "append":([("object","auto")],"nulltype"),
                "remove":([("object","auto")],"nulltype"),
                "insert":([("object","auto")],"nulltype")
            },
            "int":{},
            "real":{},
            "bool":{},
            "nulltype":{},
            "function":{},
            "module":{}
        }
        self.methods = {}
        self.build_methods()

    def build_param(self,name,tp):
        return VarSymbol(name,tp)

    def build_methods(self):
        methods = self.table.get(self.name)
        for x in methods:
            params = []
            for f in methods[x][0]:
                params.append(self.build_param(f[0],f[1]))
            m = FunSymbol(x,params)
            m.returns = methods[x][1]
            self.methods[x] = m

class ConstSymbol(Symbol):
    def __init__(self, name,stype):
        super().__init__(name,stype)

class VarSymbol(Symbol):
    def __init__(self,name,stype):
        super().__init__(name,stype)
        self.default = None
        self.arraytp = None

class FunSymbol(Symbol):
    def __init__(self,name,params = None):
        super().__init__(name)
        if params is None:
            self.params = []
        else:
            self.params = params
        self.blockast = None
        self.returns = None
        self.defaultnum = None
        self.default = None
        self.stype = BuiltinTypeSymbol("function")

class ScopeSymbolTable():
    def __init__(self,scopename = None,scopelv = None,enclosing = None):
        self.symbol = OrderedDict()
        self.name = scopename
        self.level = scopelv
        self.enclosing = enclosing

    def init(self):
        self.define(BuiltinTypeSymbol("int"))
        self.define(BuiltinTypeSymbol("real"))
        self.define(BuiltinTypeSymbol("bool"))
        self.define(BuiltinTypeSymbol("str"))
        self.define(BuiltinTypeSymbol("nulltype"))
        self.define(BuiltinTypeSymbol("array"))
        self.define(BuiltinTypeSymbol("function"))
        self.define(BuiltinTypeSymbol("module"))

    def define(self,symbol):
        symbol.level = self.level
        self.symbol[symbol.name] = symbol

    def query(self,name):
        symbol = self.symbol.get(name)
        if symbol is not None:
            return symbol
        if self.enclosing is not None:
            return self.enclosing.query(name)

class Visitor(): # 设计模式-访问者模式
    def visit(self,node):
        method = type(node).__name__
        visitor = getattr(self,"visit_" + method)
        return visitor(node)

class SemanticAnalyzer(Visitor):
    def __init__(self):
        self.table = None

    def error(self,msg):
        raise SemanticError(msg)

    def visit_ProgramBlock(self,node):
        global_table = ScopeSymbolTable("main",1,self.table)
        global_table.init()
        self.table = global_table
        self.visit(node.block)

    def visit_CompoundBlock(self,node):
        tpl = []
        for child in node.children:
            if isinstance(child,ReturnStatement):
                tp = self.visit(child)
                tpl.append(tp)
            else:
                self.visit(child)
        return tpl

    def visit_AssignStatement(self,node):
        varname = node.left.name
        tpname = node.vartype.name
        if tpname == "auto":
            valuetp = self.visit(node.right)
            varsymbol = VarSymbol(varname, self.table.query(valuetp))
            if valuetp == "array":
                pass
            self.table.define(varsymbol)
        elif tpname == "function":
            if self.visit(node.right) == "function":
                right = self.table.query(node.right.name)
                funsymbol = FunSymbol(varname,right.params)
                funsymbol.blockast = right.blockast
                funsymbol.returns = right.returns
                funsymbol.defaultnum = right.defaultnum
                self.table.define(funsymbol)
            else:
                self.error("类型错误")
        else:
            symbol = self.table.query(tpname)
            varsymbol = VarSymbol(varname,symbol)
            self.table.define(varsymbol)
            self.visit(node.left)
            tp = self.visit(node.right)
            if symbol.name != tp:
                self.error(f"variable {varname}'s type define as {symbol.name} but assign as {tp}")

    def visit_ChangeStatement(self, node):
        name = node.left.name
        symbol = self.table.query(name)
        if symbol:
            if isinstance(symbol,ConstSymbol):
                self.error("不能修改常量")
            else:
                tp = self.visit(node.right)
                if symbol.stype.name != tp:
                    self.error(f"variable {name}'s type define as {symbol.stype.name} but assign as {tp}")
                elif tp == "function":
                    right = self.table.query(node.right.name)
                    funsymbol = FunSymbol(name,right.params)
                    funsymbol.blockast = right.blockast
                    funsymbol.returns = right.returns
                    funsymbol.defaultnum = right.defaultnum
                    self.table.define(funsymbol)
        else:
            self.error(f"name {name} is not defined")

    def visit_ConstStatement(self,node):
        varname = node.left.name
        tpname = node.constype.name
        if tpname == "auto":
            valuetp = self.visit(node.right)
            varsymbol = ConstSymbol(varname, self.table.query(valuetp))
            self.table.define(varsymbol)
        elif tpname == "function":
            self.error("常量不能被定义为函数")
        else:
            symbol = self.table.query(tpname)
            varsymbol = ConstSymbol(varname,symbol)
            self.table.define(varsymbol)
            self.visit(node.left)
            tp = self.visit(node.right)
            if symbol.name != tp:
                self.error(f"variable {varname}'s type define as {symbol.name} but assign as {tp}")

    def visit_VarTerm(self,node):
        name = node.name
        symbol = self.table.query(name)
        if not symbol:
            self.error(f"name {name} is not defined")
        return symbol.stype.name

    def visit_UnaryOperate(self, node):
        return self.visit(node.expr)

    def visit_BinOperate(self, node):
        ltp = self.visit(node.left)
        rtp = self.visit(node.right)
        op = node.op._type
        if op in (SymbolToken.ADD,SymbolToken.SUB,SymbolToken.MOD,SymbolToken.POWER):
            if ltp == "function" or rtp == "function":
                self.error("function type cannot do add or sub operate")
            if ltp == rtp:
                if ltp not in ("bool","nulltype") and rtp not in ("bool","nulltype"):
                    return ltp
                else:
                    self.error("type bool or nulltype cannot do add or sub operate")
            elif (ltp,rtp) in ("int","real"):
                return "real"
            else:
                self.error(f"{ltp} ")
        elif op in (SymbolToken.MUL,SymbolToken.DIV):
            if ltp == "function" or rtp == "function":
                self.error("function type cannot do mul or div operate")
            if ltp == rtp:
                if ltp not in ("bool","nulltype") and rtp not in ("bool","nulltype"):
                    return ltp
                else:
                    self.error("type bool or nulltype cannot do add or sub operate")
            elif (ltp,rtp) in ("int","real"):
                return "real"
            elif (ltp,rtp) in ("int","str"):
                return "str"
            else:
                self.error("类型错误")
        elif op in (SymbolToken.LESS,SymbolToken.GREATER,SymbolToken.LESSEQUAL,SymbolToken.GREATEREQUAL):
            if ltp in ("int","real") and rtp in ("int","real"):
                return "bool"
            else:
                self.error("类型错误")
        else:
            return "bool"

    def visit_DotOperate(self,node):
        left = node.left
        right = node.right
        ltp = self.visit(left)
        methods = self.table.query(ltp).methods
        mname = right.name
        if mname in methods:
            if len(right.params) == len(methods[mname].params):
                for x in range(len(right.params)):
                    mtp = methods[mname].params[x].stype
                    if mtp != "auto":
                        if self.visit(right.params[x]) == mtp:
                            pass
                        else:
                            self.error("参数类型错误")
                    else:
                        pass
                return methods[mname].returns
            else:
                self.error("参数数量错误")
        else:
            self.error("方法不存在")

    def visit_IndexOperate(self,node):
        left = self.visit(node.left)
        if left in ("array","str"):
            for x in node.right:
                if self.visit(x) == "int":
                    pass
                else:
                    self.error("类型错误")
            return left
        else:
            self.error("类型错误")

    def visit_FuncallOperate(self,node):
        left = self.visit(node.left)
        if left == "function":
            if isinstance(node.left,VarTerm):
                funname = node.left.name
                table = self.table.query(funname)
                defaultnum = table.defaultnum
                greeting = table.params
                arg = node.right
                if len(greeting) <= len(arg) + defaultnum:
                    for i in range(len(arg)):
                        if self.visit(arg[i]) == greeting[i].stype.name:
                            pass
                        else:
                            self.error("类型错误")
                    return table.returns
                else:
                    self.error(f"function {funname} accept {len(greeting)} parameters but {len(arg)} were given")
            elif isinstance(node.left,FuncallOperate):
                self.visit(node.left)

    def visit_IfStatement(self,node):
        self.visit(node.condition)
        self.visit(node.then)
        self.visit(node.elsenode)

    def visit_WhileStatement(self,node):
        self.visit(node.condition)
        self.visit(node.then)

    def visit_ForStatement(self,node):
        self.visit(node.iterobj)

    def visit_ImportStatement(self,node):
        with open(f"./{node.name.name}.df","r") as file:
            code = file.read()
        # 词法分析
        lexer = Lexer(code)
        # 语法分析
        parser = Parser(lexer)
        tree = parser.program()
        self.visit(tree)

    def visit_FunctionStatement(self,node):
        funsymbol = FunSymbol(node.name)
        self.table.define(funsymbol)
        funtable = ScopeSymbolTable(node.name,self.table.level + 1,self.table)
        self.table = funtable
        for param in node.params:
            ptype = self.table.query(param._type.name)
            pname = param.name.name
            defaultvalue = param.default
            if ptype.name != "function":
                symbol = VarSymbol(pname,ptype)
            else:
                symbol = FunSymbol(pname,[])
                symbol.blockast = EmptyStatement()
                symbol.returns = None
                symbol.defaultnum = 0
            symbol.default = defaultvalue
            self.table.define(symbol)
            funsymbol.params.append(symbol)
        tpl = self.visit(node.block)
        ntp = None
        for i in range(len(tpl)):
            if i == 0:
                ntp = tpl[0]
            else:
                if tpl[i] == ntp:
                    ntp = tpl[i]
                else:
                    self.error("类型错误")
        if ntp != None and node.returns != None:
            if ntp != node.returns.name:
                self.error("类型错误")
        elif ntp == None and node.returns == None:
            pass
        elif ntp == None and node.returns != None:
            self.error("类型错误")
        self.table = self.table.enclosing
        funsymbol.blockast = node.block
        funsymbol.returns = node.returns
        funsymbol.defaultnum = node.default

    def visit_ReturnStatement(self,node):
        return self.visit(node.value)

    def visit_PrintlnFunction(self,node):
        self.visit(node.text)
        return "nulltype"

    def visit_PrintFunction(self,node):
        self.visit(node.text)
        return "nulltype"

    def visit_InputlnFunction(self,node):
        self.visit(node.text)
        return "str"

    def visit_TointFunction(self,node):
        self.visit(node.text)
        return "int"

    def visit_LengthFunction(self,node):
        tp = self.visit(node.value)
        if tp in ("str","array"):
            return "int"
        else:
            self.error("类型错误")

    def visit_OrdFunction(self,node):
        tp = self.visit(node.char)
        if tp == "str":
            return "int"
        else:
            self.error("类型错误")
            
    def visit_ChrFunction(self,node):
        tp = self.visit(node.num)
        if tp == "int":
            return "str"
        else:
            self.error("类型错误")

    def visit_RangeFunction(self,node):
        start = self.visit(node.start)
        end = self.visit(node.end)
        every = self.visit(node.every)
        if start == end == every == "int":
            return "array"
        else:
            self.error("类型错误")

    def visit_EmptyStatement(self,node):pass
    visit_BreakStatement = visit_EmptyStatement
    visit_ContinueStatement = visit_EmptyStatement
    def visit_BoolConst(self,node):
        return "bool"
    def visit_IntConst(self,node):
        return "int"
    def visit_StringConst(self,node):
        return "str"
    def visit_NullConst(self,node):
        return "nulltype"
    def visit_ListConst(self,node):
        if node.value:
            ori = node.value[0]  
        else: return "array"
        for i in node.value:
            tp = self.visit(i)
            if tp != ori:
                self.error("列表中元素类型必须相同")
        return "array"
    def visit_FloatConst(self,node):
        return "real"

class Sym:
    pass
class IntSym(Sym):
    def __init__(self, value):
        self.value = value
        self.str = str(value)
class RealSym(Sym):
    def __init__(self, value):
        self.value = value
        self.str = str(value)
class BoolSym(Sym):
    def __init__(self, value):
        self.value = value
        if self.value is True:
            self.str = "true"
        else:
            self.str = "false"
class NulltypeSym(Sym):
    def __init__(self, value):
        self.value = value
        self.str = "null"
class StringSym(Sym):
    def __init__(self, value):
        self.value = value
        self.str = value
    def split(self,char):
        return VarSym(self.value.split(char))
    def isdigit(self):
        return VarSym(self.value.isdigit())
    def isalpha(self):
        return VarSym(self.value.isalpha())
    def isalnum(self):
        return VarSym(self.value.isalnum())
    def startswith(self,char):
        return VarSym(self.value.startswith(char))
    def endswith(self, char):
        return VarSym(self.value.endswith(char))
class ArraySym(Sym):
    def __init__(self, value):
        self.value = value
        self.str = str(value)
    def append(self,value):
        self.value.append(value)
        return VarSym(self.value)
    def remove(self,value):
        self.value.remove(value)
        return VarSym(self.value)
    def insert(self,pos,value):
        self.value.insert(pos, value)
        return VarSym(self.value)
class FunctionSym(Sym):
    def __init__(self,block,enclosing):
        self.block = block
        self.params = {}
        self.str = "<function object>"
        self.enclosing = enclosing
def VarSym(value):
    if isinstance(value,bool):
        return BoolSym(value)
    elif isinstance(value,int):
        return IntSym(value)
    elif isinstance(value,str):
        return StringSym(value)
    elif value is None:
        return NulltypeSym(value)
    elif isinstance(value,list):
        return ArraySym(value)
    elif isinstance(value,float):
        return RealSym(value)

class CallStack:
    def __init__(self):
        self.stack = []

    def push(self, ar):
        self.stack = [ar] + self.stack

    def pop(self):
        value = self.stack[0]
        self.stack = self.stack[1:]
        return value

    def peek(self):
        return self.stack[0]

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

class Interpreter(Visitor):
    def __init__(self,tree):
        self.tree = tree
        self.stack = CallStack()

    def error(self,msg):
        raise InterpreterError(msg)

    def visit_BinOperate(self, node):
        left = self.visit(node.left).value
        right = self.visit(node.right).value
        tp = node.op._type
        if tp == SymbolToken.ADD:
            value =  left + right
        if tp == SymbolToken.SUB:
            value =  left - right
        if tp == SymbolToken.MUL:
            value =  left * right
        if tp == SymbolToken.DIV:
            res = left / right
            if res % 1 == 0:
                value =  int(res)
            else:
                value =  res
        if tp == SymbolToken.POWER:
            value =  left ** right
        if tp == SymbolToken.MOD:
            value =  left % right
        if tp == SymbolToken.EQUAL:
            value =  bool(left == right)
        if tp == SymbolToken.LESS:
            value =  bool(left < right)
        if tp == SymbolToken.GREATER:
            value =  bool(left > right)
        if tp == SymbolToken.LESSEQUAL:
            value =  bool(left <= right)
        if tp == SymbolToken.GREATEREQUAL:
            value =  bool(left >= right)
        if tp == SymbolToken.NOTEQUAL:
            value =  bool(left != right)
        if tp == TokenType.AND:
            value =  bool(left and right)
        if tp == TokenType.OR:
            value =  bool(left or right)
        return VarSym(value)

    def visit_UnaryOperate(self, node):
        op = node.op._type
        if op == SymbolToken.ADD:
            value =  +self.visit(node.expr).value
        elif op == SymbolToken.SUB:
            value =  -self.visit(node.expr).value
        elif op == SymbolToken.NOT:
            value =  not self.visit(node.expr).value
        return VarSym(value)

    def visit_DotOperate(self, node):
        left = self.visit(node.left)
        revice_self = [
            "append",
            "remove",
            "insert"
        ]
        params = [self.visit(var).value for var in node.right.params]
        mname = node.right.name
        if mname in revice_self:
            ar = self.stack.peek()
            ar[node.left.name] = getattr(left,mname)(*params)
        else:
            return getattr(left,mname)(*params)

    def visit_IndexOperate(self,node):
        left = self.visit(node.left).value
        right = [self.visit(value).value for value in node.right]
        leng = len(right)
        if leng == 1:
            value = left[right[0]]
        elif leng == 2:
            value = left[right[0]:right[1]]
        elif leng == 3:
            value = left[right[0]:right[1]:right[2]]
        return VarSym(value)

    def visit_FuncallOperate(self,node):
        left = node.left
        symbol = self.visit(left)
        nextar = self.stack.peek()
        ar = ActivationRecord("lambda","function",nextar.level + 1)
        formal = symbol.params
        actual = node.right
        forkey = list(formal.keys())
        for x in range(len(forkey)):
            param_symbol = formal[forkey[x]]
            paramname = forkey[x]
            if x < len(actual):
                ar[paramname] = self.visit(actual[x])
            else:
                ar[paramname] = self.visit(param_symbol)
        ar.members.update(symbol.enclosing)
        self.stack.push(ar)
        is_return = self.visit(symbol.block)
        self.stack.pop()
        return is_return

    def visit_IntConst(self,node):
        return VarSym(node.value)

    def visit_FloatConst(self,node):
        return VarSym(node.value)

    def visit_StringConst(self,node):
        value = node.value
        return VarSym(value)

    def visit_BoolConst(self,node):
        value = node.value
        if value == "true":
            return VarSym(True)
        else:
            return VarSym(False)

    def visit_NullConst(self,node):
        return VarSym(None)

    def visit_AssignStatement(self,node):
        varname = node.left.name
        ar = self.stack.peek()
        varvalue = self.visit(node.right)
        ar[varname] = varvalue

    visit_ConstStatement = visit_AssignStatement

    def visit_ChangeStatement(self,node):
        varname = node.left.name
        ar = self.stack.peek()
        if varname in ar.members:
            ar[varname] = self.visit(node.right)
        else:
            self.error(f"name '{varname}' is not defined")

    def visit_VarTerm(self,node):
        varname = node.name
        index = 0
        while index < len(self.stack.stack):
            ar = self.stack.stack[index]
            if varname in ar.members:
                return ar[varname]
            else:
                index = index + 1
        self.error(f"name '{varname}' is not defined")

    def visit_ProgramBlock(self,node):
        program_name = node.name
        ar = ActivationRecord(program_name,"main",1)
        self.stack.push(ar)
        self.visit(node.block)
        self.stack.pop()

    def visit_CompoundBlock(self,node):
        for child in node.children:
            if type(child).__name__ == "ReturnStatement":
                ret = self.visit(child)
                return ret
            else:
                ret = self.visit(child)
                if ret == BreakStatement:
                    return BreakStatement
                if ret == ContinueStatement:
                    return ContinueStatement
        return None

    def visit_IfStatement(self,node):
        if self.visit(node.condition).value:
            ret = self.visit(node.then)
            if ret == BreakStatement:
                return BreakStatement
            if ret == ContinueStatement:
                return ContinueStatement
        else:
            num = 0
            for i in node.elifnode:
                if i.con:
                    ret = self.visit(i.root)
                    if ret == BreakStatement:
                        return BreakStatement
                    if ret == ContinueStatement:
                        return ContinueStatement
                    break
                else:
                    num += 1
            if num == len(node.elifnode): # 当所有的elif节点都不满足时
                ret = self.visit(node.elsenode)
                if ret == BreakStatement:
                    return BreakStatement
                if ret == ContinueStatement:
                    return ContinueStatement

    def visit_WhileStatement(self,node):
        con = self.visit(node.condition).value
        while con:
            print("这是一次")
            ret = self.visit(node.then)
            if ret == BreakStatement:
                break
            elif ret == ContinueStatement:
                con = self.visit(node.condition).value
                continue
            else:
                con = self.visit(node.condition).value

    def visit_ForStatement(self,node):
        ar = self.stack.peek()
        var = node.var.name
        iterobj = self.visit(node.iterobj).value
        for x in iterobj:
            ar[var] = VarSym(x)
            ret = self.visit(node.block)
            if ret == BreakStatement:
                break
            elif ret == ContinueStatement:
                continue

    def visit_ImportStatement(self,node):
        with open(f"./{node.name.name}.df","r") as file:
            code = file.read()
        # 词法分析
        lexer = Lexer(code)
        # 语法分析
        parser = Parser(lexer)
        tree = parser.program()
        self.visit(tree.block)

    def visit_FunctionStatement(self,node):
        ar = self.stack.peek()
        name = node.name
        if ar.level == 1:
            enclosing = {}
        else:
            enclosing = ar.members
        fun = FunctionSym(node.block,enclosing)
        for param in node.params:
            pname = param.name.name
            dvalue = param.default
            fun.params[pname] = dvalue
        ar[name] = fun

    def visit_ReturnStatement(self,node):
        ar = self.stack.peek()
        if ar.level <= 1:
            self.error("can not return from main")
        else:
            return self.visit(node.value)

    def visit_BreakStatement(self,node):
        return BreakStatement

    def visit_ContinueStatement(self,node):
        return ContinueStatement

    def visit_PrintlnFunction(self,node):
        value = self.visit(node.text)
        sys.stdout.write(value.str + "\n")
        return None

    def visit_PrintFunction(self,node):
        value = self.visit(node.text)
        sys.stdout.write(value.str)
        return None

    def visit_InputlnFunction(self,node):
        value = self.visit(node.text)
        return input(value.str)

    def visit_TointFunction(self,node):
        return VarSym(int(self.visit(node.text).value))
        
    def visit_LengthFunction(self,node):
        return VarSym(len(self.visit(node.value).value))

    def visit_OrdFunction(self,node):
        return VarSym(ord(self.visit(node.char).value))

    def visit_ChrFunction(self,node):
        return VarSym(chr(self.visit(node.num).value))

    def visit_RangeFunction(self,node):
        start = self.visit(node.start).value
        end = self.visit(node.end).value
        every = self.visit(node.every).value
        return VarSym(list(range(start,end,every)))

    def visit_ListConst(self,node):
        res = []
        for i in node.value:
            res.append(self.visit(i).value)
        return VarSym(res)

    def visit_EmptyStatement(self,node):
        pass

    def interpret(self):
        return self.visit(self.tree)


# 堆栈机字节码翻译器
class StackBytecode(Visitor):
    def __init__(self, tree):
        self.tree = tree
        self.format_len = 30
        self.if_node_num = 0
        self.while_node_num = 0
        self.for_node_num = 0
        self.stack = CallStack()

    def stackcode(self):
        tree = self.tree  # 获取AST
        self.instructions=[]  #所有的字节码都装在这里面
        self.visit(tree)  #  遍历AST
        return self.instructions

    def insert_inst(self,inst):
        self.instructions.append(inst)

    def visit_IntConst(self,node):
        self.insert_inst('push ' + str(node.value))

    def visit_UnaryOperate(self, node): #一元运算符类型节点的方法
        op = node.op.type
        if op == SymbolToken.ADD: #+
            self.visit(node.expr) #直接取表达式的结果
        elif op == SymbolToken.SUB: #-
            self.visit(node.expr)
            self.insert_inst('neg')  #对表达式的结果取相反数
        elif op == TokenType.NOT: #NOT
            self.visit(node.expr)
            self.insert_inst('not')

    def visit_BinOperate(self,node): # 二元运算符节点
        self.visit(node.left)
        self.visit(node.right)
        tp = node.op._type
        if tp == SymbolToken.ADD:
            self.insert_inst('add')
        elif tp == SymbolToken.SUB:
            self.insert_inst("sub")
        elif tp == SymbolToken.MUL:
            self.insert_inst("mul")
        elif tp == SymbolToken.DIV:
            self.insert_inst("div")

    def visit_AssignStatement(self,node):
        name = node.left.name
        self.visit(node.right)
        self.insert_inst("pop " + name)

    def visit_ChangeStatement(self,node):
        name = node.left.name
        self.visit(node.right)
        self.insert_inst("pop " + name)

expr = """
if 6 == 1*2*3{
    println("1")
}
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