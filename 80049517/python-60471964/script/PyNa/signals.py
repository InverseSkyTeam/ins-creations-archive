from typing import Callable

SIGNAL_NOT_INITED_MSG = "NSignal 还未初始化哎~ 记得继承 NObject 或 init_signal 哦。"


class NSignal[T]:
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

    __call__ = emit


class NSignalInstance[T](NSignal):
    """真正的信号类"""

    def __init__(self) -> None:
        self.slots: list[Callable[[T], None]] = []

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

    __call__ = emit


def init_signal(obj: object):
    for key, value in obj.__annotations__.items():
        if getattr(value, "__origin__", None) and value.__origin__ == NSignal:
            setattr(obj, key, NSignalInstance())
            
