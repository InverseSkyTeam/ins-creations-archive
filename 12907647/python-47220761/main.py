from collections import deque
import math
import random
import timeit
import time

t1 = time.time()
random.seed(int(t1))

# 初始化{
width = 150
height = 50
real_height = math.floor(height*0.3)
fake_height = height - real_height
down_height = 60
whole_height = height + down_height

if fake_height < 8:
    raise Exception(f'[Bad Height] Fake_height is less than 8 (Now is {fake_height}).')

# (70%空虚 + 30%基准地形) + 个人设置行数地下
data = [[0 for j in range(width)] for i in range(fake_height)] + \
       [[1 for j in range(width)]] + \
       [[2 for j in range(width)] for i in range(real_height-1)] + \
       [[3 for j in range(width)] for i in range(down_height)]

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
    for block in data[y][max(0,x_left):min(width,x_right+1)]:
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

def get_pos_platform():
    plen = random.randint(3,6)
    position = [random.randint(0,width-plen), random.randint(fake_height-7,fake_height-2)]
    while not empty_row(position[0],
                        position[0] + plen - 1,
                        position[1],
                       ):
        position = [random.randint(0,width-plen), random.randint(fake_height-7,fake_height-2)]
    position.append(plen)
    return position

def get_pos_u_hole(args):
    return (random.randint(0,width-1),random.randint(fake_height,whole_height-1))

def addshape(times, get_pos_fun=get_pos, get_pos_args=(0,0,0), *mores):
    def decorator(shape_func):
        for i in range(times):
            if get_pos_args == 'platform':
                position_x, position_y, plength = get_pos_fun()
                shape_func(position_x, position_y, plength)
            else:
                position_x, position_y = get_pos_fun(get_pos_args)
                shape_func(position_x, position_y, *mores)
    return decorator


# } 地形函数 {
@addshape(times        = 7,
          get_pos_args = (3,3,-1)
         )
def plant_tree(x,y,*mores):
    BR.setpos(x,y)
    tree_level_rand = random.randint(1,100)
    # level1 矮树 2格    | 1-15   | 15%
    # level2 普通 3格    | 16-70  | 55%
    # level3 高树 4-5格  | 71-90  | 20%
    # level4 大树 6-10格 | 91-99  | 9%
    # level5 绝顶 11格   | 100    | 0.8%
    # level! 神树 11格   | 100    | 0.2%
    if tree_level_rand <= 90:
        if tree_level_rand <= 15:
            tree_up = 2
        elif tree_level_rand <= 70:
            tree_up = 3
            BR.fill(0,-3,12)
        else:
            tree_up = random.randint(4,5)
            BR.fill(0,-3,12)
            BR.fill(0,-4,12)
            if tree_up == 5:
                BR.fill(0,-5,12)
        # 树木
        BR.fills(
            12,
            (0,-2),(0,-1),  # 树干
            (-1,-1),(1,-1),  # 树根
        )
        # 树叶
        BR.addpos(addy=3-tree_up)
        pos_rand = random.randint(1,4)
        if pos_rand < 3:
            BR.fills(
                13,
                (random.randint(-1,1),-6),
                (-1,-5),(0,-5),(1,-5),
                (-2,-4),(-1,-4),(0,-4),(1,-4),(2,-4),
            )
        elif pos_rand == 3:
            BR.fills(
                13,
                (random.randint(-2,0),-6),
                (-2,-5),(-1,-5),(0,-5),
                (-2,-4),(-1,-4),(0,-4),(1,-4),(2,-4),
            )
        else:
            BR.fills(
                13,
                (random.randint(0,2),-6),
                (0,-5),(1,-5),(2,-5),
                (-2,-4),(-1,-4),(0,-4),(1,-4),(2,-4),
            )
    elif tree_level_rand <= 99:
        tree_up = random.randint(6,10)
        if tree_up >= 6:  BR.fill(0,-6,12)
        if tree_up >= 7:  BR.fill(0,-7,12)
        if tree_up >= 8:  BR.fill(0,-8,12)
        if tree_up >= 9:  BR.fill(0,-9,12)
        if tree_up == 10: BR.fill(0,-10,12)
        # 树木
        BR.fills(
            12,
            (0,-5),(0,-4),(0,-3),(0,-2),(0,-1),  # 树干
            (-2,-1),(-1,-1),(1,-1),(2,-1),  # 树根
        )
        BR.addpos(addy=3-tree_up)
        pos_rand = random.randint(1,4)
        if pos_rand < 3:
            BR.fills(
                13,
                (random.randint(-1,1),-6),
                (-1,-5),(0,-5),(1,-5),
                (-3,-4),(-2,-4),(-1,-4),(0,-4),(1,-4),(2,-4),(3,-4),
            )
        elif pos_rand == 3:
            BR.fills(
                13,
                (random.randint(-2,0),-6),
                (-2,-5),(-1,-5),(0,-5),
                (-3,-4),(-2,-4),(-1,-4),(0,-4),(1,-4),(2,-4),(3,-4),
            )
        else:
            BR.fills(
                13,
                (random.randint(0,2),-6),
                (0,-5),(1,-5),(2,-5),
                (-3,-4),(-2,-4),(-1,-4),(0,-4),(1,-4),(2,-4),(3,-4),
            )
    else:
        BR.addpos(addy=-8)
        tree_up = random.randint(1,10)
        if tree_up <= 8:  # tree level5
            tree_block = 12
            BR.fills(
                13,
                (0,-7),
                (-1,-6),(0,-6),(1,-6),
                (-2,-5),(-1,-5),(0,-5),(1,-5),(2,-5),
                (-3,-4),(-2,-4),(-1,-4),(0,-4),(1,-4),(2,-4),(3,-4),
            )
        else:    # tree level!
            tree_block = 22
            BR.fills(
                23,
                (0,-11),
                (-1,-10),(0,-10),(1,-10),
                (-2,-9),(-1,-9),(0,-9),(1,-9),(2,-9),
                (0,-8),
                (-1,-7),(0,-7),(1,-7),
                (-2,-6),(-1,-6),(0,-6),(1,-6),(2,-6),
                (-3,-5),(-2,-5),(-1,-5),(0,-5),(1,-5),(2,-5),(3,-5),
                (-4,-4),(-3,-4),(-2,-4),(-1,-4),(0,-4),(1,-4),(2,-4),(3,-4),(4,-4),
            )
            BR.setpos(x,y)
            BR.fills(
                tree_block,
                (-2,-2),(2,-2),
                (-1,-3),(1,-3),
                (-1,-4),(1,-4),
                (-1,-5),(1,-5),
                (-1,-6),(1,-6),
            )
        # 树木
        BR.setpos(x,y)
        BR.fills(
            tree_block,
            (0,-11),(0,-10),(0,-9),(0,-8),(0,-7),(0,-6),(0,-5),(0,-4),(0,-3),(0,-2),(0,-1),  # 树干
            (-1,-2),(1,-2),  # 上层树根
            (-3,-1),(-2,-1),(-1,-1),(1,-1),(2,-1),(3,-1),  # 下层树根
        )

@addshape(times        = 4,
          get_pos_args = (4,4,-1)
         )
def make_hill(x,y,*mores):
    BR.setpos(x,y)
    pos_rand = random.randint(1,11)
    if pos_rand <= 7:
        BR.fills(
            2,
            (-3,-1),(-2,-1),(-1,-1),(0,-1),(1,-1),(2,-1),(3,-1),
        )
    elif pos_rand == 8:
        BR.fills(
            2,
            (-3,-1),(-2,-1),(-1,-1),(0,-1),(1,-1),(2,-1),(3,-1),(4,-1),
        )
    elif pos_rand == 9:
        BR.fills(
            2,
            (-4,-1),(-3,-1),(-2,-1),(-1,-1),(0,-1),(1,-1),(2,-1),(3,-1),
        )
    elif pos_rand == 10:
        BR.fills(
            2,
            (-4,-1),(-3,-1),(-2,-1),(-1,-1),(0,-1),(1,-1),(2,-1),(3,-1),(4,-1),
        )
    else:
        BR.fills(
            2,
            (-5,-1),(-4,-1),(-3,-1),(-2,-1),(-1,-1),(0,-1),(1,-1),(2,-1),(3,-1),(4,-1),(5,-1),
        )
    if pos_rand <= 9:
        BR.addpos(random.randint(-3,-1),-2)
        BR.fills(
            2,
            (0,0),(1,0),(2,0),(3,0),(4,0),
        )
    else:
        BR.addpos(random.randint(-4,-1),-2)
        BR.fills(
            2,
            (0,0),(1,0),(2,0),(3,0),(4,0),(5,0),
        )
    BR.setpos(x,y)
    if random.randint(1,5) <= 3:
        for i in range(random.randint(3,4)):
            BR.fill(random.randint(-2,2),-3,2)
        if random.randint(1,5) <= 2:
            BR.fill(random.randint(-1,1),-4,2)

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
        BR.addpos(random.randint(-5,3),1)  # 第一次就y+1，那么相当于从y=传入的参数y开始送氵
        if abs(BR.x - x + 3) > 5:
            BR.setpos(x-random.randint(2,4),BR.y)
        for i in range(line):
            BR.fill(i,0,14)

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
        BR.fill(bid=14)
        thisx, thisy = random.choice(waterlist)
        nextxadd = random.randint(-1,1)
        nextyadd = random.randint(-1,1)
        over = not (0 <= thisx+nextxadd < width and height < thisy+nextyadd < whole_height)
        distance = abs(thisx+nextxadd-x) + abs(thisy+nextyadd-y)
        count = 0
        while ((thisx+nextxadd, thisy+nextyadd) in waterlist) or (distance > distance_most) or over:
            if count <= 5:
                nextxadd = random.choice([-1,-1,-1,1,1,1,0,-2,-2,2,2])
                nextyadd = random.choice([-1,-1,-1,1,1,1,0,-2,-2,2,2])
            elif count <= 10:
                nextxadd = random.randint(-5,5)
                nextyadd = random.randint(-5,5)
            else:
                break
            over = not (0 <= thisx+nextxadd < width and height < thisy+nextyadd < whole_height)
            distance = abs(thisx+nextxadd-x) + abs(thisy+nextyadd-y)
            count += 1
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
        BR.fill(bid=15)
        thisx, thisy = random.choice(lavalist)
        nextxadd = random.randint(-1,1)
        nextyadd = random.randint(-1,1)
        over = not (0 <= thisx+nextxadd < width and height < thisy+nextyadd < whole_height)
        distance = abs(thisx+nextxadd-x) + abs(thisy+nextyadd-y)
        count = 0
        while ((thisx+nextxadd, thisy+nextyadd) in lavalist) or (distance > distance_most) or over:
            if count <= 4:
                nextxadd = random.choice([-1,-1,-1,1,1,1,0,0,-2,2])
                nextyadd = random.choice([-1,-1,-1,1,1,1,0,0,-2,2])
            elif count <= 8:
                nextxadd = random.randint(-4,4)
                nextyadd = random.randint(-4,4)
            else:
                break
            over = not (0 <= thisx+nextxadd < width and height < thisy+nextyadd < whole_height)
            distance = abs(thisx+nextxadd-x) + abs(thisy+nextyadd-y)
            count += 1
        BR.setpos(thisx+nextxadd, thisy+nextyadd)
        lavalist.append((thisx+nextxadd, thisy+nextyadd))
        lava -= 1

@addshape(times        = 3,
          get_pos_fun  = get_pos_platform,
          get_pos_args = 'platform',
         )
def make_platform(x,y,*mores):
    BR.setpos(x,y)
    for i in range(mores[0]):
        BR.fill(bid=21)
        BR.addpos(addx=1)

CHANGEDATA = (1,2,4)
@addshape(times        = 3,
          get_pos_fun  = get_pos_u_hole,
         )
def make_underhole(x,y,*mores):
    global data
    
    _get_p = lambda: round(random.uniform(-1,1),6)
    _HOLE_SIZE_MINN = 25
    _HOLE_SIZE_MAXN = 1800
    _NEXT_HOLE_SIZE_MINN = 10
    _NEXT_HOLE_SIZE_MAXN = 310
    
    hole_size = random.randint(_HOLE_SIZE_MINN,_HOLE_SIZE_MAXN)
    queue = deque()
    
    if hole_size < 100:
        generation_max = 1
    elif hole_size < 400:
        generation_max = random.choice([1,1,1,1,1,1,1,2,2])
    elif hole_size < 800:
        generation_max = random.choice([1,1,1,1,1,1,2,2,2,3])
    elif hole_size < 1000:
        generation_max = random.choice([1,1,1,2,2,2,2,2,2,2,3,3,3])
    elif hole_size < 1400:
        generation_max = random.choice([1,2,2,2,2,2,2,2,3,3,3,3,4])
    elif hole_size < 1700:
        generation_max = random.choice([2,2,2,2,3,3,3,3,3,3,3,4,4,4])
    else:
        generation_max = random.choice([2,3,3,3,3,3,3,3,4,4,4,4,4])
        if hole_size > 1797:
            generation_max = random.choice([3,3,3,3,3,4,4,4,4,4,4,5,5])
            if (hole_size == 1800) & (generation_max == 11):
                hole_size == 666
                generation_max = 111
    
    offset_col = _get_p()
    offset_row = _get_p()
    
    # bfs------------------------------------------------------
    queue.append([x,y,1])
    while hole_size and queue:
        next_hole_size = min(random.randint(_NEXT_HOLE_SIZE_MINN,_NEXT_HOLE_SIZE_MAXN),hole_size)
        offset_col_tmp = _get_p()
        offset_row_tmp = _get_p()
        if offset_col < 0:
            while offset_col_tmp < offset_col:
                offset_col_tmp = _get_p()
        else:
            while offset_col_tmp > offset_col:
                offset_col_tmp = _get_p()
        if offset_row < 0:
            while offset_row_tmp < offset_row:
                offset_row_tmp = _get_p()
        else:
            while offset_row_tmp > offset_row:
                offset_row_tmp = _get_p()
        offset_col = offset_col_tmp
        offset_row = offset_row_tmp
        hole_size -= next_hole_size
        
        while next_hole_size and queue:
            next_hole_size -= 1
            _x, _y, _generation = queue.popleft()
            if (_x < 0) or (_x >= width) or (_y < fake_height) or (_y >= whole_height) or \
               (not data[_y][_x]) or (_generation > generation_max):
                if not queue:
                    queue.append([_x-1,_y,1])
                    queue.append([_x+1,_y,1])
                    queue.append([_x,_y-1,1])
                    queue.append([_x,_y+1,1])
                continue
            if (3 <= _x <= width-3):
                downs = _y - fake_height
                if (downs <= random.randint(3,10) and data[fake_height-1][_x]) or \
                   (downs <= random.randint(2,6) and data[fake_height-1][_x-1]) or \
                   (downs <= random.randint(2,6) and data[fake_height-1][_x+1]) or \
                   (downs <= random.randint(1,3) and data[fake_height-1][_x-2]) or \
                   (downs <= random.randint(1,3) and data[fake_height-1][_x+2]):
                    if not queue:
                        queue.append([_x,_y+1,1])
                        queue.append([_x-1,_y+1,1])
                        queue.append([_x+1,_y+1,1])
                    continue
            if (data[_y][_x] not in CHANGEDATA): continue
            data[_y][_x] = 0
            this_col = _get_p()
            this_row = _get_p()
            # 与偏移量相反就衰变到下一代。
            if this_col < offset_col:
                queue.append([_x,_y-1,_generation])
                if random.randint(0,1): queue.append([_x,_y+1,_generation+1])
            elif this_col > offset_col:
                queue.append([_x,_y-1,_generation+1])
                if random.randint(0,1): queue.append([_x,_y+1,_generation])
            else:
                queue.append([_x,_y-1,_generation])
                if random.randint(0,1): queue.append([_x,_y+1,_generation])
            if this_row < offset_row:
                queue.append([_x-1,_y,_generation])
                if random.randint(0,1): queue.append([_x+1,_y,_generation+1])
            elif this_row > offset_row:
                queue.append([_x-1,_y,_generation+1])
                if random.randint(0,1): queue.append([_x+1,_y,_generation])
            else:
                queue.append([_x-1,_y,_generation])
                if random.randint(0,1): queue.append([_x+1,_y,_generation])

def make_mountain(x,y,*mores):
    pass
    
# } 测试

t2 = time.time()

print(f'生成用时: {(t2-t1)*1000:.6f}ms\n种子: {int(t1)}')
print('生成内容是真实的，不信看源码，如果出现0ms的情况就是快到时间戳无法准确测量了')
print('本次:重大更新。修复地下水死循环bug，矿洞升级6.0算法，方块id对标，更新更新日志。')
print('\n\n\033[0m\033[38;2;160;100;0m地\033[38;2;0;255;255m形\033[38;2;230;230;0m生成完毕\033[4A\033[2B\033[8m') # \033[?25l