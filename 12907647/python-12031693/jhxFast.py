from time import *
import os
def pt(text,timed=0.5):
    print(text)
    sleep(timed)
def shut_com():
    os.system('shutdown/s /t 0')