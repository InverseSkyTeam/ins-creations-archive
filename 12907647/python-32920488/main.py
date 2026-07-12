import requests,json,time
print('将会使用吴宇航的名义以及小轩的改编爬取')
time.sleep(1)
headers = {
	'accept': 'application/json, text/plain, */*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'zh-CN,zh;q=0.9',
# 	'cookie':cookies,
	'referer': 'https://code.xueersi.com/space/17025146?to=fans',
	'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-origin',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
}
uid = input('输入你的社区id号')
page = 1
fandict = {}
l = [0]
while l != []:
    print('\033[100A\033[2J\033[100A\033[3J'*8+'正在爬取...'+'\n第'+str(page)+'页\n第'+str(len(fandict))+'位关注\n为爬取更快不显示本页关注信息')
    rs = requests.get(f"https://code.xueersi.com/api/space/follows?user_id={uid}&page={page}&per_page=10",headers = headers)
    l = json.loads(rs.text)["data"]["data"]
    for i in l:
        fandict[i["realname"]] = i["id"]
        # print(i["realname"]+'的id:',i["id"])
    page += 1
    # time.sleep(0.05)
print('\033[100A\033[2J\033[100A\033[3J'*8)
for i in fandict:
    print(i+'的id:',fandict[i])
print('正在导出数据到桌面...')
with open('../../../../../desktop/关注者数据库.txt','w') as f:
    for i in fandict:
        f.write(i+'的id:'+str(fandict[i])+'\n')
    f.close()
print('导出完毕！')