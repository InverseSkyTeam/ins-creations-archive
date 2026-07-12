import random,math,numpy,sympy

mpt = print
mipt = input

oldmath = math
hello = '\033[1;32m欢迎启动逆天工作室-小轩-jhx.mathadd库!这里能更简洁地进行数学运算!版本:1.8.9!'

# 故意数形结合出一条美丽的曲线
simple_value = {
    'h':100,
    'k':1000,
    'w':10000,
    'm':1000000,
    'b':1000000000,
    't':1000000000000,
    'h':1000000000000000,
    '##q':1000000000000000000,       # 留给数学的符号不多了，我们在不常用的前面加点符号。
    '##s':1000000000000000000000000,
    '##n':1000000000000000000000000000000,
    '##googol':10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,   # 10^100
    '##googolchime':'10^1000',    # 超大数据只能用字符串了
    '##trial':'10^10^10',
    '##max':'Ω',
    '|||':'数学烧香'    # 彩蛋
}

# 打招呼
def do_hello(type_='pt'):
    if type_ == 'pt':
        print(hello)
    else:
        return hello

def x2(value,b=2):
    if type(value) == int or type(value) == str:
        return value * b
    else:
        for i in value:
            value[value.index(i)] = i * b
        return value

# 简易运算器
def simple_calculator(formula):
    return eval(formula.replace('[','(').replace(']',')').replace('{','(').replace('}',')').replace('%','/100').replace('mod','%'))

def randmath(start=-11,end=11):
    return random.randint(start,end)

def bigdata_change(n,tp='str'):
    if tp == 'int':
        try:
            return simple_value[n]
        except:
            pass
    else:
        for i in simple_value:
            if simple_value[i] == n:
                return i
    return 'cannot find your data to change'

# 质数（素数）判断
def prime_number_is(i):
    if i < 2:
        return '不是质数或合数'
    if i == 2:
        return '质数'
    if i % 2 == 0:
        return '合数'
    for j in range(3,i):
        if i % j == 0 :
            return '合数'
    else:
        return '质数'
    return '不是质数或合数'

# 输出一个数以内的所有质数
def prime_number_list(i):
    if i <= 2:
        return '无意义的计算'
    l = [2,] + [x for x in range(3,i,2) if prime_number_is(x)=='质数']
    return l

# 一个数的所有因数
def one_all_factor(n):
    return [i for i in range(1,n+1) if n % i == 0]

# 最大公因(约)数
def max_factor(n1,n2):
    small = min([n1,n2])
    for i in range(1,small+1):
        if n1 % i == 0 and n2 % i == 0:
            n = i
    return n
def quick_mf(a,b):
    while True:
        if a % b == 0:
            return b
        else:
            a,b = b,a%b

# 最小公倍数
def min_multi(n1,n2):
    n = quick_mf(n1,n2)
    n = int(n1*n2/n)
    return n

# 所有公因数
def all_factor(n1,n2):
    l = []
    small = min([n1,n2])
    for i in range(1,small+1):
        if n1 % i == 0 and n2 % i == 0:
            l.append(i)
    return l

# 分解质因数
def cal_decomposition(n):
    printlist = ''
    x = n
    while n>1:
        for i in range(2,n+1):
            if n % i == 0:
                n=int(n/i)
                if n == 1:
                    printlist += str(i)
                else:
                    printlist += str(i)
                    printlist += '*'
                break
    return str(x)+' = '+printlist

# 给方程加上*号，如2x+3y转换成2*x+3*y
def addmulti(text):
    letterlist = [chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]+['(','[','{'] # A-Z,a-z代数字母的ASCLL符号转译
    symlist = ['+','-','*','/','%','^','(','[','{']
    text = list(text) + ['' for i in range(5)]
    x = -1
    for i in text:
        x += 1
        try:
            if (i not in symlist) and (text[x+1] in letterlist):
                text.insert(x+1,'*')
        except IndexError:
            break
    text = ''.join(text)
    text = \
    text.replace('s*q*r*t','sqrt') \
        .replace('s*i*n','sin') \
        .replace('c*o*s','cos') \
        .replace('t*a*n','tan') \
        .replace('c*o*t','cot') \
        .replace('m*o*d','mod') \
        .replace('l*o*g','log') \
        .replace('e*x*p','exp')
    return text

# 列表每项的乘积
def multi_list(l):
    x = 1
    for i in l:
        x *= i
    return x

# 马青公式求π
def pi(digits=2,fd=10):
    '''
    求π
    函数用法：pi(digits = 整数)
    digits参数可以不填，默认值2位
    digits是计算小数的位数
    fd参数可以不填，默认值10
    fd是计算精确度（10已经完全足够了）
    '''
    try:
        digits = int(digits)
    except:
        return 'error dight value'
    w = digits + fd
    b = 10 ** w
    x1 = b * 4 // 5
    x2 = b // -239
    the_sum = x1 + x2
    digits *= 2
    for i in range(3,digits,2):
        x1 //= -25
        x2 //= -57121
        x = (x1+x2) // i
        the_sum += x
    pix = the_sum*4
    pix //= 10**fd
    pil = str(pix)
    pif = pil[0]+str(".")+pil[1:len(pil)]
    return pif
Pi2 = pi()
Pi18 = pi(18)
Pi100 = pi(digits=100)
Pi = sympy.pi

# 三角函数，注意参数是弧度不是角度
class triangle(object):
    '''三角函数类，注意参数是弧度不是角度'''
    @classmethod
    def sin(cls,data):
        return round(math.sin(data),4)
    @classmethod
    def cos(cls,data):
        return round(math.cos(data),4)
    @classmethod
    def tan(cls,data):
        return round(math.tan(data),4)
    @classmethod
    def cot(cls,data):
        return round(math.cot(data),4)

# 求和
def sigma(formula,start=1,end=10):
    '''
    sigma ∑算法
    函数用法：sigma(formula,start=起始值,end=终结值)
    参数列表：
    1 formula右侧算式  默认值 无  填写类型 字符串
    2 start底下  默认值 1
    3 end顶上  默认值 10
    地位图
       end
        ∑formula
    i = start
    '''
    formula_list = []
    for i in range(start,end+1):
        formula_list.append(eval(formula.replace('i',str(i))))
    return sum(formula_list)

# 求积
def multi_pi(formula,start=1,end=10):
    '''
    同simga
    '''
    formula_list = []
    for i in range(start,end+1):
        formula_list.append(eval(formula.replace('i',str(i))))
    return multi_list(formula_list)

# 阶乘
def factorial(data):
    '''
    阶乘 !算法
    函数用法：factorial(data=整数)
    参数：
    data整数 无默认值
    返回值：data!
    data尽量不要太大(<2000)
    '''
    if data <= 20000:
        return math.factorial(int(data))
    else:
        print('\033[1;33m温馨提示：不要把数值设定太大，对你的计算机不好。它无法很好地计算。并且此结果对你的研究与代码不一定有很大帮助。\033[0m')
        if input('是否终止此程序？输入是或否') == '是':
            exit()
        else:
            return '程序跳过代码继续运行。'

# 等差数列
def sum_seq(start=1,end=100,step=1,special=0):
    '''
    sum_seq 等差数列 高斯算法 梯形算法
    函数用法：sum_seq(start=起始值,end=终结值,step=间隔值,special=特殊值)
    参数列表：
    1 start首项  默认值 1
    2 end末项  默认值 100
    3 step间隔  默认值 1
    4 special特殊值，每项需要加上的数，可以为负数  默认值 0
    '''
    the_list = range(start,end+1,step)
    return sum(the_list)+len(the_list)*special

# 等比数列
def sum_gseq(n=10,step=2):
    '''
    sum_gseq 等比数列 小轩算法
    函数用法：sum_gseq(n=项数,step=每项之间的比值)
    参数列表：
    1 n项数  默认值 10
    2 step比值  默认值 2
    建议9<n<1501,1<step<16
    '''
    return sum([step**i for i in range(n)])

# 把一个大数改写成尾数是“万”“亿”“兆”的数字
def change_large_number(n=10000000,word='亿',r=1):
    if word == '万':
        return str(round(n/10000,r)) + word
    elif word == '亿':
        return str(round(n/10000000,r)) + word
    elif word == '兆':
        return str(round(n/10000000000,r)) + word
    elif word == '吉':
        return str(round(n/10000000000000,r)) + word
    elif word == '太':
        return str(round(n/10000000000000000,r)) + word
    elif word == '拍':
        return str(round(n/10000000000000000000,r)) + word
    elif word == '艾':
        return str(round(n/10000000000000000000000,r)) + word
    elif word == '泽':
        return str(round(n/10000000000000000000000000,r)) + word
    elif word == '尧':
        return str(round(n/10000000000000000000000000000,r)) + word
    elif '1e+' in word:
        return str(round(eval('n/'+word),r)) + '*' + word
    else:
        return '描述不够准确'

# 求F(x)，(2^x)
def F2(x):
    return 2 ** x

# (约数)四舍五入、去尾法、进一法
def rd(x,d,a='四舍五入'):
    if a == '四舍五入':
        return round(x,d)
    elif a == '去尾法':
        if int(x) == x:
            return x
        else:
            return int(x)-1
    else:
        return int(x)

# 数学趣谈
def math_interesting_talk():
    print('如果每天原地踏步，那么1年你是1^365.25= 1')
    print('如果每天进步一点点，那么1年你是1.01^365.25=',1.01**365.25)
    print('如果每天努力进步，那么1年你是1.1^365.25=',1.1**365.25)
    print('如果每天牛逼，那么1年你是2^365.25=',2**365.25)
    print('如果每天逆天，那么1周你是111^30',111**30)
    print('如果每天逆天并开心，那么1周你是666^30',666**30)
    print('如果每天退步一点点，那么1年你是0.99^365.25=',0.99**365.25)
    print('如果每天总是退步，那么1年你是0.5^365.25=',0.5**365.25)
    print('如果每天垃圾放水，那么1周你是0.01^30=',0.01**30)
    print('所以，让我们提升自己吧！')

# 鸡兔同笼
def chicken_and_rabbit(heads,feet,rabbit_feet=4,chicken_feet=2):
    heads = str(int(heads))
    feet = str(int(feet))
    rabbit_feet = str(rabbit_feet)
    chicken_feet = str(chicken_feet)
    rabbit_method = '兔子:('+feet+'-'+chicken_feet+' * '+heads+') / ('+rabbit_feet+' - '+chicken_feet+')'
    rabbit = str(int(eval(rabbit_method.split(':')[1])))
    chicken_method = '鸡:'+heads+' - '+rabbit
    chicken = str(int(eval(chicken_method.split(':')[1])))
    rabbit_method += ' = '+rabbit
    chicken_method += ' = '+chicken
    return [rabbit,chicken,rabbit_method,chicken_method]

# 数列类
class Seq(object):
    def __init__(self,sequence=None):
        self.sequence = sequence
        self.fibonacclist = [1,1]
        self.l = []
    def fibonacc(self,begin=1,end=11):
        for self.i in range(begin+end):
            self.fibonacclist.append(self.fibonacclist[-2]+self.fibonacclist[-1])
        return self.fibonacclist[begin-1:end]
    def ap(self,begin=1,end=100,h=100):        # arithmetic progression
        return int((begin+end)*h/2)
    def gp(self,begin=1,end=10,ratio=2):       # geometric progression
        self.l.append(begin)
        for self.i in range(begin,end+1):
            self.l.append(self.l[-1]*ratio)
        return sum(self.l)
    def square_seq(self,start=1,end=10):
        if start == 1:
            return end*(end+1)*(2*end+1)/6
        else:
            return sum([i**2 for i in range(start,end+1)])
    def cubic_seq(self,start=1,end=10):
        if start == 1:
            return (end*(end+1)/2)**2
        else:
            return sum([i**3 for i in range(start,end+1)])
    def powers_seq(self,start=1,end=5,power=4):
        return sum([i**power for i in range(start,end+1)])

class GeometryCommandError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return str(self.msg)

class Geometry(object):
    def __init__(self,a=1,b=1,c=1,h=1,r=1,d=2,R=2,C=None,S=None,V=None,l=5,angle=360):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        self.r = r
        self.d = d
        self.R = R
        self.C = C
        self.S = S
        self.V = V
        self.l = l
        self.angle = angle
        self.imaginary_number = (0+1j)
        self.round_pi = 3.14
        self.right_angle = 90
        self.straight_angle = 180
        self.perigon = 360
        self.null_angle = 0
        self.zero = 0
        self.infinity = float('inf')
        self.nan = float('nan')
        self.syinf = sympy.oo
    
    # 正方形
    def square(self,question='S'):
        if question == 'C' or question == '周长':
            return ['C□=4a',str(self.a)+'*4',self.a*4]
        elif question == 'S' or question == '面积':
            return ['S□=a²',str(self.a)+'^2',self.a**2]
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效:未知问题'+str(question))
    
    # 长方形
    def rectangle(self,question='S'):
        if question == 'C' or question == '周长':
            return ['C▃ =2(a+b)','('+str(self.a)+'+'+str(self.b)+')*2',(self.a+self.b)*2]
        elif question == 'S' or question == '面积':
            return ['S▃ =ab',str(self.a)+'*'+str(self.b),self.a*self.b]
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效:未知问题'+str(question))
    
    # 平行四边形
    def parallelogram(self,question='S'):
        if question == 'C' or question == '周长':
            return ['C▱ =2(a+b)','('+str(self.a)+'+'+str(self.b)+')*2',(self.a+self.b)*2]
        elif question == 'S' or question == '面积':
            return ['S▱ =ah',str(self.a)+'*'+str(self.h),self.a*self.h]
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效:未知问题'+str(question))
    
    # 三角形
    def triangle(self,question='S'):
        if question == 'C' or question == '周长':
            return ['C△ =a+b+c',str(self.a)+'+'+str(self.b)+'+'+str(self.c),self.a+self.b+self.c]
        elif question == 'S' or question == '面积':
            return ['S△ =ah/2',str(self.a)+'*'+str(self.h)+'/2',self.a*self.h/2]
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效:未知问题'+str(question))
    
    # 梯形
    def trapezium(self,question='S'):
        if question == 'C' or question == '周长':
            return ['C梯=a+b+c+h',str(self.a)+'+'+str(self.b)+'+'+str(self.c)+'+'+str(self.h),self.a+self.b+self.c+self.h]
        elif question == 'S' or question == '面积':
            return ['S梯=(a+b)h/2','('+str(self.a)+'+'+str(self.b)+')*'+str(self.h)+'/2',(self.a+self.b)*self.h/2]
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效:未知问题'+str(question))
    
    # 圆
    def circle(self,question='S',know='r'):
        if question == 'C' or question == '周长':
            if know == 'r':
                return ['C○=2πr','2π*'+str(self.r),str(self.r*2)+'π']
            else:
                return ['C○=πd','π*'+str(self.d),str(self.d)+'π']
        elif question == 'S' or question == '面积':
            if know == 'r':
                return ['S○=πr²','π*'+str(self.r)+'²',str(self.r**2)+'π']
            else:
                return ['S○=π(d/2)²','π*('+str(self.d)+'/2)²',str((self.d/2)**2)+'π']
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效:未知问题'+str(question))
    
    # 环
    def ring(self):
        return ['S◎=π(R²-r²)','π*('+str(self.R)+'²-'+str(self.r)+'²)',str(self.R**2-self.r**2)+'π']
    
    # 椭圆
    def ellipse(self,question='S'):
        if question == 'L' or question == '周长':
            return ['L椭=2πb+4(a-b)','2π*'+str(self.b)+'+4*('+str(self.a)+'-'+str(self.b)+')',str(self.b*2)+'π+'+str((self.a-self.b)*4)]
        elif question == 'S' or question == '面积':
            return ['S椭=πab','π*'+str(self.a)+'*'+str(self.b),str(self.a*self.b)+'π']
        elif question == 'C':
            return '提示:你的意思是求椭圆周长吗?请用字母L表示周长'
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效:未知问题'+str(question))
    
    # 正方体
    def cube(self,question='V'):
        if question == 'C' or question == '棱长总和':
            return ['C正方体=12a','12*'+str(self.a),12*self.a]
        elif question == 'S' or question == '表面积':
            return ['S正方体=6a²','6*'+str(self.a)+'²',6*self.a**2]
        elif question == 'V' or question == '体积':
            return ['V正方体=a³',str(self.a)+'³',self.a**3]
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效')
    
    # 长方体
    def cuboid(self,question='V'):
        if question == 'C' or question == '棱长总和':
            return ['C长方体=4(a+b+h)','4*('+str(self.a)+'+'+str(self.b)+'+'+str(self.h)+')',4*(self.a+self.b+self.h)]
        elif question == 'S' or question == '表面积':
            return ['S长方体=2*(ab+ah+bh)','2*('+str(self.a)+'*'+str(self.b)+'+'+str(self.a)+'*'+str(self.h)+'+'+str(self.b)+'*'+str(self.h)+')',2*(self.a*self.b+self.a*self.h+self.b*self.h)]
        elif question == 'V' or question == '体积':
            return ['V长方体=abh',str(self.a)+'*'+str(self.b)+'*'+str(self.h),self.a*self.b*self.h]
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效')
    
    # 圆柱
    def cylinder(self,question='V'):
        if question == 'S' or question == '表面积':
            return ['S圆柱=πr²*2+2πrh','π*'+str(self.r)+'²*2+2*π*'+str(self.r)+'*'+str(self.h),str(self.r**2*2+2*self.r*self.h)+'π']
        elif question == 'V' or question == '体积':
            return ['V圆柱=πr²h','π*'+str(self.r)+'²*'+str(self.h),str(self.r**2*self.h)+'π']
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效')
    
    # 圆锥
    def cone(self,question='V'):
        if question == 'V' or question == '体积':
            return ['V圆锥=πr²h/3','1/3π*'+str(self.r)+'²*'+str(self.h),str(self.r**2*self.h/3)+'π']
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效')
    
    # 四棱锥
    def pyramid(self,question='V'):
        if question == 'V' or question == '体积':
            return ['V四棱锥=abh/3',str(self.a)+'*'+str(self.b)+'*'+str(self.h)+'/3',self.a*self.b*self.h/3]
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效')
    
    # 球
    def sphere(self,question='V'):
        if question == 'V' or question == '体积':
            return ['V球体=4/3*πr³','4/3*π*'+str(self.r)+'³',str(self.r**3*(4/3))+'π']
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效')
    
    # 勾股定理
    def triangle_pyth(self,question='c'):
        if question == 'c':
            return (self.a**2+self.b**2)**0.5
        elif question == 'b':
            return (self.c**2-self.a**2)**0.5
        elif question == 'a':
            return (self.c**2-self.b**2)**0.5
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效')
    
    # 复数信息
    def get_imaginary(self,i):
        return [i,i.real,i.imag]
    
    # 负角信息
    def negative_angle(self,angle=-30):
        return [angle,-angle,angle<0]
    
    # ∫
    def integrate_calc(self,function='x**2',begin=1,end=2):
        x = sympy.symbols("x")
        y = eval(function)
        return sympy.integrate(y,(x, float(begin), float(end)))
    
    # 极限lim(x→+0)1/x
    def lim(self,name='x',limit='0,+',formula='1/x'):
        exec(name+' = sympy.symbols(name)')
        formula = eval(formula)
        limit = limit.split(',')
        l = int(limit[0])
        ltype = limit[1]
        return sympy.limit(formula, name, l, ltype)
    
    # 方程
    def equation(self,formula='x+1=3-1',quesiton='x'):
        exec(quesiton+' = sympy.symbols(quesiton)')
        formula = formula.split('=')
        formula = sympy.Eq(eval(formula[0]),eval(formula[1]))
        return sympy.solveset(formula,quesiton,domain=sympy.S.Reals)

the_geometry = Geometry()

# 方差
def vari(l):
    return numpy.var(l)

# 集合处理
def assemblage(a1,a2,tp='交集'):
    if tp == '交集' or tp == '∩':
        a = a1&a2
        if a != set():
            return a
        else:
            return '∅'
    elif tp == '并集' or tp == '∪':
        a = a1|a2
        if a != set():
            return a
        else:
            return '∅'
    elif tp == '差集':
        a = a1-a2
        if a != set():
            return a
        else:
            return '∅'
    return False

# 竖式（乘法完成，加法未开发）
def vertical_type_calc(n1,n2,tp='*'):
    string = ''
    if n1 > n2:
        big = n1
        small = n2
    else:
        big = n2
        small = n1
    if tp == '*':
        
        zero = 0
        while str(big)[-1] == '0':
            big = int(str(big)[:-1])
            zero += 1
        while str(small)[-1] == '0':
            small = int(str(small)[:-1])
            zero += 1
        all_length = len(str(big))*2
        small_empty = (all_length-len(str(small))-1)*' '
        string += int(all_length/2)*' '+str(big)+'\n'
        string += '×'+small_empty+str(small)+'\n'
        string += '—'*all_length+'\n'
        x = -1
        for i in str(small)[::-1]:
            x += 1
            next_result = str(int(i)*big)
            if next_result != '0':
                string += (all_length-len(next_result)-x)*' '+next_result+'\n'
        string += '—'*all_length+'\n'
        total = str(big*small)
        string += (all_length-len(total))*' '+total+'\n'
        if zero != 0:
            string += total+'×10^'+str(zero)+'='+str(int(total)*10**zero)
    elif tp == '+':
        stringlist = []
        empty_length = len(str(big))-len(str(small))+2
        string += '  '+str(big)+'\n'
        string += '+ '+(empty_length-2)*' '+str(small)+'\n'
        string += '-'*(len(str(big))+2)+'\n'
        lib = list(str(big))[::-1]
        lis = list(str(small))[::-1]
        next_ = 0
        for i in range(len(lib)):
            try:
                ans = int(lib[i])+int(lis[i])+next_
            except:
                ans = int(lib[i])+next_
            if ans > 9:
                ans -= 10
                next_ = 1
            else:
                next_ = 0
            stringlist.append(ans)
        if next_ == 1:
            stringlist.append(1)
        for i in range(len(stringlist)):
            stringlist[i] = str(stringlist[i])
        stringlist = ''.join(stringlist[::-1])
        if len(stringlist) > len(str(big)):
            stringlist = ' '+stringlist
        else:
            stringlist = '  '+stringlist
        string += stringlist
    return string

def per_com(l=[3,2,1]): # Permutation and combination
    s = 1
    for i in l:
        s *= i
    return s

def multi_data(depth=9):
    return '\n'.join([' '.join('%d×%d=%d' % (x , y , x*y)   for x in range(1,y+1)) for y in range(1,depth+1)])

class Constant(object):
    def __init__(self):
        self.pi = sympy.pi
        self.e = sympy.E
        self.i = sympy.I
        self.zero = 0
    def log(self,a,n):
        return sympy.log(n,a)
    def printformat(self,f):
        sympy.pprint(f)
    def root(self,i,n):
        return sympy.root(n,i)
    def sin(self,x):
        return sympy.sin(x)
    def cos(self,x):
        return sympy.cos(x)
    def tan(self,x):
        return sympy.tan(x)
    def cot(self,x):
        return sympy.cot(x)
    def asin(self,x):
        return sympy.asin(x)
    def acos(self,x):
        return sympy.acos(x)
    def atan(self,x):
        return sympy.atan(x)

class LongFloat(object):
    def __init__(self,n=0):
        if float(n) < 0:
            raise Exception('无法计算负数')
        self.number = str(n)
        self.nlist = self.number.split('.')
        self.front_dot_site = len(self.nlist[0])
        self.dot_site = len(self.nlist[-1])
        self.digits = 10**self.dot_site
        self.bignumber = ''.join(self.nlist)
    def __str__(self):
        return str(self.number)
    def __int__(self):
        return int(round(float(self.number)))
    def __float__(self):
        return float(self.number)
    def calc(self,symbol='+',other=0):
        if symbol == '+':
            ob = int(other.bignumber)
            sb = int(self.bignumber)
            if self.digits > other.digits:
                d = self.dot_site
                ob *= 10**(self.dot_site-other.dot_site)
            elif self.digits < other.digits:
                d = other.dot_site
                sb *= 10**(other.dot_site-self.dot_site)
            else:
                d = self.dot_site
            total = str(ob+sb)
            totalfront = total[:-d] if total[:-d] else '0'
            total = totalfront+'.'+total[-d:]
            while total[-1] is '0':
                total = total[:-1]
            return LongFloat(total)
        if symbol == '-':
            ob = int(other.bignumber)
            sb = int(self.bignumber)
            if self.digits > other.digits:
                d = self.bignumber
                s = self.front_dot_site
                ob *= 10**(self.dot_site-other.dot_site)
            elif self.digits < other.digits:
                d = other.bignumber
                s = other.front_dot_site
                sb *= 10**(other.dot_site-self.dot_site)
            else:
                d = self.bignumber
                s = self.front_dot_site
            total = str(sb-ob)
            total_small = True if int(total) < 0 else False
            if total_small:
                total = str(ob-sb)
                if s == self.front_dot_site:
                    s = other.front_dot_site
                else:
                    s = self.front_dot_site
            total = (len(d)-len(total))*'0'+total
            total = total[:s] + '.' + total[s:]
            while total[0] is '0':
                total = total[1:]
            if total[0] == '.':
                total = '0' + total
            if total_small:
                total = '-' + total
            # total = total[0] + '.' + total[1:]
            return LongFloat(total)

'''
example:
f = LongFloat('14684987.011804780888047805438804780710280478780888047805438804780707808880478054388047807')
f2 = LongFloat('451052.22111118880478050118047808880478054388047807102804787808880478043871022')
# 普通计算             |麻烦、约数|  print(float(f)+float(f2))
# 使用jhx.mathadd库    |简捷、精确|  print(f.calc('+',f2))
# 普通计算             |减法的运算|  print(float(f)+float(f2))
# 使用jhx.mathadd库    |减法的运算|  print(f.calc('-',f2))
提示：正常情况下普通计算保留18位小数（不一定精确，前16位绝对精确），在高精度用途上才使用LongFloat类型，计算更慢，但精确度更高
'''

# 其他暂未开发
# 目前打算开发到此


# 作者：小轩|声明：著作权永久有效（50年后仍保有著作权） 
# ------------------------------------------------------------------------------------------------------------------------------------