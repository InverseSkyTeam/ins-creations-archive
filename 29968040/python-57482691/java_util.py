import time
import numpy as np
int64 = np.int64
int32 = np.int32


def unsigned_right_shift(num, bits):
    return int64(int(num.view(np.uint64)) >> bits)


class Random:
    serialVersionUID: int = 3905348978240129619

    def __init__(self, seed: int = None):
        self.haveNextNextGaussian: bool = False
        self.nextNextGaussian: float = 0
        self.seed: int = 0
        
        if seed is None:
            seed = int(time.time() * 1000)
        self.setSeed(seed)
    
    def setSeed(self, seed: int):
        self.seed = int((int64(seed) ^ 0x5DEECE66D) & int64((1 << 48) - 1))
        self.haveNextNextGaussian = False
        
    def next(self, bits: int) -> int:
        self.seed = int((self.seed * 0x5DEECE66D + 0xB) & ((1 << 48) - 1))
        return int(int32(unsigned_right_shift(int64(self.seed), 48 - bits)))

    def nextInt(self, n: int = None) -> int:
        if n is None:
            return self.next(32)
        if n <= 0:
            raise ValueError('n must be positive')
        if n & (-n) == n:
            return int(int32(int64(n) * int64(self.next(31)) >> 31))
        bits = self.next(31)
        val = bits % n
        while bits - val + (n - 1) < 0:
            bits = self.next(31)
            val = bits % n
        return val


if __name__ == '__main__':
    a = Random(114514)
    x = time.time()
    for i in range(10):
        print(a.nextInt(36))
    y = time.time()
    print(y-x)
