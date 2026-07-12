package com.mojang.minecraft.world.tile;

import com.mojang.minecraft.world.World;
import com.mojang.minecraft.world.Tesselator;
import com.mojang.minecraft.particle.Particle;
import com.mojang.minecraft.particle.ParticleEngine;
import com.mojang.minecraft.phys.AABB;
import java.util.Random;

public class Block {
	/**
	 * 储存已有方块种类的数组,其下标对应方块ID,BLOCKS[id]为方块类型
	 */
	public static final Block[] BLOCKS = new Block[256];
	
	public static final Block empty = null;
	public static final Block rock = new Block(1, 1);
	public static final Block grass = new GrassTile(2);
	public static final Block dirt = new DirtTile(3, 2);
	public static final Block stoneBrick = new Block(4, 16);
	public static final Block wood = new Block(5, 4);
	public static final Block bush = new Bush(6);
	public int tex;
	public final int id;

	protected Block(int id) {
		BLOCKS[id] = this;
		this.id = id;
	}

	protected Block(int id, int tex) {
		this(id);
		this.tex = tex;
	}

	/**
	 * 绘制该方块
	 * @param t 绘制器
	 * @param world 所在世界
	 * @param layer
	 * @param x
	 * @param y
	 * @param z
	 */
	public void render(Tesselator t, World world, int layer, int x, int y, int z) {
		float c1 = 1.0F;
		float c2 = 0.8F;
		float c3 = 0.6F;

		if (shouldRenderFace(world, x, y - 1, z, layer)) {
			t.color(c1, c1, c1);
			renderFace(t, x, y, z, 0);
		}

		if (shouldRenderFace(world, x, y + 1, z, layer)) {
			t.color(c1, c1, c1);
			renderFace(t, x, y, z, 1);
		}

		if (shouldRenderFace(world, x, y, z - 1, layer)) {
			t.color(c2, c2, c2);
			renderFace(t, x, y, z, 2);
		}

		if (shouldRenderFace(world, x, y, z + 1, layer)) {
			t.color(c2, c2, c2);
			renderFace(t, x, y, z, 3);
		}

		if (shouldRenderFace(world, x - 1, y, z, layer)) {
			t.color(c3, c3, c3);
			renderFace(t, x, y, z, 4);
		}

		if (shouldRenderFace(world, x + 1, y, z, layer)) {
			t.color(c3, c3, c3);
			renderFace(t, x, y, z, 5);
		}
	}

	private boolean shouldRenderFace(World world, int x, int y, int z, int layer) {
		if (!world.isSolidBlock(x, y, z))
			if ((world.isLit(x, y, z) ^ layer == 1))
				return true;
		return false;
	}

	protected int getTexture(int face) {
		return this.tex;
	}

	/**
	 * 绘制方块面
	 * @param t 多边形绘制器
	 * @param x 方块x坐标
	 * @param y 方块y坐标
	 * @param z 方块z坐标
	 * @param face 方块的面(0~5号面)
	 */
	public void renderFace(Tesselator t, int x, int y, int z, int face) {
		int tex = getTexture(face);
		float u0 = tex % 16 / 16.0F;
		float u1 = u0 + 0.0624375F;
		
		float v0 = tex / 16 / 16.0F;
		float v1 = v0 + 0.0624375F;

		float x0 = x + 0.0F;
		float x1 = x + 1.0F;
		
		float y0 = y + 0.0F;
		float y1 = y + 1.0F;
		
		float z0 = z + 0.0F;
		float z1 = z + 1.0F;

		if (face == 0) {
			t.vertexUV(x0, y0, z1, u0, v1);
			t.vertexUV(x0, y0, z0, u0, v0);
			t.vertexUV(x1, y0, z0, u1, v0);
			t.vertexUV(x1, y0, z1, u1, v1);
		}

		if (face == 1) {
			t.vertexUV(x1, y1, z1, u1, v1);
			t.vertexUV(x1, y1, z0, u1, v0);
			t.vertexUV(x0, y1, z0, u0, v0);
			t.vertexUV(x0, y1, z1, u0, v1);
		}

		if (face == 2) {
			t.vertexUV(x0, y1, z0, u1, v0);
			t.vertexUV(x1, y1, z0, u0, v0);
			t.vertexUV(x1, y0, z0, u0, v1);
			t.vertexUV(x0, y0, z0, u1, v1);
		}

		if (face == 3) {
			t.vertexUV(x0, y1, z1, u0, v0);
			t.vertexUV(x0, y0, z1, u0, v1);
			t.vertexUV(x1, y0, z1, u1, v1);
			t.vertexUV(x1, y1, z1, u1, v0);
		}

		if (face == 4) {
			t.vertexUV(x0, y1, z1, u1, v0);
			t.vertexUV(x0, y1, z0, u0, v0);
			t.vertexUV(x0, y0, z0, u0, v1);
			t.vertexUV(x0, y0, z1, u1, v1);
		}

		if (face == 5) {
			t.vertexUV(x1, y0, z1, u0, v1);
			t.vertexUV(x1, y0, z0, u1, v1);
			t.vertexUV(x1, y1, z0, u1, v0);
			t.vertexUV(x1, y1, z1, u0, v0);
		}
	}

	public void renderFaceNoTexture(Tesselator t, int x, int y, int z, int face) {
		float x0 = x + 0.0F;
		float x1 = x + 1.0F;
		float y0 = y + 0.0F;
		float y1 = y + 1.0F;
		float z0 = z + 0.0F;
		float z1 = z + 1.0F;

		if (face == 0) {
			t.vertex(x0, y0, z1);
			t.vertex(x0, y0, z0);
			t.vertex(x1, y0, z0);
			t.vertex(x1, y0, z1);
		}

		if (face == 1) {
			t.vertex(x1, y1, z1);
			t.vertex(x1, y1, z0);
			t.vertex(x0, y1, z0);
			t.vertex(x0, y1, z1);
		}

		if (face == 2) {
			t.vertex(x0, y1, z0);
			t.vertex(x1, y1, z0);
			t.vertex(x1, y0, z0);
			t.vertex(x0, y0, z0);
		}

		if (face == 3) {
			t.vertex(x0, y1, z1);
			t.vertex(x0, y0, z1);
			t.vertex(x1, y0, z1);
			t.vertex(x1, y1, z1);
		}

		if (face == 4) {
			t.vertex(x0, y1, z1);
			t.vertex(x0, y1, z0);
			t.vertex(x0, y0, z0);
			t.vertex(x0, y0, z1);
		}

		if (face == 5) {
			t.vertex(x1, y0, z1);
			t.vertex(x1, y0, z0);
			t.vertex(x1, y1, z0);
			t.vertex(x1, y1, z1);
		}
	}

	public final AABB getBlockAABB(int x, int y, int z) {
		return new AABB(x, y, z, x + 1, y + 1, z + 1);
	}

	/**
	 * 获得该方块的AABB盒
	 * @param x
	 * @param y
	 * @param z
	 * @return
	 */
	public AABB getAABB(int x, int y, int z) {
		return new AABB(x, y, z, x + 1, y + 1, z + 1);
	}

	/**
	 * 返回该方块能否降低亮度
	 * @return
	 */
	public boolean blocksLight() {
		return true;
	}

	/**
	 * 返回该方块是不是坚硬的
	 * @return
	 */
	public boolean isSolid() {
		return true;
	}

	/**
	 * 世界刻，用于某些方块的随机更新，比如裸露泥土随机变成草方块
	 * @param world
	 * @param x
	 * @param y
	 * @param z
	 * @param random
	 */
	public void tick(World world, int x, int y, int z, Random random) {
	}

	public void destroy(World world, int x, int y, int z,
			ParticleEngine particleEngine) {
		int SD = 4;
		for (int xx = 0; xx < SD; xx++)
			for (int yy = 0; yy < SD; yy++)
				for (int zz = 0; zz < SD; zz++) {
					float xp = x + (xx + 0.5F) / SD;
					float yp = y + (yy + 0.5F) / SD;
					float zp = z + (zz + 0.5F) / SD;
					particleEngine.add(new Particle(world, xp, yp, zp, xp - x
							- 0.5F, yp - y - 0.5F, zp - z - 0.5F, this.tex));
				}
	}
}

/*
 * Location:
 * H:\Game\Minecraft1.12.2\Minecraft1.12.2\.minecraft\versions\rd-161348
 * \rd-161348.jar Qualified Name: com.mojang.minecraft.world.tile.Tile JD-Core
 * Version: 0.6.2
 */