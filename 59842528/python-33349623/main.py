import pygame,sys,random,time
pygame.init()
screen = pygame.display.set_mode((500,300))
pygame.display.set_caption("2021元宵猜灯谜")
myImg = pygame.image.load("bgp1.png")
pygame.mixer.music.load("su.mp3")
pygame.mixer.music.play(-1)
b=160
score=0
def panduan(t):
    if b==t[0]:
        return t[0]
t1=["二小二小头上长草-----打一字","蒜"]
t2=["十三月-----打一字","青"]
t3=["一马过桥压桥墩-----打一字","骄"]
t4=["人门无犬吠-----打一字","问"]
t5=["两点天上来-----打一字","关"]
t6=["早不说晚不说-----打一字","许"]
t7=["第九次结婚-----打一城市","巴黎"]
t8=["上厕所排号-----打一城市","伦敦"]
t9=["双喜临门-----打一城市","重庆"]
t10=["法官进羊圈-----打一城市","沈阳"]
t11=["全面整顿-----打一城市","大理"]
t12=["超级好的牙刷-----打一成语","牙刷"]
t13=["第九次结婚-----打一城市","巴黎"]
t14=["武-----打一字","斐"]
t15=["武大郎设宴-----打一成语","高鹏满座"]
myFont = pygame.font.SysFont("kaiti", 37)
myFont1 = pygame.font.SysFont("kaiti", 60)
myFont2 = pygame.font.SysFont("kaiti", 52)
myFont3 = pygame.font.SysFont("kaiti", 40)
myText1 = myFont1.render("2021元宵猜灯谜", True, (0, 145, 255))
myText2 = myFont.render("任意键开始", True, (0, 145, 255))
myText3 = myFont.render("在右边输入答案", True, (0, 145, 255))
myText4 = myFont.render("score:"+str(score), True, (0, 145, 255))
tList=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15]
a=0
z=''
while True:
    myText4 = myFont.render("score:"+str(score), True, (0, 145, 255))
    screen.blit(myImg,(0,0))
    if a==0:
        c=random.choice(tList)
        print(c[0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if event.type==pygame.KEYDOWN :
        a=1
    if a==0:
        screen.blit(myText1, (50, 40))
        screen.blit(myText2, (b, 140))
        screen.blit(myText3, (120, 200))
        screen.blit(myText4, (0, 0))
        pygame.display.update()
        continue
    a=0
    myText2 = myFont.render("任意键开始再来一道", True, (0, 145, 255))
    b=130
    if a==0:
        myText = myFont.render(c[0], True, (0, 145, 255))
        screen.blit(myText, (70, 100))

        z=input("谜底:")
    if z== str(c[1]) :
        myText = myFont.render("正确", True, (0, 145, 255))
        score=score+1
        screen.blit(myText,(100,80))
        pygame.display.update()
        time.sleep(3)
        a=0
    else:
        myText = myFont.render("错误，正确答案是"+c[1], True, (0, 145, 255))
        screen.blit(myText,(100,80))
        pygame.display.update()
        time.sleep(3)
        a=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()