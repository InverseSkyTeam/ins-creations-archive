package com.mojang.minecraft.world;

import java.util.Random;
/*
 * °ØÁÖÔëÉùÉú³ÉÆ÷
 */
public class PerlinNoiseFilter {
	Random random = new Random();
	int seed = this.random.nextInt();
	int world = 0;
	int fuzz = 16;

	public PerlinNoiseFilter(int worlds) {
		this.world = worlds;
	}

	/**
	 * 
	 * @param width
	 * @param height
	 * @return
	 */
	public int[] read(int width, int height) {
		Random random = new Random();

		int[] tmp = new int[width * height];


		int step = width >> world;
		for (int y = 0; y < height; y += step) {
			for (int x = 0; x < width; x += step) {
				tmp[(x + y * width)] = ((random.nextInt(256) - 128) * this.fuzz);
			}

		}

		for (int step1 = width >> world; step1 > 1; step1 /= 2) {
			int val = 256 * (step1 << world);
			int ss = step1 / 2;

			for (int y = 0; y < height; y += step1) {
				for (int x = 0; x < width; x += step1) {
					int ul = tmp[((x + 0) % width + (y + 0) % height * width)];
					int ur = tmp[((x + step1) % width + (y + 0) % height
							* width)];
					int dl = tmp[((x + 0) % width + (y + step1) % height
							* width)];
					int dr = tmp[((x + step1) % width + (y + step1) % height
							* width)];

					int m = (ul + dl + ur + dr) / 4 + random.nextInt(val * 2)
							- val;

					tmp[(x + ss + (y + ss) * width)] = m;
				}
			}

			for (int y = 0; y < height; y += step1) {
				for (int x = 0; x < width; x += step1) {
					int c = tmp[(x + y * width)];
					int r = tmp[((x + step1) % width + y * width)];
					int d = tmp[(x + (y + step1) % width * width)];

					int mu = tmp[((x + ss & width - 1) + (y + ss - step1 & height - 1)
							* width)];
					int ml = tmp[((x + ss - step1 & width - 1) + (y + ss & height - 1)
							* width)];
					int m = tmp[((x + ss) % width + (y + ss) % height * width)];

					int u = (c + r + m + mu) / 4 + random.nextInt(val * 2)
							- val;
					int l = (c + d + m + ml) / 4 + random.nextInt(val * 2)
							- val;

					tmp[(x + ss + y * width)] = u;
					tmp[(x + (y + ss) * width)] = l;
				}

			}

		}

		int[] result = new int[width * height];
		for (int y = 0; y < height; y++) {
			for (int x = 0; x < width; x++) {
				result[(x + y * width)] = (tmp[(x % width + y % height * width)] / 512 + 128);
			}
		}
		return result;
	}
}

/*
 * Location:
 * H:\Game\Minecraft1.12.2\Minecraft1.12.2\.minecraft\versions\rd-161348
 * \rd-161348.jar Qualified Name: com.mojang.minecraft.world.PerlinNoiseFilter
 * JD-Core Version: 0.6.2
 */