"""
设计:
总体分为三个部分:
一、Style 用于控制输出的样式和风格
二、Screen 将终端视为屏幕
三、Components 实现不同的终端组件
"""

import sys
import time
import os
from typing import Union,Optional,Callable
import re
import math

__all__ = ["Color"]

# 错误定义
class Error(Exception):
    pass
class StyleError(Error):
    pass
class ScreenError(Error):
    pass
class ComponentsError(Error):
    pass

"""
应支持的颜色类型:
16进制、HSV、RGB、中文颜色、英文颜色
"""
class Color:
    def __init__(self,tp:str,color:Union[str,tuple,list]):
        """
        :param: tp -> 颜色类型
        :param: color -> 颜色
        """
        self._judgeType(tp)
        self.tp = tp
        self.color = color

    ### 以下划线开头的函数应当是无状态的 ###
    def _judgeType(self,tp:str):
        allow = ["hex","hsv","rgb","name"] # 支持的颜色类型
        deny = []
        if tp not in allow:
            raise StyleError("不支持的颜色类型")

    def convertColor(self,tp:str) -> None:
        """
        根据类型对颜色进行转换
        :param: tp -> 要转换为的类型
        """
        self._judgeType(tp)
        if tp == self.tp:
            return
        method:Callable[[]] = getattr(self,"convert_to_" + tp)
        self.color = method(self.tp,self.color)

    def convert_to_hex(self,tp,data:Union[tuple,list]):
        if tp == "rgb":
            r = hex(data[0])[2:]
            g = hex(data[1])[2:]
            b = hex(data[2])[2:]
            r = (2-len(r))*"0"+r
            g = (2-len(g))*"0"+g
            b = (2-len(b))*"0"+b
            return f"#{r}{g}{b}".upper()
        elif tp == "hsv":
            return self.convert_to_hex(self.convert_to_hsv(data))
    def convert_to_hsv(self,tp,data:Union[list,tuple,str]):
        if tp == "rgb":
            '''
            RGB转HSV
            r,g,b在(0-255)
            :param: data -> 传入的rgb或16进制数据
            '''
            r, g, b = data[0]/255, data[1]/255, data[2]/255
            mx, mn = max(r, g, b), min(r, g, b)
            m = mx-mn
            if mx == mn:
                h = 0
            elif mx == r:
                if g >= b:
                    h = ((g-b)/m)*60
                else:
                    h = ((g-b)/m)*60 + 360
            elif mx == g:
                h = ((b-r)/m)*60 + 120
            elif mx == b:
                h = ((r-g)/m)*60 + 240
            if mx == 0:
                s = 0
            else:
                s = m/mx
            v = mx
            return h, s, v
        elif tp == "hex":
            return self.convert_to_hsv("rgb",self.convert_to_rgb("hex",data))
    
    def convert_to_rgb(self,tp:str,data:Union[str,tuple,list]):
        """
        :param: tp -> 当前类型
        """
        if tp == "hex":
            r = Color.hex_to_int(data[1:3])
            g = Color.hex_to_int(data[3:5])
            b = Color.hex_to_int(data[5:])
            return (r,g,b)
        elif tp == "hsv":
            if len(data) != 3 or data[0] > 360 or data[0] < 0 or data[1] > 1 or data[1] < 0 or data[2] > 1 or data[2] < 0:
                raise StyleError("传入的颜色值超出hsv的标准范围")
            h = float(data[0])
            s = float(data[1])
            v = float(data[2])
            h60 = h / 60.0
            h60f = math.floor(h60)
            hi = int(h60f) % 6
            f = h60 - h60f
            p = v * (1 - s)
            q = v * (1 - f * s)
            t = v * (1 - (1 - f) * s)
            r, g, b = 0, 0, 0
            if hi == 0:
                r, g, b = v, t, p
            elif hi == 1:
                r, g, b = q, v, p
            elif hi == 2:
                r, g, b = p, v, t
            elif hi == 3:
                r, g, b = p, q, v
            elif hi == 4:
                r, g, b = t, p, v
            elif hi == 5:
                r, g, b = v, p, q
            r, g, b = int(r * 255), int(g * 255), int(b * 255)
            return r, g, b

    @staticmethod
    def hex_to_int(data:str) -> int:
        """
        :param: data -> 要转换的十六进制数
        """
        length = len(data)
        res = 0
        for i in range(length):
            try:
                res += int(data[i])*(16**(length-1-i))
            except:
                res += (ord(data[i])-64+9)*(16**(length-1-i))
        return res

color = Color("hex","#000000")
color.convertColor("hsv")
print(color.color)