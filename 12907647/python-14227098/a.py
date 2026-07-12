import requests,json
def 喜欢(url):
    pid=str(url.split("id=")[1].split("&")[0])
    pid = 'https://code.xueersi.com/api/compilers/'+pid+'?id='+pid
    headers = {'Content-Type':'application/json'}
    a=requests.get(url=pid, headers=headers)
    sdf=json.loads(a.text)
    return sdf['data']['likes']