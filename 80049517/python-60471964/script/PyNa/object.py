from .signals import NSignalInstance, init_signal


class NObject(object):
    """对象类"""

    def __init__(self) -> None:
        init_signal(self)

    def connect(sender: "NObject", signal: str, receiver: "NObject", member: str) -> None:
        """Qt 风格连接信号槽"""
        sender_signal = getattr(sender, signal)
        receiver_member = getattr(receiver, member)
        if not isinstance(sender_signal, NSignalInstance) or not isinstance(
            receiver_member, [function, NSignalInstance]
        ):
            raise TypeError("你正在使用错误的参数？666")
        sender_signal.connect(receiver_member)

    def disconnect(sender: "NObject", signal: str, receiver: "NObject", member: str) -> None:
        """Qt 风格取消连接信号槽"""
        sender_signal = getattr(sender, signal)
        receiver_member = getattr(receiver, member)
        if not isinstance(sender_signal, NSignalInstance) or not isinstance(
            receiver_member, [function, NSignalInstance]
        ):
            raise TypeError("你正在使用错误的参数？666")
        sender_signal.disconnect(receiver_member)
