import requests
import json
class CloudCodeRun():
    '''
    language说明
        python3：15
        python2：0
        c++/c：7
        c#：10
        node.js：4
    fileext说明
        python3：py3
        Python2：py
        c++：cpp
        c：c
        c#：cs
        node.js：node.js
    '''
    def __init__(self,language,fileext):
        self.head = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11"}
        self.language = language
        self.fileext = fileext
        
    def pretreatmentCode(self,precode):
        code=""
        for i in precode:
            if i=="\'":
                code+="\'"
            elif i=="\"":
                code+="\""
            else:
                code+=i
        return code
        
    def run(self,code,stdin=""):
        url = "https://tool.runoob.com/compile2.php"
        payload={
            "code": self.pretreatmentCode(code),
            "token": "4381fe197827ec87cbac9552f14ec62a",
            "stdin": stdin,
            "language": self.language,
            "fileext": self.fileext
        }
        r=requests.post(url,headers=self.head,data=payload)
        print(r)
        if(r.json()!=''):
            print(r.json()['output'])
            print(r.json()['errors'])
            return (r.json()['output'],r.json()['errors'])
        else:
            return "数据有误，请按照上边填写数据"
        
pycoder=CloudCodeRun(15,"py3")
cppcoder=CloudCodeRun(7,"cpp")
codepy='''
a=1
b=2
print(a+b)
'''
codecpp='''
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n=2;
    for(int i=0;i<=10;i++)
        cout<<(n<<i)<<" ";
    cout<<endl;
    n=2048;
    for(int i=0;i<=10;i++)
        cout<<(n>>i)<<" ";
    return 0;
}
'''
pycoder.run(codepy)
cppcoder.run(codecpp)