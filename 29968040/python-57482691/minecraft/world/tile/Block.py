from minecraft.particle import Particle
from minecraft.phys import AABB


class Block:
    # 储存已有方块种类的数组,其下标对应方块ID,BLOCKS[id]为方块类型
    BLOCKS = [None] * 256  # Block[256]
    
    empty = None  # null
    rock = None  # Block(1, 1)
    grass = None  # GrassTile(2)
    dirt = None  # DirtTile(3, 2)
    stoneBrick = None  # Block(4, 16)
    wood = None  # Block(5, 4)
    bush = None  # Bush(6)
    
    def __init__(self, _id: int, tex: int = 0):
        Block.BLOCKS[_id] = self
        self.id = _id
        self.tex = tex

    '''
     * 绘制该方块
     * @param t 绘制器
     * @param world 所在世界
     * @param layer
     * @param x
     * @param y
     * @param z
    '''
    def render(self, t, world, layer: int, x: int, y: int, z: int):
        c1: float = 1.0
        c2: float = 0.8
        c3: float = 0.6

        if self.shouldRenderFace(world, x, y - 1, z, layer):
            t.color(c1, c1, c1)
            self.renderFace(t, x, y, z, 0)

        if self.shouldRenderFace(world, x, y + 1, z, layer):
            t.color(c1, c1, c1)
            self.renderFace(t, x, y, z, 1)

        if self.shouldRenderFace(world, x, y, z - 1, layer):
            t.color(c2, c2, c2)
            self.renderFace(t, x, y, z, 2)

        if self.shouldRenderFace(world, x, y, z + 1, layer):
            t.color(c2, c2, c2)
            self.renderFace(t, x, y, z, 3)

        if self.shouldRenderFace(world, x - 1, y, z, layer):
            t.color(c3, c3, c3)
            self.renderFace(t, x, y, z, 4)

        if self.shouldRenderFace(world, x + 1, y, z, layer):
            t.color(c3, c3, c3)
            self.renderFace(t, x, y, z, 5)

    def shouldRenderFace(self, world, x: int, y: int, z: int, layer: int) -> bool:
        if not world.isSolidBlock(x, y, z):
            if world.isLit(x, y, z) ^ layer == 1:
                return True
        return False

    def getTexture(self, face: int) -> int:
        return self.tex

    '''
     * 绘制方块面
     * @param t 多边形绘制器
     * @param x 方块x坐标
     * @param y 方块y坐标
     * @param z 方块z坐标
     * @param face 方块的面(0~5号面)
    '''
    def renderFace(self, t, x: int, y: int, z: int, face: int):
        tex: int = self.getTexture(face)
        u0: float = tex % 16 / 16.0
        u1: float = u0 + 0.0624375
        
        v0: float = (tex // 16) / 16.0
        v1: float = v0 + 0.0624375

        x0: float = x + 0.0
        x1: float = x + 1.0
        
        y0: float = y + 0.0
        y1: float = y + 1.0
        
        z0: float = z + 0.0
        z1: float = z + 1.0

        if face == 0:
            t.vertexUV(x0, y0, z1, u0, v1)
            t.vertexUV(x0, y0, z0, u0, v0)
            t.vertexUV(x1, y0, z0, u1, v0)
            t.vertexUV(x1, y0, z1, u1, v1)

        if face == 1:
            t.vertexUV(x1, y1, z1, u1, v1)
            t.vertexUV(x1, y1, z0, u1, v0)
            t.vertexUV(x0, y1, z0, u0, v0)
            t.vertexUV(x0, y1, z1, u0, v1)

        if face == 2:
            t.vertexUV(x0, y1, z0, u1, v0)
            t.vertexUV(x1, y1, z0, u0, v0)
            t.vertexUV(x1, y0, z0, u0, v1)
            t.vertexUV(x0, y0, z0, u1, v1)

        if face == 3:
            t.vertexUV(x0, y1, z1, u0, v0)
            t.vertexUV(x0, y0, z1, u0, v1)
            t.vertexUV(x1, y0, z1, u1, v1)
            t.vertexUV(x1, y1, z1, u1, v0)

        if face == 4:
            t.vertexUV(x0, y1, z1, u1, v0)
            t.vertexUV(x0, y1, z0, u0, v0)
            t.vertexUV(x0, y0, z0, u0, v1)
            t.vertexUV(x0, y0, z1, u1, v1)

        if face == 5:
            t.vertexUV(x1, y0, z1, u0, v1)
            t.vertexUV(x1, y0, z0, u1, v1)
            t.vertexUV(x1, y1, z0, u1, v0)
            t.vertexUV(x1, y1, z1, u0, v0)

    def renderFaceNoTexture(self, t, x: int, y: int, z: int, face: int):
        x0: float = x + 0.0
        x1: float = x + 1.0
        y0: float = y + 0.0
        y1: float = y + 1.0
        z0: float = z + 0.0
        z1: float = z + 1.0

        if face == 0:
            t.vertex(x0, y0, z1)
            t.vertex(x0, y0, z0)
            t.vertex(x1, y0, z0)
            t.vertex(x1, y0, z1)

        if face == 1:
            t.vertex(x1, y1, z1)
            t.vertex(x1, y1, z0)
            t.vertex(x0, y1, z0)
            t.vertex(x0, y1, z1)

        if face == 2:
            t.vertex(x0, y1, z0)
            t.vertex(x1, y1, z0)
            t.vertex(x1, y0, z0)
            t.vertex(x0, y0, z0)

        if face == 3:
            t.vertex(x0, y1, z1)
            t.vertex(x0, y0, z1)
            t.vertex(x1, y0, z1)
            t.vertex(x1, y1, z1)

        if face == 4:
            t.vertex(x0, y1, z1)
            t.vertex(x0, y1, z0)
            t.vertex(x0, y0, z0)
            t.vertex(x0, y0, z1)

        if face == 5:
            t.vertex(x1, y0, z1)
            t.vertex(x1, y0, z0)
            t.vertex(x1, y1, z0)
            t.vertex(x1, y1, z1)

    def getBlockAABB(self, x: int, y: int, z: int) -> AABB:
        return AABB(x, y, z, x + 1, y + 1, z + 1)

    '''
     * 获得该方块的AABB盒
     * @param x
     * @param y
     * @param z
     * @return
    '''
    def getAABB(self, x: int, y: int, z: int) -> AABB:
        return AABB(x, y, z, x + 1, y + 1, z + 1)

    '''
     * 返回该方块能否降低亮度
     * @return
    '''
    def blocksLight(self):
        return True

    '''
     * 返回该方块是不是坚硬的
     * @return
    '''
    def isSolid(self):
        return True

    '''
     * 世界刻，用于某些方块的随机更新，比如裸露泥土随机变成草方块
     * @param world
     * @param x
     * @param y
     * @param z
     * @param random
    '''
    def tick(self, world, x: int, y: int, z: int, random):
        pass

    def destroy(self, world, x: int, y: int, z: int, particleEngine):
        SD: int = 4
        for xx in range(SD):
            for yy in range(SD):
                for zz in range(SD):
                    xp: float = x + (xx + 0.5) / SD
                    yp: float = y + (yy + 0.5) / SD
                    zp: float = z + (zz + 0.5) / SD
                    particleEngine.add(Particle(world, xp, yp, zp, 
                                                xp - x - 0.5, 
                                                yp - y - 0.5, 
                                                zp - z - 0.5, 
                                                self.tex))
