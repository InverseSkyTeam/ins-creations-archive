import requests
def send_comment(cookie,text,id):
    head = {
        "accept": 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,und;q=0.8',
        'sec-ch-ua': '"Chromium";v="96", " Not A;Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'cookie':cookie,
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.175 Safari/537.36'
    }
    pld = {
        'appid': '1001108',
        'content': text,
        'target_id': 0,
        'topic_id': f"CP_{id}"
    }
    res = requests.post("https://code.xueersi.com/api/comments/submit",headers = head,json = pld)