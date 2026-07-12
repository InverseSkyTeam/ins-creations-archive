#!/usr/bin/env python

from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import AmbientLight, DirectionalLight, LightAttrib
from panda3d.core import TextNode
from panda3d.core import LPoint3, LVector3, BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task
import sys

BLACK = (0, 0, 0, 1)
WHITE = (1, 1, 1, 1)
HIGHLIGHT = (0, 1, 1, 1)
PIECEBLACK = (.15, .15, .15, 1)

def PointAtZ(z, point, vec):
    return point + vec * ((z - point.getZ()) / vec.getZ())

def SquarePos(i):
    return LPoint3((i % 8) - 3.5, int(i // 8) - 3.5, 0)

def SquareColor(i):
    if (i + ((i // 8) % 2)) % 2:
        return BLACK
    else:
        return WHITE


class ChessboardDemo(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.title = OnscreenText(text="Panda3D: Tutorial - Mouse Picking",
                                  style=1, fg=(1, 1, 1, 1), shadow=(0, 0, 0, 1),
                                  pos=(0.8, -0.95), scale = .07)
        self.escapeEvent = OnscreenText(
            text="ESC: Quit", parent=base.a2dTopLeft,
            style=1, fg=(1, 1, 1, 1), pos=(0.06, -0.1),
            align=TextNode.ALeft, scale = .05)
        self.mouse1Event = OnscreenText(
            text="Left-click and drag: Pick up and drag piece",
            parent=base.a2dTopLeft, align=TextNode.ALeft,
            style=1, fg=(1, 1, 1, 1), pos=(0.06, -0.16), scale=.05)

        self.accept('escape', sys.exit)  
        self.disableMouse()  
        camera.setPosHpr(0, -12, 8, 0, -35, 0) 
        self.setupLights()

        self.picker = CollisionTraverser()  
        self.pq = CollisionHandlerQueue() 
        self.pickerNode = CollisionNode('mouseRay')
        self.pickerNP = camera.attachNewNode(self.pickerNode)
        self.pickerNode.setFromCollideMask(BitMask32.bit(1))
        self.pickerRay = CollisionRay()  
        self.pickerNode.addSolid(self.pickerRay)
        self.picker.addCollider(self.pickerNP, self.pq)

        self.squareRoot = render.attachNewNode("squareRoot")
        self.squares = [None for i in range(64)]
        self.pieces = [None for i in range(64)]
        for i in range(64):
            self.squares[i] = loader.loadModel("models/square")
            self.squares[i].reparentTo(self.squareRoot)
            self.squares[i].setPos(SquarePos(i))
            self.squares[i].setColor(SquareColor(i))
            self.squares[i].find("**/polygon").node().setIntoCollideMask(
                BitMask32.bit(1))
            self.squares[i].find("**/polygon").node().setTag('square', str(i))

        pieceOrder = (Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)

        for i in range(8, 16):
            self.pieces[i] = Pawn(i, WHITE)
        for i in range(48, 56):
            self.pieces[i] = Pawn(i, PIECEBLACK)
        for i in range(8):
            self.pieces[i] = pieceOrder[i](i, WHITE)
            self.pieces[i + 56] = pieceOrder[i](i + 56, PIECEBLACK)

        self.hiSq = False
        self.dragging = False
        self.mouseTask = taskMgr.add(self.mouseTask, 'mouseTask')
        self.accept("mouse1", self.grabPiece) 
        self.accept("mouse1-up", self.releasePiece) 

    def swapPieces(self, fr, to):
        temp = self.pieces[fr]
        self.pieces[fr] = self.pieces[to]
        self.pieces[to] = temp
        if self.pieces[fr]:
            self.pieces[fr].square = fr
            self.pieces[fr].obj.setPos(SquarePos(fr))
        if self.pieces[to]:
            self.pieces[to].square = to
            self.pieces[to].obj.setPos(SquarePos(to))

    def mouseTask(self, task):

        if self.hiSq is not False:
            self.squares[self.hiSq].setColor(SquareColor(self.hiSq))
            self.hiSq = False

        if self.mouseWatcherNode.hasMouse():
            mpos = self.mouseWatcherNode.getMouse()
            self.pickerRay.setFromLens(self.camNode, mpos.getX(), mpos.getY())
            if self.dragging is not False:
                nearPoint = render.getRelativePoint(
                    camera, self.pickerRay.getOrigin())
                nearVec = render.getRelativeVector(
                    camera, self.pickerRay.getDirection())
                self.pieces[self.dragging].obj.setPos(
                    PointAtZ(.5, nearPoint, nearVec))
            self.picker.traverse(self.squareRoot)
            if self.pq.getNumEntries() > 0:
                self.pq.sortEntries()
                i = int(self.pq.getEntry(0).getIntoNode().getTag('square'))
                self.squares[i].setColor(HIGHLIGHT)
                self.hiSq = i

        return Task.cont

    def grabPiece(self):
        if self.hiSq is not False and self.pieces[self.hiSq]:
            self.dragging = self.hiSq
            self.hiSq = False

    def releasePiece(self):
        if self.dragging is not False:
            if self.hiSq is False:
                self.pieces[self.dragging].obj.setPos(
                    SquarePos(self.dragging))
            else:
                self.swapPieces(self.dragging, self.hiSq)
        self.dragging = False

    def setupLights(self): 
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor((.8, .8, .8, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(LVector3(0, 45, -45))
        directionalLight.setColor((0.2, 0.2, 0.2, 1))
        render.setLight(render.attachNewNode(directionalLight))
        render.setLight(render.attachNewNode(ambientLight))

class Piece(object):
    def __init__(self, square, color):
        self.obj = loader.loadModel(self.model)
        self.obj.reparentTo(render)
        self.obj.setColor(color)
        self.obj.setPos(SquarePos(square))
class Pawn(Piece):
    model = "models/pawn"

class King(Piece):
    model = "models/king"

class Queen(Piece):
    model = "models/queen"

class Bishop(Piece):
    model = "models/bishop"

class Knight(Piece):
    model = "models/knight"

class Rook(Piece):
    model = "models/rook"
demo = ChessboardDemo()
demo.run()
