from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import*
from os import*

app = Ursina()

sky_texture = load_texture("./texture/sky.jpg")

mud_texture = load_texture("./texture/dirt.jpg")
grass_texture = load_texture("./texture/grass.jpg")
stone_texture = load_texture("./texture/stone.jpg")
bedrock_texture = load_texture("./texture/bedrock.jpg")


blockAddList = { 1 : mud_texture , 
                 2 : grass_texture,
                 3 : stone_texture    ,
                 4 : bedrock_texture
               }
nowBlock = 1

def update(self,key):
    if held_keys['1'] : nowBlock = 1
    if held_keys['2'] : nowBlock = 2
    if held_keys['3'] : nowBlock = 3
    if held_keys['4'] : nowBlock = 4

class Block(Entity):
    def __init__(self,position,texture):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture = texture,
            collider = 'box',
            position = position,
            color = color.color(0,0,random.randint(1,180))
        )
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                block = Block(position=(self.position+mouse.normal),texture=blockAddList[nowBlock])
            if key == 'right mouse down':    
                destroy(self)
                
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 10000,
            collider = 'box',
            double_sided = True
        )
sky = Sky()

noise = PerlinNoise(octaves = 3,seed = random.randint(0,100000000))

mud_depth = random.randint(-4,-3)
stone_depth = random.randint(-10,-5) + mud_depth
bedrock_depth = random.randint(-10,-5) + stone_depth

for z in range(20):
    for x in range(20):
        print(z/20*100,"%")
        system("cls")
        block = Block(position=(x,0,z),texture=blockAddList[2])
        for y in range(mud_depth,0):
            block = Block(position=(x,y,z),texture=blockAddList[1])
        for y in range(stone_depth,mud_depth):
            block = Block(position=(x,y,z),texture=blockAddList[3])
        for y in range(bedrock_depth,stone_depth):
            block = Block(position=(x,y,z),texture=blockAddList[4])
        height = floor(noise([x/14,z/14])*8)
        for y in range(1,height+1):
            block = Block(position=(x,y,z),texture=blockAddList[2])
            

player = FirstPersonController()

def update():
    x = player.position[0]
    y = player.position[1]
    z = player.position[2]
    if(y < -120):
        player.position = Vec3(15,5,15)

player.position = Vec3(15,5,14)
player.gravity = 0.3

app.run()