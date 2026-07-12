import random
import math
import time as _time
from minecraft.Entity import Entity
from minecraft.Textures import Textures
from .ZombieModel import ZombieModel
import GL11

class Zombie(Entity):
    zombieModel: ZombieModel = ZombieModel()

    def __init__(self, world, x: float, y: float, z: float):
        super().__init__(world)
        self.rotA: float = (random.random() + 1.0) * 0.01
        self.setPos(x, y, z)
        self.timeOffs: float = random.random() * 1239813.0
        self.rot: float = random.random() * 3.141592653589793 * 2.0
        self.speed: float = 1.0

    def tick(self):
        self.xo = self.x
        self.yo = self.y
        self.zo = self.z
        xa: float = 0.0
        ya: float = 0.0

        if self.y < -100.0:
            self.remove()

        self.rot += self.rotA
        self.rotA = self.rotA * 0.99
        self.rotA = self.rotA + (random.random() - random.random()) * random.random() * random.random() * 0.07999999821186066
        xa: float = math.sin(self.rot)
        ya: float = math.cos(self.rot)

        if self.onGround and random.random() < 0.08:
            self.yd = 0.5

        self.moveRelative(xa, ya, 0.1 if self.onGround else 0.02)

        self.yd = self.yd - 0.08
        self.move(self.xd, self.yd, self.zd)
        self.xd *= 0.91
        self.yd *= 0.98
        self.zd *= 0.91

        if self.onGround:
            self.xd *= 0.7
            self.zd *= 0.7

    def render(self, a: float):
        GL11.glEnable(GL11.GL_TEXTURE_2D)
        GL11.glBindTexture(GL11.GL_TEXTURE_2D, Textures.loadTexture("/char.png", GL11.GL_NEAREST))

        GL11.glPushMatrix()
        time: float = _time.time() * 10.0 * self.speed + self.timeOffs

        size: float = 0.05833333
        yy: float = -abs(math.sin(time * 0.6662)) * 5.0 - 23.0
        GL11.glTranslatef(self.xo + (self.x - self.xo) * a, 
                          self.yo + (self.y - self.yo) * a, 
                          self.zo + (self.z - self.zo) * a)
        GL11.glScalef(1.0, -1.0, 1.0)
        GL11.glScalef(size, size, size)
        GL11.glTranslatef(0.0, yy, 0.0)
        c: float = 57.29578
        GL11.glRotatef(self.rot * c + 180.0, 0.0, 1.0, 0.0)

        self.zombieModel.render(time)
        GL11.glPopMatrix()
        GL11.glDisable(GL11.GL_TEXTURE_2D)
