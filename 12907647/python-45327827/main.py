import math,random

width = 40
height = 20
real_height = math.floor(height*0.3)
fake_height = height - real_height
down_height = 15
whole_height = height + down_height

# (70%空虚 + 30%基准地形) + 个人设置行数地下
data = [[0 for j in range(width)] for i in range(fake_height)] + \
       [[1 for j in range(width)] for i in range(real_height)] + \
       [[2 for j in range(width)] for i in range(down_height)]

class BlockRender(object):   # 方块渲染器
    def __init__(self,x=0,y=0):
        self.setpos(x,y)
    def setpos(self,x=0,y=0):
        self.x = x
        self.y = y
    def abs_fill(self,x=0,y=0,bid=0):
        data[y][x] = bid
    def fill(self,addx=0,addy=0,bid=0):
        if (0 <= self.y+addy < whole_height) and (0 <= self.x+addx < width):
            data[self.y+addy][self.x+addx] = bid
    def fills(self,bid=0,*adds):
        for addx,addy in adds:
            self.fill(addx,addy,bid)
BR = BlockRender()

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

def make_hill(x,y,*mores):
    '''小丘
       **
      *****
     ******
    ********
    或
     * *
     ***
    ****
    *****
    或
        **
    *** **
    *******
    *******
    或
       *
      ***
     *****
    *******
    或
      ***
     *****
    ********
    ********
    或
     ** **
    *******
    ********
    *********
    或
        *
       **
      *****
    ********
    或
      ****
     *******
    *********
    '''

for i in range(5):
    position_x = random.randint(0,width-1)
    position_y = fake_height
    # 3以及周边放进种树函数。
    plant_tree(position_x,position_y)

for y in data:
    for x in y:
        print(x,end='')
    print()

# 种树(OK)
# 山丘(Doing)
# 洼地
# 山
# 矿洞
# 平台