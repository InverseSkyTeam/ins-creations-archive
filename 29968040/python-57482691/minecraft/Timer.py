'''
 * 游戏中的每个"行为"的经历时间以"刻(tick)"为单位执行
'''
import time


class Timer:
    NS_PER_SECOND: int = 1000000000
    MAX_NS_PER_UPDATE: int = 1000000000
    MAX_TICKS_PER_UPDATE: int = 100

    '''
     * 游戏刻发生器
     * @param ticksPerSecond 每秒钟经历多少游戏刻（TPS）
    '''
    def __init__(self, ticksPerSecond: float):
        self.ticksPerSecond: float = ticksPerSecond
        self.lastTime: int = int(time.time()*1e9)
        
        self.ticks: int = 0
        self.a: float = 0.0
        self.timeScale: float = 1.0
        self.fps: float = 0.0
        self.passedTime: float = 0.0

    # 在主线程中不停的调用该方法以生成游戏刻
    def advanceTime(self):
        now_time: int = int(time.time()*1e9)  # 当前时间（纳秒）
        passedNs: int = now_time - self.lastTime  # 计算距离上次调用过去了多少时间（纳秒）
        self.lastTime = now_time

        if passedNs < 0:
            passedNs = 0
        if passedNs > int(1e9):
            passedNs = int(1e9)

        self.fps = float(int(1e9) / passedNs)

        self.passedTime += float(passedNs) * self.timeScale * self.ticksPerSecond / 1e9

        self.ticks = int(self.passedTime)
        if self.ticks > 100:
            self.ticks = 100
        self.passedTime -= self.ticks
        self.a = self.passedTime
