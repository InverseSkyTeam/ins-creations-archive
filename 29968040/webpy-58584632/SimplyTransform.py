import math
class SimplyTransform:
    def __init__(self,FvPosition,angle):
        self.PositionX = FvPosition.x
        self.PositionY = FvPosition.y
        self.sin = math.sin(angle)
        self.cos = math.cos(angle)
