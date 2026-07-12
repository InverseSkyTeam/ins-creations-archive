from .PerlinNoiseFilter import PerlinNoiseFilter
from java_util import Random
from .tile import Block
import gzip


class World:
    TILE_UPDATE_INTERVAL: int = 400

    '''
     * 设置世界的长宽高
     * @param w
     * @param h
     * @param d
    '''
    def __init__(self, w: int, h: int, d: int):
        self.width = w
        self.height = h
        self.depth = d
        self.blocks = bytearray(w * h * d)  # 保存方块的数组
        self.lightDepths = [0] * (w * h)  # 保存方块亮度的数组

        '''
         * 世界绘制更新监听链表
         * 当世界产生变化(比如放置方块,移除方块等),就会调用这个链表里的世界绘制器来更新世界
         * 在当前版本的worldRenderChangeListeners长度为1，也就是只有一个世界，推测用链表原因是为了以后的多世界(地狱，末地之类)
        '''
        self.worldRenderChangeListeners = []
        self.random = Random()
        self.unprocessed: int = 0

        mapLoaded: bool = self.load()
        if not mapLoaded:
            self.generateMap()  # 没有保存的地图就新建一个地图
            self.calcLightDepths(0, 0, w, h)

    # 生成地图
    def generateMap(self):
        w: int = self.width
        h: int = self.height
        d: int = self.depth
        heightmap1 = PerlinNoiseFilter(0).read(w, h)
        heightmap2 = PerlinNoiseFilter(0).read(w, h)
        cf = PerlinNoiseFilter(1).read(w, h)
        rockMap = PerlinNoiseFilter(1).read(w, h)

        for x in range(w):
            for y in range(d):
                for z in range(h):
                    dh1: int = heightmap1[x + z * self.width]
                    dh2: int = heightmap2[x + z * self.width]
                    cfh: int = cf[x + z * self.width]

                    if cfh < 128:
                        dh2 = dh1

                    dh: int = dh1
                    if dh2 > dh:
                        dh = dh2
                    else:
                        dh2 = dh1
                    dh = dh // 8 + d // 3

                    rh: int = rockMap[x + z * self.width] // 8 + d // 3
                    if rh > dh - 2:
                        rh = dh - 2

                    i: int = (y * self.height + z) * self.width + x
                    _id: int = 0
                    if y == dh:
                        _id = Block.grass.id
                    if y < dh:
                        _id = Block.dirt.id
                    if y <= rh:
                        _id = Block.rock.id
                    self.blocks[i] = _id

    # 加载保存的地图数据(若无保存地图，则返回False)
    def load(self) -> bool:
        try:
            with open('world.dat', 'rb') as f:
                self.blocks = bytearray(gzip.decompress(f.read()))
                self.calcLightDepths(0, 0, self.width, self.height)
                for i in self.worldRenderChangeListeners:
                    i.allChanged()
            return True
        except Exception as e:
            print(e)
        return False

    # 保存地图
    def save(self):
        try:
            with open('world.dat', 'wb') as f:
                f.write(gzip.compress(self.blocks))
        except Exception as e:
            print(e)

    # 计算亮度深度？
    def calcLightDepths(self, x0: int, y0: int, x1: int, y1: int):
        for x in range(x0, x0 + x1):
            for z in range(y0, y0 + y1):
                oldDepth: int = self.lightDepths[x + z * self.width]
                y: int = self.depth - 1

                while y > 0 and (not Block.BLOCKS[self.blocks[(y * self.height + z) * self.width + x]] or not Block.BLOCKS[self.blocks[(y * self.height + z) * self.width + x]].blocksLight()):
                    y -= 1
                self.lightDepths[x + z * self.width] = y

                if oldDepth != y:
                    yl0: int = oldDepth if oldDepth < y else y
                    yl1: int = oldDepth if oldDepth > y else y
                    for i in self.worldRenderChangeListeners:
                        i.lightColumnChanged(x, z, yl0, yl1)

    def addListener(self, worldListener):
        self.worldRenderChangeListeners.append(worldListener)

    def removeListener(self, worldListener):
        self.worldRenderChangeListeners.remove(worldListener)

    # 返回世界某个地方的方块是否能降低亮度
    def isLightBlocker(self, x: int, y: int, z: int) -> bool:
        block = Block.BLOCKS[self.getBlock(x, y, z)]
        if block is None:
            return False
        return block.blocksLight()

    # 返回一个AABB盒链表，内容为在aABB盒内所有方块的AABB盒
    def getCubes(self, aABB):
        aABBs = []
        x0: int = int(aABB.x0)
        x1: int = int(aABB.x1 + 1.0)
        y0: int = int(aABB.y0)
        y1: int = int(aABB.y1 + 1.0)
        z0: int = int(aABB.z0)
        z1: int = int(aABB.z1 + 1.0)

        if x0 < 0:
            x0 = 0
        if y0 < 0:
            y0 = 0
        if z0 < 0:
            z0 = 0
        if x1 > self.width:
            x1 = self.width
        if y1 > self.depth:
            y1 = self.depth
        if z1 > self.height:
            z1 = self.height

        for x in range(x0, x1):
            for y in range(y0, y1):
                for z in range(z0, z1):
                    block: Block = Block.BLOCKS[self.getBlock(x, y, z)]
                    if block is not None:
                        aabb = block.getAABB(x, y, z)
                        if aabb is not None:
                            aABBs.append(aabb)
        return aABBs

    '''
     * 放置一个方块
     * @param x
     * @param y
     * @param z
     * @param block_id 方块ID
     * @return 返回方块是否放置成功
    '''
    def setBlock(self, x: int, y: int, z: int, block_id: int):
        if x < 0 or y < 0 or z < 0 or x >= self.width or y >= self.depth or z >= self.height:
            return False
        if block_id == self.blocks[(y * self.height + z) * self.width + x]:
            return False

        self.blocks[(y * self.height + z) * self.width + x] = block_id
        self.calcLightDepths(x, z, 1, 1)
        for i in self.worldRenderChangeListeners:
            i.tileChanged(x, y, z)
        return True

    # 判断世界的某个位置是不是该亮
    def isLit(self, x: int, y: int, z: int) -> bool:
        if x < 0 or y < 0 or z < 0 or x >= self.width or y >= self.depth or z >= self.height:
            return True
        return y >= self.lightDepths[x + z * self.width]

    # 获取世界某个坐标的方块的ID
    def getBlock(self, x: int, y: int, z: int):
        if x < 0 or y < 0 or z < 0 or x >= self.width or y >= self.depth or z >= self.height:
            return 0
        return self.blocks[(y * self.height + z) * self.width + x]

    # 返回世界某个地方的方块是不是坚硬(不可穿透)的
    def isSolidBlock(self, x: int, y: int, z: int):
        block: Block = Block.BLOCKS[self.getBlock(x, y, z)]
        if block is None:
            return False
        return block.isSolid()

    # 世界刻，用来做一些有关随机变化的东西，比如暴露的泥土自动变为草方块
    def tick(self):
        self.unprocessed += self.width * self.height * self.depth
        ticks: int = self.unprocessed // 400
        self.unprocessed -= ticks * 400
        # for i in range(ticks):
        #     x: int = self.random.nextInt(self.width)
        #     y: int = self.random.nextInt(self.depth)
        #     z: int = self.random.nextInt(self.height)
        #     tile: Block = Block.BLOCKS[self.getBlock(x, y, z)]
        #     if tile is not None:
        #         tile.tick(self, x, y, z, self.random)
