package com.mojang.minecraft;

import com.mojang.minecraft.world.World;
import com.mojang.minecraft.phys.AABB;
import java.util.List;

public class Entity {
	protected World world;
	//
	public float xo;
	public float yo;
	public float zo;
	
	//实体中心的世界位置(本质上是实体包围盒的中心位置)
	public float x;
	public float y;
	public float z;
	
	//速度向量
	public float xd;
	public float yd;
	public float zd;
	
	//该实体绕某个轴的旋转角度
	public float yRot;
	public float xRot;
	
	//该实体的AABB盒
	public AABB bb;
	
	//标记是否接触地面
	public boolean onGround = false;
	//标记是否被移除
	public boolean removed = false;
	protected float heightOffset = 0.0F;

	protected float bbWidth = 0.6F;
	protected float bbHeight = 1.8F;

	public Entity(World world) {
		this.world = world;
		resetPos();
	}

	/**
	 * 重置实体位置(随机)
	 */
	protected void resetPos() {
		float x = (float) Math.random() * this.world.width;
		float y = this.world.depth + 10;
		float z = (float) Math.random() * this.world.height;
		setPos(x, y, z);
	}

	/**
	 * 移除实体
	 */
	public void remove() {
		this.removed = true;
	}

	/**
	 * 设置包裹整个实体的AABB盒的大小(一个长方体，底部为正方形，边长为w)
	 * @param w
	 * @param h
	 */
	protected void setSize(float w, float h) {
		this.bbWidth = w;
		this.bbHeight = h;
	}

	/**
	 * 设置实体中心位置
	 * @param x
	 * @param y
	 * @param z
	 */
	protected void setPos(float x, float y, float z) {
		this.x = x;
		this.y = y;
		this.z = z;
		float w = this.bbWidth / 2.0F;
		float h = this.bbHeight / 2.0F;
		this.bb = new AABB(x - w, y - h, z - w, x + w, y + h, z + w);
	}


	/**
	 * 将自身绕x,y轴旋转(坐标系为当前实体自身坐标系)
	 * @param y_rot
	 * @param x_rot
	 */
	public void turn(float y_rot,float x_rot) {
		this.yRot = ((float) (this.yRot + y_rot * 0.15D));
		this.xRot = ((float) (this.xRot - x_rot * 0.15D));
		if (this.xRot < -90.0F)
			this.xRot = -90.0F;
		if (this.xRot > 90.0F)
			this.xRot = 90.0F;
	}

	/**
	 * 游戏刻
	 */
	public void tick() {
		this.xo = this.x;
		this.yo = this.y;
		this.zo = this.z;
	}

	/**
	 * 尝试将该实体移动到(xa,ya,za)[世界坐标系]
	 * <br>注:游戏逻辑里经常将速度与位移的概念混用，经常有move(xd,yd,zd)的用法[常见于tick方法里]
	 * @param xa
	 * @param ya
	 * @param za
	 */
	public void move(float xa, float ya, float za) {
		float xaOrg = xa;
		float yaOrg = ya;
		float zaOrg = za;

		List aABBs = this.world.getCubes(this.bb.expand(xa, ya, za));

		
		for (int i = 0; i < aABBs.size(); i++)
			ya = ((AABB) aABBs.get(i)).clipYCollide(this.bb, ya);
		this.bb.move(0.0F, ya, 0.0F);

		for (int i = 0; i < aABBs.size(); i++)
			xa = ((AABB) aABBs.get(i)).clipXCollide(this.bb, xa);
		this.bb.move(xa, 0.0F, 0.0F);

		for (int i = 0; i < aABBs.size(); i++)
			za = ((AABB) aABBs.get(i)).clipZCollide(this.bb, za);
		this.bb.move(0.0F, 0.0F, za);

		
		this.onGround = ((yaOrg != ya) && (yaOrg < 0.0F));

		if (xaOrg != xa)
			this.xd = 0.0F;
		if (yaOrg != ya)
			this.yd = 0.0F;
		if (zaOrg != za)
			this.zd = 0.0F;

		//更新实体中心位置
		this.x = ((this.bb.x0 + this.bb.x1) / 2.0F);
		this.y = (this.bb.y0 + this.heightOffset);
		this.z = ((this.bb.z0 + this.bb.z1) / 2.0F);
	}

	/**
	 * 相对自身坐标系的移动(自身坐标系：玩家正视方向为z轴负方向(什么反人类设定),玩家右侧为x轴正方向)
	 * </br>
	 * </br>(xa,ya)是移动方向向量,speed是移动速度
	 * @param xa 
	 * @param za 
	 * @param speed 移动速度
	 */
	public void moveRelative(float xa, float za, float speed) {
		float dist = xa * xa + za * za;
		if (dist < 0.01F)
			return;

		dist = speed / (float) Math.sqrt(dist);
		
		xa *= dist;
		za *= dist;

		float sin = (float) Math.sin(this.yRot * 3.141592653589793D / 180.0D);
		float cos = (float) Math.cos(this.yRot * 3.141592653589793D / 180.0D);

		//计算其在世界坐标系中的速度向量，并与原速度向量叠加
		this.xd += xa * cos - za * sin;
		this.zd += za * cos + xa * sin;
	}

	public boolean isLit() {
		int xTile = (int) this.x;
		int yTile = (int) this.y;
		int zTile = (int) this.z;
		return this.world.isLit(xTile, yTile, zTile);
	}
}

/*
 * Location:
 * H:\Game\Minecraft1.12.2\Minecraft1.12.2\.minecraft\versions\rd-161348
 * \rd-161348.jar Qualified Name: com.mojang.minecraft.Entity JD-Core Version:
 * 0.6.2
 */