import random, math, pygame, sys, copy, time
pygame.init()

WIDTH = 1000
HEIGHT = 700

def get_distance(p1,p2):
    _x1, _y1 = p1
    _x2, _y2 = p2
    return math.sqrt((_x1-_x2)**2+(_y1-_y2)**2)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('至简宇宙OL')

class Life:
    def __init__(self):
        self.size = 10
        self.hp = 100
        self.attack_basic = 10
        self.speed = 1
        self.position = [random.randint(0,WIDTH-self.size),random.randint(0,HEIGHT-self.size)]
        self.target = None
        self.locker = None
        self.hunt_limit = 100
        self.rect = pygame.Rect(self.position,(self.size,self.size))
    def __str__(self):
        return f'Life(hp:{self.hp},size:{self.size},{self.position})'
    def __bool__(self):
        return self.hp > 0
    
    def get_power(self):
        return self.hp + self.size + self.speed + self.get_attack() * 5
    def get_attack(self):
        return self.attack_basic + self.hp / 20 + self.size / 5
    def able_to_attack(self,target):
        hunt_distance = get_distance(self.position, target.position)
        hunt_radius = (self.speed - target.speed) * self.hunt_limit * 1.5   # 1.5捕猎信心
        return (self.get_power() - target.get_power() > 20) and (hunt_distance < hunt_radius)
    
    def act(self,hunt_range):
        self.move()
        self.hunt(hunt_range)
        self.keep()
    def show(self):
        pygame.draw.rect(screen,(min(255,math.floor(self.hp*2.55)),min(255,math.floor(self.hp*2.55)),min(255,math.floor(self.hp*2.55))),self.rect,0)
    
    def move(self):
        if self.target:
            if self.position[0] < self.target.position[0]:
                self.position[0] += self.speed
            elif self.position[0] > self.target.position[0]:
                self.position[0] -= self.speed
            if self.position[1] < self.target.position[1]:
                self.position[1] += self.speed
            elif self.position[1] > self.target.position[1]:
                self.position[1] -= self.speed
            if self.rect.colliderect(self.target.rect):
                #TODO 伤害食物
                print('你好')
                self.hp += 15
                self.target.hp = 0
                self.target = None
        else:
            self.position[0] += random.randint(-self.speed,self.speed)
            self.position[1] += random.randint(-self.speed,self.speed)
    
    def hunt(self,hunt_range):
        if self.target:
            return
        for target in hunt_range:
            if self.able_to_attack(target):
                self.target_by(target)
                target.locked_by(self)
    def locked_by(self,locker):
        self.locker = locker
    def target_by(self,target):
        self.target = target
    
    def keep(self):
        self.hp -= .4
        if self.hp < 0:
            self.hp = 0
        if self.position[0] < 0:
            self.position[0] = 0
        elif self.position[0] > WIDTH:
            self.position[0] = WIDTH
        if self.position[1] < 0:
            self.position[1] = 0
        elif self.position[1] > HEIGHT:
            self.position[1] = HEIGHT
        self.rect.center = self.position

l = Life()
l.size = 30
l.rect.w = l.rect.h = 30
l.attack_basic = 1000
l.speed = 3
lives = [Life() for i in range(10)]
lives.append(l)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    
    # model = copy.deepcopy(lives)
    life = -1
    while life < len(lives) - 1:
        life += 1
        if lives[life]:
            # lives[life].act(model)
            lives[life].act(lives)
            lives[life].show()
        else:
            lives.remove(lives[life])
    
    time.sleep(.02)
    pygame.display.update()