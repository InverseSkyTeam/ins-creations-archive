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
    
    # 正方形
    def square(self,question='S'):
        if question == 'C' or question == '周长':
            return ['C□=4a',str(self.a)+'*4',self.a*4]
        elif question == 'S' or question == '面积':
            return ['S□=a²',str(self.a)+'^2',self.a**2]
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效')
    
    # 长方形
    def rectangle(self,question='S'):
        if question == 'C' or question == '周长':
            return ['C▃ =2(a+b)','('+str(self.a)+'+'+str(self.b)+')*2',(self.a+self.b)*2]
        elif question == 'S' or question == '面积':
            return ['S▃ =ab',str(self.a)+'*'+str(self.b),self.a*self.b]
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效')
    
    # 平行四边形
    def parallelogram(self,question='S'):
        if question == 'C' or question == '周长':
            return ['C▱ =2(a+b)','('+str(self.a)+'+'+str(self.b)+')*2',(self.a+self.b)*2]
        elif question == 'S' or question == '面积':
            return ['S▱ =ah',str(self.a)+'*'+str(self.h),self.a*self.h]
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效')
    
    # 三角形
    def triangle(self,question='S'):
        if question == 'C' or question == '周长':
            return ['C△ =a+b+c',str(self.a)+'+'+str(self.b)+'+'+str(self.c),self.a+self.b+self.c]
        elif question == 'S' or question == '面积':
            return ['S△ =ah/2',str(self.a)+'*'+str(self.h)+'/2',self.a*self.h/2]
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效')
    
    # 梯形
    def trapezium(self,question='S'):
        if question == 'C' or question == '周长':
            return ['C梯=a+b+c+h',str(self.a)+'+'+str(self.b)+'+'+str(self.c)+'+'+str(self.h),self.a+self.b+self.c+self.h]
        elif question == 'S' or question == '面积':
            return ['S梯=(a+b)h/2','('+str(self.a)+'+'+str(self.b)+')*'+str(self.h)+'/2',(self.a+self.b)*self.h/2]
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效')
    
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
            raise GeometryCommandError('[Error_01]几何命令语法无效')
    
    # 环
    def ring(self):
        return ['S◎=π(R²-r²)','π*('+str(self.R)+'²-'+str(self.r)+'²)',str(self.R**2-self.r**2)+'π']
    
    # 椭圆
    def ellipse(self,question='S'):
        if question == 'L' or question == '周长':
            return ['L椭=2πb+4(a-b)','2π*'+str(self.b)+'+4*('+str(self.a)+'-'+str(self.b)+')',str(self.b*2)+'π+'+str((self.a-self.b)*4)]
        elif question == 'S' or question == '面积':
            return ['S椭=πab','π*'+str(self.a)+'*'+str(self.b),str(self.a*self.b)+'π']
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效')
    
    
t = Geometry(a=11,b=9)
t = t.ellipse('L')
print(t)