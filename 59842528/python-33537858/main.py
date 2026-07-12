import requests,sys,json

def getCookies():
    cookies = ""
    if len(sys.argv) > 1:
        try:
            cookies = json.loads(sys.argv[1])["cookies"]
        except:
            pass
    return cookies

cookie=getCookies()#"Cookie": cookie

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",

}

id=""
for i in range(getCookies().find("stu_id=")+7,getCookies().find("stu_id=")+17):
    if getCookies()[i].isdigit():
        id+=getCookies()[i]
    else:
        break

response = requests.get("https://code.xueersi.com/api/space/works?user_id="+str(id)+"&page="+str(i)+"&per_page=10", headers = header)
response.encoding = "UTF-8"
coun=int(response.json()["data"]["total"])

a=0
str1="{"
for i in range (120):

    if(a>2):
        break
    try:
        response = requests.get("https://code.xueersi.com/api/space/works?user_id="+str(id)+"&page="+str(i)+"&per_page=10", headers = header)
        response.encoding = "UTF-8"
        coun=int(response.json()["data"]["total"])
    except:
        break

    for im in range(coun):
        try:

            print("-----------------------------------------------")
            print("作品名称：",response.json()["data"]["data"][im]["name"])
            str1=str1+"\""+response.json()["data"]["data"][im]["name"]+"\" : \""+response.json()["data"]["data"][im]["thumbnail"]+"\" , "
            print("封面网址：",response.json()["data"]["data"][im]["thumbnail"])

            print("点赞：",response.json()["data"]["data"][im]["likes"],"|","踩：",response.json()["data"]["data"][im]["unlikes"],"|","收藏：",response.json()["data"]["data"][im]["favorites"],"|","观看：",response.json()["data"]["data"][im]["views"],"|","改编：",response.json()["data"]["data"][im]["source_code_views"])

            print("评论：",response.json()["data"]["data"][im]["comments"],"|","创建时间：",response.json()["data"]["data"][im]["created_at"],"|","更新时间：",response.json()["data"]["data"][im]["updated_at"],"|","热度：",response.json()["data"]["data"][im]["popular_score"])

            print("作品编号：",response.json()["data"]["data"][im]["id"],"|","语言：",response.json()["data"]["data"][im]["lang"])
            print("-----------------------------------------------")


        except:
            a+=1
            break
print(str1)