#!/usr/bin/env python

from direct.showbase.ShowBase import ShowBase
from panda3d.core import Fog
from panda3d.core import TextNode
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.interval.MetaInterval import Sequence
from direct.interval.LerpInterval import LerpFunc
from direct.interval.FunctionInterval import Func
import sys

TUNNEL_SEGMENT_LENGTH = 50
TUNNEL_TIME = 2  


class FogDemo(ShowBase):

    def genLabelText(self, i, text):
        return OnscreenText(text=text, parent=base.a2dTopLeft, scale=.05,
                            pos=(0.06, -.065 * i), fg=(1, 1, 1, 1),
                            align=TextNode.ALeft)

    def __init__(self):
        ShowBase.__init__(self)

        self.title = OnscreenText(text="Panda3D: Tutorial - Fog", style=1,
            fg=(1, 1, 1, 1), shadow=(0, 0, 0, .5), parent=base.a2dBottomRight,
            align=TextNode.ARight, pos=(-0.1, 0.1), scale=.08)

        self.escapeEventText = self.genLabelText(1, "ESC: Quit")
        self.pkeyEventText = self.genLabelText(2, "[P]: Pause")
        self.tkeyEventText = self.genLabelText(3, "[T]: Toggle Fog")
        self.dkeyEventText = self.genLabelText(4, "[D]: Make fog color black")
        self.sdkeyEventText = self.genLabelText(5, "[SHIFT+D]: Make background color black")
        self.rkeyEventText = self.genLabelText(6, "[R]: Make fog color red")
        self.srkeyEventText = self.genLabelText(7, "[SHIFT+R]: Make background color red")
        self.bkeyEventText = self.genLabelText(8, "[B]: Make fog color blue")
        self.sbkeyEventText = self.genLabelText(9, "[SHIFT+B]: Make background color blue")
        self.gkeyEventText = self.genLabelText(10, "[G]: Make fog color green")
        self.sgkeyEventText = self.genLabelText(11, "[SHIFT+G]: Make background color green")
        self.lkeyEventText = self.genLabelText(12, "[L]: Make fog color light grey")
        self.slkeyEventText = self.genLabelText(13, "[SHIFT+L]: Make background color light grey")
        self.pluskeyEventText = self.genLabelText(14, "[+]: Increase fog density")
        self.minuskeyEventText = self.genLabelText(15, "[-]: Decrease fog density")
        base.disableMouse()
        camera.setPosHpr(0, 0, 10, 0, -90, 0)
        base.setBackgroundColor(0, 0, 0) 
        self.fog = Fog('distanceFog')
        self.fog.setColor(0, 0, 0)
        self.fog.setExpDensity(.08)
        render.setFog(self.fog)
        self.accept('escape', sys.exit)
        self.accept('p', self.handlePause)
        self.accept('t', toggleFog, [render, self.fog])
        self.accept('r', self.fog.setColor, [1, 0, 0])
        self.accept('g', self.fog.setColor, [0, 1, 0])
        self.accept('b', self.fog.setColor, [0, 0, 1])
        self.accept('l', self.fog.setColor, [.7, .7, .7])
        self.accept('d', self.fog.setColor, [0, 0, 0])
        self.accept('shift-r', base.setBackgroundColor, [1, 0, 0])
        self.accept('shift-g', base.setBackgroundColor, [0, 1, 0])
        self.accept('shift-b', base.setBackgroundColor, [0, 0, 1])
        self.accept('shift-l', base.setBackgroundColor, [.7, .7, .7])
        self.accept('shift-d', base.setBackgroundColor, [0, 0, 0])
        self.accept('+', self.addFogDensity, [.01])
        self.accept('=', self.addFogDensity, [.01])
        self.accept('shift-=', self.addFogDensity, [.01])
        self.accept('-', self.addFogDensity, [-.01])
        self.initTunnel()
        self.contTunnel()

    def addFogDensity(self, change):
        self.fog.setExpDensity(
            min(1, max(0, self.fog.getExpDensity() + change)))

    def initTunnel(self):
        self.tunnel = [None] * 4

        for x in range(4):
            self.tunnel[x] = loader.loadModel('models/tunnel')
            if x == 0:
                self.tunnel[x].reparentTo(render)
            else:
                self.tunnel[x].reparentTo(self.tunnel[x - 1])
            self.tunnel[x].setPos(0, 0, -TUNNEL_SEGMENT_LENGTH)
    def contTunnel(self):
        self.tunnel = self.tunnel[1:] + self.tunnel[0:1]
        self.tunnel[0].setZ(0)
        self.tunnel[0].reparentTo(render)
        self.tunnel[0].setScale(.155, .155, .305)
        self.tunnel[3].reparentTo(self.tunnel[2])
        self.tunnel[3].setZ(-TUNNEL_SEGMENT_LENGTH)
        self.tunnel[3].setScale(1)
        self.tunnelMove = Sequence(
            LerpFunc(self.tunnel[0].setZ,
                     duration=TUNNEL_TIME,
                     fromData=0,
                     toData=TUNNEL_SEGMENT_LENGTH * .305),
            Func(self.contTunnel)
        )
        self.tunnelMove.start()
    def handlePause(self):
        toggleInterval(self.tunnelMove)
def toggleInterval(interval):
    if interval.isPlaying():
        interval.pause()
    else:
        interval.resume()

def toggleFog(node, fog):
    if node.getFog() == fog:
        node.clearFog()
    else:
        node.setFog(fog)


demo = FogDemo()
demo.run()
