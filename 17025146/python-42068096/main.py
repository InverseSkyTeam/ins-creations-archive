import os,hashlib
from xes import uploader
import shutil,requests,json,bs4
class up(object):
    def _getUploadParams(self, filename, md5):
        url = 'https://code.xueersi.com/api/assets/get_oss_upload_params'
        params = {"scene": "offline_python_assets", "md5": md5, "filename": filename}
        response = requests.get(url=url, params=params)
        data = json.loads(response.text)['data']
        return data
    def uploadAbsolutePath(self, filepath):
        md5 = None
        contents = None
        fp = open(filepath, 'rb')
        contents = fp.read()
        fp.close()
        md5 = hashlib.md5(contents).hexdigest()

        if md5 is None or contents is None:
            raise Exception("文件不存在")

        uploadParams = self._getUploadParams(filepath, md5)
        requests.request(method="PUT", url=uploadParams['host'], data=contents, headers=uploadParams['headers'])
        return uploadParams['url']
def selectfile(filenm):
    if filenm:
        file=open(filenm)
        myuploader=up()
        url=myuploader.uploadAbsolutePath(filenm)
    return url
def w(nr):
    with open("user.txt","w",encoding="utf-8") as az:
        az.write(nr)
    users = selectfile("user.txt")
    usernm = users.replace("https://livefile.xesimg.com/programme/python_assets/","").replace(".txt","")
    return usernm
def r(zh):
    head1 = {
    	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        }
    response = requests.get("https://livefile.xesimg.com/programme/python_assets/" + zh + ".txt",headers = head1).content
    ss = response.decode("utf-8")
    return ss
    
t = '''
def main(data):
    return """
    <html>
        <body>
            <h1>Hello,{}</h1>
        </body>
    </html>
    """.format(data["name"])
'''
def run(url,data):
    code = r(url)
    exec(code)
    fun = eval("main")
    return fun(data)
# print(w(t))
text = run("219e547979aed9ba2a849bf380ddae16",{"name":"小明"})
with open("hello.html","w",encoding="utf-8") as f:
    f.write(text)
import webbrowser as wb
wb.open("hello.html")