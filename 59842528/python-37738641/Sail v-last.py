import collections



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
LPAREN,RPAREN,EOF = 'LPAREN', 'RPAREN','EOF' #左括号,右括号,结束标识
EQUAL,COLON,SEMI,ENDL,COMMA='EQUAL','COLON','SEMI','\n','COMMA'
POINT ='POINT'
LBigParen,RBigParen = 'LBigParen','RBigParen' #左右大括号

#变、常量类
ID,VARTYPE = 'ID','VARTYPE'
VAR,CONST= 'VAR','CONST'

#类型类
INT,STR,NUMBER,FLOAT,BOOL= 'INT','STR','NUMBER','FLOAT','BOOL'

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

RESERVED_KEYWORDS = {  # 保留字字典
    'var': Token(VAR, 'var'),
    'const': Token(CONST, 'const'),
    'int': Token(VARTYPE, 'int'),
    'bool': Token(VARTYPE, 'bool'),
    'float' : Token(VARTYPE, 'float'),
    'str' : Token(VARTYPE, 'str'),
    'Sout' : Token(SOUT, 'Sout'),
    'Srin' : Token(SRIN, 'Srin'),
    'ENDL' : Token(ENDL, '\n'),
    'if' : Token(IFNODE,'if'),
    'elif' : Token(ELIFNODE,'elif'),
    'else' : Token(ELSE,'else'),
    'while' : Token(WHILENODE,'while')
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


class Num(AST):#一个数
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
        
class BinOp(AST):#一颗算数树
      def __init__(self,left,op,right):
          self.left=left
          self.token = self.op = op
          self.right = right

class UnaryOp(AST):#一颗正负号数
    def __init__(self,op,expr):
        self.token = self.op = op
        self.expr = expr
        
class Assign(AST):  # 添加赋值语句节点
    def __init__(self, left, operate, right,vartype):
        self.left = left  # 变量名称
        self.token = operate
        self.operate = operate  # 记号和赋值符号
        self.right = right  # 右侧表达式
        self.vartype = vartype

class Const(AST):  # 添加赋值语句节点
    def __init__(self, left, operate, right,vartype):
        self.left = left  # 变量名称
        self.token = operate
        self.operate = operate  # 记号和赋值符号
        self.right = right  # 右侧表达式
        self.vartype = vartype
        
class Var(AST):  # 添加变量节点
    def __init__(self, token):
        self.token = token  # 记号
        self.name= token.value  # 变量名称

class Change(AST):
    def __init__(self,left,operate,right):
        self.left = left
        self.operate = operate
        self.right = right

class VarType(AST):
    def __init__(self,vartype):
        self.vartype = vartype
        self.name = vartype.value 
        
class NoOp(AST):  # 添加空语句节点
    pass  # 无内容

class STRING(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Sout(AST):  # 屏幕打印节点
    def __init__(self, params):
        self.params =params 

class Srin(AST):  # 屏幕打印节点
    def __init__(self, params):
        self.params =params 

class Compound(AST):#语句堆？
    def __init__(self):
        self.children = []

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


INIT_VARTYPE = {
    'int': Num(Token(INT, 0)),
    'str': STRING(Token(STR, "")),
    'float': Float(Token(FLOAT, 0)) ,
    'bool': Bool(Token(BOOL,False))
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
            return node                     # 返回括号内的AST树
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
        left = self.variable()  # 获取变量名称节点
        token = self.current_token  # 获取当前记号
        self.eat(COLON)  # 验证：
        vartype = self.vartype()   #验证类型
        token = self.current_token  # 
        '''
        if token.type==EQUAL :
            self.eat(EQUAL)  # 验证赋值符
            right = self.expr()  # 获取表达式节点
            node = Assign(left, token, right,vartype)  # 组成赋值语句节点
            return node  # 返回赋值语句节点
        else:
            print(INIT_VARTYPE[vartype.name])
            node = Assign(left, Token(EQUAL,'='), INIT_VARTYPE[vartype.name],vartype)  # 组成赋值语句节点
        '''
        self.eat(EQUAL)  # 验证赋值符
        right = self.expr()  # 获取表达式节点
        node = Assign(left, token, right,vartype)  # 组成赋值语句节点
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
    
    def statement(self):
        if self.current_token.type == VAR:
            node = self.var()
        elif self.current_token.type == ID:
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
        else:
            node = self.empty()
        return node

    def statement_list(self):
        node = self.statement()
        nodelist = [node]

        while self.current_token.type == SEMI or self.current_token.type == ENDL :
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
    
    def parse(self):
        node = self.program()
        #print(node)
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

class BuiltinSymbol(Symbol):
    def __init__(self,name):
        super().__init__(name)

class VarSymbol(Symbol):
    def __init__(self,name,stype):
        super().__init__(name,stype)

class SymbolTable():
    def __init__(self):
        self.symbol = collections.OrderedDict()
        self.init()

    def init(self):
        self.define(BuiltinSymbol("int"))
        self.define(BuiltinSymbol("float"))
        self.define(BuiltinSymbol("bool"))
        self.define(BuiltinSymbol("string"))
        self.define(BuiltinSymbol("endl"))
    
    def __str__(self):
        symtab_header = '符号表中的内容：'
        lines = [symtab_header, '-' * len(symtab_header) * 2]  # 头部标题与分割线存入打印内容的列表
        lines.extend([f'{key:8}: {value}' for key, value in self._symbols.items()])  # 符号表内容合并到打印内容列表
        s = '\n'.join(lines)  # 以换行符连接每个列表元素组成字符串
        return s  # 返回打印内容

    __repr__ = __str__

    
    def define(self,symbol):
        self.symbol[symbol.name] = symbol

    def query(self,name):
        return self.symbol.get(name)

class SemanticAnalyzer(NodeVisitor):
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
    
    def visit_Const(self,node):
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
    
    def visit_STRING(self,node):
        pass

    def visit_Num(self,node):
        pass
    
    def visit_Float(self,node):
        pass

    def visit_Bool(self,node):
        pass

    def visit_NoOp(self, node):  # 访问空语句节点
        pass  





class Interpreter(NodeVisitor):
    
    GLOBAL_SCOPE = {
        'endl' : '\n',
        
    }  
    VAR_RALATION_TYPE = {
        'endl' : 'str',
    }
    IS_CONST = {
        'endl' : True,
    }
    
    def __init__(self, tree):  # 定义构造方法获取用户输入的表达式
        self.tree = tree

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
        if str(type(value)) == tp:
            self.VAR_RALATION_TYPE[var_name] = var_type
            self.GLOBAL_SCOPE[var_name] = value  # 以变量名称为键添加变量值到符号表
            self.IS_CONST[var_name] = False
        else:
            raise ValueError("Type of the variable changed 变量的类型发生了改变")
    
    def visit_Const(self, node):  
        var_name = node.left.name  
        var_type = node.vartype.name
        value = self.visit(node.right)
        tp = f"<class '{var_type}'>"
        if str(type(value)) == tp:
            self.VAR_RALATION_TYPE[var_name] = var_type
            self.GLOBAL_SCOPE[var_name] = value  
            self.IS_CONST[var_name] = True
        else:
            raise ValueError("Type of the const variable changed 常量的类型发生了改变")
    
    def visit_Change(self,node):
        varname = node.left.name
        value = self.visit(node.right)
        vartype = self.VAR_RALATION_TYPE[varname]
        tp = f"<class '{vartype}'>"
        if self.IS_CONST[varname] == True:
            raise ValueError("Conster variable can't be changed 常量发生了改变")
        if str(type(value)) == tp:
            self.GLOBAL_SCOPE[varname] = value
        else:
            raise ValueError("Type of the variable changed 变量的类型发生了改变")
    
    def visit_Variable(self, node):  # 访问变量节点
        var_name = node.name  # 获取变量名称
        value = self.GLOBAL_SCOPE.get(var_name)  # 获取变量值
        if value is None:  # 如果没有返回值（变量不存在）
            raise NameError(f'错误的标识符：{repr(var_name)}')  # 抛出异常
        else:  # 否则
            return value  # 返回变量值
    
    def visit_Compound(self,node):
        for child in node.children:
            self.visit(child)
    
    def visit_STRING(self,node):
        return node.value
    
    def visit_Float(self,node):
        return node.value
    
    def visit_Bool(self,node):
        return node.value
      
    def visit_Var(self,node):
        varname = node.name
        value = self.GLOBAL_SCOPE.get(varname)
        if varname in self.GLOBAL_SCOPE:
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
    
    def visit_Srin(self,node):#还没写完
        for node in node.params:
            val = input()
            tp = VAR_RALATION_TYPE[node.name]
            GLOBAL_SCOPE[node.name]

    def interpret(self):  # 执行解释的方法
        return self.visit(self.tree)







def main():
    with open("Code.txt","r") as f:
        text = f.read() 
    lexer = Lexer(text)
    parser = Parser(lexer)
    tree = parser.parse()
    
    builder = SemanticAnalyzer()
    builder.visit(tree)
    
    interpreter = Interpreter(tree)
    interpreter.interpret()
    
    print(interpreter.GLOBAL_SCOPE)  # 显示输出符号表
    print(interpreter.VAR_RALATION_TYPE)
   
if __name__ == '__main__':
    main()
