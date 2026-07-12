#Simplyvector

import math
VerySmallAmount = 0.0005
class SimplyVector:
    def __init__(self,x=0,y=0) :
        self.x = x
        self.y = y

    def __add__(self,other):#向量与向量的加法
        return  SimplyVector(self.x+other.x,self.y+other.y)
    
    def __sub__(self,other):#向量与向量的减法
        return  SimplyVector(self.x-other.x,self.y-other.y)
    
    def __mul__(self,s):#向量与标量的乘法
        return  SimplyVector(self.x*s,self.y*s)
    
    def __rmul__(self, s): # 反向乘法
        return SimplyVector(self.x * s, self.y * s)

    
    def __div__(self,s):#向量与标量的除法
        if s == 0:
            raise ZeroDivisionError("SimplyVector division by zero")
        return  SimplyVector(self.x/s,self.y/s)
    
    def __neg__(self):#取相反向量
        return SimplyVector(-self.x,-self.y)
    
    def dot(self,other):#向量点积
        return self.x*other.x + self.y*other.y
    
    def cross(self,other):#向量的叉乘
        return self.x*other.y-self.y*other.x
    
    def len(self):#向量的模长
        return math.sqrt(self.x**2+self.y**2)
    
    def abs(self):
        return SimplyVector(abs(self.x),abs(self.y))
    
    def distance(self,other):#两个向量的距离
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
    
    def __eq__(self,other):#判断两个向量是否相等
        if other != None:
            return self.x == other.x and self.y == other.y
        
    def normalize(self):#向量归一化
        length = self.len()
        return SimplyVector(self.x / length, self.y / length) if length != 0 else None
        
    def transform(Fvv,FtTransform):#向量旋转变换
        rx = FtTransform.cos * Fvv.x - FtTransform.sin*Fvv.y
        ry = FtTransform.sin * Fvv.x + FtTransform.cos*Fvv.y

        tx = rx + FtTransform.PositionX
        ty = ry + FtTransform.PositionY

        return SimplyVector(tx,ty)
    
    def LengthSquared(v):
        return v.x * v.x + v.y * v.y
    
    def DistanceSquared(a,b):
        dx = a.x - b.x
        dy = a.y - b.y
        return dx * dx + dy * dy; 

    def NearlyEqualFv(a,b):
        return SimplyVector.DistanceSquared(a,b)<VerySmallAmount*VerySmallAmount
    
    def NearlyEqual(a,b):
        return abs(a - b) < VerySmallAmount

    

