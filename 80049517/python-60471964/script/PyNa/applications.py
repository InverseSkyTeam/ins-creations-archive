from .object import NObject
from .event import NEvent
from .exceptions import NMultiInstanceException
from typing import Self


class NCoreApplication(NObject):
    """核心 application 实现"""

    INSTANCE: "NCoreApplication" = None

    def __new__(cls, *args, **kwargs) -> Self:
        if NCoreApplication.INSTANCE is not None:
            raise NMultiInstanceException("谁让你创建多个 Application 的？操！")
        obj = super().__new__(cls)
        NCoreApplication.INSTANCE = obj
        return obj

    @staticmethod
    def has_created() -> bool:
        return NCoreApplication.INSTANCE is not None

    def __init__(self) -> None:
        super().__init__()
        self.events: list[NEvent] = []

    def push_event(self, event: NEvent) -> None:
        if not isinstance(event, NEvent):
            raise TypeError("泥...泥...泥...用错参数了呢")
        self.events.append(event)

    def get_events(self) -> list[NEvent]:
        events_copy = self.events.copy()
        self.events.clear()
        return events_copy
