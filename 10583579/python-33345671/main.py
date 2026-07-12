#倒库#何嘉晨专属水印
import requests,json,time,sys#我是水印何嘉晨
from xes import sms,tool,uploader#我是水印何嘉晨
from webbrowser import open_new#我是水印何嘉晨
from os import system#本作品作者何嘉晨
from time import sleep#我是水印何嘉晨
import re#本作品作者何嘉晨
#何嘉晨专属水印
#爬取你关注的人#我是水印何嘉晨
def get_follows(uid):#我是水印何嘉晨
    headers = {#我是水印何嘉晨
    	'accept': 'application/json, text/plain, */*',#本作品作者何嘉晨
    	'accept-encoding': 'gzip, deflate, br',#何嘉晨专属水印
    	'accept-language': 'zh-CN,zh;q=0.9',#本作品作者何嘉晨
    # 	'cookie':cookies,#我是水印何嘉晨
    	'referer': 'https://code.xueersi.com/space/10583579?to=fans',#我是水印何嘉晨
    	'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',#我是水印何嘉晨
    	'sec-ch-ua-mobile': '?0',#我是水印何嘉晨
    	'sec-ch-ua-platform': '"Windows"',#我是水印何嘉晨
    	'sec-fetch-dest': 'empty',#何嘉晨专属水印
    	'sec-fetch-mode': 'cors',#何嘉晨专属水印
    	'sec-fetch-site': 'same-origin',#本作品作者何嘉晨
    	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'#我是水印何嘉晨
    }#何嘉晨专属水印
    page = 1#我是水印何嘉晨
    max_page = 500#何嘉晨专属水印
    fandict = {}#我是水印何嘉晨
    l = [0]#何嘉晨专属水印
    while l != []:#我是水印何嘉晨
        if page >= max_page:#何嘉晨专属水印
            break#我是水印何嘉晨
        print('\033[100A\033[2J\033[100A\033[3J'*8+'正在爬取...'+'\n第'+str(page)+'页\n第'+str(len(fandict))+'位关注\n为爬取更快不显示本页关注信息')#何嘉晨专属水印
        rs = requests.get(f"https://code.xueersi.com/api/space/follows?user_id={uid}&page={page}&per_page=10",headers = headers)#我是水印何嘉晨
        try:#我是水印何嘉晨
            l = json.loads(rs.text)["data"]["data"]#我是水印何嘉晨
        except:#何嘉晨专属水印
            pass#我是水印何嘉晨
        for i in l:#我是水印何嘉晨
            fandict[i["realname"]] = i["id"]#何嘉晨专属水印
            # print(i["realname"]+'的id:',i["id"])#何嘉晨专属水印
        page += 1#本作品作者何嘉晨
    print('\033[100A\033[2J\033[100A\033[3J'*8)#何嘉晨专属水印
    for i in fandict:#何嘉晨专属水印
        print(i+'的id:',fandict[i])#本作品作者何嘉晨
    print('正在导出数据到桌面...')#何嘉晨专属水印
    ask = input("1.要名字和id\n2.只要id\n你要哪个(输入数字)")#我是水印何嘉晨
    name = requests.get(f"https://code.xueersi.com/api/space/profile?user_id={uid}",headers=head).json()["data"]["realname"]#本作品作者何嘉晨
    with open(tool.desk()+'/'+name+'关注的人.txt','w') as f:#我是水印何嘉晨
        if ask == 1:#何嘉晨专属水印
            for i in fandict:#本作品作者何嘉晨
                f.write(i+'的id:'+str(fandict[i])+'\n')#何嘉晨专属水印
            f.close()#本作品作者何嘉晨
        elif ask == 2:#何嘉晨专属水印
            for i in fandict:#本作品作者何嘉晨
                f.write(str(fandict[i])+'\n')#何嘉晨专属水印
            f.close()#本作品作者何嘉晨
    print('导出完毕！')#我是水印何嘉晨
#我是水印何嘉晨
#我是水印何嘉晨
#爬取你的粉丝#我是水印何嘉晨
def get_fans(uid):#本作品作者何嘉晨
    headers = {#何嘉晨专属水印
    	'accept': 'application/json, text/plain, */*',#我是水印何嘉晨
    	'accept-encoding': 'gzip, deflate, br',#本作品作者何嘉晨
    	'accept-language': 'zh-CN,zh;q=0.9',#本作品作者何嘉晨
    # 	'cookie':cookies,#我是水印何嘉晨
    	'referer': 'https://code.xueersi.com/space/10583579?to=fans',#何嘉晨专属水印
    	'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',#何嘉晨专属水印
    	'sec-ch-ua-mobile': '?0',#何嘉晨专属水印
    	'sec-ch-ua-platform': '"Windows"',#何嘉晨专属水印
    	'sec-fetch-dest': 'empty',#本作品作者何嘉晨
    	'sec-fetch-mode': 'cors',#何嘉晨专属水印
    	'sec-fetch-site': 'same-origin',#我是水印何嘉晨
    	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'#我是水印何嘉晨
    }#我是水印何嘉晨
    page = 1#本作品作者何嘉晨
    max_page = 500#我是水印何嘉晨
    fandict = {}#我是水印何嘉晨
    l = [0]#何嘉晨专属水印
    while l != []:#本作品作者何嘉晨
        if page >= max_page:#我是水印何嘉晨
            break#何嘉晨专属水印
        print('\033[100A\033[2J\033[100A\033[3J'*8+'正在爬取...'+'\n第'+str(page)+'页\n第'+str(len(fandict))+'位粉丝\n为爬取更快不显示本页粉丝信息')#何嘉晨专属水印
        rs = requests.get(f"https://code.xueersi.com/api/space/fans?user_id={uid}&page={page}&per_page=10",headers = headers)#本作品作者何嘉晨
        try:#本作品作者何嘉晨
            l = json.loads(rs.text)["data"]["data"]#何嘉晨专属水印
        except:#本作品作者何嘉晨
            pass#本作品作者何嘉晨
        for i in l:#本作品作者何嘉晨
            fandict[i["realname"]] = i["id"]#我是水印何嘉晨
            # print(i["realname"]+'的id:',i["id"])#我是水印何嘉晨
        page += 1#本作品作者何嘉晨
    print('\033[100A\033[2J\033[100A\033[3J'*8)#何嘉晨专属水印
    for i in fandict:#何嘉晨专属水印
        print(i+'的id:',fandict[i])#本作品作者何嘉晨
    print('正在导出数据到桌面...')#本作品作者何嘉晨
    ask = input("1.要名字和id\n2.只要id\n你要哪个(输入数字)")#我是水印何嘉晨
    name = requests.get(f"https://code.xueersi.com/api/space/profile?user_id={uid}",headers=head).json()["data"]["realname"]#何嘉晨专属水印
    with open(tool.desk()+'/'+name+'的粉丝.txt','w') as f:#我是水印何嘉晨
        if ask == 1:#本作品作者何嘉晨
            for i in fandict:#我是水印何嘉晨
                f.write(i+'的id:'+str(fandict[i])+'\n')#本作品作者何嘉晨
            f.close()#我是水印何嘉晨
        elif ask == 2:#何嘉晨专属水印
            for i in fandict:#本作品作者何嘉晨
                f.write(str(fandict[i])+'\n')#本作品作者何嘉晨
            f.close()#我是水印何嘉晨
    print('导出完毕！')#我是水印何嘉晨
#何嘉晨专属水印
#本作品作者何嘉晨
#爬cookie#我是水印何嘉晨
def get_cookies():#何嘉晨专属水印
    cookies = ""#何嘉晨专属水印
    if len(sys.argv) > 1:#本作品作者何嘉晨
        try:#本作品作者何嘉晨
            cookies = json.loads(sys.argv[1])["cookies"]#何嘉晨专属水印
        except:#何嘉晨专属水印
            print("未登录")#本作品作者何嘉晨
            sys.exit(0)#我是水印何嘉晨
    return cookies#我是水印何嘉晨
#本作品作者何嘉晨
#何嘉晨专属水印
#爬取你的id#何嘉晨专属水印
def get_id():#我是水印何嘉晨
    cookie = get_cookies()#何嘉晨专属水印
    id = ''#何嘉晨专属水印
    for i in cookie.split(";"):#我是水印何嘉晨
        id = i[8:] if i[1:7] == "stu_id" else id#我是水印何嘉晨
    return id#本作品作者何嘉晨
#何嘉晨专属水印
#何嘉晨专属水印
#爬取你的个人信息#我是水印何嘉晨
def get_information(id):#何嘉晨专属水印
    head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52"}#我是水印何嘉晨
    response=requests.get(f"https://code.xueersi.com/api/space/profile?user_id={id}",headers=head).json()["data"]#本作品作者何嘉晨
    return response#何嘉晨专属水印
#何嘉晨专属水印
#本作品作者何嘉晨
#自动关注#本作品作者何嘉晨
def follow_person(cookie,follow_name,num):#本作品作者何嘉晨
    id=re.findall(r'\d+',follow_name)[0]#本作品作者何嘉晨
    head={#我是水印何嘉晨
        'cookie':cookie,#何嘉晨专属水印
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.175 Safari/537.36'#本作品作者何嘉晨
    }#何嘉晨专属水印
    if num == 1:#我是水印何嘉晨
        payload={#我是水印何嘉晨
            'followed_user_id': id,#我是水印何嘉晨
            'state': 1#本作品作者何嘉晨
        }#本作品作者何嘉晨
    if num == 2:#我是水印何嘉晨
        payload={#何嘉晨专属水印
            'followed_user_id': id,#本作品作者何嘉晨
            'state': 0#我是水印何嘉晨
        }#我是水印何嘉晨
    response=requests.post("https://code.xueersi.com/api/space/follow",headers=head,data=payload)#何嘉晨专属水印
    if str(response) == "<Response [200]>":#我是水印何嘉晨
        if num == 1:#我是水印何嘉晨
            print("关注成功")#我是水印何嘉晨
        if num == 2:#我是水印何嘉晨
            print("取关成功")#我是水印何嘉晨
    else:#本作品作者何嘉晨
        if num == 1:#何嘉晨专属水印
            print("关注失败")#本作品作者何嘉晨
        if num == 2:#我是水印何嘉晨
            print("取关失败")#何嘉晨专属水印
#我是水印何嘉晨
#我是水印何嘉晨
#自动发评论#我是水印何嘉晨
def send_comment(cookie,content,code_url):#我是水印何嘉晨
    id = int(re.findall("\d+",code_url)[0])#本作品作者何嘉晨
    headers = {
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }
    
    json_data = {
        'appid': 1001108,
        'topic_id': f'CP_{id}',
        'target_id': 0,
        'content': content,
    }
    
    res = requests.post('https://code.xueersi.com/api/comments/submit', headers=headers, json=json_data)
    print(res)#何嘉晨专属水印
    if str(res) == "<Response [200]>":#我是水印何嘉晨
        print("发送成功")#我是水印何嘉晨
    elif str(res) == "<Response [400]>":#本作品作者何嘉晨
        print("发送失败")#何嘉晨专属水印
#本作品作者何嘉晨
#我是水印何嘉晨
#自动点赞#我是水印何嘉晨
def like(cookie,like_url):#本作品作者何嘉晨
    id = int(re.findall(r'\d+',like_url)[0])#本作品作者何嘉晨
    head={#本作品作者何嘉晨
        'cookie':cookie,#本作品作者何嘉晨
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.175 Safari/537.36'#我是水印何嘉晨
    }#何嘉晨专属水印
    pld={"form": "python",#本作品作者何嘉晨
        "id": id,#何嘉晨专属水印
        "lang": "code"}#我是水印何嘉晨
    response=requests.post(f"https://code.xueersi.com/api/python/{id}/like",headers=head,json=pld)#本作品作者何嘉晨
    if str(response) == "<Response [200]>":#何嘉晨专属水印
        print("点赞成功")#我是水印何嘉晨
    elif str(response) == "<Response [400]>":#我是水印何嘉晨
        print("点赞失败")#本作品作者何嘉晨
#本作品作者何嘉晨
#何嘉晨专属水印
#自动点踩#何嘉晨专属水印
def unlike(cookie,unlike_url):#我是水印何嘉晨
    id = int(re.findall(r'\d+',unlike_url)[0])#我是水印何嘉晨
    head={#本作品作者何嘉晨
        'cookie':cookie,#何嘉晨专属水印
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.175 Safari/537.36'#本作品作者何嘉晨
    }#我是水印何嘉晨
    pld={"form": "python",#本作品作者何嘉晨
        "id": id,#我是水印何嘉晨
        "lang": "code"}#何嘉晨专属水印
    response=requests.post(f"https://code.xueersi.com/api/python/{id}/unlike",headers=head,json=pld)#我是水印何嘉晨
    if str(response) == "<Response [200]>":#何嘉晨专属水印
        print("点踩成功")#本作品作者何嘉晨
    elif str(response) == "<Response [400]>":#本作品作者何嘉晨
        print("点踩失败")#本作品作者何嘉晨
#本作品作者何嘉晨
#我是水印何嘉晨
#爬取你是谁#我是水印何嘉晨
def get_name():#我是水印何嘉晨
    return get_information(get_id())['realname']#本作品作者何嘉晨
#何嘉晨专属水印
#我是水印何嘉晨
#爬取你关注了几个人#我是水印何嘉晨
def get_the_number_of_follows():#何嘉晨专属水印
    return get_information(get_id())['follows']#本作品作者何嘉晨
#本作品作者何嘉晨
#我是水印何嘉晨
#爬取你有几个粉丝#我是水印何嘉晨
def get_the_number_of_fans():#何嘉晨专属水印
    return get_information(get_id())['fans']#本作品作者何嘉晨
#我是水印何嘉晨
#本作品作者何嘉晨
#爬取你的头像#本作品作者何嘉晨
def get_profile_photo():#何嘉晨专属水印
    id = get_id()#本作品作者何嘉晨
    head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52"}#何嘉晨专属水印
    url=requests.get(f"https://code.xueersi.com/api/space/profile?user_id={id}",headers=head).json()["data"]["avatar_path"]#何嘉晨专属水印
    open_new(url)#我是水印何嘉晨
#我是水印何嘉晨
#我是水印何嘉晨
#爬取作品信息#本作品作者何嘉晨
def get_code_infomation(code_url):#我是水印何嘉晨
    code_id = int(re.findall(r'\d+',code_url)[0])#何嘉晨专属水印
    head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52"}#我是水印何嘉晨
    url = f"https://code.xueersi.com/api/compilers/v2/{code_id}?id={code_id}"#我是水印何嘉晨
    response = requests.get(url,headers=head)#我是水印何嘉晨
    return json.loads(response.text)#何嘉晨专属水印
#本作品作者何嘉晨
#我是水印何嘉晨
#爬取作品介绍#本作品作者何嘉晨
def get_description(code_url):#何嘉晨专属水印
    return get_code_infomation(code_url)["data"]["description"]#本作品作者何嘉晨
#我是水印何嘉晨
#本作品作者何嘉晨
#爬取作品源码#本作品作者何嘉晨
def get_code(code_url):#何嘉晨专属水印
    return get_code_infomation(code_url)["data"]["xml"]#我是水印何嘉晨
#我是水印何嘉晨
#我是水印何嘉晨
#爬取作品发布时间#何嘉晨专属水印
def get_published_time(code_url):#本作品作者何嘉晨
    return get_code_infomation(code_url)["data"]["published_at"]#我是水印何嘉晨
#何嘉晨专属水印
#何嘉晨专属水印
#爬取作品流行度#何嘉晨专属水印
def get_popular_score(code_url):#何嘉晨专属水印
    return get_code_infomation(code_url)["data"]["popular_score"]#本作品作者何嘉晨
#本作品作者何嘉晨
#本作品作者何嘉晨
#爬取作品观看数#本作品作者何嘉晨
def get_views(code_url):#本作品作者何嘉晨
    return get_code_infomation(code_url)["data"]["views"]#本作品作者何嘉晨
#我是水印何嘉晨
#我是水印何嘉晨
#爬取作品点赞数#我是水印何嘉晨
def get_likes(code_url):#何嘉晨专属水印
    return get_code_infomation(code_url)["data"]["likes"]#何嘉晨专属水印
#何嘉晨专属水印
#我是水印何嘉晨
#爬取作品踩数#何嘉晨专属水印
def get_unlikes(code_url):#本作品作者何嘉晨
    return get_code_infomation(code_url)["data"]["unlikes"]#我是水印何嘉晨
#本作品作者何嘉晨
#本作品作者何嘉晨
#爬取作品收藏数#我是水印何嘉晨
def get_favourite(code_url):#何嘉晨专属水印
    return get_code_infomation(code_url)["data"]["favourite"]#何嘉晨专属水印
#本作品作者何嘉晨
#本作品作者何嘉晨
#爬取作品类型#我是水印何嘉晨
def get_tags(code_url):#何嘉晨专属水印
    return ",".join(get_code_infomation(code_url)["data"]["tags"].split())#我是水印何嘉晨
#我是水印何嘉晨
#本作品作者何嘉晨
#爬取作品改编数#本作品作者何嘉晨
def get_source_code_views(code_url):#本作品作者何嘉晨
    return get_code_infomation(code_url)["data"]["source_code_views"]#何嘉晨专属水印
#本作品作者何嘉晨
#何嘉晨专属水印
#正式开始#何嘉晨专属水印
def start():#我是水印何嘉晨
    methodlist = [get_follows,get_fans,get_id,follow_person,send_comment,like,unlike,get_name,get_the_number_of_follows,get_the_number_of_fans,get_profile_photo,get_code_infomation,get_description,get_code,get_published_time,get_popular_score,get_views,get_likes,get_unlikes,get_favourite,get_tags,get_source_code_views]#何嘉晨专属水印
    print("\033[0m欢迎回来")#何嘉晨专属水印
    print("\033[1;41m01.爬取一个人关注的人  \033[0m")#何嘉晨专属水印
    print("\033[1;43m02.爬取一个人的粉丝    \033[0m")#何嘉晨专属水印
    print("\033[1;42m03.爬取你的id          \033[0m")#本作品作者何嘉晨
    print("\033[1;44m04.自动关注            \033[0m")#我是水印何嘉晨
    print("\033[1;46m05.自动发评论          \033[0m")#本作品作者何嘉晨
    print("\033[1;45m06.自动点赞            \033[0m")#何嘉晨专属水印
    print("\033[1;41m07.自动点踩            \033[0m")#本作品作者何嘉晨
    print("\033[1;43m08.爬取你是谁          \033[0m")#本作品作者何嘉晨
    print("\033[1;42m09.爬取你关注了几个人  \033[0m")#我是水印何嘉晨
    print("\033[1;44m10.爬取你有几个粉丝    \033[0m")#何嘉晨专属水印
    print("\033[1;46m11.爬取你的头像        \033[0m")#本作品作者何嘉晨
    print("\033[1;45m12.爬取作品信息        \033[0m")#何嘉晨专属水印
    print("\033[1;41m13.爬取作品介绍        \033[0m")#我是水印何嘉晨
    print("\033[1;43m14.爬取作品源码        \033[0m")#我是水印何嘉晨
    print("\033[1;42m15.爬取作品发布时间    \033[0m")#本作品作者何嘉晨
    print("\033[1;44m16.爬取作品流行度      \033[0m")#本作品作者何嘉晨
    print("\033[1;46m17.爬取作品观看数      \033[0m")#我是水印何嘉晨
    print("\033[1;45m18.爬取作品点赞数      \033[0m")#何嘉晨专属水印
    print("\033[1;41m19.爬取作品点踩数      \033[0m")#何嘉晨专属水印
    print("\033[1;43m20.爬取作品收藏数      \033[0m")#我是水印何嘉晨
    print("\033[1;42m21.爬取作品改编数      \033[0m")#我是水印何嘉晨
    print("(输入别的编号有彩蛋哦)")#我是水印何嘉晨
    j = input("输入编号:")#本作品作者何嘉晨
    if isinstance(j,float) == False:#何嘉晨专属水印
        try:#何嘉晨专属水印
            j = int(j)#我是水印何嘉晨
        except:#本作品作者何嘉晨
            j = 9999#何嘉晨专属水印
    else:#本作品作者何嘉晨
        j = 9999#本作品作者何嘉晨
    code_url = ""#何嘉晨专属水印
    cookie = ""#本作品作者何嘉晨
    num = ""#本作品作者何嘉晨
    id = ""#何嘉晨专属水印
    content = ""#本作品作者何嘉晨
    if j == 1 or j == 2:#何嘉晨专属水印
        try:#本作品作者何嘉晨
            id = input("请输入你要爬取的这个人的id,不知道自己id的请输入帮助\n")#何嘉晨专属水印
            id = int(id)#何嘉晨专属水印
        except:#本作品作者何嘉晨
            if id == "帮助":#本作品作者何嘉晨
                system("帮助.docx")#我是水印何嘉晨
                sys.exit(0)#本作品作者何嘉晨
            else:#本作品作者何嘉晨
                print("error")#何嘉晨专属水印
                sys.exit(0)#本作品作者何嘉晨
    if j == 4 or j == 5 or j == 6 or j == 7:#本作品作者何嘉晨
        cookie = input("请输入你的cookie,不知道自己cookie的请输入帮助\n")#何嘉晨专属水印
        if cookie == "帮助":#我是水印何嘉晨
            system("帮助.docx")#本作品作者何嘉晨
            sys.exit(0)#本作品作者何嘉晨
    if j == 5:#何嘉晨专属水印
        print("请输入你要发送的评论\n")#本作品作者何嘉晨
        content = str(input(""))#何嘉晨专属水印
    if 11 < j < 22 or j == 5 or j == 6 or j == 7:#何嘉晨专属水印
        code_url = input("请输入作品url\n")#本作品作者何嘉晨
    if j == 4:#何嘉晨专属水印
        num = int(input("1.关注\n2.取关\n"))#本作品作者何嘉晨
        id = input("你要关注/取关的人的id\n")#何嘉晨专属水印
    if j > 21 or j < 1:#本作品作者何嘉晨
        print("                 00           0")#本作品作者何嘉晨
        print("             0000            0")#本作品作者何嘉晨
        print("       000000      0       0")#何嘉晨专属水印
        print("          0   0    0     0    0")#何嘉晨专属水印
        print("           0   0  0          0")#本作品作者何嘉晨
        print("                           0")#我是水印何嘉晨
        print("              0          0")#我是水印何嘉晨
        print("     0000000000000000000      0")#我是水印何嘉晨
        print("            0 0 0             0 ")#我是水印何嘉晨
        print("           0  0  0           0")#何嘉晨专属水印
        print("         0    0    0       0")#何嘉晨专属水印
        print("       0      0      0    0")#我是水印何嘉晨
        print("              0         0")#本作品作者何嘉晨
        sleep(0.5)#本作品作者何嘉晨
        print("      0000000000000000000000")#本作品作者何嘉晨
        print("                0         0")#何嘉晨专属水印
        print("                0        0")#我是水印何嘉晨
        print("          0     0000000")#我是水印何嘉晨
        print("         0      0")#我是水印何嘉晨
        print("       0 0      0")#何嘉晨专属水印
        print("     0     00")#本作品作者何嘉晨
        print("              0000000000")#本作品作者何嘉晨
        print("                0")#本作品作者何嘉晨
        print("        00000000000000000")#何嘉晨专属水印
        print("        0       0       0")#何嘉晨专属水印
        print("        00000000000000000")#我是水印何嘉晨
        print("                0")#本作品作者何嘉晨
        print("                0       0")#何嘉晨专属水印
        print("                0 00000000")#我是水印何嘉晨
        print("          00000000        0")#我是水印何嘉晨
        print("      0000                 0")#我是水印何嘉晨
        sleep(1)#何嘉晨专属水印
        for l in range(10):#何嘉晨专属水印
            for w in range(18):#何嘉晨专属水印
                print(" "*w+"滑呀滑")#本作品作者何嘉晨
                sleep(0.01)#我是水印何嘉晨
            for s in range(18):#何嘉晨专属水印
                print(" "*(18-s)+"滑呀滑")#我是水印何嘉晨
                sleep(0.01)#我是水印何嘉晨
        start()#我是水印何嘉晨
    methodlist = [get_follows,get_fans,get_id(),follow_person,send_comment,like,unlike,get_name(),get_the_number_of_follows(),get_the_number_of_fans(),get_profile_photo,get_code_infomation,get_description,get_code,get_published_time,get_popular_score,get_views,get_likes,get_unlikes,get_favourite,get_tags,get_source_code_views]#何嘉晨专属水印
    if j == 1 or j == 2:#本作品作者何嘉晨
        print(methodlist[j-1](id))#本作品作者何嘉晨
    elif j == 3 or j == 8 or j ==9 or j ==10:#我是水印何嘉晨
        print(methodlist[j-1])#本作品作者何嘉晨
    elif j == 4:#本作品作者何嘉晨
        print(follow_person(cookie,id,num))#我是水印何嘉晨
    elif j == 5:#本作品作者何嘉晨
        print(send_comment(cookie,content,code_url))#何嘉晨专属水印
    elif j == 6 or j ==7:#何嘉晨专属水印
        print(methodlist[j-1](cookie,code_url))#我是水印何嘉晨
    else:#何嘉晨专属水印
        print(methodlist[j-1](code_url))#何嘉晨专属水印
    start()#何嘉晨专属水印
start()#我是水印何嘉晨
