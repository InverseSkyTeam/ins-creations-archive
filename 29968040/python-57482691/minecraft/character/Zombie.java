package com.mojang.minecraft.character;

import com.mojang.minecraft.Entity;
import com.mojang.minecraft.Textures;
import com.mojang.minecraft.world.World;
import org.lwjgl.opengl.GL11;

public class Zombie extends Entity {
	public float rot;
	public float timeOffs;
	public float speed;
	public float rotA;
	private static ZombieModel zombieModel = new ZombieModel();

	public Zombie(World world, float x, float y, float z) {
		super(world);
		this.rotA = ((float) (Math.random() + 1.0D) * 0.01F);
		setPos(x, y, z);
		this.timeOffs = ((float) Math.random() * 1239813.0F);
		this.rot = ((float) (Math.random() * 3.141592653589793D * 2.0D));
		this.speed = 1.0F;
	}

	public void tick() {
		this.xo = this.x;
		this.yo = this.y;
		this.zo = this.z;
		float xa = 0.0F;
		float ya = 0.0F;

		if (this.y < -100.0F)
			remove();

		this.rot += this.rotA;
		this.rotA = ((float) (this.rotA * 0.99D));
		this.rotA = ((float) (this.rotA + (Math.random() - Math.random())
				* Math.random() * Math.random() * 0.07999999821186066D));
		xa = (float) Math.sin(this.rot);
		ya = (float) Math.cos(this.rot);

		if ((this.onGround) && (Math.random() < 0.08D)) {
			this.yd = 0.5F;
		}

		moveRelative(xa, ya, this.onGround ? 0.1F : 0.02F);

		this.yd = ((float) (this.yd - 0.08D));
		move(this.xd, this.yd, this.zd);
		this.xd *= 0.91F;
		this.yd *= 0.98F;
		this.zd *= 0.91F;

		if (this.onGround) {
			this.xd *= 0.7F;
			this.zd *= 0.7F;
		}
	}

	public void render(float a) {
		GL11.glEnable(3553);
		GL11.glBindTexture(3553, Textures.loadTexture("/char.png", 9728));

		GL11.glPushMatrix();
		double time = System.nanoTime() / 1000000000.0D * 10.0D * this.speed
				+ this.timeOffs;

		float size = 0.05833333F;
		float yy = (float) (-Math.abs(Math.sin(time * 0.6662D)) * 5.0D - 23.0D);
		GL11.glTranslatef(this.xo + (this.x - this.xo) * a, this.yo
				+ (this.y - this.yo) * a, this.zo + (this.z - this.zo) * a);
		GL11.glScalef(1.0F, -1.0F, 1.0F);
		GL11.glScalef(size, size, size);
		GL11.glTranslatef(0.0F, yy, 0.0F);
		float c = 57.29578F;
		GL11.glRotatef(this.rot * c + 180.0F, 0.0F, 1.0F, 0.0F);

		zombieModel.render((float) time);
		GL11.glPopMatrix();
		GL11.glDisable(3553);
	}
}

/*
 * Location:
 * H:\Game\Minecraft1.12.2\Minecraft1.12.2\.minecraft\versions\rd-161348
 * \rd-161348.jar Qualified Name: com.mojang.minecraft.character.Zombie JD-Core
 * Version: 0.6.2
 */