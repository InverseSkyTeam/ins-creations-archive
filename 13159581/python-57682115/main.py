import requests,json,sys
cookie = json.loads(sys.argv[1])["cookies"]
history = ""
while True:
    question = input("请输入：")
    history+="我："+question
    headers = {
        'Cookie':cookie,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }
    token = json.loads(requests.get(url="https://code.xueersi.com/api/ai/auth_by_run_token",headers=headers).text)["data"]["token"]
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }
    data = {"prompt":f"请回答这个问题：“{question}”，这是刚刚的对话记录{history}","history":[],"stream":False,"max_tokens":0}
    ask = json.loads(requests.post("https://codeapi.xueersi.com/ai/aigc/v2/chat",json=data,headers=headers).text)["data"]["message"]["content"]
    print("回答："+ask)
    history+="你："+ask
