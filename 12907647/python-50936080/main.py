# Firefly、storm、midlisp、speciallang
'''
吴宇航

回复了你的评论 :
这是个风(wind)雨(rain)交加的时代啊（

6,（小声bb：付起名老是喜欢跟我对着干，我写个dragonfly他要写butterfly，我写个wind他要写个rain，后来他写了tinylisp我就写了个microlisp、、、不过后来我是实在没力气写个classicallang跟他的newlang对着干了（
'''

import re

class Scanner:
    def __init__(self,code):
        self.code = code
        self.scanner = re.Scanner([
            (r'[0-9]+\.[0-9]*', lambda scanner, token: ['float',float(token)]),
            (r'\.[0-9]+', lambda scanner, token: ['float',float(token)]),
            (r'[0-9]+', lambda scanner, token: ['int',int(token)]),
            (r'[A-z][A-z0-9]*', lambda scanner, token: ['alpha',token]),
            (r'\(|\)|\[|\]|\{|\}', lambda scanner, token: ['paren',token]),
            (r'[>=<!]=', lambda scanner, token: ['op',token]),
            (r'[+-]|[*/%=|^&<>]', lambda scanner, token: ['op',token]),
            (r'\n+', lambda scanner, token: ['ln',token]),
            (r' +', lambda scanner, token: ['space',token]),
            (r'.', lambda scanner, token: ['unk',token]),
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
class Binary(Tree):...
class Unary(Tree):...
class Block(Tree):...
class If(Tree):...
class While(Tree):...
class Break(Tree):...
class Continue(Tree):...
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
        
        def block():
            if token != '{':
                return Block(stmt())
            eat('{')
            l = []
            while token not in ['','}']:
                s = stmt()
                if s != None:
                    l.append(s)
                if ttype == 'ln':
                    eat()
            eat('}')
            return Block(*l)
        
        def stmt():
            if token == 'if':
                eat()
                eat('(')
                condition = expr()
                eat(')')
                body = block()
                else_body = Empty()
                if token == 'else':
                    eat()
                    else_body = block()
                return If(condition,body,else_body)
            if token == 'while':
                eat()
                eat('(')
                condition = expr()
                eat(')')
                body = block()
                else_body = Empty()
                if token == 'else':
                    eat()
                    else_body = block()
                return While(condition,body,else_body)
            if token == 'break':
                eat()
                return Break()
            if token == 'continue':
                eat()
                return Continue()
            if token == '{':
                return block()
            e = expr()
            return e
        
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
                return Const(eat())
            if ttype == 'float':
                return Const(eat())
            if ttype == 'alpha':
                return Var(eat())
            if token == '(':
                eat()
                e = expr()
                eat(')')
                return e
            if token in ('+','-'):
                return Unary(eat(),factor())
        
        return block()
    
    def get_ast(self):
        return self.parse(self.stream)

class Interpreter:
    def __init__(self,ast):
        self.ast = ast
        self.global_scope = {}
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
    def run(self,tree,scope):
        tp = type(tree)
        if tp == Const:
            return tree[0]
        if tp == Var:
            return scope[tree[0]]
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
            for son in tree:
                v = self.run(son,scope)
                if type(v) in [Break, Continue]:
                    return v
            return
        if tp == Let:
            scope[tree[0][0]] = self.run(tree[1],scope)
            return scope[tree[0][0]]
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
        if tp == Break:
            return tree
        if tp == Continue:
            return tree
        if tp == Empty:
            return
            
    def execut(self):
        self.run(self.ast,self.global_scope)



awa = '''{
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
}'''

awa = '''{
    a = 1
    b = 0
    while (a<10){
        a = a + 1
        if (a%2) continue
        b = b + 1
    }
}
}'''

scanner = Scanner(awa)
stream, warn = scanner.scan()
# print(stream)

parser = Parser(stream)
ast = parser.get_ast()
print(ast)

print('\n\n结果:')

Interpreter = Interpreter(ast)
Interpreter.execut()
print(Interpreter.global_scope)

if warn:
    print('警告: 程序结构不完整: 开头或结尾没有{}表示域')