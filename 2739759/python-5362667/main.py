import pygame,sys,Q,random
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("我的作品")
try:
    import ntpath # 如果成功，那么是Windows
    FONTNAME = "kaiti"
    del ntpath
except ImportError: # 如果失败，是MacOS
    FONTNAME = "kaittf"
myImg = pygame.image.load("bgpic.jpg")
x1 = 0
y1 = 0
startlist = [pygame.image.load("game_start_up.png"),pygame.image.load("game_start_down.png")]
startlist[1] = pygame.transform.scale(startlist[1],(300,50))
startlist[0] = pygame.transform.scale(startlist[0],(300,50))
startrect = pygame.Rect(150,400,300,50)
num = 0
color1 = (255,255,0)
color2 = (255,255,0)
color3 = (255,255,0)
color4 = (255,255,0)
color5 = (0,0,0)
answer = 5
kind = 1
qnum = 0
score = 0
yn = ""
p = 1
one = pygame.Rect(100,140,600,30)
two = pygame.Rect(100,180,600,30)
three = pygame.Rect(100,220,600,30)
four = pygame.Rect(100,260,600,30)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            x1 = event.pos[0]
            y1 = event.pos[1]
        if startrect.collidepoint(x1,y1):
            startimg = startlist[1]
            screen.blit(startimg,startrect)
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button==1:
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.MOUSEMOTION:
                                x1 = event.pos[0]
                                y1 = event.pos[1]
                            
                            if one.collidepoint(x1,y1):
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if event.button==1:
                                        answer = "1"
                                        qnum = qnum + 1
                            if two.collidepoint(x1,y1):
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if event.button==1:
                                        answer = "2"
                                        qnum = qnum + 1
                            if three.collidepoint(x1,y1):
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if event.button==1:
                                        answer = "3"
                                        qnum = qnum + 1
                            if four.collidepoint(x1,y1):
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if event.button==1:
                                        answer = "4"
                                        qnum = qnum + 1
                            elif event.type == pygame.KEYDOWN:
                                if kind == 1:
                                    if event.key == 49:
                                        answer = "1"
                                        kind = 0
                                        qnum = qnum + 1
                                    if event.key == 50:
                                        answer = "2"
                                        kind = 0
                                        qnum = qnum + 1
                                    if event.key == 51:
                                        answer = "3"
                                        kind = 0
                                        qnum = qnum + 1
                                    if event.key == 52:
                                        answer = "4"
                                        kind = 0
                                        qnum = qnum + 1
                                if event.key == pygame.K_SPACE:
                                    num = random.randint(0,len(Q.q)-1)
                                    color1 = (255,255,0)
                                    color2 = (255,255,0)
                                    color3 = (255,255,0)
                                    color4 = (255,255,0)
                                    answer = "0"
                                    kind = 1
                                    yn = ""
                                    color5 = (0,0,0)
                                    p = 1
                            if answer == Q.q[num][5] and answer == "1":
                                color1 = (0,255,0)
                                
                                yn = "正确"
                                color5 = (0,255,0)
                            if answer == Q.q[num][5] and answer == "2":
                                color2 = (0,255,0)
                                
                                yn = "正确"
                                color5 = (0,255,0)
                            if answer == Q.q[num][5] and answer == "3":
                                color3 = (0,255,0)
                                
                                yn = "正确"
                                color5 = (0,255,0)
                            if answer == Q.q[num][5] and answer == "4":
                                color4 = (0,255,0)
                                
                                yn = "正确"
                                color5 = (0,255,0)
                            if answer != Q.q[num][5] and answer == "1":
                                color1 = (255,0,0)
                                color5 = (255,0,0)
                                if Q.q[num][5] == "1":
                                    color1 = (0,255,0)
                                if Q.q[num][5] == "2":
                                    color2 = (0,255,0)
                                if Q.q[num][5] == "3":
                                    color3 = (0,255,0)
                                if Q.q[num][5] == "4":
                                    color4 = (0,255,0)
                                yn = "错误"
                            if answer != Q.q[num][5] and answer == "2":
                                color2 = (255,0,0)
                                yn = "错误"
                                color5 = (255,0,0)
                                if Q.q[num][5] == "1":
                                    color1 = (0,255,0)
                                if Q.q[num][5] == "2":
                                    color2 = (0,255,0)
                                if Q.q[num][5] == "3":
                                    color3 = (0,255,0)
                                if Q.q[num][5] == "4":
                                    color4 = (0,255,0)
                            if answer != Q.q[num][5] and answer == "3":
                                color3 = (255,0,0)
                                yn = "错误"
                                color5 = (255,0,0)
                                if Q.q[num][5] == "1":
                                    color1 = (0,255,0)
                                if Q.q[num][5] == "2":
                                    color2 = (0,255,0)
                                if Q.q[num][5] == "3":
                                    color3 = (0,255,0)
                                if Q.q[num][5] == "4":
                                    color4 = (0,255,0)
                            if answer != Q.q[num][5] and answer == "4":
                                color4 = (255,0,0)
                                yn = "错误"
                                if Q.q[num][5] == "1":
                                    color1 = (0,255,0)
                                if Q.q[num][5] == "2":
                                    color2 = (0,255,0)
                                if Q.q[num][5] == "3":
                                    color3 = (0,255,0)
                                if Q.q[num][5] == "4":
                                    color4 = (0,255,0)
                                color5 = (255,0,0)
                            if answer == Q.q[num][5]:
                                if p == 1:
                                    score = score + 1
                                    p = 0
                            if qnum == 10:
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                    screen.fill((255,255,255))
                                    screen.blit(pygame.font.SysFont(FONTNAME,100).render("分数"+str(score),True,(0,0,0)),(150,200))
                                    pygame.display.update()
                        screen.fill((255,255,255))
                        screen.blit(myImg,(0,0))
                        screen.blit(pygame.font.SysFont(FONTNAME,30).render(Q.q[num][0],True,(0,255,255)),(100,100))
                        screen.blit(pygame.font.SysFont(FONTNAME,30).render("1."+Q.q[num][1],True,color1),one)
                        screen.blit(pygame.font.SysFont(FONTNAME,30).render("2."+Q.q[num][2],True,color2),two)
                        screen.blit(pygame.font.SysFont(FONTNAME,30).render("3."+Q.q[num][3],True,color3),three)
                        screen.blit(pygame.font.SysFont(FONTNAME,30).render("4."+Q.q[num][4],True,color4),four)
                        screen.blit(pygame.font.SysFont(FONTNAME,50).render(yn,True,color5),(250,350))
                        screen.blit(pygame.font.SysFont(FONTNAME,30).render("分数"+str(score),True,(255,0,0)),(480,40))
                        screen.blit(pygame.font.SysFont(FONTNAME,25).render("按下1-4键或点击选项回答问题",True,(255,0,255)),(125,475))
                        screen.blit(pygame.font.SysFont(FONTNAME,50).render("按下空格键回答下一个",True,(255,150,0)),(50,410))
                        screen.blit(pygame.font.SysFont(FONTNAME,45).render("百科问答：",True,(255,255,255)),(60,45))
                        pygame.display.update()
        else:
            startimg = startlist[0]
    screen.fill((255,255,255))
    screen.blit(myImg,(0,0))
    screen.blit(startimg,startrect)
    screen.blit(pygame.font.SysFont(FONTNAME,100).render("趣味问答",True,(255,255,255)),(100,50))
    pygame.display.update()