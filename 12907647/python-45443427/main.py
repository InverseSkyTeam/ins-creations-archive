import math

def sin(num):
    return math.sin(math.radians(num))
def cos(num):
    return math.cos(math.radians(num))

class Point3D(object):
    def __init__(self,position):
        self.setinit(position)
    
    def setinit(self,position):
        self.x, self.y, self.z = position
        self.focus(1.0)
    
    def focus(self,focal_length):
        self.focal_length = focal_length
    
    def on2D(self):
        x = self.x * self.focal_length / self.z
        y = self.y * self.focal_length / self.z
        return (x,y)
    
    def act_move(self,addx,addy,addz):
        self.x += addx
        self.y += addy
        self.z += addz
    
    def act_scale(self,mulx,muly,mulz):
        self.x *= mulx
        self.y *= muly
        self.z *= mulz
    
    def act_rotate_x(self,angle):
        self.y = self.y * cos(angle) - self.z * sin(angle)
        self.z = self.y * sin(angle) + self.z * cos(angle)
    
    def act_rotate_z(self,angle):
        self.x = self.x * cos(angle) - self.y * sin(angle)
        self.y = self.x * sin(angle) + self.y * cos(angle)




print('几年前随便看看不懂就堆着，现在要用去看看有些懂了。平移和缩放好理解，旋转需要通过三角函数实现计算（弧度角度需要转换），但是由于pygame和scratch的y轴坐标系不同，不知道怎么计算，希望数学大佬指出')
print('''
吴宇航版y函数是这样写的:
def rotatey(self,angle):
    self.x = self.z * sin(angle) + self.x * cos(angle)
    self.z = self.z * cos(angle) - self.x * sin(angle)
我通过x/z函数摸到一点出路，将z改为self.z = self.x * sin(angle) - self.z * cos(angle)
但是还是不对，仅仅是方向变了
我又想到坐标系相反，改y = -y
但效果一样
因为投影到2d坐标时要用y/z，所以不管是y还是z改为相反数都一样
于是我突发奇想把x=-x
然后变为动弹不得，也不行
我尝试了各种排列组合，都不行
看来需要改变三角函数了，难。正切都试了还不行
''')