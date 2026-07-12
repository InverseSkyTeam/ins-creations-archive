import time
from .character import Zombie
from .world import Chunk
from .world import Frustum
from .world import World
from .world import WorldRenderer
from .world import Tesselator
from .Player import Player
from .world.tile import Block
from .particle import ParticleEngine
from .Timer import Timer
from .HitResult import HitResult
from .Textures import Textures
import sys
import numpy as np

# import java.io.IOException
# import java.io.PrintStream
# import java.nio.FloatBuffer
# import java.nio.IntBuffer
# import java.util.ArrayList
# import javax.swing.JOptionPane
# import org.lwjgl.BufferUtils

from Keyboard import Keyboard
from Mouse import Mouse
from Display import Display
from DisplayMode import DisplayMode
import GL11
import GLU


class RubyDung:
    FULLSCREEN_MODE: bool = False

    def __init__(self):
        self.width: int = 0
        self.height: int = 0
        self.debug_time: int = 1000
        
        # 保存烟雾数据1的float缓冲
        self.fogColor0 = None
        # 保存烟雾数据2的float缓冲
        self.fogColor1 = None
        
        self.timer: Timer = Timer(20.0)
        self.world = None
        self.worldRenderer = None
        self.player = None
        self.paintTexture: int = 1
        self.particleEngine = None

        # "僵尸"(实际上是玩家模型)集合
        self.zombies = []

        # 视场设置(数据以int缓冲组保存)
        self.viewportBuffer = None

        self.selectBuffer = None
        self.hitResult = None

        self.lb = None  # BufferUtils.createFloatBuffer(16)

    def init(self):
        col0: int = 0xfefbfa
        col1: int = 0x0e0b0a
        
        fr: float = 0.5  # 天空盒的颜色
        fg: float = 0.8
        fb: float = 1.0
        # 设置雾1的数据
        self.fogColor0 = (
            (col0 >> 16 & 0xFF) / 255.0,
            (col0 >> 8 & 0xFF) / 255.0, 
            (col0 & 0xFF) / 255.0, 
            1.0
        )
        # 设置雾2的数据
        self.fogColor1 = (
            (col1 >> 16 & 0xFF) / 255.0,
            (col1 >> 8 & 0xFF) / 255.0, 
            (col1 & 0xFF) / 255.0,
            1.0
        )

        # 设置显示窗体大小
        Display.setDisplayMode(DisplayMode(1024, 768))

        Display.create()
        Keyboard.create()
        Mouse.create()

        self.width = Display.getDisplayMode().getWidth()
        self.height = Display.getDisplayMode().getHeight()

        GL11.glEnable(GL11.GL_TEXTURE_2D)
        GL11.glShadeModel(7425)
        GL11.glClearColor(fr, fg, fb, 0.0)
        GL11.glClearDepth(1.0)
        GL11.glEnable(2929)
        GL11.glDepthFunc(515)
        GL11.glEnable(3008)
        GL11.glAlphaFunc(516, 0.5)

        GL11.glMatrixMode(5889)
        GL11.glLoadIdentity()

        GL11.glMatrixMode(5888)

        self.world = World(256, 256, 64)
        self.worldRenderer = WorldRenderer(self.world)
        self.player = Player(self.world)
        self.particleEngine = ParticleEngine(self.world)

        Mouse.setGrabbed(True)

        for i in range(10):
            zombie: Zombie = Zombie(self.world, 128.0, 0.0, 128.0)
            zombie.resetPos()
            self.zombies.append(zombie)

    '''
     * 关闭游戏时进行的后续操作
    '''
    def gameStop(self):
        self.world.save()  # 保存地图数据

        Mouse.destroy()
        Keyboard.destroy()
        Display.destroy()

    def run(self):
        try:
            self.init()
        except FileNotFoundError:
            pass
        except Exception:
            print("Failed to start RubyDung")
            sys.exit(0)

        lastTime: int = int(time.time() * 1000)
        frames: int = 0
        if 1: # try:
            # 游戏主循环开始
            while not Display.isCloseRequested():
                Mouse.setGrabbed(True)
                # player.setPos(player.x, 70, player.z)
                self.timer.advanceTime()

                for _ in range(self.timer.ticks):  
                    # 近两次调用中所有的游戏刻
                    self.tick()
                
                self.render(self.timer.a)
                
                frames += 1  # FPS计数
                while int(time.time() * 1000) >= lastTime + self.debug_time:  # 用于每秒输出调试信息
                    print(frames, "fps,", Chunk.updates)
                    Chunk.updates = 0
                    lastTime += self.debug_time
                    frames = 0
                    
                    # player.turn(0, 10)
                    # player.setPos(0,70, 10)
                    # player.moveRelative(0, -100, 10f)
                    # player.move(1, 10, 0)

                if Keyboard.isKeyDown(Keyboard.KEY_ESCAPE):
                    break
            # 主循环结束
        # except Exception as e:
        #     print(e)
        # finally:
            self.gameStop()

    def tick(self):
        while Keyboard.next():  # 响应键盘事件，做出相应操作
            if Keyboard.getEventKeyState():
                if Keyboard.getEventKey() == Keyboard.KEY_RETURN:
                    self.world.save()
                if Keyboard.getEventKey() == Keyboard.KEY_1:
                    self.paintTexture = 1
                if Keyboard.getEventKey() == Keyboard.KEY_2:
                    self.paintTexture = 3
                if Keyboard.getEventKey() == Keyboard.KEY_3:
                    self.paintTexture = 4
                if Keyboard.getEventKey() == Keyboard.KEY_4:
                    self.paintTexture = 5
                if Keyboard.getEventKey() == Keyboard.KEY_6:
                    self.paintTexture = 6
                if Keyboard.getEventKey() == Keyboard.KEY_G:
                    self.zombies.append(Zombie(self.world, self.player.x, self.player.y, self.player.z))

        self.world.tick()
        self.particleEngine.tick()

        i = 0
        while i < len(self.zombies):
            self.zombies[i].tick()
            if self.zombies[i].removed:
                del self.zombies[i]
                i -= 1
            i += 1

        self.player.tick()

    def moveCameraToPlayer(self, a: float):
        GL11.glTranslatef(0.0, 0.0, -0.3)
        GL11.glRotatef(self.player.xRot, 1.0, 0.0, 0.0)
        GL11.glRotatef(self.player.yRot, 0.0, 1.0, 0.0)

        x = self.player.xo + (self.player.x - self.player.xo) * a
        y = self.player.yo + (self.player.y - self.player.yo) * a
        z = self.player.zo + (self.player.z - self.player.zo) * a
        GL11.glTranslatef(-x, -y, -z)

    def setupCamera(self, a: float):
        GL11.glMatrixMode(5889)
        GL11.glLoadIdentity()
        GLU.gluPerspective(70.0, self.width / self.height, 0.05, 1000.0)
        GL11.glMatrixMode(5888)
        GL11.glLoadIdentity()
        self.moveCameraToPlayer(a)

    def setupPickCamera(self, a: float, x: int, y: int):
        GL11.glMatrixMode(5889)
        GL11.glLoadIdentity()
        self.viewportBuffer = GL11.glGetInteger(2978)
        GLU.gluPickMatrix(x, y, 5.0, 5.0, self.viewportBuffer)
        GLU.gluPerspective(70.0, self.width / self.height, 0.05, 1000.0)
        GL11.glMatrixMode(5888)
        GL11.glLoadIdentity()
        self.moveCameraToPlayer(a)

    def pick(self, a: float):
        # self.selectBuffer.clear()
        self.selectBuffer = np.zeros(2000, dtype=np.uint32)
        GL11.glSelectBuffer(len(self.selectBuffer), self.selectBuffer)
        # self.selectBuffer = GL11.glSelectBuffer(2000)
        GL11.glRenderMode(GL11.GL_SELECT)
        self.setupPickCamera(a, self.width // 2, self.height // 2)
        self.worldRenderer.pick(self.player, Frustum.getFrustum())
        hits: int = len(GL11.glRenderMode(GL11.GL_RENDER))

        closest: int = 0
        names = [0] * 10
        hitNameCount: int = 0
        index = 0
        for i in range(hits):
            nameCount: int = self.selectBuffer[index]
            index += 1
            minZ: int = self.selectBuffer[index]
            # self.selectBuffer.get()
            index += 2

            dist: int = minZ

            if dist < closest or i == 0:
                closest = dist
                hitNameCount = nameCount
                for j in range(nameCount):
                    names[j] = self.selectBuffer[index]
                    index += 1
            else:
                for j in range(nameCount):
                    index += 1

        if hitNameCount > 0:
            self.hitResult = HitResult(names[0], names[1], names[2], names[3], names[4])
        else:
            self.hitResult = None

    def render(self, a: float):
        xo: float = Mouse.getDX()
        yo: float = Mouse.getDY()
        self.player.turn(xo, yo)
        # self.pick(a)

        '''while Mouse.next():
            if Mouse.getEventButton() == 1 and Mouse.getEventButtonState():
                if self.hitResult is not None:
                    oldTile = Block.BLOCKS[self.world.getBlock(self.hitResult.x, self.hitResult.y, self.hitResult.z)]
                    changed: bool = self.world.setBlock(self.hitResult.x, self.hitResult.y, self.hitResult.z, 0)
                    if oldTile is not None and changed:
                        oldTile.destroy(self.world, self.hitResult.x, self.hitResult.y, 
                        self.hitResult.z, self.particleEngine)
            if Mouse.getEventButton() == 0 and Mouse.getEventButtonState():
                if self.hitResult is not None:
                    x = self.hitResult.x
                    y = self.hitResult.y
                    z = self.hitResult.z

                    if self.hitResult.f == 0:
                        y -= 1
                    if self.hitResult.f == 1:
                        y += 1
                    if self.hitResult.f == 2:
                        z -= 1
                    if self.hitResult.f == 3:
                        z += 1
                    if self.hitResult.f == 4:
                        x -= 1
                    if self.hitResult.f == 5:
                        x += 1
                    self.world.setBlock(x, y, z, self.paintTexture)
        '''

        GL11.glClear(16640)
        self.setupCamera(a)

        GL11.glEnable(2884)

        frustum: Frustum = Frustum.getFrustum()

        self.worldRenderer.updateDirtyChunks(self.player)

        self.setupFog(0)
        GL11.glEnable(2912)
        self.worldRenderer.render(self.player, 0)
        _ = [zombie.render(a) for zombie in self.zombies if zombie.isLit() and frustum.isVisible(zombie.bb)]
        self.particleEngine.render(self.player, a, 0)
        self.setupFog(1)
        self.worldRenderer.render(self.player, 1)
        _ = [zombie.render(a) for zombie in self.zombies if not zombie.isLit() and frustum.isVisible(zombie.bb)]
        self.particleEngine.render(self.player, a, 1)
        GL11.glDisable(2896)
        GL11.glDisable(GL11.GL_TEXTURE_2D)
        GL11.glDisable(2912)

        if self.hitResult is not None:
            GL11.glDisable(3008)
            self.worldRenderer.renderHit(self.hitResult)
            GL11.glEnable(3008)

        self.drawGui(a)

        Display.update()

    def drawGui(self, a: float):
        screenWidth: int = self.width * 240 // self.height
        screenHeight: int = self.height * 240 // self.height

        GL11.glClear(256)
        GL11.glMatrixMode(5889)
        GL11.glLoadIdentity()
        GL11.glOrtho(0.0, screenWidth, screenHeight, 0.0, 100.0, 300.0)
        GL11.glMatrixMode(5888)
        GL11.glLoadIdentity()
        GL11.glTranslatef(0.0, 0.0, -200.0)

        GL11.glPushMatrix()
        GL11.glTranslatef(screenWidth - 16, 16.0, 0.0)
        t: Tesselator = Tesselator.instance
        GL11.glScalef(16.0, 16.0, 16.0)
        GL11.glRotatef(30.0, 1.0, 0.0, 0.0)
        GL11.glRotatef(45.0, 0.0, 1.0, 0.0)
        GL11.glTranslatef(-1.5, 0.5, -0.5)
        GL11.glScalef(-1.0, -1.0, 1.0)

        _id = Textures.loadTexture("/terrain.png", GL11.GL_NEAREST)
        GL11.glBindTexture(GL11.GL_TEXTURE_2D, _id)
        GL11.glEnable(GL11.GL_TEXTURE_2D)
        t.init()
        Block.BLOCKS[self.paintTexture].render(t, self.world, 0, -2, 0, 0)
        t.flush()
        GL11.glDisable(GL11.GL_TEXTURE_2D)
        GL11.glPopMatrix()

        wc: int = screenWidth // 2
        hc: int = screenHeight // 2
        GL11.glColor4f(1.0, 1.0, 1.0, 1.0)
        t.init()
        t.vertex(wc + 1, hc - 4, 0.0)
        t.vertex(wc - 0, hc - 4, 0.0)
        t.vertex(wc - 0, hc + 5, 0.0)
        t.vertex(wc + 1, hc + 5, 0.0)

        t.vertex(wc + 5, hc - 0, 0.0)
        t.vertex(wc - 4, hc - 0, 0.0)
        t.vertex(wc - 4, hc + 1, 0.0)
        t.vertex(wc + 5, hc + 1, 0.0)
        t.flush()

    def setupFog(self, i: int):
        if i == 0:
            GL11.glFogi(2917, 2048)
            GL11.glFogf(2914, 0.001)
            GL11.glFogfv(GL11.GL_FOG_COLOR, self.fogColor0)
            GL11.glDisable(2896)
        elif i == 1:
            GL11.glFogi(2917, 2048)
            GL11.glFogf(2914, 0.06)
            GL11.glFogfv(GL11.GL_FOG_COLOR, self.fogColor1)
            GL11.glEnable(2896)
            GL11.glEnable(2903)

            br: float = 0.6
            GL11.glLightModelfv(GL11.GL_LIGHT_MODEL_AMBIENT, self.getBuffer(br, br, br, 1.0))

    def getBuffer(self, a: float, b: float, c: float, d: float):
        self.lb = [a, b, c, d]
        return self.lb

    @staticmethod
    def main():
        RubyDung().run()
        # new Thread(new RubyDung()).start()
