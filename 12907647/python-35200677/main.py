print("""这一次是INS™(逆天团队)第二次大会，距离第一次约半年
我们要讨论一下INC接下来的路程
这些日子，我天天\033[1;31m爆肝\033[0m，因为我在整INC逆天聊软件
文件上传终于成功了。
-----------------------------------------------
一、编码
何嘉晨上传了一个python文件，导致所有用户运行时报错。
我看了一下，是编码问题。
以前我们爬取文件，都是
\033[1;32m
response = requests.get(url)
t = response.text
\033[0m
对于非文本文件，我们会发现其中有?乱码
其ascii转换成unicode的字符可以用以下代码得到:
\033[1;32m
print(chr(65533))
\033[0m
于是识别到这个乱码，我们就将其转化为二进制形式:
\033[1;32m
response = requests.get(url)
t = response.content
\033[1;0m
这个倒是会点爬虫的都会，但是当我读取文字时，经常发现俄文、拉丁文乱码
ШБЩжыъРЪЖЁσΤŒёÖŸŒÜÝ
于是我上网找资料，换编码
\033[1;32m
response = requests.get(url)
response.encoding = response.apparent_encoding
normaltext = response.text
bytetext = response.content
\033[1;0m
没有问题，但是过了一天
何嘉晨：|关机.py|
我好奇点开
UnicodeError:........
az，又是编码错误了吗
于是，我再次上网查资料
\033[1;32m
response.encoding = 'utf-8'
response.text.encode('iso-8859-1').decode('gbk')
\033[1;0m
utf-8,utf-16,iso-8859-1,gbk,gbk16超大兼容编码统统无效
我差点放弃的时候，想起记事本有一种格式
py文件有时候也会用这个？
A N S I ? ? ?
于是，完整代码:
\033[1;32m
response = requests.get(url)
try:
    response.encoding = response.apparent_encoding
except:
    response.encoding = 'ANSI'
t = response.text
type_ = 'text'
if chr(65533) in t:
    type_ = 'content'
    t = response.content
\033[1;0m
成功了！！！
-----------------------------------------------
二、存储
吴宇航近期一直说我云存储不用字典
可是字典读取绝对比字符慢，处理也不方便
后来我还是照着他做了
字典提取字符解决要很多split/replace/索引/分片
太烦了！！！！！！！！！！！！！！
但是我还是成功了
坏处:
一次只能上传一个文件
一次只能上传一个链接
表情处理麻烦

好不容易好了吴宇航又嫌我使用怪异的unicode字符
我觉得挺好的，但是这样......
然后还说，字典还要继续改，原本的列表字典嵌套，要变4层嵌套了
wc，这谁hode住
我干脆不干了
后来，我还是决心一肝，文件做完了……
既然文件能变按钮，那表情、链接……
我下决心，不会变4层嵌套，而且连字典也不是了，改回字符串！！！
就用unicode字符！
然后变按钮！
这样还能同时上传多文件！
多链接！


好了，在座的神犇们，有什么看法吗？
（上面还有呢，滚轮送上去）
""")