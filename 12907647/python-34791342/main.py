'''
1.
[{'year':2021,'month':5,'day':12,'hour':18,'minute':45},{'year':2022,'month':2,'day':7,'hour':10,'minute':15}]

2.
用户输入的表达式可以随意变动，以布尔表达式格式呈现，格式如下：
user == 小轩 and (like <= 5 or unlike != 0)
代表的是，user字段为小轩（即作者为小轩），且like字段小于等于5或者unlike字段不为0，那么就过滤掉
user != 小轩 and (like > 5 or unlike == 0)
这个表达式和上面的作用相反，只留下符合条件的
以及过滤：
给定一个列表，每一项都是字典，格式如下
[{'user':'小轩','like':5,'unlike':1},{'user':'吴宇航','like':100,'unlike':0}]
要求根据用户输入的表达式，在3秒内过滤掉所有符合（或不符合）条件的项
'''
from time import *
from liedata import data

new_data = []
command = 'user == "张紫捷" or like <= 40 and unlike != 0'
t = time()

for dic in range(len(data)):
    user = data[dic]['user']
    like = data[dic]['like']
    unlike = data[dic]['like']
    if not eval(command):
        new_data.append(data[dic])

# 输出
# print(new_data)

print('使用秒数:',time()-t)
print('过滤条件:',command)
print('原数据量:',len(data))
print('新数据量:',len(new_data))
print('过滤数据量:',len(data)-len(new_data))
print('\n小轩测试情况:测试30次，平均耗时[0.011]秒，最佳[0.008]秒，最烂[0.013]秒，根据平均耗时，过滤10w条数据需1.1s，100w条数据需11.2s')