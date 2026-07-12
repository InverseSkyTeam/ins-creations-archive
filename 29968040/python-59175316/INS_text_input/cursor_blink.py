import time


class CursorBlink:
    def __init__(self):
        self.blink_interval = 1.1
        self.start_time = time.time()  # 当前闪烁时间周期的起始时间

    @property
    def get_blink(self):
        # 计算当前时间点在周期内的位置
        time_in_cycle = (time.time() - self.start_time) % self.blink_interval
        return time_in_cycle < self.blink_interval / 2

    def create_new_cycle(self):
        self.start_time = time.time()
