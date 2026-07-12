from xes.common import*
from a import*
def getuserofthistime():
    try:
        a=getCookies()
        num=a.index("stu_id=")+7
        id=""
        for i in range(num,num+100):
            if a[i]!=";":
                id=id+a[i]
            else:
                break
        user_info=get_info(id) 
        return [id,user_info["name"]]
    except:
        return False
a=getuserofthistime()
if a==False:
    print('你暂未登录学而思账户/doge')
else:
    print("\033[94m尊敬的"+a[1]+"你好!\033[96m欢迎来到本作品")