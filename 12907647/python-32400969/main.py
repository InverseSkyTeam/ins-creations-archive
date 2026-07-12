import pygame,sys,time
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("INS-GameBox:保卫逆天塔防")

class Floor(object):
    def __init__(self,moveid,rect_index):
        self.rect = pygame.Rect(rect_index%25*40,rect_index//25*40,40,40)
        self.color = (225,255,255)
        self.move_tip = {'w':'up','s':'down','a':'left','d':'right','0':'none'}[moveid]
    def show(self):
        if self.move_tip != 'none':
            pygame.draw.rect(screen,self.color,self.rect,0)

class MainGameMap(object):
    def __init__(self,the_map):
        self.map = []
        for self.i in range(len(the_map)):
            self.map.append(Floor(the_map[self.i],self.i))
    def show(self):
        for self.i in self.map:
            # print(self.i.rect.x)
            self.i.show()

class Enemy(object):
    def __init__(self,the_map):
        self.rect = pygame.Rect(40,80,40,40)
        self.go_where = 'none'
        self.mapp = the_map
    def update_go(self):
        for self.i in self.mapp:
            if self.rect.topleft == self.i.rect.topleft:
                self.go_where = self.i.move_tip
    def move(self):
        self.update_go()
        if self.go_where == 'up':
            self.rect.y -= 1
        if self.go_where == 'down':
            self.rect.y += 1
        if self.go_where == 'left':
            self.rect.x -= 1
        if self.go_where == 'right':
            self.rect.x += 1
    def is_out(self):
        if self.rect.topleft == (920,40):
            return True
        else:
            return False
    def show(self):
        pygame.draw.rect(screen,(255,0,0),self.rect,0)

game_map1 = [
    '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
    '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','w','0',
    '0','d','d','d','d','d','d','d','d','d','s','0','0','0','0','0','0','0','0','0','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','s','0','0','0','0','0','0','0','0','0','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','s','0','0','0','0','d','d','d','d','s','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','s','0','0','0','0','w','0','0','0','s','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','s','0','0','0','0','w','0','0','0','s','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','s','0','0','0','0','w','0','0','0','s','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','s','0','0','0','0','w','0','0','0','s','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','s','0','0','0','0','w','0','0','0','s','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','s','0','0','0','0','w','0','0','0','s','0','0','0','w','0',
    '0','0','0','0','0','0','0','0','0','0','d','d','d','d','d','w','0','0','0','d','d','d','d','w','0',
    '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
    '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
    '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
    ]
main_game_map1 = MainGameMap(game_map1)
enemylist = [Enemy(main_game_map1.map)]
tt = time.time()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    if time.time() - tt > 0.4:
        tt = time.time()
        enemylist.append(Enemy(main_game_map1.map))
    main_game_map1.show()
    for i in enemylist:
        i.move()
        i.show()
        if i.is_out():
            enemylist.remove(i)
    pygame.display.update()