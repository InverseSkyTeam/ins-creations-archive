import time


ANIMATION = []


def lerp(t, value1, value2):
    return value1 + (value2 - value1) * t


class NumberAnimation:
    def __init__(self, obj, attr, duration,
                 running_func=None,
                 on_start_func=None,
                 on_finished_func=None):
        self.obj, self.attr = obj, attr
        self.duration = duration

        self.start_time = None
        self._running = False
        self._from = None
        self._to = None
        
        self.running_func = running_func
        self.on_start_func = on_start_func
        self.on_finished_func = on_finished_func

        ANIMATION.append(self)
    
    @property
    def running(self):
        return self._running

    def set_running(self, value):
        if value == self._running:
            return
        if not value and self._running:
            self.stop()
        else:
            self.start(*self.on_start_func())
    
    @running.setter
    def running(self, value):
        self.set_running(value)

    def start(self, _from=None, _to=None):
        self.start_time = time.time()
        self._running = True
        self._from = getattr(self.obj, self.attr) if _from is None else _from
        self._to = _to

    def stop(self):
        setattr(self.obj, self.attr, self._to)
        self.start_time = None
        self._running = False
        self._to = None

        if self.on_finished_func is not None:
            self.on_finished_func()

    def update(self):
        curv_time = time.time()
        if self.running_func is not None:
            self.set_running(self.running_func())
        if not self._running or self.start_time is None:
            return
        if curv_time < self.start_time:
            return
        if curv_time > self.start_time + self.duration:
            self.stop()
            return

        lerp_t = (curv_time - self.start_time) / self.duration
        lerp_res = lerp(lerp_t, self._from, self._to)
        setattr(self.obj, self.attr, lerp_res)


def update_all():
    for i in ANIMATION:
        i.update()


def remove(anim):
    ANIMATION.remove(anim)
