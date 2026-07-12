# -*- coding: utf-8 -*-
import aiml
import sys
import os
 
 
def get_module_dir(name):
 print("module", sys.modules[name])
 path = getattr(sys.modules[name], '__file__', None)
 print(path)
 if not path:
  raise AttributeError('module %s has not attribute __file__' % name)
 return os.path.dirname(os.path.abspath(path))
 
 
alice_path = get_module_dir('aiml') + '\\botdata\\alice'

os.chdir(alice_path)  # 切换到语料库所在工作目录

alice = aiml.Kernel()  # 创建机器人alice对象
alice.learn("startup.xml") # 加载...\\botdata\\alice\\startup.xml
alice.respond('LOAD ALICE') # 加载...\\botdata\\alice目录下的语料库
 
while True:
 message = input("\033[32mEnter your message >> \033[0m")
 if("exit" == message):
  exit()
 response = alice.respond(message) # 机器人应答
 print(response)

