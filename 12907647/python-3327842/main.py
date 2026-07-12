import pygame, sys, random , time
input('准备好了吗，1,2,3(暴击、猛击、随机击打)技能控制！(Enter)')
time.sleep(0.4)
from time import *
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("宠物决斗战")
bgll = pygame.image.load("ph.png")
bgPic = pygame.transform.scale(bgll,(800,600))
myPet = pygame.image.load("恐龙1.png")
enemyPet = pygame.image.load("恐龙2.png")

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,255,255)

textColor = BLUE
myword = '欢迎挑战'
myFont = pygame.font.SysFont('kaiti',30)
myText = myFont.render(myword,True,RED)
life = 100
attack = [random.randint(10,20),15,random.randint(5,40)]
defense = 40
life2 = 100
attack2 = [random.randint(1,50),10,random.randint(5,25)]
defense2 = 30

turn = 1 #回合1玩家1，2玩家1，3结束。
print('玩家1先动手！')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 and turn == 1:
                blood = attack[0]*(100-defense2)/100
                life2 = life2 - blood
                myword = '玩家1用了招数1，对方掉血：'+str(blood)+'玩家1还有血：'+str(life)
                textColor = RED
                turn = 2
            elif event.key == pygame.K_2 and turn == 1:
                blood = attack[1]*(100-defense2)/100
                life2 = life2 - blood
                myword = '玩家1用了招数2，对方掉血：'+str(blood)+'玩家1还有血：'+str(life)
                textColor = RED
                turn = 2
            elif event.key == pygame.K_3 and turn == 1:
                blood = attack[2]*(100-defense2)/100
                life2 = life2 - blood
                myword = '玩家1用了招数3，对方掉血：'+str(blood)+'玩家1还有血：'+str(life)
                textColor = RED
                turn = 2
            elif event.key == pygame.K_1 and turn == 2:
                blood = attack2[0]*(100-defense)/100
                life = life - blood
                myword = '玩家2用了招数1，对方掉血：'+str(blood)+'玩家2还有血：'+str(life2)
                textColor = GREEN
                turn = 1
            elif event.key == pygame.K_2 and turn == 2:
                blood = attack2[1]*(100-defense)/100
                life = life - blood
                myword = '玩家2用了招数2，对方掉血：'+str(blood)+'玩家2还有血：'+str(life2)
                textColor = GREEN
                turn = 1
            elif event.key == pygame.K_3 and turn == 2:
                blood = attack2[2]*(100-defense)/100
                life = life - blood
                myword = '玩家2用了招数3，对方掉血：'+str(blood)+'玩家2还有血：'+str(life2)
                textColor = GREEN
                turn = 1
                
    # game over and win !
    if life <= 0:
        myword = '玩家1被玩家2打败了！ 玩家2胜！'
        textColor = BLUE
        turn = 3
    if life2 <= 0:
        myword = '玩家2被玩家1打败了！ 玩家1胜！'
        textColor = BLUE
        turn = 3
    screen.blit(bgPic,(0,0))
    screen.blit(myPet,(0,130))
    screen.blit(enemyPet,(400,130))
    myText = myFont.render(myword,True,textColor)
    screen.blit(myText,(50,500))
    pygame.display.update()