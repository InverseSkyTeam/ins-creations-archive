class Input:
    def __init__(self,info):
        self.name = 'Input'
        self.info = bool(int(info))
    def get(self):
        return self.info

class Out:
    def __init__(self,last):
        self.name = 'Out'
        self.info = int(last.get())
    def output(self):
        print(self.info)
        return self.info

class Road:
    def __init__(self,last):
        self.name = 'Road'
        self.info = last.get()
    def get(self):
        return self.info

class Not:
    def __init__(self,last):
        self.name = 'Not'
        self.info = not last.get()
    def get(self):
        return self.info

class Or:
    def __init__(self,left,right):
        self.name = 'Or'
        self.info = left
        if self.info.get():
            self.newinfo = self.info.get()
        if Not(self.info).get():
            self.newinfo = right.get()
        self.info = self.newinfo
    def get(self):
        return self.info

class And:
    def __init__(self,left,right):
        self.name = 'And'
        self.left = Not(left)
        self.right = Not(right)
        self.info = Not(Or(self.left,self.right)).get()
    def get(self):
        return self.info

class XOR:
    def __init__(self,left,right):
        self.name = 'XOR'
        self._or = Or(left,right)
        self._and = Not(And(left,right))
        self.info = And(self._or,self._and).get()
    def get(self):
        return self.info

class XNOR:
    def __init__(self,left,right):
        self.name = 'XNOR'
        self.xor = XOR(left,right)
        self.info = Not(self.xor).get()
    def get(self):
        return self.info

def test_stream():
    print('开始测试')
    
    A = Input(1)
    B = Input(0)
    
    r1 = Road(A)
    r2 = Road(r1)
    r3 = Road(r2)
    o1 = Or(A,B)
    o2 = And(A,B)
    o3 = XOR(A,B)
    o4 = XNOR(A,B)
    
    O1 = Out(r3)
    _o1 = O1.output()
    O2 = Out(o1)
    _o2 = O2.output()
    O3 = Out(o2)
    _o3 = O3.output()
    O4 = Out(o3)
    _o4 = O4.output()
    O5 = Out(o4)
    _o5 = O5.output()
    
    if [_o1,_o2,_o3,_o4,_o5] == [1,1,0,1,0]:
        print('测试成功')
    print('-'*20)

test_stream()
print('二位二进制计算器：分别输入A1 A2 B1 B2（都是0或1，否则将会强制转为bool类型，可能报错），计算二进制数(A1A2)+(B1B2)，全过程仅使用逻辑运算。A1为A的2位，A2为A的个位。B1为B的2位，B2为B的个位。以上。\n')
A1 = Input(input('输入A1:'))
A2 = Input(input('输入A2:'))
B1 = Input(input('输入B1:'))
B2 = Input(input('输入B2:'))
O1 = O2 = O3 = None

R3 = XOR(A2,B2)
L1_1 = And(A2,B2)
L1_2 = XOR(A1,B1)
L1_3 = And(A1,B1)

R2 = XOR(L1_1,L1_2)
L2_1 = And(L1_1,L1_2)

R1 = XOR(L1_3,L2_1)

O1 = Out(R1)
O2 = Out(R2)
O3 = Out(R3)

o1 = O1.output()
o2 = O2.output()
o3 = O3.output()

print('-'*20)
print(f'{int(A1.info)}{int(A2.info)}+{int(B1.info)}{int(B2.info)}={o1}{o2}{o3}')