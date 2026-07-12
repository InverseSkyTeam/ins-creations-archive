import pygame
import sys
from pygame.locals import *
import math
import random
pygame.init()
hospital_time = 1
r_x = 350
r_y = 300
screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption("疫情传播模拟")
pygame.font.init()
radius = 2
N = 1000

people_move = 6 #人群流动速度 2 or 6
hospital_sum = 0 #医院总容量 0 or 50 or 300
hide_time = 0 #潜伏期 0 or 14
sure_num = 4
hospital_people = 0
hide_num = 0
sure_list = random.sample(list(range(0,N)), sure_num)
people_status = [0 for i in range(N)]
people_sure = [0 for i in range(N)]
people_hide = [0 for i in range(N)]
for i in sure_list:
  people_status[i] = 1
radius = 150
x = []
y = []
for i in range(N):
  a = 2 * math.pi * random.random()
  r = random.random()
  x.append(radius*math.sqrt(r)*math.cos(a) + r_x)
  y.append(radius*math.sqrt(r)*math.sin(a) + r_y)

kk = 0
button = [(40,175,110,40),(40,275,110,40),(40,375,110,40)]
button_status = [0,0,0]
def init(button_status):
  global people_move,hospital_sum,hide_time,sure_num,hospital_people,hide_num,sure_list,people_status,people_sure,people_hide,x,y,kk
  people_move_list = [6,2]
  hospital_sum_list = [0,50,300]
  hide_time_list = [0,40]
  people_move = people_move_list[button_status[0]] #人群流动速度 2 or 6
  hospital_sum = hospital_sum_list[button_status[1]] #医院总容量 0 or 50 or 300
  hide_time = hide_time_list[button_status[2]] #潜伏期 0 or 14
  sure_num = 4
  hospital_people = 0
  hide_num = 0
  sure_list = random.sample(list(range(0,N)), sure_num)
  people_status = [0 for i in range(N)]
  people_sure = [0 for i in range(N)]
  people_hide = [0 for i in range(N)]
  for i in sure_list:
    people_status[i] = 1
  x = []
  y = []
  for i in range(N):
    a = 2 * math.pi * random.random()
    r = random.random()
    x.append(radius*math.sqrt(r)*math.cos(a) + r_x)
    y.append(radius*math.sqrt(r)*math.sin(a) + r_y)
  kk = 0

while True:
  screen.fill((255,255,255))
  pygame.draw.circle(screen, (255,255,255), (r_x,r_y), radius+5, 0)
  if hospital_sum == 300:
    pygame.draw.rect(screen, (0,255,0), (550,175,31,251), 2)
  elif hospital_sum == 50:
    pygame.draw.rect(screen, (0,255,0), (550,175,6,251), 2)
  for i in range(3):
    if button_status[i] == 0:
      pygame.draw.rect(screen, (255,0,0), button[i], 0)
    elif button_status[i] == 1:
      pygame.draw.rect(screen, (0,255,0), button[i], 0)
    else:
      pygame.draw.rect(screen, (0,0,255), button[i], 0)
  myfont = pygame.font.Font("STHEITI.ttf", 18)
  text = []
  if button_status[0] == 0:
    text.append("人流速度高")
  else:
    text.append("人流速度低")
  if button_status[1] == 0:
    text.append("医院容量0")
  elif button_status[1] == 1:
    text.append("医院容量50")
  else:
    text.append("医院容量300")
  if button_status[2] == 0:
    text.append("无潜伏期")
  else:
    text.append("14天潜伏期")
  for i in range(3):
    text_screen = myfont.render(text[i], True, (0,0,0))
    screen.blit(text_screen, (button[i][0]+(button[i][2]-text_screen.get_width())/2,button[i][1]+(button[i][3]-text_screen.get_height())/2))
  hospital_circle = 0
  for i in range(6):
    for j in range(50):
      hospital_circle += 1
      if hospital_circle <= hospital_people:
        pygame.draw.circle(screen, (255,0,0), (553+i*5,178+j*5), 2, 0)
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        for i in range(3):
          if (button[i][0]<=event.pos[0]<=button[i][0]+button[i][2]) and (button[i][1]<=event.pos[1]<=button[i][1]+button[i][3]):
            button_status[i] = button_status[i] + 1
            if i == 1:
              button_status[i] = button_status[i] % 3
            else:
              button_status[i] = button_status[i] % 2
        init(button_status)
  for i in range(N):
    x[i] = round(x[i])
    y[i] = round(y[i])
    move_index = random.randint(0,8)
    move_x = random.randint(0,people_move)
    move_y = people_move - move_x
    if random.randint(0,1) == 0:
      move_x = -move_x
    if random.randint(0,1) == 0:
      move_y = -move_y
    x[i] = x[i] + move_x
    y[i] = y[i] + move_y
    while ((x[i]-r_x)*(x[i]-r_x) + (y[i]-r_y)*(y[i]-r_y) > radius*radius):
      x[i] = x[i] - move_x
      y[i] = y[i] - move_y
      move_x = random.randint(0,people_move)
      move_y = people_move - move_x
      if random.randint(0,1) == 0:
        move_x = -move_x
      if random.randint(0,1) == 0:
        move_y = -move_y
      x[i] = x[i] + move_x
      y[i] = y[i] + move_y
    if people_status[i] == 0:
      for j in range(N):
        if people_status[j] == 1:
          if ((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]) <= 5):
            people_status[i] = 2
            hide_num += 1
            break
    if people_status[i] == 2:
      people_hide[i] += 1
      if people_hide[i] >= hide_time:
        people_status[i] = 1
        sure_num += 1   
    people_color = (135, 206, 235)
    if kk >= 10:
      if people_sure[i] == hospital_time and people_status[i] != 3 and hospital_people < hospital_sum:
        people_status[i] = 3
        hospital_people += 1
    if people_status[i] == 1:
      people_sure[i] += 1
      people_color = (255,0,0)
    elif people_status[i] == 2:
      people_color = (0,255,0)
    elif people_status[i] == 3:
      people_color = (255,255,255)
    pygame.draw.circle(screen, people_color, (int(x[i]),int(y[i])), 2, 0)
  kk += 1
  pygame.display.update()