class Collider:  # 碰撞箱
    def __init__(self, pos1 = (None,) * 3, pos2 = (None,) * 3):
        # pos1: 碰撞箱顶点在-X，-Y，-Z方向的位置
        # pos2: 碰撞箱顶点在+X，+Y，+Z方向的位置

        self.x1, self.y1, self.z1 = pos1
        self.x2, self.y2, self.z2 = pos2
    
    def __add__(self, pos):
        x, y, z = pos

        return Collider(
            (self.x1 + x, self.y1 + y, self.z1 + z),
            (self.x2 + x, self.y2 + y, self.z2 + z)
        )
    
    def __and__(self, collider):
        x = min(self.x2, collider.x2) - max(self.x1, collider.x1)
        y = min(self.y2, collider.y2) - max(self.y1, collider.y1)
        z = min(self.z2, collider.z2) - max(self.z1, collider.z1)

        return x > 0 and y > 0 and z > 0
    
    def collide(self, collider, velocity):
        # self: 动态碰撞体，会移动
        # collider: 静态碰撞体，保持不动

        no_collision = 1, None

        # 找到每个轴上的进入和退出时间

        vx, vy, vz = velocity

        time = lambda x, y: x / y if y else float('-' * (x > 0) + "inf")

        x_entry = time(collider.x1 - self.x2 if vx > 0 else collider.x2 - self.x1, vx)
        x_exit  = time(collider.x2 - self.x1 if vx > 0 else collider.x1 - self.x2, vx)

        y_entry = time(collider.y1 - self.y2 if vy > 0 else collider.y2 - self.y1, vy)
        y_exit  = time(collider.y2 - self.y1 if vy > 0 else collider.y1 - self.y2, vy)

        z_entry = time(collider.z1 - self.z2 if vz > 0 else collider.z2 - self.z1, vz)
        z_exit  = time(collider.z2 - self.z1 if vz > 0 else collider.z1 - self.z2, vz)

        # 确认我们真的发生了碰撞

        if x_entry < 0 and y_entry < 0 and z_entry < 0:
            return no_collision

        if x_entry > 1 or y_entry > 1 or z_entry > 1:
            return no_collision
        
        # 我们是在哪个轴上首先发生碰撞？

        entry = max(x_entry, y_entry, z_entry)
        exit_ = min(x_exit,  y_exit,  z_exit )

        if entry > exit_:
            return no_collision
        
        # 找到我们发生碰撞的表面的法线

        nx = (0, -1 if vx > 0 else 1)[entry == x_entry]
        ny = (0, -1 if vy > 0 else 1)[entry == y_entry]
        nz = (0, -1 if vz > 0 else 1)[entry == z_entry]

        return entry, (nx, ny, nz)
