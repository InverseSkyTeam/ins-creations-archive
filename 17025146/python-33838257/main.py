import sys
import time

def output(text,t):
    for i in text:
        print(i,end="")
        time.sleep(t)
        sys.stdout.flush()
    print("")
    
output("莫名其妙的就破1000粉了？我自己都还不知道，还是别人提醒我的。。。就离谱，发个作品纪念下",0.1)