import sympy
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

t = Geometry()
t = t.equation('x**3=x+4')
print(t)