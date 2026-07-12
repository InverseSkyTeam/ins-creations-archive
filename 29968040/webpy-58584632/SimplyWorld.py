from SimplyVector import SimplyVector
from Collisions import Collisions
from SimplyMath import clamp
from SimplyManifold import SimplyManifold
Box = "Box"
Circle  = "Circle"

class SimplyWorld:
    def __init__(self):
        self.MinBodySize = 0.01*0.01 #m^2
        self.MaxBodySize = 64*64#m^2

        self.MinDensity = 0 #g/cm^3
        self.MaxDensity = 21.4 #g/cm^3

        self.MinIterations = 1
        self.MaxIteration = 32

        self.gravity = SimplyVector(0,9.8*15)
        self.bodyList =[]
        self.contactList = []
        self.ContactPointsList = []
        self.contactPairs = []

    def BodyCount(self):
        return len(self.bodyList)
    
    def AddBody(self,body):
        self.bodyList.append(body)
    
    def RemoveBody(self,body):
        return self.bodyList.remove(body)
    
    def GetBody(self,index):
        if index < 0 or index >= len(self.bodyList):
            return False,None
        
        body = self.bodyList[index]
        return True,body
    

    def Step(self,time,iterations):
        iterations  = clamp(iterations,self.MinIterations,self.MaxIteration)
        self.ContactPointsList =[]     
        for it in range(iterations):        
            self.contactPairs = []
            self.StepBodies(time,iterations)
            self.BroadPhase()
            self.NarrowPhase()


    def BroadPhase(self):
        for i in range(len(self.bodyList)): 
            bodyA = self.bodyList[i] 
            bodyA_aabb = bodyA.GetAABB()
            for j in range(len(self.bodyList)):
                if i==j: 
                    continue 
                bodyB = self.bodyList[j] 
                bodyB_aabb = bodyB.GetAABB()
                if bodyA.IsStatic and bodyB.IsStatic:
                    continue
                if not Collisions.IntersectAABBs(bodyA_aabb,bodyB_aabb):
                    continue
                self.contactPairs.append((i,j))
                

    def NarrowPhase(self):
        for i in range(len(self.contactPairs)):
            pair = self.contactPairs[i]
            bodyA = self.bodyList[pair[0]]
            bodyB = self.bodyList[pair[1]]
            CollisionOrNot,depth,normal = Collisions.Collide(bodyA,bodyB)
            if CollisionOrNot:
                SimplyWorld.SepareteBodies(bodyA,bodyB,normal*depth)
                contact1,contact2,contactCount = Collisions.FindContactPoints(bodyA,bodyB)    
                contact = SimplyManifold(bodyA,bodyB,normal,depth,contact1,contact2,contactCount)
                SimplyWorld.ResolveCollisionWithRotationAndFriction(contact)
            
    
    def StepBodies(self,time,iterations):
        for i in range(len(self.bodyList)):
                if not self.bodyList[i].IsStatic:
                    self.bodyList[i].Step(time,iterations)
        

    def SepareteBodies(bodyA,bodyB,mtv):
        if bodyA.IsStatic:
            bodyB.Move(mtv/ 2 )
        elif bodyB.IsStatic:
            bodyA.Move(-mtv/ 2 )
        else:
            bodyA.Move(-mtv / 2 )
            bodyB.Move(mtv/ 2 )

    # #公式来自https://www.chrishecker.com/Rigid_Body_Dynamics

    def ResolveCollisionWithRotationAndFriction(contact):
    # 解决碰撞并考虑旋转和摩擦力

        bodyA = contact.BodyA  # 碰撞的物体A
        bodyB = contact.BodyB  # 碰撞的物体B
        normal = contact.Normal  # 碰撞法线向量
        contact1 = contact.Contact1  # 碰撞点1
        contact2 = contact.Contact2  # 碰撞点2
        contactCount = contact.ContactCount  # 碰撞点数量

        e = min(bodyA.Restitution, bodyB.Restitution)  # 碰撞恢复系数

        sf = (bodyA.InherentStaticFriction + bodyB.InherentStaticFriction) * 0.5  # 静摩擦系数
        df = (bodyA.InherentDynamicFriction + bodyB.InherentDynamicFriction) * 0.5  # 动摩擦系数

        contactList = [contact1, contact2]  # 碰撞点列表

        frictionImpulseList = [SimplyVector(0,0)] * contactCount  # 摩擦冲量列表
        jList = [0,0]  # 冲量列表
        impulseList = [SimplyVector(0,0)] * contactCount  # 冲量列表
        raList = [SimplyVector(0,0)] * contactCount  # 碰撞点到物体A质心的向量列表
        rbList = [SimplyVector(0,0)] * contactCount  # 碰撞点到物体B质心的向量列表

        contactList[0] = contact1
        contactList[1] = contact2

        # 计算冲量
        for i in range(contactCount):
            ra = contactList[i] - bodyA.Position  # 碰撞点到物体A质心的向量
            rb = contactList[i] - bodyB.Position  # 碰撞点到物体B质心的向量

            raList[i] = ra
            rbList[i] = rb

            raPerp = SimplyVector(-ra.y, ra.x)  # ra向量的法向量
            rbPerp =  SimplyVector(-rb.y, rb.x)  # rb向量的法向量

            angularLinearVelocityA = raPerp * bodyA.AngularVelocity  # 物体A的角速度对raPerp的贡献
            angularLinearVelocityB = rbPerp * bodyB.AngularVelocity  # 物体B的角速度对rbPerp的贡献

            relativeVelocity = (bodyB.LinearVelocity + angularLinearVelocityB) - (bodyA.LinearVelocity + angularLinearVelocityA)  # 相对速度

            contactVelocityMag = SimplyVector.dot(relativeVelocity, normal)  # 相对速度在法线方向上的分量

            if contactVelocityMag > 0:
                continue

            raPerpDotN = SimplyVector.dot(raPerp, normal)  # raPerp向量与法线向量的点积
            rbPerpDotN = SimplyVector.dot(rbPerp, normal)  # rbPerp向量与法线向量的点积

            denom = bodyA.InvMass + bodyB.InvMass + (raPerpDotN * raPerpDotN) * bodyA.InvRotationalInertia + (rbPerpDotN * rbPerpDotN) * bodyB.InvRotationalInertia  # 冲量计算的分母

            j = -(1 + e) * contactVelocityMag / denom / contactCount  # 冲量大小

            jList[i] = j

            impulse = j * normal  # 冲量向量
            impulseList[i] = impulse

        # 应用冲量
        for i in range(contactCount):
            impulse = impulseList[i]
            ra = raList[i]
            rb = rbList[i]

            bodyA.LinearVelocity += -impulse * bodyA.InvMass  # 物体A线速度增量
            bodyA.AngularVelocity += -SimplyVector.cross(ra, impulse) * bodyA.InvRotationalInertia  # 物体A角速度增量
            bodyB.LinearVelocity += impulse * bodyB.InvMass  # 物体B线速度增量
            bodyB.AngularVelocity += SimplyVector.cross(rb, impulse) * bodyB.InvRotationalInertia#角速度增量

        for i in range(contactCount):
            ra = contactList[i] - bodyA.Position  # 碰撞点到物体A质心的向量
            rb = contactList[i] - bodyB.Position  # 碰撞点到物体B质心的向量

            raList[i] = ra
            rbList[i] = rb

            raPerp = SimplyVector(-ra.y, ra.x)  # ra向量的法向量
            rbPerp =  SimplyVector(-rb.y, rb.x)  # rb向量的法向量

            angularLinearVelocityA = raPerp * bodyA.AngularVelocity  # 物体A的角速度对raPerp的贡献
            angularLinearVelocityB = rbPerp * bodyB.AngularVelocity  # 物体B的角速度对rbPerp的贡献

            relativeVelocity = (bodyB.LinearVelocity + angularLinearVelocityB) - (bodyA.LinearVelocity + angularLinearVelocityA)  # 相对速度

            tangent = relativeVelocity - SimplyVector.dot(relativeVelocity, normal) * normal  # 切向方向
            if SimplyVector.NearlyEqualFv(tangent, SimplyVector(0,0)):
                continue
            else:
                tangent =  SimplyVector.normalize(tangent)  # 归一化切向向量

            raPerpDotT = SimplyVector.dot(raPerp, tangent)  # raPerp向量与切向向量的点积
            rbPerpDotT = SimplyVector.dot(rbPerp, tangent)  # rbPerp向量与切向向量的点积

            denom = bodyA.InvMass + bodyB.InvMass + (raPerpDotT * raPerpDotT) * bodyA.InvRotationalInertia + (rbPerpDotT * rbPerpDotT) * bodyB.InvRotationalInertia  # 冲量计算的分母

            jt = -SimplyVector.dot(relativeVelocity, tangent) / denom / contactCount  # 切向冲量大小
            j = jList[i]  # 法向冲量大小
            if abs(jt) <= j * sf:  # 根据静摩擦系数判断是否满足静摩擦条件
                frictionImpulse = jt * tangent  # 静摩擦冲量
            else:
                frictionImpulse = -j * tangent * df  # 动摩擦冲量

            frictionImpulseList[i] = frictionImpulse

        # 应用摩擦冲量
        for i in range(contactCount):
            frictionImpulse = frictionImpulseList[i]
            ra = raList[i]
            rb = rbList[i]

            bodyA.LinearVelocity += -frictionImpulse * bodyA.InvMass  # 物体A线速度增量
            bodyA.AngularVelocity += -SimplyVector.cross(ra, frictionImpulse) * bodyA.InvRotationalInertia  # 物体A角速度增量
            bodyB.LinearVelocity += frictionImpulse * bodyB.InvMass  # 物体B线速度增量
            bodyB.AngularVelocity += SimplyVector.cross(rb, frictionImpulse) * bodyB.InvRotationalInertia  # 物体B角速度增量
            
        