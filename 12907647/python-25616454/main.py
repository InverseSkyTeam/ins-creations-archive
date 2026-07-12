import pygame,sys,random
from time import *
pygame.init()

screen = pygame.display.set_mode((760,450))
pygame.display.set_caption("小轩井字棋")

chess_table_list = [pygame.Rect(i2*150,i*150,150,150) for i in range(3) for i2 in range(3)]
chess_table = list(range(1,10))
Xlist = []
Olist = []
if input('只是一个选择，不要怀疑，这是pygame游戏\n1=先下 2=后下') == '2':
    turn = 'AI'
else:
    turn = 'Player'
think_level = 0
tie = random.choice(['|一般一般，如此相当|','|未能赢我，不过如此|','|平手平局，旗鼓相当|','|让你一步，还是平局|','|小轩机器，你别不知|','|小轩棋法，造就本人|','|平平相对，坦坦相识|'])
win = random.choice(['|雪花飘飘，风雨潇潇|','|本以大师，啥也不是|','|不过如此，继续努力|','|下不为例，一定注意|','|小轩AI，天下无敌|','|小轩棋法，造就本人|','|我胜于你，小轩则同|'])

sound1 = pygame.mixer.Sound('落子1.wav')
sound2 = pygame.mixer.Sound('落子2.wav')

try:import ntpath
except:font = pygame.font.SysFont('kaittf', 80);font2 = pygame.font.SysFont('kaittf', 30)
else:font = pygame.font.SysFont('kaiti', 80);font2 = pygame.font.SysFont('kaiti', 30);del ntpath

def show_text(text,color=(0,0,0),pos=(0,0)):
    screen.blit(font.render((text),True,color),pos)
def show_text2(text,color=(0,0,0),pos=(0,0)):
    screen.blit(font2.render((text),True,color),pos)

def O_is_down(site):
    global chess_table
    return chess_table[site-1] == 'O'
def X_is_down(site):
    global chess_table
    return chess_table[site-1] == 'X'

def AI_think():
    global chess_table,think_level
    down_site = -1
    think_time = round(random.random(),2)
    think_level = 1
    
    # 打平了
    if (1 not in chess_table) and (2 not in chess_table) and (3 not in chess_table) and (4 not in chess_table) and (5 not in chess_table) and (6 not in chess_table) and (7 not in chess_table) and (8 not in chess_table) and (9 not in chess_table):
        return '平'
    
    # 活二区 特殊攻击 优先级：1
    '''
    例子：我方三种活二情况要下第一个：
    !OO   !--   !--    2 3
    ---   -O-   O--    5 9
    ---   --O   O--    4 7
    '''
    # 下第1个
    if ((X_is_down(2) and X_is_down(3)) or (X_is_down(5) and X_is_down(9)) or (X_is_down(4) and X_is_down(7))) and type(chess_table[0]) == int:
        return (down_site+1,think_time+0.3)
    # 下第2个
    if ((X_is_down(1) and X_is_down(3)) or (X_is_down(5) and X_is_down(8))) and type(chess_table[1]) == int:
        return (down_site+2,think_time)
    # 下第3个
    if ((X_is_down(1) and X_is_down(2)) or (X_is_down(5) and X_is_down(7)) or (X_is_down(6) and X_is_down(9))) and type(chess_table[2]) == int:
        return (down_site+3,think_time+0.3)
    # 下第4个
    if ((X_is_down(1) and X_is_down(7)) or (X_is_down(5) and X_is_down(6))) and type(chess_table[3]) == int:
        return (down_site+4,think_time)
    # 5个的不优先处理
    # 下第6个
    if ((X_is_down(3) and X_is_down(9)) or (X_is_down(4) and X_is_down(5))) and type(chess_table[5]) == int:
        return (down_site+6,think_time+0.1)
    # 下第7个
    if ((X_is_down(1) and X_is_down(4)) or (X_is_down(3) and X_is_down(5)) or (X_is_down(8) and X_is_down(9))) and type(chess_table[6]) == int:
        return (down_site+7,think_time+0.5)
    # 下第8个
    if ((X_is_down(2) and X_is_down(5)) or (X_is_down(7) and X_is_down(9))) and type(chess_table[7]) == int:
        return (down_site+8,think_time+0.1)
    # 下第9个
    if ((X_is_down(3) and X_is_down(6)) or (X_is_down(1) and X_is_down(5)) or (X_is_down(7) and X_is_down(8))) and type(chess_table[8]) == int:
        return (down_site+9,think_time+0.4)
    
    think_level += 1
    # 活二区 特级预防 优先级：2
    '''
    例子：对方三种活二情况要下第一个：
    !OO   !--   !--    2 3
    ---   -O-   O--    5 9
    ---   --O   O--    4 7
    '''
    # 下第1个
    if ((O_is_down(2) and O_is_down(3)) or (O_is_down(5) and O_is_down(9)) or (O_is_down(4) and O_is_down(7))) and type(chess_table[0]) == int:
        return (down_site+1,think_time+0.5)
    # 下第2个
    if ((O_is_down(1) and O_is_down(3)) or (O_is_down(5) and O_is_down(8))) and type(chess_table[1]) == int:
        return (down_site+2,think_time+0.25)
    # 下第3个
    if ((O_is_down(1) and O_is_down(2)) or (O_is_down(5) and O_is_down(7)) or (O_is_down(6) and O_is_down(9))) and type(chess_table[2]) == int:
        return (down_site+3,think_time+0.6)
    # 下第4个
    if ((O_is_down(1) and O_is_down(7)) or (O_is_down(5) and O_is_down(6))) and type(chess_table[3]) == int:
        return (down_site+4,think_time+0.1)
    # 5个的不优先处理
    # 下第6个
    if ((O_is_down(3) and O_is_down(9)) or (O_is_down(4) and O_is_down(5))) and type(chess_table[5]) == int:
        return (down_site+6,think_time+0.25)
    # 下第7个
    if ((O_is_down(1) and O_is_down(4)) or (O_is_down(3) and O_is_down(5)) or (O_is_down(8) and O_is_down(9))) and type(chess_table[6]) == int:
        return (down_site+7,think_time+1)
    # 下第8个
    if ((O_is_down(2) and O_is_down(5)) or (O_is_down(7) and O_is_down(9))) and type(chess_table[7]) == int:
        return (down_site+8,think_time+0.35)
    # 下第9个
    if ((O_is_down(3) and O_is_down(6)) or (O_is_down(1) and O_is_down(5)) or (O_is_down(7) and O_is_down(8))) and type(chess_table[8]) == int:
        return (down_site+9,think_time+0.75)
    
    # 空五区 一级攻击 优先级：3
    if type(chess_table[4]) == int:
        return (4,1.1)
    
    # 电脑方预双活二区 思考攻击 优先级：4
    # 对方预双活二区 思考预防 优先级：5
    think_level += 1
    
    if O_is_down(1) and X_is_down(5) and type(chess_table[8]) == int:
        return (8,2.6)
    if O_is_down(3) and X_is_down(5) and type(chess_table[6]) == int:
        return (6,2.4)
    if O_is_down(7) and X_is_down(5) and type(chess_table[2]) == int:
        return (2,2.8)
    if O_is_down(9) and X_is_down(5) and type(chess_table[0]) == int:
        return (0,2.9)
    
    # 对方预双活二区 思考预防 优先级：5
    if ((O_is_down(5) and O_is_down(9) and X_is_down(1)) or (O_is_down(1) and O_is_down(5) and X_is_down(9))) and type(chess_table[2]) == int and type(chess_table[6]) == int:
        return (random.choice([2,6]),3)
    if ((O_is_down(5) and O_is_down(7) and X_is_down(3)) or (O_is_down(3) and O_is_down(5) and X_is_down(7))) and type(chess_table[0]) == int and type(chess_table[8]) == int:
        return (random.choice([0,8]),3)
    if ((O_is_down(1) and O_is_down(9) and X_is_down(5)) or (O_is_down(3) and O_is_down(7) and X_is_down(5))) and type(chess_table[1]) == int and type(chess_table[3]) == int and type(chess_table[5]) == int and type(chess_table[7]) == int:
        return (random.choice([1,3,5,7]),3)
    
    think_level -= 1
    # 斜角 二级攻击 优先级：6
    int_list = []
    for i in chess_table:
        if i == 1 or i == 3 or i == 7 or i == 9:
            int_list.append(i-1)
    if int_list != []:
        return (random.choice(int_list),1.1)
    
    # 普通攻击 优先级：7
    int_list = []
    for i in chess_table:
        if type(i) == int:
            int_list.append(i-1)
    return (random.choice(int_list),2)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and turn == 'Player':
            for i in range(len(chess_table_list)):
                if chess_table_list[i].collidepoint(event.pos) and chess_table[i] != 'O' and chess_table[i] != 'X':
                    Orect = pygame.Rect(0,0,150,150)
                    Orect.center = chess_table_list[i].center
                    Olist.append((i,Orect))
                    chess_table[i] = 'O'
                    exec(random.choice(['sound1.play()','sound2.play()']))
                    turn = 'AI'
    screen.fill((255,255,255))
    if turn == 'Player':
        if (1 not in chess_table) and (2 not in chess_table) and (3 not in chess_table) and (4 not in chess_table) and (5 not in chess_table) and (6 not in chess_table) and (7 not in chess_table) and (8 not in chess_table) and (9 not in chess_table):
            turn = '平'
        if (X_is_down(1) and X_is_down(2) and X_is_down(3)) or (X_is_down(4) and X_is_down(5) and X_is_down(6)) or (X_is_down(7) and X_is_down(8) and X_is_down(9)) or (X_is_down(1) and X_is_down(4) and X_is_down(7)) or (X_is_down(2) and X_is_down(5) and X_is_down(8)) or (X_is_down(3) and X_is_down(6) and X_is_down(9)) or (X_is_down(1) and X_is_down(5) and X_is_down(9)) or (X_is_down(3) and X_is_down(5) and X_is_down(7)):
            turn = '胜'
    if turn == 'AI':
        AI_think_return = AI_think()
        if AI_think_return != '平':
            AI_down_site = AI_think_return[0]
            AI_think_time = AI_think_return[1]
            turn = 't_AI_think'
            t = time()
        else:
            turn = '平'
    if turn == 't_AI_think':
        if time() - t > AI_think_time:
            Xrect = pygame.Rect(0,0,150,150)
            Xrect.center = chess_table_list[AI_down_site].center
            Xlist.append((AI_down_site,Xrect))
            chess_table[AI_down_site] = 'X'
            exec(random.choice(['sound1.play()','sound2.play()']))
            turn = 'Player'
            # 小轩代表AI方大获全胜
            if (X_is_down(1) and X_is_down(2) and X_is_down(3)) or (X_is_down(4) and X_is_down(5) and X_is_down(6)) or (X_is_down(7) and X_is_down(8) and X_is_down(9)) or (X_is_down(1) and X_is_down(4) and X_is_down(7)) or (X_is_down(2) and X_is_down(5) and X_is_down(8)) or (X_is_down(3) and X_is_down(6) and X_is_down(9)) or (X_is_down(1) and X_is_down(5) and X_is_down(9)) or (X_is_down(3) and X_is_down(5) and X_is_down(7)):
                turn = '胜'
    for i in chess_table_list:
        pygame.draw.rect(screen,(255,185,12),i,3)
    if Xlist != []:
        for i in Xlist:
            pygame.draw.circle(screen,(0,0,0),(i[1].x+int(i[1].width/2),i[1].y+int(i[1].width/2)),int(i[1].width/3),0)
    if Olist != []:
        for i in Olist:
            pygame.draw.circle(screen,(255,0,0),(i[1].x+int(i[1].width/2),i[1].y+int(i[1].width/2)),int(i[1].width/3),0)
    for i in chess_table:
        if type(i) == int:
            show_text(str(i),pos=(chess_table_list[i-1].x+55,chess_table_list[i-1].y+35))
    show_text2('机器思考深度',pos=(461,11))
    show_text2(str(think_level),pos=(681,11))
    try:
        show_text2('机器思考时间',pos=(461,51))
        show_text2(str(AI_think_time)+'s',pos=(681,51))
    except:pass
    try:
        show_text2('机器思考位置',pos=(461,91))
        show_text2(str(AI_down_site+1),pos=(681,91))
    except:pass
    if turn == '平':
        show_text2(tie,color=(0,255,89),pos=(461,131))
    if turn == '胜':
        show_text2(win,color=(0,111,255),pos=(461,131))
    pygame.display.update()