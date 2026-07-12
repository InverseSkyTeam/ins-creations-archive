def get_distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2) ** 0.5

class Slider:
    def __init__(self,value,full,digit=0):
        self.value = value
        self.full = full
        self.digit = digit
    def __iadd__(self,n):
        self.value = max(0, min(self.value + n, self.full))
        return self
    def __isub__(self,n):
        self.value = max(0, min(self.value - n, self.full))
        return self
    def __imul__(self,n):
        self.value = max(0, min(self.value * n, self.full))
        return self
    def __itruediv__(self,n):
        self.value = max(0, min(self.value / n, self.full))
        return self
    def __add__(self,n):
        return round(max(0, min(self.value + n, self.full)), self.digit)
    def __sub__(self,n):
        return round(max(0, min(self.value - n, self.full)), self.digit)
    def __mul__(self,n):
        return round(max(0, min(self.value * n, self.full)), self.digit)
    def __truediv__(self,n):
        return round(max(0, min(self.value / n, self.full)), self.digit)
    def clear(self):
        self.value = 0
    def fill(self):
        self.value = self.full
    def set(self,n):
        self.value = n
    def change_full(self,n):
        self.full = n
    @property
    def v(self):
        return round(self.value,self.digit)
    @property
    def f(self):
        return round(self.full,self.digit)
    @property
    def part(self):
        return self.value / self.full