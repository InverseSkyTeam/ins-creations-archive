'''
* build calcer 计算器(eval)
* build old 旧版ij
build QCE minus 10 搭建环境，搜罗网站【log/可能还有用的资料/自制解释器】，确定大概语法
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
build 145 release 优化智能分析变量，重写正负计算，解决误吞变量问题
build 165 优化get_next_token，通过智能分析变量删减了空格和等号分析变量的部分
build 166 添加了一些数据
build 168 修改了字典名
build 170 优化与完善变量赋值情况，添加报错机制
build 15 double-release 符号多优先级用元组代替，修复正负问题，提高正负优先级在乘除之上
build 15 triple-release 加入位非符号，和正负同一级，且为右结合
build 177 添加 ** // % 运算符，增加优先级层数
build 185 添加bool类型，>= <= > < == !=判断符号，<< >>运算符号
build 190 添加bool和null类型的运算与使用，混合运算，整理运算方法，优化get_next_token
build 170 release 完善bool和null类型，清除一定屎山，封装了leftconnect函数，整体优化，变量随心用
build 100 double-release 修复一些索引越界/较短的问题
build 193 添加if-elif-else的识别和在大括号内的换行控制，同时修复self.current_token未赋值bug
build 195 添加更多检测和识别大括号
build 195 undo 撤销大括号内识别符，考虑多重嵌套，将括号判断从get_next_token(lexer)放入了expr(interpreter)中，添加处理换行后空格
build 211 get_next_token 超大改革
build 215 get_next_token 完善，if前换行处理，current_token改革
build 225 支持if语句
build 240 支持if-elif-else以及嵌套，get_next_token优化
build 246 改进换行判断，解决长整型截取索引出错
build 253 空格、换行整改
build 265 撤销删除所有if板块，增加expr_block方法，完善变量存储等，绘制“设计流程图.jpg”
build 270 换方法重新实现简单if，并未重写elif和else，重写是因为之前代码质量差，看着屎山
build 193 release 除错，改进get_next_token，实现if
build 200 release 添加大括号新的改法，更高log.py版式
build 300 超级大更！
          1.写出了完整的if-elif-else
          2.优化了换行
          3.优化了长整数读取
          4.优化了get_next_token的特殊字符
          5.优化了expr执行，传递更加方便
          6.撤销臃肿的revisit
          7.增加测试点
          8.优化大括号读取
          9.优化空格词法
          10.添加get_nears方法
          11.扩展功能
          12.优化了Token类
          13.解释器运行返回值撤销
          14.更改样例，全部通过
build 265 release 再优化if-block，整体优化
build 300 release 优化一点算法，加快了速度，优化到和最早版本几乎一样快
build 305 增删改关键字
build 308 添加clean_code，清洁代码，右大括号后空行
build 311 添加python执行类，为以后执行python的能力做奠基
build 315 插入while指示符，为while循环做奠基
build 320 第一次正式写入while和break，但处于开发模式
build 360 超级大更！
          1.[重大] 开启copy库，stack改传址为传值，修复了while循环篡改问题
          2.[重大] 实现while{break 跳出层数}格式
          3.支持自赋值:+= -= %=等
          4.修正正负数的问题
          5.修正空格词法
          6.更改优先级
          7.添加..运算符
          8.精简类型写法
          9.修正浮点数读取算法
          10.改正嵌套递归运算
          11.设置递归次数3000
          12.[重大] 实现字符串及转义
          13.继而，写出了深转义，不再是replace功夫

'''

import sys
import copy

sys.setrecursionlimit(3000)
NoneType = type(None)

token_dict = {
    int: ('int',None),
    float: ('float',None),
    bool: ('bool',None),
    str: ('str',None),
    NoneType: ('null',None),
    dict: ('dict',None),
    list: ('list',None),
    '+': ('operator','+'),
    '-': ('operator','-'),
    '*': ('operator','*'),
    '/': ('operator','/'),
    '**': ('operator','**'),
    '//': ('operator','//'),
    '%': ('operator','%'),
    '+=': ('operator','+='),
    '-=': ('operator','-='),
    '*=': ('operator','*='),
    '/=': ('operator','/='),
    '**=': ('operator','**='),
    '//=': ('operator','//='),
    '%=': ('operator','%='),
    '|': ('operator','|'),
    '&': ('operator','&'),
    '^': ('operator','^'),
    '<': ('operator','<'),
    '>': ('operator','>'),
    '<<': ('operator','<<'),
    '>>': ('operator','>>'),
    '!': ('operator','!'),
    '==': ('operator','=='),
    '!=': ('operator','=='),
    '>=': ('operator','>='),
    '<=': ('operator','<='),
    '~': ('symbol','~'),
    '=': ('symbol','='),
    '.': ('symbol','.'),
    '..': ('symbol','..'),
    '\"': ('symbol','\"'),
    '\'': ('symbol','\''),
    '(': ('symbol','('),
    ')': ('symbol',')'),
    '[': ('symbol','['),
    ']': ('symbol',']'),
    '{': ('symbol','{'),
    '}': ('symbol','}'),
    '\n': ('EOF','\n'),
    'ENDEOF': ('EOF','ENDEOF'),
}

# 极致打表
varcharlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z', '_',
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

assignmentoplist = ['=','+=','-=','*=','/=','**=','//=','%=','<<=','>>=']

keyword_list = [  # 贴在左边的已完成
    'use',   # 导库
    'in',     # stdin
    'out',    # stdout
'if',
'elif',
'else',
    'while',
    'for',
    'conti',
    'break',
    'cycle',
    'with',
    'fun',
    'class',
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

operatordict = {
    '(': (10,),
    ')': (10,),
    '~': (9,),
    '..': (8,),
    '**': (7,),
    '%': (6,),
    '//': (6,),
    '*': (6,),
    '/': (6,),
    '+': (5,9,),
    '-': (5,9,),
    '<<': (4,),
    '>>': (4,),
    '>': (3,),
    '<': (3,),
    '>=': (3,),
    '<=': (3,),
    '==': (2,),
    '!=': (2,),
    '=': (1,),
    '+=': (1,),
    '-=': (1,),
    '*=': (1,),
    '/=': (1,),
    '//=': (1,),
    '**=': (1,),
    '%=': (1,),
    '<<=': (1,),
    '>>=': (1,),
}

namespace = {}
database = []

class Token(object):
    def __init__(self,name,tp,value):
        self.name = name
        self.tp = tp
        self.value = value
    def __str__(self):
        if self.tp == 'var':
            return str(self.name)+'|'+self.tp
        return str(self.name)+'|'+self.tp+'|'+str(self.value)
    __repr__ = __str__

class PythonExer(object):
    def __init__(self,code):
        self.code = code
        self.pynamespace = {}
    def execute(self):
        try:
            exec(self.code,globals(),self.pynamespace)
        except:
            return 'error'
        return 'success'

class Interpreter(object):
    def __init__(self,code):
        self.code = code
        self.clean_code()
        self.codelength = len(self.code)
        self.code += ' '
        self.codelastindex = self.codelength - 1
        self.line = 0
        self.position = -1
        self.lineposition = -1
        self.inblocks = 0
        self.current_char = ''
        self.current_word = ''
        self.current_token = None
        self.whiles = 0
        self.breaks = 0
        self.token_stack = []
    
    def error(self,msg):
        msg = '[Error] File "main.ij":\nerror|'+msg
        raise SystemExit(msg)
        # print(msg)
        # sys.exit(0)
    
    def advance(self):
        self.position += 1
        self.lineposition += 1
        self.current_char = self.code[self.position]
        self.current_word += self.current_char
    
    def get_near(self,index=1):
        try:
            return self.code[self.position+index]
        except:
            return 'out index'
    
    def get_nears(self,start=1,end=2):
        s = ''
        for i in range(start,end+1):
            s += self.get_near(index=i)
        return s
    
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
    
    def clean_code(self):
        newcode = ''
        instring = [0,0]
        for i in self.code:
            newcode += i
            if sum(instring) == 0:
                if i == '}':
                    newcode += '\n'
            if i == '"' and instring[1] == 0 and newcode[-1] != '%':
                if instring[0]:
                    instring[0] = 0
                else:
                    instring[0] = 1
            if i == "'" and instring[0] == 0 and newcode[-1] != '%':
                if instring[1]:
                    instring[1] = 0
                else:
                    instring[1] = 1
        self.code = newcode
    
    def get_next_token(self):
        self.advance()
        if self.position >= self.codelength:
            return Token('ENDEOF','EOF','ENDEOF')
        
        # 智能判断变量
        if (self.current_char not in varcharlist) and len(self.current_word) > 1:
            self.current_token = Token(self.current_word[:-1],'var','var')
            self.current_word = ''
            self.position -= 1
            self.lineposition -= 1
            return self.current_token
        
        while self.current_word == ' ':
            self.current_word = ''
            self.advance()
        
        if self.isnum(self.current_word):   # 多位数字
            linestring = self.code.split('\n')[self.line][self.lineposition:]
            for i in integer_replacelist:
                linestring = linestring.replace(i,' ')
            linestring = linestring.split()[0]
            if '.' in linestring:
                try:
                    token = Token(float,'float',float(linestring))
                except:
                    token = Token(int,'int',int(self.current_word))   # 浮点读入异常，必是一位数
                    self.current_word = ''
                    return token
            else:
                token = Token(int,'int',int(linestring))
            self.position += len(linestring) - 1
            self.lineposition += len(linestring) - 1
            self.current_word = ''
            return token
        
        if self.current_word.isdigit():  # 一位数字
            token = Token(int,'int',int(self.current_word))
            self.current_word = ''
            return token
        
        if self.current_word in ['"',"'"] and self.get_near(-1) != '\\':
            string = self.code[self.position+1:]
            nextpos = string.find(self.current_word)
            if nextpos > 0:
                while string[nextpos-1] == '\\':
                    nextpos = string.find(self.current_word,nextpos+1)
            if nextpos == -1:
                self.error('代码中有引号不匹配')
            string = list(string[:nextpos] + ' '*10)    # 防止列表越界
            for i in range(len(string)-10):
                if ''.join(string[i:i+2]) == r'\\':
                    string[i] = '\\'
                    del string[i+1]
                elif ''.join(string[i:i+2]) == r'\"':
                    string[i] = '"'
                    del string[i+1]
                elif ''.join(string[i:i+2]) == r"\'":
                    string[i] = "'"
                    del string[i+1]
                elif ''.join(string[i:i+5]) == r'\back':
                    string[i] = '\b'
                    del string[i+1:i+5]
                elif ''.join(string[i:i+5]) == r'\line':
                    string[i] = '\n'
                    del string[i+1:i+5]
                elif ''.join(string[i:i+6]) == r'\color':
                    string[i] = '\033'
                    del string[i+1:i+6]
                elif ''.join(string[i:i+7]) == r'\return':
                    string[i] = '\r'
                    del string[i+1:i+7]
                elif ''.join(string[i:i+2]) == r'\n':
                    string[i] = '\n'
                    del string[i+1]
                elif ''.join(string[i:i+2]) == r'\r':
                    string[i] = '\r'
                    del string[i+1]
                elif ''.join(string[i:i+2]) == r'\t':
                    string[i] = '\t'
                    del string[i+1]
                elif ''.join(string[i:i+2]) == r'\h':
                    string[i] = '\t'
                    del string[i+1]
                elif ''.join(string[i:i+2]) == r'\v':
                    string[i] = '\v'
                    del string[i+1]
                elif ''.join(string[i:i+2]) == r'\c':
                    string[i] = '\033'
                    del string[i+1]
                elif ''.join(string[i:i+2]) == r'\b':
                    string[i] = '\b'
                    del string[i+1]
            string = ''.join(string[:-10])
            token = Token(str,'str',string)
            self.position += nextpos + 1
            self.lineposition += nextpos + 1
            self.current_word = ''
            return token
        
        if self.current_word in token_dict:  # 特定符号
            near_char = self.current_word + self.get_near()
            while near_char in token_dict:
                self.current_word = near_char
                near_char = self.current_word + self.get_near()
                self.position += 1
                self.lineposition += 1
            token = Token(self.current_word,
                          token_dict[self.current_word][0],
                          token_dict[self.current_word][1])
            self.current_word = ''
            return token
        
        if self.current_word in keyword_list and (self.get_near() not in varcharlist):  # 关键字
            if self.current_word == 'true':    # 特殊处理
                token = Token('bool','bool',True)
            elif self.current_word == 'false':
                token = Token('bool','bool',False)
            elif self.current_word == 'null':
                token = Token('null','NoneType',None)
            else:     # 正常处理
                token = Token(self.current_word,'keyword',self.current_word)
            if self.current_word == 'if' and self.token_stack and (not self.token_stack[-1].tp=='EOF'):
                self.position -= 2
                self.lineposition -= 2
                token = Token('\n','EOF','\n')
            elif self.current_word == 'while' and self.token_stack and (not self.token_stack[-1].tp=='EOF'):
                self.position -= 5
                self.lineposition -= 5
                token = Token('\n','EOF','\n')
            self.current_word = ''
            return token
        
        return self.get_next_token()
    
    def convert_var(self,var):
        value = namespace[var.name]
        name = type(namespace[var.name])
        tp = token_dict[name]
        return Token(name,tp,value)
    
    def calc_unary(self,name,expression):   # 一元运算
        if expression.name in namespace:
            expression = self.convert_var(expression)
        if name == '+':
            return (+expression.value, int, 'int')
        if name == '-':
            return (-expression.value, int, 'int')
        if name == '~':
            return (~expression.value, int, 'int')
    
    def calc_binary(self,name,left,right):   # 二元运算
        global namespace
        if right.name in namespace:
            right = self.convert_var(right)
        if name == '=':
            if left.name[0].isdigit():
                self.error('变量名不能以数字开头')
            if not left.name.isascii():
                self.error('变量名不能含有非ascii字符')
            if right.name in namespace:
                namespace[left.name] = namespace[right.name]
                return
            namespace[left.name] = right.value
            return
        elif name == '+=':
            namespace[left.name] += right.value
            return
        elif name == '-=':
            namespace[left.name] -= right.value
            return
        elif name == '*=':
            namespace[left.name] *= right.value
            return
        elif name == '/=':
            namespace[left.name] /= right.value
            return
        elif name == '**=':
            namespace[left.name] **= right.value
            return
        elif name == '//=':
            namespace[left.name] //= right.value
            return
        elif name == '%=':
            namespace[left.name] %= right.value
            return
        elif name == '<<=':
            namespace[left.name] <<= right.value
            return
        elif name == '>>=':
            namespace[left.name] >>= right.value
            return
        if left.name in namespace:
            left = self.convert_var(left)
        if name == '!=':
            result = left.value != right.value
        elif name == '==':
            result = left.value == right.value
        elif name == '<=':
            result = left.value <= right.value
        elif name == '>=':
            result = left.value >= right.value
        elif name == '<':
            result = left.value < right.value
        elif name == '>':
            result = left.value > right.value
        elif name == '<<':
            result = left.value << right.value
        elif name == '>>':
            result = left.value >> right.value
        elif name == '+':
            result = left.value + right.value
        elif name == '-':
            result = left.value - right.value
        elif name == '*':
            result = left.value * right.value
        elif name == '/':
            result = left.value / right.value
        elif name == '//':
            result = left.value // right.value
        elif name == '%':
            result = left.value % right.value
        elif name == '**':
            result = left.value ** right.value
        elif name == '..':
            result = list(range(left.value,right.value+1))
        else:
            self.error('解释器接收符号异常')
        tp = type(result)
        if tp == float:
            result = round(result,15)
        return (result,tp,token_dict[tp])
    
    def calc_ternary(self,name,expr1,expr2,expr3):   # 三元运算
        pass
    
    def leftconnect(self,stack,level,s=None):  # 左结合
        stack = copy.deepcopy(stack)   # 传址->传值
        token = -1
        while token < len(stack) - 1:
            token += 1
            tn = stack[token].name
            if tn in operatordict:
                if (level in operatordict[tn]):
                    left = stack[token-1]
                    right = stack[token+1]
                    oldleft = left
                    oldright = right
                    if left.name == 'null':
                        left = Token(int,'int',0)
                    if right.name == 'null':
                        right = Token(int,'int',0)
                    result = self.calc_binary(tn,left,right)
                    stack[token].value, stack[token].name, stack[token].tp = result
                    stack.remove(oldleft)
                    stack.remove(oldright)
                    token -= 1
        return stack
    
    def visit(self,stack,s=None):
        stack = copy.deepcopy(stack)
        if stack == []:
            return []
        if stack[0].name == 'break':
            if len(stack) > 2:
                self.breaks += stack[2].value
            else:
                self.breaks += 1
        
        token = -1
        if_condition_startposition = None
        while_condition_startposition = None
        block_startposition = None
        braceinside = 0
        thistype = None
        while token < len(stack) - 1:    # 分支 左结合
            token += 1
            tn = stack[token].name
            if tn == 'if':
                if thistype == None:
                    thistype = 'if'
                    if_condition_startposition = token + 1
            elif tn == 'elif':
                if thistype != 'if':
                    self.error('没有if就出现了elif')
                if_condition_startposition = token + 1
            elif tn == 'else':
                if thistype != 'if':
                    self.error('没有if就出现了else')
                if_condition_startposition = 'ELSE CON'
            elif tn == 'while':
                if thistype == None:
                    thistype = 'while'
                    while_condition_startposition = token + 1
            elif tn == '{':
                braceinside += 1
                if braceinside == 1:    # 是最外层大括号{
                    block_startposition = token + 1
                    if thistype == 'if':
                        if if_condition_startposition == 'ELSE CON':    # 是else就直接执行
                            condition = True
                        else:
                            condition = stack[if_condition_startposition:token]
                            condition = self.visit(condition,stack)[0]
                            if condition.name in namespace:
                                condition = self.convert_var(condition)
                            condition = condition.value
                    elif thistype == 'while':
                        condition = stack[while_condition_startposition:token]
            elif tn == '}':
                braceinside -= 1
                if braceinside == 0:    # 是最外层大括号}
                    if thistype == 'if':
                        if condition:
                            blockcode = stack[block_startposition:token]
                            self.exprblock(blockcode)
                            return []
                    elif thistype == 'while':
                        # self.error('while还处于开发阶段！')
                        blockcode = stack[block_startposition:token]
                        self.whiles += 1
                        while True:
                            if self.breaks:
                                self.breaks -= 1
                                break
                            condition_result = self.visit(condition)[0]
                            if condition_result.name in namespace:
                                condition_result = self.convert_var(condition_result)
                            condition_result = condition_result.value
                            if not condition_result:
                                break
                            self.exprblock(blockcode)
                        self.whiles -= 1
                        return []
                            
        if thistype != None:
            return []

        token = -1     # 括号 左结合
        parenthese_inside = 0
        parenthese_beginpos = 0
        parenthese_stack = []
        while token < len(stack)-1:
            token += 1
            tn = stack[token].name
            if parenthese_inside:
                parenthese_stack.append(stack[token])
            if tn in operatordict:
                if (10 in operatordict[tn]):
                    if tn == '(':
                        parenthese_inside += 1
                        if parenthese_inside == 1:
                            parenthese_beginpos = token
                    elif tn == ')':
                        parenthese_inside -= 1
                        if parenthese_inside == 0:    # 最外层括号结束
                            parenthese_stack.remove(parenthese_stack[-1])
                            result = self.visit(parenthese_stack)
                            if result:
                                stack[token] = result[0]
                                stack = stack[:parenthese_beginpos]+stack[token:]
                            else:
                                stack = stack[:parenthese_beginpos]+stack[token+1:]
                            token = -1    # 得到结果删除token必须重检索引
                            parenthese_stack = []
        
        token = len(stack)   # 正负 位取反 右结合
        while token > 0:
            token -= 1
            tn = stack[token].name
            if tn in operatordict:
                if (9 in operatordict[tn]):
                    left = stack[token-1]
                    right = stack[token+1]
                    if left.tp in ['operator','symbol']:
                        result = self.calc_unary(tn,right)
                        stack[token].value, stack[token].name, stack[token].tp = result
                        stack.remove(right)
        
        stack = self.leftconnect(stack,8)   # ..运算 左结合
        
        token = len(stack)   # 幂运算 右结合
        while token > 0:
            token -= 1
            tn = stack[token].name
            if tn in operatordict:
                if (7 in operatordict[tn]):
                    left = stack[token-1]
                    right = stack[token+1]
                    oldleft = left
                    oldright = right
                    if left.name == 'null':
                        left = Token(int,'int',0)
                    if right.name == 'null':
                        right = Token(int,'int',0)
                    result = self.calc_binary(tn,left,right)
                    stack[token].value, stack[token].name, stack[token].tp = result
                    stack.remove(oldleft)
                    stack.remove(oldright)
        
        # 常规左结合
        stack = self.leftconnect(stack,6)   # 乘 除 取模 整除 左结合
        stack = self.leftconnect(stack,5)   # 加 减 左结合
        stack = self.leftconnect(stack,4)   # 左移 右移 左结合
        stack = self.leftconnect(stack,3)   # 大于 小于 大于等于 小于等于 左结合
        stack = self.leftconnect(stack,2,s)   # 等于 不等于 左结合
        
        token = -1   # 赋值 左结合
        while token < len(stack)-1:
            token += 1
            tn = stack[token].name
            if tn in operatordict:
                if (1 in operatordict[tn]):
                    for i in range(token):
                        left = stack[i]
                        right = stack[token+i+1]
                        self.calc_binary(tn,left,right)  # 赋值
                    stack.clear()
        
        return stack
    
    def add_token(self):
        self.current_token = self.get_next_token()
        self.token_stack.append(self.current_token)
        if self.current_token.name == 'ENDEOF':
            return False
        if self.get_near(0) == '\n':
            self.line += 1
            self.lineposition = -1
        return True
    
    def exprblock(self,stack):
        stack = copy.deepcopy(stack)
        
        stack.append(Token('ENDEOF','EOF','ENDEOF'))
        stackline = []
        inblocks = 0
        totalindex = -1
        
        for i in stack:
            stackline.append(i)
            totalindex += 1
            if i.name == '{':
                inblocks += 1
            if i.name == '}':
                inblocks -= 1
            if i.name == '\n' and (not inblocks):
                if stack[totalindex+1].name in ['elif','else','\n']:
                    continue
                self.visit(stackline)
                stackline.clear()
        self.visit(stackline)
    
    def expr(self):
        while self.add_token():
            pass
        # print(self.token_stack)
        self.exprblock(self.token_stack)
    
    def run(self):
        self.expr()

# code = r'''
# a=666.6
# b = "az
# za"
# c = "a\line\n\"\"\"\c\\ b"
# '''

code = '''
a=3
if (a) {a = 1}
 b = a
while a<10 {
    (a+= 1)
    b = b * a
}
'''

interpreter = Interpreter(code=code)
interpreter.run()
print(namespace)