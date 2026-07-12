from typing import *

T = TypeVar('T')
V = TypeVar('V')


class Optional(Generic[T, V]):
    def __init__(self, v: Union[None, T]) -> None:
        self.v = v

    def set_v(self, v: Union[None, T]) -> None:
        self.v = v

    def null(self) -> bool:
        return self.v is None

    def or_else(self, _i: V) -> Union[T, V]:
        if self.null():
            return _i
        else:
            return self.v


class Stream(object):

    def __init__(self, _data: Iterable[Any]) -> None:
        self.list_data: list = list(_data)
        self.current_stamp = None

    def limit(self, number: int):
        if len(self.list_data) > number:
            self.list_data = self.list_data[:number]
        return self

    def foreach(self, func: Callable, *args, **kwargs):
        for _i in self.list_data:
            func(_i, *args, **kwargs)
        return self

    def map(self, func: Callable, *args, **kwargs) :
        for index in range(len(self.list_data)):
            self.list_data[index] = func(self.list_data[index], *args, **kwargs)
        return self

    def filter(self, func: Callable, *args, **kwargs) :
        rm_count: int = 0
        rm_index: list[int] = []
        for index in range(len(self.list_data)):
            if not func(self.list_data[index], *args, **kwargs):
                rm_index.append(index - rm_count)
                rm_count += 1
        for i in rm_index:
            self.list_data.pop(i)
        return self

    def to_list(self):
        return self.list_data

    def sort(self, reverse: bool = False) :
        self.list_data.sort(reverse=reverse)
        return self

    def find_all(self, func: Callable, *args, **kwargs):
        filter_data = []
        for _i in self.list_data:
            if func(_i, *args, **kwargs):
                filter_data.append(_i)
        return Stream.of(filter_data)

    def find_first(self, func: Callable, *args, **kwargs) -> Optional[Any, Any]:
        return_v = Optional[Any, Any](None)
        for _i in self.list_data:
            if func(_i, *args, **kwargs):
                return_v.set_v(_i)
                return return_v
        return return_v

    def null(self) -> bool:
        return len(self.list_data) == 0

    def do(self, func: Callable, *args, **kwargs):
        func(*args, **kwargs)
        return self

    @staticmethod
    def of(*args):
        if len(args) == 1 and isinstance(args, Iterable):
            return Stream(args[0])
        else:
            return Stream(args)


def equals(_i: Iterable) -> bool:
    last_v: Any = None
    for i in _i:
        if (last_v is not None) and (last_v != i):
            return False
        last_v = i
    return True


def equals_any(_i: Iterable) -> bool:
    return len(set(_i)) < len(list(_i))  # 集合除重
