
import pygame,sys,random
from time import *
print('xxx')
sleep(1)
qiupiu_ban = input('欢迎！1=变换角色/2=不换角色/3=闯关版')
if qiupiu_ban == '1':
    from time import *
    sleep(0.8)
    print('\033[1;36m各\033[1;0m')
    sleep(1)
    print('\033[2J')
    print('\033[1;32m各老师、学生、观众必看！！！！\033[1;0m')
    has = input('原版=1/斗鸡眼版（建议不看）=2/开会左上哈哈版（等它到左上，建议看）=3/卡顿版 = 4')
    if has == '1':
        import pygame,sys,random
        from time import *
        pygame.init()
        screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("球球大作战")
        bgImg = pygame.image.load("bgPic.png")
        
        hero_x = 300
        hero_y = 300
        hero_size = 100
        hero_speed = 50
        hero1 = pygame.image.load("大嘴怪1.png")
        hero2 = pygame.image.load("大嘴怪2.png")
        hero3 = pygame.image.load("大嘴怪3.png")
        heroImg = [hero1, hero2, hero3]
        heroImgs = pygame.transform.scale(heroImg[random.randint(0, 2)], (hero_size, hero_size))
        
        fruit1 = pygame.image.load("fruit1.png")
        fruit2 = pygame.image.load("fruit2.png")
        fruit3 = pygame.image.load("fruit3.png")
        fruit4 = pygame.image.load("fruit4.png")
        fruit5 = pygame.image.load("fruit5.png")
        fruitImg = [fruit1, fruit2, fruit3, fruit4, fruit5]
        fruitImgs = pygame.transform.scale(fruitImg[random.randint(2, 4)], (40, 40))
        
        fruitList = []
        for i in range(30):
            fruitRect = pygame.Rect(random.randint(0,700),random.randint(0,700),40,40)
            fruitList.append(fruitRect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('哈哈关不掉！按暂停！')
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        hero_y = hero_y - hero_speed
                    elif event.key == pygame.K_DOWN:
                        hero_y = hero_y + hero_speed
                    elif event.key == pygame.K_LEFT:
                        hero_x = hero_x - hero_speed
                    elif event.key == pygame.K_RIGHT:
                        hero_x = hero_x + hero_speed
        #**********-------------------------------------***********#
            heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
            for n in fruitList:
                n.x = n.x + random.randint(-1,1)
                n.y = n.y + random.randint(-1,1)
                if n.top < 0:
                    n.top = 0
                if n.bottom > 700:
                    n.bottom = 700
                if n.left < 0:
                    n.left = 0
                if n.right > 700:
                    n.right = 700
                if heroRect.colliderect(n):
                    fruitList.remove(n)
                    hero_size = hero_size + 10
                    heroImgs = pygame.transform.scale(heroImg[random.randint(0, 2)],(hero_size,hero_size))
                    print('YOU EAT A FRUIT!')
                    print('吃掉了！')
                    sleep(0.01)
            screen.blit(bgImg, (0, 0))
            screen.blit(heroImgs, (hero_x, hero_y))
            for rect in fruitList:
                screen.blit(fruitImgs, rect)
            pygame.display.update()
    elif has == '2':
        # 1.能够通过键盘控制大嘴怪的移动的代码
        # 2.当大嘴怪碰到食物时吃掉食物
        import pygame,sys,random
        from time import *
        pygame.init()
        screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("球球大作战")
        bgImg = pygame.image.load("bgPic.png")
        
        hero_x = 300
        hero_y = 300
        hero_size = 100
        hero_speed = 50
        hero1 = pygame.image.load("大嘴怪1.png")
        hero2 = pygame.image.load("大嘴怪2.png")
        hero3 = pygame.image.load("大嘴怪3.png")
        heroImg = [hero1, hero2, hero3]
        heroImgs = pygame.transform.scale(heroImg[random.randint(0, 2)], (hero_size, hero_size))
        
        fruit1 = pygame.image.load("fruit1.png")
        fruit2 = pygame.image.load("fruit2.png")
        fruit3 = pygame.image.load("fruit3.png")
        fruit4 = pygame.image.load("fruit4.png")
        fruit5 = pygame.image.load("fruit5.png")
        fruitImg = [fruit1, fruit2, fruit3, fruit4, fruit5]
        fruitImgs = pygame.transform.scale(fruitImg[random.randint(0, 1)], (40, 40))
        
        fruitList = []
        for i in range(30):
            fruitRect = pygame.Rect(random.randint(0,700),random.randint(0,700),40,40)
            fruitList.append(fruitRect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('哈哈关不掉！按暂停！')
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        hero_y = hero_y - hero_speed
                    elif event.key == pygame.K_DOWN:
                        hero_y = hero_y + hero_speed
                    elif event.key == pygame.K_LEFT:
                        hero_x = hero_x - hero_speed
                    elif event.key == pygame.K_RIGHT:
                        hero_x = hero_x + hero_speed
        #**********-------------------------------------***********#
            heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
            for n in fruitList:
                n.x = n.x + random.randint(-5,5)
                n.y = n.y + random.randint(-5,5)
                if n.top < 0:
                    n.top = 0
                if n.bottom > 700:
                    n.bottom = 700
                if n.left < 0:
                    n.left = 0
                if n.right > 700:
                    n.right = 700
                if heroRect.colliderect(n):
                    fruitList.remove(n)
                    hero_size = hero_size + 10
                    heroImgs = pygame.transform.scale(heroImg[random.randint(0, 2)],(hero_size,hero_size))
                    print('YOU EAT A FRUIT!')
                    print('吃掉了！')
                    sleep(0.01)
            screen.blit(bgImg, (0, 0))
            screen.blit(heroImgs, (hero_x, hero_y))
            for rect in fruitList:
                screen.blit(fruitImgs, rect)
            pygame.display.update()
    elif has == '3':
        import pygame,sys,random
        from time import *
        pygame.init()
        screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("球球大作战")
        bgImg = pygame.image.load("bgPic.png")
        
        hero_x = 300
        hero_y = 300
        hero_size = 100
        hero_speed = 50
        hero1 = pygame.image.load("大嘴怪1.png")
        hero2 = pygame.image.load("大嘴怪2.png")
        hero3 = pygame.image.load("大嘴怪3.png")
        heroImg = [hero1, hero2, hero3]
        heroImgs = pygame.transform.scale(heroImg[random.randint(0, 2)], (hero_size, hero_size))
        
        fruit1 = pygame.image.load("fruit1.png")
        fruit2 = pygame.image.load("fruit2.png")
        fruit3 = pygame.image.load("fruit3.png")
        fruit4 = pygame.image.load("fruit4.png")
        fruit5 = pygame.image.load("fruit5.png")
        fruitImg = [fruit1, fruit2, fruit3, fruit4, fruit5]
        fruitImgs = pygame.transform.scale(fruitImg[random.randint(2, 4)], (40, 40))
        
        fruitList = []
        for i in range(30):
            fruitRect = pygame.Rect(random.randint(0,700),random.randint(0,700),40,40)
            fruitList.append(fruitRect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('哈哈关不掉！按暂停！')
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        hero_y = hero_y - hero_speed
                    elif event.key == pygame.K_DOWN:
                        hero_y = hero_y + hero_speed
                    elif event.key == pygame.K_LEFT:
                        hero_x = hero_x - hero_speed
                    elif event.key == pygame.K_RIGHT:
                        hero_x = hero_x + hero_speed
        #**********-------------------------------------***********#
            heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
            for n in fruitList:
                n.x = n.x + random.randint(-2,1)
                n.y = n.y + random.randint(-2,1)
                if n.top < 0:
                    n.top = 0
                if n.bottom > 700:
                    n.bottom = 700
                if n.left < 0:
                    n.left = 0
                if n.right > 700:
                    n.right = 700
                if heroRect.colliderect(n):
                    fruitList.remove(n)
                    hero_size = hero_size + 10
                    heroImgs = pygame.transform.scale(heroImg[random.randint(0, 2)],(hero_size,hero_size))
                    print('YOU EAT A FRUIT!')
                    print('吃掉了！')
                    sleep(0.2)
            screen.blit(bgImg, (0, 0))
            screen.blit(heroImgs, (hero_x, hero_y))
            for rect in fruitList:
                screen.blit(fruitImgs, rect)
            pygame.display.update()
    elif has == '4':
        import pygame,sys,random
        from time import *
        pygame.init()
        screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("球球大作战")
        bgImg = pygame.image.load("bgPic.png")
        
        hero_x = 300
        hero_y = 300
        hero_size = 100
        hero_speed = 50
        hero1 = pygame.image.load("大嘴怪1.png")
        hero2 = pygame.image.load("大嘴怪2.png")
        hero3 = pygame.image.load("大嘴怪3.png")
        heroImg = [hero1, hero2, hero3]
        heroImgs = pygame.transform.scale(heroImg[random.randint(0, 2)], (hero_size, hero_size))
        
        fruit1 = pygame.image.load("fruit1.png")
        fruit2 = pygame.image.load("fruit2.png")
        fruit3 = pygame.image.load("fruit3.png")
        fruit4 = pygame.image.load("fruit4.png")
        fruit5 = pygame.image.load("fruit5.png")
        fruitImg = [fruit1, fruit2, fruit3, fruit4, fruit5]
        fruitImgs = pygame.transform.scale(fruitImg[random.randint(2, 4)], (40, 40))
        
        fruitList = []
        for i in range(30):
            fruitRect = pygame.Rect(random.randint(0,700),random.randint(0,700),40,40)
            fruitList.append(fruitRect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('哈哈关不掉！按暂停！')
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        hero_y = hero_y - hero_speed
                    elif event.key == pygame.K_DOWN:
                        hero_y = hero_y + hero_speed
                    elif event.key == pygame.K_LEFT:
                        hero_x = hero_x - hero_speed
                    elif event.key == pygame.K_RIGHT:
                        hero_x = hero_x + hero_speed
        #**********-------------------------------------***********#
            heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
            for n in fruitList:
                n.x = n.x + random.randint(-1,1)
                n.y = n.y + random.randint(-1,1)
                if n.top < 0:
                    n.top = 0
                if n.bottom > 700:
                    n.bottom = 700
                if n.left < 0:
                    n.left = 0
                if n.right > 700:
                    n.right = 700
                if heroRect.colliderect(n):
                    fruitList.remove(n)
                    hero_size = hero_size + 10
                    heroImgs = pygame.transform.scale(heroImg[random.randint(0, 2)],(hero_size,hero_size))
                    print('YOU EAT A FRUIT!')
                    print('吃掉了！')
                    sleep(0.5)
            screen.blit(bgImg, (0, 0))
            screen.blit(heroImgs, (hero_x, hero_y))
            for rect in fruitList:
                screen.blit(fruitImgs, rect)
            pygame.display.update()
if qiupiu_ban == '2':
    from time import *
    sleep(0.8)
    print('\033[1;36m各\033[1;0m')
    sleep(1)
    print('\033[2J')
    print('\033[1;32m各老师、学生、观众必看！！！！\033[1;0m')
    has = input('原版=1/斗鸡眼版（建议不看）=2/开会左上哈哈版（等它到左上，建议看）=3/卡顿版 = 4')
    if has == '1':
        import pygame,sys,random
        from time import *
        pygame.init()
        screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("球球大作战")
        bgImg = pygame.image.load("bgPic.png")
        
        hero_x = 300
        hero_y = 300
        hero_size = 100
        hero_speed = 50
        hero1 = pygame.image.load("大嘴怪1.png")
        hero2 = pygame.image.load("大嘴怪2.png")
        hero3 = pygame.image.load("大嘴怪3.png")
        heroImg = [hero1, hero2, hero3]
        a = heroImg[random.randint(0, 2)]
        heroImgs = pygame.transform.scale(a, (hero_size, hero_size))
        
        fruit1 = pygame.image.load("fruit1.png")
        fruit2 = pygame.image.load("fruit2.png")
        fruit3 = pygame.image.load("fruit3.png")
        fruit4 = pygame.image.load("fruit4.png")
        fruit5 = pygame.image.load("fruit5.png")
        fruitImg = [fruit1, fruit2, fruit3, fruit4, fruit5]
        fruitImgs = pygame.transform.scale(fruitImg[random.randint(2, 4)], (40, 40))
        
        fruitList = []
        for i in range(30):
            fruitRect = pygame.Rect(random.randint(0,700),random.randint(0,700),40,40)
            fruitList.append(fruitRect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('哈哈关不掉！按暂停！')
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        hero_y = hero_y - hero_speed
                    elif event.key == pygame.K_DOWN:
                        hero_y = hero_y + hero_speed
                    elif event.key == pygame.K_LEFT:
                        hero_x = hero_x - hero_speed
                    elif event.key == pygame.K_RIGHT:
                        hero_x = hero_x + hero_speed
        #**********-------------------------------------***********#
            heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
            for n in fruitList:
                n.x = n.x + random.randint(-1,1)
                n.y = n.y + random.randint(-1,1)
                if n.top < 0:
                    n.top = 0
                if n.bottom > 700:
                    n.bottom = 700
                if n.left < 0:
                    n.left = 0
                if n.right > 700:
                    n.right = 700
                if heroRect.colliderect(n):
                    fruitList.remove(n)
                    hero_size = hero_size + 10
                    heroImgs = pygame.transform.scale(a,(hero_size,hero_size))
                    print('YOU EAT A FRUIT!')
                    print('吃掉了！')
                    sleep(0.01)
            screen.blit(bgImg, (0, 0))
            screen.blit(heroImgs, (hero_x, hero_y))
            for rect in fruitList:
                screen.blit(fruitImgs, rect)
            pygame.display.update()
    elif has == '2':
        # 1.能够通过键盘控制大嘴怪的移动的代码
        # 2.当大嘴怪碰到食物时吃掉食物
        import pygame,sys,random
        from time import *
        pygame.init()
        screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("球球大作战")
        bgImg = pygame.image.load("bgPic.png")
        
        hero_x = 300
        hero_y = 300
        hero_size = 100
        hero_speed = 50
        hero1 = pygame.image.load("大嘴怪1.png")
        hero2 = pygame.image.load("大嘴怪2.png")
        hero3 = pygame.image.load("大嘴怪3.png")
        heroImg = [hero1, hero2, hero3]
        a = heroImg[random.randint(0, 2)]
        heroImgs = pygame.transform.scale(a, (hero_size, hero_size))
        
        fruit1 = pygame.image.load("fruit1.png")
        fruit2 = pygame.image.load("fruit2.png")
        fruit3 = pygame.image.load("fruit3.png")
        fruit4 = pygame.image.load("fruit4.png")
        fruit5 = pygame.image.load("fruit5.png")
        fruitImg = [fruit1, fruit2, fruit3, fruit4, fruit5]
        fruitImgs = pygame.transform.scale(fruitImg[random.randint(0, 1)], (40, 40))
        
        fruitList = []
        for i in range(30):
            fruitRect = pygame.Rect(random.randint(0,700),random.randint(0,700),40,40)
            fruitList.append(fruitRect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('哈哈关不掉！按暂停！')
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        hero_y = hero_y - hero_speed
                    elif event.key == pygame.K_DOWN:
                        hero_y = hero_y + hero_speed
                    elif event.key == pygame.K_LEFT:
                        hero_x = hero_x - hero_speed
                    elif event.key == pygame.K_RIGHT:
                        hero_x = hero_x + hero_speed
        #**********-------------------------------------***********#
            heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
            for n in fruitList:
                n.x = n.x + random.randint(-5,5)
                n.y = n.y + random.randint(-5,5)
                if n.top < 0:
                    n.top = 0
                if n.bottom > 700:
                    n.bottom = 700
                if n.left < 0:
                    n.left = 0
                if n.right > 700:
                    n.right = 700
                if heroRect.colliderect(n):
                    fruitList.remove(n)
                    hero_size = hero_size + 10
                    heroImgs = pygame.transform.scale(a,(hero_size,hero_size))
                    print('YOU EAT A FRUIT!')
                    print('吃掉了！')
                    sleep(0.01)
            screen.blit(bgImg, (0, 0))
            screen.blit(heroImgs, (hero_x, hero_y))
            for rect in fruitList:
                screen.blit(fruitImgs, rect)
            pygame.display.update()
    elif has == '3':
        import pygame,sys,random
        from time import *
        pygame.init()
        screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("球球大作战")
        bgImg = pygame.image.load("bgPic.png")
        
        hero_x = 300
        hero_y = 300
        hero_size = 100
        hero_speed = 50
        hero1 = pygame.image.load("大嘴怪1.png")
        hero2 = pygame.image.load("大嘴怪2.png")
        hero3 = pygame.image.load("大嘴怪3.png")
        heroImg = [hero1, hero2, hero3]
        a = heroImg[random.randint(0, 2)]
        heroImgs = pygame.transform.scale(a, (hero_size, hero_size))
        
        fruit1 = pygame.image.load("fruit1.png")
        fruit2 = pygame.image.load("fruit2.png")
        fruit3 = pygame.image.load("fruit3.png")
        fruit4 = pygame.image.load("fruit4.png")
        fruit5 = pygame.image.load("fruit5.png")
        fruitImg = [fruit1, fruit2, fruit3, fruit4, fruit5]
        fruitImgs = pygame.transform.scale(fruitImg[random.randint(2, 4)], (40, 40))
        
        fruitList = []
        for i in range(30):
            fruitRect = pygame.Rect(random.randint(0,700),random.randint(0,700),40,40)
            fruitList.append(fruitRect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('哈哈关不掉！按暂停！')
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        hero_y = hero_y - hero_speed
                    elif event.key == pygame.K_DOWN:
                        hero_y = hero_y + hero_speed
                    elif event.key == pygame.K_LEFT:
                        hero_x = hero_x - hero_speed
                    elif event.key == pygame.K_RIGHT:
                        hero_x = hero_x + hero_speed
        #**********-------------------------------------***********#
            heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
            for n in fruitList:
                n.x = n.x + random.randint(-2,1)
                n.y = n.y + random.randint(-2,1)
                if n.top < 0:
                    n.top = 0
                if n.bottom > 700:
                    n.bottom = 700
                if n.left < 0:
                    n.left = 0
                if n.right > 700:
                    n.right = 700
                if heroRect.colliderect(n):
                    fruitList.remove(n)
                    hero_size = hero_size + 10
                    heroImgs = pygame.transform.scale(a,(hero_size,hero_size))
                    print('YOU EAT A FRUIT!')
                    print('吃掉了！')
                    sleep(0.2)
            screen.blit(bgImg, (0, 0))
            screen.blit(heroImgs, (hero_x, hero_y))
            for rect in fruitList:
                screen.blit(fruitImgs, rect)
            pygame.display.update()
    elif has == '4':
        import pygame,sys,random
        from time import *
        pygame.init()
        screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("球球大作战")
        bgImg = pygame.image.load("bgPic.png")
        
        hero_x = 300
        hero_y = 300
        hero_size = 100
        hero_speed = 50
        hero1 = pygame.image.load("大嘴怪1.png")
        hero2 = pygame.image.load("大嘴怪2.png")
        hero3 = pygame.image.load("大嘴怪3.png")
        heroImg = [hero1, hero2, hero3]
        a = heroImg[random.randint(0, 2)]
        heroImgs = pygame.transform.scale(a, (hero_size, hero_size))
        
        fruit1 = pygame.image.load("fruit1.png")
        fruit2 = pygame.image.load("fruit2.png")
        fruit3 = pygame.image.load("fruit3.png")
        fruit4 = pygame.image.load("fruit4.png")
        fruit5 = pygame.image.load("fruit5.png")
        fruitImg = [fruit1, fruit2, fruit3, fruit4, fruit5]
        fruitImgs = pygame.transform.scale(fruitImg[random.randint(2, 4)], (40, 40))
        
        fruitList = []
        for i in range(30):
            fruitRect = pygame.Rect(random.randint(0,700),random.randint(0,700),40,40)
            fruitList.append(fruitRect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('哈哈关不掉！按暂停！')
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        hero_y = hero_y - hero_speed
                    elif event.key == pygame.K_DOWN:
                        hero_y = hero_y + hero_speed
                    elif event.key == pygame.K_LEFT:
                        hero_x = hero_x - hero_speed
                    elif event.key == pygame.K_RIGHT:
                        hero_x = hero_x + hero_speed
        #**********-------------------------------------***********#
            heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
            for n in fruitList:
                n.x = n.x + random.randint(-1,1)
                n.y = n.y + random.randint(-1,1)
                if n.top < 0:
                    n.top = 0
                if n.bottom > 700:
                    n.bottom = 700
                if n.left < 0:
                    n.left = 0
                if n.right > 700:
                    n.right = 700
                if heroRect.colliderect(n):
                    fruitList.remove(n)
                    hero_size = hero_size + 10
                    heroImgs = pygame.transform.scale(a,(hero_size,hero_size))
                    print('YOU EAT A FRUIT!')
                    print('吃掉了！')
                    sleep(0.5)
            screen.blit(bgImg, (0, 0))
            screen.blit(heroImgs, (hero_x, hero_y))
            for rect in fruitList:
                screen.blit(fruitImgs, rect)
            pygame.display.update()
elif qiupiu_ban == '3':
    a = input('1键准备开始：')
    if a == '1':
        import pygame,sys,random
        from time import *
        sleep(1.25)
        print('第一关：')
        pygame.init()
        screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("球球大作战第1关：")
        bgImg = pygame.image.load("bgPic.png")
        
        hero_x = 300
        hero_y = 300
        hero_size = 100
        hero_speed = 50
        hero1 = pygame.image.load("大嘴怪1.png")
        hero2 = pygame.image.load("大嘴怪2.png")
        hero3 = pygame.image.load("大嘴怪3.png")
        heroImg = [hero1, hero2, hero3]
        heroImgs = pygame.transform.scale(heroImg[random.randint(0, 2)], (hero_size, hero_size))
        
        fruit1 = pygame.image.load("fruit1.png")
        fruit2 = pygame.image.load("fruit2.png")
        fruit3 = pygame.image.load("fruit3.png")
        fruit4 = pygame.image.load("fruit4.png")
        fruit5 = pygame.image.load("fruit5.png")
        fruitImg = [fruit1, fruit2, fruit3, fruit4, fruit5]
        fruitImgs = pygame.transform.scale(fruitImg[random.randint(2, 4)], (40, 40))
        
        fruitList = []
        for i in range(8):
            fruitRect = pygame.Rect(random.randint(0,700),random.randint(0,700),40,40)
            fruitList.append(fruitRect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        hero_y = hero_y - hero_speed
                    elif event.key == pygame.K_DOWN:
                        hero_y = hero_y + hero_speed
                    elif event.key == pygame.K_LEFT:
                        hero_x = hero_x - hero_speed
                    elif event.key == pygame.K_RIGHT:
                        hero_x = hero_x + hero_speed
        #**********-------------------------------------***********#
            heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
            for n in fruitList:
                n.x = n.x + random.randint(-1,1)
                n.y = n.y + random.randint(-1,1)
                if n.top < 0:
                    n.top = 0
                if n.bottom > 700:
                    n.bottom = 700
                if n.left < 0:
                    n.left = 0
                if n.right > 700:
                    n.right = 700
                if heroRect.colliderect(n):
                    fruitList.remove(n)
                    hero_size = hero_size + 10
                    heroImgs = pygame.transform.scale(heroImg[random.randint(0, 2)],(hero_size,hero_size))
                    print('YOU EAT A FRUIT!')
                    print('吃掉了！')
                    sleep(0.01)
                if fruitList == []:
                    print('YOU WIN!')
                    sleep(1)
                    a = input('2键准备开始：')
                    if a == '2':
                        import pygame,sys,random
                        from time import *
                        sleep(1.25)
                        print('第二关：')
                        pygame.init()
                        screen = pygame.display.set_mode((700, 700))
                        pygame.display.set_caption("球球大作战第2关：")
                        bgImg = pygame.image.load("bgPic.png")
                        
                        hero_x = 300
                        hero_y = 300
                        hero_size = 100
                        hero_speed = 50
                        hero1 = pygame.image.load("大嘴怪1.png")
                        hero2 = pygame.image.load("大嘴怪2.png")
                        hero3 = pygame.image.load("大嘴怪3.png")
                        heroImg = [hero1, hero2, hero3]
                        heroImgs = pygame.transform.scale(heroImg[random.randint(0, 2)], (hero_size, hero_size))
                        
                        fruit1 = pygame.image.load("fruit1.png")
                        fruit2 = pygame.image.load("fruit2.png")
                        fruit3 = pygame.image.load("fruit3.png")
                        fruit4 = pygame.image.load("fruit4.png")
                        fruit5 = pygame.image.load("fruit5.png")
                        fruitImg = [fruit1, fruit2, fruit3, fruit4, fruit5]
                        fruitImgs = pygame.transform.scale(fruitImg[random.randint(2, 4)], (40, 40))
                        
                        fruitList = []
                        for i in range(20):
                            fruitRect = pygame.Rect(random.randint(0,700),random.randint(0,700),40,40)
                            fruitList.append(fruitRect)
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_UP:
                                        hero_y = hero_y - hero_speed
                                    elif event.key == pygame.K_DOWN:
                                        hero_y = hero_y + hero_speed
                                    elif event.key == pygame.K_LEFT:
                                        hero_x = hero_x - hero_speed
                                    elif event.key == pygame.K_RIGHT:
                                        hero_x = hero_x + hero_speed
                        #**********-------------------------------------***********#
                            heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
                            for n in fruitList:
                                n.x = n.x + random.randint(-1,1)
                                n.y = n.y + random.randint(-1,1)
                                if n.top < 0:
                                    n.top = 0
                                if n.bottom > 700:
                                    n.bottom = 700
                                if n.left < 0:
                                    n.left = 0
                                if n.right > 700:
                                    n.right = 700
                                if heroRect.colliderect(n):
                                    fruitList.remove(n)
                                    hero_size = hero_size + 10
                                    heroImgs = pygame.transform.scale(heroImg[random.randint(0, 2)],(hero_size,hero_size))
                                    print('YOU EAT A FRUIT!')
                                    print('吃掉了！')
                                    sleep(0.01)
                                if fruitList == []:
                                    print('YOU WIN!')
                                    sleep(1)
                                    a = input('3键准备开始：')
                                    if a == '3':
                                        import pygame,sys,random
                                        from time import *
                                        sleep(1.25)
                                        print('第三关：')
                                        pygame.init()
                                        screen = pygame.display.set_mode((700, 700))
                                        pygame.display.set_caption("球球大作战第3关（当心隐形怪！碰了会输！）：")
                                        bgImg = pygame.image.load("bgPic.png")
                                        
                                        hero_x = 300
                                        hero_y = 300
                                        enemy_x = 700
                                        enemy_y = 0
                                        enemy_size = 200
                                        hero_size = 100
                                        hero_speed = 50
                                        hero1 = pygame.image.load("大嘴怪1.png")
                                        hero2 = pygame.image.load("大嘴怪2.png")
                                        hero3 = pygame.image.load("大嘴怪3.png")
                                        heroImg = [hero1, hero2, hero3]
                                        heroImgs = pygame.transform.scale(heroImg[random.randint(0, 2)], (hero_size, hero_size))
                                        
                                        fruit1 = pygame.image.load("fruit1.png")
                                        fruit2 = pygame.image.load("fruit2.png")
                                        fruit3 = pygame.image.load("fruit3.png")
                                        fruit4 = pygame.image.load("fruit4.png")
                                        fruit5 = pygame.image.load("fruit5.png")
                                        fruitImg = [fruit1, fruit2, fruit3, fruit4, fruit5]
                                        fruitImgs = pygame.transform.scale(fruitImg[random.randint(2, 4)], (40, 40))
                                        
                                        enemyImg = pygame.image.load("1级怪敌人.png")
                                        enemyImgs = pygame.transform.scale(enemyImg, (enemy_size,enemy_size))
                                        
                                        fruitList = []
                                        enemyList = []
                                        for i in range(10):
                                            fruitRect = pygame.Rect(random.randint(0,700),random.randint(0,700),40,40)
                                            fruitList.append(fruitRect)
                                        enemyRect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
                                        enemyList.append(enemyRect)
                                        while True:
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    pygame.quit()
                                                    sys.exit()
                                                elif event.type == pygame.KEYDOWN:
                                                    if event.key == pygame.K_UP:
                                                        hero_y = hero_y - hero_speed
                                                    elif event.key == pygame.K_DOWN:
                                                        hero_y = hero_y + hero_speed
                                                    elif event.key == pygame.K_LEFT:
                                                        hero_x = hero_x - hero_speed
                                                    elif event.key == pygame.K_RIGHT:
                                                        hero_x = hero_x + hero_speed
                                        #**********-------------------------------------***********#
                                            heroRect = pygame.Rect(hero_x, hero_y, hero_size, hero_size)
                                        
                                            for x in enemyList:
                                                x.x = x.x + random.randint(-5,-2)
                                                x.y = x.y + random.randint(2,5)
                                                if heroRect.colliderect(x):
                                                    print('你KO了！')
                                                    hero_size = hero_size - 100
                                                    heroImgs = pygame.transform.scale(heroImg[random.randint(0, 2)],(hero_size,hero_size))
                                                    sleep(1)
                                                    print('输了!')
                                                    print('KO了！')
                                                    sleep(1)
                                                    pygame.quit()
                                                    sys.exit()
                                            for n in fruitList:
                                                n.x = n.x + random.randint(-1,1)
                                                n.y = n.y + random.randint(-1,1)
                                                if n.top < 0:
                                                    n.top = 0
                                                if n.bottom > 700:
                                                    n.bottom = 700
                                                if n.left < 0:
                                                    n.left = 0
                                                if n.right > 700:
                                                    n.right = 700
                                                if heroRect.colliderect(n):
                                                    fruitList.remove(n)
                                                    hero_size = hero_size + 10
                                                    heroImgs = pygame.transform.scale(heroImg[random.randint(0, 2)],(hero_size,hero_size))
                                                    print('YOU EAT A FRUIT!')
                                                    print('吃掉了！')
                                                    sleep(0.01)
                                                if fruitList == []:
                                                    print('YOU WIN!')
                                                    sleep(0.01)
                                                    pygame.quit()
                                                    sys.exit()
                                                    
                                            screen.blit(bgImg, (0, 0))
                                            screen.blit(heroImgs, (hero_x, hero_y))
                                            screen.blit(enemyImgs, enemyRect)
                                            for rect in fruitList:
                                                screen.blit(fruitImgs, rect)
                                            pygame.display.update()
                            screen.blit(bgImg, (0, 0))
                            screen.blit(heroImgs, (hero_x, hero_y))
                            for rect in fruitList:
                                screen.blit(fruitImgs, rect)
                            pygame.display.update()
            screen.blit(bgImg, (0, 0))
            screen.blit(heroImgs, (hero_x, hero_y))
            for rect in fruitList:
                screen.blit(fruitImgs, rect)
            pygame.display.update()