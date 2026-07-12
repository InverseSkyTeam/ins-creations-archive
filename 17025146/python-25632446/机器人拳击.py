#!/usr/bin/env python

from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import TextNode
from panda3d.core import LVector3
from direct.gui.OnscreenText import OnscreenText
from direct.interval.MetaInterval import Sequence
from direct.interval.FunctionInterval import Func, Wait
from direct.actor import Actor
from random import random
import sys


class BoxingRobotDemo(ShowBase):

    def genLabelText(self, text, i):
        return OnscreenText(text=text, parent=base.a2dTopLeft, scale=.05,
                            pos=(0.1, - 0.1 -.07 * i), fg=(1, 1, 1, 1),
                            align=TextNode.ALeft)

    def __init__(self):
        ShowBase.__init__(self)

        self.title = OnscreenText(text="Panda3D: Tutorial - Actors",
                                  parent=base.a2dBottomRight, style=1,
                                  fg=(0, 0, 0, 1), pos=(-0.2, 0.1),
                                  align=TextNode.ARight, scale=.09)

        self.escapeEventText = self.genLabelText("ESC: Quit", 0)
        self.akeyEventText = self.genLabelText("[A]: Robot 1 Left Punch", 1)
        self.skeyEventText = self.genLabelText("[S]: Robot 1 Right Punch", 2)
        self.kkeyEventText = self.genLabelText("[K]: Robot 2 Left Punch", 3)
        self.lkeyEventText = self.genLabelText("[L]: Robot 2 Right Punch", 4)

        self.disableMouse()
        camera.setPosHpr(14.5, -15.4, 14, 45, -14, 0)
        self.setBackgroundColor(0, 0, 0)

        self.setupLights()

        self.ring = loader.loadModel('models/ring')
        self.ring.reparentTo(render)

        self.robot1 = Actor.Actor('models/robot',
                                  {'leftPunch': 'models/robot_left_punch',
                                   'rightPunch': 'models/robot_right_punch',
                                   'headUp': 'models/robot_head_up',
                                   'headDown': 'models/robot_head_down'})

        self.robot1.setPosHprScale(-1, -2.5, 4, 45, 0, 0, 1.25, 1.25, 1.25)
        self.robot1.reparentTo(render)

        self.robot2 = Actor.Actor('models/robot',
                                  {'leftPunch': 'models/robot_left_punch',
                                   'rightPunch': 'models/robot_right_punch',
                                   'headUp': 'models/robot_head_up',
                                   'headDown': 'models/robot_head_down'})

        self.robot2.setPosHprScale(1, 1.5, 4, 225, 0, 0, 1.25, 1.25, 1.25)
        self.robot2.setColor((.7, 0, 0, 1))
        self.robot2.reparentTo(render)
        self.robot1.punchLeft = Sequence(
            self.robot1.actorInterval('leftPunch', startFrame=1, endFrame=10),
            Func(self.checkPunch, 2),
            self.robot1.actorInterval('leftPunch', startFrame=11, endFrame=32))

        self.robot1.punchRight = Sequence(
            self.robot1.actorInterval('rightPunch', startFrame=1, endFrame=10),
            Func(self.checkPunch, 2),
            self.robot1.actorInterval('rightPunch', startFrame=11, endFrame=32))

        self.robot2.punchLeft = Sequence(
            self.robot2.actorInterval('leftPunch', startFrame=1, endFrame=10),
            Func(self.checkPunch, 1),
            self.robot2.actorInterval('leftPunch', startFrame=11, endFrame=32))

        self.robot2.punchRight = Sequence(
            self.robot2.actorInterval('rightPunch', startFrame=1, endFrame=10),
            Func(self.checkPunch, 1),
            self.robot2.actorInterval('rightPunch', startFrame=11, endFrame=32))

        self.robot1.resetHead = Sequence(
            self.robot1.actorInterval('headUp'),
            Wait(1.5),
            self.robot1.actorInterval('headDown', playRate=.75))

        self.robot2.resetHead = Sequence(
            self.robot2.actorInterval('headUp'),
            Wait(1.5),
            self.robot2.actorInterval('headDown', playRate=.75))

        self.accept('escape', sys.exit)
        self.accept('a', self.tryPunch, [self.robot1.punchLeft])
        self.accept('s', self.tryPunch, [self.robot1.punchRight])
        self.accept('k', self.tryPunch, [self.robot2.punchLeft])
        self.accept('l', self.tryPunch, [self.robot2.punchRight])

    def tryPunch(self, interval):
        if (not self.robot1.resetHead.isPlaying() and
                not self.robot2.resetHead.isPlaying() and
                not interval.isPlaying()):
            interval.start()
    def checkPunch(self, robot):
        if robot == 1:
            if self.robot1.resetHead.isPlaying():
                return
            if (not self.robot1.punchLeft.isPlaying() and
                    not self.robot1.punchRight.isPlaying()):
                if random() > .85:
                    self.robot1.resetHead.start()
            elif random() > .95:
                self.robot1.resetHead.start()
        else:
            if self.robot2.resetHead.isPlaying():
                return
            if (not self.robot2.punchLeft.isPlaying() and
                    not self.robot2.punchRight.isPlaying()):
                if random() > .85:
                    self.robot2.resetHead.start()
            elif random() > .95:
                self.robot2.resetHead.start()

    def setupLights(self):
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.8, .8, .75, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 0, -2.5))
        directionalLight.setColor((0.9, 0.8, 0.9, 1))
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))

demo = BoxingRobotDemo()
demo.run()
