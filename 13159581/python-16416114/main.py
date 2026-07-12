from xes.common import*
from cjy import *
b = cjy()
a=getCookies()
num=a.index("stu_id=")+7
id=""
for i in range(num,num+100):
    if a[i]!=";":
        id=id+a[i]
    else:
        break
if id=="13159581":
    b.c_spark("你是作者本人",10)
elif id=="21893394":
    b.c_spark("你是作者本人",10)
elif id=="17388814":
    b.c_spark("你是荣耀工作室的总经理",10)
elif id=="11571887":
    b.c_spark("你是荣耀工作室的总裁",10)
elif id=="55510057":
    b.c_spark("你是荣耀工作室的总监",10)
else:
    b.c_print('你是外部人员哦,嘿嘿')