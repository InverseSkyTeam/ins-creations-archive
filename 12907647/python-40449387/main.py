import math
import time

__normal__ = False
__running__ = 'close'

def mxij_2d_pointdelta(x,y,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def mxij_3d_pointdelta(x,y,z,x2,y2,z2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)

def mxij_calc_formula(formula='x+y',args={'x':1,'y':1}):
    for i in args:
        formula = formula.replace(i,str(args[i]))
    return formula

def mxij_calc_times(start,end):    # 貌似有规律
    e_delta = end - start
    e_year = e_delta   # 地球年处理结束
    e_year_ = int(e_year)
    e_month = (e_year - e_year_)*12
    e_year = e_year_   # 地球月处理结束
    e_month_ = int(e_month)
    e_day = (e_month - e_month_)*30.43684941666667    # 1地球年=365.242193地球日
    e_month = e_month_   # 地球日处理结束
    e_day_ = int(e_day)
    e_hour = (e_day - e_day_)*12
    e_day = e_day_   # 小时处理结束
    e_hour_ = int(e_hour)
    e_min = (e_hour - e_hour_)*60
    e_hour = e_hour_   # 分钟处理结束
    e_min_ = int(e_min)
    e_sec = (e_min - e_min_)*60
    e_min = e_min_   # 正秒处理结束
    e_sec_ = int(e_sec)
    e_ms = (e_sec - e_sec_)*1000
    e_sec = e_sec_   # 毫秒处理结束
    e_ms_ = int(e_ms)
    e_us = (e_ms - e_ms_)*1000
    e_ms = e_ms_   # 微秒处理结束
    e_date_d = {
        'delta': e_delta,
        'year': e_year,
        'month': e_month,
        'day': e_day,
        'hour': e_hour,    # 打表积极用户
        'min': e_min,
        'sec': e_sec,
        'ms': e_ms,
        'us': e_us,
    }
    return e_date_d

def mxij_system_cls():
    print('\033[100A\033[2J\033[100A\033[3J'*8,end='')

def mxij_system_move(lines=100):
    print('\033[{}A'.format(lines),end='')

Calc3D = {
    '2d_point_delta': mxij_2d_pointdelta,
    '3d_point_delta': mxij_3d_pointdelta,
    'calc_formula': mxij_calc_formula,
    'calc_times': mxij_calc_times,
    'system_cls': mxij_system_cls,
    'system_move': mxij_system_move,
}

class Thing(object):   # 万恶之源
    def __init__(self,name='thing'):
        self.name = name   # 所有东西都有个名字

class Universe(Thing):    # 宇宙
    def __init__(self,index,name='universe'):
        super().__init__(name=name)
        self.index = index
        self.timeclock = Times()
        self.includes = []     # 可能开个千万数组
        self.length = 0
        self.width = 0
        self.height = 0
        self.hot = 0
        self.opentime = 1.0
        self.dimension = {      # 维度
            'all': 11,
            'macro': 4,
            'micro': 7,
            'macro_show': 3,
            'micro_show': 8,
        }
        self.macrodimensions = {
            1: self.length,
            2: self.width,
            3: self.height,
            4: self.timeclock,
        }
        self.set_now()
    def __str__(self):
        return str(self.get_info())
    def get_info(self):
        return [self.index,
                self.name,
                self.dimension,
                self.macrodimensions,
                self.hot,
                ]
    def get_now(self):
        return Calc3D['calc_times'](self.timeclock.start,self.timeclock.get_now())
    def set_now(self):
        self.now = self.get_now()
    def wait_open(self):
        self.set_now()
        if self.now['delta'] > self.opentime:
            return True
        return False

class Times(Thing):    # 时间
    def __init__(self):
        super().__init__(name='time')
        self.start = self.get_now()
        self.set_now()
    def get_now(self):
        return time.time()
    def set_now(self):
        self.now = self.get_now()

class Point(Thing):
    def __init__(self,index=0,pos=(0,0,0)):
        super().__init__(name='point')
        if index:
            self.name += str(index)
        self.setxyz(x,y,z)
    def __str__(self):
        return str(self.get_info())
    def get_info(self):
        return self.name
    def getxyz(self):
        return self.positon
    def setxyz(self,x=0,y=0,z=0):
        self.positon = {
            'x': x,
            'y': y,
            'z': z,
        }
    def move(self,x=0,y=0,z=0):
        self.postion['x'] += x
        self.postion['y'] += x
        self.postion['z'] += x
        return ['moved',x,y,z]

class Line(Thing):
    def __init__(self,p1,p2,name='line'):
        super().__init__(name=name)
        self.startp = p1
        self.endp = p2
        self.setlen()
    def __str__(self):
        return str(self.get_info())
    def get_info(self):
        return [self.name,self.startp,self.endp,self.length]
    def getlen(self):
        return self.length
    def setlen(self):
        self.length = Calc3D['3d_point_delta'](
            self.startp.positon['x'],
            self.startp.positon['y'],
            self.startp.positon['z'],
            self.endp.positon['x'],
            self.endp.positon['y'],
            self.endp.positon['z'],
        )
    def move(self,x,y,z):
        self.startp.move(x,y,z)
        self.endp.move(x,y,z)
        return ['moved',x,y,z]

class Surface(Thing):
    def __init__(self,lines,name='line'):
        super().__init__(name=name)
        self.setlines(lines)
        self.setarea()
    def __str__(self):
        return str(self.get_info())
    def get_info(self):
        return [self.name,self.startp,self.endp]
    def getarea(self):
        area = 0
        for i in lines:
            area += i.length
        return area
    def setarea(self):
        self.area = self.getarea()
    def setlines(self,newlines):
        self.lines = newlines
    def move(self,x,y,z):
        for i in self.lines:
            i.move(x,y,z)
        return ['moved',x,y,z]

__normal__ = True
__running__ = 'building'

universe_01 = Universe(index=1)

__running__ = 'ready'

if __normal__:
    __running__ = 'opening'

while __running__ == 'opening':
    if universe_01.wait_open():
        __running__ = 'open'

pt = 1
while __running__ == 'open':
    print(str(universe_01))
    universe_01.set_now()
    print('\npt times:',pt)
    print('update fps:',pt/(universe_01.now['delta']-1))
    Calc3D['system_move'](10)   # 10行一定够了吧
    pt += 1
