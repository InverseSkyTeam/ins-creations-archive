#!/usr/bin/env python

from direct.showbase.ShowBase import ShowBase
from panda3d.core import TextNode, TransparencyAttrib
from panda3d.core import LPoint3, LVector3
from direct.gui.OnscreenText import OnscreenText
from direct.task.Task import Task
from math import sin, cos, pi
from random import randint, choice, random
from direct.interval.MetaInterval import Sequence
from direct.interval.FunctionInterval import Wait, Func
import sys

SPRITE_POS = 55 
SCREEN_X = 20  
SCREEN_Y = 15       
TURN_RATE = 360     
ACCELERATION = 10  
MAX_VEL = 6         
MAX_VEL_SQ = MAX_VEL ** 2  
DEG_TO_RAD = pi / 180  
BULLET_LIFE = 2    
BULLET_REPEAT = .2  
BULLET_SPEED = 10   
AST_INIT_VEL = 1    
AST_INIT_SCALE = 3 
AST_VEL_SCALE = 2.2 
AST_SIZE_SCALE = .6 
AST_MIN_SCALE = 1.1 


def loadObject(tex=None, pos=LPoint3(0, 0), depth=SPRITE_POS, scale=1,
               transparency=True):
    obj = loader.loadModel("models/plane")
    obj.reparentTo(camera)
    obj.setPos(pos.getX(), depth, pos.getY())
    obj.setScale(scale)

    obj.setBin("unsorted", 0)
    obj.setDepthTest(False)

    if transparency:
        obj.setTransparency(TransparencyAttrib.MAlpha)

    if tex:
        tex = loader.loadTexture("textures/" + tex)
        obj.setTexture(tex, 1)

    return obj

def genLabelText(text, i):
    return OnscreenText(text=text, parent=base.a2dTopLeft, pos=(0.07, -.06 * i - 0.1),
                        fg=(1, 1, 1, 1), align=TextNode.ALeft, shadow=(0, 0, 0, 0.5), scale=.05)


class AsteroidsDemo(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.title = OnscreenText(text="Panda3D: Tutorial - Tasks",
                                  parent=base.a2dBottomRight, scale=.07,
                                  align=TextNode.ARight, pos=(-0.1, 0.1),
                                  fg=(1, 1, 1, 1), shadow=(0, 0, 0, 0.5))
        self.escapeText = genLabelText("ESC: Quit", 0)
        self.leftkeyText = genLabelText("[Left Arrow]: Turn Left (CCW)", 1)
        self.rightkeyText = genLabelText("[Right Arrow]: Turn Right (CW)", 2)
        self.upkeyText = genLabelText("[Up Arrow]: Accelerate", 3)
        self.spacekeyText = genLabelText("[Space Bar]: Fire", 4)
        self.disableMouse()
        self.setBackgroundColor((0, 0, 0, 1))
        self.bg = loadObject("stars.jpg", scale=146, depth=200,
                             transparency=False)
        self.ship = loadObject("ship.png")
        self.setVelocity(self.ship, LVector3.zero())

        self.keys = {"turnLeft": 0, "turnRight": 0,
                     "accel": 0, "fire": 0}

        self.accept("escape", sys.exit)
        self.accept("arrow_left",     self.setKey, ["turnLeft", 1])
        self.accept("arrow_left-up",  self.setKey, ["turnLeft", 0])
        self.accept("arrow_right",    self.setKey, ["turnRight", 1])
        self.accept("arrow_right-up", self.setKey, ["turnRight", 0])
        self.accept("arrow_up",       self.setKey, ["accel", 1])
        self.accept("arrow_up-up",    self.setKey, ["accel", 0])
        self.accept("space",          self.setKey, ["fire", 1])

        self.gameTask = taskMgr.add(self.gameLoop, "gameLoop")
        self.nextBullet = 0.0
        self.bullets = []
        self.spawnAsteroids()
    def setKey(self, key, val):
        self.keys[key] = val

    def setVelocity(self, obj, val):
        obj.setPythonTag("velocity", val)

    def getVelocity(self, obj):
        return obj.getPythonTag("velocity")

    def setExpires(self, obj, val):
        obj.setPythonTag("expires", val)

    def getExpires(self, obj):
        return obj.getPythonTag("expires")

    def spawnAsteroids(self):
        self.alive = True
        self.asteroids = []

        for i in range(10):
            asteroid = loadObject("asteroid%d.png" % (randint(1, 3)),
                                  scale=AST_INIT_SCALE)
            self.asteroids.append(asteroid)
            asteroid.setX(choice(tuple(range(-SCREEN_X, -5)) + tuple(range(5, SCREEN_X))))
            asteroid.setZ(choice(tuple(range(-SCREEN_Y, -5)) + tuple(range(5, SCREEN_Y))))
            heading = random() * 2 * pi
            v = LVector3(sin(heading), 0, cos(heading)) * AST_INIT_VEL
            self.setVelocity(self.asteroids[i], v)
    def gameLoop(self, task):
        dt = globalClock.getDt()
        if not self.alive:
            return Task.cont

        self.updateShip(dt)
        if self.keys["fire"] and task.time > self.nextBullet:
            self.fire(task.time)
            self.nextBullet = task.time + BULLET_REPEAT
        self.keys["fire"] = 0
        for obj in self.asteroids:
            self.updatePos(obj, dt)
        newBulletArray = []
        for obj in self.bullets:
            self.updatePos(obj, dt)
            if self.getExpires(obj) > task.time:
                newBulletArray.append(obj)
            else:
                obj.removeNode()
        self.bullets = newBulletArray
        for bullet in self.bullets:
            for i in range(len(self.asteroids) - 1, -1, -1):
                asteroid = self.asteroids[i]
                if ((bullet.getPos() - asteroid.getPos()).lengthSquared() <
                    (((bullet.getScale().getX() + asteroid.getScale().getX())
                      * .5) ** 2)):
                    self.setExpires(bullet, 0)
                    self.asteroidHit(i) 
        shipSize = self.ship.getScale().getX()
        for ast in self.asteroids:
            if ((self.ship.getPos() - ast.getPos()).lengthSquared() <
                    (((shipSize + ast.getScale().getX()) * .5) ** 2)):
                self.alive = False   
                for i in self.asteroids + self.bullets:
                    i.removeNode()
                self.bullets = []        
                self.ship.hide()         
                self.setVelocity(self.ship, LVector3(0, 0, 0))
                Sequence(Wait(2),    
                         Func(self.ship.setR, 0),  
                         Func(self.ship.setX, 0), 
                         Func(self.ship.setZ, 0),
                         Func(self.ship.show),    
                         Func(self.spawnAsteroids)).start() 
                return Task.cont

        if len(self.asteroids) == 0:
            self.spawnAsteroids()

        return Task.cont    

    def updatePos(self, obj, dt):
        vel = self.getVelocity(obj)
        newPos = obj.getPos() + (vel * dt)

        radius = .5 * obj.getScale().getX()
        if newPos.getX() - radius > SCREEN_X:
            newPos.setX(-SCREEN_X)
        elif newPos.getX() + radius < -SCREEN_X:
            newPos.setX(SCREEN_X)
        if newPos.getZ() - radius > SCREEN_Y:
            newPos.setZ(-SCREEN_Y)
        elif newPos.getZ() + radius < -SCREEN_Y:
            newPos.setZ(SCREEN_Y)

        obj.setPos(newPos)

    def asteroidHit(self, index):
        if self.asteroids[index].getScale().getX() <= AST_MIN_SCALE:
            self.asteroids[index].removeNode()
            del self.asteroids[index]
        else:
            asteroid = self.asteroids[index]
            newScale = asteroid.getScale().getX() * AST_SIZE_SCALE
            asteroid.setScale(newScale) 
            vel = self.getVelocity(asteroid)
            speed = vel.length() * AST_VEL_SCALE
            vel.normalize()
            vel = LVector3(0, 1, 0).cross(vel)
            vel *= speed
            self.setVelocity(asteroid, vel)

            newAst = loadObject(scale=newScale)
            self.setVelocity(newAst, vel * -1)
            newAst.setPos(asteroid.getPos())
            newAst.setTexture(asteroid.getTexture(), 1)
            self.asteroids.append(newAst)
    def updateShip(self, dt):
        heading = self.ship.getR() 
        if self.keys["turnRight"]:
            heading += dt * TURN_RATE
            self.ship.setR(heading % 360)
        elif self.keys["turnLeft"]:
            heading -= dt * TURN_RATE
            self.ship.setR(heading % 360)

        if self.keys["accel"]:
            heading_rad = DEG_TO_RAD * heading
            newVel = \
                LVector3(sin(heading_rad), 0, cos(heading_rad)) * ACCELERATION * dt
            newVel += self.getVelocity(self.ship)
            if newVel.lengthSquared() > MAX_VEL_SQ:
                newVel.normalize()
                newVel *= MAX_VEL
            self.setVelocity(self.ship, newVel)

        self.updatePos(self.ship, dt)
    def fire(self, time):
        direction = DEG_TO_RAD * self.ship.getR()
        pos = self.ship.getPos()
        bullet = loadObject("bullet.png", scale=.2)
        bullet.setPos(pos)
        vel = (self.getVelocity(self.ship) +
               (LVector3(sin(direction), 0, cos(direction)) *
                BULLET_SPEED))
        self.setVelocity(bullet, vel)
        self.setExpires(bullet, time + BULLET_LIFE)
        self.bullets.append(bullet)

demo = AsteroidsDemo()
demo.run()
