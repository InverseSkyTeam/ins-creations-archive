'''
1.
[{'year':2021,'month':5,'day':12,'hour':18,'minute':45},{'year':2022,'month':2,'day':7,'hour':10,'minute':15}]

2.
用户输入的表达式可以随意变动，以布尔表达式格式呈现，格式如下：
user == 小轩 and (like <= 5 or unlike != 0)
代表的是，user字段为小轩（即作者为小轩），且like字段小于等于5或者unlike字段不为0，那么就过滤掉
not (user == 小轩 and (like <= 5 or unlike != 0))
这个表达式和上面的作用相反，只留下符合条件的
以及过滤：
给定一个列表，每一项都是字典，格式如下
[{'user':'小轩','like':5,'unlike':10},{'user':'吴宇航','like':100,'unlike':0}
要求根据用户输入的表达式，在3秒内过滤掉所有符合（或不符合）条件的项
'''
from time import *

# 数据随机产生器
# import random
# for i in range(100):
#     print("{'year':"+str(random.randint(2019,2022))+",'month':"+str(random.randint(1,12))+",'day':"+str(random.randint(1,28))+",'hour':"+str(random.randint(0,23))+",'minute':"+str(random.randint(0,59))+"},")

def sort_data(data,sortmode='UP'):
    # '''数据排序'''
    # if type(data) == dict:
    #     new_data = {}
    #     ld = len(data)
    #     while len(new_data) != ld:
    #         if sortmode == 'UP':
    #             md = min(data)
    #         else:
    #             md = max(data)
    #         new_data[md] = data[md]
    #         del data[md]
    #     return new_data
    # if type(data) == list:
    # -缩进
    new_data = []
    ld = len(data)
    while len(new_data) != ld:
        if sortmode == 'UP':
            md = min(data)
        else:
            md = max(data)
        new_data.append(md)
        data.remove(md)
    return new_data
    # return False

timelist = [
    # 人工数据10条
    {'year':2021,'month':5,'day':12,'hour':18,'minute':45},
    {'year':2022,'month':2,'day':7,'hour':10,'minute':15},
    {'year':2021,'month':5,'day':12,'hour':18,'minute':43},
    {'year':2020,'month':1,'day':29,'hour':20,'minute':3},
    {'year':2022,'month':7,'day':11,'hour':22,'minute':0},
    {'year':2019,'month':7,'day':7,'hour':7,'minute':7},
    {'year':2018,'month':12,'day':21,'hour':19,'minute':23},
    {'year':2022,'month':3,'day':2,'hour':14,'minute':59},
    {'year':2021,'month':11,'day':1,'hour':15,'minute':36},
    {'year':2022,'month':1,'day':31,'hour':21,'minute':14},
    
    # 随机数据300条
    {'year':2022,'month':2,'day':24,'hour':17,'minute':38},
    {'year':2020,'month':2,'day':19,'hour':6,'minute':51},
    {'year':2019,'month':3,'day':14,'hour':6,'minute':55},
    {'year':2021,'month':6,'day':19,'hour':5,'minute':41},
    {'year':2021,'month':12,'day':25,'hour':10,'minute':36},
    {'year':2019,'month':10,'day':2,'hour':16,'minute':55},
    {'year':2019,'month':4,'day':25,'hour':5,'minute':18},
    {'year':2022,'month':9,'day':16,'hour':7,'minute':52},
    {'year':2022,'month':4,'day':9,'hour':17,'minute':12},
    {'year':2021,'month':6,'day':21,'hour':17,'minute':45},
    {'year':2021,'month':9,'day':28,'hour':23,'minute':55},
    {'year':2020,'month':4,'day':24,'hour':10,'minute':24},
    {'year':2020,'month':3,'day':24,'hour':20,'minute':27},
    {'year':2020,'month':7,'day':21,'hour':15,'minute':7},
    {'year':2020,'month':10,'day':12,'hour':21,'minute':12},
    {'year':2019,'month':10,'day':28,'hour':2,'minute':15},
    {'year':2019,'month':9,'day':10,'hour':12,'minute':22},
    {'year':2020,'month':6,'day':9,'hour':11,'minute':29},
    {'year':2020,'month':12,'day':16,'hour':13,'minute':50},
    {'year':2021,'month':7,'day':25,'hour':5,'minute':47},
    {'year':2020,'month':9,'day':7,'hour':10,'minute':59},
    {'year':2021,'month':10,'day':22,'hour':18,'minute':41},
    {'year':2020,'month':9,'day':3,'hour':14,'minute':8},
    {'year':2022,'month':7,'day':12,'hour':12,'minute':57},
    {'year':2021,'month':3,'day':6,'hour':16,'minute':18},
    {'year':2019,'month':8,'day':14,'hour':4,'minute':57},
    {'year':2020,'month':9,'day':26,'hour':8,'minute':46},
    {'year':2021,'month':10,'day':4,'hour':23,'minute':52},
    {'year':2021,'month':9,'day':4,'hour':6,'minute':2},
    {'year':2019,'month':11,'day':8,'hour':12,'minute':9},
    {'year':2021,'month':5,'day':27,'hour':20,'minute':12},
    {'year':2021,'month':11,'day':21,'hour':18,'minute':12},
    {'year':2019,'month':10,'day':5,'hour':5,'minute':38},
    {'year':2019,'month':5,'day':15,'hour':1,'minute':42},
    {'year':2021,'month':5,'day':10,'hour':9,'minute':4},
    {'year':2022,'month':3,'day':14,'hour':1,'minute':48},
    {'year':2019,'month':7,'day':8,'hour':7,'minute':38},
    {'year':2019,'month':6,'day':21,'hour':9,'minute':19},
    {'year':2020,'month':6,'day':10,'hour':1,'minute':34},
    {'year':2022,'month':1,'day':14,'hour':21,'minute':2},
    {'year':2022,'month':8,'day':6,'hour':6,'minute':10},
    {'year':2020,'month':2,'day':7,'hour':4,'minute':11},
    {'year':2019,'month':2,'day':11,'hour':0,'minute':52},
    {'year':2022,'month':11,'day':3,'hour':22,'minute':6},
    {'year':2020,'month':7,'day':18,'hour':23,'minute':23},
    {'year':2022,'month':1,'day':16,'hour':17,'minute':41},
    {'year':2021,'month':4,'day':27,'hour':12,'minute':51},
    {'year':2022,'month':3,'day':3,'hour':4,'minute':23},
    {'year':2021,'month':8,'day':25,'hour':13,'minute':22},
    {'year':2019,'month':12,'day':3,'hour':22,'minute':36},
    {'year':2020,'month':10,'day':28,'hour':22,'minute':44},
    {'year':2019,'month':6,'day':24,'hour':20,'minute':7},
    {'year':2021,'month':3,'day':28,'hour':3,'minute':12},
    {'year':2021,'month':12,'day':4,'hour':23,'minute':6},
    {'year':2019,'month':8,'day':1,'hour':10,'minute':39},
    {'year':2020,'month':8,'day':14,'hour':12,'minute':9},
    {'year':2021,'month':5,'day':19,'hour':3,'minute':10},
    {'year':2022,'month':9,'day':13,'hour':1,'minute':35},
    {'year':2019,'month':11,'day':21,'hour':21,'minute':18},
    {'year':2021,'month':4,'day':28,'hour':15,'minute':49},
    {'year':2021,'month':4,'day':4,'hour':3,'minute':29},
    {'year':2019,'month':2,'day':2,'hour':6,'minute':14},
    {'year':2021,'month':4,'day':13,'hour':3,'minute':57},
    {'year':2021,'month':1,'day':18,'hour':23,'minute':37},
    {'year':2022,'month':11,'day':2,'hour':17,'minute':13},
    {'year':2019,'month':10,'day':14,'hour':6,'minute':44},
    {'year':2019,'month':1,'day':18,'hour':17,'minute':16},
    {'year':2020,'month':12,'day':26,'hour':14,'minute':46},
    {'year':2020,'month':10,'day':5,'hour':21,'minute':55},
    {'year':2020,'month':3,'day':1,'hour':17,'minute':2},
    {'year':2021,'month':6,'day':24,'hour':8,'minute':36},
    {'year':2022,'month':10,'day':12,'hour':18,'minute':30},
    {'year':2019,'month':12,'day':6,'hour':11,'minute':42},
    {'year':2021,'month':5,'day':2,'hour':0,'minute':25},
    {'year':2020,'month':7,'day':23,'hour':7,'minute':14},
    {'year':2022,'month':4,'day':4,'hour':11,'minute':19},
    {'year':2020,'month':11,'day':21,'hour':13,'minute':57},
    {'year':2020,'month':12,'day':18,'hour':20,'minute':49},
    {'year':2022,'month':7,'day':28,'hour':9,'minute':33},
    {'year':2022,'month':1,'day':19,'hour':17,'minute':32},
    {'year':2019,'month':10,'day':14,'hour':0,'minute':40},
    {'year':2021,'month':8,'day':14,'hour':10,'minute':56},
    {'year':2021,'month':6,'day':24,'hour':5,'minute':21},
    {'year':2020,'month':2,'day':13,'hour':8,'minute':42},
    {'year':2020,'month':7,'day':28,'hour':16,'minute':5},
    {'year':2019,'month':11,'day':17,'hour':16,'minute':57},
    {'year':2019,'month':9,'day':26,'hour':15,'minute':55},
    {'year':2021,'month':5,'day':7,'hour':8,'minute':27},
    {'year':2019,'month':11,'day':2,'hour':13,'minute':16},
    {'year':2020,'month':8,'day':2,'hour':19,'minute':25},
    {'year':2022,'month':10,'day':11,'hour':3,'minute':16},
    {'year':2020,'month':2,'day':13,'hour':5,'minute':57},
    {'year':2020,'month':6,'day':24,'hour':9,'minute':6},
    {'year':2019,'month':11,'day':9,'hour':6,'minute':40},
    {'year':2021,'month':8,'day':19,'hour':19,'minute':58},
    {'year':2022,'month':11,'day':12,'hour':11,'minute':1},
    {'year':2022,'month':10,'day':7,'hour':8,'minute':10},
    {'year':2020,'month':1,'day':23,'hour':19,'minute':47},
    {'year':2020,'month':9,'day':6,'hour':18,'minute':1},
    {'year':2021,'month':10,'day':27,'hour':6,'minute':9},
    {'year':2019,'month':1,'day':8,'hour':2,'minute':13},
    {'year':2022,'month':7,'day':12,'hour':17,'minute':41},
    {'year':2020,'month':6,'day':16,'hour':20,'minute':48},
    {'year':2020,'month':1,'day':3,'hour':23,'minute':2},
    {'year':2020,'month':4,'day':4,'hour':19,'minute':1},
    {'year':2020,'month':11,'day':21,'hour':3,'minute':46},
    {'year':2020,'month':10,'day':4,'hour':5,'minute':0},
    {'year':2020,'month':2,'day':10,'hour':2,'minute':47},
    {'year':2020,'month':11,'day':22,'hour':1,'minute':4},
    {'year':2021,'month':4,'day':2,'hour':18,'minute':54},
    {'year':2020,'month':9,'day':15,'hour':13,'minute':12},
    {'year':2020,'month':5,'day':16,'hour':5,'minute':0},
    {'year':2019,'month':2,'day':17,'hour':2,'minute':4},
    {'year':2019,'month':4,'day':13,'hour':22,'minute':58},
    {'year':2020,'month':3,'day':7,'hour':22,'minute':26},
    {'year':2022,'month':2,'day':28,'hour':0,'minute':49},
    {'year':2020,'month':9,'day':10,'hour':14,'minute':37},
    {'year':2022,'month':8,'day':15,'hour':11,'minute':56},
    {'year':2020,'month':12,'day':11,'hour':7,'minute':47},
    {'year':2022,'month':7,'day':9,'hour':12,'minute':46},
    {'year':2019,'month':9,'day':19,'hour':1,'minute':13},
    {'year':2020,'month':6,'day':21,'hour':1,'minute':36},
    {'year':2019,'month':7,'day':5,'hour':0,'minute':57},
    {'year':2022,'month':5,'day':7,'hour':11,'minute':23},
    {'year':2019,'month':1,'day':9,'hour':20,'minute':33},
    {'year':2020,'month':8,'day':15,'hour':4,'minute':32},
    {'year':2020,'month':8,'day':14,'hour':3,'minute':15},
    {'year':2022,'month':2,'day':24,'hour':0,'minute':3},
    {'year':2021,'month':6,'day':17,'hour':22,'minute':2},
    {'year':2022,'month':9,'day':15,'hour':10,'minute':43},
    {'year':2020,'month':8,'day':27,'hour':14,'minute':31},
    {'year':2020,'month':8,'day':17,'hour':0,'minute':17},
    {'year':2022,'month':1,'day':8,'hour':22,'minute':24},
    {'year':2021,'month':7,'day':8,'hour':9,'minute':58},
    {'year':2021,'month':12,'day':3,'hour':19,'minute':27},
    {'year':2022,'month':9,'day':11,'hour':11,'minute':11},
    {'year':2019,'month':5,'day':7,'hour':12,'minute':40},
    {'year':2020,'month':3,'day':4,'hour':9,'minute':52},
    {'year':2022,'month':1,'day':2,'hour':7,'minute':39},
    {'year':2019,'month':12,'day':25,'hour':15,'minute':7},
    {'year':2019,'month':11,'day':27,'hour':19,'minute':42},
    {'year':2021,'month':7,'day':25,'hour':14,'minute':17},
    {'year':2022,'month':4,'day':22,'hour':14,'minute':0},
    {'year':2022,'month':3,'day':8,'hour':4,'minute':56},
    {'year':2021,'month':3,'day':27,'hour':20,'minute':11},
    {'year':2019,'month':10,'day':1,'hour':13,'minute':31},
    {'year':2021,'month':4,'day':1,'hour':0,'minute':58},
    {'year':2019,'month':10,'day':22,'hour':16,'minute':42},
    {'year':2022,'month':8,'day':17,'hour':18,'minute':25},
    {'year':2021,'month':5,'day':3,'hour':20,'minute':51},
    {'year':2022,'month':12,'day':17,'hour':17,'minute':3},
    {'year':2019,'month':11,'day':3,'hour':9,'minute':31},
    {'year':2019,'month':6,'day':27,'hour':18,'minute':39},
    {'year':2020,'month':11,'day':2,'hour':19,'minute':57},
    {'year':2020,'month':3,'day':26,'hour':0,'minute':11},
    {'year':2022,'month':1,'day':5,'hour':15,'minute':27},
    {'year':2020,'month':7,'day':16,'hour':1,'minute':2},
    {'year':2019,'month':6,'day':14,'hour':3,'minute':21},
    {'year':2019,'month':6,'day':13,'hour':21,'minute':20},
    {'year':2021,'month':6,'day':4,'hour':19,'minute':28},
    {'year':2019,'month':10,'day':23,'hour':22,'minute':40},
    {'year':2020,'month':5,'day':21,'hour':21,'minute':14},
    {'year':2020,'month':9,'day':28,'hour':19,'minute':43},
    {'year':2019,'month':6,'day':2,'hour':15,'minute':51},
    {'year':2021,'month':2,'day':3,'hour':2,'minute':19},
    {'year':2021,'month':5,'day':18,'hour':13,'minute':30},
    {'year':2021,'month':11,'day':12,'hour':6,'minute':47},
    {'year':2019,'month':9,'day':3,'hour':21,'minute':58},
    {'year':2021,'month':3,'day':4,'hour':5,'minute':27},
    {'year':2020,'month':11,'day':20,'hour':11,'minute':15},
    {'year':2022,'month':12,'day':13,'hour':18,'minute':9},
    {'year':2019,'month':9,'day':8,'hour':1,'minute':48},
    {'year':2022,'month':3,'day':20,'hour':0,'minute':0},
    {'year':2022,'month':4,'day':18,'hour':13,'minute':16},
    {'year':2019,'month':4,'day':22,'hour':17,'minute':44},
    {'year':2019,'month':10,'day':13,'hour':23,'minute':42},
    {'year':2020,'month':10,'day':14,'hour':15,'minute':50},
    {'year':2021,'month':5,'day':4,'hour':13,'minute':11},
    {'year':2022,'month':10,'day':3,'hour':10,'minute':51},
    {'year':2019,'month':12,'day':8,'hour':18,'minute':41},
    {'year':2021,'month':5,'day':21,'hour':10,'minute':48},
    {'year':2020,'month':1,'day':4,'hour':10,'minute':51},
    {'year':2022,'month':7,'day':10,'hour':16,'minute':54},
    {'year':2022,'month':10,'day':27,'hour':11,'minute':23},
    {'year':2022,'month':8,'day':19,'hour':4,'minute':48},
    {'year':2020,'month':12,'day':24,'hour':23,'minute':7},
    {'year':2020,'month':7,'day':19,'hour':20,'minute':8},
    {'year':2020,'month':11,'day':20,'hour':2,'minute':18},
    {'year':2019,'month':2,'day':22,'hour':12,'minute':52},
    {'year':2022,'month':6,'day':13,'hour':11,'minute':2},
    {'year':2019,'month':7,'day':8,'hour':21,'minute':22},
    {'year':2019,'month':12,'day':5,'hour':18,'minute':29},
    {'year':2022,'month':10,'day':28,'hour':18,'minute':9},
    {'year':2020,'month':11,'day':22,'hour':22,'minute':18},
    {'year':2022,'month':1,'day':11,'hour':11,'minute':34},
    {'year':2021,'month':9,'day':2,'hour':14,'minute':58},
    {'year':2021,'month':2,'day':12,'hour':9,'minute':41},
    {'year':2019,'month':6,'day':24,'hour':0,'minute':20},
    {'year':2020,'month':1,'day':28,'hour':18,'minute':42},
    {'year':2022,'month':2,'day':28,'hour':15,'minute':54},
    {'year':2021,'month':5,'day':12,'hour':10,'minute':10},
    {'year':2021,'month':11,'day':4,'hour':20,'minute':28},
    {'year':2021,'month':11,'day':1,'hour':10,'minute':34},
    {'year':2022,'month':6,'day':24,'hour':17,'minute':11},
    {'year':2021,'month':7,'day':15,'hour':22,'minute':49},
    {'year':2020,'month':9,'day':24,'hour':1,'minute':35},
    {'year':2019,'month':4,'day':28,'hour':22,'minute':42},
    {'year':2021,'month':10,'day':2,'hour':5,'minute':11},
    {'year':2019,'month':8,'day':15,'hour':16,'minute':39},
    {'year':2020,'month':7,'day':23,'hour':4,'minute':41},
    {'year':2022,'month':5,'day':21,'hour':1,'minute':23},
    {'year':2022,'month':1,'day':27,'hour':4,'minute':28},
    {'year':2020,'month':2,'day':21,'hour':8,'minute':19},
    {'year':2020,'month':12,'day':25,'hour':19,'minute':40},
    {'year':2019,'month':12,'day':18,'hour':7,'minute':58},
    {'year':2019,'month':12,'day':22,'hour':3,'minute':43},
    {'year':2021,'month':6,'day':17,'hour':23,'minute':28},
    {'year':2021,'month':11,'day':24,'hour':6,'minute':43},
    {'year':2020,'month':8,'day':5,'hour':6,'minute':32},
    {'year':2022,'month':5,'day':20,'hour':5,'minute':3},
    {'year':2019,'month':11,'day':11,'hour':12,'minute':27},
    {'year':2019,'month':9,'day':5,'hour':3,'minute':43},
    {'year':2021,'month':9,'day':4,'hour':13,'minute':29},
    {'year':2019,'month':12,'day':18,'hour':1,'minute':32},
    {'year':2021,'month':8,'day':23,'hour':18,'minute':26},
    {'year':2019,'month':11,'day':9,'hour':15,'minute':31},
    {'year':2022,'month':7,'day':10,'hour':6,'minute':14},
    {'year':2022,'month':8,'day':6,'hour':0,'minute':56},
    {'year':2022,'month':2,'day':16,'hour':11,'minute':41},
    {'year':2019,'month':4,'day':20,'hour':12,'minute':24},
    {'year':2021,'month':10,'day':16,'hour':23,'minute':28},
    {'year':2020,'month':2,'day':6,'hour':6,'minute':8},
    {'year':2022,'month':9,'day':15,'hour':4,'minute':32},
    {'year':2020,'month':7,'day':19,'hour':5,'minute':24},
    {'year':2019,'month':8,'day':26,'hour':20,'minute':18},
    {'year':2020,'month':2,'day':25,'hour':10,'minute':29},
    {'year':2021,'month':6,'day':14,'hour':13,'minute':59},
    {'year':2022,'month':7,'day':1,'hour':15,'minute':20},
    {'year':2021,'month':1,'day':11,'hour':12,'minute':49},
    {'year':2020,'month':12,'day':24,'hour':18,'minute':31},
    {'year':2019,'month':2,'day':10,'hour':9,'minute':32},
    {'year':2021,'month':7,'day':10,'hour':15,'minute':38},
    {'year':2021,'month':6,'day':4,'hour':15,'minute':21},
    {'year':2020,'month':11,'day':27,'hour':15,'minute':29},
    {'year':2020,'month':5,'day':6,'hour':2,'minute':58},
    {'year':2020,'month':12,'day':7,'hour':4,'minute':29},
    {'year':2019,'month':6,'day':19,'hour':19,'minute':22},
    {'year':2022,'month':1,'day':21,'hour':22,'minute':25},
    {'year':2019,'month':3,'day':1,'hour':0,'minute':23},
    {'year':2019,'month':12,'day':3,'hour':20,'minute':55},
    {'year':2019,'month':11,'day':7,'hour':13,'minute':12},
    {'year':2021,'month':10,'day':8,'hour':19,'minute':56},
    {'year':2020,'month':5,'day':13,'hour':10,'minute':42},
    {'year':2019,'month':1,'day':20,'hour':11,'minute':28},
    {'year':2019,'month':1,'day':11,'hour':16,'minute':23},
    {'year':2021,'month':4,'day':16,'hour':15,'minute':41},
    {'year':2019,'month':4,'day':25,'hour':13,'minute':39},
    {'year':2022,'month':8,'day':21,'hour':12,'minute':39},
    {'year':2021,'month':12,'day':9,'hour':13,'minute':18},
    {'year':2020,'month':4,'day':25,'hour':6,'minute':17},
    {'year':2019,'month':10,'day':23,'hour':20,'minute':20},
    {'year':2019,'month':1,'day':15,'hour':0,'minute':16},
    {'year':2022,'month':11,'day':3,'hour':21,'minute':40},
    {'year':2021,'month':12,'day':1,'hour':22,'minute':31},
    {'year':2020,'month':4,'day':8,'hour':16,'minute':6},
    {'year':2019,'month':9,'day':6,'hour':15,'minute':19},
    {'year':2019,'month':12,'day':24,'hour':1,'minute':16},
    {'year':2021,'month':3,'day':25,'hour':8,'minute':16},
    {'year':2021,'month':7,'day':28,'hour':5,'minute':59},
    {'year':2021,'month':10,'day':19,'hour':13,'minute':12},
    {'year':2022,'month':5,'day':7,'hour':19,'minute':54},
    {'year':2022,'month':11,'day':26,'hour':16,'minute':54},
    {'year':2020,'month':4,'day':8,'hour':7,'minute':41},
    {'year':2019,'month':7,'day':10,'hour':12,'minute':43},
    {'year':2019,'month':1,'day':18,'hour':2,'minute':56},
    {'year':2022,'month':11,'day':20,'hour':7,'minute':41},
    {'year':2022,'month':7,'day':23,'hour':8,'minute':21},
    {'year':2019,'month':6,'day':7,'hour':21,'minute':4},
    {'year':2022,'month':2,'day':27,'hour':6,'minute':3},
    {'year':2019,'month':1,'day':19,'hour':15,'minute':56},
    {'year':2020,'month':10,'day':4,'hour':7,'minute':15},
    {'year':2021,'month':12,'day':10,'hour':14,'minute':42},
    {'year':2020,'month':1,'day':8,'hour':3,'minute':14},
    {'year':2022,'month':10,'day':4,'hour':20,'minute':33},
    {'year':2021,'month':1,'day':24,'hour':21,'minute':34},
    {'year':2020,'month':7,'day':6,'hour':2,'minute':50},
    {'year':2019,'month':12,'day':10,'hour':10,'minute':28},
    {'year':2019,'month':1,'day':26,'hour':6,'minute':58},
    {'year':2022,'month':10,'day':8,'hour':14,'minute':2},
    {'year':2020,'month':5,'day':10,'hour':20,'minute':41},
    {'year':2020,'month':11,'day':20,'hour':10,'minute':8},
    {'year':2019,'month':3,'day':22,'hour':4,'minute':17},
    {'year':2019,'month':4,'day':27,'hour':11,'minute':15},
    {'year':2020,'month':6,'day':23,'hour':17,'minute':38},
    {'year':2020,'month':6,'day':26,'hour':13,'minute':29},
    {'year':2020,'month':2,'day':14,'hour':16,'minute':57},
    {'year':2019,'month':5,'day':16,'hour':6,'minute':31},
    {'year':2020,'month':12,'day':27,'hour':21,'minute':53},
    {'year':2020,'month':10,'day':23,'hour':3,'minute':16},
    {'year':2019,'month':8,'day':18,'hour':13,'minute':41},
]
newlist = []

t = time()

for timedict in timelist:
    y = str(timedict['year'])
    m = timedict['month']
    m = '0'+str(m) if m<10 else str(m)
    d = timedict['day']
    d = '0'+str(d) if d<10 else str(d)
    h = timedict['hour']
    h = '0'+str(h) if h<10 else str(h)
    M = timedict['minute']
    M = '0'+str(M) if M<10 else str(M)
    newlist.append(y+'-'+m+'-'+d+'-'+h+'-'+M)
newlist = sort_data(newlist)

timelist = []

for i in newlist:
    all_ = i.split('-')
    timelist.append({'year':all_[0],'month':all_[1],'day':all_[2],'hour':all_[3],'minute':all_[4]})
    
# 结果
# for i in timelist:
#     print(i)

print(time()-t)