import math,random

mpt = print
mipt = input

oldmath = math
hello = '\033[1;32m欢迎启动逆天工作室-小轩-jhx.mathadd库!这里能更简洁地进行数学运算!版本:1.1.14!22的11次方是'+str(22**11)+'厉害不\033[0m'

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

# 最小公倍数
def min_multi(n1,n2):
    n = max_factor(n1,n2)
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
Pi = pi()
Pi18 = pi(18)
Pi100 = pi(digits=100)

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

# 求和
def simga(formula,start=1,end=10):
    '''
    simga ∑算法
    函数用法：simga(formula,start=起始值,end=终结值)
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
    rabbit_method = '兔子:('+chicken_feet+' * '+heads+' - '+feet+') / ('+chicken_feet+' - '+rabbit_feet+')'
    rabbit = str(int(eval(rabbit_method.split(':')[1])))
    chicken_method = '鸡:'+heads+' - '+rabbit
    chicken = str(int(eval(chicken_method.split(':')[1])))
    rabbit_method += ' = '+rabbit
    chicken_method += ' = '+chicken
    return [rabbit,chicken,rabbit_method,chicken_method]