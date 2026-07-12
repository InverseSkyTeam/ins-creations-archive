from meowbit import *
p=Port(3,"IN")
p1=Port(2,"PWM")
p1.setAnalog(0)
screen.showText("程序已启动，5秒后开始运行",0,30)
sleep(5)
while True:
    v=p.getDigital()
    if v==0:
        screen.showText("倾倒！风扇关闭。",30,50)
        p1.setAnalog(0)
        buzzer.melody(2)
        sleep(5)
    else:
        screen.showText("正常。风扇满速转动。",20,50) 
        p1.setAnalog(255)
    sleep(1)
    screen.fill((0,0,0))