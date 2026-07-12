from .easing_function import parse_easing_function, ease, linear
from .parse_type import parse_time
import time


def lerp(t: float, value1, value2):
    """线性插值函数"""
    return value1 + (value2 - value1) * t


class TransitionData:
    """过渡的基础数据配置，可复用"""
    def __init__(self, transition_duration='0s',
                       transition_timing_function=ease,
                       transition_delay='0s'):
        """
        初始化过渡数据
        :param transition_duration: 过渡持续时间
        :param transition_timing_function: 缓动函数
        :param transition_delay: 延迟时间
        """
        duration = parse_time(transition_duration)
        timing_function = parse_easing_function(transition_timing_function)
        delay = parse_time(transition_delay)

        self.duration = max(duration, 0)          # 过渡持续时间（秒）
        self.timing_function = timing_function    # 缓动函数
        self.delay = delay                         # 延迟时间（秒）
        self.combine_duration = self.delay + self.duration  # 总耗时（延迟+持续时间）


class Transition:
    """表示一次具体的过渡过程（运行中的过渡实例）"""
    def __init__(self, timing_function, start_time, end_time,
                 start_value, end_value, lerp_func,
                 reverse_adjust_start_value, reverse_short_factor):
        """
        初始化过渡实例
        :param timing_function: 缓动函数
        :param start_time: 开始时间戳（秒）
        :param end_time: 结束时间戳（秒）
        :param start_value: 起始值
        :param end_value: 目标值
        :param lerp_func: 插值函数
        :param reverse_adjust_start_value: 用于反转调整的起始值（当过渡方向改变时使用）
        :param reverse_short_factor: 反转缩短因子（控制反转时的进度缩放）
        """
        self.timing_function = timing_function
        self.lerp_func = lerp_func
        self.start_time = start_time
        self.end_time = end_time
        self.start_value = start_value
        self.end_value = end_value
        self.reverse_adjust_start_value = reverse_adjust_start_value
        self.reverse_short_factor = reverse_short_factor

    def is_finished(self):
        """判断过渡是否已经完成（基于当前时间）"""
        return time.time() >= self.end_time

    def get_progress(self):
        """获取当前过渡进度（0~1），经过缓动函数映射后的值"""
        curr_time = time.time()
        duration = self.end_time - self.start_time
        assert duration >= 0

        if curr_time < self.start_time:
            return 0.0
        if curr_time >= self.end_time:
            return 1.0

        # 计算线性进度，然后通过缓动函数映射
        linear_progress = (curr_time - self.start_time) / duration
        return self.timing_function.Solve(linear_progress)

    def get_value(self):
        """根据当前进度插值得到过渡中的值"""
        progress = self.get_progress()
        return self.lerp_func(progress, self.start_value, self.end_value)


class Property:
    """管理对象某个属性的过渡行为"""
    def __init__(self, object_class, property_name, lerp_func=lerp):
        """
        :param object_class: 持有属性的对象（通常是 self 所属的实例）
        :param property_name: 属性名
        :param lerp_func: 插值函数（默认线性插值）
        """
        self.object_class = object_class
        self.name = property_name
        self.lerp_func = lerp_func

        self.transition: Transition = None           # 当前正在进行的过渡实例
        self.after_change_value = None               # 最终目标值（过渡完成后应达到的值）
        self.transition_data: TransitionData = None  # 过渡配置

    @property
    def value(self):
        """获取当前属性值"""
        return getattr(self.object_class, self.name)

    @value.setter
    def value(self, new_value):
        """设置当前属性值（直接赋值，不触发过渡）"""
        setattr(self.object_class, self.name, new_value)

    def update(self):
        """
        更新属性状态，根据 CSS 过渡规范处理：
        1. 若无过渡或过渡已完成，直接设为目标值。
        2. 若刚设置新目标值，启动新过渡。
        3. 若过渡进行中又改变了目标值，根据规范进行反转或重新开始。
        """
        # 情况1：总耗时 <= 0 → 无过渡，立即完成
        if self.transition_data.combine_duration <= 0:
            self.value = self.after_change_value
            self.transition = None
        # 情况2：没有进行中的过渡（或已结束），且当前值不等于目标值 → 开始新过渡
        elif (self.transition is None or self.transition.is_finished()) and self.value != self.after_change_value:
            start_time = time.time() + self.transition_data.delay
            self.transition = Transition(
                self.transition_data.timing_function,
                start_time,
                start_time + self.transition_data.duration,
                self.value,                # 当前值作为起始值
                self.after_change_value,
                self.lerp_func,
                self.value,                # 反转调整起始值
                1.0                        # 反转缩短因子
            )
        # 情况3：有进行中的过渡，但目标值已改变
        elif self.transition and self.transition.end_value != self.after_change_value:
            # 如果当前插值恰好等于新目标值，则直接完成
            if self.transition.get_value() == self.after_change_value:
                self.transition = None
                self.value = self.after_change_value
            # 如果新目标值等于反转调整起始值（即回到旧过渡的起始点），则进行反转缩短
            elif self.transition.reverse_adjust_start_value == self.after_change_value:
                # 计算当前进度，并乘以原有缩短因子得到新的缩短因子
                reverse_short_factor = self.transition.get_progress() * self.transition.reverse_short_factor
                reverse_short_factor += (1 - self.transition.reverse_short_factor)
                reverse_short_factor = max(min(abs(reverse_short_factor), 1), 0)

                # 计算新的开始和结束时间（延迟可能按比例缩短）
                if self.transition_data.delay >= 0:
                    start_time = time.time() + self.transition_data.delay
                else:
                    start_time = time.time() + self.transition_data.delay * reverse_short_factor
                end_time = start_time + self.transition_data.duration * reverse_short_factor

                self.transition = Transition(
                    self.transition_data.timing_function,
                    start_time,
                    end_time,
                    self.value,                 # 当前值作为起始值
                    self.after_change_value,
                    self.lerp_func,
                    self.transition.end_value,  # 旧目标值作为新的反转调整起始值
                    reverse_short_factor
                )
            else:
                # 其他情况：直接开始一个新过渡（从当前值到新目标值）
                start_time = time.time() + self.transition_data.delay
                self.transition = Transition(
                    self.transition_data.timing_function,
                    start_time,
                    start_time + self.transition_data.duration,
                    self.value,
                    self.after_change_value,
                    self.lerp_func,
                    self.value,
                    1.0
                )

        # 最后，如果存在进行中的过渡，则根据过渡结果更新属性值
        if self.transition:
            if self.transition.is_finished():
                self.value = self.transition.end_value
            else:
                self.value = self.transition.get_value()


class State:
    """定义一组属性的目标值和过渡配置（即一个“状态”）"""
    none_transition_data = TransitionData(0, linear, 0)  # 无过渡的默认配置

    def __init__(self):
        self.property = {}  # 格式：{属性名: [目标值, TransitionData对象]}

    @classmethod
    def create(cls, **kwargs):
        """
        快速创建状态，参数为 属性名 = (目标值, TransitionData对象)
        """
        new_state = cls()
        for name, data in kwargs.items():
            new_state.add_property(name, *data)
        return new_state

    def add_property(self, property_name, target_value, transition_data: TransitionData = None):
        """添加或更新一个属性的目标值和过渡配置"""
        self.property[property_name] = [target_value, transition_data or self.none_transition_data]

    def inherit_state(self, father_state: 'State'):
        """从父状态继承属性（如果当前状态没有该属性，则复制父状态的）"""
        for property_name in father_state.property:
            if property_name not in self.property:
                self.property[property_name] = father_state.property[property_name]


class TransitionGroup:
    """管理一组属性的状态切换和过渡更新"""
    def __init__(self, object_class, default_state: State, lerp_funcs: dict = None, **kwargs):
        """
        :param object_class: 持有属性的对象
        :param default_state: 默认状态
        :param lerp_funcs: 可选，指定某些属性的插值函数 {属性名: 插值函数}
        :param kwargs: 其他命名状态（状态名=State对象）
        """
        self.object_class = object_class
        self.default_state: State = default_state

        self.property = {}          # {属性名: Property对象}
        self.states = {}             # {状态名: State对象}

        # 为默认状态中的每个属性创建 Property 实例
        for property_name in self.default_state.property:
            lerp_func = lerp_funcs and lerp_funcs.get(property_name)
            self.property[property_name] = Property(object_class, property_name, lerp_func or lerp)

        self.add_states(default=default_state, **kwargs)
        self.current_state_name = 'default'
        self.set_state('default')

    def add_state(self, name, state: State):
        """添加一个命名状态，并使其继承默认状态中未定义的属性"""
        state.inherit_state(self.default_state)
        self.states[name] = state

    def add_states(self, **kwargs):
        """批量添加状态"""
        for name, state in kwargs.items():
            self.add_state(name, state)

    def update(self):
        """更新所有属性的过渡状态（通常在每一帧调用）"""
        for prop in self.property.values():
            prop.update()

    def set_state(self, new_state_name):
        """切换到指定状态，将每个属性的目标值和过渡配置更新为该状态定义的"""
        assert new_state_name in self.states
        self.current_state_name = new_state_name

        new_state = self.states[self.current_state_name]
        for property_name in self.property:
            prop = self.property[property_name]
            target_value, trans_data = new_state.property[property_name]
            prop.after_change_value = target_value
            prop.transition_data = trans_data
