import pygame
import sys
import gamedata
pygame.init()

screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption('【INS-GameBox】纸中立方 (3^3 in cube)')

try:import ntpath
except:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaittf', size).render((text),True,color),pos)")
else:exec("def show_text(text,color=(0,0,0),pos=(0,0),size=30):screen.blit(pygame.font.SysFont('kaiti', size).render((text),True,color),pos)")
finally:pass

def convert_sf(sf):   # sf -> surface
    return {
        'front': 1,
        'behind': 2,
        'left': 3,
        'right': 4,
        'on': 5,
        'under': 6,
    } [sf]

class Block:
    def __init__(self,x,y,sf,mode):
        self.position = {
            'x': x+1,
            'y': y+1,
            'surface': convert_sf(sf),
        }
        self.number = str((self.position['x']*(self.position['surface']+2) + self.position['y']*(self.position['surface'])) % 10) + \
                      str((self.position['x']*(self.position['surface']) + self.position['y']*(self.position['surface']+2)) % 10)
        self.mode = mode
        self.info = ''
        if '-' in self.mode:
            tmp = self.mode.split('-')
            self.mode = tmp[0]
            self.info = eval(self.mode[1])
        self.color = {
            'normal': (127,255,212),
            'goto': (255,250,205),
            'finish': (255,228,225),
        } [self.mode]
        self.rect = pygame.Rect(350,200,300,300)
    def draw(self):
        pygame.draw.rect(screen,(160,32,240),self.rect,6)
        pygame.draw.rect(screen,self.color,self.rect,0)
        show_text(self.number,pos=(self.rect.centerx-30,self.rect.centery-30),size=60)

class Cube:
    def __init__(self,cubedata,startpos):
        self.data = cubedata.copy()
        for sf in cubedata:
            for y in range(len(cubedata[sf])):
                for x in range(len(cubedata[sf][y])):
                    self.data[sf][y][x] = Block(x,y,sf,cubedata[sf][y][x])
        self.x = startpos[0]
        self.y = startpos[1]
    def move(self,to):
        if to == 'left':
            self.x -= 1
        elif to == 'right':
            self.x += 1
        elif to == 'up':
            self.y -= 1
        else:
            self.y += 1
        if self.y >= len(self.data['front']):
            self.rotate3d(to)
            self.y = 0
        if self.y < 0:
            self.rotate3d(to)
            self.y = len(self.data['front']) - 1
        if self.x >= len(self.data['front'][self.y]):
            self.rotate3d(to)
            self.x = 0
        if self.x < 0:
            self.rotate3d(to)
            self.x = len(self.data['front'][self.y]) - 1
    def rotate3d(self,to):
        if to == 'left':
            self.data['right'], self.data['front'], self.data['left'], self.data['behind'] = \
            self.data['front'], self.data['left'], self.data['behind'], self.data['right']
        elif to == 'right':
            self.data['front'], self.data['left'], self.data['behind'], self.data['right'] = \
            self.data['right'], self.data['front'], self.data['left'], self.data['behind']
        elif to == 'up':
            self.data['front'], self.data['on'], self.data['behind'], self.data['under'] = \
            self.data['on'], self.data['behind'], self.data['under'], self.data['front']
        else:
            self.data['on'], self.data['behind'], self.data['under'], self.data['front'] = \
            self.data['front'], self.data['on'], self.data['behind'], self.data['under']
    def get_mode(self):
        return self.data['front'][self.y][self.x].mode
    def show(self):
        self.data['front'][self.y][self.x].draw()

levelindex = 0
leveldata = gamedata.levels[levelindex]
cube = Cube(leveldata,(0,0))
tonext = False

while not tonext:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cube.move('left')
            elif event.key == pygame.K_RIGHT:
                cube.move('right')
            elif event.key == pygame.K_UP:
                cube.move('up')
            elif event.key == pygame.K_DOWN:
                cube.move('down')
            elif event.key == pygame.K_n:
                tonext = True
    screen.fill((0,0,0))
    cube.show()
    # show_text(str(list(filter(lambda x:cube.data['front']== x[1], leveldata.items()))[0][0]),color=(255,255,255),pos=(0,0))
    show_text('你好，欢迎来到这个叫做地球的世界。',color=(255,255,255),pos=(0,0))
    show_text('要想好好在这个世界里生存，请务必牢记这个世界的基础规则。',color=(255,255,255),pos=(0,30))
    show_text('它们是由这个世界的一些科学家提出的，相对可靠，但非绝对可靠。',color=(255,255,255),pos=(0,60))
    show_text('地球世界真实存在。现在请尝试按科学家提出的方法移动。',color=(255,255,255),pos=(0,90))
    show_text('移动后，如你认为完全了解了自己、地球甚至一切，按下N进入下一个大地。',color=(255,255,255),pos=(0,120))
    show_text('1.我们能看到一块脚下的带有数字的地，以及周围的黑暗、对话显示',color=(88,255,240),pos=(0,550))
    show_text('2.按下上下左右箭头移动、行走；地的颜色有很多种',color=(88,255,240),pos=(0,580))
    show_text('3.这个世界重力向下，因为地球有很大的引力',color=(88,255,240),pos=(0,610))
    show_text('4.脚下的地是一个单位，我们在多个单位的大地上行走，路线可以重复',color=(88,255,240),pos=(0,640))
    show_text('5.到达一定位置可以进入下一个大地；记载中曾有生物摆脱过地球引力',color=(88,255,240),pos=(0,670))
    pygame.display.update()

levelindex = 1
leveldata = gamedata.levels[levelindex]
cube = Cube(leveldata,(0,0))
n_down = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cube.move('left')
            elif event.key == pygame.K_RIGHT:
                cube.move('right')
            elif event.key == pygame.K_UP:
                cube.move('up')
            elif event.key == pygame.K_DOWN:
                cube.move('down')
            elif event.key == pygame.K_n:
                n_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_n:
                n_down = False
    screen.fill((0,0,0))
    cube.show()
    if cube.get_mode() == 'finish':
        show_text('提示:按下n进入下一个大地',color=(255,228,181),pos=(0,30))
        if n_down:
            n_down = False
            levelindex += 1
            startpos = (0,0)
            if levelindex == 2:
                startpos = (0,1)
            try:
                leveldata = gamedata.levels[levelindex]
                cube = Cube(leveldata,startpos)
            except:
                break
    elif cube.get_mode() == 'goto':
        show_text('提示:按下n进入传送门',color=(255,228,181),pos=(0,30))
        if n_down:
            n_down = False
            info = cude.data['front'][cube.y][cube.x].info
            cube.x, cube.y = info[1], info[2]
            if info[0] == 'behind':
                cube.data['left'], cube.data['right'] = cube.data['right'], cube.data['left']
                cube.data['front'], cube.data['behind'] = cube.data['behind'], cube.data['front']
            elif info[0] in ['left','right','up','down']:
                cube.rotate3d(info[0])
    show_text('大地序号:'+str(levelindex),color=(255,228,181),pos=(0,0))
    pygame.display.update()

print('目前的测试关胜利了，感谢测试。你已经拥有了足够过关的聪明。')