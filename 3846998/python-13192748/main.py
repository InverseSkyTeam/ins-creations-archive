from meowbit import *
p=Port(1,"ADC")
screen.showText("程序已启动，5秒后开始运行，按a停止",0,30)
sleep(5)
while True:
    v=p.getAnalog()
    screen.showText("音量：",50,50) 
    screen.showText(v,80,50)
    screen.setColor((255,0,0))
    screen.drawRect(10,80,v/25,20,1)
    sleep(1)
    if v>=2000:
        screen.showText("音量过大，请不要制造噪音",5,65) 
        buzzer.melody(2)
        sleep(5)
    screen.fill((0,0,0))