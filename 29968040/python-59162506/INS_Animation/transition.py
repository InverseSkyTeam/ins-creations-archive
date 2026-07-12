from .easing_function import parse_easing_function, ease
from .parse_type import parse_time
import time


def lerp(t: float, key, value1, value2):
    return value1 + (value2 - value1) * t


class Transition:
    def __init__(self, transition_property: tuple, transition_duration=0,
                 transition_timing_function=ease, transition_delay=0,
                 lerp_function=lerp):
        self.lerp = lerp_function
        self.property_class, self.property, self.res = transition_property
        self.duration = transition_duration
        self.timing_function = transition_timing_function
        self.delay = transition_delay

        self.start_time = None
        self.play = False
        self.start_property = None

    def start(self):
        self.start_time = time.time() + self.delay
        self.play = True
        self.start_property = getattr(self.property_class, self.property)

    def stop(self):
        self.start_time = None
        self.play = False
        self.start_property = None

    def update(self):
        curv_time = time.time()
        if not self.play or self.start_time is None:
            return
        if curv_time < self.start_time:
            return
        if curv_time > self.start_time + self.duration:
            self.stop()
            return

        lerp_t = self.timing_function.Solve((curv_time - self.start_time) / self.duration)
        lerp_res = self.lerp(lerp_t, self.property, self.start_property, self.res)
        setattr(self.property_class, self.property, lerp_res)


def transition(transition_property: tuple, transition_duration='0s',
               transition_timing_function=ease, transition_delay='0s',
               lerp_function=lerp):
    return Transition(transition_property, parse_time(transition_duration),
                      parse_easing_function(transition_timing_function),
                      parse_time(transition_delay), lerp_function)


class TransitionGroup:
    def __init__(self):
        self.transition = []

    def add_transition(self, _transition):
        if isinstance(_transition, Transition):
            self.transition.append(_transition)
        else:
            for t in _transition:
                self.transition.append(t)

    def start(self):
        for t in self.transition:
            t.start()

    def stop(self):
        for t in self.transition:
            t.stop()

    def update(self):
        for t in self.transition:
            t.update()

    @property
    def play(self):
        return any([t.play for t in self.transition])  # 内部所有动画都结束了，才算结束
