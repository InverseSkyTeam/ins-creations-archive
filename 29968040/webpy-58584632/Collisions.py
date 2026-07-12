from SimplyVector import SimplyVector

Box = "Box"
Circle  = "Circle"
class Collisions:

    def IntersectAABBs(a, b):
            if a.Max.x <= b.Min.x or b.Max.x <= a.Min.x or a.Max.y <= b.Min.y or b.Max.y <= a.Min.y:
                return False
            return True
        
    def PointSegmentDistance(p,a,b):
        ab = b-a
        ap = p-a
        proj = SimplyVector.dot(ap,ab)
        abLenSq = SimplyVector.LengthSquared(ab)
        d = proj /abLenSq
        if d<=0:
            cp = a
        elif d>=1:
            cp = b
        else:
            cp = a+ab*d
        distanceSquard = SimplyVector.DistanceSquared(p,cp)
        return distanceSquard,cp
    
    @staticmethod
    def FindContactPoints(bodyA,bodyB):

        shape_type_a = bodyA.ShapeType
        shape_type_b = bodyB.ShapeType

        contact1 = SimplyVector(0,0)
        contact2 = SimplyVector(0,0)
        contactCount = 0

        if shape_type_a == Box:
            if shape_type_b == Box:
                contact1, contact2,contactCount=Collisions.FindPolygonsContactPoints(bodyA.GetTransformedVertices(), bodyB.GetTransformedVertices());
            elif shape_type_b == Circle:
                contact1 = Collisions.FindCirclePolygonContactPoint(bodyB.Position,bodyA.GetTransformedVertices())
                contactCount = 1
        elif shape_type_a == Circle:
            if shape_type_b == Box:
                contact1 = Collisions.FindCirclePolygonContactPoint(bodyA.Position,bodyB.GetTransformedVertices())
                contactCount = 1
            elif shape_type_b == Circle:
                contact1  = Collisions.FindCirclesContactPoint(bodyA.Position,bodyA.Radius,bodyB.Position)
                contactCount = 1
        return contact1,contact2,contactCount
    
    def FindPolygonsContactPoints(verticesA,verticesB):
        contact1 = SimplyVector(0,0)
        contact2 = SimplyVector(0,0)
        contactCount = 0
        minDistSq = float("inf")
        for i in verticesA:
            p = i
            for j in range(len(verticesB)):
                va = verticesB[j]
                vb = verticesB[(j + 1) % len(verticesB)]

                distSq, cp = Collisions.PointSegmentDistance(p, va, vb)

                if SimplyVector.NearlyEqual(distSq, minDistSq):
                    if not SimplyVector.NearlyEqualFv(cp, contact1):
                        contact2 = cp
                        contactCount = 2
                elif distSq < minDistSq:
                    minDistSq = distSq
                    contactCount = 1
                    contact1 = cp

        for i in verticesB:
            p = i
            for j in range(len(verticesA)):
                va = verticesA[j]
                vb = verticesA[(j + 1) % len(verticesA)]

                distSq, cp = Collisions.PointSegmentDistance(p, va, vb)

                if SimplyVector.NearlyEqual(distSq, minDistSq):
                    if not SimplyVector.NearlyEqualFv(cp, contact1):
                        contact2 = cp
                        contactCount = 2
                elif distSq < minDistSq:
                    minDistSq = distSq
                    contactCount = 1
                    contact1 = cp

        return contact1, contact2, contactCount
        
    @staticmethod
    def FindCirclePolygonContactPoint(circleCenter,polygonVertices):
        minDistSq  =float("inf")
        cp = SimplyVector(0,0)
        LenPolygonVertices = len(polygonVertices)
        for i in range(LenPolygonVertices):
            va = polygonVertices[i]
            vb = polygonVertices[(i + 1) % LenPolygonVertices]
            distSq,contact = Collisions.PointSegmentDistance(circleCenter,va,vb)
            if distSq<minDistSq:
                minDistSq = distSq
                cp = contact
        return cp


    @staticmethod
    def FindCirclesContactPoint(centerA,RadiusA,centerB):
        v_AB = SimplyVector.normalize(centerB - centerA)
        cp = centerA+v_AB*RadiusA
        return cp
    
    @staticmethod
    def intersect_circle_polygon(circle_center, circle_Radius, polygonCenter,vertices):
        normal = SimplyVector(0, 0)
        depth = float("inf")

        # 遍历多边形的每条边
        for i in range(len(vertices)):
            va = vertices[i]
            vb = vertices[(i + 1) % len(vertices)]

            # 计算边的法向量
            edge = vb - va
            axis = SimplyVector(-edge.y, edge.x)
            axis = SimplyVector.normalize(axis)

            # 计算多边形和圆在该轴上的投影
            min_a, max_a = Collisions.project_vertices(vertices, axis)
            min_b, max_b = Collisions.project_circle(circle_center, circle_Radius, axis)

            # 判断投影是否重叠，如果不重叠则返回False
            if min_a >= max_b or min_b >= max_a:
                return False, None, None

            # 计算投影的重叠深度
            axis_depth = min(max_b - min_a, max_a - min_b)

            # 如果深度小于当前最小深度，则更新法向量和深度
            if axis_depth < depth:
                depth = axis_depth
                normal = axis

        # 找到多边形上距离圆心最近的点
        cp_index = Collisions.find_closest_point_on_polygon(circle_center, vertices)
        cp = vertices[cp_index]

        # 计算该点到圆心的方向向量
        axis = cp - circle_center
        axis = SimplyVector.normalize(axis)

        # 计算多边形和圆在该轴上的投影
        min_a, max_a = Collisions.project_vertices(vertices, axis)
        min_b, max_b = Collisions.project_circle(circle_center, circle_Radius, axis)

        # 判断投影是否重叠，如果不重叠则返回False
        if min_a >= max_b or min_b >= max_a:
            return False, None, None

        # 计算投影的重叠深度
        axis_depth = min(max_b - min_a, max_a - min_b)

        # 如果深度小于当前最小深度，则更新法向量和深度
        if axis_depth < depth:
            depth = axis_depth
            normal = axis

        # 计算重心到圆心的方向向量
        direction = polygonCenter - circle_center

        # 如果方向向量与法向量的点积为负，则取法向量的反方向
        if SimplyVector.dot(direction, normal) < 0:
            normal = -normal

        # 返回True和法向量和深度
        return True, depth, normal

    # 定义一个静态方法计算圆在某个轴上的投影
    @staticmethod
    def project_circle(center, Radius, axis):
        direction = SimplyVector.normalize(axis)
        direction_and_Radius = direction * Radius

        p1 = center + direction_and_Radius
        p2 = center - direction_and_Radius

        min = SimplyVector.dot(p1, axis)
        max = SimplyVector.dot(p2, axis)

        if min > max:
            # 交换最小值和最大值
            min, max = max, min

        return min, max

    @staticmethod
    def find_closest_point_on_polygon(circle_center, vertices):
        result = -1
        min_distance = float("inf")
        #print(len(vertices))
        for i in range(len(vertices)):
            v = vertices[i]
            distance = SimplyVector.distance(v, circle_center)

            if distance < min_distance:
                min_distance = distance
                result = i
            
        return result


    # 定义一个静态方法计算多边形在某个轴上的投影
    @staticmethod
    def project_vertices(vertices, axis):
        min = float("inf")
        max = float("-inf")
        for v in vertices:
            proj = SimplyVector.dot(v, axis)
            if proj < min:
                min = proj
            if proj > max:
                max = proj
        return min, max


    # 定义一个静态方法判断两个多边形是否相交，并返回法向量和深度
    @staticmethod
    def IntersectPoltgons(center_a ,vertices_a, center_b,vertices_b):
        normal = SimplyVector(0, 0)
        depth = float("inf")

        # 遍历多边形A的每条边
        for i in range(len(vertices_a)):
            va = vertices_a[i]
            vb = vertices_a[(i + 1) % len(vertices_a)]

            # 计算边的法向量
            edge = vb - va
            axis = SimplyVector(-edge.y, edge.x)
            axis =SimplyVector.normalize(axis)

            # 计算两个多边形在该轴上的投影
            min_a, max_a = Collisions.project_vertices(vertices_a, axis)
            min_b, max_b = Collisions.project_vertices(vertices_b, axis)

            # 判断投影是否重叠，如果不重叠则返回False
            if min_a >= max_b or min_b >= max_a:
                return False, None, None

            # 计算投影的重叠深度
            axis_depth = min(max_b - min_a, max_a - min_b)

            # 如果深度小于当前最小深度，则更新法向量和深度
            if axis_depth < depth:
                depth = axis_depth
                normal = axis

        # 遍历多边形B的每条边，重复上述过程
        for i in range(len(vertices_b)):
            va = vertices_b[i]
            vb = vertices_b[(i + 1) % len(vertices_b)]

            edge = vb - va
            axis = SimplyVector(-edge.y, edge.x)
            axis = SimplyVector.normalize(axis)

            min_a, max_a = Collisions.project_vertices(vertices_a, axis)
            min_b, max_b = Collisions.project_vertices(vertices_b, axis)

            if min_a >= max_b or min_b >= max_a:
                return False, None, None

            axis_depth = min(max_b - min_a, max_a - min_b)

            if axis_depth < depth:
                depth = axis_depth
                normal = axis

        # 计算重心的方向向量
        direction = center_b - center_a

        # 如果方向向量与法向量的点积为负，则取法向量的反方向
        if SimplyVector.dot(direction, normal) < 0:
            normal = -normal

        # 返回True和法向量和深度
        return True, depth,normal 
 
    @staticmethod
    def IntersectCircles(CenterA,RadiusA,CenterB,RadiusB):#fv,float or int,fv,float or int 
         #return元组,是否碰撞，碰撞深度，碰撞方向
        BothDistance = SimplyVector.distance(CenterA,CenterB)
        radii = RadiusA+RadiusB
        
        if BothDistance >= radii:
            return False,0,SimplyVector(0,0)
        
        normal = SimplyVector.normalize(CenterB - CenterA)#获得碰撞方向的单位向量A指向B
        depth = radii - BothDistance
       # print(CenterA,CenterB,BothDistance)
        return True,depth,normal
        
    @staticmethod
    def Collide(body_a, body_b):
        normal = SimplyVector(0, 0)
        depth = 0

        shape_type_a = body_a.ShapeType
        shape_type_b = body_b.ShapeType

        if shape_type_a == Box:
            if shape_type_b == Box:
                # 如果两个物体都是矩形，调用多边形相交的方法
                return Collisions.IntersectPoltgons(
                     body_a.Position,body_a.GetTransformedVertices(),
                     body_b.Position,body_b.GetTransformedVertices())
            elif shape_type_b == Circle:
                # 如果一个物体是矩形，另一个是圆，调用圆和多边形相交的方法
                result, depth, normal = Collisions.intersect_circle_polygon(
                    body_b.Position, body_b.Radius,
                    body_a.Position,body_a.GetTransformedVertices())
                if normal == None:
                    normal ==SimplyVector(0, 0)
                else:
                    # 反转法向量的方向
                    normal = -normal
                return result, depth, normal

        elif shape_type_a == Circle:
            if shape_type_b == Box:
                # 如果一个物体是圆，另一个是矩形，调用圆和多边形相交的方法
                return Collisions.intersect_circle_polygon(
                    body_a.Position, body_a.Radius,body_b.Position,
                   body_b.GetTransformedVertices())
            elif shape_type_b == Circle:
                # 如果两个物体都是圆，调用圆和圆相交的方法
                return Collisions.IntersectCircles(
                    body_a.Position, body_a.Radius,
                    body_b.Position, body_b.Radius)

        # 如果两个物体的形状不匹配，返回False
        return False, None, None
