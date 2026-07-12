package com.mojang.minecraft;
/*
 * 游戏中的每个"行为"的经历时间以"刻(tick)"为单位执行
 */
public class Timer {
	private static final long NS_PER_SECOND = 1000000000L;
	private static final long MAX_NS_PER_UPDATE = 1000000000L;
	private static final int MAX_TICKS_PER_UPDATE = 100;
	private float ticksPerSecond;
	private long lastTime;
	
	
	public int ticks;
	public float a;
	public float timeScale = 1.0F;
	public float fps = 0.0F;
	public float passedTime = 0.0F;

	/**
	 * 游戏刻发生器
	 * @param ticksPerSecond 每秒钟经历多少游戏刻
	 */
	public Timer(float ticksPerSecond) {
		this.ticksPerSecond = ticksPerSecond;
		this.lastTime = System.nanoTime();
	}

	/**
	 * 在主线程中不停的调用该方法以生成游戏刻
	 */
	public void advanceTime() {
		long now_time = System.nanoTime();
		long passedNs = now_time - this.lastTime;//计算距离上次调用过去了多少时间
		this.lastTime = now_time;

		if (passedNs < 0L)
			passedNs = 0L;
		if (passedNs > 1000000000L)
			passedNs = 1000000000L;

		this.fps = ((float) (1000000000L / passedNs));

		this.passedTime += (float) passedNs * this.timeScale
				* this.ticksPerSecond / 1.0E+009F;

		this.ticks = ((int) this.passedTime);
		if (this.ticks > 100)
			this.ticks = 100;
		this.passedTime -= this.ticks;
		this.a = this.passedTime;
	}
}

/*
 * Location:
 * H:\Game\Minecraft1.12.2\Minecraft1.12.2\.minecraft\versions\rd-161348
 * \rd-161348.jar Qualified Name: com.mojang.minecraft.Timer JD-Core Version:
 * 0.6.2
 */