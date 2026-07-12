package com.mojang.minecraft.character;

/**
 * @author Administrator
 * 顶点
 */
public class Vertex {
	public Vec3 pos;//顶点空间坐标
	public float u,v;//顶点二维纹理坐标


	/**
	 * 设置一个顶点
	 * @param x
	 * @param y
	 * @param z
	 * @param u
	 * @param v
	 */
	public Vertex(float x, float y, float z, float u, float v) {
		this(new Vec3(x, y, z), u, v);
	}

	/**
	 * 返回一个空间坐标相同，二维纹理坐标不同的顶点
	 * @param u
	 * @param v
	 * @return
	 */
	public Vertex remap(float u, float v) {
		return new Vertex(this, u, v);
	}

	/**
	 * 设置一个空间坐标与vertex相同，纹理坐标为UV的顶点
	 * @param vertex
	 * @param u
	 * @param v
	 */
	public Vertex(Vertex vertex, float u, float v) {
		this.pos = vertex.pos;
		this.u = u;
		this.v = v;
	}

	/**
	 * 设置一个空间坐标为pos，纹理坐标为UV的顶点
	 * @param pos
	 * @param u
	 * @param v
	 */
	public Vertex(Vec3 pos, float u, float v) {
		this.pos = pos;
		this.u = u;
		this.v = v;
	}
}

/*
 * Location:
 * H:\Game\Minecraft1.12.2\Minecraft1.12.2\.minecraft\versions\rd-161348
 * \rd-161348.jar Qualified Name: com.mojang.minecraft.character.Vertex JD-Core
 * Version: 0.6.2
 */