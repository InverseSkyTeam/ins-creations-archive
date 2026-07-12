import collections,sys
from enum import Enum


class Token:  # 定义记号类
    def __init__(self, type, value):  # 定义构造方法
        self.type  = type  # 记号中值的类型
        self.value = value  # 记号中的值

    def __str__(self):  # 重写查看记号内容的方法
        return 'Token({type},{value})'.format(type=self.type, value=self.value)

    def __repr__(self):  # 也可以写成 __repr__=__str__
        return self.__str__()

#运算符
PLUS, MINUS,MUL,DIV,MOD='PLUS', 'MINUS','MUL', 'DIV','MOD' #加法，减法，乘法、除法

#符号类
LPAREN,RPAREN,EOF = 'LPAREN', 'RPAREN','EOF' 
EQUAL,COLON,SEMI,ENDL,COMMA='EQUAL','COLON','SEMI','\n','COMMA'
POINT ='POINT'
LBigParen,RBigParen = 'LBigParen','RBigParen' #左右大括号
ARRPOINT = 'ARRPOINT' #'->'

#变、常量类
ID,VARTYPE = 'ID','VARTYPE'
VAR,CONST= 'VAR','CONST'

#类型类
INT,STR,NUMBER,FLOAT,BOOL= 'INT','STR','NUMBER','FLOAT','BOOL'
CHANGEABLE = 'CHANGEABLE'

#逻辑运算类
LessThan,MoreThan = 'LessThan','MoreThan' #<、>
LessThanEqual,MoreThanEqual  = 'LessThanEqual','MoreThanEqual'
AND,OR ,EQUALITY= 'AND','OR','EQUALITY' #'=='

#输入输出流
SRIN,RinSymbol = 'SRIN','RinSymbol'  
SOUT,OutSymbol = 'SOUT','OutSymbol' 

#语句类
IFNODE,WHILENODE='IFNODE','WHILENODE'
ELIFNODE,ELSENODE,ELSE = 'ELIFNODE','ELSENODE','ELSE'
FUNC,RETURN ='FUNC','RETURN'

#控制类
BREAK = 'BREAK'
CONTINUE = 'CONTINUE'

#自带函数
LEN = 'LEN'
TOSTR,TOINT,TOCHR,TOORD = 'TOSTR','TOINT','TOCHR','TOORD'






RESERVED_KEYWORDS = {  # 保留字字典
    'var': Token(VAR, 'var'),
    'const': Token(CONST, 'const'),
    'int': Token(VARTYPE, 'int'),
    'bool': Token(VARTYPE, 'bool'),
    'float' : Token(VARTYPE, 'float'),
    'str' : Token(VARTYPE, 'str'),
    'changeable' : Token(VARTYPE, 'changeable'),
    'Sout' : Token(SOUT, 'Sout'),
    'Srin' : Token(SRIN, 'Srin'),
    'ENDL' : Token(ENDL, '\n'),
    'if' : Token(IFNODE,'if'),
    'elif' : Token(ELIFNODE,'elif'),
    'else' : Token(ELSE,'else'),
    'while' : Token(WHILENODE,'while'),
    'def' : Token(FUNC,'def'),
    'len' : Token(LEN,'len'),
    'toint' : Token(TOINT,'toint'),
    'tostr' : Token(TOSTR,'tostr'),
    'toord' : Token(TOORD,'toord'),
    'tochr' : Token(TOCHR,'tochr'),
    'return' : Token(RETURN,'return')
}



#------词法分析器Lexer部分------
class Token:  # 定义记号类
    def __init__(self, type, value):  # 定义构造方法
        self.type  = type  # 记号中值的类型
        self.value = value  # 记号中的值

    def __str__(self):  # 重写查看记号内容的方法
        return 'Token({type},{value})'.format(type=self.type, value=self.value)

    def __repr__(self):  # 也可以写成 __repr__=__str__
        return self.__str__()

class Lexer():       #词法分析器
    def __init__(self, text):  # 定义构造方法获取用户输入的表达式
        self.text = text  # 用户输入的表达式
        self.position = 0  # 获取表达式中每一个字符时的位置
        self.current_char = self.text[self.position]  # 设置当前字符为指定位置的字符
        
    def error(self):  # 定义提示错误的方法
        raise Exception('警告：错误的输入内容！')  # 抛出异常

    def advance(self):  # 定义获取下一个字符的方法
        self.position += 1  # 获取字符的位置自增
        if self.position >= len(self.text):  # 如果位置到达字符串的末尾
            self.current_char = None  # 设置当前字符为None值
        else:  # 否则
            self.current_char = self.text[self.position]  # 设置当前字符为指定位置的字符
        
    def skip_whitespace(self):  # 定义跳过空格的方法
        while self.current_char is not None and self.current_char.isspace() :  # 如果当前字符不是None值并且当前字符是空格
            self.advance()  # 获取下一个字符
            
    def skip_comment(self):  # 添加跳过注释内容到的方法
        while self.current_char != '\n':  
            self.advance()  # 提取下一个字符
        self.advance()  # 提取下一个字符（跳过注释结束符号）
    
    def skip_longcomment(self):  # 添加跳过注释内容到的方法
        while True:
            if self.current_char == "*" and self.peek() == "/":
                self.advance()
                self.advance()
                break
            else:
                self.advance()
        
    def number(self):  # 获取多位数字
        result = ''
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):  # 如果当前字符不是None值并且当前字符是数字
            result += self.current_char  # 连接数字
            self.advance()  # 获取下一个字符
        if ('.' in result):
            return float(result)  # 返回浮点数
        else:
            return int(result)  # 返回整数
        
    def peek(self):
        pos = self.position + 1  # 获取下一个位置
        if pos >= len(self.text):  # 如果超出文本末端
            return None  # 返回None
        else:  # 否则
            return self.text[pos]  
    def last(self):
        pos = self.position - 1  
        if pos < 0:  
            return None 
        else:  # 否则
            return self.text[pos]  
            
    def var_id(self):  # 获取保留字或赋值名称记号的方法
        result = ''
        while self.current_char is not None and self.current_char.isalnum():  # 如果当前字符是字母数字
            result += self.current_char  # 连接字符
            self.advance()  # 提取下一个字符
        token = RESERVED_KEYWORDS.get(result, Token(ID, result))  # 如果是保留字返回保留字记号，默认返回ID记号
        return token 
    
    def string(self): # 获取字符串
        result = ''
        start = self.current_char
        while self.current_char is not None:
            result += self.current_char  # 连接字符串
            self.advance()  # 获取下一个字符
            if (self.current_char==start):#字符串结束
                break;
        self.advance()    # 跳过字符串结束符号"
        token=Token(STR,result[1:])
        return token
    
    
    def get_next_token(self):
        while self.current_char is not None:  # 如果当前字符不是None值
            if self.current_char == "\n":
                self.advance()  
                return Token(ENDL, "\n")  
            if self.current_char.isspace():  
                self.skip_whitespace()  
                continue
            if self.current_char == '/':
                if self.peek() == '/':  
                    self.skip_comment()  
                    continue
                if self.peek() == '*':  
                    self.skip_longcomment()  
                    continue
            if self.current_char.isdigit():  
                value = self.number()
                inttp = "<class 'int'>"
                floattp = "<class 'float'>"
                if str(type(value)) == inttp:
                    return Token(INT, value)  # 获取完整的数字创建记号对象并返回
                if str(type(value)) == floattp:
                    return Token(FLOAT, value)
            if self.current_char == '+':  
                self.advance()  
                return Token(PLUS, '+')  
            if self.current_char == '-': 
                if self.peek() == '>':  
                    self.advance() 
                    self.advance() 
                    return Token(ARRPOINT, '->')  
                else:
                    self.advance() 
                    return Token(MINUS, '-')  
            if self.current_char == '*':
                self.advance()  
                return Token(MUL, '*')  
            if self.current_char == '/':
                self.advance() 
                return Token(DIV, '/')  
            if self.current_char == '(':
                self.advance()  
                return Token(LPAREN, '(') 
            if self.current_char == ')':
                self.advance() 
                return Token(RPAREN, ')') 
            if self.current_char == '=':
                if self.peek() == "=":
                    self.advance()
                    self.advance()
                    return Token(EQUALITY,'==')
                else:
                    self.advance()
                    return Token(EQUAL,'=')
            if self.current_char == ':':  
                self.advance()  
                return Token(COLON, ':') 
            if self.current_char.isalnum() or self.current_char == "_":
                return self.var_id()
            if self.current_char == ';':  
                self.advance()  
                return Token(SEMI, ';')  
            
            if self.current_char=='\'' or self.current_char=='\"': 
                return self.string()  
            if self.current_char == '<':  
                if self.peek() == "=":
                    self.advance()
                    self.advance()
                    return Token(LessThanEqual, '<=') 
                elif self.peek() == '<':
                    self.advance()
                    self.advance()
                    return Token(OutSymbol, '<<')
                else:
                    self.advance()
                    return Token(LessThan, '<')  
            if self.current_char == '>':  
                if self.peek() == "=":
                    self.advance()
                    self.advance()
                    return Token(MoreThanEqual, '>=')
                elif self.peek() == ">":
                    self.advance()
                    self.advance()
                    return Token(RinSymbol, '>>') 
                else:
                    self.advance()
                    return Token(MoreThan, '>') 

            if self.current_char == ',':  
                self.advance()  
                return Token(COMMA, ',')  
            if self.current_char == '%':
                self.advance()  
                return Token(MOD, '%')  
            if self.current_char == '{':
                self.advance()  
                return Token(LBigParen, '{')  
            if self.current_char == '}':
                self.advance()  
                return Token(RBigParen, '}')  
            self.error()  # 如果以上都不是，则抛出异常。
        return Token(EOF, None)  # 遍历结束返回结束标识创建的记号对象







###############################################################################                                                                         #
#  PARSER   语法分析器                                                         #
###############################################################################

class AST(object):
    pass

# 程序类

class Program(AST):
    def __init__(self, name,compound):
        self.name = name
        self.compound = compound
    def __str__(self):
        return self.name
        
class Compound(AST):
    def __init__(self):
        self.children = []    
      
#数据类型类  
class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
        
class Float(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Bool(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
        
class STRING(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value        
#变量类

class Var(AST):  # 变量节点
    def __init__(self, token):
        self.token = token  
        self.name= token.value  # 变量名称
        
class VarType(AST):
    def __init__(self,vartype):
        self.vartype = vartype
        self.name = vartype.value  
        
#运算类
class BinOp(AST):
      def __init__(self,left,op,right):
          self.left=left
          self.token = self.op = op
          self.right = right

class UnaryOp(AST):#一颗正负号数
    def __init__(self,op,expr):
        self.token = self.op = op
        self.expr = expr
        
        
       
#语句类        
class Assign(AST):  # 添加赋值语句节点
    def __init__(self, left, operate, right,vartype):
        self.left = left  # 变量名称
        self.token = operate
        self.operate = operate  # 记号和赋值符号
        self.right = right  # 右侧表达式
        self.vartype = vartype

class ManyAssign(AST):
    def __init__(self):
        self.children = []    

class Const(AST):  
    def __init__(self, left, operate, right,vartype):
        self.left = left  # 变量名称
        self.token = operate
        self.operate = operate 
        self.right = right  # 右侧表达式
        self.vartype = vartype

class Change(AST):
    def __init__(self,left,operate,right):
        self.left = left
        self.operate = operate
        self.right = right

class Sout(AST):  # 屏幕打印节点
    def __init__(self, params):
        self.params =params 

class Srin(AST):  # 屏幕打印节点
    def __init__(self, params):
        self.params =params 

#分支

class IF(AST):  # 添加条件控制语句节点
    def __init__(self, condition, then_node , else_node):#,elif_nodelist,else_node
        self.condition = condition  
        self.then_node = then_node 
        #self.elif_nodelist = elif_nodelist
        self.else_node = else_node
        
class Elif(AST):
    def __init__(self, condition, then_node):
        self.condition = condition  # 条件
        self.then_node = then_node  # then节点

      
class While(AST):  # 添加条件控制语句节点
    def __init__(self, condition, then_node):
        self.condition = condition  # 条件
        self.then_node = then_node  # then节点
# 函数

class Return(AST):
    def __init__(self, value):
        self.value = value
  
class Param(AST):
    def __init__(self, name,types):
        self.name = name
        self.types = types

class FuncNode(AST):
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
        
class Return(AST):
    def __init__(self,value):
        self.value = value
#控制语句

class Break(AST):
    def __init__(self):
        pass

class Continue(AST):
    def __init__(self):
        pass

# 自带函数

class Len(AST):
    def __init__(self,string):
        self.string=string
        
class Toint(AST):
    def __init__(self,string):
        self.string=string
        
class Tostr(AST):
    def __init__(self,inter):
        self.inter=inter

class Toord(AST):
    def __init__(self,char):
        self.char=char

class Tochr(AST):
    def __init__(self,inter):
        self.inter=inter

class Len(AST):
    def __init__(self,string):
        self.string=string

class NoOp(AST):  # 空语句节点
    pass       


INIT_VARTYPE = {
    'int': Num(Token(INT, 0)),
    'str': STRING(Token(STR, "")),
    'float': Float(Token(FLOAT, 0.0)) ,
    'bool': Bool(Token(BOOL,False)),
    'changeable': Num(Token(CHANGEABLE,0)),
}





class Parser:  #语法分析器
    def __init__(self, lexer):  # 定义构造方法获取用户输入的表达式
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token() # 语法分析器初始化

    def eat(self,token_type):
        if (self.current_token.type==token_type):
            self.current_token = self.lexer.get_next_token()
        else:  # 否则
            self.lexer.error()  # 抛出异常

    def factor(self):          #语法分析器最底层结构：整数或括号
        token = self.current_token  # 获取记号
        if (token.type == PLUS or token.type == MINUS):
            self.eat(token.type)
            node=UnaryOp(token,self.factor())
            return node
        if (token.type == INT):   # 整数
            self.eat(INT)
            return Num(token)  # 返回数字节点对象
        if token.type ==FLOAT:
            self.eat(FLOAT)
            return Float(token)
        elif (token.type == LPAREN):  # 左括号
            self.eat(LPAREN)
            node = self.expr()              # 求出括号里面的AST树
            self.eat(RPAREN)                # 右括号
            return node  
        elif token.type == ID and self.lexer.current_char == "(":
            node = self.funcall()
            return node
        elif token.type == TOSTR:
            node = self.tostr()
            return node
        elif token.type == TOINT:
            node = self.toint()
            return node
        elif token.type == TOCHR:
            node = self.tochr()
            return node
        elif token.type == TOORD:
            node = self.toord()
            return node
        elif token.type == LEN:
            node = self.lens()
            return node
        elif (token.type == STR):   # 字符串
            self.eat(STR)
            return STRING(token)
        
        else:  # 新增变量因子
            node = self.variable()  # 获取变量节点
            return node  # 返回变量节点

    def term(self):           #语法分析器中间层结构：乘除
        node=self.factor()    # 获取第一个数字树,如没有乘除法，将直接返回一个代表数字的叶节点树
        while (self.current_token.type in (MUL,DIV,MOD)):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            if token.type == DIV:
                self.eat(DIV)
            if token.type == MOD:
                self.eat(MOD)
            # 生成新的树：把目前已经获取到的乘除法树整体做为左子树，起到连续乘除的作用
            node = BinOp(left=node, op=token, right=self.factor())
            # 新的树以取得新的数字或括号内的树为右子树
        return node

    def expr(self):          #语法分析器最高层结构：加减
        node=self.term()     # 获取第一段乘除
        while (self.current_token.type in (PLUS,MINUS,EQUALITY,LessThanEqual,MoreThanEqual,LessThan,MoreThan)):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            if token.type == MINUS:
                self.eat(MINUS)
            if token.type == EQUALITY:
                self.eat(EQUALITY)
            if token.type == LessThan:
                self.eat(LessThan)
            if token.type == MoreThan:
                self.eat(MoreThan)
            if token.type == LessThanEqual:
                self.eat(LessThanEqual)
            if token.type == MoreThanEqual:
                self.eat(MoreThanEqual)

            # 生成新的树：把目前已经获取到的加减法树整体做为左子树，起到连续加减的作用
            node = BinOp(left=node, op=token, right=self.term())
            # 新的树以取得新的数字或括号内的树为右子树
        return node
    
    

    def var(self):
        self.eat(VAR)
        return self.assignment()
    
    def const(self):
        self.eat(CONST)
        return self.constment()
    
    def vartype(self):
        node = VarType(self.current_token)
        self.eat(VARTYPE)
        return node
        
    def variable(self):  # 添加获取变量节点的方法
        node = Var(self.current_token)  # 获取变量节点
        self.eat(ID)  # 验证变量名称
        return node  # 返回变量节点
        
    def empty(self):  # 添加获取空语句节点的方法
        return NoOp()  # 返回空语句节点

    def assignment(self):  # 添加获取赋值语句节点的方法
        leftlist=[]
        rightlist=[]
        leftlist.append(self.variable())  # 获取变量名称节点
        while self.current_token.type == COMMA :
            self.eat(COMMA)
            leftlist.append(self.variable())
        token = self.current_token  # 获取当前记号
        self.eat(COLON)  # 验证：
        vartype = self.vartype()   #验证类型
        
        pos = self.lexer.position
        if self.current_token.type ==EQUAL:
            self.eat(EQUAL)  # 验证赋值符
            rightlist.append(self.expr()) # 获取表达式节点
            while self.current_token.type == COMMA :
                self.eat(COMMA)
                rightlist.append(self.expr())
        else:
            self.lexer.position = pos
            for i in range(len(leftlist)):
                rightlist.append(INIT_VARTYPE[vartype.name])
        
        assigns=[]
        
        if len(leftlist) != len(rightlist):
            KeyError("对应的变量的值缺失")
        else:
            for i in range(len(leftlist)):
                assigns.append(Assign(leftlist[i], token, rightlist[i],vartype))
                
        node = ManyAssign() 
        node.children=assigns
        return node  # 返回赋值语句节点
    
    def constment(self):  # 添加获取赋值语句节点的方法
        left = self.variable()  # 获取变量名称节点
        token = self.current_token  # 获取当前记号
        self.eat(COLON)  # 验证：
        vartype = self.vartype()   #验证类型
        token = self.current_token  # 
        self.eat(EQUAL)  # 验证赋值符
        right = self.expr()  # 获取表达式节点
        node = Const(left, token, right,vartype)  # 组成赋值语句节点
        return node  # 返回赋值语句节点
    
    
    def change(self):
        left = self.variable()
        token = self.current_token
        self.eat(EQUAL)
        right = self.expr()
        node = Change(left,token,right)
        return node
    
    def if_statement(self): 
        self.eat(IFNODE)  
        con = self.expr() 
        self.eat(LBigParen)  
        then_nodes = self.statement_list()  
        then_root = Compound()  # 创建复合语句节点对象
        then_root.children = then_nodes  # 将语句节点列表添作为复合语句节点的子节点列表
        self.eat(RBigParen)
        else_root = Compound()  # 创建复合语句节点对
        else_root.children = []
        pos = self.lexer.position
        if self.current_token.type == ELSE:
            self.eat(ELSE)  # 验证ELSE
            self.eat(LBigParen)  
            else_nodes = self.statement_list()  # 获取ELSE后面的分支块节点
            else_root.children = else_nodes  # 将语句节点列表添作为复合语句节点的子节点列表
            self.eat(RBigParen)
        else:
            self.lexer.position = pos
        node=IF(con,then_root,else_root)
        return node
    
    def while_statement(self): 
        self.eat(WHILENODE)  
        con = self.expr() 
        self.eat(LBigParen)  
        then_nodes = self.statement_list()  
        then_root = Compound()  # 创建复合语句节点对象
        then_root.children = then_nodes  # 将语句节点列表添作为复合语句节点的子节点列表
        self.eat(RBigParen) 
        node=While(con,then_root)
        return node  
      
    def Sout(self):  # 屏幕打印节点的方法
        self.eat(SOUT)  
        self.eat(OutSymbol)  
        params=[self.expr()]        
        while (self.current_token.type != SEMI):  
            self.eat(OutSymbol)  
            params.append(self.expr())  

        node=Sout(params=params)
        return node 
    
    def Srin(self):  # 屏幕打印节点的方法
        self.eat(SRIN)  
        self.eat(RinSymbol)
        params=[self.variable()]        
        while (self.current_token.type != SEMI):  
            self.eat(RinSymbol)
            params.append(self.variable())   
        node=Srin(params=params)
        return node  # 返回屏幕打印节点 
        
    def params_list(self):
        if self.current_token.type != ID:
            return []
        params = []
        name1 = self.variable()
        self.eat(COLON)
        tp = self.vartype()
        params.append(Param(name1,tp))
        while self.current_token.type != RPAREN:
            self.eat(COMMA)
            name = self.variable()
            self.eat(COLON)
            tp = self.vartype()
            params.append(Param(name,tp))
        return params
        
    def func_statement(self):

        self.eat(FUNC)
        funcname = self.current_token.value
        self.eat(ID)
        self.eat(LPAREN)
        params = self.params_list()  # 获取参数列表
        self.eat(RPAREN) 

        returntype = None
        if self.current_token.type == ARRPOINT:
            self.eat(ARRPOINT)
            returntype = self.vartype()
            
        self.eat(LBigParen)
        slist = self.statement_list()
        self.eat(RBigParen)
        
        compound = Compound()
        compound.children = slist
        
        node = FuncNode(funcname,params,compound,returntype)
        return node
    
    def funcall(self):
        token = self.current_token
        funname = self.current_token.value
        self.eat(ID)
        self.eat(LPAREN)
        params = []
        if self.current_token.type != RPAREN:
            node = self.expr()
            params.append(node)
        while self.current_token.type == COMMA:
            self.eat(COMMA)
            node = self.expr()
            params.append(node)
        self.eat(RPAREN)
        node = FunCall(funname,params,token)
        return node
    
    def return_statement(self):
        self.eat(RETURN)
        value = self.expr()
        node = Return(value)
        return node
        
    def tochr(self):
        self.eat(TOCHR)
        self.eat(LPAREN)
        inter = self.expr()
        self.eat(RPAREN)
        node = Tochr(inter)
        return node
    
    def toord(self):
        self.eat(TOORD)
        self.eat(LPAREN)
        char = self.expr()
        self.eat(RPAREN)
        node = Toord(char)
        return node
    
    def toint(self):
        self.eat(TOINT)
        self.eat(LPAREN)
        s = self.expr()
        self.eat(RPAREN)
        node = Toint(s)
        return node
    
    def tostr(self):
        self.eat(TOSTR)
        self.eat(LPAREN)
        inter = self.expr()
        self.eat(RPAREN)
        node = Tostr(inter)
        return node
    
    def lens(self):
        self.eat(LEN)
        self.eat(LPAREN)
        string = self.expr()
        self.eat(RPAREN)
        node = Len(string)
        return node
        
    def statement(self):

        if self.current_token.type == VAR:
            node = self.var()
        elif self.current_token.type == ID:
            if self.lexer.current_char == "(":
                node = self.funcall()
            else:
                node = self.change()
        elif self.current_token.type == CONST:
            node = self.const()
        elif self.current_token.type == SOUT:
            node = self.Sout()
        elif self.current_token.type == SRIN:
            node = self.Srin()
        elif self.current_token.type == IFNODE:
            node = self.if_statement()
        elif self.current_token.type == WHILENODE:
            node = self.while_statement()
        elif self.current_token.type == FUNC:#定义函数
            node = self.func_statement()
        elif self.current_token.type == RETURN:
            node = self.return_statement()
        elif self.current_token.type == TOINT:
            node = self.toint()
        elif self.current_token.type == TOSTR:
            node = self.tostr()
        elif self.current_token.type == TOINT:
            node = self.toord()
        elif self.current_token.type == TOINT:
            node = self.tochr()
        else:
            node = self.empty()
        
        return node

    def statement_list(self):
        node = self.statement()
        nodelist = [node]

        while self.current_token.type in (SEMI,ENDL) :
            if self.current_token.type == SEMI:
                self.eat(SEMI)
            elif self.current_token.type == ENDL:
                self.eat(ENDL)
            nodelist.append(self.statement())
 
        return nodelist

    def program(self):
        nodelist = self.statement_list()
        root = Compound()
        root.children = nodelist
        return root
    
    def parse(self,name):
        node = Program(name,self.program())
        return node  # 返回程序节点




###############################################################################
#  INTERPRETER    解释器
###############################################################################

class NodeVisitor(object):
    def visit(self, node):
        # 获取节点类型名称组成访问器方法名（子类Interpreter中方法的名称）
        method_name = 'visit_' + type(node).__name__
        # 获取访问器对象，找不到访问器时获取“generic_visit”
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))
        
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

class ProcedureSymbol(Symbol):  # 添加过程符号类
    def __init__(self, name, params=None):  # 过程包含名称与形式参数信息
        super().__init__(name)
        self.params = params if params is not None else []  # 获取形式参数，如果未传入则为空列表。

    def __str__(self):
        return f"<{self.__class__.__name__}(name='{self.name}',parameters={self.params})>"  # 过程的信息

    __repr__ = __str__
    
class FunSymbol(Symbol):
    def __init__(self,name,params = None):
        super().__init__(name)
        if params is None:
            self.params = []
        else:
            self.params = params
        self.blockast = None
        self.returns = None
        
class ScopedSymbolTable():
    def __init__(self,scope_name, scope_level,enclosing_scope=None):#
        self.symbol = collections.OrderedDict()
        self.scope_name = scope_name  # 添加作用域名称
        self.scope_level = scope_level  # 添加作用域级别
        self.enclosing_scope = enclosing_scope  # 添加外围作用域
        self.init()

    def init(self):
        self.define(BuiltinSymbol("int"))
        self.define(BuiltinSymbol("float"))
        self.define(BuiltinSymbol("bool"))
        self.define(BuiltinSymbol("string"))
        self.define(BuiltinSymbol("endl"))
        self.define(BuiltinSymbol("true"))
        self.define(BuiltinSymbol("false"))
        self.define(BuiltinSymbol("endl"))
    
    def __str__(self):
        scope_header = '作用域符号表：'
        lines = ['\n', scope_header, '=' * len(scope_header) * 2]
        for header_name, header_value in (
                ('作用域名称', self.scope_name),
                ('作用域级别', self.scope_level),
                ('外围作用域', self.enclosing_scope.scope_name if self.enclosing_scope else None)  # 如果不存在外围作用域则为None
        ):  # 遍历作用域名称和级别以及外围作用域
            lines.append(f'{header_name:15}:{header_value}')
        symtab_header = '符号表中的内容：'
        lines.extend(['\n', symtab_header, '-' * len(symtab_header) * 2])
        lines.extend([f'{key:8}: {value}' for key, value in self._symbols.items()])
        s = '\n'.join(lines)
        return s

    __repr__ = __str__

    
    def define(self,symbol):
        self.symbol[symbol.name] = symbol

    def query(self,name):
        #print(f'查询：{name}(作用域：{self.scope_name})')
        symbol = self.symbol.get(name)  # 在当前作用域查找符号
        if symbol:  
            return symbol 
        if self.enclosing_scope:  # 如果当前作用域没有找到符号并且存在外围作用域
            return self.enclosing_scope.query(name)  # 递归方式在外围作用域进行查找

class SemanticAnalyzer(NodeVisitor):
    def __init__(self):
        self.current_scope = None

    def visit_Compound(self,node):
        for child in node.children:
            self.visit(child)
        
        
    def visit_ManyAssign(self,node):
        for child in node.children:
            self.visit(child)
    
    def visit_Assign(self,node):
        varname = node.left.name
        tpname = node.vartype.name
        symbol = self.current_scope.query(tpname)
        varsymbol = VarSymbol(varname,symbol)
        self.current_scope.define(varsymbol)
        
    
    def visit_Const(self,node):
        varname = node.left.name
        tpname = node.vartype.name
        symbol = self.current_scope.query(tpname)
        varsymbol = VarSymbol(varname,symbol)
        self.current_scope.define(varsymbol)

    def visit_Change(self, node):
        name = node.left.name
        symbol = self.current_scope.query(name)
        if symbol:
            self.visit(node.right)
        else:
            raise NameError("未定义的变量值")
    
    def visit_FuncNode(self,node):
        funsymbol = FunSymbol(node.name)
        self.current_scope.define(funsymbol)
        funtable = ScopedSymbolTable(node.name,self.current_scope.scope_level + 1,self.current_scope)
        self.current_scope = funtable
        for param in node.params:
            ptype = self.current_scope.query(param.types.name)
            pname = param.name.name
            symbol = VarSymbol(pname,ptype)
            self.current_scope.define(symbol)
            funsymbol.params.append(symbol)
        self.visit(node.block)
        self.current_scope = self.current_scope.enclosing_scope
        funsymbol.blockast = node.block

    def visit_FunCall(self,node):
        funname = node.name
        table = self.current_scope.query(funname)
        greeting = table.params
        arg = node.params
        if len(greeting) == len(arg):
            for param in node.params:
                self.visit(param)
        else:
            self.error(f"function {funname} accept {len(greeting)} parameters but {len(arg)} were given")
        symbol = self.current_scope.query(funname)
        node.symbol = symbol
    
    def visit_Return(self,node):
        self.visit(node.value)
        
    def visit_Var(self,node):
        name = node.name
        symbol = self.current_scope.query(name)
        if not symbol:
            raise NameError(f'引用了不存在的标识符：{repr(var_name)}')  # 抛出语义错误

    def visit_UnaryOp(self, node):
        self.visit(node.expr)

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)
    
    def visit_Sout(self, node):
        for node in node.params:
            self.visit(node)
    
    def visit_Srin(self, node):
        for node in node.params:
            self.visit(node)
    
    def visit_IF(self,node):
        self.visit(node.condition)
        self.visit(node.then_node)
        self.visit(node.else_node)
    
    def visit_While(self,node):
        self.visit(node.condition)
        self.visit(node.then_node)
    
    def visit_Return(self,node):
        return self.visit(node.value)
        
    def visit_Toint(self,node):
        self.visit(node.string)
    
    def visit_Tostr(self,node):
        self.visit(node.inter)
    
    def visit_Toord(self,node):
        self.visit(node.char)
    
    def visit_Tochr(self,node):
        self.visit(node.inter)
    
    def visit_Len(self,node):
        self.visit(node.string)
    
    def visit_STRING(self,node):
        pass

    def visit_Num(self,node):
        pass
    
    def visit_Float(self,node):
        pass

    def visit_Bool(self,node):
        pass

    def visit_NoOp(self, node):  
        pass  
    
    def visit_Program(self, node):  
        print('>>> 进入作用域：global')
        global_scope = ScopedSymbolTable(scope_name='global', scope_level=1,
                                         enclosing_scope=self.current_scope)  # 创建全局作用域符号表
        global_scope.init()  
        self.current_scope = global_scope
        self.visit(node.compound)  
        self.current_scope = self.current_scope.enclosing_scope  # 离开作用域时设置当前作用域为外围作用域
        print('<<< 离开作用域：global')


class ARType(Enum):
    PROGRAM   = 'PROGRAM'
    
class CallStack:
    def __init__(self):
        self._records = []

    def push(self, ar):
        self._records.append(ar)

    def pop(self):
        return self._records.pop()

    def peek(self):
        if len(self._records)-1>=0:
            return self._records[len(self._records)-1]
        else:
            return None
    def __str__(self):
        s = '\n'.join(repr(ar) for ar in reversed(self._records))
        s = f'CALL STACK\n{s}\n'
        return s

    def __repr__(self):
        return self.__str__()

class ActivationRecord:
    def __init__(self, name, type, nesting_level):
        self.name = name
        self.type = type
        self.nesting_level = nesting_level
        self.members = {
            'endl' : '\n',
            'true' : True,
            'false' : False,
        }
        self.types = {
            'endl' : 'str',
            'true' : 'bool',
            'false' : 'bool'
        }
        self.isconst = {
            'endl' : True,
            'true' : True,
            'false' : True,
        }

    def __setitem__(self, key, value):
        self.members[key] = value

    def __getitem__(self, key):
        return self.members[key]

    def get(self, key):
        return self.members.get(key)

    def __str__(self):
        lines = [
            '{level}: {type} {name}'.format(
                level=self.nesting_level,
                type=self.type,
                name=self.name,
            )
        ]
        for name, val in self.members.items():
            lines.append(f'   {name:<20}: {val}')

        s = '\n'.join(lines)
        return s

    def __repr__(self):
        return self.__str__()

class Interpreter(NodeVisitor):
    
    '''
    GLOBAL_SCOPE = {'endl' : '\n','true' : True,'false' : False,}  
    VAR_RALATION_TYPE = {'endl' : 'str','true' : 'bool','false' : 'bool',}
    IS_CONST = {'endl' : True,'true' : True,'false' : True,}
    '''
    
    def __init__(self, tree):  # 定义构造方法获取用户输入的表达式
        self.tree = tree
        self.stack = CallStack()
        
    def visit_BinOp(self, node):  # 访问二元运算符类型节点的方法
        left = self.visit(node.left)
        right = self.visit(node.right)
        if node.op.type == PLUS:  # 如果操作符类型是加法
            return left + right 
        elif node.op.type == MINUS:
            return left - right 
        elif node.op.type == MUL:
            return left * right 
        elif node.op.type == DIV:
            return left // right 
        elif node.op.type == EQUALITY:  
            return bool(left == right ) 
        elif node.op.type == LessThan:  
            return bool(left < right )
        elif node.op.type == MoreThan:  
            return bool(left > right )
        elif node.op.type == LessThanEqual:  
            return bool(left <= right )
        elif node.op.type == MoreThanEqual:  
            return bool(left >= right )
    def visit_Num(self, node):  # 访问数字类型节点的方法
        return node.value

    def visit_UnaryOp(self, node):
        op = node.op.type
        if op == PLUS:
            return +self.visit(node.expr)
        elif op == MINUS:
            return -self.visit(node.expr)
            
    def visit_Assign(self, node):  # 访问赋值语句节点
        var_name = node.left.name  # 获取变量名称
        var_type = node.vartype.name
        value = self.visit(node.right)
        tp = f"<class '{var_type}'>"
        if str(type(value)) == tp or var_type == 'changeable':
            ar = self.stack.peek()  #获取调用栈的栈顶
            ar.types[var_name] = var_type
            ar.isconst[var_name] = False
            ar[var_name] = value
        else:
            raise ValueError("Type of the variable changed 变量的类型发生了改变")
    
    def visit_ManyAssign(self,node):
        for child in node.children:
            self.visit(child)
    
    def visit_Const(self, node):  
        var_name = node.left.name  
        var_type = node.vartype.name
        value = self.visit(node.right)
        tp = f"<class '{var_type}'>"
        if str(type(value)) == tp:
            ar = self.stack.peek()  #获取调用栈的栈顶
            ar.types[var_name] = var_type
            ar.isconst[var_name] = True 
            ar[var_name] = value
        else:
            raise ValueError("Type of the const variable changed 常量的类型发生了改变")
    
    def visit_Change(self,node):
        ar = self.stack.peek()
        varname = node.left.name
        if varname in ar.members:
            value = self.visit(node.right)
            vartype = ar.types[varname]
            tp = f"<class '{vartype}'>"
            if ar.isconst[varname] == True:
                raise ValueError("Consted variable can't be changed 常量发生了改变")
            elif str(type(value)) == tp or vartype=='changeable':
                ar[varname] = value
            else:
                raise ValueError("类型发生改变")
        else:
            raise ValueError("变量不存在")
        
    def visit_Variable(self, node):  # 访问变量节点
        var_name = node.name  # 获取变量名称
        ar = self.stack.peek()  #获取调用栈的栈顶
        var_value = ar.get(var_name)
        value = self.GLOBAL_SCOPE.get(var_name)  # 获取变量值
        if var_value is None:  # 变量不存在
            raise NameError(f'错误的标识符：{repr(var_name)}')  # 抛出异常
        else:  # 否则
            return var_value  # 返回变量值
    
    def visit_Compound(self,node):
        for child in node.children:
            if type(child).__name__ == "Return":
                ret = self.visit(child)
                return ret
            self.visit(child)
        return None
        
    def visit_STRING(self,node):
        return node.value
        
    def visit_Float(self,node):
        return node.value
    
    def visit_Bool(self,node):
        return node.value
      
    def visit_Var(self,node):
        ar = self.stack.peek()  #获取调用栈的栈顶
        varname = node.name
        if varname in ar.members:
            value = ar[varname]
            return value
        else:
            raise NameError("不存在的变量值")

    def visit_IF(self,node):
        Is_vis=False
        con=self.visit(node.condition)   #判断条件节点的值
        if con:                #条件成立,则以then节点为准
            self.visit(node.then_node)
            Is_vis=True
        else:
            self.visit(node.else_node)
        
    def visit_While(self,node):
       
        while self.visit(node.condition):           
            self.visit(node.then_node)
    
    def visit_NoOp(self, node):  # 访问空语句节点
        pass  # 无操作
    
    def visit_Sout(self,node):
        for node in node.params:
            print(self.visit(node),end='')
    
    def visit_Toint(self,node):
        return int(self.visit(node.string))
    
    def visit_Tostr(self,node):
        return str(self.visit(node.inter))
    
    def visit_Toord(self,node):
        return ord(self.visit(node.char))
    
    def visit_Tochr(self,node):
        return chr(self.visit(node.inter))
    
    def visit_Len(self,node):
        return len(self.visit(node.string))
    
    def visit_Srin(self,node):
        ar = self.stack.peek()
        vallist =  sys.stdin.readline().split(' ')
        i=0
        for node in node.params:
            val =vallist[i]
            name = node.name
            if ar.types[name] == 'int':
                valnode = Num(Token(INT,int(val)))
            elif ar.types[name] == 'float':
                valnode = Float(Token(FLOAT,float(val)))
            elif ar.types[name] == 'bool':
                valnode = Bool(Token(BOOL,bool(val)))
            elif ar.types[name] == 'str':
                valnode = STRING(Token(STR,val))
            else:
                valnode = STRING(Token(STR,val))
            i+=1
            self.visit(Change(node,Token(EQUAL,'='),valnode))
    
    def visit_FuncNode(self,node):
        pass
    
    def visit_FunCall(self,node):
        funname = node.name
        node.symbol = FunSymbol(node.name)
        #这上面那行不加会报错，我也不知道对不对，而且必须加一个visit_NoneType?我也不知道为啥
        print("node.symbol",node.symbol)
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
        if ar.nesting_level <= 0:
            print ("can not return from main")
            raise(ValueError)
        else:
            return self.visit(node.value)
    
    
    def visit_Program(self, node):  # abs()

        program_name = node.name
        print(f'ENTER: PROGRAM {program_name}')
        
        ar = ActivationRecord(
            name=program_name,
            type = ARType.PROGRAM,
            nesting_level=1,
        )
        self.stack.push(ar) # 当前活动记录入栈
        self.visit(node.compound)  # 访问语句块
        #print(str(self.stack))
        print(f'LEAVE: PROGRAM {program_name}') #离开当前活动记录
        self.stack.pop()   #当前活动记录出栈
        #print(str(self.stack))
        
    def visit_NoneType(self,node):
        pass
        
    def interpret(self):  # 执行解释的方法
        self.visit(self.tree)
        
def main():
    with open("Code.txt","r") as f:
        text = f.read() 
    lexer = Lexer(text)
    parser = Parser(lexer)
    tree = parser.parse('Code.sail')
    
    builder = SemanticAnalyzer()
    builder.visit(tree)
    
    interpreter = Interpreter(tree)
    interpreter.interpret()
    
    


if __name__ == '__main__':
    main()
