package com.mojang.minecraft.world.tile;

import com.mojang.minecraft.world.World;
import java.util.Random;

public class GrassTile extends Block {
	protected GrassTile(int id) {
		super(id);
		this.tex = 3;
	}

	protected int getTexture(int face) {
		if (face == 1)
			return 0;
		if (face == 0)
			return 2;
		return 3;
	}

	public void tick(World world, int x, int y, int z, Random random) {
		if (!world.isLit(x, y, z)) {
			world.setBlock(x, y, z, Block.dirt.id);
		} else {
			for (int i = 0; i < 4; i++) {
				int xt = x + random.nextInt(3) - 1;
				int yt = y + random.nextInt(5) - 3;
				int zt = z + random.nextInt(3) - 1;
				if ((world.getBlock(xt, yt, zt) == Block.dirt.id)
						&& (world.isLit(xt, yt, zt))) {
					world.setBlock(xt, yt, zt, Block.grass.id);
				}
			}
		}
	}
}

/*
 * Location:
 * H:\Game\Minecraft1.12.2\Minecraft1.12.2\.minecraft\versions\rd-161348
 * \rd-161348.jar Qualified Name: com.mojang.minecraft.world.tile.GrassTile
 * JD-Core Version: 0.6.2
 */