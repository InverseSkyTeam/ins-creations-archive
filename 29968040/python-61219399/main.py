import zipfile
with zipfile.ZipFile('./engine.zip', 'r') as zip_ref:
    zip_ref.extractall('.')


import math
import time
import pygame
import engine
from engine import config
from engine.events import *
from engine.operators import *
from engine.types import *
from engine.cast import *


@sprite('Stage')
class Stage(Target):
    """Sprite Stage"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self._set_shown(True)
        self.pen = Pen(self)

        self.costume = Costumes(
            self.sprite, 0, 100, "None", [
            {
                'name': "backdrop1",
                'path': "cd21514d0531fdffb22204e0ec5ed84a-svg-2x.png",
                'center': (480, 360),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_CAMERAX = 0
        self.var_CAMERAY = 0
        self.var_CAMERASIZE = 10
        self.var_SELECTED = "none"
        self.var_GRID = "false"
        self.var_LEVEL = 1
        self.var_NEWX1 = 0.8829379021166757
        self.var_NEWX2 = -3.0075485483631192
        self.var_NEWY1 = -5.288250168831743
        self.var_NEWY2 = 1.702037034040047
        self.var_NEWRAD = 8
        self.var_SELECTEDMATERIAL = "road"
        self.var_MOUSEOVERMATERIALS = "False"
        self.var_MOUSEOVERPLAY = "False"
        self.varMODE = "edit"
        self.var_STRESS = "false"
        self.var_MOUSEOVERDELETE = "False"
        self.var_lastmouse = "False"
        self.varcoins = 0
        self.var_bug = 0
        self.var_counter = 2
        self.var_max = 8000
        self.var_ = 0
        self.var_budget = -1000

        self.list_VERTICES = List(
            [-15, -7, -15, -7, "False", 15, -7, 15, -7, "False"]
        )
        self.list_STICKS = List(
            []
        )
        self.list_LEVEL = List(
            [-30, -7, -15, -7, 15, -7, 30, -7, -15, -7, -15, -25, 15, -7, 15, -25]
        )
        self.list_POSSIBLEMATERIALS = List(
            ["road", "log"]
        )
        self.list_PLAYERS = List(
            [-19, 0, -19, 0, 90, 0, 1.5, "#f33434", 0.7]
        )
        self.list_FLAGS = List(
            ["false", 18, -7, "#f33434"]
        )
        self.list_SAVE = List(
            [-15, -7, -15, -7, "False", 15, -7, 15, -7, "False", "∀", -19, 0, -19, 0, 90, 0, 1.5, "#f33434", 0.7]
        )

        self.sprite.layer = 0




@sprite('Manager')
class SpriteManager(Target):
    """Sprite Manager"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self._set_shown(True)
        self.pen = Pen(self)

        self.costume = Costumes(
            self.sprite, 0, 100, "all around", [
            {
                'name': "costume1",
                'path': "3339a2953a3bf62bb80e54ff575dbced-fallback.png",
                'center': (0, 0),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_lastLevel = 1



        self.sprite.layer = 1

    @on_green_flag
    async def green_flag(self, util):
        self.pen.clear_all()
        # util.send_broadcast("end")
        # return
        while not not util.inputs.mouse_down:
            await self.yield_()
        if not (bool(0) or eq(config.USERNAME, "GonSanVi")):
            while not (util.inputs.mouse_down and lt(util.inputs.mouse_y, -100)):
                if lt(util.inputs.mouse_y, -100):
                    util.sprites.stage.var_counter = 1
                else:
                    util.sprites.stage.var_counter = 0
                await util.sprites["TextEngine"].broadcast_turbowarp(util)

                await self.yield_()
            while not not util.inputs.mouse_down:
                await self.yield_()
        util.sprites.stage.var_budget = -1000
        util.sprites.stage.var_counter = 2
        util.sprites.stage.var_GRID = "false"
        util.sprites.stage.var_LEVEL = 1
        util.sprites.stage.var_STRESS = "false"
        await util.sprites["Editor"].broadcast_loadlevel(util)
        while True:
            if eq(util.sprites.stage.varMODE, "edit"):
                await util.sprites["Editor"].broadcast_editor(util)
                await util.sprites["Render Editor"].broadcast_rendereditor(util)
            else:
                await util.sprites["Physics"].broadcast_physics(util)
                await util.sprites["Render Physics"].broadcast_renderphysics(util)
            if eq(util.sprites.stage.var_LEVEL, (self.var_lastLevel + 1)):
                if eq(util.sprites.stage.var_LEVEL, 10):
                    util.send_broadcast("end")
                    return None
                await util.sprites["Editor"].broadcast_loadlevel(util)
            self.var_lastLevel = util.sprites.stage.var_LEVEL

            await self.yield_()


@sprite('Editor')
class SpriteEditor(Target):
    """Sprite Editor"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self._set_shown(True)
        self.pen = Pen(self)

        self.costume = Costumes(
            self.sprite, 0, 100, "all around", [
            {
                'name': "costume1",
                'path': "3339a2953a3bf62bb80e54ff575dbced-fallback.png",
                'center': (0, 0),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_i = 0
        self.var_lowestD = 8
        self.var_lowestID = 3
        self.var_i2 = 26.079901448935882
        self.var_mx = 24
        self.var_my = -18
        self.var_i3 = "3"



        self.sprite.layer = 2

    @on_broadcast('editor')
    async def broadcast_editor(self, util):
        await self.my_editor(util, )

    @warp
    async def my_loadlevel(self, util, arg_x):
        if eq(arg_x, 1):
            util.sprites.stage.list_POSSIBLEMATERIALS.append("log")
            util.sprites.stage.var_max = 8000
            util.sprites.stage.var_CAMERAX = 0
            util.sprites.stage.var_CAMERAY = 0
            util.sprites.stage.var_CAMERASIZE = 10
            await self.my_addvertexat(util, -15, -7, not toBoolean(None))
            await self.my_addvertexat(util, 15, -7, not toBoolean(None))
            await self.my_addlevellinefromto(util, -30, -7, -15, -7)
            await self.my_addlevellinefromto(util, 15, -7, 30, -7)
            await self.my_addlevellinefromto(util, -15, -7, -15, -25)
            await self.my_addlevellinefromto(util, 15, -7, 15, -25)
            await self.my_addplayeratradcolorspeed(util, -19, 0, 1.5, "#f33434", 0.7)
            await self.my_addflagatcolor(util, 18, -7, "#f33434")
        else:
            if eq(arg_x, 2):
                util.sprites.stage.list_POSSIBLEMATERIALS.append("log")
                util.sprites.stage.var_max = 8000
                util.sprites.stage.var_CAMERAX = 0
                util.sprites.stage.var_CAMERAY = 15
                util.sprites.stage.var_CAMERASIZE = 10
                await self.my_addvertexat(util, -15, -7, not toBoolean(None))
                await self.my_addvertexat(util, 15, 0, not toBoolean(None))
                await self.my_addlevellinefromto(util, -30, -7, -15, -7)
                await self.my_addlevellinefromto(util, 15, 0, 30, 0)
                await self.my_addlevellinefromto(util, -15, -7, -15, -25)
                await self.my_addlevellinefromto(util, 15, 0, 15, -25)
                await self.my_addplayeratradcolorspeed(util, -19, 0, 1.5, "#f33434", 0.75)
                await self.my_addflagatcolor(util, 18, 0, "#f33434")
            else:
                if eq(arg_x, 3):
                    util.sprites.stage.list_POSSIBLEMATERIALS.append("log")
                    util.sprites.stage.list_POSSIBLEMATERIALS.append("steel")
                    util.sprites.stage.var_max = 15000
                    util.sprites.stage.var_CAMERAX = 0
                    util.sprites.stage.var_CAMERAY = 0
                    util.sprites.stage.var_CAMERASIZE = 10
                    await self.my_addvertexat(util, -15, -7, not toBoolean(None))
                    await self.my_addvertexat(util, 15, -7, not toBoolean(None))
                    await self.my_addlevellinefromto(util, -30, -7, -15, -7)
                    await self.my_addlevellinefromto(util, 15, -7, 30, -7)
                    await self.my_addlevellinefromto(util, -15, -7, -15, -25)
                    await self.my_addlevellinefromto(util, 15, -7, 15, -25)
                    await self.my_addplayeratradcolorspeed(util, -19, 0, 2.5, "#5be329", 0.5)
                    await self.my_addflagatcolor(util, 18, -7, "#5be329")
                else:
                    if eq(arg_x, 4):
                        util.sprites.stage.list_POSSIBLEMATERIALS.append("log")
                        util.sprites.stage.list_POSSIBLEMATERIALS.append("steel")
                        util.sprites.stage.var_CAMERAX = 0
                        util.sprites.stage.var_CAMERAY = 15
                        util.sprites.stage.var_CAMERASIZE = 10
                        util.sprites.stage.var_max = 11000
                        await self.my_addvertexat(util, -15, 4, not toBoolean(None))
                        await self.my_addvertexat(util, 15, 4, not toBoolean(None))
                        await self.my_addvertexat(util, -15, -7, not toBoolean(None))
                        await self.my_addvertexat(util, 15, -7, not toBoolean(None))
                        await self.my_addlevellinefromto(util, -30, -7, -15, -7)
                        await self.my_addlevellinefromto(util, 15, -7, 30, -7)
                        await self.my_addlevellinefromto(util, -15, -7, -15, -25)
                        await self.my_addlevellinefromto(util, 15, -7, 15, -25)
                        await self.my_addlevellinefromto(util, -30, 4, -15, 4)
                        await self.my_addlevellinefromto(util, 15, 4, 30, 4)
                        await self.my_addplayeratradcolorspeed(util, -19, -3, 1.75, "#f33434", 0.75)
                        await self.my_addplayeratradcolorspeed(util, 19, 8, 1.75, "#c72cf2", -0.75)
                        await self.my_addflagatcolor(util, 18, -7, "#f33434")
                        await self.my_addflagatcolor(util, -18, 4, "#c72cf2")
                    else:
                        if eq(arg_x, 5):
                            util.sprites.stage.list_POSSIBLEMATERIALS.append("log")
                            util.sprites.stage.list_POSSIBLEMATERIALS.append("spring")
                            util.sprites.stage.var_max = 5500
                            util.sprites.stage.var_CAMERAX = 50
                            util.sprites.stage.var_CAMERAY = 0
                            util.sprites.stage.var_CAMERASIZE = 7.5
                            await self.my_addvertexat(util, -13, 3, not toBoolean(None))
                            await self.my_addvertexat(util, 25, -7, not toBoolean(None))
                            await self.my_addvertexat(util, 1, -3, not toBoolean(None))
                            await self.my_addvertexat(util, 10, -3, not toBoolean(None))
                            await self.my_addlevellinefromto(util, -30, 3, -13, 3)
                            await self.my_addlevellinefromto(util, 25, -7, 40, -7)
                            await self.my_addlevellinefromto(util, 25, -7, 25, -25)
                            await self.my_addlevellinefromto(util, 1, -3, 10, -3)
                            await self.my_addlevellinefromto(util, 1, -3, 1, -25)
                            await self.my_addlevellinefromto(util, 10, -3, 10, -25)
                            await self.my_addplayeratradcolorspeed(util, -19, 8, 2.25, "#f5ff1b", 0.1)
                            await self.my_addflagatcolor(util, 34, -7, "#f5ff1b")
                        else:
                            if eq(arg_x, 6):
                                util.sprites.stage.list_POSSIBLEMATERIALS.append("log")
                                util.sprites.stage.list_POSSIBLEMATERIALS.append("steel")
                                util.sprites.stage.var_max = 11000
                                util.sprites.stage.var_CAMERAX = 0
                                util.sprites.stage.var_CAMERAY = -15
                                util.sprites.stage.var_CAMERASIZE = 6
                                await self.my_addvertexat(util, -24, -7, not toBoolean(None))
                                await self.my_addvertexat(util, 24, -7, not toBoolean(None))
                                await self.my_addvertexat(util, 0, -18, not toBoolean(None))
                                await self.my_addlevellinefromto(util, -45, -7, -24, -7)
                                await self.my_addlevellinefromto(util, 24, -7, 45, -7)
                                await self.my_addlevellinefromto(util, -24, -7, -24, -35)
                                await self.my_addlevellinefromto(util, 24, -7, 24, -35)
                                await self.my_addlevellinefromto(util, 0, -18, -10, -35)
                                await self.my_addlevellinefromto(util, 0, -18, 10, -35)
                                await self.my_addplayeratradcolorspeed(util, -30, -3, 2.25, "#f5ff1b", 0.1)
                                await self.my_addflagatcolor(util, 30, -7, "#f5ff1b")
                            else:
                                if eq(arg_x, 7):
                                    util.sprites.stage.list_POSSIBLEMATERIALS.append("log")
                                    util.sprites.stage.list_POSSIBLEMATERIALS.append("steel")
                                    util.sprites.stage.var_max = 10000
                                    util.sprites.stage.var_CAMERAX = 0
                                    util.sprites.stage.var_CAMERAY = -15
                                    util.sprites.stage.var_CAMERASIZE = 6
                                    await self.my_addvertexat(util, -24, -7, not toBoolean(None))
                                    await self.my_addvertexat(util, 24, -7, not toBoolean(None))
                                    await self.my_addvertexat(util, -24, -14, not toBoolean(None))
                                    await self.my_addvertexat(util, 24, -14, not toBoolean(None))
                                    await self.my_addlevellinefromto(util, -45, -7, -24, -7)
                                    await self.my_addlevellinefromto(util, 24, -7, 45, -7)
                                    await self.my_addlevellinefromto(util, -24, -7, -24, -35)
                                    await self.my_addlevellinefromto(util, 24, -7, 24, -35)
                                    await self.my_addplayeratradcolorspeed(util, -30, -3, 1.75, "#f33434", 0.75)
                                    await self.my_addflagatcolor(util, 30, -7, "#f33434")
                                else:
                                    if eq(arg_x, 8):
                                        util.sprites.stage.list_POSSIBLEMATERIALS.append("log")
                                        util.sprites.stage.list_POSSIBLEMATERIALS.append("steel")
                                        util.sprites.stage.var_max = 10000
                                        util.sprites.stage.var_CAMERAX = 0
                                        util.sprites.stage.var_CAMERAY = -15
                                        util.sprites.stage.var_CAMERASIZE = 6
                                        await self.my_addvertexat(util, -24, -7, not toBoolean(None))
                                        await self.my_addvertexat(util, 24, -7, not toBoolean(None))
                                        await self.my_addvertexat(util, 0, 10, not toBoolean(None))
                                        await self.my_addlevellinefromto(util, -45, -7, -24, -7)
                                        await self.my_addlevellinefromto(util, 24, -7, 45, -7)
                                        await self.my_addlevellinefromto(util, -24, -7, -24, -35)
                                        await self.my_addlevellinefromto(util, 24, -7, 24, -35)
                                        await self.my_addlevellinefromto(util, 0, 10, -10, 35)
                                        await self.my_addlevellinefromto(util, 0, 10, 10, 35)
                                        await self.my_addplayeratradcolorspeed(util, -30, -3, 2.25, "#f5ff1b", 0.2)
                                        await self.my_addflagatcolor(util, 30, -7, "#f5ff1b")
                                    else:
                                        if eq(arg_x, 9):
                                            util.sprites.stage.list_POSSIBLEMATERIALS.append("log")
                                            util.sprites.stage.list_POSSIBLEMATERIALS.append("steel")
                                            util.sprites.stage.list_POSSIBLEMATERIALS.append("spring")
                                            util.sprites.stage.var_max = 8000
                                            util.sprites.stage.var_CAMERAX = -30
                                            util.sprites.stage.var_CAMERAY = -20
                                            util.sprites.stage.var_CAMERASIZE = 6
                                            await self.my_addvertexat(util, -26, -7, not toBoolean(None))
                                            await self.my_addvertexat(util, -26, -15, not toBoolean(None))
                                            await self.my_addlevellinefromto(util, -60, 15, -26, -7)
                                            await self.my_addlevellinefromto(util, 15, -18, 45, -18)
                                            await self.my_addlevellinefromto(util, -26, -7, -26, -35)
                                            await self.my_addlevellinefromto(util, 15, -18, 15, -35)
                                            await self.my_addplayeratradcolorspeed(util, -42, 8, 1.5, "#f33434", 0.75)
                                            await self.my_addflagatcolor(util, 22, -18, "#f33434")
                                        else:
                                            pass

    @on_broadcast('load level')
    async def broadcast_loadlevel(self, util):
        util.sprites.stage.list_LEVEL.delete_all()
        util.sprites.stage.list_FLAGS.delete_all()
        util.sprites.stage.list_STICKS.delete_all()
        util.sprites.stage.list_PLAYERS.delete_all()
        util.sprites.stage.list_VERTICES.delete_all()
        util.sprites.stage.list_POSSIBLEMATERIALS.delete_all()
        util.sprites.stage.list_POSSIBLEMATERIALS.append("road")
        await self.my_loadlevel(util, util.sprites.stage.var_LEVEL)
        await self.my_save(util, )
        util.sprites.stage.varMODE = "edit"
        util.sprites.stage.var_SELECTED = "none"
        util.sprites.stage.var_SELECTEDMATERIAL = "road"

    @warp
    async def my_addvertexat(self, util, arg_x, arg_y, arg_fixed):
        util.sprites.stage.list_VERTICES.append(arg_x)
        util.sprites.stage.list_VERTICES.append(arg_y)
        util.sprites.stage.list_VERTICES.append(arg_x)
        util.sprites.stage.list_VERTICES.append(arg_y)
        util.sprites.stage.list_VERTICES.append(not arg_fixed)

    @warp
    async def my_addlevellinefromto(self, util, arg_x, arg_y, arg_x2, arg_y2):
        util.sprites.stage.list_LEVEL.append(arg_x)
        util.sprites.stage.list_LEVEL.append(arg_y)
        util.sprites.stage.list_LEVEL.append(arg_x2)
        util.sprites.stage.list_LEVEL.append(arg_y2)

    @warp
    async def my_editor(self, util, ):
        util.sprites.stage.var_MOUSEOVERDELETE = str((lt(util.inputs.mouse_x, -121) and gt(util.inputs.mouse_y, 123))).lower()
        util.sprites.stage.var_MOUSEOVERMATERIALS = str((lt(util.inputs.mouse_x, (-253 + (len(util.sprites.stage.list_POSSIBLEMATERIALS) * 60))) and lt(util.inputs.mouse_y, -122))).lower()
        util.sprites.stage.var_MOUSEOVERPLAY = str((gt(util.inputs.mouse_x, 123) and gt(util.inputs.mouse_y, 123))).lower()
        if (eq(util.sprites.stage.var_MOUSEOVERMATERIALS, "false") and (eq(util.sprites.stage.var_MOUSEOVERPLAY, "false") and eq(util.sprites.stage.var_MOUSEOVERDELETE, "false"))):
            self.var_mx = div((util.inputs.mouse_x + util.sprites.stage.var_CAMERAX), util.sprites.stage.var_CAMERASIZE)
            self.var_my = div((util.inputs.mouse_y + util.sprites.stage.var_CAMERAY), util.sprites.stage.var_CAMERASIZE)
            if eq(util.sprites.stage.var_SELECTED, "none"):
                if (util.inputs.mouse_down and not eq(util.sprites.stage.var_lastmouse, "true")):
                    self.var_lowestD = 99999999999
                    self.var_lowestID = 0
                    self.var_i = 0
                    for _ in create_repeat(div(len(util.sprites.stage.list_VERTICES), 5)):
                        self.var_i += 5
                        self.var_i2 = sqrt((((self.var_mx - toNumber(util.sprites.stage.list_VERTICES[(self.var_i - 4)])) * (self.var_mx - toNumber(util.sprites.stage.list_VERTICES[(self.var_i - 4)]))) + ((self.var_my - toNumber(util.sprites.stage.list_VERTICES[(self.var_i - 3)])) * (self.var_my - toNumber(util.sprites.stage.list_VERTICES[(self.var_i - 3)])))))
                        if lt(self.var_i2, self.var_lowestD):
                            self.var_lowestD = self.var_i2
                            self.var_lowestID = div(self.var_i, 5)
                    if lt(self.var_lowestD, 0.7):
                        util.sprites.stage.var_SELECTED = NumberToString(self.var_lowestID)
                    else:
                        if eq(util.sprites.stage.var_GRID, "true"):
                            await self.my_addvertexat(util, _round(self.var_mx), _round(self.var_my), toBoolean(None))
                        else:
                            await self.my_addvertexat(util, self.var_mx, self.var_my, toBoolean(None))
                        util.sprites.stage.var_SELECTED = NumberToString(div(len(util.sprites.stage.list_VERTICES), 5))
                    util.sprites.stage.var_NEWX1 = util.sprites.stage.list_VERTICES[((ScratchStringToNumber(util.sprites.stage.var_SELECTED) * 5) - 4)]
                    util.sprites.stage.var_NEWY1 = util.sprites.stage.list_VERTICES[((ScratchStringToNumber(util.sprites.stage.var_SELECTED) * 5) - 3)]
                    util.sprites.stage.var_NEWX2 = util.sprites.stage.list_VERTICES[((ScratchStringToNumber(util.sprites.stage.var_SELECTED) * 5) - 4)]
                    util.sprites.stage.var_NEWY2 = util.sprites.stage.list_VERTICES[((ScratchStringToNumber(util.sprites.stage.var_SELECTED) * 5) - 3)]
            else:
                util.sprites.stage.var_NEWX1 = util.sprites.stage.list_VERTICES[((ScratchStringToNumber(util.sprites.stage.var_SELECTED) * 5) - 4)]
                util.sprites.stage.var_NEWY1 = util.sprites.stage.list_VERTICES[((ScratchStringToNumber(util.sprites.stage.var_SELECTED) * 5) - 3)]
                util.sprites.stage.var_NEWX2 = self.var_mx
                util.sprites.stage.var_NEWY2 = self.var_my
                if eq(util.sprites.stage.var_GRID, "true"):
                    util.sprites.stage.var_NEWX2 = _round(toNumber(util.sprites.stage.var_NEWX2))
                    util.sprites.stage.var_NEWY2 = _round(toNumber(util.sprites.stage.var_NEWY2))
                if eq(util.sprites.stage.var_SELECTEDMATERIAL, "road"):
                    util.sprites.stage.var_NEWRAD = 8
                else:
                    if eq(util.sprites.stage.var_SELECTEDMATERIAL, "log"):
                        util.sprites.stage.var_NEWRAD = 8
                    else:
                        if eq(util.sprites.stage.var_SELECTEDMATERIAL, "steel"):
                            util.sprites.stage.var_NEWRAD = 16
                        else:
                            if eq(util.sprites.stage.var_SELECTEDMATERIAL, "spring"):
                                util.sprites.stage.var_NEWRAD = 12
                            else:
                                pass
                self.var_i2 = sqrt((((toNumber(util.sprites.stage.var_NEWX1) - toNumber(util.sprites.stage.var_NEWX2)) * (toNumber(util.sprites.stage.var_NEWX1) - toNumber(util.sprites.stage.var_NEWX2))) + ((toNumber(util.sprites.stage.var_NEWY1) - toNumber(util.sprites.stage.var_NEWY2)) * (toNumber(util.sprites.stage.var_NEWY1) - toNumber(util.sprites.stage.var_NEWY2)))))
                if gt(self.var_i2, util.sprites.stage.var_NEWRAD):
                    util.sprites.stage.var_NEWX2 = (toNumber(util.sprites.stage.var_NEWX1) + div(((toNumber(util.sprites.stage.var_NEWX2) - toNumber(util.sprites.stage.var_NEWX1)) * util.sprites.stage.var_NEWRAD), self.var_i2))
                    util.sprites.stage.var_NEWY2 = (toNumber(util.sprites.stage.var_NEWY1) + div(((toNumber(util.sprites.stage.var_NEWY2) - toNumber(util.sprites.stage.var_NEWY1)) * util.sprites.stage.var_NEWRAD), self.var_i2))
                    if eq(util.sprites.stage.var_GRID, "true"):
                        if gt(util.sprites.stage.var_NEWX2, util.sprites.stage.var_NEWX1):
                            util.sprites.stage.var_NEWX2 = floor(toNumber(util.sprites.stage.var_NEWX2))
                        else:
                            util.sprites.stage.var_NEWX2 = ceil(toNumber(util.sprites.stage.var_NEWX2))
                        if gt(util.sprites.stage.var_NEWY2, util.sprites.stage.var_NEWY1):
                            util.sprites.stage.var_NEWY2 = floor(toNumber(util.sprites.stage.var_NEWY2))
                        else:
                            util.sprites.stage.var_NEWY2 = ceil(toNumber(util.sprites.stage.var_NEWY2))
                if ((util.inputs.mouse_down and not eq(util.sprites.stage.var_lastmouse, "true")) and not (eq(util.sprites.stage.var_NEWX1, util.sprites.stage.var_NEWX2) and eq(util.sprites.stage.var_NEWY1, util.sprites.stage.var_NEWY2))):
                    self.var_i3 = util.sprites.stage.var_SELECTED
                    self.var_lowestD = 9999999
                    self.var_i = 0
                    for _ in create_repeat(div(len(util.sprites.stage.list_VERTICES), 5)):
                        self.var_i += 5
                        self.var_i2 = sqrt((((toNumber(util.sprites.stage.var_NEWX2) - toNumber(util.sprites.stage.list_VERTICES[(self.var_i - 4)])) * (toNumber(util.sprites.stage.var_NEWX2) - toNumber(util.sprites.stage.list_VERTICES[(self.var_i - 4)]))) + ((toNumber(util.sprites.stage.var_NEWY2) - toNumber(util.sprites.stage.list_VERTICES[(self.var_i - 3)])) * (toNumber(util.sprites.stage.var_NEWY2) - toNumber(util.sprites.stage.list_VERTICES[(self.var_i - 3)])))))
                        if lt(self.var_i2, self.var_lowestD):
                            self.var_lowestD = self.var_i2
                            self.var_lowestID = div(self.var_i, 5)
                    if lt(self.var_lowestD, 0.7):
                        util.sprites.stage.var_SELECTED = NumberToString(self.var_lowestID)
                    else:
                        await self.my_addvertexat(util, util.sprites.stage.var_NEWX2, util.sprites.stage.var_NEWY2, toBoolean(None))
                        util.sprites.stage.var_SELECTED = NumberToString(div(len(util.sprites.stage.list_VERTICES), 5))
                    await self.my_addstickmodedist(util, self.var_i3, util.sprites.stage.var_SELECTED, util.sprites.stage.var_SELECTEDMATERIAL, sqrt((((toNumber(util.sprites.stage.var_NEWX2) - toNumber(util.sprites.stage.var_NEWX1)) * (toNumber(util.sprites.stage.var_NEWX2) - toNumber(util.sprites.stage.var_NEWX1))) + ((toNumber(util.sprites.stage.var_NEWY2) - toNumber(util.sprites.stage.var_NEWY1)) * (toNumber(util.sprites.stage.var_NEWY2) - toNumber(util.sprites.stage.var_NEWY1))))))
        else:
            if (util.inputs.mouse_down and not eq(util.sprites.stage.var_lastmouse, "true")):
                if eq(util.sprites.stage.var_MOUSEOVERMATERIALS, "true"):
                    util.sprites.stage.var_SELECTED = "none"
                    util.sprites.stage.var_SELECTEDMATERIAL = util.sprites.stage.list_POSSIBLEMATERIALS[_round(div((285 + util.inputs.mouse_x), 65))]
                    if eq(util.sprites.stage.var_SELECTEDMATERIAL, ""):
                        util.sprites.stage.var_SELECTEDMATERIAL = "road"
                else:
                    if eq(util.sprites.stage.var_MOUSEOVERDELETE, "true"):
                        if lt(util.inputs.mouse_x, -190):
                            await self.my_deleteall(util, )
                        else:
                            await self.my_deleteselected(util, )
                    else:
                        if gt(util.inputs.mouse_x, 190):
                            await self.my_save(util, )
                            util.sprites.stage.varMODE = "physics"
                        else:
                            util.sprites.stage.var_GRID = str(eq(util.sprites.stage.var_GRID, "false")).lower()
        await self.my_calculatebudget(util, )
        util.sprites.stage.var_lastmouse = str(util.inputs.mouse_down).lower()

    @warp
    async def my_addstickmodedist(self, util, arg_1, arg_2, arg_m, arg_d):
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_STICKS), 5)):
            self.var_i += 5
            if ((eq(util.sprites.stage.list_STICKS[(self.var_i - 3)], arg_1) and eq(util.sprites.stage.list_STICKS[(self.var_i - 2)], arg_2)) or (eq(util.sprites.stage.list_STICKS[(self.var_i - 2)], arg_1) and eq(util.sprites.stage.list_STICKS[(self.var_i - 3)], arg_2))):
                self.var_i += -5
                for _ in create_repeat(5):
                    util.sprites.stage.list_STICKS.delete((self.var_i + 1))
        util.sprites.stage.list_STICKS.append("")
        util.sprites.stage.list_STICKS.append(arg_1)
        util.sprites.stage.list_STICKS.append(arg_2)
        util.sprites.stage.list_STICKS.append(arg_d)
        util.sprites.stage.list_STICKS.append(arg_m)

    @warp
    async def my_addplayeratradcolorspeed(self, util, arg_x, arg_y, arg_r, arg_c, arg_s):
        util.sprites.stage.list_PLAYERS.append(arg_x)
        util.sprites.stage.list_PLAYERS.append(arg_y)
        util.sprites.stage.list_PLAYERS.append(arg_x)
        util.sprites.stage.list_PLAYERS.append(arg_y)
        util.sprites.stage.list_PLAYERS.append(90)
        util.sprites.stage.list_PLAYERS.append(0)
        util.sprites.stage.list_PLAYERS.append(arg_r)
        util.sprites.stage.list_PLAYERS.append(arg_c)
        util.sprites.stage.list_PLAYERS.append(arg_s)

    @warp
    async def my_addflagatcolor(self, util, arg_x, arg_y, arg_c):
        util.sprites.stage.list_FLAGS.append("false")
        util.sprites.stage.list_FLAGS.append(arg_x)
        util.sprites.stage.list_FLAGS.append(arg_y)
        util.sprites.stage.list_FLAGS.append(arg_c)

    @warp
    async def my_save(self, util, ):
        util.sprites.stage.list_SAVE.delete_all()
        self.var_i = 0
        for _ in create_repeat(len(util.sprites.stage.list_VERTICES)):
            self.var_i += 1
            util.sprites.stage.list_SAVE.append(util.sprites.stage.list_VERTICES[self.var_i])
        util.sprites.stage.list_SAVE.append("∀")
        self.var_i = 0
        for _ in create_repeat(len(util.sprites.stage.list_PLAYERS)):
            self.var_i += 1
            util.sprites.stage.list_SAVE.append(util.sprites.stage.list_PLAYERS[self.var_i])

    @warp
    async def my_deleteall(self, util, ):
        util.sprites.stage.list_STICKS.delete_all()
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_VERTICES), 5)):
            self.var_i += 5
            if toBoolean(util.sprites.stage.list_VERTICES[self.var_i]):
                self.var_i += -5
                for _ in create_repeat(5):
                    util.sprites.stage.list_VERTICES.delete((self.var_i + 1))
        util.sprites.stage.var_SELECTED = "none"

    @warp
    async def my_deleteselected(self, util, ):
        if toBoolean(util.sprites.stage.list_VERTICES[(ScratchStringToNumber(util.sprites.stage.var_SELECTED) * 5)]):
            for _ in create_repeat(5):
                util.sprites.stage.list_VERTICES.delete(((ScratchStringToNumber(util.sprites.stage.var_SELECTED) * 5) + -4))
            self.var_i = 0
            for _ in create_repeat(div(len(util.sprites.stage.list_STICKS), 5)):
                self.var_i += 5
                if (eq(util.sprites.stage.list_STICKS[(self.var_i - 3)], util.sprites.stage.var_SELECTED) or eq(util.sprites.stage.list_STICKS[(self.var_i - 2)], util.sprites.stage.var_SELECTED)):
                    self.var_i += -5
                    for _ in create_repeat(5):
                        util.sprites.stage.list_STICKS.delete((self.var_i + 1))
                else:
                    if gt(util.sprites.stage.list_STICKS[(self.var_i - 3)], util.sprites.stage.var_SELECTED):
                        util.sprites.stage.list_STICKS[(self.var_i - 3)] = (toNumber(util.sprites.stage.list_STICKS[(self.var_i - 3)]) - 1)
                    if gt(util.sprites.stage.list_STICKS[(self.var_i - 2)], util.sprites.stage.var_SELECTED):
                        util.sprites.stage.list_STICKS[(self.var_i - 2)] = (toNumber(util.sprites.stage.list_STICKS[(self.var_i - 2)]) - 1)
        util.sprites.stage.var_SELECTED = "none"

    @warp
    async def my_calculatebudget(self, util, ):
        self.var_i = 0
        util.sprites.stage.var_ = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_STICKS), 5)):
            self.var_i += 5
            if eq(util.sprites.stage.list_STICKS[self.var_i], "road"):
                util.sprites.stage.var_ += _round((toNumber(util.sprites.stage.list_STICKS[(self.var_i - 1)]) * 50))
            else:
                if eq(util.sprites.stage.list_STICKS[self.var_i], "log"):
                    util.sprites.stage.var_ += _round((toNumber(util.sprites.stage.list_STICKS[(self.var_i - 1)]) * 45))
                else:
                    if eq(util.sprites.stage.list_STICKS[self.var_i], "steel"):
                        util.sprites.stage.var_ += _round((toNumber(util.sprites.stage.list_STICKS[(self.var_i - 1)]) * 112.5))
                    else:
                        pass


@sprite('Render Editor')
class SpriteRenderEditor(Target):
    """Sprite Render Editor"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -167
        self._ypos = 142
        self._direction = 30
        self._set_shown(False)
        self.pen = Pen(self)

        self.costume = Costumes(
            self.sprite, 0, 100, "don't rotate", [
            {
                'name': "costume1",
                'path': "32649153fd0540a67bf66a33a0858b94.png",
                'center': (480, 360),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_i = 2
        self.var_i2 = 1.5



        self.sprite.layer = 3

    @on_broadcast('render editor')
    async def broadcast_rendereditor(self, util):
        await self.my_render(util, )
        await util.sprites["TextEngine"].broadcast_rendereditortext(util)

    @warp
    async def my_render(self, util, ):
        self.pen.clear_all()
        self.gotoxy(0, 0)
        self.pen.exact_color("#989bc5")
        self.pen.set_size(999)
        self.pen.down()
        self.pen.up()
        if eq(util.sprites.stage.var_GRID, "true"):
            self.pen.exact_color("#818181")
            self.pen.set_size((0.05 * util.sprites.stage.var_CAMERASIZE))
            await self.my_rendergridatsize(util, util.sprites.stage.var_CAMERAX, util.sprites.stage.var_CAMERAY, util.sprites.stage.var_CAMERASIZE)
        await self.my_renderplayers(util, )
        await self.my_flags(util, )
        await self.my_renderlevel(util, )
        self.pen.set_size((0.65 * util.sprites.stage.var_CAMERASIZE))
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_STICKS), 5)):
            self.var_i += 5
            self.var_i2 = (toNumber(util.sprites.stage.list_STICKS[(self.var_i - 3)]) * 5)
            await self.my_setcolorto(util, util.sprites.stage.list_STICKS[self.var_i])
            self.pen.up()
            await self.my_goto(util, util.sprites.stage.list_VERTICES[(toNumber(self.var_i2) - 4)], util.sprites.stage.list_VERTICES[(toNumber(self.var_i2) - 3)])
            self.pen.down()
            self.var_i2 = (toNumber(util.sprites.stage.list_STICKS[(self.var_i - 2)]) * 5)
            await self.my_goto(util, util.sprites.stage.list_VERTICES[(toNumber(self.var_i2) - 4)], util.sprites.stage.list_VERTICES[(toNumber(self.var_i2) - 3)])
            self.pen.up()
        if not eq(util.sprites.stage.var_SELECTED, "none"):
            self.pen.exact_color("#5a5a5a")
            self.pen.set_color("transparency", 35)
            self.pen.up()
            await self.my_goto(util, util.sprites.stage.var_NEWX1, util.sprites.stage.var_NEWY1)
            self.pen.down()
            await self.my_goto(util, util.sprites.stage.var_NEWX2, util.sprites.stage.var_NEWY2)
            self.pen.up()
            self.var_i = (25 * util.timer())
            for _ in create_repeat((util.sprites.stage.var_NEWRAD * 3)):
                self.var_i += div(120, util.sprites.stage.var_NEWRAD)
                await self.my_goto(util, (toNumber(util.sprites.stage.var_NEWX1) + (util.sprites.stage.var_NEWRAD * math.sin(math.radians(self.var_i)))), (toNumber(util.sprites.stage.var_NEWY1) + (util.sprites.stage.var_NEWRAD * math.cos(math.radians(self.var_i)))))
                self.pen.down()
                self.pen.up()
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_VERTICES), 5)):
            self.var_i += 5
            await self.my_goto(util, util.sprites.stage.list_VERTICES[(self.var_i - 4)], util.sprites.stage.list_VERTICES[(self.var_i - 3)])
            if eq(util.sprites.stage.var_SELECTED, div(self.var_i, 5)):
                self.pen.exact_color("#f7f7f7")
                self.pen.set_size((2 * util.sprites.stage.var_CAMERASIZE))
                self.pen.down()
                self.pen.up()
                self.pen.set_size((1.35 * util.sprites.stage.var_CAMERASIZE))
            else:
                self.pen.set_size((1.25 * util.sprites.stage.var_CAMERASIZE))
            if toBoolean(util.sprites.stage.list_VERTICES[self.var_i]):
                self.pen.exact_color("#f7e30c")
            else:
                self.pen.exact_color("#db0a0a")
            self.pen.down()
            self.pen.up()
        await self.my_renderui(util, )

    @warp
    async def my_rendergridatsize(self, util, arg_x, arg_y, arg_s):
        self.pen.up()
        self.var_i = (-240 - mod(arg_x, arg_s))
        for _ in create_repeat((div(480, arg_s) + 1)):
            self.pen.up()
            self.xpos = self.var_i
            self.ypos = 200
            self.pen.down()
            self.ypos = -200
            self.var_i += arg_s
        self.var_i = (-180 - mod(arg_y, arg_s))
        for _ in create_repeat((div(360, arg_s) + 1)):
            self.pen.up()
            self.ypos = self.var_i
            self.xpos = -300
            self.pen.down()
            self.xpos = 300
            self.var_i += arg_s
        self.pen.up()

    @warp
    async def my_renderlevel(self, util, ):
        self.pen.set_size((0.75 * util.sprites.stage.var_CAMERASIZE))
        self.pen.exact_color("#3a4054")
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_LEVEL), 4)):
            self.var_i += 4
            self.pen.up()
            await self.my_goto(util, util.sprites.stage.list_LEVEL[(self.var_i - 3)], util.sprites.stage.list_LEVEL[(self.var_i - 2)])
            self.pen.down()
            await self.my_goto(util, util.sprites.stage.list_LEVEL[(self.var_i - 1)], util.sprites.stage.list_LEVEL[self.var_i])
        self.pen.up()

    @warp
    async def my_goto(self, util, arg_x, arg_y):
        self.gotoxy(((toNumber(arg_x) * util.sprites.stage.var_CAMERASIZE) - util.sprites.stage.var_CAMERAX), ((toNumber(arg_y) * util.sprites.stage.var_CAMERASIZE) - util.sprites.stage.var_CAMERAY))

    @warp
    async def my_renderplayers(self, util, ):
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_PLAYERS), 9)):
            self.var_i += 9
            self.var_i2 = util.sprites.stage.list_PLAYERS[(self.var_i - 2)]
            await self.my_goto(util, util.sprites.stage.list_PLAYERS[(self.var_i - 8)], util.sprites.stage.list_PLAYERS[(self.var_i - 7)])
            self.pen.exact_color(util.sprites.stage.list_PLAYERS[(self.var_i - 1)])
            self.pen.set_size((2 * (util.sprites.stage.var_CAMERASIZE * toNumber(self.var_i2))))
            self.pen.down()
            self.pen.up()
            self.pen.set_size((util.sprites.stage.var_CAMERASIZE * 0.65))
            self.pen.change_color("brightness", -20)
            self.pen.down()
            await self.my_goto(util, (toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 8)]) + (toNumber(self.var_i2) * math.sin(math.radians(toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 4)]))))), (toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 7)]) + (toNumber(self.var_i2) * math.cos(math.radians(toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 4)]))))))
            self.pen.up()

    @warp
    async def my_renderui(self, util, ):
        if eq(util.sprites.stage.var_MOUSEOVERMATERIALS, "true"):
            self.pen.exact_color("#404040")
        else:
            self.pen.exact_color("#4e4e4e")
        self.pen.set_size(15)
        self.gotoxy(-240, -130)
        self.pen.down()
        self.gotoxy((-240 + (len(util.sprites.stage.list_POSSIBLEMATERIALS) * 50)), -130)
        self.gotoxy((-240 + (len(util.sprites.stage.list_POSSIBLEMATERIALS) * 50)), -180)
        self.gotoxy(-240, -155)
        self.pen.set_size(55)
        self.gotoxy((-265 + (len(util.sprites.stage.list_POSSIBLEMATERIALS) * 50)), -152)
        self.pen.up()
        if not eq(util.sprites.stage.var_SELECTEDMATERIAL, "none"):
            self.pen.change_color("brightness", 10)
            self.pen.set_size(40)
            self.xpos = (-260 + (util.sprites.stage.list_POSSIBLEMATERIALS.index(util.sprites.stage.var_SELECTEDMATERIAL) * 50))
            self.pen.down()
            self.pen.up()
        self.var_i = 0
        self.pen.set_size(8)
        for _ in create_repeat(len(util.sprites.stage.list_POSSIBLEMATERIALS)):
            self.var_i += 1
            await self.my_setcolorto(util, util.sprites.stage.list_POSSIBLEMATERIALS[self.var_i])
            self.gotoxy((-273 + (self.var_i * 50)), -165)
            self.pen.down()
            self.gotoxy((self.xpos + 26), -139)
            self.pen.up()
        self.pen.set_size(15)
        if eq(util.sprites.stage.var_MOUSEOVERPLAY, "true"):
            self.pen.exact_color("#404040")
        else:
            self.pen.exact_color("#4e4e4e")
        self.gotoxy(240, 130)
        self.pen.down()
        self.gotoxy(130, 130)
        self.gotoxy(130, 180)
        self.gotoxy(158, 157)
        self.pen.set_size(60)
        self.gotoxy(240, 165)
        self.pen.up()
        if eq(util.sprites.stage.var_MOUSEOVERPLAY, "true"):
            self.pen.exact_color("#199a00")
        else:
            self.pen.exact_color("#22ce00")
        self.pen.set_size(10)
        self.gotoxy(202, 165)
        self.pen.down()
        self.gotoxy(202, 140)
        self.gotoxy(225, 152.5)
        self.gotoxy(202, 165)
        self.gotoxy(210, 152)
        self.pen.up()
        self.pen.set_size(5)
        if eq(util.sprites.stage.var_MOUSEOVERPLAY, "true"):
            self.pen.exact_color("#4f4f4f")
        else:
            self.pen.exact_color("#676767")
        self.gotoxy(140, 168)
        self.pen.down()
        self.gotoxy(170, 168)
        self.gotoxy(170, 138)
        self.gotoxy(140, 138)
        self.gotoxy(140, 168)
        self.gotoxy(140, 148)
        self.gotoxy(170, 148)
        self.gotoxy(170, 158)
        self.gotoxy(140, 158)
        self.gotoxy(140, 168)
        self.gotoxy(150, 168)
        self.gotoxy(150, 138)
        self.gotoxy(160, 138)
        self.gotoxy(160, 168)
        self.pen.up()
        self.pen.set_size(15)
        if eq(util.sprites.stage.var_MOUSEOVERDELETE, "true"):
            self.pen.exact_color("#404040")
        else:
            self.pen.exact_color("#4e4e4e")
        self.gotoxy(-240, 130)
        self.pen.down()
        self.gotoxy(-130, 130)
        self.gotoxy(-130, 180)
        self.gotoxy(-157, 157)
        self.pen.set_size(60)
        self.gotoxy(-240, 165)
        self.pen.up()
        if eq(util.sprites.stage.var_MOUSEOVERDELETE, "true"):
            self.pen.exact_color("#c31010")
        else:
            self.pen.exact_color("#de1313")
        self.pen.set_size(7)
        self.gotoxy(-207, 165)
        self.pen.down()
        self.direction = -90
        for _ in create_repeat(12):
            self.move(5)
            self.direction -= 20
        self.gotoxy(-195, 145)
        self.gotoxy(-205, 147)
        self.gotoxy(-195, 145)
        self.gotoxy(-193, 135)
        self.pen.up()
        self.gotoxy(-173, 165)
        self.pen.down()
        self.gotoxy(-143, 165)
        self.pen.up()
        self.gotoxy(-158, 170)
        self.pen.down()
        self.pen.up()
        self.gotoxy(-173, 156)
        self.pen.down()
        self.gotoxy(-143, 156)
        self.gotoxy(-143, 136)
        self.gotoxy(-173, 136)
        self.gotoxy(-173, 156)
        self.gotoxy(-165, 146)
        self.pen.set_size(17)
        self.gotoxy(-150, 146)
        self.pen.up()
        if eq(util.sprites.stage.var_MOUSEOVERDELETE, "true"):
            self.pen.exact_color("#404040")
        else:
            self.pen.exact_color("#4e4e4e")
        self.pen.set_size(6)
        self.gotoxy(-149, 150)
        self.pen.down()
        self.gotoxy(-149, 142)
        self.pen.up()
        self.gotoxy(-158, 150)
        self.pen.down()
        self.gotoxy(-158, 142)
        self.pen.up()
        self.gotoxy(-167, 150)
        self.pen.down()
        self.gotoxy(-167, 142)
        self.pen.up()

    @warp
    async def my_flags(self, util, ):
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_FLAGS), 4)):
            self.var_i += 4
            self.pen.set_size((util.sprites.stage.var_CAMERASIZE * 0.6))
            self.pen.up()
            self.pen.exact_color("#9b4808")
            await self.my_goto(util, util.sprites.stage.list_FLAGS[(self.var_i - 2)], util.sprites.stage.list_FLAGS[(self.var_i - 1)])
            self.pen.down()
            await self.my_goto(util, util.sprites.stage.list_FLAGS[(self.var_i - 2)], (toNumber(util.sprites.stage.list_FLAGS[(self.var_i - 1)]) + 6))
            self.pen.up()
            self.pen.exact_color(util.sprites.stage.list_FLAGS[self.var_i])
            self.pen.set_size((util.sprites.stage.var_CAMERASIZE * 0.65))
            self.pen.down()
            await self.my_goto(util, util.sprites.stage.list_FLAGS[(self.var_i - 2)], (toNumber(util.sprites.stage.list_FLAGS[(self.var_i - 1)]) + 3.5))
            self.pen.down()
            await self.my_goto(util, util.sprites.stage.list_FLAGS[(self.var_i - 2)], (toNumber(util.sprites.stage.list_FLAGS[(self.var_i - 1)]) + 6))
            await self.my_goto(util, (toNumber(util.sprites.stage.list_FLAGS[(self.var_i - 2)]) + 2.5), (toNumber(util.sprites.stage.list_FLAGS[(self.var_i - 1)]) + 4.75))
            await self.my_goto(util, util.sprites.stage.list_FLAGS[(self.var_i - 2)], (toNumber(util.sprites.stage.list_FLAGS[(self.var_i - 1)]) + 3.5))
            await self.my_goto(util, (toNumber(util.sprites.stage.list_FLAGS[(self.var_i - 2)]) + 0.85), (toNumber(util.sprites.stage.list_FLAGS[(self.var_i - 1)]) + 4.75))
            self.pen.set_size((util.sprites.stage.var_CAMERASIZE * 2.1))
            self.pen.down()
            self.pen.up()

    @warp
    async def my_setcolorto(self, util, arg_x):
        if eq(arg_x, "road"):
            self.pen.exact_color("#80410d")
        else:
            if eq(arg_x, "log"):
                self.pen.exact_color("#efa745")
            else:
                if eq(arg_x, "steel"):
                    self.pen.exact_color("#af635b")
                else:
                    if eq(arg_x, "spring"):
                        self.pen.exact_color("#f3f322")
                    else:
                        self.pen.exact_color("#de156c")


@sprite('Physics')
class SpritePhysics(Target):
    """Sprite Physics"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self._set_shown(True)
        self.pen = Pen(self)

        self.costume = Costumes(
            self.sprite, 0, 100, "all around", [
            {
                'name': "costume1",
                'path': "3339a2953a3bf62bb80e54ff575dbced-fallback.png",
                'center': (0, 0),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_i = 4
        self.var_x = 3.9521253469894106
        self.var_y = -17.26381180260722
        self.var_x2 = 4.9414521338520485
        self.var_y2 = -18.283905394931416
        self.var_friction = 0.01
        self.var_gravity = -0.08
        self.var_1 = 20
        self.var_2 = 5
        self.var_d = -0.0014535960986120603
        self.var_elasticity = 1
        self.var_diff = 7.582018484788173
        self.var_nx = 0.9471283905793966
        self.var_ny = -0.3208548141425998
        self.var_x3 = 15
        self.var_y3 = -17.263811802607222
        self.var_dot = 0.5702117668115122
        self.var_collision = 0
        self.var_r = 0.7
        self.var_i2 = 4
        self.var_change = 0.8518518518518519
        self.var_rotFriction = 0.5
        self.var_r2 = 0.018326
        self.var_smoothness = 0
        self.var_1s = 0.38014548863287534
        self.var_2s = 0.6198545113671247
        self.var_touching = 0
        self.var_tnx = 0.442588842808438
        self.var_tny = 0.8967246602059562
        self.var_i3 = 43.297064375702014
        self.var_strenght = 2.2



        self.sprite.layer = 4

    @warp
    async def my_circletolinedetectioncirclelineoutline(self, util, arg_circleX, arg_circleY, arg_circleR, arg_x1, arg_y1, arg_x2, arg_y2, arg_o):
        self.var_collision = 0
        self.var_d = (((toNumber(arg_x1) - toNumber(arg_x2)) * (toNumber(arg_x1) - toNumber(arg_x2))) + ((toNumber(arg_y1) - toNumber(arg_y2)) * (toNumber(arg_y1) - toNumber(arg_y2))))
        self.var_dot = div((((toNumber(arg_circleX) - toNumber(arg_x1)) * (toNumber(arg_x2) - toNumber(arg_x1))) + ((toNumber(arg_circleY) - toNumber(arg_y1)) * (toNumber(arg_y2) - toNumber(arg_y1)))), self.var_d)
        if gt(self.var_dot, 1):
            self.var_dot = 1
        if gt(0, self.var_dot):
            self.var_dot = 0
        self.var_x3 = (toNumber(arg_x1) + (self.var_dot * (toNumber(arg_x2) - toNumber(arg_x1))))
        self.var_y3 = (toNumber(arg_y1) + (self.var_dot * (toNumber(arg_y2) - toNumber(arg_y1))))
        if ((not lt(arg_x1, self.var_x3) or not lt(arg_x2, self.var_x3)) and (not gt(arg_x1, self.var_x3) or not gt(arg_x2, self.var_x3))):
            self.var_d = sqrt((((self.var_x3 - toNumber(arg_circleX)) * (self.var_x3 - toNumber(arg_circleX))) + ((self.var_y3 - toNumber(arg_circleY)) * (self.var_y3 - toNumber(arg_circleY)))))
            if lt(self.var_d, (toNumber(arg_circleR) + arg_o)):
                self.var_collision = 1
                self.var_nx = div((toNumber(arg_circleX) - self.var_x3), self.var_d)
                self.var_ny = div((toNumber(arg_circleY) - self.var_y3), self.var_d)

    @on_broadcast('physics')
    async def broadcast_physics(self, util):
        await self.my_physics(util, )

    @warp
    async def my_physics(self, util, ):
        await self.my_stress1(util, )
        await self.my_vertex(util, )
        await self.my_ballsmove(util, )
        if lt(self.var_y2, div((util.sprites.stage.var_CAMERAY - 180), util.sprites.stage.var_CAMERASIZE)):
            await self.my_reset(util, )
            return None
        await self.my_sticks(util, toBoolean(None))
        for _ in create_repeat(20):
            await self.my_ballscollide(util, )
            await self.my_sticks(util, not toBoolean(None))
        await self.my_ui(util, )
        await self.my_touchingflags(util, )
        if not "false" in util.sprites.stage.list_FLAGS:
            util.sprites.stage.varMODE = "edit"
            if gt(util.sprites.stage.var_, util.sprites.stage.var_max):
                await self.my_reset(util, )
                util.sprites.stage.var_budget = (util.timer() + 2)
                return None
            else:
                util.sprites.stage.var_LEVEL += 1
                return None
        util.sprites.stage.var_lastmouse = str(util.inputs.mouse_down).lower()

    @warp
    async def my_vertex(self, util, ):
        self.var_i = -4
        for _ in create_repeat(div(len(util.sprites.stage.list_VERTICES), 5)):
            self.var_i += 5
            if toBoolean(util.sprites.stage.list_VERTICES[(self.var_i + 4)]):
                self.var_x = util.sprites.stage.list_VERTICES[self.var_i]
                self.var_y = util.sprites.stage.list_VERTICES[(self.var_i + 1)]
                self.var_x2 = ((toNumber(self.var_x) - toNumber(util.sprites.stage.list_VERTICES[(self.var_i + 2)])) * (1 - self.var_friction))
                self.var_y2 = ((toNumber(self.var_y) - toNumber(util.sprites.stage.list_VERTICES[(self.var_i + 3)])) * (1 - self.var_friction))
                util.sprites.stage.list_VERTICES[(self.var_i + 2)] = self.var_x
                util.sprites.stage.list_VERTICES[(self.var_i + 3)] = self.var_y
                util.sprites.stage.list_VERTICES[self.var_i] = (toNumber(self.var_x) + toNumber(self.var_x2))
                util.sprites.stage.list_VERTICES[(self.var_i + 1)] = ((toNumber(self.var_y) + toNumber(self.var_y2)) + self.var_gravity)

    @on_green_flag
    async def green_flag(self, util):
        self.var_friction = 0.01
        self.var_gravity = -0.08
        self.var_rotFriction = 0.5
        self.var_smoothness = 0

    @warp
    async def my_sticks(self, util, arg_stress):
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_STICKS), 5)):
            self.var_i += 5
            if lt(util.sprites.stage.list_STICKS[(self.var_i - 4)], 1):
                self.var_1 = (toNumber(util.sprites.stage.list_STICKS[(self.var_i - 3)]) * 5)
                self.var_2 = (toNumber(util.sprites.stage.list_STICKS[(self.var_i - 2)]) * 5)
                self.var_x = (toNumber(util.sprites.stage.list_VERTICES[(self.var_2 - 4)]) - toNumber(util.sprites.stage.list_VERTICES[(self.var_1 - 4)]))
                self.var_y = (toNumber(util.sprites.stage.list_VERTICES[(self.var_2 - 3)]) - toNumber(util.sprites.stage.list_VERTICES[(self.var_1 - 3)]))
                self.var_diff = sqrt(((toNumber(self.var_x) * toNumber(self.var_x)) + (toNumber(self.var_y) * toNumber(self.var_y))))
                if eq(util.sprites.stage.list_STICKS[self.var_i], "road"):
                    self.var_elasticity = 1
                    self.var_strenght = 2.2
                else:
                    if eq(util.sprites.stage.list_STICKS[self.var_i], "log"):
                        self.var_elasticity = 1
                        self.var_strenght = 3
                    else:
                        if eq(util.sprites.stage.list_STICKS[self.var_i], "steel"):
                            self.var_elasticity = 1
                            self.var_strenght = 3
                        else:
                            if eq(util.sprites.stage.list_STICKS[self.var_i], "spring"):
                                self.var_elasticity = 40
                                self.var_strenght = 35
                            else:
                                pass
                if arg_stress:
                    util.sprites.stage.list_STICKS[(self.var_i - 4)] = (toNumber(util.sprites.stage.list_STICKS[(self.var_i - 4)]) + (0.35 * abs(div((toNumber(util.sprites.stage.list_STICKS[(self.var_i - 1)]) - self.var_diff), self.var_strenght))))
                if (toBoolean(util.sprites.stage.list_VERTICES[self.var_1]) and toBoolean(util.sprites.stage.list_VERTICES[self.var_2])):
                    self.var_d = div(div((toNumber(util.sprites.stage.list_STICKS[(self.var_i - 1)]) - self.var_diff), (self.var_diff * self.var_elasticity)), 2)
                    util.sprites.stage.list_VERTICES[(self.var_1 - 4)] = (toNumber(util.sprites.stage.list_VERTICES[(self.var_1 - 4)]) - (toNumber(self.var_x) * self.var_d))
                    util.sprites.stage.list_VERTICES[(self.var_1 - 3)] = (toNumber(util.sprites.stage.list_VERTICES[(self.var_1 - 3)]) - (toNumber(self.var_y) * self.var_d))
                    util.sprites.stage.list_VERTICES[(self.var_2 - 4)] = (toNumber(util.sprites.stage.list_VERTICES[(self.var_2 - 4)]) + (toNumber(self.var_x) * self.var_d))
                    util.sprites.stage.list_VERTICES[(self.var_2 - 3)] = (toNumber(util.sprites.stage.list_VERTICES[(self.var_2 - 3)]) + (toNumber(self.var_y) * self.var_d))
                else:
                    self.var_d = div((toNumber(util.sprites.stage.list_STICKS[(self.var_i - 1)]) - self.var_diff), (self.var_diff * self.var_elasticity))
                    if toBoolean(util.sprites.stage.list_VERTICES[self.var_1]):
                        util.sprites.stage.list_VERTICES[(self.var_1 - 4)] = (toNumber(util.sprites.stage.list_VERTICES[(self.var_1 - 4)]) - (toNumber(self.var_x) * self.var_d))
                        util.sprites.stage.list_VERTICES[(self.var_1 - 3)] = (toNumber(util.sprites.stage.list_VERTICES[(self.var_1 - 3)]) - (toNumber(self.var_y) * self.var_d))
                    else:
                        util.sprites.stage.list_VERTICES[(self.var_2 - 4)] = (toNumber(util.sprites.stage.list_VERTICES[(self.var_2 - 4)]) + (toNumber(self.var_x) * self.var_d))
                        util.sprites.stage.list_VERTICES[(self.var_2 - 3)] = (toNumber(util.sprites.stage.list_VERTICES[(self.var_2 - 3)]) + (toNumber(self.var_y) * self.var_d))

    @warp
    async def my_ballsmove(self, util, ):
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_PLAYERS), 9)):
            self.var_i += 9
            if not toBoolean(util.sprites.stage.list_FLAGS[((div(self.var_i, 9) * 4) - 3)]):
                self.var_touching = 0
                self.var_x = util.sprites.stage.list_PLAYERS[(self.var_i - 8)]
                self.var_y = util.sprites.stage.list_PLAYERS[(self.var_i - 7)]
                self.var_x2 = (toNumber(self.var_x) + ((toNumber(self.var_x) - toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 6)])) * (1 - self.var_friction)))
                self.var_y2 = (toNumber(self.var_y) + (((toNumber(self.var_y) - toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 5)])) + self.var_gravity) * (1 - self.var_friction)))
                util.sprites.stage.list_PLAYERS[(self.var_i - 6)] = self.var_x
                util.sprites.stage.list_PLAYERS[(self.var_i - 5)] = self.var_y
                self.var_r = util.sprites.stage.list_PLAYERS[self.var_i]
                util.sprites.stage.list_PLAYERS[(self.var_i - 4)] = (toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 4)]) + toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 3)]))
                self.var_r2 = (((3.1416 * toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 2)])) * div(toNumber(self.var_r), 180)) * (1 - self.var_smoothness))
                if lt(self.var_y2, div((util.sprites.stage.var_CAMERAY - 180), util.sprites.stage.var_CAMERASIZE)):
                    util.sprites.stage.list_PLAYERS[(self.var_i - 8)] = self.var_x2
                    util.sprites.stage.list_PLAYERS[(self.var_i - 7)] = self.var_y2
                    return None
                self.var_i2 = 0
                for _ in create_repeat(div(len(util.sprites.stage.list_STICKS), 5)):
                    self.var_i2 += 5
                    if (eq(util.sprites.stage.list_STICKS[self.var_i2], "road") and lt(util.sprites.stage.list_STICKS[(self.var_i2 - 4)], 1)):
                        self.var_1 = (toNumber(util.sprites.stage.list_STICKS[(self.var_i2 - 3)]) * 5)
                        self.var_2 = (toNumber(util.sprites.stage.list_STICKS[(self.var_i2 - 2)]) * 5)
                        await self.my_circletolinedetectioncirclelineoutline(util, util.sprites.stage.list_PLAYERS[(self.var_i - 8)], util.sprites.stage.list_PLAYERS[(self.var_i - 7)], util.sprites.stage.list_PLAYERS[(self.var_i - 2)], util.sprites.stage.list_VERTICES[(self.var_1 - 4)], util.sprites.stage.list_VERTICES[(self.var_1 - 3)], util.sprites.stage.list_VERTICES[(self.var_2 - 4)], util.sprites.stage.list_VERTICES[(self.var_2 - 3)], 0.5)
                        if eq(self.var_collision, 1):
                            self.var_x2 = toNumber(self.var_x2) + (self.var_ny * self.var_r2)
                            self.var_y2 = toNumber(self.var_y2) + ((0 - self.var_nx) * self.var_r2)
                            self.var_touching = 1
                            self.var_tnx = self.var_nx
                            self.var_tny = self.var_ny
                self.var_i2 = 0
                for _ in create_repeat(div(len(util.sprites.stage.list_LEVEL), 4)):
                    self.var_i2 += 4
                    await self.my_circletolinedetectioncirclelineoutline(util, util.sprites.stage.list_PLAYERS[(self.var_i - 8)], util.sprites.stage.list_PLAYERS[(self.var_i - 7)], util.sprites.stage.list_PLAYERS[(self.var_i - 2)], util.sprites.stage.list_LEVEL[(self.var_i2 - 3)], util.sprites.stage.list_LEVEL[(self.var_i2 - 2)], util.sprites.stage.list_LEVEL[(self.var_i2 - 1)], util.sprites.stage.list_LEVEL[self.var_i2], 0.5)
                    if eq(self.var_collision, 1):
                        self.var_x2 = toNumber(self.var_x2) + (self.var_ny * self.var_r2)
                        self.var_y2 = toNumber(self.var_y2) + ((0 - self.var_nx) * self.var_r2)
                        self.var_touching = 1
                        self.var_tnx = self.var_nx
                        self.var_tny = self.var_ny
                util.sprites.stage.list_PLAYERS[(self.var_i - 8)] = self.var_x2
                util.sprites.stage.list_PLAYERS[(self.var_i - 7)] = self.var_y2
                if eq(self.var_touching, 1):
                    self.var_d = sqrt((((toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 6)]) - toNumber(self.var_x2)) * (toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 6)]) - toNumber(self.var_x2))) + ((toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 5)]) - toNumber(self.var_y2)) * (toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 5)]) - toNumber(self.var_y2)))))
                    self.var_nx = div((toNumber(self.var_x2) - toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 6)])), self.var_d)
                    self.var_ny = div((toNumber(self.var_y2) - toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 5)])), self.var_d)
                    self.var_i3 = ((self.var_nx * self.var_tny) + (self.var_ny * (0 - self.var_tnx)))
                    self.var_i3 = (self.var_i3 * (self.var_d * div(180, (3.1416 * toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 2)])))))
                    util.sprites.stage.list_PLAYERS[(self.var_i - 3)] = (((toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 3)]) + toNumber(self.var_r)) + self.var_i3) * (1 - self.var_rotFriction))
                else:
                    util.sprites.stage.list_PLAYERS[(self.var_i - 3)] = ((toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 3)]) + toNumber(self.var_r)) * (1 - self.var_rotFriction))

    @warp
    async def my_ballscollide(self, util, ):
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_PLAYERS), 9)):
            self.var_i += 9
            self.var_i2 = 0
            for _ in create_repeat(div(len(util.sprites.stage.list_STICKS), 5)):
                self.var_change = (1 - div(0.5, (toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 2)]) * (toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 2)]) * toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 2)])))))
                self.var_i2 += 5
                if (eq(util.sprites.stage.list_STICKS[self.var_i2], "road") and lt(util.sprites.stage.list_STICKS[(self.var_i2 - 4)], 1)):
                    self.var_1 = (toNumber(util.sprites.stage.list_STICKS[(self.var_i2 - 3)]) * 5)
                    self.var_2 = (toNumber(util.sprites.stage.list_STICKS[(self.var_i2 - 2)]) * 5)
                    self.var_x = util.sprites.stage.list_VERTICES[(self.var_1 - 4)]
                    self.var_y = util.sprites.stage.list_VERTICES[(self.var_1 - 3)]
                    self.var_x2 = util.sprites.stage.list_VERTICES[(self.var_2 - 4)]
                    self.var_y2 = util.sprites.stage.list_VERTICES[(self.var_2 - 3)]
                    await self.my_circletolinedetectioncirclelineoutline(util, util.sprites.stage.list_PLAYERS[(self.var_i - 8)], util.sprites.stage.list_PLAYERS[(self.var_i - 7)], util.sprites.stage.list_PLAYERS[(self.var_i - 2)], self.var_x, self.var_y, self.var_x2, self.var_y2, 0.2)
                    if eq(self.var_collision, 1):
                        if eq(self.var_x, self.var_x2):
                            self.var_1s = div((self.var_y3 - toNumber(self.var_y)), (toNumber(self.var_y2) - toNumber(self.var_y)))
                            self.var_2s = div((toNumber(self.var_y2) - self.var_y3), (toNumber(self.var_y2) - toNumber(self.var_y)))
                        else:
                            self.var_1s = div((self.var_x3 - toNumber(self.var_x)), (toNumber(self.var_x2) - toNumber(self.var_x)))
                            self.var_2s = div((toNumber(self.var_x2) - self.var_x3), (toNumber(self.var_x2) - toNumber(self.var_x)))
                        while not eq(self.var_collision, 0):
                            if not (toBoolean(util.sprites.stage.list_VERTICES[self.var_1]) or toBoolean(util.sprites.stage.list_VERTICES[self.var_2])):
                                self.var_change = 0.5
                            util.sprites.stage.list_PLAYERS[(self.var_i - 8)] = (toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 8)]) + (self.var_nx * (1 - self.var_change)))
                            util.sprites.stage.list_PLAYERS[(self.var_i - 7)] = (toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 7)]) + (self.var_ny * (1 - self.var_change)))
                            await self.my_circletolinedetectioncirclelineoutline(util, util.sprites.stage.list_PLAYERS[(self.var_i - 8)], util.sprites.stage.list_PLAYERS[(self.var_i - 7)], util.sprites.stage.list_PLAYERS[(self.var_i - 2)], self.var_x, self.var_y, self.var_x2, self.var_y2, 0.2)
                            if toBoolean(util.sprites.stage.list_VERTICES[self.var_1]):
                                await self.my_movevertby(util, self.var_1, (self.var_1s * (self.var_nx * (0 - self.var_change))), (self.var_1s * (self.var_ny * (0 - self.var_change))))
                            if toBoolean(util.sprites.stage.list_VERTICES[self.var_2]):
                                await self.my_movevertby(util, self.var_2, (self.var_2s * (self.var_nx * (0 - self.var_change))), (self.var_2s * (self.var_ny * (0 - self.var_change))))
            self.var_i2 = 0
            for _ in create_repeat(div(len(util.sprites.stage.list_LEVEL), 4)):
                self.var_i2 += 4
                self.var_x = util.sprites.stage.list_PLAYERS[(self.var_i - 8)]
                self.var_y = util.sprites.stage.list_PLAYERS[(self.var_i - 7)]
                self.var_r = util.sprites.stage.list_PLAYERS[(self.var_i - 2)]
                await self.my_circletolinedetectioncirclelineoutline(util, self.var_x, self.var_y, self.var_r, util.sprites.stage.list_LEVEL[(self.var_i2 - 3)], util.sprites.stage.list_LEVEL[(self.var_i2 - 2)], util.sprites.stage.list_LEVEL[(self.var_i2 - 1)], util.sprites.stage.list_LEVEL[self.var_i2], 0.3)
                if eq(self.var_collision, 1):
                    self.var_x = toNumber(self.var_x) + (self.var_nx * ((toNumber(self.var_r) + 0.3) - self.var_d))
                    self.var_y = toNumber(self.var_y) + (self.var_ny * ((toNumber(self.var_r) + 0.3) - self.var_d))
                util.sprites.stage.list_PLAYERS[(self.var_i - 8)] = self.var_x
                util.sprites.stage.list_PLAYERS[(self.var_i - 7)] = self.var_y

    @warp
    async def my_movevertby(self, util, arg_id, arg_x, arg_y):
        util.sprites.stage.list_VERTICES[(arg_id - 4)] = (toNumber(util.sprites.stage.list_VERTICES[(arg_id - 4)]) + arg_x)
        util.sprites.stage.list_VERTICES[(arg_id - 3)] = (toNumber(util.sprites.stage.list_VERTICES[(arg_id - 3)]) + arg_y)

    @warp
    async def my_stress1(self, util, ):
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_STICKS), 5)):
            self.var_i += 5
            if lt(util.sprites.stage.list_STICKS[(self.var_i - 4)], 1):
                util.sprites.stage.list_STICKS[(self.var_i - 4)] = 0

    @warp
    async def my_reset(self, util, ):
        util.sprites.stage.varMODE = "edit"
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_STICKS), 5)):
            self.var_i += 5
            util.sprites.stage.list_STICKS[(self.var_i - 4)] = 0
        self.var_i = 1
        util.sprites.stage.list_VERTICES.delete_all()
        while not eq(util.sprites.stage.list_SAVE[self.var_i], "∀"):
            util.sprites.stage.list_VERTICES.append(util.sprites.stage.list_SAVE[self.var_i])
            self.var_i += 1
        util.sprites.stage.list_PLAYERS.delete_all()
        while not gt(self.var_i, len(util.sprites.stage.list_SAVE)):
            self.var_i += 1
            if not gt(self.var_i, len(util.sprites.stage.list_SAVE)):
                util.sprites.stage.list_PLAYERS.append(util.sprites.stage.list_SAVE[self.var_i])
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_FLAGS), 4)):
            self.var_i += 4
            util.sprites.stage.list_FLAGS[(self.var_i - 3)] = "false"

    @warp
    async def my_touchingflags(self, util, ):
        self.var_i = 0
        self.var_i2 = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_FLAGS), 4)):
            self.var_i += 9
            self.var_i2 += 4
            if not toBoolean(util.sprites.stage.list_FLAGS[(self.var_i2 - 3)]):
                self.var_x = util.sprites.stage.list_PLAYERS[(self.var_i - 8)]
                self.var_y = util.sprites.stage.list_PLAYERS[(self.var_i - 7)]
                self.var_r = util.sprites.stage.list_PLAYERS[(self.var_i - 2)]
                self.var_x2 = util.sprites.stage.list_FLAGS[(self.var_i2 - 2)]
                self.var_y2 = util.sprites.stage.list_FLAGS[(self.var_i2 - 1)]
                if ((lt((toNumber(self.var_x) - toNumber(self.var_r)), (toNumber(self.var_x2) + 3)) and gt((toNumber(self.var_x) + toNumber(self.var_r)), self.var_x2)) and (lt((toNumber(self.var_y) - toNumber(self.var_r)), (toNumber(self.var_y2) + 6)) and gt((toNumber(self.var_y) + toNumber(self.var_r)), self.var_y2))):
                    util.sprites.stage.list_FLAGS[(self.var_i2 - 3)] = "true"

    @warp
    async def my_ui(self, util, ):
        util.sprites.stage.var_MOUSEOVERPLAY = str((gt(util.inputs.mouse_x, 123) and gt(util.inputs.mouse_y, 123))).lower()
        if (util.inputs.mouse_down and not eq(util.sprites.stage.var_lastmouse, "true")):
            if eq(util.sprites.stage.var_MOUSEOVERPLAY, "true"):
                if gt(util.inputs.mouse_x, 190):
                    util.sprites.stage.var_SELECTED = "none"
                    await self.my_reset(util, )
                else:
                    util.sprites.stage.var_STRESS = str(eq(util.sprites.stage.var_STRESS, "false")).lower()


@sprite('Render Physics')
class SpriteRenderPhysics(Target):
    """Sprite Render Physics"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 155
        self._ypos = 148
        self._direction = 90
        self._set_shown(False)
        self.pen = Pen(self)

        self.costume = Costumes(
            self.sprite, 0, 100, "all around", [
            {
                'name': "costume1",
                'path': "a1f5fcb96b48020acb5628b4291cf8da.png",
                'center': (480, 360),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_i = 55
        self.var_i2 = 5



        self.sprite.layer = 5

    @on_broadcast('render physics')
    async def broadcast_renderphysics(self, util):
        await self.my_render(util, )

    @warp
    async def my_render(self, util, ):
        self.pen.clear_all()
        self.gotoxy(0, 0)
        self.pen.exact_color("#43bde6")
        self.pen.set_size(999)
        self.pen.down()
        self.pen.up()
        await self.my_renderplayers(util, )
        await self.my_flags(util, )
        self.pen.set_size((0.75 * util.sprites.stage.var_CAMERASIZE))
        self.pen.exact_color("#4e4e4e")
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_LEVEL), 4)):
            self.var_i += 4
            await self.my_goto(util, util.sprites.stage.list_LEVEL[(self.var_i - 3)], util.sprites.stage.list_LEVEL[(self.var_i - 2)])
            self.pen.down()
            await self.my_goto(util, util.sprites.stage.list_LEVEL[(self.var_i - 1)], util.sprites.stage.list_LEVEL[self.var_i])
            self.pen.up()
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_STICKS), 5)):
            self.var_i += 5
            self.pen.up()
            if eq(util.sprites.stage.var_STRESS, "true"):
                self.pen.exact_color("#ce1414")
                if lt(util.sprites.stage.list_STICKS[(self.var_i - 4)], 1):
                    self.var_i2 = div(((toNumber(util.sprites.stage.list_STICKS[(self.var_i - 4)]) * toNumber(util.sprites.stage.list_STICKS[(self.var_i - 4)])) + toNumber(util.sprites.stage.list_STICKS[(self.var_i - 4)])), 2)
                    self.pen.set_color("color", (30 * (1 - toNumber(self.var_i2))))
                else:
                    self.pen.set_color("transparency", (70 + (math.sin(math.radians((util.timer() * 150))) * 30)))
            else:
                await self.my_setcolorto(util, util.sprites.stage.list_STICKS[self.var_i])
                if not lt(util.sprites.stage.list_STICKS[(self.var_i - 4)], 1):
                    self.pen.set_color("transparency", (70 + (math.sin(math.radians((util.timer() * 150))) * 30)))
            self.var_i2 = (toNumber(util.sprites.stage.list_STICKS[(self.var_i - 3)]) * 5)
            await self.my_goto(util, util.sprites.stage.list_VERTICES[(toNumber(self.var_i2) - 4)], util.sprites.stage.list_VERTICES[(toNumber(self.var_i2) - 3)])
            self.pen.down()
            self.var_i2 = (toNumber(util.sprites.stage.list_STICKS[(self.var_i - 2)]) * 5)
            await self.my_goto(util, util.sprites.stage.list_VERTICES[(toNumber(self.var_i2) - 4)], util.sprites.stage.list_VERTICES[(toNumber(self.var_i2) - 3)])
            self.pen.up()
        self.pen.exact_color("#676767")
        self.pen.set_size((1.25 * util.sprites.stage.var_CAMERASIZE))
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_VERTICES), 5)):
            self.var_i += 5
            await self.my_goto(util, util.sprites.stage.list_VERTICES[(self.var_i - 4)], util.sprites.stage.list_VERTICES[(self.var_i - 3)])
            self.pen.down()
            self.pen.up()
        await self.my_renderui(util, )

    @warp
    async def my_goto(self, util, arg_x, arg_y):
        self.gotoxy(((toNumber(arg_x) * util.sprites.stage.var_CAMERASIZE) - util.sprites.stage.var_CAMERAX), ((toNumber(arg_y) * util.sprites.stage.var_CAMERASIZE) - util.sprites.stage.var_CAMERAY))

    @warp
    async def my_renderplayers(self, util, ):
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_PLAYERS), 9)):
            self.var_i += 9
            self.var_i2 = util.sprites.stage.list_PLAYERS[(self.var_i - 2)]
            await self.my_goto(util, util.sprites.stage.list_PLAYERS[(self.var_i - 8)], util.sprites.stage.list_PLAYERS[(self.var_i - 7)])
            self.pen.exact_color(util.sprites.stage.list_PLAYERS[(self.var_i - 1)])
            self.pen.set_size((2 * (util.sprites.stage.var_CAMERASIZE * toNumber(self.var_i2))))
            self.pen.down()
            self.pen.up()
            self.pen.set_size((util.sprites.stage.var_CAMERASIZE * 0.65))
            self.pen.change_color("brightness", -20)
            self.pen.down()
            await self.my_goto(util, (toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 8)]) + (toNumber(self.var_i2) * math.sin(math.radians(toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 4)]))))), (toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 7)]) + (toNumber(self.var_i2) * math.cos(math.radians(toNumber(util.sprites.stage.list_PLAYERS[(self.var_i - 4)]))))))
            self.pen.up()

    @warp
    async def my_flags(self, util, ):
        self.var_i = 0
        for _ in create_repeat(div(len(util.sprites.stage.list_FLAGS), 4)):
            self.var_i += 4
            if not toBoolean(util.sprites.stage.list_FLAGS[(self.var_i - 3)]):
                self.pen.set_size((util.sprites.stage.var_CAMERASIZE * 0.6))
                self.pen.up()
                self.pen.exact_color("#9b4808")
                await self.my_goto(util, util.sprites.stage.list_FLAGS[(self.var_i - 2)], util.sprites.stage.list_FLAGS[(self.var_i - 1)])
                self.pen.down()
                await self.my_goto(util, util.sprites.stage.list_FLAGS[(self.var_i - 2)], (toNumber(util.sprites.stage.list_FLAGS[(self.var_i - 1)]) + 6))
                self.pen.up()
                self.pen.exact_color(util.sprites.stage.list_FLAGS[self.var_i])
                self.pen.set_size((util.sprites.stage.var_CAMERASIZE * 0.65))
                self.pen.down()
                await self.my_goto(util, util.sprites.stage.list_FLAGS[(self.var_i - 2)], (toNumber(util.sprites.stage.list_FLAGS[(self.var_i - 1)]) + 3.5))
                self.pen.down()
                await self.my_goto(util, util.sprites.stage.list_FLAGS[(self.var_i - 2)], (toNumber(util.sprites.stage.list_FLAGS[(self.var_i - 1)]) + 6))
                await self.my_goto(util, (toNumber(util.sprites.stage.list_FLAGS[(self.var_i - 2)]) + 2.5), (toNumber(util.sprites.stage.list_FLAGS[(self.var_i - 1)]) + 4.75))
                await self.my_goto(util, util.sprites.stage.list_FLAGS[(self.var_i - 2)], (toNumber(util.sprites.stage.list_FLAGS[(self.var_i - 1)]) + 3.5))
                await self.my_goto(util, (toNumber(util.sprites.stage.list_FLAGS[(self.var_i - 2)]) + 0.85), (toNumber(util.sprites.stage.list_FLAGS[(self.var_i - 1)]) + 4.75))
                self.pen.set_size((util.sprites.stage.var_CAMERASIZE * 2.1))
                self.pen.down()
                self.pen.up()

    @warp
    async def my_renderui(self, util, ):
        self.pen.set_size(15)
        if eq(util.sprites.stage.var_MOUSEOVERPLAY, "true"):
            self.pen.exact_color("#404040")
        else:
            self.pen.exact_color("#4e4e4e")
        self.gotoxy(240, 130)
        self.pen.down()
        self.gotoxy(130, 130)
        self.gotoxy(130, 180)
        self.gotoxy(158, 157)
        self.pen.set_size(60)
        self.gotoxy(240, 165)
        self.pen.up()
        if eq(util.sprites.stage.var_MOUSEOVERPLAY, "true"):
            self.pen.exact_color("#199a00")
        else:
            self.pen.exact_color("#22ce00")
        self.pen.set_size(10)
        self.gotoxy(202, 165)
        self.pen.down()
        self.gotoxy(202, 140)
        self.gotoxy(225, 152.5)
        self.gotoxy(202, 165)
        self.gotoxy(210, 152)
        self.pen.up()
        self.pen.set_size(5)
        if eq(util.sprites.stage.var_MOUSEOVERPLAY, "true"):
            self.pen.exact_color("#4f4f4f")
        else:
            self.pen.exact_color("#676767")
        self.gotoxy(145, 160)
        self.pen.down()
        self.gotoxy(165, 160)
        self.gotoxy(170, 138)
        self.gotoxy(140, 138)
        self.gotoxy(145, 160)
        self.gotoxy(155, 148)
        self.pen.set_size(25)
        self.pen.down()

    @warp
    async def my_setcolorto(self, util, arg_x):
        if eq(arg_x, "road"):
            self.pen.exact_color("#80410d")
        else:
            if eq(arg_x, "log"):
                self.pen.exact_color("#efa745")
            else:
                if eq(arg_x, "steel"):
                    self.pen.exact_color("#af635b")
                else:
                    if eq(arg_x, "spring"):
                        self.pen.exact_color("#f3f322")
                    else:
                        self.pen.exact_color("#de156c")


@sprite('TextEngine')
class SpriteTextEngine(Target):
    """Sprite TextEngine"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 44.69999999999999
        self._ypos = 140.00000000000003
        self._direction = 90
        self._set_shown(False)
        self.pen = Pen(self)

        self.costume = Costumes(
            self.sprite, 1, 54000, "don't rotate", [
            {
                'name': "blank",
                'path': "9af27a7ad39ec41b7cbfda3622d08a1a-fallback.png",
                'center': (0, 0),
                'scale': 1
            },
            {
                'name': " _",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "a_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "b_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "c_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "d_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "e_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "f_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "g_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "h_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "i_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "j_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "k_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "l_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "m_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "n_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "o_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "p_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "q_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "r_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "s_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "t_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "u_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "v_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "w_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "x_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "y_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "z_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "A_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "B_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "C_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "D_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "E_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "F_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "G_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "H_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "I_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "J_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "K_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "L_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "N_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "M_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "O_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "P_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "Q_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "R_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "S_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "T_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "U_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "V_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "W_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "X_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "Y_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "Z_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "0_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "1_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "2_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "3_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "4_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "5_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "6_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "7_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "8_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "9_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "!_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "@_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "#_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "$_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "%_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "^_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "&_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "*_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "(_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': ")_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "-_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "–_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "—_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "=_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "[_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "]_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "\\_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': ";_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "'_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "‘_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "’_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': ",_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "._",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "/_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "__",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "+_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "{_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "}_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "|_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': ":_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "\"_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "“_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "”_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "<_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': ">_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "?_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "`_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "~_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "¢_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "€_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "£_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "¥_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "°_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "′_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "″_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "≠_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "≤_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "≥_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "×_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "⋅_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "÷_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            },
            {
                'name': "±_",
                'path': "89e9c28db982688d9e408d4459ae4700.png",
                'center': (48, 36),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])

        self.varx = 51.8
        self.vary = 130
        self.vari0 = 14
        self.vari1 = 13
        self.vari2 = 1390
        self.vari3 = 0.5
        self.vari4 = 2.7
        self.vari5 = 1.75
        self.vari6 = 0
        self.vari7 = 10
        self.vari8 = 10
        self.vari9 = "0"
        self.varwidth = 98.20000000000002
        self.varbq = 2
        self.varbq2 = 16

        self.listfontName = StaticList(
            ["parabolic", "curvature", "geometric", "angular"]
        )
        self.listfontIndex = StaticList(
            [1, 348, 659, 1006]
        )
        self.listfontData = StaticList(
            ["Parabolic_1592695915713", 115, 1, 0.2, "0;;;;0;;;;", 2, 0.52, "2;Q;;;.04;.6;3;;.16;.08;-.2;.1;-.48;.24;-.44;0;L;0;-.48;;.52;.375;4;;L;-.25;-.015;;.54;-.27;-.3476;-.0081;.38;0;.34;-.17;-.46;.28;.3;0;0;;;;", 3, 0.57, "2;Q;;;0;1.05;1;;L;0;-1.05;;0;.52;4;;.32;.06;-.36;.18;-.58;.29;-.7;0;-.58;0;.7;-.35;.32;-.22;.4;0;0;;;;", 4, 0.55, "1;Q;;;.55;.57;4;;-.27;-.06;-.26;.13;.59;-.295;-.7;0;.59;0;.7;-.35;-.27;.195;.26;0;0;;;;", 5, 0.57, "2;Q;;;.57;1.05;1;;L;0;-1.05;;.57;.52;4;;-.32;-.06;-.36;.18;.58;-.29;-.7;0;.58;0;.7;-.35;-.32;.22;.4;0;0;;;;", 6, 0.57, "1;Q;;;0;.35;5;;L;.57;0;;-.55;0;-.7;.35;.59;-.295;-.7;0;.57;0;.7;-.35;-.225;.1825;.2;0;0;;;;", 7, 0.34, "2;Q;;;.34;1.045;3;;-.01;-.02;-.01;.005;.31;-.155;-.3;0;L;0;-.9;;0;.7;1;;L;.325;0;;0;;;;", 8, 0.57, "2;Q;;;.57;.7;3;;L;0;-.78;;-.55;0;.48;-.24;.27;-.195;.2;0;.57;.52;4;;-.32;-.06;-.36;.18;.58;-.29;-.7;0;.58;0;.7;-.35;-.32;.22;.4;0;0;;;;", 9, 0.55, "2;Q;;;0;1.05;1;;L;0;-1.05;;0;.52;3;;.34;.06;-.36;.18;-.52;.26;-.6;0;L;0;-.4;;0;;;;", 10, 0, "1;;;;0;.7;1;;0;-.7;;;1;;;;0;1.03;;;", 11, 0, "1;Q;;;0;.7;2;;L;0;-.87;;-.3;0;.3;-.15;1;;;;0;1.03;;;", 12, 0.47, "3;;;;0;1.05;1;;0;-1.05;;;.45;.7;1;;-.45;-.45;;;.125;.375;1;;.345;-.375;;;0;;;;", 13, 0, "1;;;;0;1.05;1;;0;-1.05;;;0;;;;", 14, 0.96, "3;Q;;;0;.7;1;;L;0;-.7;;0;.47;3;;.34;.04;-.46;.23;-.46;.23;-.5;0;L;0;-.45;;.48;.45;3;;.4;.03;-.5;.25;-.44;.22;-.5;0;L;0;-.45;;0;;;;", 15, 0.55, "2;Q;;;0;.7;1;;L;0;-.7;;0;.52;3;;.34;.06;-.36;.18;-.52;.26;-.6;0;L;0;-.4;;0;;;;", 16, 0.6, "1;Q;;;.3;.7;4;;-.6;.3;-.7;0;-.6;0;.7;-.35;.6;-.3;.7;0;.6;0;-.7;.35;0;;;;", 17, 0.57, "2;Q;;;0;.7;1;;L;0;-.99;;0;.52;4;;.32;.06;-.36;.18;-.58;.29;-.7;0;-.58;0;.7;-.35;.32;-.22;.4;0;0;;;;", 18, 0.57, "2;Q;;;.57;.7;1;;L;0;-.99;;.57;.52;4;;-.32;-.06;-.36;.18;.58;-.29;-.7;0;.58;0;.7;-.35;-.32;.22;.4;0;0;;;;", 19, 0.32, "2;Q;;;0;.7;1;;L;0;-.7;;0;.52;2;;.3;.06;-.36;.18;0;.025;-.01;0;0;;;;", 20, 0.49, "1;Q;;;.49;.6;6;;-.21;-.065;-.2;.1;.49;-.245;-.37;0;.48;0;.19;-.13;-.48;.24;-.21;-.035;-.48;0;.35;-.175;.22;-.18;.2;0;0;;;;", 21, 0.32, "2;Q;;;.14;.91;3;;L;0;-.76;;.25;0;.3;-.15;.03;.015;.006;0;0;.7;1;;L;.32;0;;0;;;;", 22, 0.54, "2;Q;;;.54;.7;1;;L;0;-.7;;0;.7;3;;L;0;-.4;;.5;0;.6;-.3;-.34;.23;.4;0;0;;;;", 23, 0.56, "1;;;;0;.7;2;;.28;-.7;;;.28;.7;;;0;;;;", 24, 0.92, "1;;;;0;.7;4;;.23;-.7;;;.23;.7;;;.23;-.7;;;.23;.7;;;0;;;;", 25, 0.54, "2;;;;0;.7;1;;.54;-.7;;;.54;.7;1;;-.54;-.7;;;0;;;;", 26, 0.59, "2;Q;;;.59;.7;3;;L;-.32;-.8;;-.032;-.082;.44;-.22;-.01;-.02;.004;0;0;.7;1;;L;.31;-.7;;0;;;;", 27, 0.55, "1;;;;0;.7;3;;.55;0;;;-.55;-.7;;;.55;0;;;0;;;;", 28, 0.77, "2;;;;0;0;2;;.385;1;;;.385;-1;;;.11165;.29;1;;.5467;0;;;0;;;;", 29, 0.69, "1;Q;;;0;.52;8;;L;.37;0;;-.64;.32;-.54;0;-.64;0;.5;-.25;L;-.37;0;;L;0;1;;L;.35;0;;-.58;.29;-.48;0;-.64;0;.48;-.24;0;;;;", 30, 0.76, "1;Q;;;.76;.78;4;;-.5;-.06;-.44;.22;.78;-.39;-1;0;.78;0;1;-.5;-.5;.31;.44;0;0;;;;", 31, 0.76, "1;Q;;;0;1;5;;L;.3;0;;-.92;.46;-1;0;-.92;0;1;-.5;L;-.3;0;;L;0;1;;0;;;;", 32, 0.6, "2;;;;.6;1;3;;-.6;0;;;0;-1;;;.6;0;;;0;.51;1;;.57;0;;;0;;;;", 33, 0.59, "2;;;;.59;1;2;;-.59;0;;;0;-1;;;0;.49;1;;.55;0;;;0;;;;", 34, 0.8, "1;Q;;;.8;.78;6;;-.48;-.07;-.44;.22;.84;-.42;-1;0;.86;0;1;-.5;-.74;.37;.76;0;L;0;.08;;L;-.33;0;;0;;;;", 35, 0.75, "3;;;;0;1;1;;0;-1;;;.75;1;1;;0;-1;;;0;.51;1;;.75;0;;;0;;;;", 36, 0, "1;;;;0;1;1;;0;-1;;;0;;;;", 37, 0.5, "1;Q;;;.5;1;3;;L;0;-.71;;-.52;0;.58;-.29;.36;-.21;.4;0;0;;;;", 38, 0.66, "3;;;;0;1;1;;0;-1;;;.64;1;1;;-.64;-.64;;;.185;.545;1;;.475;-.545;;;0;;;;", 39, 0.6, "1;;;;0;1;2;;0;-1;;;.6;0;;;0;;;;", 40, 0.75, "1;;;;0;0;3;;0;1;;;.75;-1;;;0;1;;;0;;;;", 41, 0.92, "1;;;;0;0;4;;0;1;;;.46;-1;;;.46;1;;;0;-1;;;0;;;;", 42, 0.84, "1;Q;;;.42;1;4;;-.84;.42;-1;0;-.84;0;1;-.5;.84;-.42;1;0;.84;0;-1;.5;0;;;;", 43, 0.65, "1;Q;;;0;0;5;;L;0;1;;L;.32;0;;-.66;.33;-.58;0;-.66;0;.58;-.29;L;-.32;0;;0;;;;", 44, 0.84, "2;Q;;;.42;1;4;;-.84;.42;-1;0;-.84;0;1;-.5;.84;-.42;1;0;.84;0;-1;.5;.5;.22;1;;L;.24;-.32;;0;;;;", 45, 0.68, "2;Q;;;0;0;5;;L;0;1;;L;.35;0;;-.62;.31;-.55;0;-.48;0;.45;-.245;L;-.42;0;;.42;.46;1;;L;.26;-.46;;0;;;;", 46, 0.65, "1;Q;;;.64;.82;6;;-.38;-.06;-.36;.18;.62;-.31;-.52;0;.63;0;.28;-.185;-.63;.315;-.32;-.045;-.65;0;.52;-.26;.41;-.265;.4;0;0;;;;", 47, 0.7, "2;;;;0;1;1;;.7;0;;;.35;1;1;;0;-1;;;0;;;;", 48, 0.74, "1;Q;;;0;1;4;;L;0;-.625;;.74;0;.75;-.375;-.74;.37;.75;0;L;0;.625;;0;;;;", 49, 0.76, "1;;;;0;1;2;;.38;-1;;;.38;1;;;0;;;;", 50, 1.08, "1;;;;0;1;4;;.27;-1;;;.27;1;;;.27;-1;;;.27;1;;;0;;;;", 51, 0.74, "2;;;;0;1;1;;.74;-1;;;.74;1;1;;-.74;-1;;;0;;;;", 52, 0.74, "2;;;;0;1;2;;.37;-.54;;;.37;.54;;;.37;.46;1;;0;-.46;;;0;;;;", 53, 0.71, "1;;;;.01;1;3;;.69;0;;;-.7;-1;;;.71;0;;;0;;;;", 54, 0.62, "1;Q;;;.31;1;4;;-.62;.31;-1;0;-.62;0;1;-.5;.62;-.31;1;0;.62;0;-1;.5;0;;;;", 55, 0.4, "1;;;;0;.8;2;;.3;.2;;;0;-1;;;0;;;;", 56, 0.6, "1;Q;;;0;.78;5;;.39;.055;-.44;.22;-.55;.275;-.54;0;-.28;0;.02;-.15;L;-.44;-.44;;L;.6;0;;0;;;;", 57, 0.62, "2;Q;;;.015;.8;3;;.38;.055;-.4;.2;-.55;.275;-.49;0;-.58;0;.37;-.215;.23;.51;4;;L;.07;0;;-.64;.32;-.44;-.01;-.64;0;.54;-.27;.38;-.245;.4;0;0;;;;", 58, 0.7, "1;;;;.54;0;3;;0;1;;;-.54;-.75;;;.7;0;;;0;;;;", 59, 0.61, "1;Q;;;.56;1;6;;L;-.495;0;;L;-.045;-.51;;.09;.12;-.24;.12;-.61;.305;-.61;0;-.64;0;.61;-.305;.36;-.235;.4;0;0;;;;", 60, 0.64, "1;Q;;;.62;.85;7;;-.21;-.08;-.3;.15;.71;-.355;-1.08;0;.02;0;.05;-.085;.43;.0525;.63;-.315;-.62;.31;.6;0;-.58;0;-.6;.3;.44;-.28;-.57;0;0;;;;", 61, 0.62, "1;;;;0;1;2;;.62;0;;;-.5;-1;;;0;;;;", 62, 0.63, "2;Q;;;.315;1;4;;-.56;.28;-.48;0;-.56;0;.48;-.24;.56;-.28;.48;0;.56;0;-.48;.24;.315;.52;4;;-.63;.315;-.52;0;-.63;0;.52;-.26;.63;-.315;.52;0;.63;0;-.52;.26;0;;;;", 63, 0.64, "1;Q;;;.02;.15;7;;.22;.08;.3;-.15;-.7;.35;1.08;0;-.016;0;-.08;.085;-.488;-.044;-.66;.33;.6;-.3;-.62;0;.58;0;.58;-.29;-.436;.28;.54;0;0;;;;", 64, 0, "1;;;;0;1;1;;0;-.67;;;1;;;;0;0;;;", 65, 1.06, "2;Q;;;.73;.49;4;;-.2;-.05;-.28;.14;.42;-.21;-.51;0;.42;0;.51;-.255;-.2;.15;.28;0;.73;.63;7;;L;0;-.35;;.26;0;.32;-.16;-.4;.2;.62;0;-1.06;0;-1.04;.52;1.06;-.53;-1.19;0;1.04;0;1.11;-.555;0;.12;.08;0;0;;;;", 66, 0.8, "4;;;;.32;1;1;;-.2;-1;;;.68;1;1;;-.2;-1;;;.08;.7;1;;.72;0;;;0;.3;1;;.72;0;;;0;;;;", 67, 0.63, "2;Q;;;.63;.82;6;;-.43;-.05;-.36;.18;.61;-.305;-.51;0;.59;.01;.29;-.19;-.61;.305;-.32;-.045;-.63;0;.52;-.26;.39;-.255;.4;0;.32;1.13;1;;L;0;-1.26;;0;;;;", 68, 0.96, "3;Q;;;.11;0;1;;L;.74;1;;.17;1;4;;-.34;.17;-.4;0;-.34;0;.4;-.2;.34;-.17;.4;0;.34;0;-.4;.2;.79;.4;4;;-.34;.17;-.4;0;-.34;0;.4;-.2;.34;-.17;.4;0;.34;0;-.4;.2;0;;;;", 69, 0.46, "1;;;;0;.56;2;;.23;.44;;;.23;-.44;;;0;;;;", 70, 0.82, "1;Q;;;.82;0;8;;L;-.63;.63;;.14;-.07;.1;.07;.41;0;-.36;.18;-.43;.215;-.4;0;-.54;0;.14;-.17;.54;-.27;-.16;-.1;.62;0;.5;-.25;-.81;.435;1.02;0;0;;;;", 71, 0.43301, "3;;;;.21651;1;1;;0;-.5;;;0;.875;1;;.43301;-.25;;;0;.625;1;;.43301;.25;;;0;;;;", 72, 0.18, "1;Q;;;.18;1;2;;.36;-.18;-.36;-.22;.36;0;.4;-.41;0;;;;", 73, 0.18, "1;Q;;;0;1;2;;-.36;.18;-.36;-.22;-.36;0;.4;-.41;0;;;;", 74, 0.38, "1;;;;0;.36;1;;.38;0;;;0;;;;", 75, 0.6, "1;;;;0;.36;1;;.6;0;;;0;;;;", 76, 1.2, "1;;;;0;.36;1;;1.2;0;;;0;;;;", 77, 0.62, "2;;;;0;.505;1;;.62;0;;;0;.215;1;;.62;0;;;0;;;;", 78, 0.22, "1;;;;.22;1;3;;-.22;0;;;0;-1.2;;;.22;0;;;0;;;;", 79, 0.22, "1;;;;0;1;3;;.22;0;;;0;-1.2;;;-.22;0;;;0;;;;", 80, 0.315, "1;;;;0;1;1;;.315;-1.26;;;0;;;;", 81, 0, "1;;;;0;.05;1;;-.06;-.25;;;1;;;;0;.6;;;", 82, 0, "1;;;;0;1;1;;0;-.3;;;0;;;;", 83, 0.075, "1;;;;0;1;1;;.075;-.3;;;0;;;;", 84, 0.075, "1;;;;.075;1;1;;-.075;-.3;;;0;;;;", 85, 0, "1;;;;0;.05;1;;-.06;-.25;;;0;;;;", 86, 0, "0;;;;1;;;;0;0;;;", 87, 0.315, "1;;;;0;-.26;1;;.315;1.26;;;0;;;;", 88, 0.64, "1;;;;0;-.2;1;;.64;0;;;0;;;;", 89, 0.64, "2;;;;.32;.68;1;;0;-.64;;;0;.36;1;;.64;0;;;0;;;;", 90, 0.33, "1;Q;;;.33;1.06;6;;.4;-.2;-.36;0;L;0;-.29;;-.26;0;.12;-.13;-.26;.13;-.12;-.07;L;0;-.29;;.4;0;.36;-.18;0;;;;", 91, 0.33, "1;Q;;;0;1.06;6;;-.4;.2;-.36;0;L;0;-.29;;.26;0;.12;-.13;.26;-.13;-.12;-.07;L;0;-.29;;-.4;0;.36;-.18;0;;;;", 92, 0, "1;;;;0;1;1;;0;-1.26;;;0;;;;", 93, 0, "0;;;;2;;;;0;.6;;;0;0;;;", 94, 0.27, "2;;;;0;1;1;;0;-.3;;;.27;1;1;;0;-.3;;;0;;;;", 95, 0.355, "2;;;;0;1;1;;.075;-.3;;;.28;1;1;;.075;-.3;;;0;;;;", 96, 0.355, "2;;;;.075;1;1;;-.075;-.3;;;.355;1;1;;-.075;-.3;;;0;;;;", 97, 0.6, "1;;;;.6;.74;2;;-.6;-.36;;;.6;-.36;;;0;;;;", 98, 0.6, "1;;;;0;.74;2;;.6;-.36;;;-.6;-.36;;;0;;;;", 99, 0.56, "1;Q;;;0;.8;5;;.36;.055;-.4;.2;-.54;.27;-.5;0;-.3;0;.14;-.15;.3;-.15;-.04;-.08;L;0;-.03;;1;;;;.26;0;;;", 100, 0.2, "1;;;;0;1.13;1;;.2;-.23;;;0;;;;", 101, 0.6, "1;Q;;;0;.4;4;;.23;.015;-.28;.14;-.05;.09;-.16;0;.05;.065;.16;-.08;-.23;.13;.28;0;0;;;;", 102, 0.58, "3;Q;;;.58;.73;4;;-.24;-.07;-.28;.14;.64;-.32;-.74;0;.64;0;.74;-.37;-.24;.19;.28;0;.32;1;1;;L;0;-.13;;.32;.13;1;;L;0;-.13;;0;;;;", 103, 0.7, "3;Q;;;.7;.994;4;;0;-.04;-.012;.006;.94;-.47;-1;0;.94;0;1;-.5;0;.04;.012;0;0;.62;1;;L;.59;0;;0;.38;1;;L;.59;0;;0;;;;", 104, 0.7, "2;Q;;;.67;.97;4;;0;-.09;-.06;.03;1.22;-.45;-1;0;-.8224;.1056;.32;-.33;L;.7;0;;0;.5;1;;L;.59;0;;0;;;;", 105, 0.74, "4;;;;0;1;2;;.37;-.54;;;.37;.54;;;.37;.46;1;;0;-.46;;;.15;.42;1;;.44;0;;;.15;.2;1;;.44;0;;;0;;;;", 106, 0.38, "1;Q;;;.19;1;4;;-.38;.19;-.38;0;-.38;0;.38;-.19;.38;-.19;.38;0;.38;0;-.38;.19;0;;;;", 107, 0.075, "1;;;;.075;1;1;;-.075;-.3;;;0;;;;", 108, 0.355, "2;;;;.075;1;1;;-.075;-.3;;;.355;1;1;;-.075;-.3;;;0;;;;", 109, 0.62, "3;;;;0;.505;1;;.62;0;;;0;.215;1;;.62;0;;;.18;.03;1;;.26;.64;;;0;;;;", 110, 0.6, "2;;;;0;.1;1;;.6;0;;;.6;.74;2;;-.6;-.21;;;.6;-.21;;;0;;;;", 111, 0.6, "2;;;;0;.1;1;;.6;0;;;0;.74;2;;.6;-.21;;;-.6;-.21;;;0;;;;", 112, 0.48, "2;;;;0;.6;1;;.48;-.48;;;.48;.6;1;;-.48;-.48;;;0;;;;", 113, 0.1, "0;;;;1;;;;.05;.36;;;", 114, 0.6, "1;;;;0;.36;1;;.6;0;;;2;;;;.3;.62;;;.3;.1;;;", 115, 0.6, "3;;;;0;.1;1;;.6;0;;;0;.48;1;;.6;0;;;.3;.67;1;;0;-.38;;;0;;;;", "Curvature_1592695926964", 103, 1, 0.45, "0;;;;0;;;;", 2, 0.5, "2;Q;;;.06;.6;3;;.06;.08;-.08;.04;-.5;.25;-.4;0;L;0;-.44;;.5;.32;4;;-.1;-.1;-.04;.02;.5;-.25;-.28;-.02;.4;0;.32;-.16;-.28;.22;.2;0;0;;;;", 3, 0.54, "2;Q;;;0;1.07;1;;L;0;-1.07;;0;.51;4;;.14;.1;-.26;.13;-.54;.27;-.64;0;-.54;0;.64;-.32;.06;-.15;.24;0;0;;;;", 4, 0.5, "1;Q;;;.5;.6;4;;-.06;-.08;-.08;.04;.62;-.31;-.64;0;.62;0;.64;-.32;-.06;.11;.08;0;0;;;;", 5, 0.54, "2;Q;;;.54;1.07;1;;L;0;-1.07;;.54;.51;4;;-.14;-.1;-.26;.13;.54;-.27;-.64;0;.54;0;.64;-.32;-.06;.15;.24;0;0;;;;", 6, 0.54, "1;Q;;;0;.32;5;;L;.54;0;;-.54;0;-.64;.32;.54;-.27;-.64;0;.58;0;.64;-.32;-.06;.11;.08;0;0;;;;", 7, 0.36, "2;Q;;;.4;1.06;3;;-.01;-.03;-.02;.01;.33;-.165;-.38;0;L;0;-.88;;0;.64;1;;L;.36;0;;0;;;;", 8, 0.54, "2;Q;;;.54;.64;3;;L;0;-.74;;-.58;0;.44;-.22;.06;-.11;.08;0;.54;.51;4;;-.14;-.1;-.26;.13;.54;-.27;-.64;0;.54;0;.64;-.32;-.06;.15;.24;0;0;;;;", 9, 0.54, "2;Q;;;0;1.07;1;;L;0;-1.07;;0;.51;3;;.14;.1;-.26;.13;-.54;.27;-.52;0;L;0;-.38;;0;;;;", 10, 0, "1;;;;0;.64;1;;0;-.64;;;1;;;;0;1.02;;;", 11, 0, "1;Q;;;0;.64;3;;L;0;-.77;;-.33;0;.38;-.19;.01;-.035;.02;0;1;;;;0;1.02;;;", 12, 0.4, "2;Q;;;0;1.07;1;;L;0;-1.07;;.4;.64;4;;L;-.28;-.28;;-.08;-.04;.08;-.04;-.08;.08;-.08;0;L;.28;-.28;;0;;;;", 13, 0, "1;;;;0;1.07;1;;0;-1.07;;;0;;;;", 14, 0.9, "3;Q;;;0;.64;1;;L;0;-.64;;0;.51;3;;.1;.1;-.26;.13;-.2;.15;-.26;0;L;0;-.51;;.45;.51;3;;.1;.1;-.26;.13;-.4;.2;-.52;0;L;0;-.38;;0;;;;", 15, 0.54, "2;Q;;;0;.64;1;;L;0;-.64;;0;.51;3;;.14;.1;-.26;.13;-.54;.27;-.52;0;L;0;-.38;;0;;;;", 16, 0.54, "1;Q;;;.27;.64;4;;-.54;.27;-.64;0;-.54;0;.64;-.32;.54;-.27;.64;0;.54;0;-.64;.32;0;;;;", 17, 0.54, "2;Q;;;0;.64;1;;L;0;-.96;;0;.51;4;;.14;.1;-.26;.13;-.54;.27;-.64;0;-.54;0;.64;-.32;.06;-.15;.24;0;0;;;;", 18, 0.54, "2;Q;;;.54;.64;1;;L;0;-.96;;.54;.51;4;;-.14;-.1;-.26;.13;.54;-.27;-.64;0;.54;0;.64;-.32;-.06;.15;.24;0;0;;;;", 19, 0.27, "2;Q;;;0;.64;1;;L;0;-.64;;0;.51;1;;.14;.1;-.26;.13;0;;;;", 20, 0.46, "1;Q;;;.46;.6;6;;-.14;-.08;-.08;.04;.46;-.23;-.31;0;.46;0;.17;-.125;-.46;.23;-.17;-.04;-.46;0;.31;-.155;.14;-.15;.08;0;0;;;;", 21, 0.38, "2;Q;;;.17;.95;3;;L;0;-.76;;.33;0;.38;-.19;-.01;.025;.015;0;0;.64;1;;L;.38;0;;0;;;;", 22, 0.54, "2;Q;;;.54;.64;1;;L;0;-.64;;0;.64;3;;L;0;-.38;;.54;0;.52;-.26;-.06;.15;.24;0;0;;;;", 23, 0.54, "1;;;;0;.64;2;;.27;-.64;;;.27;.64;;;0;;;;", 24, 0.92, "1;;;;0;.64;4;;.23;-.64;;;.23;.64;;;.23;-.64;;;.23;.64;;;0;;;;", 25, 0.54, "2;;;;0;.64;1;;.54;-.64;;;.54;.64;1;;-.54;-.64;;;0;;;;", 26, 0.54, "2;Q;;;.54;.64;2;;L;-.32484;-.77;;-.02968;-.08016;.4;-.19;0;.64;1;;L;.27;-.64;;0;;;;", 27, 0.54, "1;;;;0;.64;3;;.54;0;;;-.54;-.64;;;.54;0;;;0;;;;", 28, 0.74, "2;;;;0;0;2;;.37;1;;;.37;-1;;;.111;.3;1;;.518;0;;;0;;;;", 29, 0.72, "1;Q;;;0;.5;8;;L;.45;0;;-.54;.27;-.5;0;-.54;0;.5;-.25;L;-.45;0;;L;0;1;;L;.43;0;;-.54;.27;-.5;0;-.54;0;.5;-.25;0;;;;", 30, 0.74, "1;Q;;;.74;.9;4;;-.14;-.12;-.2;.1;.86;-.43;-1;0;.86;0;1;-.5;-.14;.19;.2;0;0;;;;", 31, 0.74, "1;Q;;;0;1;5;;L;.3;0;;-.88;.44;-1;0;-.88;0;1;-.5;L;-.3;0;;L;0;1;;0;;;;", 32, 0.72, "2;;;;.72;1;3;;-.72;0;;;0;-1;;;.72;0;;;0;.5;1;;.7;0;;;0;;;;", 33, 0.72, "2;;;;.72;1;2;;-.72;0;;;0;-1;;;0;.5;1;;.7;0;;;0;;;;", 34, 0.74, "1;Q;;;.74;.9;6;;-.14;-.12;-.2;.1;.86;-.43;-1;0;.86;0;1;-.5;-.14;.19;.2;0;L;0;.35;;L;-.32;0;;0;;;;", 35, 0.74, "3;;;;0;1;1;;0;-1;;;.74;1;1;;0;-1;;;0;.5;1;;.74;0;;;0;;;;", 36, 0.3, "3;;;;.15;1;1;;0;-1;;;0;1;1;;.3;0;;;0;0;1;;.3;0;;;0;;;;", 37, 0.4, "1;Q;;;.4;1;3;;L;0;-.6;;-.64;0;.8;-.4;.04;-.05;.04;0;0;;;;", 38, 0.65, "3;Q;;;0;1;1;;L;0;-1;;.65;1;2;;L;-.45;-.4;;.05;-.1125;.2;-.1;0;.5;2;;.05;.0875;-.2;0;L;.45;-.4;;0;;;;", 39, 0.72, "1;;;;0;1;2;;0;-1;;;.72;0;;;0;;;;", 41, 0.98, "1;;;;0;0;4;;0;1;;;.49;-1;;;.49;1;;;0;-1;;;0;;;;", 40, 0.74, "1;;;;0;0;3;;0;1;;;.74;-1;;;0;1;;;0;;;;", 42, 0.9, "1;Q;;;.45;1;4;;-.9;.45;-1;0;-.9;0;1;-.5;.9;-.45;1;0;.9;0;-1;.5;0;;;;", 43, 0.72, "1;Q;;;0;0;5;;L;0;1;;L;.45;0;;-.54;.27;-.55;0;-.54;0;.55;-.275;L;-.45;0;;0;;;;", 44, 0.9, "2;Q;;;.45;1;4;;-.9;.45;-1;0;-.9;0;1;-.5;.9;-.45;1;0;.9;0;-1;.5;.55;.26;1;;L;.3;-.31;;0;;;;", 45, 0.72, "2;Q;;;0;0;5;;L;0;1;;L;.45;0;;-.54;.27;-.55;0;-.54;0;.55;-.275;L;-.45;0;;.45;.45;1;;L;.27;-.45;;0;;;;", 46, 0.68, "1;Q;;;.68;.9;6;;-.18;-.12;-.2;.1;.7;-.35;-.47;0;.7;0;.33;-.215;-.66;.33;-.33;-.05;-.7;0;.47;-.235;.18;-.21;.2;0;0;;;;", 47, 0.76, "2;;;;.38;1;1;;0;-1;;;0;1;1;;.76;0;;;0;;;;", 48, 0.74, "1;Q;;;0;1;4;;L;0;-.6;;.74;0;.8;-.4;-.74;.37;.8;0;L;0;.6;;0;;;;", 49, 0.76, "1;;;;0;1;2;;.38;-1;;;.38;1;;;0;;;;", 50, 1.04, "1;;;;0;1;4;;.26;-1;;;.26;1;;;.26;-1;;;.26;1;;;0;;;;", 51, 0.74, "2;;;;0;1;1;;.74;-1;;;.74;1;1;;-.74;-1;;;0;;;;", 52, 0.74, "2;;;;.37;.45;1;;0;-.45;;;0;1;2;;.37;-.55;;;.37;.55;;;0;;;;", 53, 0.74, "1;;;;0;1;3;;.74;0;;;-.74;-1;;;.74;0;;;0;;;;", 54, 0.6, "1;Q;;;.3;1;6;;-.6;.3;-.95;0;L;0;-.05;;-.6;0;.95;-.475;.6;-.3;.95;0;L;0;.05;;.6;0;-.95;.475;0;;;;", 55, 0.4, "1;;;;0;.85;2;;.28;.15;;;0;-1;;;0;;;;", 56, 0.6, "1;Q;;;0;.9;5;;.12;.12;-.2;.1;-.6;.3;-.56;0;-.8;0;.04;-.22;.4;-.2;-.2;-.1;L;.6;0;;0;;;;", 57, 0.6, "2;Q;;;0;.9;4;;.12;.12;-.2;.1;-.6;.3;-.54;0;-.5;0;.46;-.23;L;-.1;0;;.35;.5;3;;-.5;.25;-.46;0;-.6;0;.54;-.27;.12;-.18;.2;0;0;;;;", 58, 0.6, "1;;;;.48;0;3;;0;1;;;-.48;-.75;;;.6;0;;;0;;;;", 59, 0.6, "1;Q;;;.58;1;6;;L;-.56;0;;L;-.02;-.48;;.28;.08;-.08;.04;-.6;.3;-.56;0;-.6;0;.56;-.28;.12;-.18;.2;0;0;;;;", 60, 0.6, "1;Q;;;.52;.975;6;;-.04;-.07;-.05;.025;.72;-.36;-1.08;0;.6;0;.92;-.46;-.6;.3;.56;0;-.6;0;-.56;.28;.28;-.22;-.2;0;0;;;;", 61, 0.64, "1;;;;0;1;2;;.64;0;;;-.465;-1;;;0;;;;", 62, 0.6, "2;Q;;;.3;1;4;;-.54;.27;-.46;0;-.54;0;.46;-.23;.54;-.27;.46;0;.54;0;-.46;.23;.3;.54;4;;-.6;.3;-.54;0;-.6;0;.54;-.27;.6;-.3;.54;0;.6;0;-.54;.27;0;;;;", 63, 0.6, "1;Q;;;.08;.025;6;;.04;.07;.05;-.025;-.72;.36;1.08;0;-.6;0;-.92;.46;.6;-.3;-.56;0;.6;0;.56;-.28;-.36;.24;.2;0;0;;;;", 64, 0, "1;;;;0;1;1;;0;-.68;;;1;;;;0;0;;;", 65, 1, "2;Q;;;.7;.7;7;;L;0;-.4;;.22;0;.2;-.1;-.38;.19;.6;0;-1;0;-.9;.45;1;-.5;-1;0;1;0;1;-.5;-.08;.17;.1;0;.7;.64;4;;-.16;-.07;-.12;.06;.44;-.22;-.5;0;.44;0;.5;-.25;-.16;.15;.2;0;0;;;;", 66, 0.7, "4;;;;.3225;1;1;;-.225;-.9;;;.6025;1;1;;-.225;-.9;;;.1;.75;1;;.6;0;;;0;.35;1;;.6;0;;;0;;;;", 67, 0.68, "2;Q;;;.68;.9;6;;-.18;-.12;-.2;.1;.7;-.35;-.47;0;.7;0;.33;-.215;-.66;.33;-.33;-.05;-.7;0;.47;-.235;.18;-.21;.2;0;.34;1.15;1;;L;0;-1.3;;0;;;;", 68, 1, "3;Q;;;.2;0;1;;L;.6;1;;.17;1;4;;-.34;.17;-.4;0;-.34;0;.4;-.2;.34;-.17;.4;0;.34;0;-.4;.2;.83;.4;4;;-.34;.17;-.4;0;-.34;0;.4;-.2;.34;-.17;.4;0;.34;0;-.4;.2;0;;;;", 69, 0.4, "1;;;;0;.6;2;;.2;.4;;;.2;-.4;;;0;;;;", 70, 0.9, "1;Q;;;.9;0;9;;-.06;-.15;.4;0;.39;-.27;-.44;.3;.15;-.075;.12;.08;.4;0;-.4;.2;-.4;.2;-.4;0;-.55;0;.08;-.15;.55;-.275;-.14;-.11;.7;0;.5;-.25;-.6;.4;1;0;0;;;;", 71, 0.47553, "3;;;;.23776;1;1;;0;-.25;;;0;.82725;2;;.23776;-.07725;;;.23777;.07725;;;.09082;.54775;2;;.14694;.20225;;;.14695;-.20225;;;0;;;;", 72, 0.25, "1;Q;;;.25;1;2;;.5;-.25;-.2;-.25;.5;0;0;-.3;0;;;;", 73, 0.25, "1;Q;;;0;1;2;;-.5;.25;-.2;-.25;-.5;0;0;-.3;0;;;;", 74, 0.5, "1;;;;0;.4;1;;.5;0;;;0;;;;", 77, 0.55, "2;;;;0;.55;1;;.55;0;;;0;.25;1;;.55;0;;;0;;;;", 78, 0.25, "1;;;;.25;1;3;;-.25;0;;;0;-1.2;;;.25;0;;;0;;;;", 79, 0.25, "1;;;;0;1;3;;.25;0;;;0;-1.2;;;-.25;0;;;0;;;;", 80, 0.4, "1;;;;0;1;1;;.45;-1.2;;;0;;;;", 81, 0, "1;Q;;;0;.05;1;;-.12;0;0;-.1;1;;;;0;.6;;;", 82, 0, "1;;;;0;1;1;;0;-.25;;;0;;;;", 85, 0, "1;Q;;;0;.05;1;;-.12;0;0;-.1;0;;;;", 86, 0, "0;;;;1;;;;0;0;;;", 97, 0.5, "1;;;;.5;.65;2;;-.5;-.25;;;.5;-.25;;;0;;;;", 98, 0.5, "1;;;;0;.65;2;;.5;-.25;;;-.5;-.25;;;0;;;;", 87, 0.4, "1;;;;0;-.2;1;;.4;1.2;;;0;;;;", 88, 0.7, "1;;;;0;-.2;1;;.7;0;;;0;;;;", 89, 0.5, "2;;;;0;.4;1;;.5;0;;;.25;.65;1;;0;-.5;;;0;;;;", 90, 0.3, "1;Q;;;.3;1;6;;.3;-.15;-.28;-.03;L;0;-.2;;-.3;0;.28;-.17;-.3;.15;-.28;-.03;L;0;-.2;;.3;0;.28;-.17;0;;;;", 91, 0.3, "1;Q;;;0;1;6;;-.3;.15;-.28;-.03;L;0;-.2;;.3;0;.28;-.17;.3;-.15;-.28;-.03;L;0;-.2;;-.3;0;.28;-.17;0;;;;", 92, 0, "1;;;;0;1.05;1;;0;-1.25;;;0;;;;", 93, 0, "0;;;;2;;;;0;.6;;;0;0;;;", 94, 0.25, "2;;;;0;1;1;;0;-.25;;;.25;1;1;;0;-.25;;;0;;;;", 99, 0.5, "1;Q;;;0;.9;4;;.1;.1;-.2;.1;-.5;.25;-.54;0;-.275;0;.06;-.13;.28;-.14;.04;-.1;1;;;;.225;0;;;", 100, 0.2, "1;;;;0;1.075;1;;.2;-.2;;;0;;;;", 101, 0.6, "1;Q;;;0;.325;4;;.14;.03;-.3;.15;-.02;.09;-.15;0;.02;.08;.15;-.075;-.14;.1;.3;0;0;;;;", 103, 0.74, "3;Q;;;.74;.93;4;;-.2;-.08;-.14;.07;.66;-.33;-1;0;.66;0;1;-.5;-.2;.18;.14;0;0;.62;1;;L;.6;0;;0;.38;1;;L;.6;0;;0;;;;", 104, 0.74, "2;Q;;;.7;.93;5;;-.12;-.08;-.14;.07;.56;-.28;-.6;0;L;0;-.35;;-.4;0;.5;-.3;L;.74;0;;0;.5;1;;L;.58;0;;0;;;;", 83, 0, "1;Q;;;0;.85;1;;.12;0;0;.1;0;;;;", 84, 0, "1;Q;;;0;1.05;1;;-.12;0;0;-.1;0;;;;", 95, 0.25, "2;Q;;;0;.85;1;;.12;0;0;.1;.25;.85;1;;.12;0;0;.1;0;;;;", 96, 0.25, "2;Q;;;0;1.05;1;;-.12;0;0;-.1;.25;1.05;1;;-.12;0;0;-.1;0;;;;", 107, 0.05, "1;;;;.05;1.05;1;;-.05;-.2;;;0;;;;", 108, 0.25, "2;;;;.05;1.05;1;;-.05;-.2;;;.25;1.05;1;;-.05;-.2;;;0;;;;", "Geometric_1592695965870", 115, 1, 0.2, "0;;;;0;;;;", 2, 0.52, "2;;;;.04;.6;4;;.1;.1;;;.26;0;;;.12;-.12;;;0;-.58;;;.52;.36;6;;-.4;0;;;-.12;-.12;;;0;-.12;;;.12;-.12;;;.25;0;;;.15;.15;;;0;;;;", 3, 0.57, "2;;;;0;1.05;1;;0;-1.05;;;0;.52;7;;.2;.18;;;.19;0;;;.18;-.18;;;0;-.34;;;-.18;-.18;;;-.19;0;;;-.2;.18;;;0;;;;", 4, 0.55, "1;;;;.55;.56;7;;-.14;.14;;;-.23;0;;;-.18;-.18;;;0;-.34;;;.18;-.18;;;.23;0;;;.14;.14;;;0;;;;", 5, 0.57, "2;;;;.57;1.05;1;;0;-1.05;;;.57;.52;7;;-.2;.18;;;-.19;0;;;-.18;-.18;;;0;-.34;;;.18;-.18;;;.19;0;;;.2;.18;;;0;;;;", 6, 0.57, "1;;;;0;.35;9;;.57;0;;;0;.17;;;-.18;.18;;;-.21;0;;;-.18;-.18;;;0;-.34;;;.18;-.18;;;.24;0;;;.11;.1;;;0;;;;", 7, 0.34, "2;;;;.34;1.05;3;;-.1;0;;;-.1;-.1;;;0;-.95;;;0;.7;1;;.325;0;;;0;;;;", 8, 0.57, "2;;;;.57;.7;4;;0;-.88;;;-.14;-.14;;;-.29;0;;;-.1;.1;;;.57;.52;7;;-.2;.18;;;-.19;0;;;-.18;-.18;;;0;-.34;;;.18;-.18;;;.19;0;;;.2;.18;;;0;;;;", 9, 0.55, "2;;;;0;1.05;1;;0;-1.05;;;0;.52;4;;.2;.18;;;.2;0;;;.17;-.17;;;0;-.53;;;0;;;;", 10, 0, "1;;;;0;.7;1;;0;-.7;;;1;;;;0;1.03;;;", 11, 0, "1;;;;0;.7;3;;0;-.945;;;-.075;-.075;;;-.075;0;;;1;;;;0;1.03;;;", 12, 0.47, "3;;;;0;1.05;1;;0;-1.05;;;.45;.7;1;;-.45;-.45;;;.125;.375;1;;.345;-.375;;;0;;;;", 13, 0, "1;;;;0;1.05;1;;0;-1.05;;;0;;;;", 14, 0.96, "3;;;;0;.7;1;;0;-.7;;;0;.56;4;;.18;.14;;;.16;0;;;.14;-.14;;;0;-.56;;;.48;.56;4;;.16;.14;;;.18;0;;;.14;-.14;;;0;-.56;;;0;;;;", 15, 0.55, "2;;;;0;.7;1;;0;-.7;;;0;.52;4;;.2;.18;;;.18;0;;;.17;-.17;;;0;-.53;;;0;;;;", 16, 0.6, "1;;;;.18;.7;8;;.24;0;;;.18;-.18;;;0;-.34;;;-.18;-.18;;;-.24;0;;;-.18;.18;;;0;.34;;;.18;.18;;;0;;;;", 17, 0.57, "2;;;;0;.7;1;;0;-.99;;;0;.52;7;;.2;.18;;;.19;0;;;.18;-.18;;;0;-.34;;;-.18;-.18;;;-.19;0;;;-.2;.18;;;0;;;;", 18, 0.57, "2;;;;.57;.7;1;;0;-.99;;;.57;.52;7;;-.2;.18;;;-.19;0;;;-.18;-.18;;;0;-.34;;;.18;-.18;;;.19;0;;;.2;.18;;;0;;;;", 19, 0.32, "2;;;;0;.7;1;;0;-.7;;;0;.55;2;;.17;.15;;;.15;0;;;0;;;;", 20, 0.49, "1;;;;.49;.6;11;;-.1;.1;;;-.28;0;;;-.1;-.1;;;0;-.15;;;.09;-.1;;;.29;0;;;.1;-.1;;;0;-.15;;;-.1;-.1;;;-.29;0;;;-.1;.1;;;0;;;;", 21, 0.32, "2;;;;.14;.91;3;;0;-.83;;;.08;-.08;;;.09;0;;;0;.7;1;;.32;0;;;0;;;;", 22, 0.54, "2;;;;.54;.7;1;;0;-.7;;;0;.7;4;;0;-.54;;;.16;-.16;;;.18;0;;;.2;.18;;;0;;;;", 23, 0.56, "1;;;;0;.7;2;;.28;-.7;;;.28;.7;;;0;;;;", 24, 0.92, "1;;;;0;.7;4;;.23;-.7;;;.23;.7;;;.23;-.7;;;.23;.7;;;0;;;;", 25, 0.54, "2;;;;0;.7;1;;.54;-.7;;;.54;.7;1;;-.54;-.7;;;0;;;;", 26, 0.59, "2;;;;.59;.7;3;;-.376;-.92;;;-.09;-.1;;;-.07;0;;;0;.7;1;;.31;-.7;;;0;;;;", 27, 0.55, "1;;;;0;.7;3;;.55;0;;;-.55;-.7;;;.55;0;;;0;;;;", 28, 0.77, "2;;;;0;0;2;;.385;1;;;.385;-1;;;.11165;.29;1;;.5467;0;;;0;;;;", 29, 0.69, "1;;;;0;.52;10;;.49;0;;;.2;-.17;;;0;-.2;;;-.15;-.15;;;-.54;0;;;0;1;;;.49;0;;;.15;-.15;;;0;-.18;;;-.15;-.15;;;0;;;;", 30, 0.76, "1;;;;.76;.8;7;;-.2;.2;;;-.31;0;;;-.25;-.25;;;0;-.5;;;.25;-.25;;;.31;0;;;.2;.2;;;0;;;;", 31, 0.76, "1;;;;0;1;6;;.51;0;;;.25;-.25;;;0;-.5;;;-.25;-.25;;;-.51;0;;;0;1;;;0;;;;", 32, 0.6, "2;;;;.6;1;3;;-.6;0;;;0;-1;;;.6;0;;;0;.51;1;;.57;0;;;0;;;;", 33, 0.59, "2;;;;.59;1;2;;-.59;0;;;0;-1;;;0;.49;1;;.55;0;;;0;;;;", 34, 0.8, "1;;;;.8;.8;9;;-.2;.2;;;-.35;0;;;-.25;-.25;;;0;-.5;;;.25;-.25;;;.33;0;;;.22;.22;;;0;.24;;;-.33;0;;;0;;;;", 35, 0.75, "3;;;;0;1;1;;0;-1;;;.75;1;1;;0;-1;;;0;.51;1;;.75;0;;;0;;;;", 36, 0, "1;;;;0;1;1;;0;-1;;;0;;;;", 37, 0.5, "1;;;;.5;1;4;;0;-.85;;;-.15;-.15;;;-.2;0;;;-.15;.15;;;0;;;;", 38, 0.66, "3;;;;0;1;1;;0;-1;;;.64;1;1;;-.64;-.64;;;.185;.545;1;;.475;-.545;;;0;;;;", 39, 0.6, "1;;;;0;1;2;;0;-1;;;.6;0;;;0;;;;", 40, 0.75, "1;;;;0;0;3;;0;1;;;.75;-1;;;0;1;;;0;;;;", 41, 0.92, "1;;;;0;0;4;;0;1;;;.46;-1;;;.46;1;;;0;-1;;;0;;;;", 42, 0.84, "1;;;;.25;1;8;;.34;0;;;.25;-.25;;;0;-.5;;;-.25;-.25;;;-.34;0;;;-.25;.25;;;0;.5;;;.25;.25;;;0;;;;", 43, 0.65, "1;;;;0;0;6;;0;1;;;.48;0;;;.17;-.17;;;0;-.24;;;-.17;-.17;;;-.48;0;;;0;;;;", 44, 0.84, "2;;;;.25;1;8;;.34;0;;;.25;-.25;;;0;-.5;;;-.25;-.25;;;-.34;0;;;-.25;.25;;;0;.5;;;.25;.25;;;.54;.22;1;;.26;-.32;;;0;;;;", 45, 0.68, "2;;;;0;0;6;;0;1;;;.5;0;;;.16;-.16;;;0;-.21;;;-.2;-.17;;;-.46;0;;;.46;.46;1;;.22;-.46;;;0;;;;", 46, 0.65, "1;;;;.64;.85;11;;-.15;.15;;;-.32;0;;;-.15;-.15;;;0;-.19;;;.15;-.15;;;.33;0;;;.15;-.15;;;0;-.21;;;-.15;-.15;;;-.35;0;;;-.15;.15;;;0;;;;", 47, 0.7, "2;;;;0;1;1;;.7;0;;;.35;1;1;;0;-1;;;0;;;;", 48, 0.74, "1;;;;0;1;5;;0;-.78;;;.22;-.22;;;.3;0;;;.22;.22;;;0;.78;;;0;;;;", 49, 0.76, "1;;;;0;1;2;;.38;-1;;;.38;1;;;0;;;;", 50, 1.08, "1;;;;0;1;4;;.27;-1;;;.27;1;;;.27;-1;;;.27;1;;;0;;;;", 51, 0.74, "2;;;;0;1;1;;.74;-1;;;.74;1;1;;-.74;-1;;;0;;;;", 52, 0.74, "2;;;;0;1;2;;.37;-.54;;;.37;.54;;;.37;.46;1;;0;-.46;;;0;;;;", 53, 0.71, "1;;;;.01;1;3;;.69;0;;;-.7;-1;;;.71;0;;;0;;;;", 54, 0.62, "1;;;;.18;1;8;;.26;0;;;.18;-.18;;;0;-.64;;;-.18;-.18;;;-.26;0;;;-.18;.18;;;0;.64;;;.18;.18;;;0;;;;", 55, 0.4, "1;;;;0;.8;2;;.3;.2;;;0;-1;;;0;;;;", 56, 0.6, "1;;;;0;.83;6;;.17;.17;;;.26;0;;;.17;-.17;;;0;-.23;;;-.6;-.6;;;.6;0;;;0;;;;", 57, 0.62, "2;;;;.02;.85;5;;.15;.15;;;.27;0;;;.15;-.15;;;0;-.19;;;-.15;-.15;;;.23;.51;6;;.21;0;;;.18;-.16;;;0;-.2;;;-.15;-.15;;;-.32;0;;;-.15;.15;;;0;;;;", 58, 0.7, "1;;;;.54;0;3;;0;1;;;-.54;-.75;;;.7;0;;;0;;;;", 59, 0.61, "1;;;;.56;1;9;;-.4975;0;;;-.0425;-.51;;;.2;.12;;;.21;0;;;.18;-.18;;;0;-.25;;;-.18;-.18;;;-.25;0;;;-.18;.18;;;0;;;;", 60, 0.64, "1;;;;.62;.86;12;;-.14;.14;;;-.23;0;;;-.15;-.1;;;-.1;-.26;;;0;-.41;;;.18;-.23;;;.28;0;;;.18;.18;;;0;.24;;;-.18;.18;;;-.26;0;;;-.2;-.18;;;0;;;;", 61, 0.62, "1;;;;0;1;2;;.62;0;;;-.5;-1;;;0;;;;", 62, 0.63, "1;;;;.46;.52;15;;.135;.14;;;0;.2;;;-.14;.14;;;-.28;0;;;-.14;-.14;;;0;-.2;;;.135;-.14;;;.29;0;;;.17;-.15;;;0;-.22;;;-.15;-.15;;;-.33;0;;;-.15;.15;;;0;.22;;;.17;.15;;;0;;;;", 63, 0.64, "1;;;;.02;.14;12;;.14;-.14;;;.23;0;;;.15;.1;;;.1;.24;;;0;.43;;;-.18;.23;;;-.28;0;;;-.18;-.18;;;0;-.24;;;.18;-.18;;;.26;0;;;.2;.18;;;0;;;;", 64, 0, "1;;;;0;1;1;;0;-.67;;;1;;;;0;0;;;", 65, 1.06, "2;;;;.73;.51;7;;-.14;.12;;;-.15;0;;;-.12;-.12;;;0;-.27;;;.12;-.12;;;.19;0;;;.1;.1;;;.73;.63;11;;0;-.41;;;.1;-.1;;;.13;0;;;.1;.1;;;0;.42;;;-.31;.31;;;-.44;0;;;-.31;-.31;;;0;-.53;;;.31;-.31;;;.45;0;;;0;;;;", 66, 0.8, "4;;;;.32;1;1;;-.2;-1;;;.68;1;1;;-.2;-1;;;.08;.7;1;;.72;0;;;0;.3;1;;.72;0;;;0;;;;", 67, 0.63, "2;;;;.63;.85;11;;-.15;.15;;;-.32;0;;;-.15;-.15;;;0;-.19;;;.15;-.15;;;.32;0;;;.15;-.15;;;0;-.21;;;-.15;-.15;;;-.33;0;;;-.15;.15;;;.32;1.13;1;;0;-1.26;;;0;;;;", 68, 0.96, "3;;;;.11;0;1;;.74;1;;;.1;1;8;;.14;0;;;.1;-.1;;;0;-.2;;;-.1;-.1;;;-.14;0;;;-.1;.1;;;0;.2;;;.1;.1;;;.72;.4;8;;.14;0;;;.1;-.1;;;0;-.2;;;-.1;-.1;;;-.14;0;;;-.1;.1;;;0;.2;;;.1;.1;;;0;;;;", 69, 0.46, "1;;;;0;.56;2;;.23;.44;;;.23;-.44;;;0;;;;", 70, 0.82, "1;;;;.82;0;15;;-.7;.7;;;0;.18;;;.12;.12;;;.18;0;;;.12;-.12;;;0;-.17;;;-.1;-.1;;;-.32;-.13;;;-.12;-.12;;;0;-.21;;;.15;-.15;;;.25;0;;;.15;.06;;;.19;.24;;;.035;.21;;;0;;;;", 71, 0.43301, "3;;;;.21651;1;1;;0;-.5;;;0;.875;1;;.43301;-.25;;;0;.625;1;;.43301;.25;;;0;;;;", 72, 0.18, "1;;;;.18;1;3;;-.18;-.32;;;0;-.61;;;.18;-.31;;;0;;;;", 73, 0.18, "1;;;;0;1;3;;.18;-.32;;;0;-.61;;;-.18;-.31;;;0;;;;", 74, 0.38, "1;;;;0;.36;1;;.38;0;;;0;;;;", 75, 0.6, "1;;;;0;.36;1;;.6;0;;;0;;;;", 76, 1.2, "1;;;;0;.36;1;;1.2;0;;;0;;;;", 77, 0.62, "2;;;;0;.505;1;;.62;0;;;0;.215;1;;.62;0;;;0;;;;", 78, 0.22, "1;;;;.22;1;3;;-.22;0;;;0;-1.2;;;.22;0;;;0;;;;", 79, 0.22, "1;;;;0;1;3;;.22;0;;;0;-1.2;;;-.22;0;;;0;;;;", 80, 0.315, "1;;;;0;1;1;;.315;-1.26;;;0;;;;", 81, 0, "1;;;;0;.05;1;;-.06;-.25;;;1;;;;0;.6;;;", 82, 0, "1;;;;0;1;1;;0;-.3;;;0;;;;", 83, 0.075, "1;;;;0;1;1;;.075;-.3;;;0;;;;", 84, 0.075, "1;;;;.075;1;1;;-.075;-.3;;;0;;;;", 85, 0, "1;;;;0;.05;1;;-.06;-.25;;;0;;;;", 86, 0, "0;;;;1;;;;0;0;;;", 87, 0.315, "1;;;;0;-.26;1;;.315;1.26;;;0;;;;", 88, 0.64, "1;;;;0;-.2;1;;.64;0;;;0;;;;", 89, 0.64, "2;;;;.32;.68;1;;0;-.64;;;0;.36;1;;.64;0;;;0;;;;", 90, 0.33, "1;;;;.33;1.06;8;;-.1;0;;;-.1;-.1;;;0;-.44;;;-.13;-.13;;;.13;-.13;;;0;-.44;;;.1;-.1;;;.1;0;;;0;;;;", 91, 0.33, "1;;;;0;1.06;8;;.1;0;;;.1;-.1;;;0;-.44;;;.13;-.13;;;-.13;-.13;;;0;-.44;;;-.1;-.1;;;-.1;0;;;0;;;;", 92, 0, "1;;;;0;1;1;;0;-1.26;;;0;;;;", 93, 0, "0;;;;2;;;;0;.6;;;0;0;;;", 94, 0.27, "2;;;;0;1;1;;0;-.3;;;.27;1;1;;0;-.3;;;0;;;;", 95, 0.355, "2;;;;0;1;1;;.075;-.3;;;.28;1;1;;.075;-.3;;;0;;;;", 96, 0.355, "2;;;;.075;1;1;;-.075;-.3;;;.355;1;1;;-.075;-.3;;;0;;;;", 97, 0.6, "1;;;;.6;.74;2;;-.6;-.36;;;.6;-.36;;;0;;;;", 98, 0.6, "1;;;;0;.74;2;;.6;-.36;;;-.6;-.36;;;0;;;;", 99, 0.56, "1;;;;0;.84;6;;.16;.16;;;.24;0;;;.16;-.16;;;0;-.24;;;-.3;-.19;;;0;-.1;;;1;;;;.26;0;;;", 100, 0.2, "1;;;;0;1.13;1;;.2;-.23;;;0;;;;", 101, 0.6, "1;;;;0;.4;5;;.08;.14;;;.12;0;;;.2;-.16;;;.12;0;;;.08;.14;;;0;;;;", 102, 0.58, "3;;;;.58;.71;7;;-.14;.14;;;-.26;0;;;-.18;-.18;;;0;-.34;;;.18;-.18;;;.26;0;;;.14;.14;;;.31;1;1;;0;-.15;;;.31;.15;1;;0;-.15;;;0;;;;", 103, 0.7, "3;;;;.7;1;5;;-.3;0;;;-.25;-.25;;;0;-.5;;;.25;-.25;;;.3;0;;;0;.62;1;;.59;0;;;0;.38;1;;.59;0;;;0;;;;", 104, 0.7, "2;;;;.67;1;5;;-.33;0;;;-.21;-.21;;;.11;-.57;;;-.24;-.22;;;.7;0;;;0;.5;1;;.59;0;;;0;;;;", 105, 0.74, "4;;;;0;1;2;;.37;-.54;;;.37;.54;;;.37;.46;1;;0;-.46;;;.15;.42;1;;.44;0;;;.15;.2;1;;.44;0;;;0;;;;", 106, 0.38, "1;;;;.11;1;8;;.16;0;;;.11;-.11;;;0;-.16;;;-.11;-.11;;;-.16;0;;;-.11;.11;;;0;.16;;;.11;.11;;;0;;;;", 107, 0.075, "1;;;;.075;1;1;;-.075;-.3;;;0;;;;", 108, 0.355, "2;;;;.075;1;1;;-.075;-.3;;;.355;1;1;;-.075;-.3;;;0;;;;", 109, 0.62, "3;;;;0;.505;1;;.62;0;;;0;.215;1;;.62;0;;;.18;.03;1;;.26;.64;;;0;;;;", 110, 0.6, "2;;;;0;.1;1;;.6;0;;;.6;.74;2;;-.6;-.21;;;.6;-.21;;;0;;;;", 111, 0.6, "2;;;;0;.1;1;;.6;0;;;0;.74;2;;.6;-.21;;;-.6;-.21;;;0;;;;", 112, 0.48, "2;;;;0;.6;1;;.48;-.48;;;.48;.6;1;;-.48;-.48;;;0;;;;", 113, 0.1, "0;;;;1;;;;.05;.36;;;", 114, 0.6, "1;;;;0;.36;1;;.6;0;;;2;;;;.3;.62;;;.3;.1;;;", 115, 0.6, "3;;;;0;.1;1;;.6;0;;;0;.48;1;;.6;0;;;.3;.67;1;;0;-.38;;;0;;;;", "Angular_1592695976827", 103, 1, 0.5, "0;;;;0;;;;", 2, 0.5, "1;;;;.1;.6;5;;.4;0;;;0;-.6;;;-.5;0;;;0;.3;;;.5;0;;;0;;;;", 3, 0.5, "1;;;;0;1.1;4;;0;-1.1;;;.5;0;;;0;.6;;;-.5;0;;;0;;;;", 4, 0.5, "1;;;;.5;.6;3;;-.5;0;;;0;-.6;;;.5;0;;;0;;;;", 5, 0.5, "1;;;;.5;1.1;4;;0;-1.1;;;-.5;0;;;0;.6;;;.5;0;;;0;;;;", 6, 0.5, "1;;;;0;.3;5;;.5;0;;;0;.3;;;-.5;0;;;0;-.6;;;.4;0;;;0;;;;", 7, 0.3, "2;;;;.3;1.1;2;;-.15;-.15;;;0;-.95;;;0;.6;1;;.3;0;;;0;;;;", 8, 0.5, "1;;;;.5;0;5;;-.5;0;;;0;.6;;;.5;0;;;0;-.9;;;-.4;0;;;0;;;;", 9, 0.5, "2;;;;0;1.1;1;;0;-1.1;;;0;.6;2;;.5;0;;;0;-.6;;;0;;;;", 10, 0, "1;;;;0;.6;1;;0;-.6;;;1;;;;0;1;;;", 11, 0, "1;;;;0;.6;2;;0;-.75;;;-.15;-.15;;;1;;;;0;1;;;", 12, 0.4, "2;;;;0;1.1;1;;0;-1.1;;;.4;.6;2;;-.4;-.3;;;.4;-.3;;;0;;;;", 13, 0, "1;;;;0;1.1;1;;0;-1.1;;;0;;;;", 14, 0.8, "2;;;;0;0;3;;0;.6;;;.8;0;;;0;-.6;;;.4;.6;1;;0;-.6;;;0;;;;", 15, 0.5, "1;;;;0;0;4;;0;.6;;;.35;0;;;.15;-.15;;;0;-.45;;;0;;;;", 16, 0.5, "1;;;;0;.6;4;;.5;0;;;0;-.6;;;-.5;0;;;0;.6;;;0;;;;", 17, 0.5, "1;;;;0;0;4;;.5;0;;;0;.6;;;-.5;0;;;0;-.9;;;0;;;;", 18, 0.5, "1;;;;.5;0;4;;-.5;0;;;0;.6;;;.5;0;;;0;-.9;;;0;;;;", 19, 0.3, "1;;;;0;0;3;;0;.45;;;.15;.15;;;.15;0;;;0;;;;", 20, 0.5, "1;;;;.5;.6;5;;-.5;0;;;0;-.3;;;.5;0;;;0;-.3;;;-.5;0;;;0;;;;", 21, 0.3, "2;;;;.15;.9;1;;0;-.9;;;0;.6;1;;.3;0;;;0;;;;", 22, 0.5, "1;;;;.5;.6;4;;0;-.6;;;-.35;0;;;-.15;.15;;;0;.45;;;0;;;;", 23, 0.5, "1;;;;0;.6;2;;.25;-.6;;;.25;.6;;;0;;;;", 24, 0.9, "1;;;;0;.6;4;;.225;-.6;;;.225;.6;;;.225;-.6;;;.225;.6;;;0;;;;", 25, 0.5, "2;;;;0;.6;1;;.5;-.6;;;.5;.6;1;;-.5;-.6;;;0;;;;", 26, 0.5, "2;;;;.5;.6;1;;-.375;-.9;;;0;.6;1;;.25;-.6;;;0;;;;", 27, 0.5, "1;;;;0;.6;3;;.5;0;;;-.5;-.6;;;.5;0;;;0;;;;", 28, 0.8, "2;;;;0;0;2;;.4;1;;;.4;-1;;;.12;.3;1;;.56;0;;;0;;;;", 29, 0.85, "1;;;;0;.5;6;;.85;0;;;0;-.5;;;-.85;0;;;0;1;;;.65;0;;;0;-.5;;;0;;;;", 30, 0.8, "1;;;;.8;1;5;;-.5;0;;;-.3;-.3;;;0;-.4;;;.3;-.3;;;.5;0;;;0;;;;", 31, 0.85, "1;;;;0;1;5;;.55;0;;;.3;-.3;;;0;-.7;;;-.85;0;;;0;1;;;0;;;;", 32, 0.8, "2;;;;.8;1;3;;-.8;0;;;0;-1;;;.8;0;;;0;.5;1;;.8;0;;;0;;;;", 33, 0.8, "2;;;;.8;1;2;;-.8;0;;;0;-1;;;0;.5;1;;.8;0;;;0;;;;", 34, 0.8, "1;;;;.8;1;5;;-.8;0;;;0;-1;;;.8;0;;;0;.5;;;-.35;0;;;0;;;;", 35, 0.8, "3;;;;0;1;1;;0;-1;;;.8;1;1;;0;-1;;;0;.5;1;;.8;0;;;0;;;;", 36, 0.4, "3;;;;.2;1;1;;0;-1;;;0;1;1;;.4;0;;;0;0;1;;.4;0;;;0;;;;", 37, 0.6, "1;;;;.6;1;3;;0;-.75;;;-.25;-.25;;;-.35;0;;;0;;;;", 38, 0.7, "2;;;;0;1;1;;0;-1;;;.7;1;2;;-.7;-.5;;;.7;-.5;;;0;;;;", 39, 0.8, "1;;;;0;1;2;;0;-1;;;.8;0;;;0;;;;", 41, 1, "1;;;;0;0;4;;0;1;;;.5;-1;;;.5;1;;;0;-1;;;0;;;;", 40, 0.8, "1;;;;0;0;3;;0;1;;;.8;-1;;;0;1;;;0;;;;", 42, 1, "1;;;;.3;1;8;;.4;0;;;.3;-.3;;;0;-.4;;;-.3;-.3;;;-.4;0;;;-.3;.3;;;0;.4;;;.3;.3;;;0;;;;", 43, 0.8, "1;;;;0;0;4;;0;1;;;.8;0;;;0;-.5;;;-.8;0;;;0;;;;", 44, 1, "2;;;;.3;1;8;;.4;0;;;.3;-.3;;;0;-.4;;;-.3;-.3;;;-.4;0;;;-.3;.3;;;0;.4;;;.3;.3;;;.7;.3;1;;.3;-.3;;;0;;;;", 45, 0.8, "2;;;;0;0;4;;0;1;;;.8;0;;;0;-.5;;;-.8;0;;;.55;.5;1;;.25;-.5;;;0;;;;", 46, 0.8, "1;;;;.8;1;7;;-.65;0;;;-.15;-.3;;;.2;-.2;;;.4;0;;;.2;-.2;;;-.15;-.3;;;-.65;0;;;0;;;;", 47, 0.8, "2;;;;.4;1;1;;0;-1;;;0;1;1;;.8;0;;;0;;;;", 48, 0.8, "1;;;;0;1;5;;0;-.75;;;.25;-.25;;;.3;0;;;.25;.25;;;0;.75;;;0;;;;", 49, 0.8, "1;;;;0;1;2;;.4;-1;;;.4;1;;;0;;;;", 50, 1, "1;;;;0;1;4;;.25;-1;;;.25;1;;;.25;-1;;;.25;1;;;0;;;;", 51, 0.8, "2;;;;0;1;1;;.8;-1;;;.8;1;1;;-.8;-1;;;0;;;;", 52, 0.8, "2;;;;.4;.45;1;;0;-.45;;;0;1;2;;.4;-.55;;;.4;.55;;;0;;;;", 53, 0.8, "1;;;;0;1;3;;.8;0;;;-.8;-1;;;.8;0;;;0;;;;", 54, 0.6, "2;;;;0;1;4;;.6;0;;;0;-1;;;-.6;0;;;0;1;;;0;.2;1;;.6;.6;;;0;;;;", 55, 0.45, "1;;;;0;.85;2;;.3;.15;;;0;-1;;;0;;;;", 56, 0.6, "1;;;;0;1;4;;.4;0;;;.2;-.3;;;-.6;-.7;;;.6;0;;;0;;;;", 57, 0.6, "2;;;;0;1;3;;.6;0;;;0;-1;;;-.6;0;;;.6;.5;1;;-.4;0;;;0;;;;", 58, 0.7, "1;;;;.55;0;3;;0;1;;;-.55;-.7;;;.7;0;;;0;;;;", 59, 0.6, "1;;;;.6;1;7;;-.6;0;;;0;-.5;;;.45;0;;;.15;-.15;;;0;-.2;;;-.15;-.15;;;-.45;0;;;0;;;;", 60, 0.6, "1;;;;.6;1;5;;-.6;0;;;0;-1;;;.6;0;;;0;.5;;;-.6;0;;;0;;;;", 61, 0.65, "1;;;;0;1;2;;.65;0;;;-.47;-1;;;0;;;;", 62, 0.6, "1;;;;0;.5;6;;0;.5;;;.6;0;;;0;-1;;;-.6;0;;;0;.5;;;.6;0;;;0;;;;", 63, 0.6, "1;;;;0;0;5;;.6;0;;;0;1;;;-.6;0;;;0;-.5;;;.6;0;;;0;;;;", 64, 0, "1;;;;0;1;1;;0;-.7;;;1;;;;0;0;;;", 65, 1, "1;;;;.7;.3;8;;0;.4;;;-.4;0;;;0;-.4;;;.7;0;;;0;.7;;;-1;0;;;0;-1;;;1;0;;;0;;;;", 66, 0.6, "4;;;;.15;.95;1;;0;-.9;;;.45;.95;1;;0;-.9;;;0;.65;1;;.6;0;;;0;.35;1;;.6;0;;;0;;;;", 67, 0.8, "2;;;;.8;1;7;;-.65;0;;;-.15;-.3;;;.2;-.2;;;.4;0;;;.2;-.2;;;-.15;-.3;;;-.65;0;;;.4;1.15;1;;0;-1.3;;;0;;;;", 68, 1, "3;;;;0;0;1;;1;1;;;0;1;4;;.35;0;;;0;-.35;;;-.35;0;;;0;.35;;;.65;.35;4;;.35;0;;;0;-.35;;;-.35;0;;;0;.35;;;0;;;;", 69, 0.5, "1;;;;0;.7;2;;.25;.3;;;.25;-.3;;;0;;;;", 70, 1, "1;;;;1;0;8;;-.9;.8;;;.1;.2;;;.3;0;;;.1;-.2;;;-.6;-.5;;;.1;-.3;;;.5;0;;;.4;.45;;;0;;;;", 71, 0.5, "3;;;;.25;1;1;;0;-.5;;;0;.9;1;;.5;-.3;;;.5;.9;1;;-.5;-.3;;;0;;;;", 72, 0.3, "1;;;;.3;1.15;3;;-.3;-.3;;;0;-.7;;;.3;-.3;;;0;;;;", 73, 0.3, "1;;;;0;1.15;3;;.3;-.3;;;0;-.7;;;-.3;-.3;;;0;;;;", 74, 0.5, "1;;;;0;.4;1;;.5;0;;;0;;;;", 77, 0.5, "2;;;;0;.55;1;;.5;0;;;0;.25;1;;.5;0;;;0;;;;", 78, 0.3, "1;;;;.3;1.15;3;;-.3;0;;;0;-1.3;;;.3;0;;;0;;;;", 79, 0.3, "1;;;;0;1.15;3;;.3;0;;;0;-1.3;;;-.3;0;;;0;;;;", 80, 0.4, "1;;;;0;1.15;1;;.4;-1.3;;;0;;;;", 81, 0, "1;;;;0;.05;1;;-.05;-.2;;;1;;;;0;.5;;;", 82, 0, "1;;;;0;1.05;1;;0;-.25;;;0;;;;", 85, 0, "1;;;;0;.05;1;;-.05;-.2;;;0;;;;", 86, 0, "0;;;;1;;;;0;0;;;", 87, 0.4, "1;;;;0;-.15;1;;.4;1.3;;;0;;;;", 88, 0.8, "1;;;;0;-.15;1;;.8;0;;;0;;;;", 89, 0.5, "2;;;;0;.4;1;;.5;0;;;.25;.65;1;;0;-.5;;;0;;;;", 90, 0.3, "1;;;;.3;1.15;6;;-.15;-.15;;;0;-.35;;;-.15;-.15;;;.15;-.15;;;0;-.35;;;.15;-.15;;;0;;;;", 91, 0.3, "1;;;;0;1.15;6;;.15;-.15;;;0;-.35;;;.15;-.15;;;-.15;-.15;;;0;-.35;;;-.15;-.15;;;0;;;;", 92, 0, "1;;;;0;1.15;1;;0;-1.3;;;0;;;;", 93, 0, "0;;;;2;;;;0;.5;;;0;0;;;", 94, 0.2, "2;;;;0;1.05;1;;0;-.25;;;.2;1.05;1;;0;-.25;;;0;;;;", 97, 0.5, "1;;;;.5;.6;2;;-.5;-.2;;;.5;-.2;;;0;;;;", 98, 0.5, "1;;;;0;.6;2;;.5;-.2;;;-.5;-.2;;;0;;;;", 99, 0.6, "1;;;;0;1;3;;.4;0;;;.2;-.3;;;-.3;-.4;;;1;;;;.3;0;;;", 100, 0.2, "1;;;;0;1.1;1;;.2;-.2;;;0;;;;", 101, 0.6, "1;;;;0;.3;3;;.12;.2;;;.36;-.2;;;.12;.2;;;0;;;;", 103, 0.8, "3;;;;.8;1;3;;-.6;0;;;0;-1;;;.6;0;;;0;.62;1;;.7;0;;;0;.38;1;;.7;0;;;0;;;;", 104, 0.75, "2;;;;.7;1;5;;-.35;0;;;-.15;-.15;;;0;-.6;;;-.2;-.25;;;.75;0;;;0;.5;1;;.65;0;;;0;;;;", 83, 0, "1;;;;0;.85;1;;.05;.2;;;0;;;;", 84, 0, "1;;;;0;1.05;1;;-.05;-.2;;;0;;;;", 95, 0.2, "2;;;;0;.85;1;;.05;.2;;;.2;.85;1;;.05;.2;;;0;;;;", 96, 0.2, "2;;;;0;1.05;1;;-.05;-.2;;;.2;1.05;1;;-.05;-.2;;;0;;;;", 107, 0.05, "1;;;;.05;1.05;1;;-.05;-.25;;;0;;;;", 108, 0.25, "2;;;;.05;1.05;1;;-.05;-.25;;;.25;1.05;1;;-.05;-.25;;;0;;;;"]
        )
        self.listchIndex = List(
            [2, 28, 54, 80, 106, 132, 158, 184, 210, 236, 262, 288, 314, 340, 366, 392, 418, 444, 470, 496, 522, 548, 574, 600, 626, 652, 678, 704, 730, 756, 782, 808, 834, 860, 886, 912, 938, 964, 990, 1016, 1042, 1068, 1094, 1120, 1146, 1172, 1198, 1224, 1250, 1276, 1302, 1328, 1354, 1380, 1406, 1432, 1458, 1484, 1510, 1536, 1562, 1588, 1614, 1640, 1666, 1692, 1718, 1744, 1770, 1796, 1822, 1848, 1874, 1900, 1926, 1952, 1978, 2004, 2030, 2056, 2082, 2108, 2134, 2160, 2186, 2212, 2238, 2264, 2290, 2316, 2342, 2368, 2394, 2420, 2446, 2472, 2498, 2524, 2550, 2576, 2602, 2628, 2654, 2680, 2706, 2732, 2758, 2784, 2810, 2836, 2862, 2888, 2914, 2940, 2966]
        )
        self.listchWidth = List(
            [0.2, 0.52, 0.57, 0.55, 0.57, 0.57, 0.34, 0.57, 0.55, 0, 0, 0.47, 0, 0.96, 0.55, 0.6, 0.57, 0.57, 0.32, 0.49, 0.32, 0.54, 0.56, 0.92, 0.54, 0.59, 0.55, 0.77, 0.69, 0.76, 0.76, 0.6, 0.59, 0.8, 0.75, 0, 0.5, 0.66, 0.6, 0.75, 0.92, 0.84, 0.65, 0.84, 0.68, 0.65, 0.7, 0.74, 0.76, 1.08, 0.74, 0.74, 0.71, 0.62, 0.4, 0.6, 0.62, 0.7, 0.61, 0.64, 0.62, 0.63, 0.64, 0, 1.06, 0.8, 0.63, 0.96, 0.46, 0.82, 0.43301, 0.18, 0.18, 0.38, 0.6, 1.2, 0.62, 0.22, 0.22, 0.315, 0, 0, 0.075, 0.075, 0, 0, 0.315, 0.64, 0.64, 0.33, 0.33, 0, 0, 0.27, 0.355, 0.355, 0.6, 0.6, 0.56, 0.2, 0.6, 0.58, 0.7, 0.7, 0.74, 0.38, 0.075, 0.355, 0.62, 0.6, 0.6, 0.48, 0.1, 0.6, 0.6]
        )
        self.listchData0 = List(
            ["__", 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.04, 0.1, 0.26, 0.12, 0, 0.52, -0.4, -0.12, 0, 0.12, 0.25, 0.15, 0, "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0, 0, 0.2, 0.19, 0.18, 0, -0.18, -0.19, -0.2, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.55, -0.14, -0.23, -0.18, 0, 0.18, 0.23, 0.14, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.57, 0, 0.57, -0.2, -0.19, -0.18, 0, 0.18, 0.19, 0.2, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.57, 0, -0.18, -0.21, -0.18, 0, 0.18, 0.24, 0.11, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.34, -0.1, -0.1, 0, 0, 0.325, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.57, 0, -0.14, -0.29, -0.1, 0.57, -0.2, -0.19, -0.18, 0, 0.18, 0.19, 0.2, 0, "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0, 0, 0.2, 0.2, 0.17, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0, 1, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0, -0.075, -0.075, 1, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 3, 0, 0, 0.45, -0.45, 0.125, 0.345, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 3, 0, 0, 0, 0.18, 0.16, 0.14, 0, 0.48, 0.16, 0.18, 0.14, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0, 0, 0.2, 0.18, 0.17, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.18, 0.24, 0.18, 0, -0.18, -0.24, -0.18, 0, 0.18, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0, 0, 0.2, 0.19, 0.18, 0, -0.18, -0.19, -0.2, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.57, 0, 0.57, -0.2, -0.19, -0.18, 0, 0.18, 0.19, 0.2, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0, 0, 0.17, 0.15, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.49, -0.1, -0.28, -0.1, 0, 0.09, 0.29, 0.1, 0, -0.1, -0.29, -0.1, 0, "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.14, 0, 0.08, 0.09, 0, 0.32, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.54, 0, 0, 0, 0.16, 0.18, 0.2, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.28, 0.28, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.23, 0.23, 0.23, 0.23, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0.54, 0.54, -0.54, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.59, -0.376, -0.09, -0.07, 0, 0.31, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.55, -0.55, 0.55, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0.385, 0.385, 0.11165, 0.5467, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.49, 0.2, 0, -0.15, -0.54, 0, 0.49, 0.15, 0, -0.15, 0, "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.76, -0.2, -0.31, -0.25, 0, 0.25, 0.31, 0.2, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.51, 0.25, 0, -0.25, -0.51, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.6, -0.6, 0, 0.6, 0, 0.57, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.59, -0.59, 0, 0, 0.55, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.8, -0.2, -0.35, -0.25, 0, 0.25, 0.33, 0.22, 0, -0.33, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 3, 0, 0, 0.75, 0, 0, 0.75, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0, 0, 0.3, 0, 0.3, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.5, 0, -0.15, -0.2, -0.15, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 3, 0, 0, 0.64, -0.64, 0.185, 0.475, 0, "L", 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0, 0.6, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0, 0.75, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0, 0.46, 0.46, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.25, 0.34, 0.25, 0, -0.25, -0.34, -0.25, 0, 0.25, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0, 0.48, 0.17, 0, -0.17, -0.48, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.25, 0.34, 0.25, 0, -0.25, -0.34, -0.25, 0, 0.25, 0.54, 0.26, 0, "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0, 0.5, 0.16, 0, -0.2, -0.46, 0.46, 0.22, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.64, -0.15, -0.32, -0.15, 0, 0.15, 0.33, 0.15, 0, -0.15, -0.35, -0.15, 0, "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0.7, 0.35, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0, 0.22, 0.3, 0.22, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.38, 0.38, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.27, 0.27, 0.27, 0.27, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0.74, 0.74, -0.74, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0.37, 0.37, 0.37, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.01, 0.69, -0.7, 0.71, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.18, 0.26, 0.18, 0, -0.18, -0.26, -0.18, 0, 0.18, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.3, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.17, 0.26, 0.17, 0, -0.6, 0.6, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.02, 0.15, 0.27, 0.15, 0, -0.15, 0.23, 0.21, 0.18, 0, -0.15, -0.32, -0.15, 0, "", "", "", "", "", "", "", "", "", "", "__", 1, 0.54, 0, -0.54, 0.7, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.56, -0.4975, -0.0425, 0.2, 0.21, 0.18, 0, -0.18, -0.25, -0.18, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.62, -0.14, -0.23, -0.15, -0.1, 0, 0.18, 0.28, 0.18, 0, -0.18, -0.26, -0.2, 0, "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.62, -0.5, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.46, 0.135, 0, -0.14, -0.28, -0.14, 0, 0.135, 0.29, 0.17, 0, -0.15, -0.33, -0.15, 0, 0.17, 0, "", "", "", "", "", "", "", "__", 1, 0.02, 0.14, 0.23, 0.15, 0.1, 0, -0.18, -0.28, -0.18, 0, 0.18, 0.26, 0.2, 0, "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0, 1, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.73, -0.14, -0.15, -0.12, 0, 0.12, 0.19, 0.1, 0.73, 0, 0.1, 0.13, 0.1, 0, -0.31, -0.44, -0.31, 0, 0.31, 0.45, 0, "", "", "", "__", 4, 0.32, -0.2, 0.68, -0.2, 0.08, 0.72, 0, 0.72, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.63, -0.15, -0.32, -0.15, 0, 0.15, 0.32, 0.15, 0, -0.15, -0.33, -0.15, 0.32, 0, 0, "", "", "", "", "", "", "", "", "", "__", 3, 0.11, 0.74, 0.1, 0.14, 0.1, 0, -0.1, -0.14, -0.1, 0, 0.1, 0.72, 0.14, 0.1, 0, -0.1, -0.14, -0.1, 0, 0.1, 0, "", "", "", "__", 1, 0, 0.23, 0.23, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.82, -0.7, 0, 0.12, 0.18, 0.12, 0, -0.1, -0.32, -0.12, 0, 0.15, 0.25, 0.15, 0.19, 0.035, 0, "", "", "", "", "", "", "", "__", 3, 0.21651, 0, 0, 0.43301, 0, 0.43301, 0, 0.14695, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.18, -0.18, 0, 0.18, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.18, 0, -0.18, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.38, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.6, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 1.2, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0.62, 0, 0.62, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.22, -0.22, 0, 0.22, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.22, 0, -0.22, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.315, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, -0.06, 1, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.075, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.075, -0.075, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, -0.06, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 0, 1, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.315, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.64, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.32, 0, 0, 0.64, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.33, -0.1, -0.1, 0, -0.13, 0.13, 0, 0.1, 0.1, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.1, 0.1, 0, 0.13, -0.13, 0, -0.1, -0.1, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 0, 2, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0, 0.27, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0.075, 0.28, 0.075, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.075, -0.075, 0.355, -0.075, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.6, -0.6, 0.6, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.6, -0.6, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.16, 0.24, 0.16, 0, -0.3, 0, 1, 0.26, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.2, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.08, 0.12, 0.2, 0.12, 0.08, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 3, 0.58, -0.14, -0.26, -0.18, 0, 0.18, 0.26, 0.14, 0.31, 0, 0.31, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "__", 3, 0.7, -0.3, -0.25, 0, 0.25, 0.3, 0, 0.59, 0, 0.59, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.67, -0.33, -0.21, 0.11, -0.24, 0.7, 0, 0.59, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 4, 0, 0.37, 0.37, 0.37, 0, 0.15, 0.44, 0.15, 0.44, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.11, 0.16, 0.11, 0, -0.11, -0.16, -0.11, 0, 0.11, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0.075, -0.075, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0.075, -0.075, 0.355, -0.075, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 3, 0, 0.62, 0, 0.62, 0.18, 0.26, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0.6, 0.6, -0.6, 0.6, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0.6, 0, 0.6, -0.6, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 2, 0, 0.48, 0.48, -0.48, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 0, 1, 0.05, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 1, 0, 0.6, 2, 0.3, 0.3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__", 3, 0, 0.6, 0, 0.6, 0.3, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "__"]
        )
        self.listchData1 = List(
            ["Geometric_1592695965870", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.6, 0.1, 0, -0.12, -0.58, 0.36, 0, -0.12, -0.12, -0.12, 0, 0.15, "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1.05, -1.05, 0.52, 0.18, 0, -0.18, -0.34, -0.18, 0, 0.18, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.56, 0.14, 0, -0.18, -0.34, -0.18, 0, 0.14, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1.05, -1.05, 0.52, 0.18, 0, -0.18, -0.34, -0.18, 0, 0.18, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.35, 0, 0.17, 0.18, 0, -0.18, -0.34, -0.18, 0, 0.1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1.05, 0, -0.1, -0.95, 0.7, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.7, -0.88, -0.14, 0, 0.1, 0.52, 0.18, 0, -0.18, -0.34, -0.18, 0, 0.18, "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1.05, -1.05, 0.52, 0.18, 0, -0.17, -0.53, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.7, -0.7, "", 1.03, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.7, -0.945, -0.075, 0, "", 1.03, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1.05, -1.05, 0.7, -0.45, 0.375, -0.375, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1.05, -1.05, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.7, -0.7, 0.56, 0.14, 0, -0.14, -0.56, 0.56, 0.14, 0, -0.14, -0.56, "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.7, -0.7, 0.52, 0.18, 0, -0.17, -0.53, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.7, 0, -0.18, -0.34, -0.18, 0, 0.18, 0.34, 0.18, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.7, -0.99, 0.52, 0.18, 0, -0.18, -0.34, -0.18, 0, 0.18, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.7, -0.99, 0.52, 0.18, 0, -0.18, -0.34, -0.18, 0, 0.18, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.7, -0.7, 0.55, 0.15, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.6, 0.1, 0, -0.1, -0.15, -0.1, 0, -0.1, -0.15, -0.1, 0, 0.1, "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.91, -0.83, -0.08, 0, 0.7, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.7, -0.7, 0.7, -0.54, -0.16, 0, 0.18, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.7, -0.7, 0.7, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.7, -0.7, 0.7, -0.7, 0.7, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.7, -0.7, 0.7, -0.7, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.7, -0.92, -0.1, 0, 0.7, -0.7, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.7, 0, -0.7, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0, 1, -1, 0.29, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.52, 0, -0.17, -0.2, -0.15, 0, 1, 0, -0.15, -0.18, -0.15, "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.8, 0.2, 0, -0.25, -0.5, -0.25, 0, 0.2, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, 0, -0.25, -0.5, -0.25, 0, 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, 0, -1, 0, 0.51, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, 0, -1, 0.49, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.8, 0.2, 0, -0.25, -0.5, -0.25, 0, 0.22, 0.24, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -1, 1, -1, 0.51, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -1, "", 0, 0, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -0.85, -0.15, 0, 0.15, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -1, 1, -0.64, 0.545, -0.545, "", 0.45, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -1, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0, 1, -1, 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0, 1, -1, 1, -1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, 0, -0.25, -0.5, -0.25, 0, 0.25, 0.5, 0.25, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0, 1, 0, -0.17, -0.24, -0.17, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, 0, -0.25, -0.5, -0.25, 0, 0.25, 0.5, 0.25, 0.22, -0.32, "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0, 1, 0, -0.16, -0.21, -0.17, 0, 0.46, -0.46, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.85, 0.15, 0, -0.15, -0.19, -0.15, 0, -0.15, -0.21, -0.15, 0, 0.15, "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, 0, 1, -1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -0.78, -0.22, 0, 0.22, 0.78, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -1, 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -1, 1, -1, 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -1, 1, -1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -0.54, 0.54, 0.46, -0.46, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, 0, -1, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, 0, -0.18, -0.64, -0.18, 0, 0.18, 0.64, 0.18, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.8, 0.2, -1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.83, 0.17, 0, -0.17, -0.23, -0.6, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.85, 0.15, 0, -0.15, -0.19, -0.15, 0.51, 0, -0.16, -0.2, -0.15, 0, 0.15, "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0, 1, -0.75, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, 0, -0.51, 0.12, 0, -0.18, -0.25, -0.18, 0, 0.18, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.86, 0.14, 0, -0.1, -0.26, -0.41, -0.23, 0, 0.18, 0.24, 0.18, 0, -0.18, "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, 0, -1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.52, 0.14, 0.2, 0.14, 0, -0.14, -0.2, -0.14, 0, -0.15, -0.22, -0.15, 0, 0.15, 0.22, 0.15, "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.14, -0.14, 0, 0.1, 0.24, 0.43, 0.23, 0, -0.18, -0.24, -0.18, 0, 0.18, "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -0.67, "", 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.51, 0.12, 0, -0.12, -0.27, -0.12, 0, 0.1, 0.63, -0.41, -0.1, 0, 0.1, 0.42, 0.31, 0, -0.31, -0.53, -0.31, 0, "", "", "", "", "Geometric_1592695965870", "", 1, -1, 1, -1, 0.7, 0, 0.3, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.85, 0.15, 0, -0.15, -0.19, -0.15, 0, -0.15, -0.21, -0.15, 0, 0.15, 1.13, -1.26, "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0, 1, 1, 0, -0.1, -0.2, -0.1, 0, 0.1, 0.2, 0.1, 0.4, 0, -0.1, -0.2, -0.1, 0, 0.1, 0.2, 0.1, "", "", "", "", "Geometric_1592695965870", "", 0.56, 0.44, -0.44, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0, 0.7, 0.18, 0.12, 0, -0.12, -0.17, -0.1, -0.13, -0.12, -0.21, -0.15, 0, 0.06, 0.24, 0.21, "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -0.5, 0.875, -0.25, 0.625, 0.25, "", -0.20225, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -0.32, -0.61, -0.31, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -0.32, -0.61, -0.31, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.36, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.36, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.36, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.505, 0, 0.215, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, 0, -1.2, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, 0, -1.2, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -1.26, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.05, -0.25, "", 0.6, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -0.3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -0.3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -0.3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.05, -0.25, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", "", 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", -0.26, 1.26, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", -0.2, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.68, -0.64, 0.36, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1.06, 0, -0.1, -0.44, -0.13, -0.13, -0.44, -0.1, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1.06, 0, -0.1, -0.44, -0.13, -0.13, -0.44, -0.1, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -1.26, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", "", 0.6, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -0.3, 1, -0.3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -0.3, 1, -0.3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -0.3, 1, -0.3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.74, -0.36, -0.36, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.74, -0.36, -0.36, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.84, 0.16, 0, -0.16, -0.24, -0.19, -0.1, "", 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1.13, -0.23, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.4, 0.14, 0, -0.16, 0, 0.14, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.71, 0.14, 0, -0.18, -0.34, -0.18, 0, 0.14, 1, -0.15, 0.15, -0.15, "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, 0, -0.25, -0.5, -0.25, 0, 0.62, 0, 0.38, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, 0, -0.21, -0.57, -0.22, 0, 0.5, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -0.54, 0.54, 0.46, -0.46, 0.42, 0, 0.2, 0, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, 0, -0.11, -0.16, -0.11, 0, 0.11, 0.16, 0.11, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -0.3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 1, -0.3, 1, -0.3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.505, 0, 0.215, 0, 0.03, 0.64, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.1, 0, 0.74, -0.21, -0.21, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.1, 0, 0.74, -0.21, -0.21, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.6, -0.48, 0.6, -0.48, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", "", 0.36, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.36, 0, "", 0.62, 0.1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Geometric_1592695965870", "", 0.1, 0, 0.48, 0, 0.67, -0.38, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "none"]
        )
        self.listchData2 = List(
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 4, "", "", "", "", 6, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 7, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 7, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 7, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 9, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 3, "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 4, "", "", "", "", 7, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 4, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 4, "", "", "", "", 4, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 4, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 8, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 7, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 7, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 2, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 11, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 3, "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 4, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 2, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 4, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 3, "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 2, "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 10, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 7, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 6, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 3, "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 2, "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 9, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 4, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", 1, "", "", -0.4, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 2, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 4, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 8, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 6, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 8, "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 6, "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 11, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 5, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 2, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 4, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 2, "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 8, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 2, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 6, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 5, "", "", "", "", "", 6, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 9, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 12, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 2, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 15, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 12, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 7, "", "", "", "", "", "", "", 11, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 11, "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 8, "", "", "", "", "", "", "", "", 8, "", "", "", "", "", "", "", "", "", "", "", "", "", "", 2, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 15, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 3, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 8, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 8, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 2, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 2, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 6, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 5, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 7, "", "", "", "", "", "", "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 5, "", "", "", "", "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 5, "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 2, "", "", 1, "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 8, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 2, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 2, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 1, "", 1, "", 1, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        )
        self.listww0 = List(
            []
        )
        self.listww1 = List(
            []
        )
        self.listww2 = List(
            []
        )
        self.listchData3 = List(
            ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        )

        self.sprite.layer = 7

    @warp
    async def mycalcWW(self, util, arg_text, arg_width, arg_firstWidth, arg_cspace, arg_spaceWidth):
        self.listww0.delete_all()
        self.listww1.delete_all()
        self.listww2.delete_all()
        self.vari3 = 1
        self.vari4 = 0
        self.vari5 = 0
        self.vari6 = 0
        self.vari7 = arg_firstWidth
        for _ in create_repeat(len(_ToString(arg_text))):
            if eq(letter_of(_ToString(arg_text), toNumber(self.vari3)), " "):
                if eq(self.vari4, 0):
                    if gt((toNumber(self.vari7) + (toNumber(self.vari5) - toNumber(arg_cspace))), arg_width):
                        self.listww0.insert(1, 1)
                        self.listww1.append(0)
                        self.listww2.append(0)
                        self.vari6 = 1
                    self.vari7 = toNumber(self.vari7) + (toNumber(self.vari5) - toNumber(arg_cspace))
                else:
                    if gt((toNumber(self.vari7) + (arg_spaceWidth + toNumber(self.vari5))), arg_width):
                        if gt(self.vari4, self.vari6):
                            self.listww1.append(self.vari7)
                            self.listww2.append(((toNumber(self.vari4) - toNumber(self.vari6)) - 1))
                        self.vari6 = self.vari4
                        self.vari7 = (toNumber(self.vari5) - toNumber(arg_cspace))
                    else:
                        self.vari7 = toNumber(self.vari7) + (arg_spaceWidth + toNumber(self.vari5))
                self.listww0.append(1)
                self.vari4 = len(self.listww0)
                self.vari5 = 0
            else:
                self.costume.switch("blank")
                self.costume.switch((letter_of(_ToString(arg_text), toNumber(self.vari3)) + "_"))
                self.vari9 = NumberToString((self.costume.number - 1))
                if gt(self.vari9, 0):
                    self.vari8 = self.listchWidth[ScratchStringToNumber(self.vari9)]
                    if gt((toNumber(self.vari5) + toNumber(self.vari8)), arg_width):
                        if gt(self.vari4, self.vari6):
                            self.listww1.append(self.vari7)
                            self.listww2.append(((toNumber(self.vari4) - toNumber(self.vari6)) - 1))
                        self.listww1.append((toNumber(self.vari5) - toNumber(arg_cspace)))
                        self.listww2.append((len(self.listww0) - toNumber(self.vari4)))
                        self.listww0.append(1)
                        self.vari4 = len(self.listww0)
                        self.vari5 = (toNumber(self.vari8) + toNumber(arg_cspace))
                        self.vari6 = self.vari4
                        self.vari7 = (-1 * (toNumber(arg_cspace) + arg_spaceWidth))
                    else:
                        self.vari5 = toNumber(self.vari5) + (toNumber(self.vari8) + toNumber(arg_cspace))
                    self.listww0.append(self.vari9)
            self.vari3 = toNumber(self.vari3) + 1
        if gt(len(self.listww0), self.vari6):
            if eq(self.vari4, 0):
                if gt((toNumber(self.vari7) + (toNumber(self.vari5) - toNumber(arg_cspace))), arg_width):
                    self.listww0.insert(1, 1)
                    self.listww1.append(0)
                    self.listww2.append(0)
                    self.vari6 = 1
                self.vari7 = toNumber(self.vari7) + (toNumber(self.vari5) - toNumber(arg_cspace))
            else:
                if gt((toNumber(self.vari7) + (arg_spaceWidth + toNumber(self.vari5))), arg_width):
                    if gt(self.vari4, self.vari6):
                        self.listww1.append(self.vari7)
                        self.listww2.append(((toNumber(self.vari4) - toNumber(self.vari6)) - 1))
                    self.vari6 = self.vari4
                    self.vari7 = (toNumber(self.vari5) - toNumber(arg_cspace))
                else:
                    self.vari7 = toNumber(self.vari7) + (arg_spaceWidth + toNumber(self.vari5))
            self.listww1.append(self.vari7)
            self.listww2.append((len(self.listww0) - toNumber(self.vari6)))

    @on_green_flag
    async def green_flag(self, util):
        self.pen.up()
        await self.my_LoadFont(util, "Geometric")
        self.shown = False
        self.costume.switch("blank")
        self.costume.size = 100000
        self.costume.switch(" _")
        self.gotoxy(0, 0)
        self.direction = 90
        self.costume.rotation_style = 'don\'t rotate'

    @warp
    async def my_ClearCharacterData(self, util, ):
        self.costume.switch("blank")
        self.costume.switch((self.costume.number - 1))
        if gt((self.costume.number - 1), len(self.listchIndex)):
            self.vari0 = (self.costume.number - 1)
        else:
            self.vari0 = len(self.listchIndex)
        self.listchIndex.delete_all()
        self.listchWidth.delete_all()
        self.listchData0.delete_all()
        self.listchData1.delete_all()
        self.listchData2.delete_all()
        self.listchData3.delete_all()
        for _ in create_repeat(toNumber(self.vari0)):
            self.listchData0.append("__")
            self.listchData1.append("none")
            self.listchData2.append("")
            self.listchData3.append("")
            self.listchIndex.append((len(self.listchData0) + 1))
            self.listchWidth.append((1 * 0))
            for _ in create_repeat(25):
                self.listchData0.append("")
                self.listchData1.append("")
                self.listchData2.append("")
                self.listchData3.append("")
        self.listchData0.append("__")
        self.listchData1.append("none")
        self.listchData2.append("")
        self.listchData3.append("")

    @warp
    async def my_LoadFont(self, util, arg_fontName):
        self.vari0 = self.listfontName.index(arg_fontName)
        if lt(self.vari0, 1):
            return None
        self.vari0 = self.listfontIndex[toNumber(self.vari0)]
        self.vari1 = self.listfontData[toNumber(self.vari0)]
        self.vari0 = toNumber(self.vari0) + 2
        for _ in create_repeat(toNumber(self.listfontData[(toNumber(self.vari0) - 1)])):
            self.vari2 = self.listfontData[toNumber(self.vari0)]
            self.listchWidth[toNumber(self.vari2)] = self.listfontData[(toNumber(self.vari0) + 1)]
            self.vari3 = self.listchIndex[toNumber(self.vari2)]
            if not eq(self.listchData1[(toNumber(self.vari3) - 1)], self.vari1):
                self.listchData1[(toNumber(self.vari3) - 1)] = self.vari1
                self.listchData2[(toNumber(self.vari3) - 1)] = ""
                self.listchData3[(toNumber(self.vari3) - 1)] = ""
                await self.myunpackDef(util, self.vari2, self.vari3, self.listfontData[(toNumber(self.vari0) + 2)])
            self.vari0 = toNumber(self.vari0) + 3

    @warp
    async def my_SetPenColorRGBA(self, util, arg_R, arg_G, arg_B, arg_A):
        self.pen.exact_color((_round(arg_B) + (256 * (_round(arg_G) + (256 * (_round(arg_R) + (256 * _round(arg_A))))))))

    @warp
    async def myunpackDef(self, util, arg_id, arg_idx, arg_d):
        self.vari5 = len(_ToString(arg_d))
        self.vari6 = arg_idx
        self.vari7 = 1
        self.vari8 = 0
        while not gt(self.vari7, self.vari5):
            if eq(self.listchData0[toNumber(self.vari6)], "__"):
                self.listchData0.insert(toNumber(self.vari6), "")
                self.listchData1.insert(toNumber(self.vari6), "")
                self.listchData2.insert(toNumber(self.vari6), "")
                self.listchData3.insert(toNumber(self.vari6), "")
                self.vari8 = toNumber(self.vari8) + 1
            self.vari9 = ""
            while not (letter_of(_ToString(arg_d), toNumber(self.vari7)).lower() in ";".lower()):
                self.vari9 = (self.vari9 + letter_of(_ToString(arg_d), toNumber(self.vari7)))
                self.vari7 = toNumber(self.vari7) + 1
            self.vari7 = toNumber(self.vari7) + 1
            if eq(self.vari9, (1 * ScratchStringToNumber(self.vari9))):
                self.listchData0[toNumber(self.vari6)] = (1 * ScratchStringToNumber(self.vari9))
            else:
                self.listchData0[toNumber(self.vari6)] = self.vari9
            self.vari9 = ""
            while not (letter_of(_ToString(arg_d), toNumber(self.vari7)).lower() in ";".lower()):
                self.vari9 = (self.vari9 + letter_of(_ToString(arg_d), toNumber(self.vari7)))
                self.vari7 = toNumber(self.vari7) + 1
            self.vari7 = toNumber(self.vari7) + 1
            if eq(self.vari9, (1 * ScratchStringToNumber(self.vari9))):
                self.listchData1[toNumber(self.vari6)] = (1 * ScratchStringToNumber(self.vari9))
            else:
                self.listchData1[toNumber(self.vari6)] = self.vari9
            self.vari9 = ""
            while not (letter_of(_ToString(arg_d), toNumber(self.vari7)).lower() in ";".lower()):
                self.vari9 = (self.vari9 + letter_of(_ToString(arg_d), toNumber(self.vari7)))
                self.vari7 = toNumber(self.vari7) + 1
            self.vari7 = toNumber(self.vari7) + 1
            if eq(self.vari9, (1 * ScratchStringToNumber(self.vari9))):
                self.listchData2[toNumber(self.vari6)] = (1 * ScratchStringToNumber(self.vari9))
            else:
                self.listchData2[toNumber(self.vari6)] = self.vari9
            self.vari9 = ""
            while not (letter_of(_ToString(arg_d), toNumber(self.vari7)).lower() in ";".lower()):
                self.vari9 = (self.vari9 + letter_of(_ToString(arg_d), toNumber(self.vari7)))
                self.vari7 = toNumber(self.vari7) + 1
            self.vari7 = toNumber(self.vari7) + 1
            if eq(self.vari9, (1 * ScratchStringToNumber(self.vari9))):
                self.listchData3[toNumber(self.vari6)] = (1 * ScratchStringToNumber(self.vari9))
            else:
                self.listchData3[toNumber(self.vari6)] = self.vari9
            self.vari6 = toNumber(self.vari6) + 1
        if gt(self.vari8, 0):
            self.vari5 = arg_id
            for _ in create_repeat((len(self.listchIndex) - toNumber(self.vari5))):
                self.vari5 = toNumber(self.vari5) + 1
                self.listchIndex[toNumber(self.vari5)] = (toNumber(self.listchIndex[toNumber(self.vari5)]) + toNumber(self.vari8))

    @warp
    async def mygetWidth(self, util, arg_text, arg_size, arg_cspace):
        self.varwidth = 0
        self.vari0 = 1
        self.vari1 = 0
        for _ in create_repeat(len(_ToString(arg_text))):
            self.costume.switch("blank")
            self.costume.switch((letter_of(_ToString(arg_text), toNumber(self.vari0)) + "_"))
            self.vari2 = (self.costume.number - 1)
            if gt(self.vari2, 0):
                self.varwidth += ((toNumber(arg_size) * toNumber(self.listchWidth[toNumber(self.vari2)])) + toNumber(arg_cspace))
                self.vari1 = toNumber(self.vari1) + 1
            self.vari0 = toNumber(self.vari0) + 1
        if gt(self.vari1, 0):
            self.varwidth += (-1 * toNumber(arg_cspace))

    async def my_NewLinesNumberSizeSpace(self, util, arg_lines, arg_size, arg_lspace):
        self.vary = toNumber(self.vary) + ((toNumber(arg_lines) + int(eq(arg_lines, ""))) * ((toNumber(arg_size) + (12 * int(eq(arg_size, "")))) * (-1 - (0.7 * (toNumber(arg_lspace) + int(eq(arg_lspace, "")))))))

    @warp
    async def my_PrintPosSizeBoundsSpaceStyleUnderlineAlignText(self, util, arg_x, arg_y, arg_size, arg_width, arg_xmin, arg_xmax, arg_cspace, arg_weight, arg_slant, arg_ulheight, arg_ulweight, arg_alx, arg_aly, arg_text):
        self.pen.up()
        self.vari8 = (arg_size + (12 * int(eq(arg_size, ""))))
        if not gt(self.vari8, 0):
            self.varx = (1 * ScratchStringToNumber(arg_x))
            self.vary = (1 * arg_y)
            self.costume.switch(" _")
            return None
        self.vari7 = ((ScratchStringToNumber(arg_width) + int(eq(arg_width, ""))) * toNumber(self.vari8))
        self.vari9 = NumberToString((tan(ScratchStringToNumber(arg_slant)) * toNumber(self.vari8)))
        self.vari2 = (ScratchStringToNumber(arg_alx) + ((0.5 * int(eq(arg_alx, "c"))) + int(eq(arg_alx, "r"))))
        self.vari3 = (ScratchStringToNumber(arg_aly) + ((0.5 * int(eq(arg_aly, "c"))) + int(eq(arg_aly, "t"))))
        self.vari4 = ((ScratchStringToNumber(arg_cspace) + int(eq(arg_cspace, ""))) * (0.27 * toNumber(self.vari8)))
        self.pen.set_size((0.125 * ((ScratchStringToNumber(arg_weight) + int(eq(arg_weight, ""))) * toNumber(self.vari8))))
        await self.myprintText(util, arg_text, (1 * ScratchStringToNumber(arg_x)), (arg_y - (toNumber(self.vari3) * toNumber(self.vari8))), (ScratchStringToNumber(arg_xmin) + (int(eq(arg_xmin, "")) * div(-1, 0))), (ScratchStringToNumber(arg_xmax) + (int(eq(arg_xmax, "")) * div(1, 0))), self.vari4, arg_ulheight, ((ScratchStringToNumber(arg_weight) + int(eq(arg_weight, ""))) * (ScratchStringToNumber(arg_ulweight) + int(eq(arg_ulweight, "")))), (-1 * toNumber(self.vari2)))

    @warp
    async def my_GetWidthSizeSpaceText(self, util, arg_size, arg_width, arg_cspace, arg_text):
        await self.mygetWidth(util, arg_text, ((toNumber(arg_size) + (12 * int(eq(arg_size, "")))) * (toNumber(arg_width) + int(eq(arg_width, "")))), ((toNumber(arg_cspace) + int(eq(arg_cspace, ""))) * (0.27 * (toNumber(arg_size) + (12 * int(eq(arg_size, "")))))))

    @warp
    async def my_PrintWWPosSizeBoundsSpaceStyleUnderlineAlignText(self, util, arg_x, arg_y, arg_size, arg_width, arg_xmin, arg_xmax, arg_ymax, arg_ymin, arg_cspace, arg_lspace, arg_weight, arg_slant, arg_ulheight, arg_ulweight, arg_alx, arg_aly, arg_text):
        self.pen.up()
        self.vari0 = (toNumber(arg_size) + (12 * int(eq(arg_size, ""))))
        if not gt(self.vari0, 0):
            self.varx = (1 * toNumber(arg_x))
            self.vary = (1 * toNumber(arg_y))
            self.costume.switch(" _")
            return None
        self.vari0 = ((toNumber(arg_width) + int(eq(arg_width, ""))) * toNumber(self.vari0))
        self.vari1 = (toNumber(arg_xmin) + (-230 * int(eq(arg_xmin, ""))))
        self.vari2 = (toNumber(arg_xmax) + (230 * int(eq(arg_xmax, ""))))
        self.vari3 = self.listchWidth[1]
        self.vari4 = div((0.27 * (toNumber(arg_cspace) + int(eq(arg_cspace, "")))), (toNumber(arg_width) + int(eq(arg_width, ""))))
        await self.mycalcWW(util, arg_text, div((toNumber(self.vari2) - toNumber(self.vari1)), toNumber(self.vari0)), (int(not eq(arg_x, "")) * div((toNumber(arg_x) - toNumber(self.vari1)), toNumber(self.vari0))), self.vari4, (toNumber(self.vari4) + toNumber(self.vari3)))
        self.vari7 = self.vari0
        self.vari8 = (toNumber(arg_size) + (12 * int(eq(arg_size, ""))))
        self.vari3 = (toNumber(arg_alx) + ((0.5 * int(eq(arg_alx, "c"))) + int(eq(arg_alx, "r"))))
        self.vari0 = (toNumber(arg_lspace) + int(eq(arg_lspace, "")))
        if eq(arg_aly, ""):
            self.vari4 = 1
        else:
            if eq(arg_aly, (1 * toNumber(arg_aly))):
                self.vari4 = arg_aly
            else:
                if eq(arg_aly, "b"):
                    self.vari4 = (len(self.listww1) - int((eq(self.listww2[1], 0) and eq(arg_x, ""))))
                else:
                    if eq(arg_aly, "c"):
                        self.vari4 = (0.5 * (div((0.7 * toNumber(self.vari0)), ((0.7 * toNumber(self.vari0)) + 1)) + (len(self.listww1) - int((eq(self.listww2[1], 0) and eq(arg_x, ""))))))
                    else:
                        self.vari4 = div((0.7 * toNumber(self.vari0)), ((0.7 * toNumber(self.vari0)) + 1))
        self.vari5 = (0.1 * (((toNumber(arg_ulweight) + int(eq(arg_ulweight, ""))) * (toNumber(arg_weight) + int(eq(arg_weight, "")))) * toNumber(self.vari8)))
        if eq(arg_ymax, ""):
            self.vari6 = div(1, 0)
        else:
            self.vari6 = (toNumber(arg_ymax) - toNumber(self.vari0))
        self.vari9 = NumberToString((tan(toNumber(arg_slant)) * toNumber(self.vari8)))
        await self.myprintWW(util, (((1 - toNumber(self.vari3)) * toNumber(self.vari1)) + (toNumber(self.vari3) * toNumber(self.vari2))), arg_x, (1 - int(eq(arg_x, ""))), (1 * toNumber(arg_y)), self.vari6, (toNumber(arg_ymin) + (int(eq(arg_ymin, "")) * div(-1, 0))), ((toNumber(arg_cspace) + int(eq(arg_cspace, ""))) * (0.27 * toNumber(self.vari8))), (toNumber(self.vari8) * (-1 - (0.7 * toNumber(self.vari0)))), (0.125 * ((toNumber(arg_weight) + int(eq(arg_weight, ""))) * toNumber(self.vari8))), (toNumber(arg_ulheight) * toNumber(self.vari8)), self.vari5, (toNumber(arg_ulheight) * ScratchStringToNumber(self.vari9)), not eq(arg_ulheight, ""), (-1 * (toNumber(self.vari3) * toNumber(self.vari7))), self.vari4)

    @warp
    async def myprintText(self, util, arg_text, arg_x, arg_y, arg_xmin, arg_xmax, arg_cspace, arg_ulheight, arg_ulweight, arg_alx):
        self.varx = arg_x
        self.vary = arg_y
        if not eq(arg_alx, 0):
            self.varwidth = 0
            await self.mygetWidth(util, arg_text, self.vari7, arg_cspace)
            self.varx = toNumber(self.varx) + (arg_alx * self.varwidth)
        self.varbq = ceil(((0.075 * sqrt((toNumber(self.vari7) * toNumber(self.vari8)))) + 0.5))
        self.varbq2 = (4 * (self.varbq * self.varbq))
        self.vari0 = 1
        if (eq(arg_xmin, div(-1, 0)) and eq(arg_xmax, div(1, 0))):
            if eq(self.vari9, 0):
                for _ in create_repeat(len(_ToString(arg_text))):
                    self.costume.switch("blank")
                    self.costume.switch((letter_of(_ToString(arg_text), toNumber(self.vari0)) + "_"))
                    if gt(self.costume.number, 1):
                        await self.myprintCh(util, (self.costume.number - 1))
                        self.varx = toNumber(self.varx) + toNumber(arg_cspace)
                    self.vari0 = toNumber(self.vari0) + 1
            else:
                for _ in create_repeat(len(_ToString(arg_text))):
                    self.costume.switch("blank")
                    self.costume.switch((letter_of(_ToString(arg_text), toNumber(self.vari0)) + "_"))
                    if gt(self.costume.number, 1):
                        await self.myprintChSl(util, (self.costume.number - 1))
                        self.varx = toNumber(self.varx) + toNumber(arg_cspace)
                    self.vari0 = toNumber(self.vari0) + 1
        else:
            for _ in create_repeat(len(_ToString(arg_text))):
                self.costume.switch("blank")
                self.costume.switch((letter_of(_ToString(arg_text), toNumber(self.vari0)) + "_"))
                if gt(self.costume.number, 1):
                    if not (lt(self.varx, arg_xmin) or gt((toNumber(self.varx) + (toNumber(self.vari7) * toNumber(self.listchWidth[(self.costume.number - 1)]))), arg_xmax)):
                        await self.myprintChSl(util, (self.costume.number - 1))
                    else:
                        self.varx = toNumber(self.varx) + (toNumber(self.vari7) * toNumber(self.listchWidth[(self.costume.number - 1)]))
                    self.varx = toNumber(self.varx) + toNumber(arg_cspace)
                self.vari0 = toNumber(self.vari0) + 1
        self.costume.switch(" _")
        if not eq(arg_ulheight, ""):
            self.pen.set_size((0.1 * ((arg_ulweight + int(eq(arg_ulweight, ""))) * toNumber(self.vari8))))
            self.vari1 = (arg_x + (arg_alx * self.varwidth))
            if lt(self.vari1, arg_xmin):
                self.vari1 = arg_xmin
            self.gotoxy(((toNumber(self.vari1) + (ScratchStringToNumber(self.vari9) * toNumber(arg_ulheight))) - (0.13 * toNumber(self.vari7))), (arg_y + (toNumber(arg_ulheight) * toNumber(self.vari8))))
            self.pen.down()
            self.vari2 = (toNumber(self.varx) - toNumber(arg_cspace))
            if gt(self.vari2, arg_xmax):
                self.vari2 = arg_xmax
            self.xpos = ((toNumber(self.vari2) + (ScratchStringToNumber(self.vari9) * toNumber(arg_ulheight))) + (0.13 * toNumber(self.vari7)))
            self.pen.up()

    @warp
    async def myprintWW(self, util, arg_x, arg_firstX, arg_firstLine, arg_y, arg_ymax, arg_ymin, arg_cspace, arg_lspace, arg_wt, arg_ulheight, arg_ulweight, arg_uloffset, arg_undl, arg_alx, arg_aly):
        self.costume.switch(" _")
        self.varx = arg_x
        self.vary = (arg_y - ((toNumber(arg_aly) - 1) * arg_lspace))
        self.vari0 = 1
        self.vari1 = 1
        if eq(self.listww2[1], 0):
            self.vari0 = toNumber(self.vari0) + 1
            self.vari1 = toNumber(self.vari1) + 1
            if eq(arg_firstLine, 1):
                self.vary = toNumber(self.vary) + arg_lspace
        while not (not gt(self.vary, arg_ymax) or gt(self.vari0, len(self.listww1))):
            self.vari1 = toNumber(self.vari1) + (toNumber(self.listww2[toNumber(self.vari0)]) + 1)
            self.vari0 = toNumber(self.vari0) + 1
            self.vary = toNumber(self.vary) + arg_lspace
        self.varbq = ceil(((0.075 * sqrt((toNumber(self.vari7) * toNumber(self.vari8)))) + 0.5))
        self.varbq2 = (4 * (self.varbq * self.varbq))
        while not (lt(self.vary, arg_ymin) or gt(self.vari0, len(self.listww1))):
            if eq(self.vari0, arg_firstLine):
                self.varx = arg_firstX
            else:
                self.varx = (arg_x + (arg_alx * toNumber(self.listww1[toNumber(self.vari0)])))
            self.pen.set_size(arg_wt)
            if eq(self.vari9, 0):
                for _ in create_repeat(toNumber(self.listww2[toNumber(self.vari0)])):
                    await self.myprintCh(util, self.listww0[toNumber(self.vari1)])
                    self.varx = toNumber(self.varx) + arg_cspace
                    self.vari1 = toNumber(self.vari1) + 1
            else:
                for _ in create_repeat(toNumber(self.listww2[toNumber(self.vari0)])):
                    await self.myprintChSl(util, self.listww0[toNumber(self.vari1)])
                    self.varx = toNumber(self.varx) + arg_cspace
                    self.vari1 = toNumber(self.vari1) + 1
            if arg_undl:
                self.pen.set_size(toNumber(arg_ulweight))
                if eq(self.vari0, arg_firstLine):
                    self.gotoxy(((toNumber(arg_firstX) + arg_uloffset) - (0.13 * toNumber(self.vari7))), (toNumber(self.vary) + arg_ulheight))
                else:
                    self.gotoxy((((arg_x + (arg_alx * toNumber(self.listww1[toNumber(self.vari0)]))) + arg_uloffset) - (0.13 * toNumber(self.vari7))), (toNumber(self.vary) + arg_ulheight))
                self.pen.down()
                self.xpos = (((toNumber(self.varx) - arg_cspace) + arg_uloffset) + (0.13 * toNumber(self.vari7)))
                self.pen.up()
            self.vari0 = toNumber(self.vari0) + 1
            self.vari1 = toNumber(self.vari1) + 1
            self.vary = toNumber(self.vary) + arg_lspace
        if gt((len(self.listww1) - int(eq(self.listww2[1], 0))), 0):
            self.vary = toNumber(self.vary) + (-1 * arg_lspace)
        self.listww0.delete_all()
        self.listww1.delete_all()
        self.listww2.delete_all()

    @warp
    async def myprintCh(self, util, arg_id):
        self.vari2 = self.listchIndex[toNumber(arg_id)]
        if eq(self.listchData1[toNumber(self.vari2)], "Q"):
            for _ in create_repeat(toNumber(self.listchData0[toNumber(self.vari2)])):
                self.vari2 = toNumber(self.vari2) + 1
                self.gotoxy((toNumber(self.varx) + (toNumber(self.vari7) * toNumber(self.listchData0[toNumber(self.vari2)]))), (toNumber(self.vary) + (toNumber(self.vari8) * toNumber(self.listchData1[toNumber(self.vari2)]))))
                self.pen.down()
                for _ in create_repeat(toNumber(self.listchData2[toNumber(self.vari2)])):
                    self.vari2 = toNumber(self.vari2) + 1
                    if eq(self.listchData0[toNumber(self.vari2)], "L"):
                        self.gotoxy((self.xpos + (toNumber(self.vari7) * toNumber(self.listchData1[toNumber(self.vari2)]))), (self.ypos + (toNumber(self.vari8) * toNumber(self.listchData2[toNumber(self.vari2)]))))
                    else:
                        self.vari3 = div((toNumber(self.vari7) * toNumber(self.listchData0[toNumber(self.vari2)])), self.varbq2)
                        self.vari4 = (div((toNumber(self.vari7) * toNumber(self.listchData1[toNumber(self.vari2)])), self.varbq) + div(toNumber(self.vari3), 2))
                        self.vari5 = div((toNumber(self.vari8) * toNumber(self.listchData2[toNumber(self.vari2)])), self.varbq2)
                        self.vari6 = (div((toNumber(self.vari8) * toNumber(self.listchData3[toNumber(self.vari2)])), self.varbq) + div(toNumber(self.vari5), 2))
                        for _ in create_repeat(self.varbq):
                            self.gotoxy((self.xpos + toNumber(self.vari4)), (self.ypos + toNumber(self.vari6)))
                            self.vari4 = toNumber(self.vari4) + toNumber(self.vari3)
                            self.vari6 = toNumber(self.vari6) + toNumber(self.vari5)
                            self.gotoxy((self.xpos + toNumber(self.vari4)), (self.ypos + toNumber(self.vari6)))
                            self.vari4 = toNumber(self.vari4) + toNumber(self.vari3)
                            self.vari6 = toNumber(self.vari6) + toNumber(self.vari5)
                self.pen.up()
        else:
            for _ in create_repeat(toNumber(self.listchData0[toNumber(self.vari2)])):
                self.vari2 = toNumber(self.vari2) + 1
                self.gotoxy((toNumber(self.varx) + (toNumber(self.vari7) * toNumber(self.listchData0[toNumber(self.vari2)]))), (toNumber(self.vary) + (toNumber(self.vari8) * toNumber(self.listchData1[toNumber(self.vari2)]))))
                self.pen.down()
                for _ in create_repeat(toNumber(self.listchData2[toNumber(self.vari2)])):
                    self.vari2 = toNumber(self.vari2) + 1
                    self.gotoxy((self.xpos + (toNumber(self.vari7) * toNumber(self.listchData0[toNumber(self.vari2)]))), (self.ypos + (toNumber(self.vari8) * toNumber(self.listchData1[toNumber(self.vari2)]))))
                self.pen.up()
        self.vari2 = toNumber(self.vari2) + 1
        self.pen.change_size(1)
        for _ in create_repeat(toNumber(self.listchData0[toNumber(self.vari2)])):
            self.vari2 = toNumber(self.vari2) + 1
            self.gotoxy((toNumber(self.varx) + (toNumber(self.vari7) * toNumber(self.listchData0[toNumber(self.vari2)]))), (toNumber(self.vary) + (toNumber(self.vari8) * toNumber(self.listchData1[toNumber(self.vari2)]))))
            self.pen.down()
            self.pen.up()
        self.pen.change_size(-1)
        self.varx = toNumber(self.varx) + (toNumber(self.vari7) * toNumber(self.listchWidth[toNumber(arg_id)]))

    @warp
    async def myprintChSl(self, util, arg_id):
        self.vari2 = self.listchIndex[toNumber(arg_id)]
        if eq(self.listchData1[toNumber(self.vari2)], "Q"):
            for _ in create_repeat(toNumber(self.listchData0[toNumber(self.vari2)])):
                self.vari2 = toNumber(self.vari2) + 1
                self.gotoxy((toNumber(self.varx) + ((toNumber(self.vari7) * toNumber(self.listchData0[toNumber(self.vari2)])) + (ScratchStringToNumber(self.vari9) * toNumber(self.listchData1[toNumber(self.vari2)])))), (toNumber(self.vary) + (toNumber(self.vari8) * toNumber(self.listchData1[toNumber(self.vari2)]))))
                self.pen.down()
                for _ in create_repeat(toNumber(self.listchData2[toNumber(self.vari2)])):
                    self.vari2 = toNumber(self.vari2) + 1
                    if eq(self.listchData0[toNumber(self.vari2)], "L"):
                        self.gotoxy((self.xpos + ((toNumber(self.vari7) * toNumber(self.listchData1[toNumber(self.vari2)])) + (ScratchStringToNumber(self.vari9) * toNumber(self.listchData2[toNumber(self.vari2)])))), (self.ypos + (toNumber(self.vari8) * toNumber(self.listchData2[toNumber(self.vari2)]))))
                    else:
                        self.vari3 = div(((toNumber(self.vari7) * toNumber(self.listchData0[toNumber(self.vari2)])) + (ScratchStringToNumber(self.vari9) * toNumber(self.listchData2[toNumber(self.vari2)]))), self.varbq2)
                        self.vari4 = (div(((toNumber(self.vari7) * toNumber(self.listchData1[toNumber(self.vari2)])) + (ScratchStringToNumber(self.vari9) * toNumber(self.listchData3[toNumber(self.vari2)]))), self.varbq) + div(toNumber(self.vari3), 2))
                        self.vari5 = div((toNumber(self.vari8) * toNumber(self.listchData2[toNumber(self.vari2)])), self.varbq2)
                        self.vari6 = (div((toNumber(self.vari8) * toNumber(self.listchData3[toNumber(self.vari2)])), self.varbq) + div(toNumber(self.vari5), 2))
                        for _ in create_repeat(self.varbq):
                            self.gotoxy((self.xpos + toNumber(self.vari4)), (self.ypos + toNumber(self.vari6)))
                            self.vari4 = toNumber(self.vari4) + toNumber(self.vari3)
                            self.vari6 = toNumber(self.vari6) + toNumber(self.vari5)
                            self.gotoxy((self.xpos + toNumber(self.vari4)), (self.ypos + toNumber(self.vari6)))
                            self.vari4 = toNumber(self.vari4) + toNumber(self.vari3)
                            self.vari6 = toNumber(self.vari6) + toNumber(self.vari5)
                self.pen.up()
        else:
            for _ in create_repeat(toNumber(self.listchData0[toNumber(self.vari2)])):
                self.vari2 = toNumber(self.vari2) + 1
                self.gotoxy((toNumber(self.varx) + ((toNumber(self.vari7) * toNumber(self.listchData0[toNumber(self.vari2)])) + (ScratchStringToNumber(self.vari9) * toNumber(self.listchData1[toNumber(self.vari2)])))), (toNumber(self.vary) + (toNumber(self.vari8) * toNumber(self.listchData1[toNumber(self.vari2)]))))
                self.pen.down()
                for _ in create_repeat(toNumber(self.listchData2[toNumber(self.vari2)])):
                    self.vari2 = toNumber(self.vari2) + 1
                    self.gotoxy((self.xpos + ((toNumber(self.vari7) * toNumber(self.listchData0[toNumber(self.vari2)])) + (ScratchStringToNumber(self.vari9) * toNumber(self.listchData1[toNumber(self.vari2)])))), (self.ypos + (toNumber(self.vari8) * toNumber(self.listchData1[toNumber(self.vari2)]))))
                self.pen.up()
        self.vari2 = toNumber(self.vari2) + 1
        self.pen.change_size(1)
        for _ in create_repeat(toNumber(self.listchData0[toNumber(self.vari2)])):
            self.vari2 = toNumber(self.vari2) + 1
            self.gotoxy((toNumber(self.varx) + ((toNumber(self.vari7) * toNumber(self.listchData0[toNumber(self.vari2)])) + (ScratchStringToNumber(self.vari9) * toNumber(self.listchData1[toNumber(self.vari2)])))), (toNumber(self.vary) + (toNumber(self.vari8) * toNumber(self.listchData1[toNumber(self.vari2)]))))
            self.pen.down()
            self.pen.up()
        self.pen.change_size(-1)
        self.varx = toNumber(self.varx) + (toNumber(self.vari7) * toNumber(self.listchWidth[toNumber(arg_id)]))

    @on_broadcast('render editor text')
    async def broadcast_rendereditortext(self, util):
        await self.my_editor(util, )

    @warp
    async def my_editor(self, util, ):
        if gt(util.sprites.stage.var_, util.sprites.stage.var_max):
            await self.my_SetPenColorRGBA(util, 225, 25, 25, 255)
        else:
            await self.my_SetPenColorRGBA(util, 25, 200, 25, 255)
        await self.my_PrintPosSizeBoundsSpaceStyleUnderlineAlignText(util, "", 160, 20, "", "", "", "", "", "", "", "", "0.5", "0.5", ("$" + NumberToString(util.sprites.stage.var_)))
        await self.my_SetPenColorRGBA(util, 225, 225, 25, 255)
        await self.my_PrintPosSizeBoundsSpaceStyleUnderlineAlignText(util, "", 135, 10, "", "", "", "", "", "", "", "", "0.5", "0.5", ("Budget: $" + NumberToString(util.sprites.stage.var_max)))
        if gt(util.sprites.stage.var_budget, util.timer()):
            await self.my_SetPenColorRGBA(util, 225, 25, 25, 255)
            self.pen.set_color("transparency", ((((1 - div((util.sprites.stage.var_budget - util.timer()), 2)) * 3) - 2) * 100))
            await self.my_PrintPosSizeBoundsSpaceStyleUnderlineAlignText(util, "", 0, 35, "", "", "", "", "", "", "", "", "0.5", "0.5", "Overbudget")

    @on_broadcast('turbowarp')
    async def broadcast_turbowarp(self, util):
        await self.my_turbowarp(util, )

    @warp
    async def my_turbowarp(self, util, ):
        self.pen.set_size(999999)
        self.pen.exact_color("#0e3977")
        self.gotoxy(0, 0)
        self.pen.down()
        self.pen.up()
        self.pen.exact_color("#114796")
        if eq(util.sprites.stage.var_counter, 1):
            self.pen.set_size(100)
        else:
            self.pen.set_size(85)
        await self.my_linefromto(util, -240, -140, 240, -140)
        self.pen.exact_color("#000000")
        await self.my_PrintPosSizeBoundsSpaceStyleUnderlineAlignText(util, "-110", 110, 28, "", "", "", "", "1.2", "", "", "", "", "", "Turbowarp:")
        await self.my_PrintPosSizeBoundsSpaceStyleUnderlineAlignText(util, "-190", 50, 16, "", "", "", "", "", "10", "", "", "", "", "You are running this is scratch, and")
        await self.my_PrintPosSizeBoundsSpaceStyleUnderlineAlignText(util, "-184", 15, 16, "", "", "", "", "", "10", "", "", "", "", "this project can get very laggy, so")
        await self.my_PrintPosSizeBoundsSpaceStyleUnderlineAlignText(util, "-190", -20, 16, "", "", "", "", "", "10", "", "", "", "", "I recommend to run it in Turbowarp")
        await self.my_PrintPosSizeBoundsSpaceStyleUnderlineAlignText(util, "-115", -55, 16, "", "", "", "", "", "10", "", "", "", "", "(link is in description)")
        await self.my_PrintPosSizeBoundsSpaceStyleUnderlineAlignText(util, "-110", -150, 24, "", "", "", "", NumberToString((1 + div(util.sprites.stage.var_counter, 5))), "", "", "", "", "", "Run in scratch")

    @warp
    async def my_linefromto(self, util, arg_x, arg_y, arg_x2, arg_y2):
        self.pen.up()
        self.gotoxy(arg_x, arg_y)
        self.pen.down()
        self.gotoxy(arg_x2, arg_y2)
        self.pen.up()


@sprite('Music')
class SpriteMusic(Target):
    """Sprite Music"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self._set_shown(True)
        self.pen = Pen(self)

        self.costume = Costumes(
            self.sprite, 0, 100, "all around", [
            {
                'name': "costume1",
                'path': "3339a2953a3bf62bb80e54ff575dbced-fallback.png",
                'center': (0, 0),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "polyBridgeMusic",
                'path': "a8a2da92eaccb22854f3dc6cf872de51.wav"
            }
        ])





        self.sprite.layer = 6

    @on_green_flag
    async def green_flag(self, util):
        await self.sleep(0.5)
        while not eq(util.sprites.stage.var_counter, 2):
            await self.yield_()
        while True:
            await self.sounds.play("polyBridgeMusic")
            await self.sleep(1)

            await self.yield_()


@sprite('End')
class SpriteEnd(Target):
    """Sprite End"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self._set_shown(True)
        self.pen = Pen(self)

        self.costume = Costumes(
            self.sprite, 14, 100, "all around", [
            {
                'name': "descarga (1)",
                'path': "191f784199be985af29b958c9942fc86-svg-2x.png",
                'center': (1176, 882),
                'scale': 2
            },
            {
                'name': "descarga (2)",
                'path': "940db155c4418d143e160e4f5c3f6a0c-svg-2x.png",
                'center': (1176, 882),
                'scale': 2
            },
            {
                'name': "descarga (3)",
                'path': "ca2d718e34341351565ec21f3d27a8d3-svg-2x.png",
                'center': (1176, 882),
                'scale': 2
            },
            {
                'name': "descarga (4)",
                'path': "9a8e2e0d9bca64b51fb6607eb1e8f199-svg-2x.png",
                'center': (1176, 882),
                'scale': 2
            },
            {
                'name': "descarga (5)",
                'path': "62b7f80fbd698a47050a2385f775b6b9-svg-2x.png",
                'center': (1176, 882),
                'scale': 2
            },
            {
                'name': "descarga (6)",
                'path': "5664b8dc90198a16ecfaea268c1d050a-svg-2x.png",
                'center': (1176, 882),
                'scale': 2
            },
            {
                'name': "descarga (7)",
                'path': "eebfbfd397034dc15c61203a13f41b08-svg-2x.png",
                'center': (1176, 882),
                'scale': 2
            },
            {
                'name': "descarga (8)",
                'path': "adb9746cb3fef5cbad4cb44f3d499fd4-svg-2x.png",
                'center': (1176, 882),
                'scale': 2
            },
            {
                'name': "descarga (9)",
                'path': "f6c81c9dfa17ee1056974b9de3954cef-svg-2x.png",
                'center': (1176, 882),
                'scale': 2
            },
            {
                'name': "descarga (10)",
                'path': "c1a27ebe85b1fcc1d71940e8506afe7f-svg-2x.png",
                'center': (1176, 882),
                'scale': 2
            },
            {
                'name': "descarga (11)",
                'path': "6a08ae907bb9b3e526db3a2e567fef9c-svg-2x.png",
                'center': (1176, 882),
                'scale': 2
            },
            {
                'name': "descarga (12)",
                'path': "656385fc210f63e2c3b0100398c3d639-svg-2x.png",
                'center': (1176, 882),
                'scale': 2
            },
            {
                'name': "descarga (13)",
                'path': "046a9119d139b912dc9b8d04966c304d-svg-2x.png",
                'center': (1176, 882),
                'scale': 2
            },
            {
                'name': "descarga",
                'path': "4756f55b95abc5b6badb9a8eed84dd12-svg-2x.png",
                'center': (1176, 882),
                'scale': 2
            },
            {
                'name': "End",
                'path': "dea486972d7318980c22c3f8595252ca-svg-2x.png",
                'center': (1370, 1097),
                'scale': 2
            },
            {
                'name': "costume1",
                'path': "cd21514d0531fdffb22204e0ec5ed84a-svg-2x.png",
                'center': (0, 0),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "pop",
                'path': "83a9787d4cb6f3b7632b4ddfebf74367.wav"
            }
        ])

        self.var_ix = 360



        self.sprite.layer = 8

    @on_broadcast('end')
    async def broadcast_end1(self, util):
        for _ in create_repeat(1):
            self.delete_clone(util)

            await self.yield_()
        await self.my_render(util, )
        await self.my_clone(util, )
        self.shown = True
        self.costume.switch("costume1")
        self.costume.size = 100
        self.gotoxy(0, 0)
        self.costume.switch("End")

    @warp
    async def my_render(self, util, ):
        self.pen.clear_all()
        self.gotoxy(0, 0)
        self.pen.exact_color("#333333")
        self.pen.set_size(999)
        self.pen.down()
        self.pen.up()
        self.costume.size = 10

    @warp
    async def my_clone(self, util, ):
        self.var_ix = -240
        for _ in create_repeat(5):
            await self.my_goto(util, self.var_ix, 135)
            self.create_clone_of(util, "_myself_")
            await self.my_goto(util, self.var_ix, 45)
            self.create_clone_of(util, "_myself_")
            await self.my_goto(util, self.var_ix, -45)
            self.create_clone_of(util, "_myself_")
            await self.my_goto(util, self.var_ix, -135)
            self.create_clone_of(util, "_myself_")
            self.var_ix += 120

    @warp
    async def my_goto(self, util, arg_x, arg_y):
        self.costume.size = 100
        self.gotoxy(arg_x, arg_y)
        self.costume.size = 10

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False

    @on_clone_start
    async def clone_start(self, util):
        self.shown = True
        self.costume.set_effect('brightness', 0)
        self.costume.switch(pick_rand(1, 14))
        while True:
            self.var_ix += 0.5
            if gt(self.var_ix, 300):
                self.var_ix = -299.5
            await self.my_goto(util, self.var_ix, self.ypos)

            await self.yield_()




if __name__ == '__main__':
    engine.start_program()
