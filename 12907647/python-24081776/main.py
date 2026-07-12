import requests
import pygame,sys
print('太伤人心了！！！竟然有人对我上次说素材可以超过20MB是假的不可能！！！说我是纸上谈兵！！！那今天小轩就给你们康康，什么才是实战！！！')
print('我说过，我的素材内存是无限！小A就会有下面几首BGM（background music，背景音乐）！')
head = {
        "Referer": "http://www.htqyy.com/top/hot",
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11",
    }
print('123键（不是数字键区的）切换歌：\n1.破茧\n2.干饭人之歌\n3.九龙赞')
url = 'https://webfs.ali.kugou.com/202108281343/f02041ed88102b4a289ede6164c5ff83/KGTX/CLTX001/56c7d8eeff2d125750dd63a921c5d999.mp3'
url2 = 'https://gm-sycdn.kuwo.cn/110eae4b34d9485feff4162bb325df13/6129ce3c/resource/n2/88/78/3642423505.mp3'
url3 = 'https://win-web-rb01-sycdn.kuwo.cn/fd83548206042f2cf8bc040cb5365e44/6129cc26/resource/n3/83/26/1343223772.mp3'
response = requests.get(url,headers=head)
response2 = requests.get(url2,headers=head)
response3 = requests.get(url3,headers=head)
with open('D:/破茧.mp3','wb') as file:
    file.write(response.content)
    file.close()
with open('D:/干饭人.mp3','wb') as file:
    file.write(response2.content)
    file.close()
with open('D:/九龙赞.mp3','wb') as file:
    file.write(response3.content)
    file.close()
print('\033[1;31m还不信就看源码，一个素材都没有。再不行就不是人了')

pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("我的作品")
pygame.mixer.music.load('D:/破茧.mp3')
pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == ord('1'):
                pygame.mixer.music.load('D:/破茧.mp3')
                pygame.mixer.music.play(-1)
            if event.key == ord('2'):
                pygame.mixer.music.load('D:/干饭人.mp3')
                pygame.mixer.music.play(-1)
            if event.key == ord('3'):
                pygame.mixer.music.load('D:/九龙赞.mp3')
                pygame.mixer.music.play(-1)
    screen.fill((255,255,255))
    pygame.display.update()