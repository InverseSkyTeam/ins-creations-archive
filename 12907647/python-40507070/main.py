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
'''

import sys

token_dict = {
    ' ': ('space',' '),
    'integer': ('int',None),
    'floating': ('float',None),
    'bool': ('bool',None),
    'string': ('str',None),
    'null': ('NoneType',None),
    '+': ('operator','+'),
    '-': ('operator','-'),
    '*': ('operator','*'),
    '/': ('operator','/'),
    '**': ('operator','**'),
    '//': ('operator','//'),
    '%': ('operator','%'),
    '|': ('operator','|'),
    '&': ('operator','&'),
    '^': ('operator','^'),
    '<': ('operator','<'),
    '>': ('operator','>'),
    '<<': ('operator','<<'),
    '>>': ('operator','>>'),
    '==': ('operator','=='),
    '!=': ('operator','=='),
    '>=': ('operator','>='),
    '<=': ('operator','<='),
    '~': ('symbol','~'),
    '=': ('symbol','='),
    '.': ('symbol','.'),
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

tpdict = {
    'int': 'integer',
    'str': 'string',
    'float': 'floating',
    'bool': 'bool',
    'NoneType': 'null',
}

keyword_list = [  # 贴在左边的已完成
    'read',   # 导库
    'in',     # stdin
    'out',    # stdout
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

operatordict = {
    '(': (9,),
    ')': (9,),
    '~': (8,),
    '**': (7,),
    '%': (6,),
    '//': (6,),
    '*': (6,),
    '/': (6,),
    '+': (5,8,),
    '-': (5,8,),
    '<<': (4,),
    '>>': (4,),
    '>': (3,),
    '<': (3,),
    '>=': (3,),
    '<=': (3,),
    '==': (2,),
    '!=': (2,),
    '=': (1,),
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
        self.inblocks = 0
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
    
    def get_next_token(self):
        if self.advance() == 'end':
            return Token('ENDEOF','EOF','ENDEOF')
        
        # 智能判断变量
        if (self.current_char not in varcharlist) and len(self.current_word) > 1:
            self.current_token = Token(self.current_word[:-1],'var',None)
            self.current_word = ''
            self.position -= 1
            self.lineposition -= 1
            return self.current_token
        
        if self.isnum(self.current_word):   # 多位数字
            linestring = self.code.split('\n')[self.line][self.lineposition:]
            for i in integer_replacelist:
                linestring = linestring.replace(i,' ')
            linestring = linestring.split()[0]
            if '.' in linestring:
                try:
                    token = Token('floating','float',float(linestring))
                except:
                    self.error('浮点数'+linestring+'不正确')
            else:
                token = Token('integer','int',int(linestring))
            self.position += len(linestring) - 1
            self.lineposition += len(linestring) - 1
            self.current_word = ''
            return token
        
        if self.current_word.isdigit():  # 一位数字
            token = Token('integer','int',int(self.current_word))
            self.current_word = ''
            return token
        
        if self.current_word in token_dict:  # 特定符号
            near_char = self.current_word + self.get_near()
            if near_char in token_dict:
                self.current_word = near_char
                self.position += 1
                self.lineposition += 1
            else:     # 特殊处理
                if self.current_word == ' ':   # 最重要的语法：空格~
                    if (not self.token_stack) or self.token_stack[-1].name in ['\n',' ','=','}']:   # 跳过重复无用空格
                        self.current_word = ''
                        return self.get_next_token()
                    self.current_word = ''
                    return Token(' ','space',' ')
                elif self.current_word == '=':   # 变量赋值
                    if self.token_stack and self.token_stack[-1].name == ' ':   # 删除无用空格
                        self.token_stack = self.token_stack[:-1]
                    self.current_word = ''
                    return Token('=','symbol','=')
                elif self.current_word == '{':
                    if self.token_stack and self.token_stack[-1].name == ' ':   # 删除无用空格
                        self.token_stack = self.token_stack[:-1]
                    self.current_word = ''
                    return Token('{','symbol','{')
            
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
            self.current_word = ''
            return token
        
        if (self.current_word in namespace) and (self.get_near() not in varcharlist):   # 使用命名空间中的statement
            # if '=' not in self.code.split('\n')[self.line][self.lineposition:]:   # 如果不是赋值(=不在右侧)，就转化
            value = namespace[self.current_word]
            token = Token(self.current_word,'var',value[2])
            self.current_word = ''
            return token
        
        return self.get_next_token()
    
    def convert_var(self,var):
        varinfo = namespace[var.name]
        var.name = varinfo[0]
        var.tp = varinfo[1]
        var.value = varinfo[2]
        return var
    
    def calc_unary(self,name,expression):   # 一元运算
        if expression.name in namespace:
            expression = self.convert_var(expression)
        if name == '+':
            return (+expression, 'integer', 'int')
        if name == '-':
            return (-expression, 'integer', 'int')
        if name == '~':
            return (~expression, 'integer', 'int')
    
    def calc_binary(self,name,left,right):   # 二元运算
        global namespace
        if name == '=':
            if left.name == right.name == ' ':
                return
            if left.name[0].isdigit():
                self.error('变量名不能以数字开头')
            if not left.name.isascii():
                self.error('变量名不能含有非ascii字符')
            if right.name in namespace:
                namespace[left.name] = namespace[right.name]
                return
            namespace[left.name] = (right.name,right.tp,right.value)
            return
        if left.name in namespace:
            left = self.convert_var(left)
        if right.name in namespace:
            right = self.convert_var(right)
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
        else:
            self.error('解释器接收符号异常')
        tp = str(type(result))[8:-2]
        if tp == 'int':
            name = 'integer'
        elif tp == 'float':
            name = 'floating'
            result = round(result,15)
        elif tp == 'bool':
            name = 'bool'
        return (result,name,tp)
    
    def calc_ternary(self,name,expr1,expr2,expr3):   # 三元运算
        pass
    
    def leftconnect(self,stack,level):  # 左结合
        token = -1
        while token < len(stack) - 1:
            token += 1
            tn = stack[token].name
            if tn in operatordict:
                if (level in operatordict[tn]):
                    left = stack[token-1]
                    right = stack[token+1]
                    while left.tp is 'space':
                        del stack[token-1]
                        token -= 1
                        left = stack[token-1]
                        right = stack[token+1]
                    while right.tp is 'space':
                        del stack[token+1]
                        left = stack[token-1]
                        right = stack[token+1]
                    result = self.calc_binary(tn,left,right)
                    stack[token].value, stack[token].name, stack[token].tp = result
                    stack.remove(left)
                    stack.remove(right)
                    token -= 1
        return stack
    
    def visit(self,stack):
        if stack == []:
            return []
        
        token = -1
        leftstack = None   # 执行后拼接左右栈为新栈
        rightstack = None
        condition_startposition = None
        block_startposition = None
        braceinside = 0
        did = False  # 是否执行过了
        while token < len(stack) - 1:    # 分支 左结合
            token += 1
            tn = stack[token].name
            if tn == 'if':
                did = False
                condition_startposition = token + 2
            elif tn == 'elif':
                condition_startposition = token + 2
            elif tn == 'else':
                condition_startposition = 'ELSE CON'
            elif tn == '{':
                if leftstack is None:
                    if type(condition_startposition) == int:
                        leftstack = stack[:condition_startposition-1]
                    else:
                        leftstack = stack[:token]
                braceinside += 1
                if braceinside == 1:    # 是最外层大括号{
                    block_startposition = token + 1
                    if did:    # 执行过了后面的直接跳过
                        continue
                    if condition_startposition == 'ELSE CON':    # 是else就直接执行
                        condition = True
                        continue
                    condition = stack[condition_startposition:token]
                    condition = self.visit(condition)[0]
                    if condition.name in namespace:
                        condition = self.convert_var(condition)
                    condition = condition.value
            elif tn == '}':
                rightstack = stack[token+1:]
                braceinside -= 1
                if braceinside == 0:    # 是最外层大括号}
                    if did:
                        continue
                    if condition:
                        blockcode = stack[block_startposition:token]
                        # print(blockcode)
                        self.exprblock(blockcode)
                        did = True
        if leftstack and rightstack:
            stack = leftstack + rightstack
        # print('\033[1;32m',stack,'\033[1;33m',leftstack,rightstack,'\033[0m')
        
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
                if (9 in operatordict[tn]):
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
                if (8 in operatordict[tn]):
                    left = stack[token-1]
                    right = stack[token+1]
                    while left.tp is 'space':
                        del stack[token-1]
                        token -= 1
                        left = stack[token-1]
                        right = stack[token+1]
                    while right.tp is 'space':
                        del stack[token+1]
                        left = stack[token-1]
                        right = stack[token+1]
                    if left.tp == 'operator':
                        result = self.calc_unary(tn,right)
                        stack[token].value, stack[token].name, stack[token].tp = result
                        stack.remove(right)
        
        token = len(stack)   # 幂运算 右结合
        while token > 0:
            token -= 1
            tn = stack[token].name
            if tn in operatordict:
                if (7 in operatordict[tn]):
                    left = stack[token-1]
                    while left.tp is 'space':
                        del stack[token-1]
                        token -= 1
                        left = stack[token-1]
                    right = stack[token+1]
                    result = self.calc_binary(tn,left,right)
                    stack[token].value, stack[token].name, stack[token].tp = result
                    stack.remove(left)
                    stack.remove(right)
                    # 右结合不用改索引
        
        # 常规式左结合
        stack = self.leftconnect(stack,6)   # 乘 除 取模 整除 左结合
        stack = self.leftconnect(stack,5)   # 加 减 左结合
        stack = self.leftconnect(stack,4)   # 左移 右移 左结合
        stack = self.leftconnect(stack,3)   # 大于 小于 大于等于 小于等于 左结合
        stack = self.leftconnect(stack,2)   # 等于 不等于 左结合
        
        token = -1   # 变量 左结合
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
        self.exprblock(self.token_stack)
    
    def run(self):
        self.expr()

code = '''
a = true (c=null)
b d = a+a c
a = 1
()()()()()()()()()()()()()()()()e=1+1
()()f((())())=(())e()(())(((()()(())((())))())())(()())+(())e()()()
age = 3 if false {
    age=0
} elif false {
    age=1
} else {
    if age == 1{
        age = 2
    }
    else {
        age=age+10
    }
}
'''

code2 = '''
a = 1
if false {
    a = 666
}
elif true {

    if false {
        a = 2
    } elif true{
        a = 3
    } else {
        a = 4
    }

}
'''

interpreter = Interpreter(code=code)
interpreter.run()
print(namespace)
print('''
ij重大版本:build 300
这是一个里程碑式的进步，实现了{}的codeblock和if-elif-else控制流。没有ast和节点，没有之一！
经过上百次的测试盒实验，堆成山的样例，终于全部得到的希望的结果！
完美解决if-block控制流编程耗时超过40多个小时，我的肝啊！好用三连。
打开改编可以学习

目录:
root
 |\033[1;34m-->main.py 约700行 主程序\033[0m
 |-log.py 开发日志
 |\033[1;32m-设计流程图.jpg 流程图片\033[0m
 |-sf.py 删除无用空行的代码(压缩空行，剩下只有300行了)

谢谢观看！
''')
...
...
...