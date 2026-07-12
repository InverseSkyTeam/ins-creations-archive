import time
import sys

def to_one(l):
    if type(l) == list:
        s = sum(l)
    else:
        s = l
    s = abs(s)
    while len(str(s)) != 1:
        s = to_one([int(i) for i in list(str(s))])
    return s

def gettimeseed():
    timeseed = round(time.localtime()[5]*int(str(time.time())[-1])/10)
    if timeseed < 10:
        timeseed *= 14
        timeseed -= int(str(round(time.time(),2))[-1])
    if (timeseed % 60) in time.localtime():
        timeseed *= int(str(round(time.time(),3))[-1])
        timeseed %= int(time.localtime()[2])
        timeseed += int(str(round(time.time(),1))[-1])
        timeseed = round(timeseed*1.556*float('0.'+str(time.time()).split('.')[-1]))
    timeseed = to_one(timeseed)
    return timeseed

def setuserseed(n):
    global userseed,infoseed
    userseed = round(ord(str(n))*infoseed//166.235)

infoseed = len(str(sys.argv))//10+len(sys.executable)
maxsizeseed = to_one(sys.maxsize)
platseed = len(sys.platform)
userseed = 1
setuserseed(userseed)

def calcseed():
    global infoseed,maxsizeseed,userseed,platseed
    timeseed = gettimeseed()
    totalseed1 = timeseed*infoseed+maxsizeseed*platseed-userseed%(timeseed+1)
    totalseed2 = (abs(timeseed-platseed-userseed//infoseed)+0.013)**(-platseed)+timeseed*maxsizeseed
    timeseed = gettimeseed()
    totalseed3 = (totalseed1*maxsizeseed-totalseed2*platseed)/(timeseed-userseed)
    totalseed4 = round(((totalseed1*2-(-userseed))%maxsizeseed+timeseed)**maxsizeseed**1.5)
    timeseed = gettimeseed()
    totalseed5 = round(((-abs(totalseed3-totalseed4))*0.2+0.014+totalseed1*userseed//200)*3.5)
    timeseed = gettimeseed()
    totalseed = (totalseed1*totalseed4-totalseed2*totalseed5+totalseed3)*timeseed
    for i in range(maxsizeseed*52):
        totalseed += gettimeseed()
    totalseed = to_one(round(totalseed-totalseed1))
    if abs(totalseed2-totalseed1) < 450:
        return 0
    return totalseed

for i in range(100):
    print(calcseed(),end='')
    time.sleep(0.05)   # 小声咕咕：时间是个关键秘钥！