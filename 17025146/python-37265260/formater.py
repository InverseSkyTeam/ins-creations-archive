from typing import Union, Optional
import re


def fillton(text: Union[str, int], n: int, fill: str) -> str:
    text = str(text)
    leng = len(text)
    if leng < n:
        text = fill * (n - leng) + text
        return text
    else:
        return text


def removefill(text: str, fill: str) -> str:
    text = str(text)
    num = 0
    for i in text:
        if i == fill:
            num += 1
        else:
            break
    return text[num:]


def toint(data: list) -> list:
    target = []
    for i in data:
        if i != "000":
            target.append(int(removefill(i, "0")))
        else:
            target.append(0)
    return target


def cuttext(text: str, lenth: int) -> list:
    textArr = re.findall('.{' + str(lenth) + '}', text)
    textArr.append(text[(len(textArr) * lenth):])
    if len(text) % lenth == 0:
        return textArr[0:-1]
    else:
        return textArr


def list2int(userlist: list) -> dict:
    """
    传入数据结构
    [
        [name,[x,y],(r,g,b),is_win]
        [......]
    ]
    返回数据结构
    {
        "name":[xy-int,rgb-int,is_win]
        ......
    }
    """
    target = {}
    for i in userlist:
        rgb = list(i[2])
        for x in range(len(rgb)):
            rgb[x] = fillton(rgb[x], 3, "0")
        rgb = "1" + "".join(rgb)
        x, y = i[1]  # 解包x,y
        x = fillton(x, 3, "0")
        y = fillton(y, 3, "0")
        xy = "1" + x + y
        target[i[0]] = [xy, rgb, i[3]]
    return target


def int2list(data: dict) -> list:
    target = []
    for i in data:
        d = data[i]
        xy, rgb, is_win = d
        rgb = rgb[1:]
        xy = xy[1:]
        rgblist = cuttext(rgb, 3)
        xylist = cuttext(xy, 3)
        x, y = toint(xylist)
        r, g, b = toint(rgblist)
        target.append([i, [x, y], (r, g, b), is_win])
    return target
