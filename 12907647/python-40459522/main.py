'''
* build calcer 计算器(eval)
* build old 旧版ij
build QCE minus 10 搭建环境，搜罗网站【log/#/自制解释器】，确定大概语法
build QCE minus 5 搭建符号类
build QCE minus 0 搭建解释器类
build D 0 支持加法运算
build 0 支持加减
build 5 支持跳空格、乘除
build 10 运算优先级，增加lexer
build 15 支持正负
build 20 支持括号，增加AST和parser
build 23 自制visit方法
build 25 标准教程
build 27 废除parser，改进lexer
build 30 废除lexer
build 0 release 重写，定义符号字典、关键字列表等
build 35 自己写解释器类
build 40 导入sys库，添加error方法、advance推进字符
build 45 添加expr方法、run方法用于运行；get_next_token用于获取下一个token
build 50 token存储在stack中
build 60 增加识别符号，整数、加减乘除等
build 65 添加get_near获取邻近字符、is_end判断末尾、isnum判断是否是数字，is_num_or_point判断是否是数字或小数点
build 70 延长数字的方法
build 85 优化延长数字算法，用字符串分割，添加数字置换方法
build 90 添加add_token，并且用expr传入visit计算并返回结果
build 10 release visit的一元、二元、三元计算分支，写出加减乘除优先级分别遍历计算并返回结果
build 15 release 支持正负
build 20 release 字符删除后问题修复，for循环改方便的while，并支持一层括号
build 35 release 分索引，递归支持多层括号
build 40 release 浮点数error返回，改进error报错
build 50 release 优化stack存储方式，改为行存储
build 100 修复括号内索引bug
build 105 分离正负、加减
1/8 build90假名100发布，pid=40496105
build 60 release 优化识别符号
build 118 多括号索引删除问题解决，完全支持四则运算，添加namespace和database
build 140 实现变量，中间的艰难过程6小时就不说了
build 100 release 修复少量bug，完全打倒cell版本insjhx，增加变量代入
build 145 变量完善，支持注释计算法（不常用），如b=1 (a=1+1)
build 155 变量继续完善，完善注释计算法（不常用），简化变量交换，如(e=5)a(g=7)=(f=6)1(b=2(d=4))(c=3)都不会报错
build 10 double-release 优化get_next_token，明确运算优先
build 140 release 优化get_next_token，智能分析变量
build 160 变量继续完善，双赋值优化
'''

import sys

token_dict = {
    ' ': ('space',' '),
    'integer': ('int',None),
    'string': ('str',None),
    'floating': ('float',None),
    '+': ('operator','+'),
    '-': ('operator','-'),
    '*': ('operator','*'),
    '/': ('operator','/'),
    '//': ('operator','//'),
    '%': ('operator','%'),
    '|': ('operator','|'),
    '&': ('operator','&'),
    '^': ('operator','^'),
    '<': ('operator','<'),
    '>': ('operator','>'),
    '=': ('symbol','='),
    '.': ('symbol','.'),
    '(': ('symbol','('),
    ')': ('symbol',')'),
    '[': ('symbol','['),
    ']': ('symbol',']'),
    '\n': ('EOF','\n'),
    'ENDEOF': ('EOF','ENDEOF'),
}

# 极致打表
varcharlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

tpdict = {
    'int': 'integer',
    'str': 'string',
    'float': 'floating',
}

keyword_list = [
    'read',   # 导库
    # 'in',     # stdin
    # 'out',    # stdout
    'if',
    'elif',
    'else',
    'while',
    'for',
    'conti',
    'break',
    'let',
    'fun',
    'class',
    'struct',
    'db',
    'cfg',
    'true',
    'false',
    'null',
    'because',
]

integer_replacelist = [   # 不要加进小数点
    '!','@','#','$','%','^','&','*','(',')',
    '[',']','{','}','+','-','/','=','|',',',
    '\'','\"',';',':','<','>','?','\\',
    '~','·','`',
]

operatorlist = {
    '(': 4,
    ')': 4,
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '=': 1,
}

namespace = {}
database = []

class Token(object):
    def __init__(self,name,tp,value):
        self.name = name
        self.tp = tp
        self.value = value
    def __str__(self):
        return self.name+'|'+self.tp+'|'+str(self.value)
    __repr__ = __str__

class Interpreter(object):
    def __init__(self,code):
        self.code = code
        self.codelength = len(self.code)
        self.codelastindex = self.codelength - 1
        self.line = 0
        self.position = -1
        self.lineposition = -1
        self.current_char = ''
        self.current_word = ''
        self.current_token = None
        self.token_stack = []
    
    def error(self,msg):
        msg = '[Error] File "main.insjhx":\nerror|'+msg
        raise SystemExit(msg)
        # print(msg)
        # sys.exit(0)
    
    def is_end(self):
        return self.position >= self.codelength
    
    def advance(self):
        self.position += 1
        self.lineposition += 1
        if self.is_end():
            return 'end'
        self.current_char = self.code[self.position]
        self.current_word += self.current_char
        return 'normal'
    
    def get_near(self,index=1):
        try:
            return self.code[self.position+index]
        except:
            return 'out index'
    
    def isnum_or_point(self,string):
        return string.isdigit() or string == '.'
    
    def isnum(self,string):
        left = string
        right = self.get_near()
        return (left.isdigit() and right.isdigit()) \
            or (left.isdigit() and right == '.') \
            or (left == '.' and right.isdigit()) \
    
    def is_defined(self,string):
        return (string in token_dict) \
            or (string in keyword_list) \
            or (string in namespace)
    
    def get_next_token(self):
        if self.advance() == 'end':
            return Token('ENDEOF','EOF','ENDEOF')
        
        # 智能判断变量
        if (self.current_char not in varcharlist) and len(self.current_word) > 1:
            self.token_stack.append(Token('variable','var',self.current_word[:-1]))
            self.current_word = self.current_char
        
        if self.isnum(self.current_word):   # 多位数字
            linestring = self.code.split('\n')[self.line][self.lineposition:]
            for i in integer_replacelist:
                linestring = linestring.replace(i,' ')
            linestring = linestring.split()[0]
            if '.' in linestring:
                try:
                    self.current_token = Token('floating','float',float(linestring))
                except:
                    self.error('浮点数'+linestring+'不正确')
            else:
                self.current_token = Token('integer','int',int(linestring))
            self.position += len(linestring) - 1
            self.lineposition += len(linestring) - 1
            self.current_word = ''
            return self.current_token
        
        if self.current_word.isdigit():  # 一位数字
            self.current_token = Token('integer','int',int(self.current_word))
            self.current_word = ''
            return self.current_token
        
        if self.current_char == ' ':   # 最重要的语法：空格~
            # 定义变量
            if len(self.current_word) > 1:
                left = self.current_word[:-1]
                # if not self.is_defined(left):
                self.token_stack.append(Token('variable','var',left))
            if self.token_stack and self.token_stack[-1].name in [' ','=']:
                self.current_word = ''
                return self.get_next_token()
            self.current_word = ''
            return Token(' ','space',' ')
        
        if self.current_char == '=':   # 变量赋值
            if len(self.current_word) > 1:
                self.current_token = Token('variable','var',self.current_word[:-1])
                self.token_stack.append(self.current_token)
            if self.token_stack and self.token_stack[-1].name == ' ':   # 删除无用空格
                self.token_stack = self.token_stack[:-1]
            self.current_word = ''
            return Token('=','symbol','=')
        
        if self.current_word in token_dict:  # 特定符号
            self.current_token = Token(self.current_word,
                                       token_dict[self.current_word][0],
                                       token_dict[self.current_word][1])
            self.current_word = ''
            return self.current_token
        
        if self.current_word in namespace:   # 使用命名空间中的statement
            # if '=' not in self.code.split('\n')[self.line][self.lineposition:]:   # 如果不是赋值(=不在右侧)，就转化
            value = namespace[self.current_word]
            self.current_token = Token(self.current_word,'var-'+value[1],value[2])
            self.current_word = ''
            return self.current_token
        
        return self.get_next_token()
    
    def calc_unary(self,name,expression):   # 一元运算
        if name == '+':
            return (+expression, 'integer', 'int')
        if name == '-':
            return (-expression, 'integer', 'int')
    
    def calc_binary(self,name,left,right):   # 二元运算
        global namespace
        if name == '=':
            if left == right.value == ' ':
                return
            if left[0].isdigit():
                self.error('变量名不能以数字开头')
            if not left.isascii():
                self.error('变量名不能含有非ascii字符')
            namespace[left] = (right.name,right.tp,right.value)
            return
        if name == '+':
            result = left + right
        if name == '-':
            result = left - right
        if name == '*':
            result = left * right
        if name == '/':
            result = left / right
        if name == '//':
            result = left // right
        if name == '%':
            result = left % right
        if name == '**':
            result = left ** right
        tp = str(type(result))[8:-2]
        if tp == 'int':
            name = 'integer'
        elif tp == 'float':
            name = 'floating'
            result = round(result,15)
        return (result,name,tp)
    
    def calc_ternary(self,name,expr1,expr2,expr3):   # 三元运算
        pass
    
    def revisit(self,stack):     # 交互式递归突破python限制
        return self.visit(stack)
    
    def visit(self,stack):
        token = -1     # 括号 左结合
        parenthese_inside = 0
        parenthese_beginpos = 0
        parenthese_stack = []
        while token < len(stack)-1:
            token += 1
            tn = stack[token].name
            if parenthese_inside:
                parenthese_stack.append(stack[token])
            if tn in operatorlist:
                if operatorlist[tn] == 4:
                    if tn == '(':
                        parenthese_inside += 1
                        if parenthese_inside == 1:
                            parenthese_beginpos = token
                    elif tn == ')':
                        parenthese_inside -= 1
                        if parenthese_inside == 0:    # 最外层括号结束
                            parenthese_stack.remove(parenthese_stack[-1])
                            result = self.revisit(parenthese_stack)
                            if result:
                                stack[token] = result[0]
                                stack = stack[:parenthese_beginpos]+stack[token:]
                            else:
                                stack = stack[:parenthese_beginpos]+stack[token+1:]
                            token = 0    # 得到结果删除token必须重检索引
                            parenthese_stack = []
                    
        token = -1   # 乘除 左结合
        while token < len(stack)-1:
            token += 1
            tn = stack[token].name
            if tn in operatorlist:
                if operatorlist[tn] == 3:
                    left = stack[token-1]
                    right = stack[token+1]
                    result = self.calc_binary(tn,left.value,right.value)
                    stack[token].value, stack[token].name, stack[token].tp = result
                    stack.remove(left)
                    stack.remove(right)
                    token -= 1
        
        token = len(stack)   # 正负 右结合
        while token > -1:
            token -= 1
            tn = stack[token].name
            if tn in operatorlist:
                if operatorlist[tn] == 2:
                    left = stack[token-1]
                    right = stack[token+1]
                    if left.name not in ('integer','floating'):
                        result = self.calc_unary(tn,right.value)
                        stack[token].value, stack[token].name, stack[token].tp = result
                        stack.remove(right)
        
        token = -1   # 加减 左结合
        while token < len(stack)-1:
            token += 1
            tn = stack[token].name
            if tn in operatorlist:
                if operatorlist[tn] == 2:
                    left = stack[token-1]
                    right = stack[token+1]
                    result = self.calc_binary(tn,left.value,right.value)
                    stack[token].value, stack[token].name, stack[token].tp = result
                    stack.remove(left)
                    stack.remove(right)
                    token -= 1
        token = -1   # 变量 左结合
        while token < len(stack)-1:
            token += 1
            tn = stack[token].name
            if tn in operatorlist:
                if operatorlist[tn] == 1:
                    for i in range(token):
                        left = stack[i]
                        right = stack[token+i+1]
                        if left.tp.split('-')[0] == 'var' and left.name != 'variable':
                            left.value = left.name
                        if right.tp.split('-')[0] == 'var':
                            right.tp = right.tp.split('-')[1]
                            right.name = tpdict[right.tp]
                        self.calc_binary(tn,left.value,right)  # 赋值
                    stack.clear()
        return stack
    
    def add_token(self):
        self.current_token = self.get_next_token()
        self.token_stack.append(self.current_token)
        if self.current_token.name == 'ENDEOF':
            return False
        if self.current_token.name == '\n':
            self.line += 1
            self.lineposition = -1
        return True
    
    def expr(self):
        while self.add_token():
            if self.current_token.name == '\n':
                self.token_stack = self.visit(self.token_stack)
                self.token_stack.clear()   # 一行运行结束清除session(bushi+doge
        self.token_stack = self.visit(self.token_stack)
        self.token_stack.clear()
            
        return self.token_stack
    
    def run(self):
        return self.expr()

code = '''
a = 1(b= 2)
a=b(b=a)
'''

interpreter = Interpreter(code=code)
r = interpreter.run()
# print(r)
print(namespace)