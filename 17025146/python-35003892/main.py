import requests
import json
from win10toast import ToastNotifier
import time

toast = ToastNotifier()
cookie = input('键入你的cookie:')
headers = {
    'Cookie':cookie,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
url = 'https://code.xueersi.com/api/messages/overview'
while True:
    response = requests.get(url,headers=headers)
    data = json.loads(response.text)['data'][0]['count']
    if data:
        toast.show_toast(title="有新消息", msg=f"有{data}条消息",duration=10)
    else:
        print('无消息')
    time.sleep(3) #等待3秒,避免请求频繁