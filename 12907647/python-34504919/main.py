# Error maker:
class GeometryCommandError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return str(self.msg)
# 

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
            return ['C△ =abc',str(self.a)+'+'+str(self.b)+'+'+str(self.c),(self.a+self.b+self.c)]
        elif question == 'S' or question == '面积':
            return ['S△ =ah/2',str(self.a)+'*'+str(self.h)+'/2',self.a*self.h/2]
        else:
            raise GeometryCommandError('[Error_01]几何命令语法无效')

# using[
print('Please input what you want to calc:\nsquare\nrectangle\nparallelogram\ntriangle')
text = input('to do >>')
a = input('Input the long of Edge A of it:\nYou can only type a number or "n" to continue\nnext>>')
b = input('Input the long of Edge B of it:\nYou can only type a number or "n" to continue\nnext>>')
c = input('Input the long of Edge C of it:\nYou can only type a number or "n" to continue\nnext>>')
h = input('Input the height of it:\nYou can only type a number or "n" to continue\nto do>>')
try:a=int(a)
except:pass
try:b=int(b)
except:pass
try:c=int(c)
except:pass
try:h=int(h)
except:pass
print('calc...>>to do it>>')
print('making Geometry CLASS /')
geo = Geometry(a=a,b=b,c=c,h=h)
print('OK /')
print('start calc it>>to do it>>')
print('calc......')
C = eval('geo.'+text+'()')
S = eval('geo.'+text+'("S")')
print('a:',a)
print('b:',b)
print('c:',c)
print('h:',h)
print('C:',C)
print('S:',S)
print('thank for your using!')
#]