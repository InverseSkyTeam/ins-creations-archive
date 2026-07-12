import pygame,sys,platform,pygame as pg,pyperclip,time
pygame.init()
screen = pygame.display.set_mode((1200,650))
pygame.display.set_caption("tk窗口制作器")
FONTNAME = 'kaiti'
startlist = [pygame.image.load("game_start_up.png"),pygame.image.load("game_start_down.png")]
startlist[1] = pygame.transform.scale(startlist[1],(300,50))
startlist[0] = pygame.transform.scale(startlist[0],(300,50))
startrect = pygame.Rect(450,550,300,50)
x1 = 0
y1 = 0
out_flag = 0
def show_code(text):
    wordx=10
    wordy=45
    for i in text:
        if i!= "\n":
            screen.blit(pygame.font.SysFont(FONTNAME,20).render(i,True,(0,0,0)),(wordx,wordy))
        wordx+=10
        if i == "\n":
            wordy+=20
            wordx=10
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
                    out_flag = 1
        if not startrect.collidepoint(x1,y1):
            startimg = startlist[0]
    if out_flag == 1:
        break
    screen.fill((255,255,100))
    screen.blit(pygame.font.SysFont(FONTNAME,150).render("制作窗口",True,(0,0,0)),(325,100))
    screen.blit(startimg,startrect)
    pygame.display.update()
out_flag = 0
rect = pygame.Rect(0,0,200,200)
drag_rect = pygame.Rect(190,190,20,20)
drag_text_rect = pygame.Rect(0,0,100,20)
x1 = 205
y1 = 205
select_rect = pygame.Rect(700,30,495,610)

COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.SysFont("kaiti", 20)
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                # if event.key == pg.K_RETURN:
                #     print(self.text)
                #     self.text = ''
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self,but):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
        but.text = self.text

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+1))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
entry = InputBox(select_rect.x+5,select_rect.y+100, 140, 32)

class Button():
    def __init__(self):
        global select_rect
        self.img = pygame.transform.scale(pygame.image.load("button.png"),(10,20))
        self.rect = self.img.get_rect()
        self.drag_flag = 0
        self.text = ""
        self.edit_flag = 0
        self.edit_rect = pygame.Rect(10,20,64,19)
        self.edit_color = (255,255,255)
        self.place_flag = 1
        self.add_flag = 0
        self.delete_rect = pygame.Rect(10,39,64,19)
        self.delete_color = (255,255,255)
        self.show_pos_rect = pygame.Rect(10,20,100,19)
        self.edit_type = 0
        self.red_rect = pygame.Rect(select_rect.x+5,select_rect.y+55,20,20)
        self.red_rect_color = (255,0,0)
        self.green_rect = pygame.Rect(select_rect.x+80,select_rect.y+55,20,20)
        self.green_rect_color = (0,255,0)
        self.blue_rect = pygame.Rect(select_rect.x+105,select_rect.y+55,20,20)
        self.blue_rect_color = (0,0,255)
        self.orange_rect = pygame.Rect(select_rect.x+30,select_rect.y+55,20,20)
        self.orange_rect_color = (255,200,0)
        self.yellow_rect = pygame.Rect(select_rect.x+55,select_rect.y+55,20,20)
        self.yellow_rect_color = (255,255,0)
        self.purple_rect = pygame.Rect(select_rect.x+130,select_rect.y+55,20,20)
        self.purple_rect_color = (150,0,255)
        self.white_rect = pygame.Rect(select_rect.x+155,select_rect.y+55,20,20)
        self.white_rect_color = (230,230,230)
        self.color_rect = pygame.Surface((self.rect.width,self.rect.height))
        self.color_rect.set_alpha(70)
        self.color_rect.fill((255,255,255))
        self.color_rect_color = (230,230,230)
    def edit(self):
        global page,edit_type
        page = 3
        edit_type = 1
        # self.color_rect_color = self.color_rect.get_at((0,0))
        self.color_rect = pygame.Surface((self.rect.width,self.rect.height))
        self.color_rect.fill((self.color_rect_color))
        self.color_rect.set_alpha(70)
        if platform.system() == "Darwin":
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("编辑按钮:",True,(0,0,0)),(select_rect.x+5,select_rect.y+1))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("按钮背景色",True,(0,0,0)),(select_rect.x+5,select_rect.y+26))
            pygame.draw.rect(screen,self.red_rect_color,self.red_rect,0)
            pygame.draw.rect(screen,self.green_rect_color,self.green_rect,0)
            pygame.draw.rect(screen,self.blue_rect_color,self.blue_rect,0)
            pygame.draw.rect(screen,self.orange_rect_color,self.orange_rect,0)
            pygame.draw.rect(screen,self.yellow_rect_color,self.yellow_rect,0)
            pygame.draw.rect(screen,self.purple_rect_color,self.purple_rect,0)
            pygame.draw.rect(screen,self.white_rect_color,self.white_rect,0)
            # pygame.draw.rect(screen,(0,0,0),self.white_rect,1)
            entry.update(self)
            entry.draw(screen)
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("按钮文字",True,(0,0,0)),(select_rect.x+5,select_rect.y+71))
        else:
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("编辑按钮:",True,(0,0,0)),(select_rect.x+5,select_rect.y+5))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("按钮背景色",True,(0,0,0)),(select_rect.x+5,select_rect.y+30))
            pygame.draw.rect(screen,self.red_rect_color,self.red_rect,0)
            pygame.draw.rect(screen,self.green_rect_color,self.green_rect,0)
            pygame.draw.rect(screen,self.blue_rect_color,self.blue_rect,0)
            pygame.draw.rect(screen,self.orange_rect_color,self.orange_rect,0)
            pygame.draw.rect(screen,self.yellow_rect_color,self.yellow_rect,0)
            pygame.draw.rect(screen,self.purple_rect_color,self.purple_rect,0)
            pygame.draw.rect(screen,self.white_rect_color,self.white_rect,0)
            # pygame.draw.rect(screen,(0,0,0),self.white_rect,1)
            entry.update(self)
            entry.draw(screen)
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("按钮文字",True,(0,0,0)),(select_rect.x+5,select_rect.y+75))
    def show(self):
        self.img = pygame.transform.scale(pygame.image.load("button.png"),(10+len(self.text)*15,20))
        self.rect = self.img.get_rect(center = self.rect.center)
        self.edit_rect.x = self.rect.x+self.rect.width
        self.edit_rect.y = self.rect.y+self.rect.height
        self.delete_rect.x = self.rect.x+self.rect.width
        self.delete_rect.y = self.rect.y+self.rect.height+19
        if self.place_flag == 1:
            if self.rect.x<0:
                self.rect.x=0
            if self.rect.y<0:
                self.rect.y=0
            if self.rect.x>rect.width-self.rect.width:
                self.rect.x=rect.width-self.rect.width
            if self.rect.y>rect.height-self.rect.height:
                self.rect.y=rect.height-self.rect.height
        if self.edit_flag == 1:
            pygame.draw.rect(screen,self.edit_color,self.edit_rect,0)
            pygame.draw.rect(screen,(0,0,0),self.edit_rect,1)
            pygame.draw.rect(screen,self.delete_color,self.delete_rect,0)
            pygame.draw.rect(screen,(0,0,0),self.delete_rect,1)
            if platform.system() == "Windows":
                screen.blit(pygame.font.SysFont(FONTNAME,15).render("编辑按钮",True,(0,0,0)),(self.edit_rect.x+2,self.edit_rect.y+2))
                screen.blit(pygame.font.SysFont(FONTNAME,15).render("删除按钮",True,(0,0,0)),(self.delete_rect.x+2,self.delete_rect.y+2))
            if platform.system() == "Darwin":
                screen.blit(pygame.font.SysFont(FONTNAME,15).render("编辑按钮",True,(0,0,0)),(self.edit_rect.x+2,self.edit_rect.y-2))
                screen.blit(pygame.font.SysFont(FONTNAME,15).render("删除按钮",True,(0,0,0)),(self.delete_rect.x+2,self.delete_rect.y-2))
        screen.blit(self.img,self.rect)
        screen.blit(pygame.font.SysFont(FONTNAME,15).render(self.text,True,(0,0,0)),(self.rect.x+5,self.rect.y))
        screen.blit(self.color_rect,(self.rect.x,self.rect.y))
    def get_event(self):
        global drag_button
        if drag_button.rect.collidepoint(x1,y1):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.add_flag = 1
        if self.rect.collidepoint(x1,y1):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.drag_flag = 1
                if event.button == 3 and self.place_flag==1:
                    self.edit_flag = 1
        if self.edit_flag == 1 and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if not self.edit_rect.collidepoint(x1,y1):
                    if not self.delete_rect.collidepoint(x1,y1):
                        self.edit_flag = 0
        if self.edit_rect.collidepoint(x1,y1) and self.edit_flag == 1:
            self.edit_color = (200,200,200)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.edit_flag = 0
                    self.edit_type = 1
        else:
            self.edit_color = (255,255,255)
        
        if self.edit_type == 1:
            self.edit()
        if self.delete_rect.collidepoint(x1,y1) and self.edit_flag == 1:
            self.delete_color = (200,200,200)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_list.remove(self)
        else:
            self.delete_color = (255,255,255)
        if event.type == pygame.MOUSEBUTTONUP and x1<rect.width and y1<rect.height:
            self.drag_flag = 0
            if self.place_flag == 0:
                if self.add_flag == 1:
                    button_list.append(Button())
                    self.add_flag = 0
                    button_list[len(button_list)-1].rect.x,button_list[len(button_list)-1].rect.y = drag_button.rect.x,drag_button.rect.y
                self.rect.x,self.rect.y = (select_rect.x+7,select_rect.y+30)
                
        if self.drag_flag == 1:
            self.rect.center = (x1,y1)
            self.show_pos_rect.x,self.show_pos_rect.y = self.rect.x+self.rect.width,self.rect.y+self.rect.height
            pygame.draw.rect(screen,(200,200,200),self.show_pos_rect,0)
            if platform.system() == "Windows":
                screen.blit(pygame.font.SysFont(FONTNAME,15).render("x:"+str(self.rect.x)+",y:"+str(self.rect.y),True,(0,0,0)),(self.rect.x+self.rect.width+5,self.rect.y+self.rect.height+2))
            if platform.system() == "Darwin":
                screen.blit(pygame.font.SysFont(FONTNAME,15).render("x:"+str(self.rect.x)+"y:"+str(self.rect.y),True,(0,0,0)),(self.rect.x+self.rect.width+5,self.rect.y+self.rect.height-2))
        if self.red_rect.collidepoint(x1,y1):
            self.red_rect_color = (200,0,0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    self.color_rect.fill((255,0,0))
                    self.color_rect_color = (255,0,0)
        else:
            self.red_rect_color = (255,0,0)
        if self.orange_rect.collidepoint(x1,y1):
            self.orange_rect_color = (200,145,0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    self.color_rect.fill((255,200,0))
                    self.color_rect_color = (255,200,0)
        else:
            self.orange_rect_color = (255,200,0)
        if self.yellow_rect.collidepoint(x1,y1):
            self.yellow_rect_color = (200,200,0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    self.color_rect.fill((255,255,0))
                    self.color_rect_color = (255,255,0)
        else:
            self.yellow_rect_color = (255,255,0)
        if self.green_rect.collidepoint(x1,y1):
            self.green_rect_color = (0,200,0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    self.color_rect.fill((0,255,0))
                    self.color_rect_color = (0,255,0)
        else:
            self.green_rect_color = (0,255,0)
        if self.blue_rect.collidepoint(x1,y1):
            self.blue_rect_color = (0,0,200)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    self.color_rect.fill((0,0,255))
                    self.color_rect_color = (0,0,255)
        else:
            self.blue_rect_color = (0,0,255)
        if self.purple_rect.collidepoint(x1,y1):
            self.purple_rect_color = (145,0,200)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    self.color_rect.fill((150,0,255))
                    self.color_rect_color = (150,0,255)
        else:
            self.purple_rect_color = (200,0,255)
        if self.white_rect.collidepoint(x1,y1):
            self.white_rect_color = (150,150,150)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    self.color_rect.fill((255,255,255))
                    self.color_rect_color = (230,230,230)
        else:
            self.white_rect_color = (230,230,230)
button_list = []
drag_button = Button()
drag_flag = 0
new_select_rect = pygame.Rect(1125,11,70,19)
edit_select_rect = pygame.Rect(1050,11,70,19)
button_select_rect = pygame.Rect(975,11,70,19)
drag_button.rect.x,drag_button.rect.y = (select_rect.x+7,select_rect.y+30)
drag_button.place_flag = 0
page = 1

class Entry():
    def __init__(self):
        self.img = pygame.transform.scale(pygame.image.load("entry.png"),(100,16))
        self.rect = self.img.get_rect()
        self.drag_flag = 0
        self.edit_flag = 0
        self.edit_color = (255,255,255)
        self.edit_rect = pygame.Rect(10,20,64,19)
        self.delete_color = (255,255,255)
        self.delete_rect = pygame.Rect(10,39,64,19)
        self.lenth = 100
        self.lenth_drag_rect = pygame.Rect(select_rect.x+105,select_rect.y+51,20,20)
        self.lenth_rect = pygame.Rect(select_rect.x+5,select_rect.y+58.5,100,5)
        self.start_edit = 0
        self.drag_type = 0
        self.place_type = 0
    def edit(self):
        global page
        page = 4
        self.lenth = self.lenth_drag_rect.x-select_rect.x-5
        screen.blit(pygame.font.SysFont(FONTNAME,20).render("编辑输入框:",True,(0,0,0)),(select_rect.x+5,select_rect.y+1))
        screen.blit(pygame.font.SysFont(FONTNAME,20).render("编辑长度:",True,(0,0,0)),(select_rect.x+5,select_rect.y+21))
        pygame.draw.ellipse(screen,(0,0,0),self.lenth_drag_rect,0)
        pygame.draw.rect(screen,(0,0,0),self.lenth_rect,0)
        self.lenth_rect.width = self.lenth
        self.rect.width = self.lenth_drag_rect.x-select_rect.x-5
    def show(self):
        self.img = pygame.transform.scale(pygame.image.load("entry.png"),(self.lenth,16))
        screen.blit(self.img,self.rect)
    def get_event(self):
        if self.lenth_drag_rect.collidepoint(x1,y1):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.drag_type = 1
        if event.type == pygame.MOUSEBUTTONUP:
            self.drag_type = 0
            if self.place_type == 1 and drag_entry.rect.x<rect.width and drag_entry.rect.y<rect.height:
                entry_list.append(Entry())
                entry_list[len(entry_list)-1].rect.x = drag_entry.rect.x
                entry_list[len(entry_list)-1].rect.y = drag_entry.rect.y
                drag_entry.rect.x,drag_entry.rect.y = select_rect.x+7,select_rect.y+95
        if self.drag_type == 1:
            self.lenth_drag_rect.center = (x1,select_rect.y+61.5)
            if self.place_type == 0:
                if self.lenth_drag_rect.x<select_rect.x+5:
                    self.lenth_drag_rect.x = select_rect.x+5
                if self.lenth_drag_rect.x>select_rect.x+205:
                    self.lenth_drag_rect.x = select_rect.x+205
        if self.rect.collidepoint(x1,y1):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.drag_flag = 1
                if event.button == 3 and self.place_type == 0:
                    self.edit_flag = 1
        if event.type == pygame.MOUSEBUTTONUP:
            self.drag_flag = 0
        if self.drag_flag == 1:
            self.rect.center = (x1,y1)
        if self.delete_rect.collidepoint(x1,y1):
            self.delete_color = (200,200,200)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.edit_flag = 0
                    entry_list.remove(self)
        else:
            self.delete_color = (255,255,255)
        if self.edit_rect.collidepoint(x1,y1):
            self.edit_color = (200,200,200)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.edit_flag = 0
                    self.start_edit = 1
        else:
            self.edit_color = (255,255,255)
        if self.start_edit == 1:
            self.edit()
        if self.edit_flag == 1:
            self.edit_rect.x = self.rect.x+self.rect.width
            self.delete_rect.x = self.rect.x+self.rect.width
            self.edit_rect.y = self.rect.y+self.rect.height
            self.delete_rect.y = self.rect.y+self.rect.height+19
            pygame.draw.rect(screen,self.edit_color,self.edit_rect,0)
            pygame.draw.rect(screen,self.delete_color,self.delete_rect,0)
            pygame.draw.rect(screen,(0,0,0),self.edit_rect,1)
            pygame.draw.rect(screen,(0,0,0),self.delete_rect,1)
            if platform.system() == "Windows":
                screen.blit(pygame.font.SysFont(FONTNAME,15).render("编辑控件",True,(0,0,0)),(self.edit_rect.x+2,self.edit_rect.y+2))
                screen.blit(pygame.font.SysFont(FONTNAME,15).render("删除控件",True,(0,0,0)),(self.delete_rect.x+2,self.delete_rect.y+2))
            if platform.system() == "Darwin":
                screen.blit(pygame.font.SysFont(FONTNAME,15).render("编辑控件",True,(0,0,0)),(self.edit_rect.x+2,self.edit_rect.y-2))
                screen.blit(pygame.font.SysFont(FONTNAME,15).render("删除控件",True,(0,0,0)),(self.delete_rect.x+2,self.delete_rect.y-2))
entry_list = []
drag_entry = Entry()
drag_entry.place_type = 1
drag_entry.rect.x = select_rect.x+7
drag_entry.rect.y = select_rect.y+95
new_select_rect_color = (200,200,200)
edit_select_rect_color = (230,230,230)
button_select_rect_color = (230,230,230)
lenth_drag_rect = pygame.Rect(select_rect.x+46,select_rect.y+30,20,20)
width_drag_rect = pygame.Rect(select_rect.x+61,select_rect.y+55,20,20)
lenth_rect = pygame.Rect(select_rect.x+30,select_rect.y+37.5,16,5)
width_rect = pygame.Rect(select_rect.x+30,select_rect.y+63.5,31,5)
lenth_drag_flag = 0
width_drag_flag = 0
red_drag_rect = pygame.Rect(select_rect.x+270,select_rect.y+105,20,20)
green_drag_rect = pygame.Rect(select_rect.x+270,select_rect.y+130,20,20)
blue_drag_rect = pygame.Rect(select_rect.x+270,select_rect.y+155,20,20)
red_rect = pygame.Rect(select_rect.x+30,select_rect.y+112.5,240,5)
green_rect = pygame.Rect(select_rect.x+30,select_rect.y+137.5,240,5)
blue_rect = pygame.Rect(select_rect.x+30,select_rect.y+162.5,240,5)
red_drag_flag = 0
green_drag_flag = 0
blue_drag_flag = 0
color = (240,240,240)
edit_type = 0
nextlist = [pygame.image.load("next2.png"),pygame.image.load("next.png")]
nextlist[1] = pygame.transform.scale(nextlist[1],(300,70))
nextlist[0] = pygame.transform.scale(nextlist[0],(300,70))
nextrect = pygame.Rect(875,575,300,100)
nextimg = nextlist[0]
exit = False
while True:
    screen.fill((255,255,100))
    pygame.draw.rect(screen,color,rect,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        entry.handle_event(event)
        if event.type == pygame.MOUSEMOTION:
            x1 = event.pos[0]
            y1 = event.pos[1]
        if nextrect.collidepoint(x1,y1):
            nextimg = nextlist[1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    exit = True
        if not nextrect.collidepoint(x1,y1):
            nextimg = nextlist[0]
        if drag_rect.collidepoint(x1,y1):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drag_flag = 1
        if event.type == pygame.MOUSEBUTTONUP:
            drag_flag = 0
        if new_select_rect.collidepoint(x1,y1):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    page = 1
        if edit_select_rect.collidepoint(x1,y1):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    page = 2
        if lenth_drag_rect.collidepoint(x1,y1):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    lenth_drag_flag = 1
        if lenth_drag_flag == 1 and page == 2:
            lenth_drag_rect.x = x1-10
            rect.width = (lenth_drag_rect.x-select_rect.x-30)*12
            rect.height = (width_drag_rect.x-select_rect.x-30)*6.5
        if event.type == pygame.MOUSEBUTTONUP:
            lenth_drag_flag = 0
        if width_drag_rect.collidepoint(x1,y1):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    width_drag_flag = 1
        if width_drag_flag == 1 and page == 2:
            width_drag_rect.x = x1-10
            rect.width = (lenth_drag_rect.x-select_rect.x-30)*12
            rect.height = (width_drag_rect.x-select_rect.x-30)*6.5
        if event.type == pygame.MOUSEBUTTONUP:
            width_drag_flag = 0
        if red_drag_rect.collidepoint(x1,y1):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    red_drag_flag = 1
        if red_drag_flag == 1:
            red_drag_rect.x = x1-10
        if green_drag_rect.collidepoint(x1,y1):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    green_drag_flag = 1
        if green_drag_flag == 1:
            green_drag_rect.x = x1-10
        if blue_drag_rect.collidepoint(x1,y1):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    blue_drag_flag = 1
        if blue_drag_flag == 1:
            blue_drag_rect.x = x1-10
        if event.type == pygame.MOUSEBUTTONUP:
            red_drag_flag = 0
            green_drag_flag = 0
            blue_drag_flag = 0
    if red_drag_rect.x>select_rect.x+285:
        red_drag_rect.x=select_rect.x+285
    if green_drag_rect.x>select_rect.x+285:
        green_drag_rect.x=select_rect.x+285
    if blue_drag_rect.x>select_rect.x+285:
        blue_drag_rect.x=select_rect.x+285
    if red_drag_rect.x<select_rect.x+30:
        red_drag_rect.x=select_rect.x+30
    if green_drag_rect.x<select_rect.x+30:
        green_drag_rect.x=select_rect.x+30
    if blue_drag_rect.x<select_rect.x+30:
        blue_drag_rect.x=select_rect.x+30
    if lenth_drag_rect.x>select_rect.x+130:
        lenth_drag_rect.x = select_rect.x+130
    if lenth_drag_rect.x<select_rect.x+30:
        lenth_drag_rect.x = select_rect.x+30
    if width_drag_rect.x>select_rect.x+130:
        width_drag_rect.x = select_rect.x+130
    if width_drag_rect.x<select_rect.x+30:
        width_drag_rect.x = select_rect.x+30
    if drag_flag == 1:
        drag_text_rect.x,drag_text_rect.y = x1,y1
        pygame.draw.rect(screen,(200,200,200),drag_text_rect,0)
        screen.blit(pygame.font.SysFont(FONTNAME,15).render("宽"+str(rect.width)+"高"+str(rect.height),True,(0,0,0)),(x1+10,y1))
        drag_rect.center = (x1,y1)
        rect.width = drag_rect.x+10
        rect.height = drag_rect.y+10
    pygame.draw.rect(screen,new_select_rect_color,new_select_rect,0)
    pygame.draw.rect(screen,edit_select_rect_color,edit_select_rect,0)
    pygame.draw.rect(screen,(200,200,200),select_rect,0)
    if platform.system() == "Windows":
        screen.blit(pygame.font.SysFont(FONTNAME,15).render("新建控件",True,(0,0,0)),(new_select_rect.x+5,new_select_rect.y+2))
        screen.blit(pygame.font.SysFont(FONTNAME,15).render("编辑窗口",True,(0,0,0)),(edit_select_rect.x+5,edit_select_rect.y+2))
    if platform.system() == "Darwin":
        screen.blit(pygame.font.SysFont(FONTNAME,15).render("新建控件",True,(0,0,0)),(new_select_rect.x+5,new_select_rect.y-2))
        screen.blit(pygame.font.SysFont(FONTNAME,15).render("编辑窗口",True,(0,0,0)),(edit_select_rect.x+5,edit_select_rect.y-2))
    if page == 1:
        for i in button_list:
            i.edit_type = 0
        for i in entry_list:
            i.start_edit = 0
        screen.blit(pygame.font.SysFont(FONTNAME,20).render("新建按钮控件:",True,(0,0,0)),(select_rect.x+5,select_rect.y+5))
        screen.blit(drag_button.img,(select_rect.x+7,select_rect.y+30))
        screen.blit(pygame.font.SysFont(FONTNAME,20).render("新建输入框控件:",True,(0,0,0)),(select_rect.x+5,select_rect.y+70))
        screen.blit(drag_entry.img,(select_rect.x+7,select_rect.y+95))
        new_select_rect_color = (200,200,200)
        edit_select_rect_color = (230,230,230)
        drag_button.show()
        drag_button.get_event()
        drag_entry.show()
        drag_entry.get_event()
    if page == 2:
        for i in button_list:
            i.edit_type = 0
        for i in entry_list:
            i.start_edit = 0
        new_select_rect_color = (230,230,230)
        edit_select_rect_color = (200,200,200)
        pygame.draw.ellipse(screen,(100,100,100),lenth_drag_rect,0)
        pygame.draw.ellipse(screen,(100,100,100),width_drag_rect,0)
        lenth_rect = pygame.Rect(select_rect.x+30,select_rect.y+37.5,lenth_drag_rect.x-select_rect.x-30,5)
        width_rect = pygame.Rect(select_rect.x+30,select_rect.y+63.5,width_drag_rect.x-select_rect.x-30,5)
        pygame.draw.rect(screen,(0,0,0),lenth_rect,0)
        pygame.draw.rect(screen,(0,0,0),width_rect,0)
        color = (red_drag_rect.x-select_rect.x-30,green_drag_rect.x-select_rect.x-30,blue_drag_rect.x-select_rect.x-30)
        pygame.draw.ellipse(screen,(255,0,0),red_drag_rect,0)
        pygame.draw.ellipse(screen,(0,255,0),green_drag_rect,0)
        pygame.draw.ellipse(screen,(0,0,255),blue_drag_rect,0)
        red_rect.width = red_drag_rect.x-select_rect.x-30
        green_rect.width = green_drag_rect.x-select_rect.x-30
        blue_rect.width = blue_drag_rect.x-select_rect.x-30
        pygame.draw.rect(screen,(200,0,0),red_rect,0)
        pygame.draw.rect(screen,(0,200,0),green_rect,0)
        pygame.draw.rect(screen,(0,0,200),blue_rect,0)
        if platform.system() == "Windows":
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("编辑窗口:",True,(0,0,0)),(select_rect.x+5,select_rect.y+5))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("长:",True,(0,0,0)),(select_rect.x+5,select_rect.y+30))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("宽:",True,(0,0,0)),(select_rect.x+5,select_rect.y+55))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render(str(rect.width),True,(0,0,0)),(select_rect.x+145,select_rect.y+30))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render(str(rect.height),True,(0,0,0)),(select_rect.x+145,select_rect.y+55))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("窗口颜色:",True,(0,0,0)),(select_rect.x+5,select_rect.y+80))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("红:",True,(255,0,0)),(select_rect.x+5,select_rect.y+105))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("绿:",True,(0,255,0)),(select_rect.x+5,select_rect.y+130))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("蓝:",True,(0,0,255)),(select_rect.x+5,select_rect.y+155))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render(str(color[0]),True,(255,0,0)),(select_rect.x+320,select_rect.y+105))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render(str(color[1]),True,(0,255,0)),(select_rect.x+320,select_rect.y+130))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render(str(color[2]),True,(0,0,255)),(select_rect.x+320,select_rect.y+155))
        if platform.system() == "Darwin":
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("编辑窗口:",True,(0,0,0)),(select_rect.x+5,select_rect.y+1))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("长:",True,(0,0,0)),(select_rect.x+5,select_rect.y+26))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("宽:",True,(0,0,0)),(select_rect.x+5,select_rect.y+51))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render(str(rect.width),True,(0,0,0)),(select_rect.x+145,select_rect.y+26))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render(str(rect.height),True,(0,0,0)),(select_rect.x+145,select_rect.y+51))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("窗口颜色:",True,(0,0,0)),(select_rect.x+5,select_rect.y+76))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("红:",True,(255,0,0)),(select_rect.x+5,select_rect.y+101))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("绿:",True,(0,255,0)),(select_rect.x+5,select_rect.y+126))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render("蓝:",True,(0,0,255)),(select_rect.x+5,select_rect.y+151))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render(str(color[0]),True,(255,0,0)),(select_rect.x+320,select_rect.y+101))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render(str(color[1]),True,(0,255,0)),(select_rect.x+320,select_rect.y+126))
            screen.blit(pygame.font.SysFont(FONTNAME,20).render(str(color[2]),True,(0,0,255)),(select_rect.x+320,select_rect.y+151))
    if page == 3:
        for i in entry_list:
            i.start_edit = 0
        new_select_rect_color = (230,230,230)
        edit_select_rect_color = (230,230,230)
        button_select_rect_color = (200,200,200)
        pygame.draw.rect(screen,button_select_rect_color,button_select_rect,0)
        if platform.system() == "Windows":
            screen.blit(pygame.font.SysFont(FONTNAME,15).render("编辑按钮",True,(0,0,0)),(button_select_rect.x+5,button_select_rect.y+2))
        if platform.system() == "Darwin":
            screen.blit(pygame.font.SysFont(FONTNAME,15).render("编辑按钮",True,(0,0,0)),(button_select_rect.x+5,button_select_rect.y-2))
    if page == 4:
        for i in button_list:
            i.edit_type = 0
        new_select_rect_color = (230,230,230)
        edit_select_rect_color = (230,230,230)
        button_select_rect_color = (200,200,200)
        pygame.draw.rect(screen,button_select_rect_color,button_select_rect,0)
        if platform.system() == "Windows":
            screen.blit(pygame.font.SysFont(FONTNAME,15).render("编辑控件",True,(0,0,0)),(button_select_rect.x+5,button_select_rect.y+2))
        if platform.system() == "Darwin":
            screen.blit(pygame.font.SysFont(FONTNAME,15).render("编辑控件",True,(0,0,0)),(button_select_rect.x+5,button_select_rect.y-2))
    for i in button_list:
        i.get_event()
        i.show()
    for i in entry_list:
        i.show()
        i.get_event()
    screen.blit(nextimg,nextrect)
    if exit == True:
        break;
    pygame.display.update()
text = "import tkinter as tk\nroot = tk.Tk()\nroot.geometry(\""+str(rect.width)+"x"+str(rect.height)+"\")\n"
for i in range(len(button_list)):
    # print(button_list[i].color_rect_color)
    if button_list[i].color_rect_color == (255,0,0):
        bg_color = "red"
    if button_list[i].color_rect_color == (255,200,0):
        bg_color = "orange"
    if button_list[i].color_rect_color == (255,255,0):
        bg_color = "yellow"
    if button_list[i].color_rect_color == (0,255,0):
        bg_color = "green"
    if button_list[i].color_rect_color == (0,0,255):
        bg_color = "blue"
    if button_list[i].color_rect_color == (150,0,255):
        bg_color = "purple"
    if button_list[i].color_rect_color == (230,230,230):
        bg_color = "gray"
    text+="Button"+str(i+1)+" = tk.Button(root,text = \""+button_list[i].text+"\",bg = \""+bg_color+"\")\nButton"+str(i+1)+".place(x="+str(button_list[i].rect.x)+",y="+str(button_list[i].rect.y)+")\n"
for i in range(len(entry_list)):
    text+="Entry"+str(i+1)+" = tk.Entry(root,width="+str(int(entry_list[i].lenth/10))+")\nEntry"+str(i+1)+".place(x="+str(entry_list[i].rect.x)+",y="+str(entry_list[i].rect.y)+")\n"
text+="root.mainloop()"
# print(text)
copylist = [pygame.image.load("copy.png"),pygame.image.load("copy2.png")]
copylist[1] = pygame.transform.scale(copylist[1],(300,70))
copylist[0] = pygame.transform.scale(copylist[0],(300,70))
copyrect = pygame.Rect(875,475,300,100)
copyimg = copylist[0]
copy = pygame.image.load("copyimg.png")
copyed = False
copyedrect = pygame.Surface((120,120))
copyedrect.fill((0,0,0))
copyedrect.set_alpha(170)
t1 = 0
while True:
    screen.fill((255,255,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            x1 = event.pos[0]
            y1 = event.pos[1]
        if copyrect.collidepoint(x1,y1):
            copyimg = copylist[1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pyperclip.copy(text)
                    copyed = True
                    t1 = time.time()
        else:
            copyimg = copylist[0]
    screen.blit(pygame.font.SysFont(FONTNAME,30).render("最终代码:",True,(0,0,0)),(10,10))
    show_code(text)
    screen.blit(copyimg,copyrect)
    if copyed == True:
        screen.blit(copyedrect,(540,265))
        screen.blit(copy,(550,275))
    pygame.display.update()
    t2 = time.time()
    if t2-t1>1:
        copyed = False