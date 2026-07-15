import time
import traceback


class Logger(object):
    def __init__(self, name: str = "main"):
        self.name = name
    
    def _log(self, level, messages, format="") -> None:
        if len(level) < 5:
            level = f"[{level}] "
        else:
            level = f"[{level}]"
        msgs = []
        for i in messages:
            i = str(i)
            for j in i.split("\n"):
                msgs.append(j)
        for msg in msgs:
            print(f"{format}[{self.name}] [{time.strftime('%Y-%m-%d %H:%M:%S')}] {level} {msg}\033[0m")
    
    def info(self, *message) -> None:
        self._log("INFO", message)

    def warning(self, *message) -> None:
        self._log("WARN", message, "\033[93m")

    def error(self, *message) -> None:
        self._log("ERROR", message, "\033[91m")

    def debug(self, *message) -> None:
        self._log("DEBUG", message, "\033[2m")
    
    def format_exc(self) -> None:
        self.error(traceback.format_exc())
