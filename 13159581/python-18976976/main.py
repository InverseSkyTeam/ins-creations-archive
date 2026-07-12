from urllib.request import *
a = urlopen("https://placekitten.com/634/675")
b = a.read()
with open("E:\\miaomiao.jpg",'wb') as f:
    f.write(b)