from SimplyVector import SimplyVector 
from SimplyTransform import SimplyTransform
from SimplyWorld import SimplyWorld 
import SimplyMath as fm
import math
from SimplyAABB import SimplyAABB

SimplyWorld = SimplyWorld()

Circle = "Circle"
Box = "Box"
def CreateBoxVertices(width,height):#获得box的顶点
    left = -width /2
    right = left + width
    bottom = - height /2
    top = bottom + height

    vertices  = [SimplyVector(left,top),SimplyVector(right,top),SimplyVector(right,bottom),SimplyVector(left,bottom)]
    return vertices

class SimplyBody:
    def __init__(self, Mass ,Density ,Restitution ,Area ,IsStatic,
                Radius, width,height,ShapeType,RotationalInertia,vertices,InherentStaticFriction,InherentDynamicFriction):#Position为SimplyVector
        
        self.Position =  SimplyVector(0,0) # 位置向量x
        self.LinearVelocity = SimplyVector(0,0)  # 线速度向量m/s
        self.angle = 0  # 角度
        self.AngularVelocity = 0  # 角速度rad/s

        self.Mass = Mass  # 质量kg
        self.InvMass = 1/Mass if Mass > 0 else 0
        self.Density = Density  # 密度g/cm^3
        self.Restitution = Restitution  # 恢复系数
        self.Area = Area  # 面积
        self.Radius = Radius  # 半径m
        self.width = width  # 宽m
        self.height = height  # 高m
        self.ShapeType = ShapeType # 形状类型str
        self.Force = SimplyVector(0,0)
        if InherentDynamicFriction<InherentStaticFriction:
            self.InherentStaticFriction =InherentStaticFriction
            self.InherentDynamicFriction = InherentDynamicFriction
        else:
            raise Exception("静摩擦力必须大于滑动摩擦力")


        self.IsStatic = IsStatic  # 是否完全静止——理想情况下完全静止的物体（类似于以太的效果）
        self.RotationalInertia = RotationalInertia
        self.InvRotationalInertia = 1/RotationalInertia if RotationalInertia > 0 else 0
        
        self.transformUpdateRequired = False#转换请求
        self.aabb=[]
        self.aabbUpdateRequired = False

        if  self.ShapeType == Box:#只有Box才有顶线
            self.vertices = vertices#矩形的顶点向量集合
            self.transformedVertices = []#Fv类型的列表
        else :
            self.vertices = None
            self.transformedVertices =None

        self.transformUpdateRequired =True
        self.aabbUpdateRequired =True

    def GetTransformedVertices(self):
        #获得转换坐标后的box的顶点坐标
        if self.transformUpdateRequired:
            transfrom = SimplyTransform(self.Position,self.angle)
            for i in range(len(self.vertices)):
                v = self.vertices[i]
                if len(self.transformedVertices) == len(self.vertices):#判断如果超出了列表长度则弹出第一个元素
                    self.transformedVertices.pop(0)
                self.transformedVertices.append(SimplyVector.transform(v,transfrom))
        self.transformUpdateRequired = False
        return self.transformedVertices
    
    def GetAABB(self):
        if self.aabbUpdateRequired:
            minX = float("inf")
            minY = float("inf")
            maxX = float("-inf")
            maxY = float("-inf")
            if self.ShapeType == Box:
                self.transformUpdateRequired = True
                vertices = self.GetTransformedVertices()
                for i in vertices:
                    if i.x<minX:
                        minX = i.x
                    if i.x>maxX:
                        maxX = i.x
                    if i.y<minY:
                        minY = i.y
                    if i.y>maxY:
                        maxY = i.y
            elif self.ShapeType == Circle:
                minX = self.Position.x-self.Radius
                minY = self.Position.y-self.Radius
                maxX = self.Position.x+self.Radius
                maxY = self.Position.y+self.Radius
            else :
                raise Exception("Unknown Shapetype")
            self.aabb = SimplyAABB(minX,minY,maxX,maxY)
        self.aabbUpdateRequired =False
        return self.aabb 

    def AddForce(self,amount):
        self.Force = amount
        
    def Step(self,time,iteration):
        if self.IsStatic:
            return
        time /= iteration
        self.LinearVelocity += SimplyWorld.gravity *time
        self.Position +=self.LinearVelocity *time
        self.angle += self.AngularVelocity *time
        self.Force = SimplyVector(0,0)
        self.aabbUpdateRequired =True
        self.transformUpdateRequired = True

    def Move(self,amount):#amount为Fv
        self.Position +=  amount#使用速度向量来改变物理位置
        self.transformUpdateRequired =True
        self.aabbUpdateRequired =True

    def MoveTo(self,Position):
        self.Position = Position
        self.transformUpdateRequired =True
        self.aabbUpdateRequired =True


    def Rotate(self,amount):#改变角速度
        self.angle += amount
        self.transformUpdateRequired=True
        self.aabbUpdateRequired =True

    def RotateTo(self,angle):
        self.angle = angle
        self.transformUpdateRequired=True
        self.aabbUpdateRequired =True


    def CreateCircleBody(Radius,Density,IsStatic,Restitution,InherentStaticFriction,InherentDynamicFriction):
        Area = math.pi*Radius**2#算面积

        #判断创建的Circle是否满足Fw的限制
        if Area <SimplyWorld.MinBodySize:
            raise ValueError
        if Area >SimplyWorld.MaxBodySize:
            raise ValueError
        if Density <SimplyWorld.MinDensity:
            raise ValueError
        if Density >SimplyWorld.MaxDensity:
            raise ValueError
        
        Restitution = fm.clamp(Restitution,0,1)#钳位恢复系数
        Mass = 0
        RotationalInertia = 0

        if not IsStatic:
            Mass = Area*Density*100#算质量
            RotationalInertia = (1/12)*Mass*Radius*Radius

        body = SimplyBody( Mass ,Density ,Restitution ,Area ,IsStatic,
                  Radius, 0,0,"Circle",RotationalInertia,None,InherentStaticFriction,InherentDynamicFriction)#创建对象
        return True,body,"Circle"#返回创建成功，SimplyBody对象，ShapeType
        
    def CreateBoxBody(width,height,Density,IsStatic,Restitution,InherentStaticFriction,InherentDynamicFriction):
        Area = width*height
        if Area < SimplyWorld.MinBodySize:
            raise ValueError
        if Area > SimplyWorld.MaxBodySize:
            raise ValueError
        if Density < SimplyWorld.MinDensity:
            raise ValueError
        if Density > SimplyWorld.MaxDensity:
            raise ValueError
        Restitution = fm.clamp(Restitution,0,1)
        Mass = 0
        RotationalInertia = 0

        if not IsStatic:
            Mass = Area*Density*100
            RotationalInertia = (1/12)*Mass*(width*width+height*height)

        vertices = CreateBoxVertices(width,height)
        body = SimplyBody( Mass ,Density ,Restitution ,Area ,IsStatic,
                  0, width,height,"Box",RotationalInertia,vertices,InherentStaticFriction,InherentDynamicFriction)
        return True,body,"Box"