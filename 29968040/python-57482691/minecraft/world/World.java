package com.mojang.minecraft.world;

import com.mojang.minecraft.world.tile.Block;
import com.mojang.minecraft.phys.AABB;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.ArrayList;
import java.util.Random;
import java.util.zip.GZIPInputStream;
import java.util.zip.GZIPOutputStream;

public class World {
	private static final int TILE_UPDATE_INTERVAL = 400;
	public final int width;
	public final int height;
	public final int depth;
	/**
	 * 保存某位置方块信息的数组
	 */
	private byte[] blocks;
	/**
	 * 保存某位置方块亮度信息的数组
	 */
	private int[] lightDepths;
	/**
	 * 世界绘制更新监听链表
	 * </br>当世界产生变化(比如放置方块,移除方块等),就会调用这个链表里的世界绘制器来更新世界
	 * </br>在当前版本的worldRenderChangeListeners长度为1，也就是只有一个世界，推测用链表原因是为了以后的多世界(地狱，末地之类)
	 */
	private ArrayList<WorldListener> worldRenderChangeListeners = new ArrayList();
	private Random random = new Random();

	int unprocessed = 0;

	/**
	 * 设置世界的长宽高
	 * @param w
	 * @param h
	 * @param d
	 */
	public World(int w, int h, int d) {
		this.width = w;
		this.height = h;
		this.depth = d;
		this.blocks = new byte[w * h * d];//保存方块的数组
		this.lightDepths = new int[w * h];//保存方块亮度的数组

		boolean mapLoaded = load();
		if (!mapLoaded)generateMap();//没有保存的地图就新建一个地图

		calcLightDepths(0, 0, w, h);
	}

	/**
	 * 生成地图
	 */
	private void generateMap() {
		int w = this.width;
		int h = this.height;
		int d = this.depth;
		int[] heightmap1 = new PerlinNoiseFilter(0).read(w, h);
		int[] heightmap2 = new PerlinNoiseFilter(0).read(w, h);
		int[] cf = new PerlinNoiseFilter(1).read(w, h);
		int[] rockMap = new PerlinNoiseFilter(1).read(w, h);

		for (int x = 0; x < w; x++)
			for (int y = 0; y < d; y++)
				for (int z = 0; z < h; z++) {
					int dh1 = heightmap1[(x + z * this.width)];
					int dh2 = heightmap2[(x + z * this.width)];
					int cfh = cf[(x + z * this.width)];

					if (cfh < 128)
						dh2 = dh1;

					int dh = dh1;
					if (dh2 > dh)
						dh = dh2;
					else
						dh2 = dh1;
					dh = dh / 8 + d / 3;

					int rh = rockMap[(x + z * this.width)] / 8 + d / 3;
					if (rh > dh - 2)
						rh = dh - 2;

					int i = (y * this.height + z) * this.width + x;
					int id = 0;
					if (y == dh)
						id = Block.grass.id;
					if (y < dh)
						id = Block.dirt.id;
					if (y <= rh)
						id = Block.rock.id;
					this.blocks[i] = ((byte) id);
				}
	}

	/**
	 * 加载保存的地图数据(若无保存地图，则返回false)
	 * @return
	 */
	public boolean load() {
		try {
			DataInputStream dis = new DataInputStream(new GZIPInputStream(new FileInputStream(new File("world.dat"))));
			dis.readFully(this.blocks);
			calcLightDepths(0, 0, this.width, this.height);
			for (int i = 0; i < this.worldRenderChangeListeners.size(); i++)
				((WorldListener) this.worldRenderChangeListeners.get(i)).allChanged();
			dis.close();
			return true;
		} catch (Exception e) {
			e.printStackTrace();
		}
		return false;
	}

	/**
	 * 保存地图
	 */
	public void save() {
		try {
			DataOutputStream dos = new DataOutputStream(new GZIPOutputStream(
					new FileOutputStream(new File("world.dat"))));
			dos.write(this.blocks);
			dos.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * 计算亮度深度？
	 * @param x0
	 * @param y0
	 * @param x1
	 * @param y1
	 */
	public void calcLightDepths(int x0, int y0, int x1, int y1) {
		for (int x = x0; x < x0 + x1; x++)
			for (int z = y0; z < y0 + y1; z++) {
				int oldDepth = this.lightDepths[(x + z * this.width)];
				int y = this.depth - 1;
				while ((y > 0) && (!isLightBlocker(x, y, z)))
					y--;
				this.lightDepths[(x + z * this.width)] = y;

				if (oldDepth != y) {
					int yl0 = oldDepth < y ? oldDepth : y;
					int yl1 = oldDepth > y ? oldDepth : y;
					for (int i = 0; i < this.worldRenderChangeListeners.size(); i++)
						((WorldListener) this.worldRenderChangeListeners.get(i)).lightColumnChanged(x, z, yl0, yl1);
				}
			}
	}

	public void addListener(WorldListener worldListener) {
		this.worldRenderChangeListeners.add(worldListener);
	}

	public void removeListener(WorldListener worldListener) {
		this.worldRenderChangeListeners.remove(worldListener);
	}

	/**
	 * 返回世界某个地方的方块是否能降低亮度
	 * @param x
	 * @param y
	 * @param z
	 * @return
	 */
	public boolean isLightBlocker(int x, int y, int z) {
		Block block = Block.BLOCKS[getBlock(x, y, z)];
		if (block == null)
			return false;
		return block.blocksLight();
	}

	/**
	 * 返回一个AABB盒链表，内容为在aABB盒内所有方块的AABB盒
	 * @param aABB
	 * @return
	 */
	public ArrayList<AABB> getCubes(AABB aABB) {
		ArrayList aABBs = new ArrayList();
		int x0 = (int) aABB.x0;
		int x1 = (int) (aABB.x1 + 1.0F);
		int y0 = (int) aABB.y0;
		int y1 = (int) (aABB.y1 + 1.0F);
		int z0 = (int) aABB.z0;
		int z1 = (int) (aABB.z1 + 1.0F);

		if (x0 < 0)
			x0 = 0;
		if (y0 < 0)
			y0 = 0;
		if (z0 < 0)
			z0 = 0;
		if (x1 > this.width)
			x1 = this.width;
		if (y1 > this.depth)
			y1 = this.depth;
		if (z1 > this.height)
			z1 = this.height;

		for (int x = x0; x < x1; x++) {
			for (int y = y0; y < y1; y++)
				for (int z = z0; z < z1; z++) {
					Block block = Block.BLOCKS[getBlock(x, y, z)];
					if (block != null) {
						AABB aabb = block.getAABB(x, y, z);
						if (aabb != null)
							aABBs.add(aabb);
					}
				}
		}
		return aABBs;
	}

	/**
	 * 放置一个方块
	 * @param x
	 * @param y
	 * @param z
	 * @param block_id 方块ID
	 * @return 返回方块是否放置成功
	 */
	public boolean setBlock(int x, int y, int z, int block_id) {
		if ((x < 0) || (y < 0) || (z < 0) || (x >= this.width)
				|| (y >= this.depth) || (z >= this.height))
			return false;
		if (block_id == this.blocks[((y * this.height + z) * this.width + x)])
			return false;

		
		this.blocks[((y * this.height + z) * this.width + x)] = ((byte) block_id);
		calcLightDepths(x, z, 1, 1);
		for (int i = 0; i < this.worldRenderChangeListeners.size(); i++) {
			((WorldListener) this.worldRenderChangeListeners.get(i)).tileChanged(x, y, z);
		}
		return true;
	}

	/**
	 * 判断世界的某个位置是不是该亮
	 * @param x
	 * @param y
	 * @param z
	 * @return
	 */
	public boolean isLit(int x, int y, int z) {	
		if ((x < 0) || (y < 0) || (z < 0) || (x >= this.width)
				|| (y >= this.depth) || (z >= this.height))
			return true;
		return y >= this.lightDepths[(x + z * this.width)];
	}

	/**
	 * 获取世界某个坐标的方块的ID
	 * @param x
	 * @param y
	 * @param z
	 * @return
	 */
	public int getBlock(int x, int y, int z) {
		if ((x < 0) || (y < 0) || (z < 0) || (x >= this.width)
				|| (y >= this.depth) || (z >= this.height))
			return 0;
		return this.blocks[((y * this.height + z) * this.width + x)];
	}

	/**
	 * 返回世界某个地方的方块是不是坚硬(不可穿透)的
	 * @param x
	 * @param y
	 * @param z
	 * @return
	 */
	public boolean isSolidBlock(int x, int y, int z) {
		Block block = Block.BLOCKS[getBlock(x, y, z)];
		if (block == null)
			return false;
		return block.isSolid();
	}

	/**
	 * 世界刻,用来做一些有关随机变化的东西，比如暴露的泥土自动变为草方块
	 */
	public void tick() {
		this.unprocessed += this.width * this.height * this.depth;
		int ticks = this.unprocessed / 400;
		this.unprocessed -= ticks * 400;
		for (int i = 0; i < ticks; i++) {
			int x = this.random.nextInt(this.width);
			int y = this.random.nextInt(this.depth);
			int z = this.random.nextInt(this.height);
			Block tile = Block.BLOCKS[getBlock(x, y, z)];
			if (tile != null) {
				tile.tick(this, x, y, z, this.random);
			}
		}
	}
}
