import random, math, pygame, sys, copy, time
pygame.init()

# random.seed(100)

WIDTH = 1000
HEIGHT = 700
HALFWIDTH = 500
HALFHEIGHT = 350

def get_distance(p1,p2):
    _x1, _y1 = p1
    _x2, _y2 = p2
    return math.sqrt((_x1-_x2)**2+(_y1-_y2)**2)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('至简宇宙OL')

class Life:
    def __init__(self,size,hp,ab,speed):
        self.size = round(size)
        self.tothp = self.hp = round(hp,1)
        self.live_time = 0
        self.to_new_time = 0
        self.new_time = random.randint(100,200)
        self.attack_basic = round(ab)
        self.speed = speed
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
        return (self.get_power() - target.get_power() > 10) and (hunt_distance < hunt_radius)
    
    def act(self,_range):
        self.move()
        self.hunt(_range)
        self.keep(_range)
    def show(self):
        pygame.draw.rect(screen,(min(255,math.floor(self.hp*2.55)),min(255,math.floor(self.hp*2.55)),min(255,math.floor(self.hp*2.55))),self.rect,0)
    
    def move(self):
        if self.locker:
            if abs(self.position[0] - self.locker.position[0]) < HALFWIDTH:
                if self.position[0] < self.locker.position[0]: self.position[0] -= self.speed
                else: self.position[0] += self.speed
            else:
                if self.position[0] < self.locker.position[0]: self.position[0] += self.speed
                else: self.position[0] -= self.speed
            if abs(self.position[1] - self.locker.position[1]) < HALFHEIGHT:
                if self.position[1] < self.locker.position[1]: self.position[1] -= self.speed
                else: self.position[1] += self.speed
            else:
                if self.position[1] < self.locker.position[1]: self.position[1] += self.speed
                else: self.position[1] -= self.speed
            return
        if self.target:
            if abs(self.position[0] - self.target.position[0]) < HALFWIDTH:
                if self.position[0] < self.target.position[0]: self.position[0] += self.speed
                else: self.position[0] -= self.speed
            else:
                if self.position[0] < self.target.position[0]: self.position[0] -= self.speed
                else: self.position[0] += self.speed
            if abs(self.position[1] - self.target.position[1]) < HALFHEIGHT:
                if self.position[1] < self.target.position[1]: self.position[1] += self.speed
                else: self.position[1] -= self.speed
            else:
                if self.position[1] < self.target.position[1]: self.position[1] -= self.speed
                else: self.position[1] += self.speed
            if self.rect.colliderect(self.target.rect):
                print(self.size,self.tothp,self.speed,self.attack_basic)
                if self.hp < self.tothp * 0.1:
                    if self.hp < self.target.hp - 35:
                        if random.randint(0,1):
                            self.hp += 35
                        else:
                            self.hp = 1
                    else:
                        self.hp = self.tothp * random.randint(23,35) / 100 + 1
                elif self.hp < self.tothp * 0.4:
                    self.hp += random.randint(12,17)
                elif self.hp < self.tothp * 0.6:
                    if self.hp > self.target.hp:
                        self.hp += random.randint(7,14)
                    else:
                        self.hp += random.randint(3,6)
                elif self.hp < self.tothp * 0.9:
                    self.hp += random.randint(8,11)
                else:
                    self.hp = self.tothp
                self.target.hp = 0
                self.target = None
            return
        self.position[0] += random.randint(-round(self.speed*100),round(self.speed*100)) / 100
        self.position[1] += random.randint(-round(self.speed*100),round(self.speed*100)) / 100
    
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
    
    def keep(self,new_range):
        self.hp -= .4
        self.live_time += 1
        self.to_new_time += 1
        if self.to_new_time == self.new_time:
            self.new_time = random.randint(140,180)
            self.to_new_time = 0
            if random.randint(0,1):
                self.create_new(new_range)
        if (not self.target) and (self.target is not None):
            self.target = None
        if (not self.locker) and (self.locker is not None):
            self.locker = None
        if self.hp < 0:
            self.hp = 0
        elif self.hp > self.tothp:
            self.hp = self.tothp
        if self.position[0] < 0:
            self.position[0] = WIDTH
        elif self.position[0] > WIDTH:
            self.position[0] = 0
        if self.position[1] < 0:
            self.position[1] = HEIGHT
        elif self.position[1] > HEIGHT:
            self.position[1] = 0
        self.rect.centerx, self.rect.centery = round(self.position[0]), round(self.position[1])
    def create_new(self,new_range):
        new_attr = random.randint(1,10000)
        if new_attr <= 1500:
            new_range.append(Life(self.size,self.tothp,self.attack_basic,self.speed))
        elif new_attr <= 8500:
            new_range.append(Life(
                max(min(self.size + random.randint(-2,2), 60), 3),
                max(min(self.tothp + random.randint(-6,6), 1000), 15),
                max(min(self.attack_basic + random.randint(-2,2), 500), 1),
                self.speed,
            ))
        elif new_attr <= 9500:
            new_range.append(Life(
                max(min(self.size * random.randint(9,16) / 10, 60), 3),
                max(min(self.tothp * random.randint(7,18) / 10, 1000), 15),
                max(min(self.attack_basic * random.randint(5,20) / 10, 500), 1),
                max(min(self.speed * random.randint(9,12) / 10, 10), 0.5),
            ))
        elif new_attr <= 9900:
            new_range.append(Life(
                max(min(self.size + random.randint(-3,3), 60), 3),
                max(min(self.tothp * random.randint(9,19) / 10, 1000), 15),
                max(min(self.attack_basic * random.randint(9,19) / 10, 500), 1),
                max(min(self.speed * random.randint(9,14) / 10, 12), 1),
            ))
        else:
            new_range.append(Life(
                max(min(self.size + random.randint(-3,3), 60), 3),
                max(min(self.tothp * random.randint(12,20) / 10, 1000), 15),
                max(min(self.attack_basic * random.randint(15,25) / 10, 500), 1),
                max(min(self.speed * random.randint(14,18) / 10, 15), 1),
            ))
        self.hp -= 2

l = Life(30,100,1000,3)
lives = [Life(10,100,10,1) for i in range(80)]
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