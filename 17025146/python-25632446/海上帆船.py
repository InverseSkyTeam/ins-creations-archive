#!/usr/bin/env python


from direct.showbase.ShowBase import ShowBase
from panda3d.core import FrameBufferProperties, TextNode, BitMask32, LPoint3
from panda3d.core import WindowProperties, GraphicsOutput, Texture, GraphicsPipe
from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenText import OnscreenText
from sys import exit
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1, 1, 1, 1),
                        pos=(-1.25, pos), align=TextNode.ALeft, scale=.05)
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1, 1, 1, 1), shadow=(0, 0, 0, 1),
                        pos=(1.25, -0.95), align=TextNode.ARight, scale=.07)


class DistortionDemo(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        if not base.win.getGsg().getSupportsBasicShaders():
            t = addTitle("Distortion Demo: Video driver says Cg shaders not supported.")
            return

        self.disableMouse()
        self.setBackgroundColor(0, 0, 0)
        self.title = addTitle("Panda3D: Tutorial - Distortion Effect")
        self.inst1 = addInstructions(0.92, "ESC: Quit")
        self.inst2 = addInstructions(0.86, "Space: Toggle distortion filter On/Off")
        self.inst4 = addInstructions(0.80, "V: View the render-to-texture results")
        self.seascape = loader.loadModel("models/plane")
        self.seascape.reparentTo(render)
        self.seascape.setPosHpr(0, 145, 0, 0, 0, 0)
        self.seascape.setScale(100)
        self.seascape.setTexture(loader.loadTexture("models/ocean.jpg"))
        # scene,
        self.distortionBuffer = self.makeFBO("model buffer")
        self.distortionBuffer.setSort(-3)
        self.distortionBuffer.setClearColor((0, 0, 0, 0))
        distortionCamera = self.makeCamera(self.distortionBuffer, scene=render,
                                           lens=self.cam.node().getLens(), mask=BitMask32.bit(4))
        self.distortionObject = loader.loadModel("models/boat")
        self.distortionObject.setScale(1)
        self.distortionObject.setPos(0, 20, -3)
        self.distortionObject.hprInterval(10, LPoint3(360, 0, 0)).loop()
        self.distortionObject.reparentTo(render)

        distortionShader = loader.loadShader("distortion.sha")
        self.distortionObject.setShader(distortionShader)
        self.distortionObject.hide(BitMask32.bit(4))
        tex1 = loader.loadTexture("models/water.png")
        self.distortionObject.setShaderInput("waves", tex1)

        self.texDistortion = Texture()
        self.distortionBuffer.addRenderTexture(
            self.texDistortion, GraphicsOutput.RTMBindOrCopy, GraphicsOutput.RTPColor)
        self.distortionObject.setShaderInput("screen", self.texDistortion)

        self.accept("v", self.bufferViewer.toggleEnable)
        self.accept("V", self.bufferViewer.toggleEnable)
        self.bufferViewer.setPosition("llcorner")
        self.bufferViewer.setLayout("hline")
        self.bufferViewer.setCardSize(0.652, 0)
        self.accept("space", self.toggleDistortion)
        self.accept("escape", exit, [0])
        self.distortionOn = True

    def makeFBO(self, name):
        winprops = WindowProperties()
        props = FrameBufferProperties()
        props.setRgbColor(1)
        return self.graphicsEngine.makeOutput(
            self.pipe, "model buffer", -2, props, winprops,
            GraphicsPipe.BFSizeTrackHost | GraphicsPipe.BFRefuseWindow,
            self.win.getGsg(), self.win)

    def toggleDistortion(self):
        if self.distortionOn:
            self.distortionObject.hide()
        else:
            self.distortionObject.show()
        self.distortionOn = not(self.distortionOn)

demo = DistortionDemo()
demo.run()
