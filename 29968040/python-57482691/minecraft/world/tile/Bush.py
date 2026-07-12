from .Block import Block
import math


class Bush(Block):
    def __init__(self, _id: int):
        super().__init__(_id)
        self.tex = 15

    def tick(self, world, x: int, y: int, z: int, random):
        below: int = world.getBlock(x, y - 1, z)
        if not world.isLit(x, y, z) or (below != Block.dirt.id and below != Block.grass.id):
            world.setBlock(x, y, z, 0)

    def render(self, t, world, layer: int, x: int, y: int, z: int):
        if world.isLit(x, y, z) ^ layer != 1:
            return

        tex: int = self.getTexture(15)
        u0: float = tex % 16 / 16.0
        u1: float = u0 + 0.0624375
        v0: float = (tex // 16) / 16.0
        v1: float = v0 + 0.0624375

        rots: int = 2
        t.color(1.0, 1.0, 1.0)
        for r in range(rots):
            xa: float = math.sin(r * math.pi / rots + 0.7853981633974483) * 0.5
            za: float = math.cos(r * math.pi / rots + 0.7853981633974483) * 0.5
            x0: float = x + 0.5 - xa
            x1: float = x + 0.5 + xa
            y0: float = y + 0.0
            y1: float = y + 1.0
            z0: float = z + 0.5 - za
            z1: float = z + 0.5 + za

            t.vertexUV(x0, y1, z0, u1, v0)
            t.vertexUV(x1, y1, z1, u0, v0)
            t.vertexUV(x1, y0, z1, u0, v1)
            t.vertexUV(x0, y0, z0, u1, v1)

            t.vertexUV(x1, y1, z1, u0, v0)
            t.vertexUV(x0, y1, z0, u1, v0)
            t.vertexUV(x0, y0, z0, u1, v1)
            t.vertexUV(x1, y0, z1, u0, v1)

    def getAABB(self, x: int, y: int, z: int):
        return None

    def blocksLight(self) -> bool:
        return False

    def isSolid(self) -> bool:
        return False
