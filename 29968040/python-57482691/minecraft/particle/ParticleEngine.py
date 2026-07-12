from .Particle import Particle
from minecraft.world.Tesselator import Tesselator
from minecraft.Textures import Textures

import math
import GL11


# 粒子引擎,渲染破坏粒子效果
class ParticleEngine:
    def __init__(self, world):
        self.world = world
        self.particles = []

    '''
     * 添加粒子
     * @param p
    '''
    def add(self, p: Particle):
        self.particles.append(p)

    def tick(self):
        i = 0
        while i < len(self.particles):
            p: Particle = self.particles[i]
            p.tick()
            if p.removed:
                del self.particles[i]
                i -= 1
            i += 1

    def render(self, player, a: float, layer: int):
        GL11.glEnable(GL11.GL_TEXTURE_2D)
        _id: int = Textures.loadTexture("/terrain.png", GL11.GL_NEAREST)
        GL11.glBindTexture(GL11.GL_TEXTURE_2D, _id)
        xa: float = -math.cos(player.yRot * math.pi / 180.0)
        za: float = -math.sin(player.yRot * math.pi / 180.0)

        xa2: float = -za * math.sin(player.xRot * math.pi / 180.0)
        za2: float = xa * math.sin(player.xRot * math.pi / 180.0)
        ya: float = math.cos(player.xRot * math.pi / 180.0)

        t: Tesselator = Tesselator.instance
        GL11.glColor4f(0.8, 0.8, 0.8, 1.0)
        t.init()
        for i in range(len(self.particles)):
            p: Particle = self.particles[i]
            if p.isLit() ^ layer == 1:
                p.render(t, a, xa, ya, za, xa2, za2)
        t.flush()
        GL11.glDisable(GL11.GL_TEXTURE_2D)
