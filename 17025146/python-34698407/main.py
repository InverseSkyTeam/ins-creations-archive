from XesCloud import *
cloud = XesCloud("num")
cloud.open()
cloud.create()
cloud.write(11)
print(cloud.read())
cloud.close()