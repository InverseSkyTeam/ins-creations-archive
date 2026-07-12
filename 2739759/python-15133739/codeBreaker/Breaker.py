import requests,json
def help_():
    print('''这个api找的我累死了
然后再谷歌翻译找到标签，真#
才找到这些东西，再弄一个tk\n''')
    print('导入codeBreaker文件夹（Breaker.py + tk_helper.py）\n导入方式:from codeBreaker.Breaker import *')
    print('具体用法如下：')
    print('''a = 作品访问器.喜欢(网址) a的值就是点赞数
a = 作品访问器.观看(网址) a的值就是浏览数
a = 作品访问器.源码(网址) 以下不多说了
[略] 作品访问器.作者(网址)
作品访问器.作品名称(网址)
作品访问器.踩(网址) 可以看到踩了
作品访问器.作者主页(网址) 值是主页的网址
作品访问器.发布时间(网址)
作品访问器.更改时间(网址)
作品访问器.作者头像源(网址) 值是头像的网址，可以将图片下载到本地
作品访问器.收藏(网址)
作品访问器.作品说明(网址) 如果没有值，表示无作品说明
作品访问器2.代码多少(网址) 这个是第二个作品访问器
作品访问器2.运行源代码(网址) 这个研究项目不成熟，无法加载素材
作品访问器3.展示(网址) 展示作品综合信息
help_() 输出此帮助
''')
def 版权():
    print('小轩&&宇宙工作室')
class 作品访问器(object):
    @classmethod
    def 喜欢(cls,url):
        pid=str(url.split("id=")[1].split("&")[0])
        pid = 'https://code.xueersi.com/api/compilers/'+pid+'?id='+pid
        headers = {'Content-Type':'application/json'}
        a=requests.get(url=pid, headers=headers)
        sdf=json.loads(a.text)
        return sdf['data']['likes']
    @classmethod
    def 观看(cls,url):
        pid=str(url.split("id=")[1].split("&")[0])
        pid = 'https://code.xueersi.com/api/compilers/'+pid+'?id='+pid
        headers = {'Content-Type':'application/json'}
        a=requests.get(url=pid, headers=headers)
        sdf=json.loads(a.text)
        return sdf['data']['views']
    @classmethod
    def 源码(cls,url):
        pid=str(url.split("id=")[1].split("&")[0])
        pid = 'https://code.xueersi.com/api/compilers/'+pid+'?id='+pid
        headers = {'Content-Type':'application/json'}
        a=requests.get(url=pid, headers=headers)
        sdf=json.loads(a.text)
        return sdf['data']['xml']
    @classmethod
    def 作者(cls,url):
        pid=str(url.split("id=")[1].split("&")[0])
        pid = 'https://code.xueersi.com/api/compilers/'+pid+'?id='+pid
        headers = {'Content-Type':'application/json'}
        a=requests.get(url=pid, headers=headers)
        sdf=json.loads(a.text)
        return sdf['data']['username']
    @classmethod
    def 作品名称(cls,url):
        pid=str(url.split("id=")[1].split("&")[0])
        pid = 'https://code.xueersi.com/api/compilers/'+pid+'?id='+pid
        headers = {'Content-Type':'application/json'}
        a=requests.get(url=pid, headers=headers)
        sdf=json.loads(a.text)
        return sdf['data']['name']
    @classmethod
    def 踩(cls,url):
        pid=str(url.split("id=")[1].split("&")[0])
        pid = 'https://code.xueersi.com/api/compilers/'+pid+'?id='+pid
        headers = {'Content-Type':'application/json'}
        a=requests.get(url=pid, headers=headers)
        sdf=json.loads(a.text)
        return sdf['data']['unlikes']
    @classmethod
    def 作者主页(cls,url):
        pid=str(url.split("id=")[1].split("&")[0])
        pid = 'https://code.xueersi.com/api/compilers/'+pid+'?id='+pid
        headers = {'Content-Type':'application/json'}
        a=requests.get(url=pid, headers=headers)
        sdf=json.loads(a.text)
        return 'https://code.xueersi.com/space/'+str(sdf['data']['user_id'])
    @classmethod
    def 发布时间(cls,url):
        pid=str(url.split("id=")[1].split("&")[0])
        pid = 'https://code.xueersi.com/api/compilers/'+pid+'?id='+pid
        headers = {'Content-Type':'application/json'}
        a=requests.get(url=pid, headers=headers)
        sdf=json.loads(a.text)
        return sdf['data']['published_at']
    @classmethod
    def 更改时间(cls,url):
        pid=str(url.split("id=")[1].split("&")[0])
        pid = 'https://code.xueersi.com/api/compilers/'+pid+'?id='+pid
        headers = {'Content-Type':'application/json'}
        a=requests.get(url=pid, headers=headers)
        sdf=json.loads(a.text)
        return sdf['data']['modified_at']
    @classmethod
    def 作者头像源(cls,url):
        pid=str(url.split("id=")[1].split("&")[0])
        pid = 'https://code.xueersi.com/api/compilers/'+pid+'?id='+pid
        headers = {'Content-Type':'application/json'}
        a=requests.get(url=pid, headers=headers)
        sdf=json.loads(a.text)
        return sdf['data']['user_avatar']
    @classmethod
    def 收藏(cls,url):
        pid=str(url.split("id=")[1].split("&")[0])
        pid = 'https://code.xueersi.com/api/compilers/'+pid+'?id='+pid
        headers = {'Content-Type':'application/json'}
        a=requests.get(url=pid, headers=headers)
        sdf=json.loads(a.text)
        return sdf['data']['favorites']
    @classmethod
    def 作品说明(cls,url):
        pid=str(url.split("id=")[1].split("&")[0])
        pid = 'https://code.xueersi.com/api/compilers/'+pid+'?id='+pid
        headers = {'Content-Type':'application/json'}
        a=requests.get(url=pid, headers=headers)
        sdf=json.loads(a.text)
        return sdf['data']['description']

class 作品访问器2(object):
    @classmethod
    def 运行源代码(cls,url):
        try:
            exec(作品访问器.源码(url))
        except:
            print('来自代码访问器的提示：无法找到源码的素材')
    @classmethod
    def 代码多少(cls,url):
        lenth = len(作品访问器.源码(url))
        if lenth <= 5000:
            return_text = '代码很少，可能很氵，有'+str(lenth)+'个字符，大约有50~100行'
        elif lenth <= 10000:
            return_text = '代码有点少，可能还行，有'+str(lenth)+'个字符，大约有200~300行'
        elif lenth <= 20000:
            return_text = '代码不多不少，如果不是普通python可能还不错，有'+str(lenth)+'个字符，大约有400~600行'
        elif lenth <= 50000:
            return_text = '代码不少，应该还不错，有'+str(lenth)+'个字符，大约有650~1000行'
        elif lenth <= 100000:
            return_text = '代码挺多，可能很棒，'+str(lenth)+'个字符，大约有900~1300行'
        elif lenth <= 200000:
            return_text = '代码老多，大神级别，'+str(lenth)+'个字符，大约有1300~2000行'
        elif lenth <= 300000:
            return_text = '代码超多，大佬级别，'+str(lenth)+'个字符，大约有2200~3000行'
        elif lenth <= 500000:
            return_text = '代码无敌多，无敌级别，'+str(lenth)+'个字符，大约有5000~6000行，但这么多不大对劲'
        else:
            return_text = '代码已经是一个数据，'+str(lenth)+'个字符，有6000行以上，我怀疑这是凑数的！'
        return return_text

class 作品访问器3(object):
    @classmethod
    def 展示(cls,url):
        from codeBreaker import tk_helper
        tk_helper.show_data('作品全面剖析器-|宇宙工作室|小轩&胡锦辉',url)