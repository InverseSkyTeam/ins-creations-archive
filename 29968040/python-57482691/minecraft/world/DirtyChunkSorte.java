package com.mojang.minecraft.world;

import com.mojang.minecraft.Player;
import java.util.Comparator;

public class DirtyChunkSorter implements Comparator<Chunk> {
	private Player player;
	private Frustum frustum;
	private long now = System.currentTimeMillis();

	public DirtyChunkSorter(Player player, Frustum frustum) {
		this.player = player;
		this.frustum = frustum;
	}

	public int compare(Chunk c0, Chunk c1) {
		boolean i0 = this.frustum.isVisible(c0.aabb);
		boolean i1 = this.frustum.isVisible(c1.aabb);
		if ((i0) && (!i1))
			return -1;
		if ((i1) && (!i0))
			return 1;
		int t0 = (int) ((this.now - c0.dirtiedTime) / 2000L);
		int t1 = (int) ((this.now - c1.dirtiedTime) / 2000L);
		if (t0 < t1)
			return -1;
		if (t0 > t1)
			return 1;
		return c0.distanceToSqr(this.player) < c1.distanceToSqr(this.player)
				? -1
				: 1;
	}
}

/*
 * Location:
 * H:\Game\Minecraft1.12.2\Minecraft1.12.2\.minecraft\versions\rd-161348
 * \rd-161348.jar Qualified Name: com.mojang.minecraft.world.DirtyChunkSorter
 * JD-Core Version: 0.6.2
 */