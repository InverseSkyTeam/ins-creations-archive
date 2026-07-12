import time

__import__ = ['time']
__author__ = 'INS逆天小轩'
__copyright__ = '(C)逆天团队2021-2023.\nAll rights reserved.'
__protocol__ = 'GPL3.0 开源协议'

seed = 1
acknum = 2**24

def setseed(s):
    global seed
    seed = s

def settimeseed():
    timeseed = int(time.time() * 100000) % 10000000
    setseed(timeseed)

def probability():
    global seed
    setseed((seed * 1140671485 + 128201163) % acknum)
    return round(seed/acknum,15)

def boolean():
    p = probability()
    if p > 0.5:
        return True
    else:
        return False

def digit():
    return int(probability() * 10)

def random(minn=0,maxn=9,tp='int'):
    r = round((maxn - minn) * probability()) + minn
    if tp == 'float':
        r += probability()
        if r > maxn:
            r -= 1
    return r

def choose(*item):
    item = list(item)
    while len(item) == 1:
        if item == item[0]:
            break
        item = item[0]
        item = list(item)
    return item[random(0,len(item)-1)]

def choose_key(dic):
    return dic[choose(dic)]

settimeseed()