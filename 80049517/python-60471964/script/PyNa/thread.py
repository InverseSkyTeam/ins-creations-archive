from .object import NObject
from .signals import NSignal
import threading


class NThread(NObject):
    """线程类，基于 threading"""

    finished: NSignal[None]
    crashed: NSignal[Exception]

    def __init__(self, daemon=False):
        super().__init__()
        self._thread: threading.Thread = None
        self.daemon = daemon

    def run(self):
        pass

    def _thread_wrapper(self, *args, **kwargs):
        try:
            self.run(*args, **kwargs)
        except Exception as e:
            self.crashed.emit(e)
        else:
            self.finished.emit(None)

    def start(self, *args, **kwargs):
        self._thread = threading.Thread(
            target=self._thread_wrapper, args=args, kwargs=kwargs, daemon=self.daemon
        )
        self._thread.start()
    
    def stop(self):
        if self._thread:
            # 不稳定，说不定哪天就没了呢
            # 来自 threading.py
            self._thread._tstate_lock.release()
            self._thread._stop()
