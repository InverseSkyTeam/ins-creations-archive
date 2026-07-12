import requests,json
def new_var(name,value):
    """
    新建一个云变量
    传入：
    name: 云变量名
    value: 云变量值
    
    返回：
    token: 非常重要，关系到云变量的更改
    """
    head = {'Content-Type': 'application/json'}
    URL = "https://chen123666888.pythonanywhere.com/new"
    data = json.dumps({"key": name,"value": value})
    response = requests.post(url=URL,data=data,headers=head)
    return response.json()

def set_var(name,value,token):
    """
    为云变量设置新值
    传入：
    name:  新建云变量时的云变量名
    value: 云变量新值
    token: 新建云变量时给的token
    """
    head = {'Content-Type': 'application/json'}
    URL = "https://chen123666888.pythonanywhere.com/set"
    data = json.dumps({"key": name,"value": value,"token": token})
    response = requests.post(url=URL,data=data,headers=head)
    return response.json()

def remove_var(name,token):
    """
    为云变量设置新值
    传入：
    name:  新建云变量时的云变量名
    token: 新建云变量时给的token
    """
    head = {'Content-Type': 'application/json'}
    URL = "https://chen123666888.pythonanywhere.com/remove"
    data = json.dumps({"key": name,"token": token})
    response = requests.post(url=URL,data=data,headers=head)
    return response.json()

def get_var(name):
    """
    获取云变量值
    传入：
    name:  新建云变量时的云变量名
    """
    head = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"
    }
    URL = f"https://chen123666888.pythonanywhere.com/get?key={name}"
    response = requests.get(URL,headers=head)
    return response.json()
