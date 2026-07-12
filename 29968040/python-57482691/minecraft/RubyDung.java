package com.mojang.minecraft;

import com.mojang.minecraft.character.Zombie;
import com.mojang.minecraft.world.Chunk;
import com.mojang.minecraft.world.Frustum;
import com.mojang.minecraft.world.World;
import com.mojang.minecraft.world.WorldRenderer;
import com.mojang.minecraft.world.Tesselator;
import com.mojang.minecraft.world.tile.Block;
import com.mojang.minecraft.particle.ParticleEngine;
import java.io.IOException;
import java.io.PrintStream;
import java.nio.FloatBuffer;
import java.nio.IntBuffer;
import java.util.ArrayList;
import javax.swing.JOptionPane;
import org.lwjgl.BufferUtils;
import org.lwjgl.LWJGLException;
import org.lwjgl.input.Keyboard;
import org.lwjgl.input.Mouse;
import org.lwjgl.opengl.Display;
import org.lwjgl.opengl.DisplayMode;
import org.lwjgl.opengl.GL11;
import org.lwjgl.util.glu.GLU;

public class RubyDung implements Runnable {
	private static final boolean FULLSCREEN_MODE = false;
	private int width;
	private int height;
	private final long debug_time = 1000L;
	/**
	 * 保存烟雾数据1的float缓冲
	 */
	private FloatBuffer fogColor0 = BufferUtils.createFloatBuffer(4);
	/**
	 * 保存烟雾数据2的float缓冲
	 */
	private FloatBuffer fogColor1 = BufferUtils.createFloatBuffer(4);
	private Timer timer = new Timer(20.0F);
	private World world;
	private WorldRenderer worldRenderer;
	private Player player;
	private int paintTexture = 1;
	private ParticleEngine particleEngine;
	
	/**
	 * "僵尸"(实际上是玩家模型)集合
	 */
	private ArrayList<Zombie> zombies = new ArrayList();

	/**
	 * 视场设置(数据以int缓冲组保存)
	 */
	private IntBuffer viewportBuffer = BufferUtils.createIntBuffer(16);

	private IntBuffer selectBuffer = BufferUtils.createIntBuffer(2000);
	private HitResult hitResult = null;

	FloatBuffer lb = BufferUtils.createFloatBuffer(16);

	public void init() throws LWJGLException, IOException {
		int col0 = 16710650;
		int col1 = 920330;
		
		float fr = 0.5F;//天空盒的颜色
		float fg = 0.8F;
		float fb = 1.0F;
		//设置雾1的数据
		this.fogColor0.put(new float[]
				{
					(col0 >> 16 & 0xFF) / 255.0F,
					(col0 >> 8 & 0xFF) / 255.0F, 
					(col0 & 0xFF) / 255.0F, 
					1.0F
				}
		);
		this.fogColor0.flip();
		//设置雾2的数据
		this.fogColor1.put(new float[]
				{
				(col1 >> 16 & 0xFF) / 255.0F,
				(col1 >> 8 & 0xFF) / 255.0F, 
				(col1 & 0xFF) / 255.0F, 1.0F
				}
		);
		this.fogColor1.flip();

		//设置显示窗体大小
		Display.setDisplayMode(new DisplayMode(1024, 768));

		Display.create();
		Keyboard.create();
		Mouse.create();

		this.width = Display.getDisplayMode().getWidth();
		this.height = Display.getDisplayMode().getHeight();

		GL11.glEnable(3553);
		GL11.glShadeModel(7425);
		GL11.glClearColor(fr, fg, fb, 0.0F);
		GL11.glClearDepth(1.0D);
		GL11.glEnable(2929);
		GL11.glDepthFunc(515);
		GL11.glEnable(3008);
		GL11.glAlphaFunc(516, 0.5F);

		GL11.glMatrixMode(5889);
		GL11.glLoadIdentity();

		GL11.glMatrixMode(5888);

		this.world = new World(256, 256, 64);
		this.worldRenderer = new WorldRenderer(this.world);
		this.player = new Player(this.world);
		this.particleEngine = new ParticleEngine(this.world);

		Mouse.setGrabbed(true);

		for (int i = 0; i < 10; i++) {
			Zombie zombie = new Zombie(this.world, 128.0F, 0.0F, 128.0F);
			zombie.resetPos();
			this.zombies.add(zombie);
		}
	}

	/**
	 * 关闭游戏时进行的后续操作
	 */
	public void gameStop() {
		this.world.save();//保存地图数据

		Mouse.destroy();
		Keyboard.destroy();
		Display.destroy();
	}

	public void run() {//游戏主进程
		try {
			init();
		} catch (Exception e) {
			JOptionPane.showMessageDialog(null, e.toString(),
					"Failed to start RubyDung", 0);
			System.exit(0);
		}

		long lastTime = System.currentTimeMillis();
		int frames = 0;
		try {
			//游戏主循环开始
			do {
//				player.setPos(player.x, 70, player.z);
				this.timer.advanceTime();
				
				for (int i = 0; i < this.timer.ticks; i++) {//近两次调用中所有的游戏刻
					tick();
				}
				
				render(this.timer.a);
				
				frames++;//FPS计数
				while (System.currentTimeMillis() >= lastTime + debug_time) {//用于每秒输出调试信息
					System.out.println(frames + " fps, " + Chunk.updates);
					Chunk.updates = 0;
					lastTime += debug_time;
					frames = 0;
					
					player.turn(0, 10);
//					player.setPos(0,70, 10);
//					player.moveRelative(0, -100, 10f);
//					player.move(1, 10, 0);
				}
				
				
				if (Keyboard.isKeyDown(1))
					break;
				
			//主循环结束	
			} while (!Display.isCloseRequested());
			
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			gameStop();
		}
	}

	public void tick() {
		while (Keyboard.next()) {//响应键盘事件，做出相应操作
			if (Keyboard.getEventKeyState()) {
				if (Keyboard.getEventKey() == 28) {
					this.world.save();
				}
				if (Keyboard.getEventKey() == 2)
					this.paintTexture = 1;
				if (Keyboard.getEventKey() == 3)
					this.paintTexture = 3;
				if (Keyboard.getEventKey() == 4)
					this.paintTexture = 4;
				if (Keyboard.getEventKey() == 5)
					this.paintTexture = 5;
				if (Keyboard.getEventKey() == 7)
					this.paintTexture = 6;
				if (Keyboard.getEventKey() == 34) {
					this.zombies.add(new Zombie(this.world, this.player.x,
							this.player.y, this.player.z));
				}
			}
		}

		this.world.tick();
		this.particleEngine.tick();

		for (int i = 0; i < this.zombies.size(); i++) {
			((Zombie) this.zombies.get(i)).tick();
			if (((Zombie) this.zombies.get(i)).removed) {
				this.zombies.remove(i--);
			}
		}

		this.player.tick();
	}

	private void moveCameraToPlayer(float a) {
		GL11.glTranslatef(0.0F, 0.0F, -0.3F);
		GL11.glRotatef(this.player.xRot, 1.0F, 0.0F, 0.0F);
		GL11.glRotatef(this.player.yRot, 0.0F, 1.0F, 0.0F);

		float x = this.player.xo + (this.player.x - this.player.xo) * a;
		float y = this.player.yo + (this.player.y - this.player.yo) * a;
		float z = this.player.zo + (this.player.z - this.player.zo) * a;
		GL11.glTranslatef(-x, -y, -z);
	}

	private void setupCamera(float a) {
		GL11.glMatrixMode(5889);
		GL11.glLoadIdentity();
		GLU.gluPerspective(70.0F, this.width / this.height, 0.05F, 1000.0F);
		GL11.glMatrixMode(5888);
		GL11.glLoadIdentity();
		moveCameraToPlayer(a);
	}

	private void setupPickCamera(float a, int x, int y) {
		GL11.glMatrixMode(5889);
		GL11.glLoadIdentity();
		this.viewportBuffer.clear();
		GL11.glGetInteger(2978, this.viewportBuffer);
		this.viewportBuffer.flip();
		this.viewportBuffer.limit(16);
		GLU.gluPickMatrix(x, y, 5.0F, 5.0F, this.viewportBuffer);
		GLU.gluPerspective(70.0F, this.width / this.height, 0.05F, 1000.0F);
		GL11.glMatrixMode(5888);
		GL11.glLoadIdentity();
		moveCameraToPlayer(a);
	}

	private void pick(float a) {
		this.selectBuffer.clear();
		GL11.glSelectBuffer(this.selectBuffer);
		GL11.glRenderMode(7170);
		setupPickCamera(a, this.width / 2, this.height / 2);
		this.worldRenderer.pick(this.player, Frustum.getFrustum());
		int hits = GL11.glRenderMode(7168);
		this.selectBuffer.flip();
		this.selectBuffer.limit(this.selectBuffer.capacity());

		long closest = 0L;
		int[] names = new int[10];
		int hitNameCount = 0;
		System.out.println(hits);
		for (int i = 0; i < hits; i++) {
			int nameCount = this.selectBuffer.get();
			long minZ = this.selectBuffer.get();
			this.selectBuffer.get();

			long dist = minZ;

			if ((dist < closest) || (i == 0)) {
				closest = dist;
				hitNameCount = nameCount;
				for (int j = 0; j < nameCount; j++)
					names[j] = this.selectBuffer.get();
			} else {
				for (int j = 0; j < nameCount; j++) {
					this.selectBuffer.get();
				}
			}
		}
		if (hitNameCount > 0) {
			this.hitResult = new HitResult(names[0], names[1], names[2],
					names[3], names[4]);
		} else {
			this.hitResult = null;
		}
	}

	public void render(float a) {
		float xo = Mouse.getDX();
		float yo = Mouse.getDY();
		this.player.turn(xo, yo);
		pick(a);

		while (Mouse.next()) {
			if ((Mouse.getEventButton() == 1) && (Mouse.getEventButtonState())) {
				if (this.hitResult != null) {
					Block oldTile = Block.BLOCKS[this.world.getBlock(
							this.hitResult.x, this.hitResult.y,
							this.hitResult.z)];
					boolean changed = this.world.setBlock(this.hitResult.x,
							this.hitResult.y, this.hitResult.z, 0);
					if ((oldTile != null) && (changed)) {
						oldTile.destroy(this.world, this.hitResult.x,
								this.hitResult.y, this.hitResult.z,
								this.particleEngine);
					}
				}
			}
			if ((Mouse.getEventButton() == 0) && (Mouse.getEventButtonState())) {
				if (this.hitResult != null) {
					int x = this.hitResult.x;
					int y = this.hitResult.y;
					int z = this.hitResult.z;

					if (this.hitResult.f == 0)
						y--;
					if (this.hitResult.f == 1)
						y++;
					if (this.hitResult.f == 2)
						z--;
					if (this.hitResult.f == 3)
						z++;
					if (this.hitResult.f == 4)
						x--;
					if (this.hitResult.f == 5)
						x++;

					this.world.setBlock(x, y, z, this.paintTexture);
				}

			}

		}

		GL11.glClear(16640);
		setupCamera(a);

		GL11.glEnable(2884);

		Frustum frustum = Frustum.getFrustum();

		this.worldRenderer.updateDirtyChunks(this.player);

		setupFog(0);
		GL11.glEnable(2912);
		this.worldRenderer.render(this.player, 0);
		for (int i = 0; i < this.zombies.size(); i++) {
			Zombie zombie = (Zombie) this.zombies.get(i);
			if ((zombie.isLit()) && (frustum.isVisible(zombie.bb))) {
				((Zombie) this.zombies.get(i)).render(a);
			}
		}
		this.particleEngine.render(this.player, a, 0);
		setupFog(1);
		this.worldRenderer.render(this.player, 1);
		for (int i = 0; i < this.zombies.size(); i++) {
			Zombie zombie = (Zombie) this.zombies.get(i);
			if ((!zombie.isLit()) && (frustum.isVisible(zombie.bb))) {
				((Zombie) this.zombies.get(i)).render(a);
			}
		}
		this.particleEngine.render(this.player, a, 1);
		GL11.glDisable(2896);
		GL11.glDisable(3553);
		GL11.glDisable(2912);

		if (this.hitResult != null) {
			GL11.glDisable(3008);
			this.worldRenderer.renderHit(this.hitResult);
			GL11.glEnable(3008);
		}

		drawGui(a);

		Display.update();
	}

	private void drawGui(float a) {
		int screenWidth = this.width * 240 / this.height;
		int screenHeight = this.height * 240 / this.height;

		GL11.glClear(256);
		GL11.glMatrixMode(5889);
		GL11.glLoadIdentity();
		GL11.glOrtho(0.0D, screenWidth, screenHeight, 0.0D, 100.0D, 300.0D);
		GL11.glMatrixMode(5888);
		GL11.glLoadIdentity();
		GL11.glTranslatef(0.0F, 0.0F, -200.0F);

		GL11.glPushMatrix();
		GL11.glTranslatef(screenWidth - 16, 16.0F, 0.0F);
		Tesselator t = Tesselator.instance;
		GL11.glScalef(16.0F, 16.0F, 16.0F);
		GL11.glRotatef(30.0F, 1.0F, 0.0F, 0.0F);
		GL11.glRotatef(45.0F, 0.0F, 1.0F, 0.0F);
		GL11.glTranslatef(-1.5F, 0.5F, -0.5F);
		GL11.glScalef(-1.0F, -1.0F, 1.0F);

		int id = Textures.loadTexture("/terrain.png", 9728);
		GL11.glBindTexture(3553, id);
		GL11.glEnable(3553);
		t.init();
		Block.BLOCKS[this.paintTexture].render(t, this.world, 0, -2, 0, 0);
		t.flush();
		GL11.glDisable(3553);
		GL11.glPopMatrix();

		int wc = screenWidth / 2;
		int hc = screenHeight / 2;
		GL11.glColor4f(1.0F, 1.0F, 1.0F, 1.0F);
		t.init();
		t.vertex(wc + 1, hc - 4, 0.0F);
		t.vertex(wc - 0, hc - 4, 0.0F);
		t.vertex(wc - 0, hc + 5, 0.0F);
		t.vertex(wc + 1, hc + 5, 0.0F);

		t.vertex(wc + 5, hc - 0, 0.0F);
		t.vertex(wc - 4, hc - 0, 0.0F);
		t.vertex(wc - 4, hc + 1, 0.0F);
		t.vertex(wc + 5, hc + 1, 0.0F);
		t.flush();
	}

	private void setupFog(int i) {
		if (i == 0) {
			GL11.glFogi(2917, 2048);
			GL11.glFogf(2914, 0.001F);
			GL11.glFog(2918, this.fogColor0);
			GL11.glDisable(2896);
		} else if (i == 1) {
			GL11.glFogi(2917, 2048);
			GL11.glFogf(2914, 0.06F);
			GL11.glFog(2918, this.fogColor1);
			GL11.glEnable(2896);
			GL11.glEnable(2903);

			float br = 0.6F;
			GL11.glLightModel(2899, getBuffer(br, br, br, 1.0F));
		}
	}

	private FloatBuffer getBuffer(float a, float b, float c, float d) {
		this.lb.clear();
		this.lb.put(a).put(b).put(c).put(d);
		this.lb.flip();
		return this.lb;
	}

	public static void checkError() {
		int e = GL11.glGetError();
		if (e != 0) {
			throw new IllegalStateException(GLU.gluErrorString(e));
		}
	}

	public static void main(String[] args) throws LWJGLException {
		new Thread(new RubyDung()).start();
	}
}

/*
 * Location:
 * H:\Game\Minecraft1.12.2\Minecraft1.12.2\.minecraft\versions\rd-161348
 * \rd-161348.jar Qualified Name: com.mojang.minecraft.RubyDung JD-Core Version:
 * 0.6.2
 */