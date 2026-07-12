package com.mojang.minecraft.character;

/**
 * @author Administrator
 * 3维向量
 */
public class Vec3 {
	public float x;
	public float y;
	public float z;

	public Vec3(float x, float y, float z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}

	/**
	 * 返回一个该向量与t向量之间的差值向量
	 * @param t
	 * @param p
	 * @return 差值向量
	 */
	public Vec3 interpolateTo(Vec3 t, float p) {
		float xt = this.x + (t.x - this.x) * p;
		float yt = this.y + (t.y - this.y) * p;
		float zt = this.z + (t.z - this.z) * p;

		return new Vec3(xt, yt, zt);
	}

	/**
	 * 设置向量
	 * @param x
	 * @param y
	 * @param z
	 */
	public void set(float x, float y, float z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}
}

/*
 * Location:
 * H:\Game\Minecraft1.12.2\Minecraft1.12.2\.minecraft\versions\rd-161348
 * \rd-161348.jar Qualified Name: com.mojang.minecraft.character.Vec3 JD-Core
 * Version: 0.6.2
 */