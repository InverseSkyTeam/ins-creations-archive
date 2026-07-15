class NEvent[T]:
    """事件类"""

    def __init__(self, event_name: str, event_arg: T) -> None:
        self.name = event_name
        self.arg = event_arg

    def __repr__(self) -> str:
        return f"Event(name={repr(self.name)})"
