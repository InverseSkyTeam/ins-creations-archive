from java_util import Random
from typing import List


# 柏林噪声生成器
class PerlinNoiseFilter:
    def __init__(self, worlds: int):
        self.random: Random = Random()
        self.seed: int = self.random.nextInt()
        self.fuzz: int = 16
        self.world: int = worlds

    '''
     * 
     * @param width
     * @param height
     * @return
    '''
    def read(self, width: int, height: int) -> List[int]:
        random: Random = Random()

        tmp: List[int] = [0] * (width * height)

        step: int = width >> self.world
        for y in range(0, height, step):
            for x in range(0, width, step):
                tmp[(x + y * width)] = (random.nextInt(256) - 128) * self.fuzz

        step1: int = width >> self.world
        while step1 > 1:
            val: int = 256 * (step1 << self.world)
            ss: int = step1 // 2

            for y in range(0, height, step1):
                for x in range(0, width, step1):
                    ul: int = tmp[((x + 0) % width + (y + 0) % height * width)]
                    ur: int = tmp[((x + step1) % width + (y + 0) % height * width)]
                    dl: int = tmp[((x + 0) % width + (y + step1) % height * width)]
                    dr: int = tmp[((x + step1) % width + (y + step1) % height * width)]

                    m: int = (ul + dl + ur + dr) // 4 + random.nextInt(val * 2) - val

                    tmp[(x + ss + (y + ss) * width)] = m
            for y in range(0, height, step1):
                for x in range(0, width, step1):
                    c: int = tmp[(x + y * width)]
                    r: int = tmp[((x + step1) % width + y * width)]
                    d: int = tmp[(x + (y + step1) % width * width)]

                    mu: int = tmp[((x + ss & width - 1) + (y + ss - step1 & height - 1) * width)]
                    ml: int = tmp[((x + ss - step1 & width - 1) + (y + ss & height - 1) * width)]
                    m: int = tmp[((x + ss) % width + (y + ss) % height * width)]

                    u: int = (c + r + m + mu) // 4 + random.nextInt(val * 2) - val
                    l: int = (c + d + m + ml) // 4 + random.nextInt(val * 2) - val

                    tmp[(x + ss + y * width)] = u
                    tmp[(x + (y + ss) * width)] = l
            step1 //= 2

        result: List[int] = [0] * (width * height)
        for y in range(height):
            for x in range(width):
                result[(x + y * width)] = tmp[(x % width + y % height * width)] // 512 + 128
        return result
