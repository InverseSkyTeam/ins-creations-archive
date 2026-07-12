from SimplyVector import SimplyVector
class SimplyAABB:
    def __init__(self,minX,minY,maxX,maxY):
        self.Min = SimplyVector(minX,minY)
        self.Max = SimplyVector(maxX,maxY)