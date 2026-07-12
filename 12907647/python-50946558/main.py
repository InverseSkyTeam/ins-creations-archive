# notlisp、Firefly、storm、speciallang

import re

class Scanner:
    def __init__(self,code):
        self.code = code
        self.scanner = re.Scanner([
            (r'[0-9]+\.[0-9]*', lambda scanner, token: ['float',token]),
            (r'\.[0-9]+', lambda scanner, token: ['float',token]),
            (r'[0-9]+', lambda scanner, token: ['int',token]),
            (r'\\.', lambda scanner, token: ['escape',token]),
            ('["\']', lambda scanner, token: ['quoter',token]),
            (r'[A-Za-z_]\w*', lambda scanner, token: ['alpha',token]),
            (r'\(|\)|\[|\]|\{|\}', lambda scanner, token: ['paren',token]),
            (r',', lambda scanner, token: ['comma',token]),
            (r'[>=<!]=', lambda scanner, token: ['op',token]),
            (r'[+-]|[*/%=|^&<>]', lambda scanner, token: ['op',token]),
            (r'\n+', lambda scanner, token: ['ln',token]),
            (r' +', lambda scanner, token: ['space',token]),
            (r'.+', lambda scanner, token: ['unk',token]),
        ])
        self.warn = False
        while self.code[0] == '\n':
            self.code = self.code[1:]
        while self.code[-1] == '\n':
            self.code = self.code[:-1]
        if self.code[0] != '{':
            self.code = '{\n' + self.code
            self.warn = True
        if self.code[-1] != '}':
            self.code = self.code + '\n}'
            self.warn = True
    def scan(self):
        result, rest = self.scanner.scan(self.code)
        if rest: raise Exception(f'小丑吧，怎么解析不出来这代码！\n剩余:\n{rest}')
        return (result + [['EOF','']], self.warn)

class Tree:
    def __init__(self,*args):
        self.args=args
    def __getitem__(self,n):
        return self.args[n]
    def __str__(self):
        return type(self).__name__+"("+",".join(map(str,self.args))+")"
    __repr__=__str__
class Const(Tree):...
class Var(Tree):...
class Let(Tree):...
class Def(Tree):...
class NewFn(Tree):...
class Binary(Tree):...
class Unary(Tree):...
class Block(Tree):...
class PublicBlock(Tree):...
class If(Tree):...
class While(Tree):...
class Break(Tree):...
class Return(Tree):...
class Continue(Tree):...
class Call(Tree):...
class Empty(Tree):...

class Parser:
    def __init__(self,stream):
        self.stream = stream
    
    def get_prio(self,op):
        return {
            '*': 10, '/': 10, '%': 10, '//': 10,
            '+': 9, '-': 9,
            '>>': 8, '<<': 8,
            '==': 7, '!=': 7, '<': 7, '>': 7, '>=': 7, '<=': 7,
        }[op]
    
    def escape(self,e):
        return {
            r'\n': '\n',
            r'\r': '\r',
            r'\t': '\t',
            r'\v': '\v',
            r'\s': ' ',
            r'\a': '\a',
            r'\b': '\b',
            r'\f': '\f',
            r'\\': '\\',
            r'\"': '"',
            r"\'": "'",
        }[e]
    
    def parse(self,stream):
        p = 0
        ttype, token = stream[p]
        
        # 返回此并指向下
        def eat(ex=None):
            nonlocal ttype, token, stream, p
            if ex in [None,token]:
                this = token
                p += 1
                while stream[p][0] == 'space':
                    p += 1
                ttype, token = stream[p]
                return this
            raise Exception(f'不匹配的单词{token}')
        
        def block(public=False):
            if token != '{':
                if public:
                    return PublicBlock(stmt())
                return Block(stmt())
            eat('{')
            l = []
            while token != '}':
                s = stmt()
                if s != None:
                    l.append(s)
                if ttype == 'ln':
                    eat()
            eat('}')
            if public:
                return PublicBlock(*l)
            return Block(*l)
        
        def stmt():
            if token == 'if':
                eat()
                eat('(')
                condition = expr()
                eat(')')
                body = block(True)
                else_body = Empty()
                if token == 'else':
                    eat()
                    else_body = block(True)
                return If(condition,body,else_body)
            if token == 'while':
                eat()
                eat('(')
                condition = expr()
                eat(')')
                body = block(True)
                else_body = Empty()
                if token == 'else':
                    eat()
                    else_body = block(True)
                return While(condition,body,else_body)
            if token == 'return':
                eat()
                return Return(expr())
            if token == 'break':
                eat()
                return Break()
            if token == 'continue':
                eat()
                return Continue()
            if token == 'def':
                eat()
                name = eat()
                return Def(name,parse_fn())
            if token == '{':
                return block()
            e = expr()
            return e
        
        def parse_fn():    # 定义函数
            eat('(')
            if token == ')':
                param_list = []
            else:
                param_list = [eat()]
                while token == ',':
                    eat()
                    param_list.append(eat())
            eat(')')
            return NewFn(param_list,block())
        
        def expr():
            res = factor()
            if token in ['+','-','*','/','%','>','<','>=','<=','==','!=',]:
                res = Binary(eat(),res,factor())
                while token in ['+','-','*','/','%','>','<','>=','<=','==','!=',]:
                    op = eat()
                    fac = factor()
                    if self.get_prio(res[0]) > self.get_prio(op):
                        res=Binary(op,res,fac)
                    else:
                        res=Binary(res[0],res[1],Binary(op,res[2],fac))
            if token == '=':
                eat()
                if type(res) != Var:
                    raise Exception(f'不可以给非变量赋值！\n错误:{res}')
                res = Let(res,expr())
            return res
        
        def factor():
            if token == 'true':
                eat()
                return Const(True)
            if token == 'false':
                eat()
                return Const(False)
            if token == 'null':
                eat()
                return Const(None)
            if ttype == 'int':
                return Const(int(eat()))
            if ttype == 'float':
                return Const(float(eat()))
            if ttype == 'alpha':
                name = eat()
                if token == '(':     # call了函数
                    call_list = get_call_list()
                    return Call(name,call_list)
                return Var(name)     # 变量
            if token == '(':
                eat()
                e = expr()
                eat(')')
                return e
            if token in ['"',"'"]:
                string = get_string()
                return Const(string)
            if token in ('+','-'):
                return Unary(eat(),factor())
        
        # 获取字符串
        def get_string():
            q = eat()
            text = ''
            while token != q:         # 没有遇到下一个相同引号
                if ttype == 'escape':    # 需要转义
                    text += self.escape(eat())
                else:
                    text += eat()
            eat(q)
            return text
        
        # 获取参数列表
        def get_call_list():
            eat('(')
            l = []
            while token != ')':
                e = expr()
                l.append(e)
                if token == ',':
                    eat()
            eat(')')
            return l
        
        return block()
    
    def get_ast(self):
        return self.parse(self.stream)

class Fn:
    def __init__(self,param,body,closure):
        self.param, self.body, self.closure = param, body, closure
    def __call__(self,runner,*args):
        if len(args) != len(self.param):
            raise Exception('参数数量不匹配')
        ret = runner(self.body, self.closure + [dict(zip(self.param,args))])
        if ret == None:
            return None
        return ret[0]

class Interpreter:
    def __init__(self,ast):
        self.ast = ast
        self.global_scope = [{
            'out': print,
            'int': int,
            'float': float,
            'str': str,
            'len': len,
            'round': round,
            'pow': pow,
            'ord': ord,
            'chr': chr,
        }]
        self.dic_op_bin = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '%': lambda a, b: a % b,
            '==':lambda a, b: a == b,
            '!=':lambda a, b: a != b,
            '>': lambda a, b: a > b,
            '<': lambda a, b: a < b,
            '>=': lambda a, b: a >= b,
            '<=': lambda a, b: a <= b,
            '<<': lambda a, b: a << b,
            '>>': lambda a, b: a >> b,
            '&': lambda a, b: a & b,
            '|': lambda a, b: a | b,
            '^': lambda a, b: a ^ b,
        }
        self.dic_op_un = {
            '+': lambda expr: +expr,
            '-': lambda expr: -expr,
            '~': lambda expr: ~expr,
            # '!': lambda expr: not expr,
        }
    def get_var(self,name,scope):
        for level in reversed(scope):
            if name in level:
                return level[name]
        raise NameError(f'没有变量{name}')
    def run(self,tree,scope):
        tp = type(tree)
        if tp == Const:
            return tree[0]
        if tp == Var:
            return self.get_var(tree[0],scope)
        if tp == Unary:
            op = tree[0]
            expr = self.run(tree[1],scope)
            return self.dic_op_un[op](expr)
        if tp == Binary:
            op = tree[0]
            l = self.run(tree[1],scope)
            r = self.run(tree[2],scope)
            return self.dic_op_bin[op](l,r)
        if tp == Block:
            scope.append({})
            for son in tree:
                v = self.run(son,scope)
                if type(v) in [Return, Break, Continue]:
                    scope.pop(-1)
                    return v
            scope.pop(-1)
            return
        if tp == PublicBlock:
            for son in tree:
                v = self.run(son,scope)
                if type(v) in [Return, Break, Continue]:
                    return v
            return
        if tp == Let:
            scope[-1][tree[0][0]] = self.run(tree[1],scope)
            return scope[-1][tree[0][0]]
        if tp == NewFn:
            return Fn(tree[0],tree[1],scope)
        if tp == Def:
            scope[-1][tree[0]] = self.run(tree[1],scope)
            return
        if tp == If:
            if self.run(tree[0],scope):
                return self.run(tree[1],scope)
            return self.run(tree[2],scope)
        if tp == While:
            while self.run(tree[0],scope):
                v = self.run(tree[1],scope)
                if type(v) == Break:
                    break
                if type(v) == Continue:
                    continue
            else:
                return self.run(tree[2],scope)
            return
        if tp == Return:
            return Return(self.run(tree[0],scope))
        if tp == Break:
            return tree
        if tp == Continue:
            return tree
        if tp == Call:
            func = self.get_var(tree[0],scope)
            if type(func) == Fn:
                return func(self.run,*[self.run(t,scope) for t in tree[1]])
            return func(*[self.run(t,scope) for t in tree[1]])
        if tp == Empty:
            return
            
    def execut(self):
        self.run(self.ast,self.global_scope)



awa = r'''{
    {
        a=2
        while (a<5) {
            b=a
            a=a*b
        } else {
            c=a
            d=a+c
        }
        while (b<a){
            b = b + 1
            if (b==10) {
                e=true
                f=e*2
                if (f) if (e) {if (a) break}
            }
        }
        if (a-b>0) g=666
        text = text2 = (1.+-.1)*2*-3+(3+(3+((((b+c)))+3))+3)/(1+2)-1+1+3/3-(2+5)%2-true + 1 + true - false
        out(text,text2,text!=text2)
    }
    out('-'*40)
    {
        a = 1
        b = 0
        while (a < 10){
            a = a + 1
            if (a%2) continue
            b = b + 1
            out(a,b)
        }
        out(a,b)
    }
    out('-'*40)
    {
        a = 1
        def func(x,y,z) {
            a = a + x + y - z
            out(a-y)
        }
        func(2,1,false)
        out(a)
    }
    out('-'*40)
    {
        a=10
        out(pow(a,len(str(a))))
    }
    out('-'*40)
    {
        def a(x){
            x = x + 1
            if (x<10) {
                return b(x)
            }
            return x
        }
        def b(x){
            x = x + 2
            if (x<10) {
                return a(x)
            }
            return x
        }
        out(a(2))
    }
    out('-'*40)
    {
        def a(x){
            def b(x){
                out(x)
                return x+1
            }
            out(x)
            x = b(x)
            out(x)
            return x
        }
        out(a(1))
    }
    out('-'*40)
    {
        {{out("123\t12-\\3_h\nh")}}
    }
}'''

# awa = 'out("\\"")'

scanner = Scanner(awa)
stream, warn = scanner.scan()
# print(stream)

parser = Parser(stream)
ast = parser.get_ast()
# print(ast)

print('\n\n结果:')

Interpreter = Interpreter(ast)
Interpreter.execut()

if warn:
    print('警告: 程序结构不完整: 开头或结尾没有{}表示域')