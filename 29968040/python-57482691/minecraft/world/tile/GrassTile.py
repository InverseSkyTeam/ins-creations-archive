from .Block import Block


class GrassTile(Block):
	def __init__(self, _id: int):
		super().__init__(_id)
		self.tex = 3

	def getTexture(self, face: int):
		if face == 1:
			return 0
		if face == 0:
			return 2
		return 3

	def tick(self, world, x: int, y: int, z: int, random):
		if not world.isLit(x, y, z):
			world.setBlock(x, y, z, Block.dirt.id)
		else:
			for i in range(4):
				xt: int = x + random.nextInt(3) - 1
				yt: int = y + random.nextInt(5) - 3
				zt: int = z + random.nextInt(3) - 1
				if world.getBlock(xt, yt, zt) == Block.dirt.id and world.isLit(xt, yt, zt):
					world.setBlock(xt, yt, zt, Block.grass.id)
