class DisplayMode:
    def __init__(self, w, h):
        self.w: int = w
        self.h: int = h

    def getWidth(self):
        return self.w
    
    def getHeight(self):
        return self.h
    
    def get_size(self):
        return self.w, self.h
