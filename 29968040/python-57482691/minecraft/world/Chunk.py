from minecraft.phys import AABB
from .Tesselator import Tesselator
import time
from .tile import Block
import GL11
from numba import jit


class Chunk:
    t: Tesselator = Tesselator.instance

    updates: int = 0

    totalTime: int = 0
    totalUpdates: int = 0

    def __init__(self, world, 
                 x0: int, y0: int, z0: int, 
                 x1: int, y1: int, z1: int):
        self.world = world
        self.x0: int = x0
        self.y0: int = y0
        self.z0: int = z0
        self.x1: int = x1
        self.y1: int = y1
        self.z1: int = z1

        self.x: float = (x0 + x1) / 2.0
        self.y: float = (y0 + y1) / 2.0
        self.z: float = (z0 + z1) / 2.0

        self.aabb = AABB(x0, y0, z0, x1, y1, z1)
        self.lists = GL11.glGenLists(2)
        
        self.dirty: bool = True
        self.dirtiedTime: int = 0

    def _rebuild(self, layer: int):  # 此函数经优化
        self.dirty = False

        Chunk.updates += 1

        before: int = int(time.time() * 1e9)
        GL11.glNewList(self.lists + layer, 4864)
        self.t.init()
        blocks = self.world.blocks
        tiles: int = 0
        t = self.t
        for x in range(self.x0, self.x1):
            for y in range(self.y0, self.y1):
                for z in range(self.z0, self.z1):
                    tileId = blocks[(y * self.world.height + z) * self.world.width + x]
                    if tileId > 0:
                        Block.BLOCKS[tileId].render(t, self.world, layer, x, y, z)
                        tiles += 1
        self.t.flush()
        GL11.glEndList()
        after: int = int(time.time() * 1e9)
        if tiles > 0:
            self.totalTime += after - before
            self.totalUpdates += 1

    def rebuild(self):
        self._rebuild(0)
        self._rebuild(1)

    def render(self, layer: int):
        GL11.glCallList(self.lists + layer)

    def setDirty(self):
        if not self.dirty:
            self.dirtiedTime = int(time.time() * 1000)
        self.dirty = True

    def isDirty(self) -> bool:
        return self.dirty

    def distanceToSqr(self, player) -> float:
        xd: float = player.x - self.x
        yd: float = player.y - self.y
        zd: float = player.z - self.z
        return xd * xd + yd * yd + zd * zd
