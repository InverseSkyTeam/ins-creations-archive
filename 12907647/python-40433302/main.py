from base64 import *
message = 'a bc->1 23\n该方法可以处理吴宇航版本CCP返回代码中中文无法正常解码的问题'
msg = b64encode(message.encode())
msg2 = b64decode(msg)
print('加密(1种)与解密(2种)：',msg,str(msg2,'utf-8'),msg2.decode(),sep='\n\n\n')