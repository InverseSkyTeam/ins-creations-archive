import math
import random
import time

t1 = time.time()
# random.seed(input('种子(1000<=n<=10^8,n∈ N):'))


# 初始化{
width = 150
height = 20
real_height = math.floor(height*0.3)
fake_height = height - real_height
down_height = 30
whole_height = height + down_height

# (70%空虚 + 30%基准地形) + 个人设置行数地下
data = [[0 for j in range(width)] for i in range(fake_height)] + \
       [[4 for j in range(width)]] + \
       [[1 for j in range(width)] for i in range(real_height-1)] + \
       [[2 for j in range(width)] for i in range(down_height)]

class BlockRender(object):   # 方块渲染器
    def __init__(self,x=0,y=0):
        self.setpos(x,y)
    def setpos(self,x=0,y=0):
        self.x = x
        self.y = y
    def addpos(self,addx=0,addy=0):
        self.x += addx
        self.y += addy
    def abs_fill(self,x=0,y=0,bid=0):
        data[y][x] = bid
    def fill(self,addx=0,addy=0,bid=0):
        if (0 <= self.y+addy < whole_height) and (0 <= self.x+addx < width):
            data[self.y+addy][self.x+addx] = bid
    def fills(self,bid=0,*adds):
        for addx,addy in adds:
            self.fill(addx,addy,bid)
BR = BlockRender()

def empty_row(x_left,x_right,y):
    for block in data[y][x_left:x_right+1]:
        if block:
            return False
    return True

def get_pos(args):
    left_least_space  = args[0]
    right_least_space = args[1]
    y_add             = args[2]
    position = [random.randint(0,width-1), fake_height]
    while not empty_row(position[0] - left_least_space,
                        position[0] + right_least_space,
                        position[1] + y_add
                       ):
        position[0] = random.randint(0,width-1)
    return position

def get_pos_undergroundwater(args='water'):
    return (random.randint(0,width-1),random.randint(height+(0 if args=='water' else math.ceil(down_height/2)),whole_height-1))

def addshape(times, get_pos_fun=get_pos, get_pos_args=(0,0,0), *mores):
    def decorator(shape_func):
        for i in range(times):
            position_x, position_y = get_pos_fun(get_pos_args)
            shape_func(position_x,position_y,*mores)
    return decorator


# } 地形函数 {
@addshape(times        = 6,
          get_pos_args = (3,3,-1)
         )
def plant_tree(x,y,*mores):
    BR.setpos(x,y)
    # 树木
    BR.fills(
        8, # 12
        (0,-4),(0,-3),(0,-2),(0,-1),  # 树干
        (-1,-1),(1,-1),  # 树根
    )
    # 树叶
    pos_rand = random.randint(1,4)
    if pos_rand < 3:
        BR.fills(
            9, # 13
            (random.randint(-1,1),-6),
            (-1,-5),(0,-5),(1,-5),
            (-2,-4),(-1,-4),(0,-4),(1,-4),(2,-4),
        )
    elif pos_rand == 3:
        BR.fills(
            9, # 13
            (random.randint(-2,0),-6),
            (-2,-5),(-1,-5),(0,-5),
            (-2,-4),(-1,-4),(0,-4),(1,-4),(2,-4),
        )
    else:
        BR.fills(
            9, # 13
            (random.randint(0,2),-6),
            (0,-5),(1,-5),(2,-5),
            (-2,-4),(-1,-4),(0,-4),(1,-4),(2,-4),
        )

@addshape(times        = 4,
          get_pos_args = (4,4,-1)
         )
def make_hill(x,y,*mores):
    BR.setpos(x,y)
    pos_rand = random.randint(1,11)
    if pos_rand <= 7:
        BR.fills(
            3,   # 17
            (-3,-1),(-2,-1),(-1,-1),(0,-1),(1,-1),(2,-1),(3,-1),
        )
    elif pos_rand == 8:
        BR.fills(
            3,   # 17
            (-3,-1),(-2,-1),(-1,-1),(0,-1),(1,-1),(2,-1),(3,-1),(4,-1),
        )
    elif pos_rand == 9:
        BR.fills(
            3,   # 17
            (-4,-1),(-3,-1),(-2,-1),(-1,-1),(0,-1),(1,-1),(2,-1),(3,-1),
        )
    elif pos_rand == 10:
        BR.fills(
            3,   # 17
            (-4,-1),(-3,-1),(-2,-1),(-1,-1),(0,-1),(1,-1),(2,-1),(3,-1),(4,-1),
        )
    else:
        BR.fills(
            3,   # 17
            (-5,-1),(-4,-1),(-3,-1),(-2,-1),(-1,-1),(0,-1),(1,-1),(2,-1),(3,-1),(4,-1),(5,-1),
        )
    if pos_rand <= 9:
        BR.addpos(random.randint(-3,-1),-2)
        BR.fills(
            3,   # 17
            (0,0),(1,0),(2,0),(3,0),(4,0),
        )
    else:
        BR.addpos(random.randint(-4,-1),-2)
        BR.fills(
            3,   # 17
            (0,0),(1,0),(2,0),(3,0),(4,0),(5,0),
        )
    BR.setpos(x,y)
    if random.randint(1,5) <= 3:
        for i in range(random.randint(3,4)):
            BR.fill(random.randint(-2,2),-3,3)
        if random.randint(1,5) <= 2:
            BR.fill(random.randint(-1,1),-4,3)

@addshape(times        = 4,
          get_pos_args = (2,2,-1)
         )
def make_puddle(x,y,*mores):
    BR.setpos(x-3,y-1)
    waterlist = [random.randint(2,9)]
    for i in range(random.randint(0,4)):
        waterlist.append(waterlist[i] + random.randint(-2,2))
        if (abs(waterlist[i+1] - waterlist[0]) > 4) or (waterlist[i+1] < 1):
            waterlist[i+1] = waterlist[0] + random.randint(-3,3)
    for line in waterlist:
        BR.addpos(0,1)  # 第一次就y+1，那么相当于从y=传入的参数y开始送氵
        for i in range(line):
            BR.fill(i,0,5)

@addshape(times        = 10,
          get_pos_fun  = get_pos_undergroundwater,
          get_pos_args = 'water'
         )
def make_undergroundwater(x,y,*mores):
    BR.setpos(x,y)
    waterlist     = [(x,y)]
    water_least   = mores[0] if mores else 1
    water_most    = mores[1] if mores else 30
    water         = random.randint(water_least,water_most)
    distance_most = math.ceil(math.sqrt(water_most)) + 2
    while water > 0:
        BR.fill(bid=5)
        thisx, thisy = random.choice(waterlist)
        nextxadd = random.randint(-1,1)
        nextyadd = random.randint(-1,1)
        over = not (0 <= thisx+nextxadd < width and height < thisy+nextyadd < whole_height)
        distance = abs(thisx+nextxadd-x) + abs(thisy+nextyadd-y)
        while ((thisx+nextxadd, thisy+nextyadd) in waterlist) or (distance > distance_most) or over:
            nextxadd = random.choice([-1,-1,-1,1,1,1,0,-2,-2,2,2])
            nextyadd = random.choice([-1,-1,-1,1,1,1,0,-2,-2,2,2])
            over = not (0 <= thisx+nextxadd < width and height < thisy+nextyadd < whole_height)
            distance = abs(thisx+nextxadd-x) + abs(thisy+nextyadd-y)
        BR.setpos(thisx+nextxadd, thisy+nextyadd)
        waterlist.append((thisx+nextxadd, thisy+nextyadd))
        water -= 1

@addshape(times        = 5,
          get_pos_fun  = get_pos_undergroundwater,
          get_pos_args = 'lava'
         )
def make_lava(x,y,*mores):    # 偷偷用raplace把water换成lava
    BR.setpos(x,y)
    lavalist     = [(x,y)]
    lava_least   = mores[0] if mores else 5
    lava_most    = mores[1] if mores else 40
    lava         = random.randint(lava_least,lava_most)
    distance_most = math.ceil(math.sqrt(lava_most)) + 2
    while lava > 0:
        BR.fill(bid=6)
        thisx, thisy = random.choice(lavalist)
        nextxadd = random.randint(-1,1)
        nextyadd = random.randint(-1,1)
        over = not (0 <= thisx+nextxadd < width and height < thisy+nextyadd < whole_height)
        distance = abs(thisx+nextxadd-x) + abs(thisy+nextyadd-y)
        while ((thisx+nextxadd, thisy+nextyadd) in lavalist) or (distance > distance_most) or over:
            nextxadd = random.choice([-1,-1,-1,1,1,1,0,0,-2,2])
            nextyadd = random.choice([-1,-1,-1,1,1,1,0,0,-2,2])
            over = not (0 <= thisx+nextxadd < width and height < thisy+nextyadd < whole_height)
            distance = abs(thisx+nextxadd-x) + abs(thisy+nextyadd-y)
        BR.setpos(thisx+nextxadd, thisy+nextyadd)
        lavalist.append((thisx+nextxadd, thisy+nextyadd))
        lava -= 1
# } 测试

t2 = time.time()

for y in data:
    ttext = ''
    for x in y:
        if x == 0: text = '\033[48;2;111;255;255m '
        if x == 1: text = '\033[48;2;160;100;0m '
        if x == 2: text = '\033[40m '
        if x == 3: text = '\033[43m '
        if x == 4: text = '\033[42m '
        if x == 5: text = '\033[44m '
        if x == 6: text = '\033[41m '
        if x == 8: text = '\033[48;2;255;180;130m '
        if x == 9: text = '\033[42m '
        ttext += text + '\033[0m'
    print(ttext,flush=True)

print(f'生成共用时{round((t2-t1)*1000,6)}ms(保留六位小数)')
print('\n\n\033[0m\033[38;2;160;100;0m地\033[38;2;0;255;255m形\033[38;2;230;230;0m生成成功\033[4A\033[8m\033[?25l')

# 种树(OK)
# 山丘(OK)
# 洼地(OK)
# 地下水(OK)
# 岩浆(OK)
# 山(Ready?)
# 矿洞(地下出现大洞,Ready?)
# 平台(Ready?)