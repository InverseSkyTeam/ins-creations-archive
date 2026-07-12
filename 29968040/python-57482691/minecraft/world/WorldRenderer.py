from minecraft.Textures import Textures
from .tile import Block
import GL11
import time
import math
from functools import cmp_to_key
from .DirtyChunkSorter import DirtyChunkSorter
from .Tesselator import Tesselator
from .WorldListener import WorldListener
from .Chunk import Chunk
from .Frustum import Frustum
from typing import List
from numba import jit


class WorldRenderer(WorldListener):
    MAX_REBUILDS_PER_FRAME: int = 8
    CHUNK_SIZE: int = 16

    '''
     * 世界绘制器
     * @param world 要绘制的世界
    '''
    def __init__(self, world):
        self.world = world
        world.addListener(self)

        self.xChunks: int = world.width // 16
        self.yChunks: int = world.depth // 16
        self.zChunks: int = world.height // 16
        
        def set_chunk(world, x, y, z):
            x0: int = x * 16
            y0: int = y * 16
            z0: int = z * 16
            x1: int = x0 + 16  # (x + 1) * 16
            y1: int = y0 + 16  # (y + 1) * 16
            z1: int = z0 + 16  # (z + 1) * 16

            if x1 > world.width:
                x1 = world.width
            if y1 > world.depth:
                y1 = world.depth
            if z1 > world.height:
                z1 = world.height
            return Chunk(world, x0, y0, z0, x1, y1, z1)

        self.chunks: List[Chunk] = [None] * (self.xChunks * self.yChunks * self.zChunks)
        for x in range(self.xChunks):
            for y in range(self.yChunks):
                for z in range(self.zChunks):
                    self.chunks[(x + y * self.xChunks) * self.zChunks + z] = set_chunk(world, x, y, z)

    def getAllDirtyChunks(self):
        dirty = [chunk for chunk in self.chunks if chunk.isDirty()]
        if len(dirty) == 0:
            return None
        # dirty = None
        # for chunk in self.chunks:
        #     if chunk.isDirty():
        #         if dirty is None:
        #             dirty = []
        #         dirty.append(chunk)
        return dirty

    def render(self, player, layer: int):
        GL11.glEnable(GL11.GL_TEXTURE_2D)
        _id: int = Textures.loadTexture("/terrain.png", GL11.GL_NEAREST)
        GL11.glBindTexture(GL11.GL_TEXTURE_2D, _id)
        frustum: Frustum = Frustum.getFrustum()
        for i in range(len(self.chunks)):
            if frustum.isVisible(self.chunks[i].aabb):
                self.chunks[i].render(layer)
        GL11.glDisable(GL11.GL_TEXTURE_2D)

    def updateDirtyChunks(self, player):
        dirty = self.getAllDirtyChunks()
        if dirty is None:
            return
        _cmp = DirtyChunkSorter(player, Frustum.getFrustum()).compare
        dirty.sort(key=cmp_to_key(_cmp))
        max_update = 1024
        a = time.time()
        _ = [dirty[i].rebuild() for i in range(0, min(max_update, len(dirty)))]
        print(time.time() - a)

    # @jit(forceobj=True)
    def pick(self, player, frustum):
        t: Tesselator = Tesselator.instance
        r: float = 3.0
        box = player.bb.grow(r, r, r)
        x0: int = int(box.x0)
        x1: int = int(box.x1 + 1.0)
        y0: int = int(box.y0)
        y1: int = int(box.y1 + 1.0)
        z0: int = int(box.z0)
        z1: int = int(box.z1 + 1.0)
        all_w, all_h, all_d = self.world.width, self.world.height, self.world.depth

        GL11.glInitNames()
        GL11.glPushName(0)
        GL11.glPushName(0)
        # print(x0, x1, y0, y1, z0, z1)
        for x in range(x0, x1):
            GL11.glLoadName(x)
            GL11.glPushName(0)
            for y in range(y0, y1):
                GL11.glLoadName(y)
                GL11.glPushName(0)
                for z in range(z0, z1):
                    # tile = Block.BLOCKS[self.world.getBlock(x, y, z)]
                    if x < 0 or y < 0 or z < 0 or x >= all_w or y >= all_d or z >= all_h:
                        continue
                    tile = Block.BLOCKS[self.world.blocks[(y * all_h + z) * all_w + x]]
                    if (tile is not None) and frustum.isVisible(tile.getBlockAABB(x, y, z)):
                        GL11.glLoadName(z)
                        GL11.glPushName(0)
                        for i in range(6):
                            GL11.glLoadName(i)
                            t.init()
                            tile.renderFaceNoTexture(t, x, y, z, i)
                            t.flush()
                        GL11.glPopName()
                GL11.glPopName()
            GL11.glPopName()
        GL11.glPopName()
        GL11.glPopName()

    def renderHit(self, h):
        t: Tesselator = Tesselator.instance
        GL11.glEnable(GL11.GL_BLEND)

        GL11.glBlendFunc(GL11.GL_SRC_ALPHA, 1)
        GL11.glColor4f(1.0, 1.0, 1.0, (math.sin(int(time.time() * 1000) / 100.0) * 0.2 + 0.4) * 0.5)
        t.init()
        Block.rock.renderFaceNoTexture(t, h.x, h.y, h.z, h.f)
        t.flush()
        GL11.glDisable(GL11.GL_BLEND)

    def setDirty(self, x0: int, y0: int, z0: int, 
                 x1: int, y1: int, z1: int):
        x0, x1 = max(x0 // 16, 0), min(x1 // 16, self.xChunks - 1)
        y0, y1 = max(y0 // 16, 0), min(y1 // 16, self.yChunks - 1)
        z0, z1 = max(z0 // 16, 0), min(z1 // 16, self.zChunks - 1)

        for x in range(x0, x1):
            for y in range(y0, y1):
                for z in range(z0, z1):
                    self.chunks[(x + y * self.xChunks) * self.zChunks + z].setDirty()

    def tileChanged(self, x: int, y: int, z: int):
        self.setDirty(x - 1, y - 1, z - 1, x + 1, y + 1, z + 1)

    def lightColumnChanged(self, x: int, z: int, y0: int, y1: int):
        self.setDirty(x - 1, y0 - 1, z - 1, x + 1, y1 + 1, z + 1)

    def allChanged(self):
        self.setDirty(0, 0, 0, self.world.width, self.world.depth, self.world.height)
