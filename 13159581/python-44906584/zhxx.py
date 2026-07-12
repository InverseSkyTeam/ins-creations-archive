from easygui import *
from pickle import *
import os

xxx = os.getcwd() + "\\信息.txt"
msg = "请填写以下联系方式"
title = "请填写你需要填写的信息"
fieldNames = ["*用户名","*真实姓名","*手机号码","QQ"]
fieldValues = []
fieldValues = multenterbox(msg,title,fieldNames)

file = open(xxx,"wb")
dump(fieldValues,file)
file.close()
