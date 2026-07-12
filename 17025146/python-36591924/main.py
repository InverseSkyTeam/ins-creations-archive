text = """
其他的不想介绍了，重点介绍下排行榜
写入:
from CloudMemorizer.kernel.ranking import *
rank = CloudRanking(cloudid,name) #cloudid为scratch作品id,name为排行榜名称
rank.open(userid) #userid为要读写的用户id
rank.setScore(123) #写入的数据必须为整数,位数尽量不超过15位,否则会被取近似数
rank.close() #可有可无，最好加上
读取:
from CloudMemorizer.kernel.ranking import *
rank = CloudRanking(cloudid,name) #cloudid为scratch作品id,name为排行榜名称
rank.open(userid) #userid为要读写的用户id
data = rank.readRanking()#读取所有用户的分数和排名
userdata = rank.readUser()#读取指定用户的分数\
rank.close()
"""
print(text)