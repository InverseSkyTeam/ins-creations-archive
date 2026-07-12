package com.mojang.minecraft.world;

public abstract interface WorldListener {
	public abstract void tileChanged(int paramInt1, int paramInt2, int paramInt3);

	public abstract void lightColumnChanged(int paramInt1, int paramInt2,
			int paramInt3, int paramInt4);

	public abstract void allChanged();
}

/*
 * Location:
 * H:\Game\Minecraft1.12.2\Minecraft1.12.2\.minecraft\versions\rd-161348
 * \rd-161348.jar Qualified Name: com.mojang.minecraft.world.LevelListener
 * JD-Core Version: 0.6.2
 */