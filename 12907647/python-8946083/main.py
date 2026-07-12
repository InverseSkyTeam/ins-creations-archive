import pygame,sys,random,os,tkinter as tk
from time import *
pygame.init()
print('室长小轩亲手制作')
print('点黑色窗口右上角的X关闭窗口有彩蛋然后开始游戏')
sleep(1)
import spaceSign

part = 0
chance = 5
chance_add = 0
score = 0
coins = 580
speed = 0.40
bulletRectSize = 25
flag = 'No ?'
guan_2_is_via = False
rainp = False

try:import ntpath
except:osingxing = 'MacOs';font = pygame.font.SysFont('kaittf', 30);font2 = pygame.font.SysFont('kaittf', 20)
else:osingxing = 'Windows';font = pygame.font.SysFont('kaiti', 30);font2 = pygame.font.SysFont('kaiti', 20);del ntpath

class music_play(object):
    def __init__(self):
        self.init_play_jhx = 'init_play'
    
    @classmethod
    def load_music(cls):
        pygame.mixer.music.load('黑客帝国.mp3')
    
    @classmethod
    def play_music(cls,condition):
        global flag
        if condition:
            pygame.mixer.music.play(-1)
            flag = '?'
    
    @classmethod
    def stop_music(cls,condition):
        global flag
        if condition:
            pygame.mixer.music.stop()
            flag = 'No ?'
            
music_play.load_music()
music_play.play_music(flag=='No ?')



while True:
    pygame.init()
    while part == 0:
        chance = 5
        score = 0
        root = tk.Tk()
        root.geometry('300x400')
        root.title('大战外星电脑-选关')
        
        bulletImg = pygame.transform.scale(pygame.image.load("子弹.png"),(bulletRectSize,bulletRectSize))
        bulletRect = bulletImg.get_rect()
        bulletRect.width = bulletRect.height = bulletRectSize
        
        def great1():
            global part,chance
            part = 1
            chance = chance + chance_add
            root.destroy()
        def great2():
            global part,chance
            part = 2
            chance = chance + chance_add
            root.destroy()
        def great3():
            global part,chance
            part = 3
            chance = chance + chance_add
            root.destroy()
        def boss():
            global part,chance
            part = 111
            chance = chance + chance_add
            root.destroy()
        def Music():
            global music_play,flag
            if flag == 'No ?':
                music_play.play_music(flag=='No ?')
            else:
                music_play.stop_music(flag=='?')
        def helpG():
            helpW=tk.Toplevel(root)
            helpW.geometry('400x400')
            helpW.title('攻略 help 共4条')
            label = tk.Label(helpW,text='1.越靠近怪物能让怪物下落得越慢，但故意会让战场不停地闪\n2.如果你打完第二关所有怪物，你就解锁第3关、Boss，老怪都有很多金币\n3.1~3关生命值在左上角，变成了血量条，音乐给你带来动感\n4.如果你编程好，不要看源码、改编，注意游戏有趣性，发现抄袭直接。。。\n',bg='yellow')
            label.pack()
        def rain():
            global rainp
            rainp = True
            t1 = time()
            window=tk.Toplevel(root)
            window.geometry('300x400')
            def coin666():
                global coins
                coins += random.randint(10,30)
                t2 = time()
                if t2 - t1 > 5:
                    window.destroy()
            a = tk.Button(window,text='猛戳拿金币',bg='red',command=coin666)
            a.pack()
        def Store():
            window=tk.Toplevel(root)
            window.geometry('300x400')
            window.title('Hero Store City')
            def buy1():
                global coins,speed
                if coins >= 100:
                    coins -= 100
                    speed -= 0.05
            def buy2():
                global coins,chance_add
                if coins >= 500:
                    coins -= 500
                    chance_add += 5
            def buy3():
                global coins,bulletRectSize
                if coins >= 500:
                    coins -= 500
                    bulletRectSize += 10
                pass
            def close_Store():
                window.destroy()
            button1 = tk.Button(window,text='(100金币)游戏速度+',bg='blue',command=buy1)
            button2 = tk.Button(window,text='(500金币)电脑生命+',bg='green',command=buy2)
            button3 = tk.Button(window,text='(500金币)子弹大小+',bg='yellow',command=buy3)
            button4 = tk.Button(window,text='关闭窗口',bg='orange',command=close_Store)
            button1.pack()
            button2.pack()
            button3.pack()
            button4.pack()
        
        button1 = tk.Button(root,text='第1关（ROUND 1:Easy）',bg='blue',command=great1)
        button2 = tk.Button(root,text='第2关（ROUND 2:Normal）',bg='green',command=great2)
        if guan_2_is_via == True:
            button3 = tk.Button(root,text='第3关（ROUND 3:Hard）',bg='orange',command=great3)
            button4 = tk.Button(root,text='挑战Boss（FAINL ROUND:Insane）',bg='red',command=boss)
        else:
            button3 = tk.Button(root,text='锁',bg='orange')
            button4 = tk.Button(root,text='锁',bg='red')
        button5 = tk.Button(root,text='商城（Hero Store City）',bg='#b06ca8',command=Store)
        TextButton = tk.Button(root,text='金币数：'+str(coins))
        mButton = tk.Button(root,text='音乐器开/关',bg='yellow',command=Music)
        helpButton = tk.Button(root,text='攻略',bg='orange',command=helpG)
        rain = tk.Button(root,text='金币雨',bg='red',command=rain)
        label = tk.Label(root,text='')
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        label.pack()
        button5.pack()
        TextButton.pack()
        mButton.pack()
        helpButton.pack()
        if rainp == False:
            rain.pack()
        root.mainloop()
        
        screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption("大战外星电脑")
        myImg = pygame.image.load("computer.png")
        myRect = myImg.get_rect()
        
        mPos = [0,0]
        enemyList = []
        bulletList = []
        t1 = time()
        t3 = time()
    
    
    
    while part == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.MOUSEMOTION:
                mPos = event.pos
        
        if chance <= 0:
            part = 0
        
        screen.fill((25,200,255))
        myRect.center = mPos
        screen.blit(myImg,myRect)
        screen.blit(font.render(('有怪 '+str(30-score)),True,(0,0,0)),(0,0))
        screen.blit(font.render(' '*chance,True,(0,0,255),(0,0,255)),(0,30))
        
        t2 = time()
        t4 = time()
        
        if 30 - score == 0:
            part = 0
        if t2 > t1 + speed:
            bullet = {
                "surface": bulletImg,
                "rect": pygame.Rect(myRect.x + (myRect.width-bulletRect.width) / 2, myRect.y, \
                                    bulletRect.width, bulletRect.height),
                "move_x": 0,
                "move_y": -15
            }
            bulletList.append(bullet)
            t1 = t2
        if t4 > t3 + 1.5:
            if score <= 30:
                enemy = {
                        "rect": pygame.Rect(375,-100,50,50),
                        "move_x": 0,
                        "move_y": 1,
                        "life": random.randint(1,3)
                    }
                if enemy['life'] <= 3:
                    enemy['color'] = (0,100,255)
                elif enemy['life'] <= 8:
                    enemy['color'] = (10,255,5)
                elif enemy['life'] <= 15:
                    enemy['color'] = (200,100,20)
                else:
                    enemy['color'] = (255,10,0)
                enemyList.append(enemy)
                t3 = t4
        
        for a1 in bulletList:
            a1["rect"].move_ip(a1["move_x"],a1["move_y"])
            if a1["rect"].top < 0:
                bulletList.remove(a1)
            screen.blit(a1["surface"],a1["rect"])
            for b1 in enemyList:
                b1["rect"].move_ip(b1["move_x"], b1["move_y"])
                if b1["rect"].top > 800:
                    enemyList.remove(b1)
                    chance -= b1['life']
                    if score < 30:
                        score += 1
                if b1["rect"].colliderect(a1["rect"]):
                    try:
                        bulletList.remove(a1)
                        b1['life'] -= 1
                    except:
                        pass
                if b1['life'] <= 0:
                    enemyList.remove(b1)
                    if score < 30:
                        score += 1
                    coins += random.randint(1,3)
                pygame.draw.rect(screen,b1["color"],b1["rect"],0)
                screen.blit(font2.render(str(b1['life']),True,(0,0,0)),(b1['rect'].center[0]-10,b1['rect'].center[1]-10))
        
        pygame.mouse.set_visible(False)
        pygame.display.update()
        pygame.time.delay(25)
    
    while part == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.MOUSEMOTION:
                mPos = event.pos
        
        if chance <= 0:
            part = 0
        
        screen.fill((25,200,255))
        myRect.center = mPos
        screen.blit(myImg,myRect)
        screen.blit(font.render(('有怪 '+str(50-score)),True,(0,0,0)),(0,0))
        screen.blit(font.render(' '*chance,True,(0,0,255),(0,0,255)),(0,30))
        
        t2 = time()
        t4 = time()
        
        if 50 - score == 0:
            guan_2_is_via = True
            part = 0
        if t2 > t1 + speed:
            bullet = {
                "surface": bulletImg,
                "rect": pygame.Rect(myRect.x + (myRect.width-bulletRect.width) / 2, myRect.y, \
                                    bulletRect.width, bulletRect.height),
                "move_x": 0,
                "move_y": -15
            }
            bulletList.append(bullet)
            t1 = t2
        if t4 > t3 + 1.5:
            if score <= 50:
                enemy = {
                        "rect": pygame.Rect(random.randint(0,750),-100,50,50),
                        "move_x": 0,
                        "move_y": 1,
                        "life": random.randint(1,10)
                    }
                if enemy['life'] <= 3:
                    enemy['color'] = (0,100,255)
                elif enemy['life'] <= 8:
                    enemy['color'] = (10,255,5)
                elif enemy['life'] <= 15:
                    enemy['color'] = (200,100,20)
                else:
                    enemy['color'] = (255,10,0)
                enemyList.append(enemy)
                t3 = t4
        
        for a1 in bulletList:
            a1["rect"].move_ip(a1["move_x"],a1["move_y"])
            if a1["rect"].top < 0:
                bulletList.remove(a1)
            screen.blit(a1["surface"],a1["rect"])
            for b1 in enemyList:
                b1["rect"].move_ip(b1["move_x"], b1["move_y"])
                if b1["rect"].top > 800:
                    enemyList.remove(b1)
                    chance -= b1['life']
                    if score < 50:
                        score += 1
                if b1["rect"].colliderect(a1["rect"]):
                    try:
                        bulletList.remove(a1)
                        b1['life'] -= 1
                    except:
                        pass
                if b1['life'] <= 0:
                    enemyList.remove(b1)
                    if score < 50:
                        score += 1
                    coins += random.randint(1,10)
                pygame.draw.rect(screen,b1["color"],b1["rect"],0)
                screen.blit(font2.render(str(b1['life']),True,(0,0,0)),(b1['rect'].center[0]-10,b1['rect'].center[1]-10))
        
        pygame.mouse.set_visible(False)
        pygame.display.update()
        pygame.time.delay(50)
    
    while part == 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.MOUSEMOTION:
                mPos = event.pos
        
        if chance <= 0:
            part = 0
            
        try:
            badBig
        except:
            badBig = {
                        "surface": pygame.image.load('badBig.png'),
                        "move_x": 0,
                        "move_y": 0,
                        "life": 50
                    }
            badBig['rect'] = badBig['surface'].get_rect()
            badBig['rect'].x = 350
            badBig['rect'].y = 50
        
        screen.fill((25,200,255))
        myRect.center = mPos
        screen.blit(myImg,myRect)
        screen.blit(font.render(('有怪 '+str(50-score)),True,(0,0,0)),(0,0))
        screen.blit(font.render(' '*chance,True,(0,0,255),(0,0,255)),(0,30))
        
        t2 = time()
        t4 = time()
        
        if 50 - score == 0:
            part = 0
        if t2 > t1 + speed:
            bullet = {
                "surface": bulletImg,
                "rect": pygame.Rect(myRect.x + (myRect.width-bulletRect.width) / 2, myRect.y, \
                                    bulletRect.width, bulletRect.height),
                "move_x": 0,
                "move_y": -15
            }
            bulletList.append(bullet)
            t1 = t2
        if t4 > t3 + 1.5:
            if score <= 50:
                enemy = {
                        "rect": pygame.Rect(badBig['rect'].x,badBig['rect'].y,50,50),
                        "move_x": 0,
                        "move_y": 1,
                        "life": random.randint(1,20)
                    }
                if enemy['life'] <= 3:
                    enemy['color'] = (0,100,255)
                elif enemy['life'] <= 8:
                    enemy['color'] = (10,255,5)
                elif enemy['life'] <= 15:
                    enemy['color'] = (200,100,20)
                else:
                    enemy['color'] = (255,10,0)
                enemyList.append(enemy)
                t3 = t4
        
        for a1 in bulletList:
            a1["rect"].move_ip(a1["move_x"],a1["move_y"])
            if a1["rect"].top < 0:
                bulletList.remove(a1)
            screen.blit(a1["surface"],a1["rect"])
            for b1 in enemyList:
                b1["rect"].move_ip(b1["move_x"], b1["move_y"])
                if b1["rect"].top > 800:
                    enemyList.remove(b1)
                    chance -= b1['life']
                    if score < 50:
                        score += 1
                if b1["rect"].colliderect(a1["rect"]):
                    try:
                        bulletList.remove(a1)
                        b1['life'] -= 1
                    except:
                        pass
                if b1['life'] <= 0:
                    enemyList.remove(b1)
                    if score < 50:
                        score += 1
                    coins += random.randint(1,10)
                pygame.draw.rect(screen,b1["color"],b1["rect"],0)
                screen.blit(font2.render(str(b1['life']),True,(0,0,0)),(b1['rect'].center[0]-10,b1['rect'].center[1]-10))
            
            if badBig["rect"].colliderect(a1["rect"]):
                try:
                    bulletList.remove(a1)
                    badBig['life'] -= 1
                except:
                    pass
            if badBig['life'] <= 0:
                coins += 500
                part = 0
            
            screen.blit(badBig['surface'],badBig['rect'])
            screen.blit(font2.render(str(badBig['life']),True,(0,0,0)),(badBig['rect'].center[0]-10,badBig['rect'].center[1]-10))
        
        pygame.mouse.set_visible(False)
        pygame.display.update()
        pygame.time.delay(50)
    
    while part == 111:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.MOUSEMOTION:
                mPos = event.pos
        
        if chance <= 0:
            part = 0
            
        try:
            Boss
        except:
            Boss = {
                        "surface": pygame.image.load('bad4computer.png'),
                        "move_x": 0,
                        "move_y": 0,
                        "life": 180
                    }
            Boss['rect'] = Boss['surface'].get_rect()
            Boss['rect'].x = 350
            Boss['rect'].y = 50
        
        screen.fill((25,200,255))
        myRect.center = mPos
        screen.blit(myImg,myRect)
        screen.blit(font.render(('有怪 '+str(50-score)),True,(0,0,0)),(0,0))
        screen.blit(font.render('命 '+str(chance),True,(0,0,255)),(0,30))
        
        t2 = time()
        t4 = time()
        
        if 50 - score == 0:
            part = 0
        if t2 > t1 + speed:
            bullet = {
                "surface": bulletImg,
                "rect": pygame.Rect(myRect.x + (myRect.width-bulletRect.width) / 2, myRect.y, \
                                    bulletRect.width, bulletRect.height),
                "move_x": 0,
                "move_y": -15
            }
            bulletList.append(bullet)
            t1 = t2
        if t4 > t3 + 1.5:
            if score <= 50:
                enemy = {
                        "rect": pygame.Rect(Boss['rect'].x,Boss['rect'].y,50,50),
                        "move_x": 0,
                        "move_y": 1,
                        "life": random.randint(1,30)
                    }
                if enemy['life'] <= 3:
                    enemy['color'] = (0,100,255)
                elif enemy['life'] <= 8:
                    enemy['color'] = (10,255,5)
                elif enemy['life'] <= 15:
                    enemy['color'] = (200,100,20)
                else:
                    enemy['color'] = (255,10,0)
                enemyList.append(enemy)
                t3 = t4
        
        for a1 in bulletList:
            a1["rect"].move_ip(a1["move_x"],a1["move_y"])
            if a1["rect"].top < 0:
                bulletList.remove(a1)
            screen.blit(a1["surface"],a1["rect"])
            for b1 in enemyList:
                b1["rect"].move_ip(b1["move_x"], b1["move_y"])
                if b1["rect"].top > 800:
                    enemyList.remove(b1)
                    chance -= b1['life']
                    if score < 50:
                        score += 1
                if b1["rect"].colliderect(a1["rect"]):
                    try:
                        bulletList.remove(a1)
                        b1['life'] -= 1
                    except:
                        pass
                if b1['life'] <= 0:
                    enemyList.remove(b1)
                    if score < 50:
                        score += 1
                    coins += random.randint(1,10)
                pygame.draw.rect(screen,b1["color"],b1["rect"],0)
                screen.blit(font2.render(str(b1['life']),True,(0,0,0)),(b1['rect'].center[0]-10,b1['rect'].center[1]-10))
            
            if Boss["rect"].colliderect(a1["rect"]):
                try:
                    bulletList.remove(a1)
                    Boss['life'] -= 1
                except:
                    pass
            if Boss['life'] <= 0:
                coins += 3000
                part = 0
            
            screen.blit(Boss['surface'],Boss['rect'])
            screen.blit(font2.render(str(Boss['life']),True,(0,0,0)),(Boss['rect'].center[0]-10,Boss['rect'].center[1]-10))
        
        pygame.mouse.set_visible(False)
        pygame.display.update()
        pygame.time.delay(50)
    
