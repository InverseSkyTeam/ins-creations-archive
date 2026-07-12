import copy
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
    LINEDOWN = "|"


# 类型Token
class TokenType(Enum):
    # 内置类型
    INT = "INT" # 整数类型
    FLOAT = "FLOAT" # 浮点数类型
    STR = "STR" # 字符串类型
    BOOL = "BOOL" # 布尔类型
    LIST = "LIST" # 列表类型
    MAP = "MAP" # 地图类型
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
    DEFAULT = "DEFAULT" # 变量判断-default
    # 循环
    WHILE = "WHILE" # 条件循环
    LOOP = "LOOP" # 无限循环
    FOR = "FOR" # 遍历对象
    IN ="IN" # for语句组成部分
    BREAK = "BREAK" # 结构控制-break
    CONTINUE = "CONTINUE" # 结构控制-continue
    # 函数
    FUN = "FUN" # 函数定义
    RETURN = "RETURN" # 函数返回
    FUNC = "FUNC" # 函数字面量
    # 导入模块
    IMPORT = "IMPORT"
    AS = "AS"
    # 调试
    DEBUGGER = "DEBUGGER" # 调试
    # 布尔运算
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
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
    defaultR = Token(TokenType.DEFAULT,"default") # 变量判断-default
    whileR = Token(TokenType.WHILE,"while") # 条件循环
    loopR = Token(TokenType.LOOP,"loop") # 无限循环
    forR = Token(TokenType.FOR,"for") # 遍历数组
    inR = Token(TokenType.IN,"in") # for语句必需结构
    importR = Token(TokenType.IMPORT,"import") # 导入模块语句
    asR = Token(TokenType.AS,"as") # 导入别名语句
    debuggerR = Token(TokenType.DEBUGGER, "debugger") # 调试语句
    # 结构体
    funR = Token(TokenType.FUN,"fun") # 函数定义
    funcR = Token(TokenType.FUNC,"func")
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
    functionR = Token(TokenType.VARTYPE,"function") # 函数类型
    mapR = Token(TokenType.VARTYPE,"map") # 地图类型
    autoR = Token(TokenType.VARTYPE, "auto") # 自动推导
    # 内置常量
    trueR = Token(TokenType.BOOL,"true") # bool-真值
    talseR = Token(TokenType.BOOL,"false") # bool-假值
    nullR = Token(TokenType.NULL,"null") # NoneType-空值


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

    def tokens(self):
        ret = []
        while True:
            token = self.get_token()
            ret.append(token)
            if token._type == TokenType.END:
                break
        return ret



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
# 字典常量
class MapConst(AST):
    def __init__(self,value):
        self.value = value
# 函数字面量
class FuncConst(AST):
    def __init__(self,params,block,ret):
        self.params = params
        self.block = block
        self.ret = ret

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
# case语句
class CaseStatement(AST):
    def __init__(self,con,block) -> None:
        self.con = con
        self.block = block
# switch语句
class SwitchStatement(AST):
    def __init__(self,var,case,default):
        self.var = var
        self.case = case
        self.default = default
#调试语句
class DebuggerStatement(AST):
    pass

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
# 作用域块
class ScopeBlock(AST):
    def __init__(self,block) -> None:
        self.block = block

class Parser():
    def __init__(self,tokens):
        self.tokens = tokens
        self.pos = 0
        self.token = self.tokens[self.pos]
        self.constdict = {
            TokenType.INT:IntConst,
            TokenType.FLOAT: FloatConst,
            TokenType.STR:StringConst,
            TokenType.BOOL:BoolConst,
            TokenType.NULL:NullConst
        }
        self.statements = [
            TokenType.IF,
            TokenType.WHILE,
            TokenType.LOOP,
            TokenType.FOR,
            TokenType.FUN,
            TokenType.BREAK,
            TokenType.CONTINUE,
            TokenType.RETURN,
            TokenType.LET,
            TokenType.CONST,
            TokenType.IMPORT,
            TokenType.SWITCH,
            TokenType.DEBUGGER
        ]

    # 报错函数
    def error(self,error_code,token):
        raise ParserError(f"{error_code} -> {token}")

    # 验证Token类型
    def judg(self,_type = None):
        if _type is not None:
            if self.token._type == _type:
                self.pos += 1
                self.token = self.tokens[self.pos]
            else:
                print(_type)
                print(self.token._type)
                self.error(
                    "Unexpected token",
                    self.token
                )
        else:
            self.pos += 1
            self.token = self.tokens[self.pos]

    def back(self,num):
        self.pos -= num
        self.token = self.tokens[self.pos]

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
        left = self.method()
        if isinstance(left,(VarTerm,IndexOperate)):
            token = self.token
            self.judg(SymbolToken.ASSIGN)
            right = self.expr()
            node = ChangeStatement(left,token,right)
            return node
        else:
            self.error("错误")

    def newscope(self):
        self.judg(SymbolToken.LPARAN)
        stmt = self.statement_list()
        block = CompoundBlock()
        block.children = stmt
        self.judg(SymbolToken.RPARAN)
        return ScopeBlock(block)

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
    def get_map(self):
        self.judg(SymbolToken.LPARAN)
        res = {}
        if self.token._type == SymbolToken.RPARAN:
            self.judg(SymbolToken.RPARAN)
            return MapConst(res)
        name1 = self.variable().name
        self.judg(SymbolToken.COLON)
        value1 = self.expr()
        res[name1] = value1
        while self.token._type == SymbolToken.COMMA:
            name = self.variable().name
            self.judg(SymbolToken.COLON)
            value = self.expr()
            res[name] = value
        self.judg(SymbolToken.RPARAN)
        return MapConst(res)
    def func(self):
        self.judg(TokenType.FUNC)
        self.judg(SymbolToken.LBR)
        params = []
        num = 0
        if self.token._type == TokenType.VARIABLE:
            name1 = self.variable()
            self.judg(SymbolToken.COLON)
            tp = self.vartype()
            if self.token._type == SymbolToken.ASSIGN:
                self.judg()
                dv = self.expr()
                num += 1
            else:dv = None
            params.append(ParamTerm(name1,tp,dv))
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
        stmt = self.statement_list()
        self.judg(SymbolToken.RPARAN)
        block = CompoundBlock()
        block.children = stmt
        return FuncConst(params,block,rettype)
    def fn(self):
        self.judg(SymbolToken.LINEDOWN)
        params = []
        num = 0
        if self.token._type == TokenType.VARIABLE:
            name1 = self.variable()
            self.judg(SymbolToken.COLON)
            tp = self.vartype()
            if self.token._type == SymbolToken.ASSIGN:
                self.judg()
                dv = self.expr()
                num += 1
            else:dv = None
            params.append(ParamTerm(name1,tp,dv))
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
        self.judg(SymbolToken.LINEDOWN)
        rettype = None
        if self.token._type == SymbolToken.ARROW:
            self.judg(SymbolToken.ARROW)
            rettype = self.vartype()
        if self.token._type == SymbolToken.LPARAN:
            self.judg(SymbolToken.LPARAN)
            stmt = self.statement_list()
            self.judg(SymbolToken.RPARAN)
        else:
            ex = self.expr()
            stmt = [ReturnStatement(ex)]
        block = CompoundBlock()
        block.children = stmt
        return FuncConst(params,block,rettype)

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
            while self.token._type == SymbolToken.ENDL:
                self.judg()
            if self.token._type == SymbolToken.LPARAN:
                self.judg(SymbolToken.LPARAN)
                node = self.statement_list()
                self.judg(SymbolToken.RPARAN)
            else:
                node = [self.statement()]
            root = CompoundBlock()
            root.children = node
            return con,root
        con,root = get_branch(TokenType.IF)
        elifnode = []
        elseroot = None
        n = 0
        while self.token._type == SymbolToken.ENDL:
            self.judg()
            n += 1
        if self.token._type not in (TokenType.ELIF,TokenType.ELSE):
            self.back(n)
        del n # 不用了就释放掉
        while True:
            if self.token._type == TokenType.ELIF:
                elifcon,elifroot = get_branch(TokenType.ELIF)
                elifnode.append(ElifStatement(elifcon,elifroot))
                n = 0
                while self.token._type == SymbolToken.ENDL:
                    self.judg()
                    n += 1
                if self.token._type not in (TokenType.ELIF,TokenType.ELSE):
                    self.back(n)
                del n
            elif self.token._type == TokenType.ELSE:
                elsecon,elseroot = get_branch(TokenType.ELSE,False)
                break
            else:
                break
        return IfStatement(con,root,elifnode,elseroot)
    # switch-case语句
    def switch_statement(self):
        self.judg(TokenType.SWITCH)
        var = self.expr()
        while self.token._type == SymbolToken.ENDL:
            self.judg()
        self.judg(SymbolToken.LPARAN)
        caselist = []
        default = EmptyStatement()
        while True:
            if self.token._type == TokenType.CASE:
                self.judg(TokenType.CASE)
                con = self.expr()
                self.judg(SymbolToken.COLON)
                block = self.statement_list()
                com = CompoundBlock()
                com.children = block
                caselist.append(CaseStatement(con,com))
            elif self.token._type == TokenType.DEFAULT:
                self.judg(TokenType.DEFAULT)
                self.judg(SymbolToken.COLON)
                block = self.statement_list()
                com = CompoundBlock()
                com.children = block
                default = com
            elif self.token._type == SymbolToken.ENDL:
                self.judg()
                continue
            else:
                break
        self.judg(SymbolToken.RPARAN)
        return SwitchStatement(var,caselist,default)
    # while条件循环语句
    def while_statement(self):
        self.judg(TokenType.WHILE)
        con = self.expr()
        if self.token._type == SymbolToken.LPARAN:
            self.judg(SymbolToken.LPARAN)
            statements = self.statement_list()
            self.judg(SymbolToken.RPARAN)
        else:
            statements = [self.statement()]
        then = CompoundBlock()
        then.children = statements
        node = WhileStatement(con,then)
        return node
    # loop无限循环语句
    def loop_statement(self):
        self.judg(TokenType.LOOP)
        if self.token._type == SymbolToken.LPARAN:
            self.judg(SymbolToken.LPARAN)
            statements = self.statement_list()
            self.judg(SymbolToken.RPARAN)
        else:
            statements = [self.statement()]
        then = CompoundBlock()
        then.children = statements
        node = WhileStatement(BoolConst(Token(TokenType.BOOL,"true")),then)
        return node
    # for循环与遍历语句
    def for_statement(self):
        self.judg(TokenType.FOR)
        var = self.variable()
        self.judg(TokenType.IN)
        iterobj = self.expr()
        if self.token._type == SymbolToken.LPARAN:
            self.judg(SymbolToken.LPARAN)
            statements = self.statement_list()
            self.judg(SymbolToken.RPARAN)
        else:
            statements = [self.statement()]
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
            if self.token._type == SymbolToken.ASSIGN:
                self.judg()
                dv = self.expr()
                num += 1
            else:dv = None
            params.append(ParamTerm(name1,tp,dv))
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
    # 调试语句
    def debugger_statement(self):
        self.judg(TokenType.DEBUGGER)
        return DebuggerStatement()
    # 导入模块
    def import_statement(self):
        self.judg(TokenType.IMPORT)
        modname = self.variable()
        return ImportStatement(modname)

    # 语句与程序
    # 获取单条语句
    def statement(self,is_change = 1):
        # print(self.token._type)
        if self.token._type in self.statements:
            node = getattr(self,self.token.value + "_statement")()
        elif self.token._type == TokenType.VARIABLE and is_change:
            pos = self.pos
            expr = self.expr()
            if self.token._type == SymbolToken.ASSIGN:
                self.pos = pos
                self.token = self.tokens[self.pos]
                node = self.change()
            else:
                self.pos = pos
                self.token = self.tokens[self.pos]
                node = self.statement(0)
        elif self.token._type == SymbolToken.LPARAN:
            node = self.newscope()
        elif self.token._type in (SymbolToken.ENDL,SymbolToken.LPARAN,SymbolToken.RPARAN,TokenType.END,TokenType.CASE,TokenType.DEFAULT):
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
        elif token._type == SymbolToken.LPARAN:
            node = self.get_map()
            return node
        elif token._type == TokenType.FUNC:
            node = self.func()
            return node
        elif token._type == SymbolToken.LINEDOWN:
            node = self.fn()
            return node
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
            "module":{},
            "map":{}
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

class BuiltinFunction(Symbol):
    def __init__(self,name,tp,params = None,returns = None):
        self.params = params
        self.name = name
        self.tp = tp
        self.returns = returns
        self.stype = BuiltinTypeSymbol("function")

class ScopeSymbolTable():
    def __init__(self,scopename = None,scopelv = None,enclosing = None):
        self.symbol = OrderedDict()
        self.name = scopename
        self.level = scopelv
        self.enclosing = enclosing
        self.builtintypes = [
            "int","real","bool","str","nulltype","array","function","module","map"
        ]
        self.builtinfunctions = {
            "println":[[("str")],"nulltype",1,1], # 参数类型,返回类型,参数个数下限,参数个数上线
            "inputln":[[("str")],"str",1,1],
            "print":[[("str")],"nulltype",1,1],
            "range":[[("int"),("int"),("int")],"array",1,3],
            "length":[[("str","array")],"int",1,1],
            "toint":[[("str","real","int")],"int",1,1],
            "tostr":[[("any")],"str",1,1],
            "toreal":[[("str","real")],"int",1,1],
            "tobool":[[("any")],"bool",1,1],
        }

    def init(self):
        for tp in self.builtintypes:
            self.define(BuiltinTypeSymbol(tp))
        for fn in self.builtinfunctions:
            self.define(BuiltinFunction(fn,fn))

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

    def visit_ScopeBlock(self,node):
        self.table = ScopeSymbolTable("scope",self.table.level + 1,self.table)
        self.table.symbol.update(self.table.enclosing.symbol)
        self.visit(node.block)
        self.table = self.table.enclosing

    def visit_AssignStatement(self,node):
        varname = node.left.name
        tpname = node.vartype.name
        if tpname == "auto":
            valuetp = self.visit(node.right)
            if valuetp != "function":
                varsymbol = VarSymbol(varname, self.table.query(valuetp))
                if valuetp == "array":
                    pass
                self.table.define(varsymbol)
            else:
                funsymbol = FunSymbol(varname,[])
                self.table.define(funsymbol)
        elif tpname == "function":
            if self.visit(node.right) == "function":
                try:
                    right = self.table.query(node.right.name)
                    if isinstance(right,BuiltinFunction):
                        fun = BuiltinFunction(varname,right.name)
                        self.table.define(fun)
                    else:
                        funsymbol = FunSymbol(varname,right.params)
                        funsymbol.blockast = right.blockast
                        funsymbol.returns = right.returns
                        funsymbol.defaultnum = right.defaultnum
                        self.table.define(funsymbol)
                except:
                    right = node.right
                    funsymbol = FunSymbol(varname,right.params)
                    funsymbol.blockast = right.block
                    funsymbol.returns = right.ret
                    self.table.define(funsymbol)
            else:
                self.error("类型错误")
        else:
            symbol = self.table.query(tpname)
            varsymbol = VarSymbol(varname,symbol)
            self.table.define(varsymbol)
            tp = self.visit(node.right)
            if symbol.name != tp:
                self.error(f"variable {varname}'s type define as {symbol.name} but assign as {tp}")

    def visit_ChangeStatement(self, node):
        left = node.left
        while True:
            try:
                name = left.name
                break
            except:
                left = left.left
        symbol = self.table.query(name)
        if symbol:
            if isinstance(symbol,ConstSymbol):
                self.error("不能修改常量")
            else:
                tp = self.visit(node.right)
                if symbol.stype.name != tp:
                    if not isinstance(node.left,IndexOperate):
                        self.error(f"variable {name}'s type define as {symbol.stype.name} but assign as {tp}")
                elif tp == "function":
                    right = self.table.query(node.right.name)
                    if isinstance(right,BuiltinFunction):
                        fun = BuiltinFunction(name,right.name)
                        self.table.define(fun)
                    else:
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
        if left in ("array","str","map"):
            for x in node.right:
                t = self.visit(x)
                if  t == "int" or t == "str":
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
                if isinstance(table,BuiltinFunction):
                    return self.table.builtinfunctions[table.name][1]
                defaultnum = table.defaultnum if table.defaultnum else 0
                greeting = table.params
                arg = node.right
                if len(greeting) <= len(arg) + defaultnum and len(greeting) >= len(arg):
                    for i in range(len(arg)):
                        if self.visit(arg[i]) == greeting[i].stype.name:
                            pass
                        else:
                            self.error("类型错误")
                    return table.returns
                else:
                    # self.error(f"function {funname} accept {len(greeting)} parameters but {len(arg)} were given")
                    pass
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

    def visit_CaseStatement(self,node):
        self.visit(node.con)
        self.visit(node.block)

    def visit_SwitchStatement(self,node):
        self.visit(node.var)
        for i in node.case:
            self.visit(i)
        self.visit(node.default)

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
            else:
                funsymbol.returns = node.returns
        elif ntp == None and node.returns == None:
            funsymbol.returns = "null"
        elif ntp == None and node.returns != None:
            self.error("类型错误")
        elif ntp != None and node.returns == None:
            funsymbol.returns = ntp
        self.table = self.table.enclosing
        funsymbol.blockast = node.block
        funsymbol.defaultnum = node.default

    def visit_ReturnStatement(self,node):
        return self.visit(node.value)

    def visit_EmptyStatement(self,node):pass
    visit_BreakStatement = visit_EmptyStatement
    visit_ContinueStatement = visit_EmptyStatement
    visit_DebuggerStatement = visit_EmptyStatement
    def visit_FuncConst(self,node):
        funtable = ScopeSymbolTable("func",self.table.level + 1,self.table)
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
        if ntp != None and node.ret != None:
            if ntp != node.returns.name:
                self.error("类型错误")
        elif ntp == None and node.ret == None:
            pass
        elif ntp == None and node.ret != None:
            self.error("类型错误")
        elif ntp != None and node.ret == None:
            pass
        self.table = self.table.enclosing
        return "function"
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
    def visit_MapConst(self,node):
        for i in node.value:
            self.visit(node.value[i])
        return "map"
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
class MapSym(Sym):
    def __init__(self,value):
        self.value = value
        self.str = str(value)
class FunctionSym(Sym):
    def __init__(self,block,enclosing):
        self.block = block
        self.params = {}
        self.str = "<function object>"
        self.enclosing = enclosing
class BuiltinfunSym(Sym):
    def __init__(self,name):
        self.name = name
        self.str = "<builtin function object>"
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
    elif isinstance(value,dict):
        return MapSym(value)

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
        self.closure = {}

    def __setitem__(self, key, value):
        self.members[key] = value

    def __getitem__(self, key):
        return self.members[key]

class Interpreter(Visitor):
    def __init__(self,tree,is_debug = 0):
        self.tree = tree
        self.is_debug = is_debug
        self.stack = CallStack()
        self.builtinfun = {
            "println":lambda a:print(*a),
            "inputln":lambda a:input(*a),
            "print":lambda a:print(*a,end = ""),
            "length":lambda a:len(*a),
            "toint":lambda a:int(*a),
            "tostr":lambda a:str(*a),
            "toreal":lambda a:float(*a),
            "tobool":lambda a:bool(*a),
            "range":lambda a:list(range(*a))
        }

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
        if isinstance(value,(FunctionSym,BuiltinfunSym)):return value
        if isinstance(left,dict):
            return value
        else:
            return VarSym(value)

    def visit_FuncallOperate(self,node):
        left = node.left
        symbol = self.visit(left)
        if isinstance(symbol,BuiltinfunSym):
            name = symbol.name
            fun = self.builtinfun[name]
            params = [self.visit(param).value for param in node.right]
            return VarSym(fun(params))
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
        ar.closure = symbol.enclosing
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

    def visit_FuncConst(self,node):
        ar = self.stack.peek()
        enclosing = ar.members
        fun = FunctionSym(node.block,enclosing)
        for param in node.params:
            pname = param.name.name
            dvalue = param.default
            fun.params[pname] = dvalue
        return fun

    def visit_AssignStatement(self,node):
        varname = node.left.name
        ar = self.stack.peek()
        varvalue = self.visit(node.right)
        ar[varname] = copy.deepcopy(varvalue)

    visit_ConstStatement = visit_AssignStatement

    ###这个方法轻易不要动###
    def visit_ChangeStatement(self,node):
        if isinstance(node.left,VarTerm):
            varname = node.left.name
            ar = self.stack.peek()
            if varname in ar.members:
                ar[varname] = copy.deepcopy(self.visit(node.right))
            elif varname in ar.closure:
                sym = self.visit(node.right)
                ar.closure[varname].value = sym.value
                ar.closure[varname].str = sym.str
            else:
                self.error("未定义的变量")
        elif isinstance(node.left,IndexOperate):
            l = node.left
            r = []
            while isinstance(l,IndexOperate):
                r.append(l.right)
                l = l.left
            r = r[::-1]
            if isinstance(l,VarTerm):
                name = l.name
                ar = self.stack.peek()
                if name in ar.members or name in ar.closure:
                    value = ar[name].value
                    valuelist = []
                    for i in r:
                        leng = len(i)
                        if leng == 1:
                            start = i[0].value
                            value = value[start]
                        elif leng == 2:
                            start = i[0].value
                            end = i[1].value
                            value = value[start:end]
                        elif leng == 3:
                            start = i[0].value
                            end = i[1].value
                            every = i[2].value
                            value = value[start:end:every]
                        valuelist.append(value)
                    r = r[::-1]
                    valuelist = valuelist[::-1]
                    valuelist[0] = self.visit(node.right).value
                    valuelist.append(ar[name].value)
                    for x in range(len(r)):
                        v = valuelist[x + 1]
                        i = r[x]
                        leng = len(i)
                        if leng == 1:
                            start = i[0].value
                            v[start] = valuelist[x]
                        elif leng == 2:
                            start = i[0].value
                            end = i[1].value
                            v[start:end] = valuelist[x]
                        elif leng == 3:
                            start = i[0].value
                            end = i[1].value
                            every = i[2].value
                            v[start:end:every] = valuelist[x]
                        valuelist[x+1] = v
                    if name in ar.members:
                        ar[name] = VarSym(valuelist[-1])
                    else:
                        sym = VarSym(valuelist[-1])
                        ar.closure[name].value = sym.value
                        ar.closure[name].str = sym.str
                else:
                    self.error("不存在的变量")

    def visit_VarTerm(self,node):
        varname = node.name
        index = 0
        while index < len(self.stack.stack):
            ar = self.stack.stack[index]
            if varname in ar.members:
                return ar[varname]
            elif varname in ar.closure:
                return ar.closure[varname]
            else:
                index = index + 1
        self.error(f"name '{varname}' is not defined")

    def visit_ProgramBlock(self,node):
        program_name = node.name
        ar = ActivationRecord(program_name,"main",1)
        self.stack.push(ar)
        for fn in self.builtinfun:
            self.stack.peek()[fn] = BuiltinfunSym(fn)
        self.visit(node.block)
        self.stack.pop()

    def visit_CompoundBlock(self,node):
        for child in node.children:
            ret = self.visit(child)
            if ret == BreakStatement:
                return BreakStatement
            if ret == ContinueStatement:
                return ContinueStatement
            if isinstance(ret,tuple):
                return ret[1]
        return None

    def visit_ScopeBlock(self,node):
        ar = self.stack.peek()
        newar = ActivationRecord("scope","scope",ar.level + 1)
        newar.members.update(ar.members)
        self.stack.push(newar)
        ret = self.visit(node.block)
        self.stack.pop()
        return ReturnStatement,ret

    def visit_IfStatement(self,node):
        if self.visit(node.condition).value:
            ret = self.visit(node.then)
            if ret == BreakStatement:
                return BreakStatement
            if ret == ContinueStatement:
                return ContinueStatement
            if isinstance(ret,tuple):return ReturnStatement,ret
        else:
            num = 0
            for i in node.elifnode:
                if self.visit(i.con).value:
                    ret = self.visit(i.root)
                    if ret == BreakStatement:
                        return BreakStatement
                    if ret == ContinueStatement:
                        return ContinueStatement
                    if isinstance(ret,tuple):return ReturnStatement,ret 
                    break
                else:
                    num += 1
            if num == len(node.elifnode): # 当所有的elif节点都不满足时
                ret = self.visit(node.elsenode)
                if ret == BreakStatement:
                    return BreakStatement
                if ret == ContinueStatement:
                    return ContinueStatement
                if isinstance(ret,tuple):return ReturnStatement,ret 

    def visit_WhileStatement(self,node):
        con = self.visit(node.condition).value
        while con:
            ret = self.visit(node.then)
            if ret == BreakStatement:
                break
            elif ret == ContinueStatement:
                con = self.visit(node.condition).value
                continue
            elif isinstance(ret,tuple):return ReturnStatement,ret 
            else:
                con = self.visit(node.condition).value

    def visit_SwitchStatement(self,node):
        var = self.visit(node.var).value
        num = 0
        for i in node.case:
            if var == self.visit(i.con).value:
                ret = self.visit(i.block)
                if ret == BreakStatement:
                    return BreakStatement
                if ret == ContinueStatement:
                    return ContinueStatement
                if isinstance(ret,tuple):return ReturnStatement,ret 
                break
            else:
                num += 1
        if num == len(node.case):
            ret = self.visit(node.default)
            if ret == BreakStatement:
                return BreakStatement
            if ret == ContinueStatement:
                return ContinueStatement
            if isinstance(ret,tuple):return ReturnStatement,ret 

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
            elif isinstance(ret,tuple):return ReturnStatement,ret

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
            return ReturnStatement,self.visit(node.value)

    def visit_BreakStatement(self,node):
        return BreakStatement

    def visit_ContinueStatement(self,node):
        return ContinueStatement

    def visit_ListConst(self,node):
        res = []
        for i in node.value:
            res.append(self.visit(i).value)
        return VarSym(res)

    def visit_MapConst(self,node):
        res = {}
        for i in node.value:
            res[i] = self.visit(node.value[i]).value
        return VarSym(res)

    def visit_DebuggerStatement(self,node):
        # if not self.is_debug:return
        ar = self.stack.peek()
        print("遇到debugger,终止程序")
        print("当前作用域符号表如下:")
        print("members:")
        for i in ar.members:
            print(i,":",ar.members[i].str)
        print("------------")
        if ar.closure:
            print("closure:")
            for i in ar.closure:
                print(i,":",ar.closure[i].str)
        input("回车继续运行程序:")

    def visit_EmptyStatement(self,node):
        pass

    def interpret(self):
        return self.visit(self.tree)

expr = """
println('
Dragonfly1.8
这次还是比预期差了很多功能，这是因为代码又需要重构了，不然会变成代码屎山，所以推了很多功能，但是会在2.0全部补上
1、增加switch-case结构
2、增加func声明函数字面量
3、使用{}声明一层新的作用域
4、闭包和函数一等公民
5、函数的缺省参数
6、列表的单个元素修改
上面的内容是在1.8pre中见过的内容，此处不再赘述，下面是1.8pre后新增的内容：
7、map类型的初步支持
只是初步支持，所以功能什么的比较差，但是2.0会补上的
let a = {
    name:"小明",
    do:func(){
        println("去上学")
    }
}
println(a["name"]) // 小明
a["do"]() // 去上学
这个还不能支持用xx.xx来访问的方法，里面的函数也不支持this，不过2.0会加的

8、内置函数的高级特性
把内置函数作为first-class，可以传递和赋值
let a = println
a("HelloWorld")
fun main(){
    return println
}
main()("HelloWorld")
增加了tobool和toreal两个内置函数

9、Rust-Style的匿名函数语法糖
这是个语法糖，但是挺好用的
let a = |num:int| num + 1
println(a(1)) // 2

let b = |num:int| -> int{
    return num + 1
}
println(b(1)) // 2
如果形如1，也就是不使用大括号的形式，返回值不需要return

10、if、while、for、loop等语句若为单语句,无需大括号
很好理解，来一个优美的例子：
// 求绝对值
let a = |num:int|{
    if num < 0 return -num
    else return num
}
println(a(-5)) // 5
这个语法糖还是非常优雅的

11、使用debugger关键字进行调试
在代码适当的地方加上debugger，可以优雅的调试程序，而无需到处println(1)来测试


因为有人说Dragonfly可读性和可写性不够好，那就来看看几个示例程序，到底好不好：
计数器:
fun Counter(original:int){
    return |value:int|{
        original = original + value
    }
}
let counter = Counter(0)
counter(1)
counter(2)

斐波那契数列（闭包实现）：
fun fibonacci(){
    let a = 0
    let b = 1
    return ||{
        let result = a
        a = b
        b = result + b
        return result
    }
}
let f = fibonacci()
for i in range(10){
    println(f())
}
总体就这些，2.0会添加更多功能

')
"""
# 词法分析
lexer = Lexer(expr)
tokens = lexer.tokens()
# 语法分析
parser = Parser(tokens)
tree = parser.program()
# 语义分析
builder = SemanticAnalyzer()
builder.visit(tree)
# 解释器
interpreter = Interpreter(tree,is_debug = 1)
interpreter.interpret()




"""
changelog:
7、内置函数的高级特性
8、map类型的初级支持
9、Rust-Style的匿名函数语法糖
10、使用debugger关键字进行调试
11、if、while、for、loop等语句若为单语句,无需大括号
"""