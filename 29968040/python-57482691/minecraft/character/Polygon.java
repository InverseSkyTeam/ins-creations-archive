package com.mojang.minecraft.character;

import org.lwjgl.opengl.GL11;

/**
 * @author Administrator
 * 多边形绘制器(其实是矩形)
 */
public class Polygon {
	public Vertex[] vertices;
	/**
	 * 顶点计数
	 */
	public int vertexCount = 0;

	public Polygon(Vertex[] vertices) {
		this.vertices = vertices;
		this.vertexCount = vertices.length;
	}

	/**
	 * 多边形绘制设置(其实是矩形，因为看后面绑定的纹理坐标就知道只有四个顶点)
	 * @param vertices 多边形顶点数组
	 * @param u0 纹理的左下角x坐标
	 * @param v0 纹理的左下角y坐标
	 * @param u1 纹理的右上角x坐标
	 * @param v1 纹理的右上角y坐标
	 */
	public Polygon(Vertex[] vertices, int u0, int v0, int u1, int v1) {
		this(vertices);

		vertices[0] = vertices[0].remap(u1, v0);
		vertices[1] = vertices[1].remap(u0, v0);
		vertices[2] = vertices[2].remap(u0, v1);
		vertices[3] = vertices[3].remap(u1, v1);
	}

	/**
	 * 绘制多边形(划掉)
	 */
	public void render() {
		GL11.glColor3f(1.0F, 1.0F, 1.0F);
		for (int i = 3; i >= 0; i--) {
			Vertex v = this.vertices[i];
			GL11.glTexCoord2f(v.u / 63.999001F, v.v / 31.999001F);
			GL11.glVertex3f(v.pos.x, v.pos.y, v.pos.z);
		}
	}
}

/*
 * Location:
 * H:\Game\Minecraft1.12.2\Minecraft1.12.2\.minecraft\versions\rd-161348
 * \rd-161348.jar Qualified Name: com.mojang.minecraft.character.Polygon JD-Core
 * Version: 0.6.2
 */