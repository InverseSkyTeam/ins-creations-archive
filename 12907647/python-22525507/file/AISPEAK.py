'''
衷心感谢#学而思编程#
'''
from time import *
from xes import (common,ext)
import requests
import pygame

# pygame.init()

g_gender="male"
g_rate=None
g_pitch=None

def setmode(gender):
    if gender == "boy":
        gender = "male"
    elif gender == "girl":
        gender = "female"
    global g_gender
    g_gender = gender

def setspeed(rate):
    if not isinstance(rate, int) and not isinstance(rate, float):
        raise Exception("语速设置功能参数范围为0-2，调整下参数范围吧")
    if rate < 0 or rate > 2:
        raise Exception("语速设置功能参数范围为0-2，调整下参数范围吧")
    global g_rate
    g_rate = rate

def aispeak(text):
    text = text.strip()
    if text == "":
        raise Exception("文本不能为空")
    global g_gender,g_rate,g_pitch
    params = {"text":text,"gender":g_gender,"rate":g_rate,"pitch":g_pitch}
    cookies = common.getCookies()
    headers = {"Cookie": cookies}
    rep = requests.get("https://code.xueersi.com/api/ai/python_tts/tts", params=params, headers=headers)
    repDic = common.jsonLoads(rep.text)
    if repDic is None:
        raise Exception("微软语言服务请求超时，请稍后再试")

    if repDic["stat"] != 1:
        raise Exception(repDic["msg"])

    voiceUrl = repDic["data"]["url"]
    duration = repDic["data"]["duration"]
    r = requests.get(voiceUrl)
    filename = 'newsound.wav'
        
    with open(filename, "wb") as f:
        f.write(r.content)
    f.close()
    return [filename,duration]