# 全站最丝滑的加载条
from time import *
import random

class Loadline:
    def __init__(self,length=30,speed=0.05,text='loading...'):
        self.length = length
        self.speed = speed
        self.text = text
    def copyright(self):
        print('全站最丝滑的加载条 by 小轩\nCopyright.INS(c)2015-2022\n逆天小轩保留所有权利')
    def load(self):
        if type(self.speed) in [int,float]:
            for i in range(self.length+1):
                print('\033[100A\033[2J'+self.text+'\n\033[42m'+' '*i+'\033[41m'+' '*(self.length-i)+'\033[0m('+str(round(100/self.length*i,2))+'%/100%)')
                sleep(self.speed)
            print()
        elif type(self.speed) in [tuple,list,set]:
            for i in range(self.length+1):
                print('\033[100A\033[2J'+self.text+'\n\033[42m'+' '*i+'\033[41m'+' '*(self.length-i)+'\033[0m('+str(round(100/self.length*i,2))+'%/100%)')
                sleep(round(random.uniform(self.speed[0],self.speed[1]),6))
            print()
        else:
            print('Param speed must be int,float,tuple,list or set.But now the type is '+type(self.speed))
        
# loadline = Loadline(30,0.04,'loading system config...')
# loadline.load()
print('用法')
print('1.\nloadline = Loadline(加载条长度,每加载一下需要几秒,\'加载显示的内容\')')
print('2.\nloadline = Loadline(加载条长度,(加载一下最快需要几秒,加载一下最慢需要几秒),\'加载显示的内容\')')
print('两种加载条都要加上:\nloadline.load()不然加载条不会来鸟你')