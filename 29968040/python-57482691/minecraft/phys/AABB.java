package com.mojang.minecraft.phys;

/**
 * @author Administrator
 * 轴对齐碰撞盒
 * </br>若从z轴正方向的反方向看过去
 * </br>x0,y0,z0推测为左下前顶点，名为1顶点
 * </br>x0,y0,z0推测为右上后顶点，名为2顶点
 */
public class AABB {
	/**
	 * 偏移量，指发生碰撞时二者的分离距离
	 * 
	 */
	private float epsilon = 0.0F;
	public float x0;
	public float y0;
	public float z0;
	public float x1;
	public float y1;
	public float z1;

	public AABB(float x0, float y0, float z0, float x1, float y1, float z1) {
		this.x0 = x0;
		this.y0 = y0;
		this.z0 = z0;
		this.x1 = x1;
		this.y1 = y1;
		this.z1 = z1;
	}

	/**
	 * 扩大AABB盒
	 *</br> 如果xa,ya,za中的某个是负数，则1顶点的对应的坐标向对应轴的负方向扩展相应的大小
	 *</br> 比如xa = -11，则1号顶点的x坐标向x轴负方向扩展11
	 *</br> 如果xa,ya,za中的某个是正数，则2顶点的对应的坐标向对应轴的正方向扩展相应的大小
	 *</br> 比如ya = 5，则2号顶点的y坐标向y轴正方向扩展5
	 * @param xa
	 * @param ya
	 * @param za
	 * @return 返回一个扩大的AABB盒
	 */
	public AABB expand(float xa, float ya, float za) {
		float _x0 = this.x0;
		float _y0 = this.y0;
		float _z0 = this.z0;
		float _x1 = this.x1;
		float _y1 = this.y1;
		float _z1 = this.z1;

		if (xa < 0.0F)_x0 += xa;
		if (xa > 0.0F)_x1 += xa;

		if (ya < 0.0F)_y0 += ya;
		if (ya > 0.0F)_y1 += ya;

		if (za < 0.0F)_z0 += za;
		if (za > 0.0F)_z1 += za;

		return new AABB(_x0, _y0, _z0, _x1, _y1, _z1);
	}

	/**
	 * aabb盒均匀扩大(我能理解,不知道怎么描述)
	 * @param xa
	 * @param ya
	 * @param za
	 * @return
	 */
	public AABB grow(float xa, float ya, float za) {
		float _x0 = this.x0 - xa;
		float _y0 = this.y0 - ya;
		float _z0 = this.z0 - za;
		float _x1 = this.x1 + xa;
		float _y1 = this.y1 + ya;
		float _z1 = this.z1 + za;

		return new AABB(_x0, _y0, _z0, _x1, _y1, _z1);
	}

	/**
	 * 计算碰撞盒c是否能沿x轴前进xa而不碰到该碰撞盒，若可以则返回xa，若不行，则返回能前进的最大距离(指c移动这么多刚好碰到该碰撞盒)
	 * @param c
	 * @param xa 尝试前进的距离
	 * @return 
	 */
	public float clipXCollide(AABB c, float xa) {
		
		//下面两种情况AABB盒不可能相交，直接返回
		if ((c.y1 <= this.y0) || (c.y0 >= this.y1))
			return xa;
		if ((c.z1 <= this.z0) || (c.z0 >= this.z1))
			return xa;

		if ((xa > 0.0F) && (c.x1 <= this.x0)) {
			float max = this.x0 - c.x1 - this.epsilon;//计算两个碰撞盒在X轴上的最大距离，epsilon是偏移量
			if (max < xa)
				xa = max;
		}
		if ((xa < 0.0F) && (c.x0 >= this.x1)) {
			float max = this.x1 - c.x0 + this.epsilon;
			if (max > xa)
				xa = max;
		}

		return xa;
	}

	/**
	 * 计算碰撞盒c是否能沿y轴前进ya而不碰到该碰撞盒，若可以则返回ya，若不行，则返回能前进的最大距离(指c移动这么多刚好碰到该碰撞盒)
	 * @param c
	 * @param ya 尝试前进的距离
	 * @return
	 */
	public float clipYCollide(AABB c, float ya) {
		if ((c.x1 <= this.x0) || (c.x0 >= this.x1))
			return ya;
		if ((c.z1 <= this.z0) || (c.z0 >= this.z1))
			return ya;

		if ((ya > 0.0F) && (c.y1 <= this.y0)) {
			float max = this.y0 - c.y1 - this.epsilon;
			if (max < ya)
				ya = max;
		}
		if ((ya < 0.0F) && (c.y0 >= this.y1)) {
			float max = this.y1 - c.y0 + this.epsilon;
			if (max > ya)
				ya = max;
		}

		return ya;
	}

	/**
	 * 计算碰撞盒c是否能沿z轴前进za而不碰到该碰撞盒，若可以则返回za，若不行，则返回能前进的最大距离(指c移动这么多刚好碰到该碰撞盒)
	 * @param c
	 * @param za 尝试前进的距离
	 * @return
	 */
	public float clipZCollide(AABB c, float za) {
		if ((c.x1 <= this.x0) || (c.x0 >= this.x1))
			return za;
		if ((c.y1 <= this.y0) || (c.y0 >= this.y1))
			return za;

		if ((za > 0.0F) && (c.z1 <= this.z0)) {
			float max = this.z0 - c.z1 - this.epsilon;
			if (max < za)
				za = max;
		}
		if ((za < 0.0F) && (c.z0 >= this.z1)) {
			float max = this.z1 - c.z0 + this.epsilon;
			if (max > za)
				za = max;
		}

		return za;
	}

	/**
	 * 计算碰撞盒c是否与该碰撞盒相交
	 * @param c
	 * @return
	 */
	public boolean intersects(AABB c) {
		if ((c.x1 <= this.x0) || (c.x0 >= this.x1))
			return false;
		if ((c.y1 <= this.y0) || (c.y0 >= this.y1))
			return false;
		if ((c.z1 <= this.z0) || (c.z0 >= this.z1))
			return false;
		return true;
	}

	/**
	 * 移动该碰撞盒(向XYZ方向移动对应距离)
	 * @param xa
	 * @param ya
	 * @param za
	 */
	public void move(float xa, float ya, float za) {
		this.x0 += xa;
		this.y0 += ya;
		this.z0 += za;
		this.x1 += xa;
		this.y1 += ya;
		this.z1 += za;
	}
}

/*
 * Location:
 * H:\Game\Minecraft1.12.2\Minecraft1.12.2\.minecraft\versions\rd-161348
 * \rd-161348.jar Qualified Name: com.mojang.minecraft.phys.AABB JD-Core
 * Version: 0.6.2
 */