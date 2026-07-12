from meowbit import *
p=Port(3,"IN")
screen.showText("程序已启动，5秒后开始运行",0,30)
sleep(5)
while True:
    v=p.getDigital()
    if v==0:
        screen.showText("倾倒！",60,50)
        buzzer.melody(2)
        sleep(5)
    else:
        screen.showText("正常。",60,50) 
    sleep(1)
    screen.fill((0,0,0))