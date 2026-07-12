class KeyFrames:
    def __init__(self, func):
        self.key_frames = []
        self.func = func

    def add_frames(self, percent, data):
        self.key_frames.append((percent, data))
        return self

    def calc_index(self, t):
        for i in range(len(self.key_frames) - 1):
            if t <= self.key_frames[i + 1][0]:
                return i

    def solve(self, t):
        i = self.calc_index(t)
        frame = self.key_frames[i]
        next_frame = self.key_frames[i + 1]
        t1 = self.func.Solve((t - frame[0]) / (next_frame[0] - frame[0]))
        return frame[1] + (next_frame[1] - frame[1]) * t1
