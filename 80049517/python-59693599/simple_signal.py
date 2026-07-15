from typing import TypeVar, Generic, List, Callable

T = TypeVar("T")
SIGNAL_NOT_INITED_MSG = "Signal 还未初始化哎~ 记得继承 UseSignal 哦。"


class Signal(Generic[T]):
    """信号类"""

    def emit(self, value: T) -> None:
        """推送信号"""
        raise NotImplementedError(SIGNAL_NOT_INITED_MSG)

    def connect(self, func: Callable[[T], None]) -> None:
        """添加槽函数"""
        raise NotImplementedError(SIGNAL_NOT_INITED_MSG)

    def disconnect(self, func: Callable[[T], None]) -> None:
        """移除槽函数"""
        raise NotImplementedError(SIGNAL_NOT_INITED_MSG)


class _SignalInstance(Signal, Generic[T]):
    """真正的信号类"""

    def __init__(self) -> None:
        self.slots: List[Callable[[T], None]] = []

    def emit(self, value: T) -> None:
        """推送信号"""
        slots_copy = self.slots.copy()
        for slot in slots_copy:
            slot(value)

    def connect(self, func: Callable[[T], None]) -> None:
        """添加槽函数"""
        self.slots.append(func)

    def disconnect(self, func: Callable[[T], None]) -> None:
        """移除槽函数"""
        self.slots.remove(func)


class UseSignal(object):
    """使用 Signal 记得用这个初始化"""

    def __init__(self) -> None:
        for key, value in self.__annotations__.items():
            if isinstance(value(), Signal):
                setattr(self, key, _SignalInstance())
