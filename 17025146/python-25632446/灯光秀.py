#!/usr/bin/env python

from direct.showbase.ShowBase import ShowBase
from panda3d.core import PerspectiveLens
from panda3d.core import NodePath
from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import PointLight, Spotlight
from panda3d.core import TextNode
from panda3d.core import Material
from panda3d.core import LVector3
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
import math
import sys
import colorsys
from tkinter import *

def clamp(i, mn=0, mx=1):
    return min(max(i, mn), mx)


class DiscoLightsDemo(ShowBase):
    def makeStatusLabel(self, i):
        return OnscreenText(
            parent=base.a2dTopLeft, align=TextNode.ALeft,
            style=1, fg=(1, 1, 0, 1), shadow=(0, 0, 0, .4),
            pos=(0.06, -0.1 -(.06 * i)), scale=.05, mayChange=True)

    def __init__(self):
        ShowBase.__init__(self)

        self.title = OnscreenText(text="Panda3D: Tutorial - Lighting",
                                  style=1, fg=(1, 1, 0, 1), shadow=(0, 0, 0, 0.5),
                                  pos=(0.87, -0.95), scale = .07)

        self.ambientText = self.makeStatusLabel(0)
        self.directionalText = self.makeStatusLabel(1)
        self.spotlightText = self.makeStatusLabel(2)
        self.pointLightText = self.makeStatusLabel(3)
        self.spinningText = self.makeStatusLabel(4)
        self.ambientBrightnessText = self.makeStatusLabel(5)
        self.directionalBrightnessText = self.makeStatusLabel(6)
        self.spotlightBrightnessText = self.makeStatusLabel(7)
        self.spotlightExponentText = self.makeStatusLabel(8)
        self.lightingPerPixelText = self.makeStatusLabel(9)
        self.lightingShadowsText = self.makeStatusLabel(10)

        self.disco = loader.loadModel("models/disco_hall")
        self.disco.reparentTo(render)
        self.disco.setPosHpr(0, 50, -4, 90, 0, 0)
        self.ambientLight = render.attachNewNode(AmbientLight("ambientLight"))
        self.ambientLight.node().setColor((.1, .1, .1, 1))
        self.directionalLight = render.attachNewNode(
            DirectionalLight("directionalLight"))
        self.directionalLight.node().setColor((.35, .35, .35, 1))
        self.directionalLight.node().setDirection(LVector3(1, 1, -2))
        self.directionalLight.setZ(6)
        dlens = self.directionalLight.node().getLens()
        dlens.setFilmSize(41, 21)
        dlens.setNearFar(50, 75)
        self.spotlight = camera.attachNewNode(Spotlight("spotlight"))
        self.spotlight.node().setColor((.45, .45, .45, 1))
        self.spotlight.node().setSpecularColor((0, 0, 0, 1))
        self.spotlight.node().setLens(PerspectiveLens())
        self.spotlight.node().getLens().setFov(16, 16)
        self.spotlight.node().setAttenuation(LVector3(1, 0.0, 0.0))
        self.spotlight.node().setExponent(60.0)
        self.redHelper = loader.loadModel('models/sphere')
        self.redHelper.setColor((1, 0, 0, 1))
        self.redHelper.setPos(-6.5, -3.75, 0)
        self.redHelper.setScale(.25)
        self.redPointLight = self.redHelper.attachNewNode(
            PointLight("redPointLight"))
        self.redPointLight.node().setColor((.35, 0, 0, 1))
        self.redPointLight.node().setAttenuation(LVector3(.1, 0.04, 0.0))
        self.greenHelper = loader.loadModel('models/sphere')
        self.greenHelper.setColor((0, 1, 0, 1))
        self.greenHelper.setPos(0, 7.5, 0)
        self.greenHelper.setScale(.25)
        self.greenPointLight = self.greenHelper.attachNewNode(
            PointLight("greenPointLight"))
        self.greenPointLight.node().setAttenuation(LVector3(.1, .04, .0))
        self.greenPointLight.node().setColor((0, .35, 0, 1))
        self.blueHelper = loader.loadModel('models/sphere')
        self.blueHelper.setColor((0, 0, 1, 1))
        self.blueHelper.setPos(6.5, -3.75, 0)
        self.blueHelper.setScale(.25)
        self.bluePointLight = self.blueHelper.attachNewNode(
            PointLight("bluePointLight"))
        self.bluePointLight.node().setAttenuation(LVector3(.1, 0.04, 0.0))
        self.bluePointLight.node().setColor((0, 0, .35, 1))
        self.bluePointLight.node().setSpecularColor((1, 1, 1, 1))
        self.pointLightHelper = render.attachNewNode("pointLightHelper")
        self.pointLightHelper.setPos(0, 50, 11)
        self.redHelper.reparentTo(self.pointLightHelper)
        self.greenHelper.reparentTo(self.pointLightHelper)
        self.blueHelper.reparentTo(self.pointLightHelper)
        render.setLight(self.ambientLight)
        render.setLight(self.directionalLight)
        render.setLight(self.spotlight)
        render.setLight(self.redPointLight)
        render.setLight(self.greenPointLight)
        render.setLight(self.bluePointLight)
        self.pointLightsSpin = self.pointLightHelper.hprInterval(
            6, LVector3(360, 0, 0))
        self.pointLightsSpin.loop()
        self.arePointLightsSpinning = True
        self.perPixelEnabled = False
        self.shadowsEnabled = False
        self.accept("escape", sys.exit)
        self.accept("a", self.toggleLights, [[self.ambientLight]])
        self.accept("d", self.toggleLights, [[self.directionalLight]])
        self.accept("s", self.toggleLights, [[self.spotlight]])
        self.accept("p", self.toggleLights, [[self.redPointLight,
                                              self.greenPointLight,
                                              self.bluePointLight]])
        self.accept("r", self.toggleSpinningPointLights)
        self.accept("l", self.togglePerPixelLighting)
        self.accept("e", self.toggleShadows)
        self.accept("z", self.addBrightness, [self.ambientLight, -.05])
        self.accept("x", self.addBrightness, [self.ambientLight, .05])
        self.accept("c", self.addBrightness, [self.directionalLight, -.05])
        self.accept("v", self.addBrightness, [self.directionalLight, .05])
        self.accept("b", self.addBrightness, [self.spotlight, -.05])
        self.accept("n", self.addBrightness, [self.spotlight, .05])
        self.accept("q", self.adjustSpotlightExponent, [self.spotlight, -1])
        self.accept("w", self.adjustSpotlightExponent, [self.spotlight, 1])
        self.updateStatusLabel()
    def toggleLights(self, lights):
        for light in lights:
            if render.hasLight(light):
                render.clearLight(light)
            else:
                render.setLight(light)
        self.updateStatusLabel()
    def toggleSpinningPointLights(self):
        if self.arePointLightsSpinning:
            self.pointLightsSpin.pause()
        else:
            self.pointLightsSpin.resume()
        self.arePointLightsSpinning = not self.arePointLightsSpinning
        self.updateStatusLabel()
    def togglePerPixelLighting(self):
        if self.perPixelEnabled:
            self.perPixelEnabled = False
            render.clearShader()
        else:
            self.perPixelEnabled = True
            render.setShaderAuto()
        self.updateStatusLabel()
    def toggleShadows(self):
        if self.shadowsEnabled:
            self.shadowsEnabled = False
            self.directionalLight.node().setShadowCaster(False)
        else:
            if not self.perPixelEnabled:
                self.togglePerPixelLighting()
            self.shadowsEnabled = True
            self.directionalLight.node().setShadowCaster(True, 512, 512)
        self.updateStatusLabel()
    def adjustSpotlightExponent(self, spotlight, amount):
        e = clamp(spotlight.node().getExponent() + amount, 0, 128)
        spotlight.node().setExponent(e)
        self.updateStatusLabel()
    def addBrightness(self, light, amount):
        color = light.node().getColor()
        h, s, b = colorsys.rgb_to_hsv(color[0], color[1], color[2])
        brightness = clamp(b + amount)
        r, g, b = colorsys.hsv_to_rgb(h, s, brightness)
        light.node().setColor((r, g, b, 1))

        self.updateStatusLabel()
    def updateStatusLabel(self):
        self.updateLabel(self.ambientText, "(a) ambient is",
                         render.hasLight(self.ambientLight))
        self.updateLabel(self.directionalText, "(d) directional is",
                         render.hasLight(self.directionalLight))
        self.updateLabel(self.spotlightText, "(s) spotlight is",
                         render.hasLight(self.spotlight))
        self.updateLabel(self.pointLightText, "(p) point lights are",
                         render.hasLight(self.redPointLight))
        self.updateLabel(self.spinningText, "(r) point light spinning is",
                         self.arePointLightsSpinning)
        self.ambientBrightnessText.setText(
            "(z,x) Ambient Brightness: " +
            self.getBrightnessString(self.ambientLight))
        self.directionalBrightnessText.setText(
            "(c,v) Directional Brightness: " +
            self.getBrightnessString(self.directionalLight))
        self.spotlightBrightnessText.setText(
            "(b,n) Spotlight Brightness: " +
            self.getBrightnessString(self.spotlight))
        self.spotlightExponentText.setText(
            "(q,w) Spotlight Exponent: " +
            str(int(self.spotlight.node().getExponent())))
        self.updateLabel(self.lightingPerPixelText, "(l) Per-pixel lighting is",
                         self.perPixelEnabled)
        self.updateLabel(self.lightingShadowsText, "(e) Shadows are",
                         self.shadowsEnabled)

    def updateLabel(self, obj, base, var):
        if var:
            s = " (on)"
        else:
            s = " (off)"
        obj.setText(base + s)
    def getBrightnessString(self, light):
        color = light.node().getColor()
        h, s, b = colorsys.rgb_to_hsv(color[0], color[1], color[2])
        return "%.2f" % b


demo = DiscoLightsDemo()
demo.run()
