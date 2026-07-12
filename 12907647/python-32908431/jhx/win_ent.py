from time import *
try:
    import win32con
    import win32api
except:
    try:
        import pypiwin32
    except:
        import pywin32

keydict = {
    'enter':13,'tab':9,'backspace':8,'ctrl':17,'shift':16,'space':32,
    'a':65,'b':66,'c':67,'d':68,'e':69,'f':70,'g':71,
    'h':72,'i':73,'j':74,'k':75,'l':76,'m':77,'n':78,
    'o':79,'p':80,'q':81,'r':82,'s':83,'t':84,'u':85,
    'v':86,'w':87,'x':88,'y':89,'z':90,
    '0':48,'1':49,'2':50,'3':51,'4':52,'5':53,'6':54,'7':55,'8':56,'9':57,
    '#l':37,'#r':39,'#u':38,'#d':40,'#ins':45,'#del':46,'#esc':27,
}

def keyhit(keylist=['enter'],hittimes=10,hit_wait_time=0.11,wait_time=2,tp=True,keydict=keydict):
    time.sleep(wait_time)
    # 算法不好，重复，但是电脑跑得更快
    if tp:
        for i in range(hittimes):
            for x in keylist:
                win32api.keybd_event(keydict[x], 0, 0, 0)
                win32api.keybd_event([keydict][x], 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(hit_wait_time)
    else:
        for i in range(hittimes):
            for x in keylist:
                win32api.keybd_event(keydict[x], 0, 0, 0)
            time.sleep(hit_wait_time)