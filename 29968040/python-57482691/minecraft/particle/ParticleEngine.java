package com.mojang.minecraft.particle;

import com.mojang.minecraft.Player;
import com.mojang.minecraft.Textures;
import com.mojang.minecraft.world.World;
import com.mojang.minecraft.world.Tesselator;
import java.util.ArrayList;
import java.util.List;
import org.lwjgl.opengl.GL11;
/*
 * 粒子引擎,渲染破坏粒子效果
 */
public class ParticleEngine {
	protected World world;
	private List<Particle> particles = new ArrayList();

	public ParticleEngine(World world) {
		this.world = world;
	}

	/**
	 * 添加粒子
	 * @param p
	 */
	public void add(Particle p) {
		this.particles.add(p);
	}

	public void tick() {
		for (int i = 0; i < this.particles.size(); i++) {
			Particle p = (Particle) this.particles.get(i);
			p.tick();
			if (p.removed) {
				this.particles.remove(i--);
			}
		}
	}

	public void render(Player player, float a, int layer) {
		GL11.glEnable(3553);
		int id = Textures.loadTexture("/terrain.png", 9728);
		GL11.glBindTexture(3553, id);
		float xa = -(float) Math.cos(player.yRot * 3.141592653589793D / 180.0D);
		float za = -(float) Math.sin(player.yRot * 3.141592653589793D / 180.0D);

		float xa2 = -za
				* (float) Math.sin(player.xRot * 3.141592653589793D / 180.0D);
		float za2 = xa
				* (float) Math.sin(player.xRot * 3.141592653589793D / 180.0D);
		float ya = (float) Math.cos(player.xRot * 3.141592653589793D / 180.0D);

		Tesselator t = Tesselator.instance;
		GL11.glColor4f(0.8F, 0.8F, 0.8F, 1.0F);
		t.init();
		for (int i = 0; i < this.particles.size(); i++) {
			Particle p = (Particle) this.particles.get(i);
			if ((p.isLit() ^ layer == 1)) {
				p.render(t, a, xa, ya, za, xa2, za2);
			}
		}
		t.flush();
		GL11.glDisable(3553);
	}
}

/*
 * Location:
 * H:\Game\Minecraft1.12.2\Minecraft1.12.2\.minecraft\versions\rd-161348
 * \rd-161348.jar Qualified Name: com.mojang.minecraft.particle.ParticleEngine
 * JD-Core Version: 0.6.2
 */