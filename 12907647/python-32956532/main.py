try:
    import win32con
    import win32api
except:
    import pypiwin32
import time
print('步骤：把输入框的发送方式改为回车就发送的')
x = int(input('输入刷屏的条数(输入的条数太多刷卡你电脑不偿命)'))
input('回车开始，然后请在3秒后把光标移到微信/qq/腾讯会议等输入框（在班级群等里面刷屏后果自负）')
time.sleep(3)
for i in range(x):
    win32api.keybd_event(97, 0, 0, 0)   # 1
    win32api.keybd_event(13, 0, 0, 0)   # Enter
    # time.sleep(0.06)