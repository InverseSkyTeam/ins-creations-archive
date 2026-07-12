'''
Cloud
onlinenum
onlinepersonlist{序列号：[参与次数，获胜次数，是否已经匹配]}
onracinglist{对战序列号：[题目列表，自己序列号，对方序列号，自己答对，对方答对，谁先答对，答题总题数]}

'''
import io
import json

onlinenum = io.IO("21192662","59842528")
onlinenum.open('onlinenum')#要存储的变量名
onlinenum.write(json.dumps(0))
onlinenum.close()

oi.open(name)
data = json.loads(io.read())#loads用于转换为字典或列表
io.close()





import pygame,sys

pygame.init()

screen = pygame.display.set_mode((700,500))

pygame.display.set_caption("我的作品")

def insertText(stri,col,x,y,sr,big):
    sr.blit(pygame.font.Font("Font.ttf",big).render(stri,True,col),(x,y))
def insertRect(col,x,y,w,h,sr,b):
    pygame.draw.rect(sr,col,pygame.Rect(x,y,w,h),b)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    insertText("在线人数",(50,50,50),0,0,screen,40)
    pygame.display.update()