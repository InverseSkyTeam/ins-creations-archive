import requests,json
# cookies = "自己的cookie"
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
page = 1
uid = 17025146
rs = requests.get(f"https://code.xueersi.com/api/space/follows?user_id={uid}&page={page}&per_page=10",headers = headers)
list1 = json.loads(rs.text)["data"]["data"]
for i in list1:
	print(i["id"],i["realname"])