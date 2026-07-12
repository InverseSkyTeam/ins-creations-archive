# 总值 = 100
print('统计并计算未来可能性概率')
print('版本：alpha-sp-0.1')
print('类型：特殊(Special,简称sp)处理化（效率垃圾）')
print('因素：14个（极少）')
print('误差：±23.333%')
print('内容：预测一周内我们班不会发生坏事的概率')
print('算法：小白算法，很垃圾')
event_value = 100
factor1 = 0.976   # 混乱时局97.6%
factor2 = 0.994   # 压力99.4%
factor3 = 0.984   # 同学之间不信任
factor4 = 0.998   # 打架/吵架
factor5 = 0.999   # 随机事件
factor6 = 0.993   # 讨厌老师
factor7 = 0.999   # 隔阂
factor8 = 0.989   # 懒
factor9 = 0.999   # 随机事件
factor10 = 0.998   # 其他事件
factor11 = 0.997   # 烦
factor12 = 0.999   # 考试
factor13 = 0.999   # 随机事件
factor14 = 1.03   # 有利因素
for day in range(7): # 一周过去了！
    for i in range(1,15): # 乘上概率
        event_value *= eval('factor'+str(i))
print(event_value,end='') # 结果
print('%')

import random
print('\033[1;33m统计并计算未来可能性概率(每次运行结果均不同，如果相同你都可以去中1w亿的彩票了)')
print('版本：alpha-sp-0.2')
print('类型：特殊(Special,简称sp)处理化（效率垃圾）')
print('因素：14个（极少）')
print('误差：±17.69%')
print('内容：预测一周内我们班不会发生坏事的概率')
print('算法：小白算法，很垃圾')
event_value = 100
factor1 = 0.976
factor2 = 0.994
factor3 = 0.984
factor4 = 0.998
factor5 = 0.999
factor6 = 0.993
factor7 = 0.999
factor8 = 0.989
factor9 = 0.999
factor10 = 0.998
factor11 = 0.997
factor12 = 0.999
factor13 = 0.999
factor14 = 1.03
for day in range(7):
    for i in range(14):
        event_value *= eval('factor'+str(random.choice([x for x in range(1,13) for n in range(10)]+[14 for m in range(7)]))) # 随机了
print(event_value,end='') # 结果
print('%')

print('\033[1;32m统计并计算未来可能性概率(每次运行结果均不同，如果相同你都可以去中1w亿的彩票了)')
print('版本：alpha-sp-0.3')
print('类型：特殊(Special,简称sp)处理化（效率垃圾）')
print('因素：14个（极少）')
print('误差：±16.666%')
print('内容：预测一周内我们班不会发生坏事的概率')
print('算法：垃圾小白算法')
event_value = 100
factor1 = 0.976
factor2 = 0.994
factor3 = 0.984
factor4 = 0.998
factor5 = 0.999
factor6 = 0.993
factor7 = 0.999
factor8 = 0.989
factor9 = 0.999
factor10 = 0.998
factor11 = 0.997
factor12 = 0.999
factor13 = 0.999
factor14 = 1.035
for day in range(7):
    for i in range(14):
        event_value *= eval('factor'+str(random.choice([x for x in range(1,13) for n in range(10)]+[14 for m in range(8)]))) # 随机了
print(event_value,end='') # 结果
print('%')