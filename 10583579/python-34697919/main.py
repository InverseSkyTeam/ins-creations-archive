from XesCloud import *
import time
cloud = XesCloud("num",22189899)
cloud.open()
t = time.time()
for i in range(101):
    cloud.write(1)
cloud.read()
print(time.time()-t)