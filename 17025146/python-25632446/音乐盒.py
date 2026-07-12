#!/usr/bin/env python

from direct.showbase.ShowBase import ShowBase
from panda3d.core import NodePath, TextNode
from panda3d.core import PointLight, AmbientLight
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.interval.SoundInterval import SoundInterval
from direct.gui.DirectSlider import DirectSlider
from direct.gui.DirectButton import DirectButton
from direct.interval.MetaInterval import Parallel
from direct.interval.LerpInterval import LerpHprInterval
import sys

base = ShowBase()

class MusicBox(DirectObject):
    def __init__(self):
        self.title = OnscreenText(text="Panda3D: Tutorial - Music Box",
                                  parent=base.a2dBottomCenter,
                                  pos=(0, 0.08), scale=0.08,
                                  fg=(1, 1, 1, 1), shadow=(0, 0, 0, .5))
        self.escapeText = OnscreenText(text="ESC: Quit", parent=base.a2dTopLeft,
                                       fg=(1, 1, 1, 1), pos=(0.06, -0.1),
                                       align=TextNode.ALeft, scale=.05)
        self.accept('escape', sys.exit)

        base.disableMouse()
        self.musicBoxSound = loader.loadMusic('music/musicbox.ogg')
        self.musicBoxSound.setLoopCount(0)
        self.plight = PointLight("light")
        self.plight.setColor((0.7, 0.7, 0.5, 1))
        light_path = base.render.attachNewNode(self.plight)
        light_path.setPos(0, 0, 20)
        base.render.setLight(light_path)

        alight = AmbientLight("ambient")
        alight.setColor((0.3, 0.3, 0.4, 1))
        base.render.setLight(base.render.attachNewNode(alight))

        base.render.setShaderAuto()
        self.musicTime = 0

        self.lidSfx = loader.loadSfx('music/openclose.ogg')
        self.lidOpenSfx = SoundInterval(self.lidSfx, duration=2, startTime=0)
        self.lidCloseSfx = SoundInterval(self.lidSfx, startTime=5)

        self.sliderText = OnscreenText("Volume", pos=(-0.1, 0.87), scale=.07,
                                       fg=(1, 1, 1, 1), shadow=(0, 0, 0, 1))
        self.slider = DirectSlider(pos=(-0.1, 0, .75), scale=0.8, value=.50,
                                   command=self.setMusicBoxVolume)
        self.button = DirectButton(pos=(.9, 0, .75), text="Open",
                                   scale=.1, pad=(.2, .2),
                                   rolloverSound=None, clickSound=None,
                                   command=self.toggleMusicBox)

        self.boxOpen = False

        self.musicBox = loader.loadModel('models/MusicBox')
        self.musicBox.setPos(0, 60, -9)
        self.musicBox.reparentTo(render)
        self.Lid = self.musicBox.find('**/lid')
        self.Panda = self.musicBox.find('**/turningthing')

        self.HingeNode = self.musicBox.find(
            '**/box').attachNewNode('nHingeNode')
        self.HingeNode.setPos(.8659, 6.5, 5.4)
        self.Lid.wrtReparentTo(self.HingeNode)
        self.HingeNode.setHpr(0, 90, 0)

        self.lidClose = Parallel(
            self.lidCloseSfx,
            LerpHprInterval(self.HingeNode, 2.0, (0, 90, 0), blendType='easeInOut'))

        self.lidOpen = Parallel(
            self.lidOpenSfx,
            LerpHprInterval(self.HingeNode, 2.0, (0, 0, 0), blendType='easeInOut'))

        self.PandaTurn = self.Panda.hprInterval(7, (360, 0, 0))
        self.PandaTurn.loop()
        self.PandaTurn.pause()

    def setMusicBoxVolume(self):
        newVol = self.slider.guiItem.getValue()
        self.musicBoxSound.setVolume(newVol)

    def toggleMusicBox(self):

        if self.boxOpen:
            self.lidOpen.pause()

            self.lidClose.start()
            self.PandaTurn.pause() 
            self.musicTime = self.musicBoxSound.getTime()
            self.musicBoxSound.stop()
            self.button['text'] = "Open"
        else:
            self.lidClose.pause()

            self.lidOpen.start()  
            self.PandaTurn.resume()  
            self.musicBoxSound.setTime(self.musicTime)
            self.musicBoxSound.play()
            self.button['text'] = "Close"

        self.button.setText()
        self.boxOpen = not self.boxOpen
mb = MusicBox()
base.run()
