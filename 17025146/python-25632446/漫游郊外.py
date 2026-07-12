#!/usr/bin/env python

from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import Filename, AmbientLight, DirectionalLight
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from panda3d.core import CollideMask
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
import random
import sys
import os
import math

def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1, 1, 1, 1), scale=.05,
                        shadow=(0, 0, 0, 1), parent=base.a2dTopLeft,
                        pos=(0.08, -pos - 0.04), align=TextNode.ALeft)

def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1, 1, 1, 1), scale=.07,
                        parent=base.a2dBottomRight, align=TextNode.ARight,
                        pos=(-0.1, 0.09), shadow=(0, 0, 0, 1))


class RoamingRalphDemo(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.win.setClearColor((0, 0, 0, 1))

        self.keyMap = {
            "left": 0, "right": 0, "forward": 0, "cam-left": 0, "cam-right": 0}

        self.title = addTitle(
            "Panda3D Tutorial: Roaming Ralph (Walking on Uneven Terrain)")
        self.inst1 = addInstructions(0.06, "[ESC]: Quit")
        self.inst2 = addInstructions(0.12, "[Left Arrow]: Rotate Ralph Left")
        self.inst3 = addInstructions(0.18, "[Right Arrow]: Rotate Ralph Right")
        self.inst4 = addInstructions(0.24, "[Up Arrow]: Run Ralph Forward")
        self.inst6 = addInstructions(0.30, "[A]: Rotate Camera Left")
        self.inst7 = addInstructions(0.36, "[S]: Rotate Camera Right")


        self.environ = loader.loadModel("models/world")
        self.environ.reparentTo(render)

        ralphStartPos = self.environ.find("**/start_point").getPos()
        self.ralph = Actor("models/ralph",
                           {"run": "models/ralph-run",
                            "walk": "models/ralph-walk"})
        self.ralph.reparentTo(render)
        self.ralph.setScale(.2)
        self.ralph.setPos(ralphStartPos + (0, 0, 0.5))


        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(self.ralph)
        self.floater.setZ(2.0)

        self.accept("escape", sys.exit)
        self.accept("arrow_left", self.setKey, ["left", True])
        self.accept("arrow_right", self.setKey, ["right", True])
        self.accept("arrow_up", self.setKey, ["forward", True])
        self.accept("a", self.setKey, ["cam-left", True])
        self.accept("s", self.setKey, ["cam-right", True])
        self.accept("arrow_left-up", self.setKey, ["left", False])
        self.accept("arrow_right-up", self.setKey, ["right", False])
        self.accept("arrow_up-up", self.setKey, ["forward", False])
        self.accept("a-up", self.setKey, ["cam-left", False])
        self.accept("s-up", self.setKey, ["cam-right", False])

        taskMgr.add(self.move, "moveTask")
        self.isMoving = False
        self.disableMouse()
        self.camera.setPos(self.ralph.getX(), self.ralph.getY() + 10, 2)
        self.cTrav = CollisionTraverser()

        self.ralphGroundRay = CollisionRay()
        self.ralphGroundRay.setOrigin(0, 0, 9)
        self.ralphGroundRay.setDirection(0, 0, -1)
        self.ralphGroundCol = CollisionNode('ralphRay')
        self.ralphGroundCol.addSolid(self.ralphGroundRay)
        self.ralphGroundCol.setFromCollideMask(CollideMask.bit(0))
        self.ralphGroundCol.setIntoCollideMask(CollideMask.allOff())
        self.ralphGroundColNp = self.ralph.attachNewNode(self.ralphGroundCol)
        self.ralphGroundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.ralphGroundColNp, self.ralphGroundHandler)

        self.camGroundRay = CollisionRay()
        self.camGroundRay.setOrigin(0, 0, 9)
        self.camGroundRay.setDirection(0, 0, -1)
        self.camGroundCol = CollisionNode('camRay')
        self.camGroundCol.addSolid(self.camGroundRay)
        self.camGroundCol.setFromCollideMask(CollideMask.bit(0))
        self.camGroundCol.setIntoCollideMask(CollideMask.allOff())
        self.camGroundColNp = self.camera.attachNewNode(self.camGroundCol)
        self.camGroundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.camGroundColNp, self.camGroundHandler)

        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.3, .3, .3, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection((-5, -5, -5))
        directionalLight.setColor((1, 1, 1, 1))
        directionalLight.setSpecularColor((1, 1, 1, 1))
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))
    def setKey(self, key, value):
        self.keyMap[key] = value
    def move(self, task):
        dt = globalClock.getDt()
        if self.keyMap["cam-left"]:
            self.camera.setX(self.camera, -20 * dt)
        if self.keyMap["cam-right"]:
            self.camera.setX(self.camera, +20 * dt)

        startpos = self.ralph.getPos()

        if self.keyMap["left"]:
            self.ralph.setH(self.ralph.getH() + 300 * dt)
        if self.keyMap["right"]:
            self.ralph.setH(self.ralph.getH() - 300 * dt)
        if self.keyMap["forward"]:
            self.ralph.setY(self.ralph, -25 * dt)

        if self.keyMap["forward"] or self.keyMap["left"] or self.keyMap["right"]:
            if self.isMoving is False:
                self.ralph.loop("run")
                self.isMoving = True
        else:
            if self.isMoving:
                self.ralph.stop()
                self.ralph.pose("walk", 5)
                self.isMoving = False

        camvec = self.ralph.getPos() - self.camera.getPos()
        camvec.setZ(0)
        camdist = camvec.length()
        camvec.normalize()
        if camdist > 10.0:
            self.camera.setPos(self.camera.getPos() + camvec * (camdist - 10))
            camdist = 10.0
        if camdist < 5.0:
            self.camera.setPos(self.camera.getPos() - camvec * (5 - camdist))
            camdist = 5.0


        entries = list(self.ralphGroundHandler.entries)
        entries.sort(key=lambda x: x.getSurfacePoint(render).getZ())

        if len(entries) > 0 and entries[0].getIntoNode().name == "terrain":
            self.ralph.setZ(entries[0].getSurfacePoint(render).getZ())
        else:
            self.ralph.setPos(startpos)


        entries = list(self.camGroundHandler.entries)
        entries.sort(key=lambda x: x.getSurfacePoint(render).getZ())

        if len(entries) > 0 and entries[0].getIntoNode().name == "terrain":
            self.camera.setZ(entries[0].getSurfacePoint(render).getZ() + 1.0)
        if self.camera.getZ() < self.ralph.getZ() + 2.0:
            self.camera.setZ(self.ralph.getZ() + 2.0)
        self.camera.lookAt(self.floater)

        return task.cont


demo = RoamingRalphDemo()
demo.run()
