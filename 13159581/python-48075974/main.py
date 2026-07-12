import pystray as stray
from PIL import Image
import os

def oqc():
    icon.stop()

def otk():
    os.system("bq.exe")

image = Image.open("hhh.ico")
menu = (
    stray.MenuItem(text="退出",action=oqc),
    stray.MenuItem(text="打开",action=otk,default=True),
        )
icon = stray.Icon("name",image,"tk便签",menu)

icon.run()
